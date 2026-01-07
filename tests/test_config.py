"""Tests for configuration module."""

import pytest

from sheaia.config import Settings, get_settings


def test_default_settings():
    """Test that default settings load correctly."""
    settings = Settings()
    
    assert settings.app_name == "SHEAIA"
    assert settings.environment == "development"
    assert settings.debug is False


def test_settings_llm_defaults():
    """Test LLM settings defaults."""
    settings = Settings()
    
    assert settings.llm.n_ctx == 16384
    assert settings.llm.n_gpu_layers == -1
    assert settings.llm.n_batch == 512


def test_settings_i18n_defaults():
    """Test i18n settings defaults."""
    settings = Settings()
    
    assert settings.i18n.default_language == "en"
    assert "en" in settings.i18n.supported_languages
    assert "zh-CN" in settings.i18n.supported_languages
    assert "zh-TW" in settings.i18n.supported_languages
    assert "th" in settings.i18n.supported_languages
