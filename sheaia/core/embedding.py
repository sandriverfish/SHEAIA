"""Embedding service for vector operations."""

import logging
from abc import ABC, abstractmethod
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)


class BaseEmbedding(ABC):
    """Abstract base class for embedding implementations."""
    
    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the embedding dimension."""
        ...
    
    @abstractmethod
    def embed_documents(self, texts: list[str]) -> np.ndarray:
        """Embed a list of documents."""
        ...
    
    @abstractmethod
    def embed_query(self, text: str) -> np.ndarray:
        """Embed a single query text."""
        ...


class SentenceTransformerEmbedding(BaseEmbedding):
    """Embedding using sentence-transformers."""
    
    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
        device: str = "auto",
        batch_size: int = 32,
    ):
        self.model_name = model_name
        self.device = device
        self.batch_size = batch_size
        self._model = None
        self._dimension: Optional[int] = None
    
    def _load_model(self):
        """Lazy load the model."""
        if self._model is not None:
            return
        
        try:
            from sentence_transformers import SentenceTransformer
            
            logger.info(f"Loading embedding model: {self.model_name}")
            
            device = self.device
            if device == "auto":
                import torch
                device = "cuda" if torch.cuda.is_available() else "cpu"
            
            self._model = SentenceTransformer(
                self.model_name,
                device=device,
            )
            self._dimension = self._model.get_sentence_embedding_dimension()
            logger.info(f"Embedding model loaded. Dimension: {self._dimension}")
            
        except ImportError:
            raise ImportError(
                "sentence-transformers is required. Install with: "
                "pip install sentence-transformers"
            )
    
    @property
    def dimension(self) -> int:
        """Return the embedding dimension."""
        if self._dimension is None:
            self._load_model()
        return self._dimension  # type: ignore
    
    def embed_documents(self, texts: list[str]) -> np.ndarray:
        """Embed a list of documents."""
        self._load_model()
        
        embeddings = self._model.encode(  # type: ignore
            texts,
            batch_size=self.batch_size,
            show_progress_bar=len(texts) > 100,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        
        return embeddings
    
    def embed_query(self, text: str) -> np.ndarray:
        """Embed a single query text."""
        self._load_model()
        
        embedding = self._model.encode(  # type: ignore
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        
        return embedding


# Global embedding instance (lazy loaded)
_embedding_instance: Optional[BaseEmbedding] = None


def get_embedding() -> BaseEmbedding:
    """Get the global embedding instance."""
    global _embedding_instance
    
    if _embedding_instance is None:
        from sheaia.config import get_settings
        
        settings = get_settings()
        _embedding_instance = SentenceTransformerEmbedding(
            model_name=settings.embedding.model_name,
            device=settings.embedding.device,
            batch_size=settings.embedding.batch_size,
        )
    
    return _embedding_instance


__all__ = [
    "BaseEmbedding",
    "SentenceTransformerEmbedding",
    "get_embedding",
]
