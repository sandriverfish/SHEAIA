"""Chat API endpoints."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from sheaia.i18n import Language

logger = logging.getLogger(__name__)

router = APIRouter()


class ChatRequest(BaseModel):
    """Chat request model."""
    
    message: str = Field(..., description="User message", min_length=1, max_length=10000)
    conversation_id: Optional[str] = Field(None, description="Conversation ID for context")
    language: str = Field(default="en", description="Response language")
    
    model_config = {"extra": "forbid"}


class ChatResponse(BaseModel):
    """Chat response model."""
    
    response: str = Field(..., description="AI response")
    conversation_id: str = Field(..., description="Conversation ID")
    sources: list[dict] = Field(default=[], description="Data sources used")
    sql: Optional[str] = Field(None, description="Generated SQL if applicable")


class StreamingToken(BaseModel):
    """Streaming token model."""
    
    type: str = Field(..., description="Token type: token, done, error")
    content: str = Field(default="", description="Token content")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Send a chat message and receive a complete response.
    
    This endpoint is for synchronous chat - use the WebSocket endpoint
    for streaming responses.
    """
    try:
        lang = Language.from_string(request.language)
        
        # TODO: Implement actual agent-based chat
        # For now, return a placeholder response
        
        response_text = {
            Language.EN: f"I received your message: '{request.message}'. "
                        "The full agent system is being implemented.",
            Language.ZH_CN: f"我收到了您的消息：'{request.message}'。"
                           "完整的代理系统正在实现中。",
            Language.ZH_TW: f"我收到了您的訊息：'{request.message}'。"
                           "完整的代理系統正在實現中。",
            Language.TH: f"ฉันได้รับข้อความของคุณ: '{request.message}' "
                        "ระบบตัวแทนกำลังถูกพัฒนา",
        }.get(lang, f"I received your message: '{request.message}'")
        
        return ChatResponse(
            response=response_text,
            conversation_id=request.conversation_id or "new-conversation",
            sources=[],
            sql=None,
        )
        
    except Exception as e:
        logger.exception("Chat error")
        raise HTTPException(status_code=500, detail=str(e))


@router.websocket("/chat/stream")
async def chat_stream(websocket: WebSocket):
    """
    WebSocket endpoint for streaming chat responses.
    
    Client sends: {"message": "...", "conversation_id": "...", "language": "en"}
    Server sends: {"type": "token", "content": "..."} for each token
                  {"type": "done", "content": ""} when complete
                  {"type": "error", "content": "..."} on error
    """
    await websocket.accept()
    
    try:
        while True:
            # Receive message
            data = await websocket.receive_json()
            message = data.get("message", "")
            language = data.get("language", "en")
            
            if not message:
                await websocket.send_json({
                    "type": "error",
                    "content": "Message is required"
                })
                continue
            
            lang = Language.from_string(language)
            
            # TODO: Implement actual streaming with LLM
            # For now, send placeholder tokens
            
            thinking_msg = {
                Language.EN: "Processing your request",
                Language.ZH_CN: "正在处理您的请求",
                Language.ZH_TW: "正在處理您的請求",
                Language.TH: "กำลังประมวลผลคำขอของคุณ",
            }.get(lang, "Processing your request")
            
            # Simulate streaming
            for word in thinking_msg.split():
                await websocket.send_json({
                    "type": "token",
                    "content": word + " "
                })
            
            await websocket.send_json({
                "type": "done",
                "content": ""
            })
            
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        logger.exception("WebSocket error")
        try:
            await websocket.send_json({
                "type": "error",
                "content": str(e)
            })
        except Exception:
            pass
