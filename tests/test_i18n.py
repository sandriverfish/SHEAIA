"""Tests for i18n module."""

import pytest

from sheaia.i18n import Language, t, get_translations_for_language


class TestLanguage:
    """Tests for Language enum."""
    
    def test_from_string_english(self):
        assert Language.from_string("en") == Language.EN
        assert Language.from_string("en-US") == Language.EN
        assert Language.from_string("EN") == Language.EN
    
    def test_from_string_simplified_chinese(self):
        assert Language.from_string("zh-CN") == Language.ZH_CN
        assert Language.from_string("zh") == Language.ZH_CN
        assert Language.from_string("zh-Hans") == Language.ZH_CN
    
    def test_from_string_traditional_chinese(self):
        assert Language.from_string("zh-TW") == Language.ZH_TW
        assert Language.from_string("zh-Hant") == Language.ZH_TW
    
    def test_from_string_thai(self):
        assert Language.from_string("th") == Language.TH
        assert Language.from_string("th-TH") == Language.TH
    
    def test_from_string_fallback(self):
        assert Language.from_string("de") == Language.EN
        assert Language.from_string("unknown") == Language.EN


class TestTranslation:
    """Tests for translation function."""
    
    def test_translate_english(self):
        result = t("common.save", Language.EN)
        assert result == "Save"
    
    def test_translate_simplified_chinese(self):
        result = t("common.save", Language.ZH_CN)
        assert result == "保存"
    
    def test_translate_traditional_chinese(self):
        result = t("common.save", Language.ZH_TW)
        assert result == "儲存"
    
    def test_translate_thai(self):
        result = t("common.save", Language.TH)
        assert result == "บันทึก"
    
    def test_translate_with_interpolation(self):
        result = t("error.connection_failed", Language.EN, source="MySQL")
        assert "MySQL" in result
        assert "Failed to connect" in result
    
    def test_translate_missing_key(self):
        result = t("nonexistent.key", Language.EN)
        assert result == "nonexistent.key"
    
    def test_translate_fallback_to_english(self):
        # Even if a key only has English, it should work
        result = t("common.save", Language.EN)
        assert result == "Save"


class TestGetTranslations:
    """Tests for get_translations_for_language."""
    
    def test_get_all_translations(self):
        translations = get_translations_for_language(Language.EN)
        
        assert "common.save" in translations
        assert translations["common.save"] == "Save"
    
    def test_get_chinese_translations(self):
        translations = get_translations_for_language(Language.ZH_CN)
        
        assert translations["common.save"] == "保存"
        assert translations["chat.send"] == "发送"
