"""Configuration management for SHEAIA platform."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    """LLM inference settings."""
    
    model_path: str = Field(
        default="models/llm/qwen2.5-14b-instruct-q4_k_m.gguf",
        description="Path to the primary LLM model file"
    )
    reasoning_model_path: str = Field(
        default="models/llm/qwen2.5-32b-instruct-q4_k_m.gguf",
        description="Path to the reasoning LLM model file (optional larger model)"
    )
    n_ctx: int = Field(default=16384, description="Context window size")
    n_gpu_layers: int = Field(default=-1, description="Number of layers to offload to GPU (-1 for all)")
    n_batch: int = Field(default=512, description="Batch size for prompt processing")
    device: str = Field(default="auto", description="Device to use: auto, cuda:0, rocm:0, cpu")


class EmbeddingSettings(BaseSettings):
    """Embedding model settings."""
    
    model_name: str = Field(
        default="BAAI/bge-m3",
        description="Embedding model name or path"
    )
    device: str = Field(default="auto", description="Device: auto, cuda, npu, cpu")
    batch_size: int = Field(default=32, description="Batch size for embedding")


class DatabaseSettings(BaseSettings):
    """Database connection settings."""
    
    # ClickHouse
    clickhouse_host: str = Field(default="localhost", description="ClickHouse host")
    clickhouse_port: int = Field(default=9000, description="ClickHouse native port")
    clickhouse_database: str = Field(default="sheaia", description="ClickHouse database name")
    clickhouse_user: str = Field(default="default", description="ClickHouse user")
    clickhouse_password: str = Field(default="", description="ClickHouse password")
    
    # Milvus
    milvus_uri: str = Field(
        default="./data/milvus.db",
        description="Milvus connection URI (file path for Milvus Lite)"
    )
    milvus_collection: str = Field(default="sheaia_vectors", description="Milvus collection name")
    
    # SQLite (metadata, schema graph)
    sqlite_path: str = Field(default="./data/metadata.db", description="SQLite database path")


class APISettings(BaseSettings):
    """API server settings."""
    
    host: str = Field(default="0.0.0.0", description="API server host")
    port: int = Field(default=8000, description="API server port")
    reload: bool = Field(default=False, description="Enable auto-reload (development)")
    workers: int = Field(default=1, description="Number of worker processes")
    cors_origins: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:5173"],
        description="Allowed CORS origins"
    )


class SecuritySettings(BaseSettings):
    """Security settings."""
    
    secret_key: str = Field(
        default="CHANGE-THIS-SECRET-KEY-IN-PRODUCTION",
        description="Secret key for JWT signing"
    )
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(default=60, description="Access token expiration")
    vault_master_key: str = Field(
        default="",
        description="Master key for credential vault (leave empty to derive from secret_key)"
    )


class I18nSettings(BaseSettings):
    """Internationalization settings."""
    
    default_language: Literal["en", "zh-CN", "zh-TW", "th"] = Field(
        default="en",
        description="Default language"
    )
    supported_languages: list[str] = Field(
        default=["en", "zh-CN", "zh-TW", "th"],
        description="Supported languages"
    )


class Settings(BaseSettings):
    """Main application settings."""
    
    model_config = SettingsConfigDict(
        env_prefix="SHEAIA_",
        env_nested_delimiter="__",
        case_sensitive=False,
    )
    
    # Application
    app_name: str = Field(default="SHEAIA", description="Application name")
    environment: Literal["development", "staging", "production"] = Field(
        default="development",
        description="Environment"
    )
    debug: bool = Field(default=False, description="Enable debug mode")
    
    # Data directory
    data_dir: Path = Field(default=Path("./data"), description="Data directory path")
    models_dir: Path = Field(default=Path("./models"), description="Models directory path")
    
    # Nested settings
    llm: LLMSettings = Field(default_factory=LLMSettings)
    embedding: EmbeddingSettings = Field(default_factory=EmbeddingSettings)
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    api: APISettings = Field(default_factory=APISettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    i18n: I18nSettings = Field(default_factory=I18nSettings)
    
    @classmethod
    def from_yaml(cls, path: str | Path) -> "Settings":
        """Load settings from YAML file."""
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return cls(**config) if config else cls()


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    config_path = Path("config/settings.yaml")
    if config_path.exists():
        return Settings.from_yaml(config_path)
    return Settings()
