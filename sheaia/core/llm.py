"""LLM inference service."""

import logging
from abc import ABC, abstractmethod
from typing import AsyncIterator, Optional

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class GenerationConfig(BaseModel):
    """Configuration for text generation."""
    
    max_tokens: int = 2048
    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 40
    repeat_penalty: float = 1.1
    stop: list[str] = []


class LLMResponse(BaseModel):
    """Response from LLM generation."""
    
    text: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    model: str = ""


class BaseLLM(ABC):
    """Abstract base class for LLM implementations."""
    
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        config: Optional[GenerationConfig] = None,
    ) -> LLMResponse:
        """Generate text from prompt."""
        ...
    
    @abstractmethod
    async def stream(
        self,
        prompt: str,
        config: Optional[GenerationConfig] = None,
    ) -> AsyncIterator[str]:
        """Stream text generation token by token."""
        ...
    
    @abstractmethod
    def load_model(self) -> None:
        """Load the model into memory."""
        ...
    
    @abstractmethod
    def unload_model(self) -> None:
        """Unload the model from memory."""
        ...


class LlamaCppLLM(BaseLLM):
    """LLM implementation using llama.cpp."""
    
    def __init__(
        self,
        model_path: str,
        n_ctx: int = 16384,
        n_gpu_layers: int = -1,
        n_batch: int = 512,
    ):
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_gpu_layers = n_gpu_layers
        self.n_batch = n_batch
        self._model = None
    
    def load_model(self) -> None:
        """Load the model into memory."""
        if self._model is not None:
            return
        
        try:
            from llama_cpp import Llama
            
            logger.info(f"Loading model from {self.model_path}")
            self._model = Llama(
                model_path=self.model_path,
                n_ctx=self.n_ctx,
                n_gpu_layers=self.n_gpu_layers,
                n_batch=self.n_batch,
                verbose=False,
            )
            logger.info("Model loaded successfully")
        except ImportError:
            raise ImportError(
                "llama-cpp-python is required. Install with: "
                "pip install llama-cpp-python"
            )
    
    def unload_model(self) -> None:
        """Unload the model from memory."""
        if self._model is not None:
            del self._model
            self._model = None
            logger.info("Model unloaded")
    
    async def generate(
        self,
        prompt: str,
        config: Optional[GenerationConfig] = None,
    ) -> LLMResponse:
        """Generate text from prompt."""
        if self._model is None:
            self.load_model()
        
        config = config or GenerationConfig()
        
        response = self._model(
            prompt,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            top_p=config.top_p,
            top_k=config.top_k,
            repeat_penalty=config.repeat_penalty,
            stop=config.stop or None,
        )
        
        return LLMResponse(
            text=response["choices"][0]["text"],
            prompt_tokens=response["usage"]["prompt_tokens"],
            completion_tokens=response["usage"]["completion_tokens"],
            total_tokens=response["usage"]["total_tokens"],
            model=self.model_path,
        )
    
    async def stream(
        self,
        prompt: str,
        config: Optional[GenerationConfig] = None,
    ) -> AsyncIterator[str]:
        """Stream text generation token by token."""
        if self._model is None:
            self.load_model()
        
        config = config or GenerationConfig()
        
        stream = self._model(
            prompt,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            top_p=config.top_p,
            top_k=config.top_k,
            repeat_penalty=config.repeat_penalty,
            stop=config.stop or None,
            stream=True,
        )
        
        for chunk in stream:
            text = chunk["choices"][0]["text"]
            if text:
                yield text


# Global LLM instance (lazy loaded)
_llm_instance: Optional[BaseLLM] = None


def get_llm() -> BaseLLM:
    """Get the global LLM instance."""
    global _llm_instance
    
    if _llm_instance is None:
        from sheaia.config import get_settings
        
        settings = get_settings()
        _llm_instance = LlamaCppLLM(
            model_path=settings.llm.model_path,
            n_ctx=settings.llm.n_ctx,
            n_gpu_layers=settings.llm.n_gpu_layers,
            n_batch=settings.llm.n_batch,
        )
    
    return _llm_instance


__all__ = [
    "GenerationConfig",
    "LLMResponse",
    "BaseLLM",
    "LlamaCppLLM",
    "get_llm",
]
