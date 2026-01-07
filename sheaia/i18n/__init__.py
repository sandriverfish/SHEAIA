"""Internationalization module for SHEAIA."""

from enum import Enum
from typing import Dict


class Language(str, Enum):
    """Supported languages."""
    
    EN = "en"
    ZH_CN = "zh-CN"
    ZH_TW = "zh-TW"
    TH = "th"
    
    @classmethod
    def from_string(cls, value: str) -> "Language":
        """Parse language from string, with fallback to English."""
        value = value.lower().strip()
        
        # Handle various formats
        if value.startswith("zh-tw") or value.startswith("zh-hant"):
            return cls.ZH_TW
        elif value.startswith("zh"):
            return cls.ZH_CN
        elif value.startswith("th"):
            return cls.TH
        elif value.startswith("en"):
            return cls.EN
        
        # Try exact match
        for lang in cls:
            if lang.value.lower() == value:
                return lang
        
        return cls.EN  # Default fallback


# Translation dictionary
TRANSLATIONS: Dict[str, Dict[Language, str]] = {
    # Common
    "common.save": {
        Language.EN: "Save",
        Language.ZH_CN: "保存",
        Language.ZH_TW: "儲存",
        Language.TH: "บันทึก",
    },
    "common.cancel": {
        Language.EN: "Cancel",
        Language.ZH_CN: "取消",
        Language.ZH_TW: "取消",
        Language.TH: "ยกเลิก",
    },
    "common.delete": {
        Language.EN: "Delete",
        Language.ZH_CN: "删除",
        Language.ZH_TW: "刪除",
        Language.TH: "ลบ",
    },
    "common.search": {
        Language.EN: "Search",
        Language.ZH_CN: "搜索",
        Language.ZH_TW: "搜尋",
        Language.TH: "ค้นหา",
    },
    "common.loading": {
        Language.EN: "Loading...",
        Language.ZH_CN: "加载中...",
        Language.ZH_TW: "載入中...",
        Language.TH: "กำลังโหลด...",
    },
    "common.success": {
        Language.EN: "Success",
        Language.ZH_CN: "成功",
        Language.ZH_TW: "成功",
        Language.TH: "สำเร็จ",
    },
    "common.error": {
        Language.EN: "Error",
        Language.ZH_CN: "错误",
        Language.ZH_TW: "錯誤",
        Language.TH: "ข้อผิดพลาด",
    },
    
    # Errors
    "error.connection_failed": {
        Language.EN: "Failed to connect to {source}. Please check your credentials.",
        Language.ZH_CN: "无法连接到 {source}。请检查您的凭据。",
        Language.ZH_TW: "無法連接到 {source}。請檢查您的憑據。",
        Language.TH: "ไม่สามารถเชื่อมต่อกับ {source} ได้ กรุณาตรวจสอบข้อมูลรับรองของคุณ",
    },
    "error.query_failed": {
        Language.EN: "Query execution failed: {reason}",
        Language.ZH_CN: "查询执行失败：{reason}",
        Language.ZH_TW: "查詢執行失敗：{reason}",
        Language.TH: "การดำเนินการค้นหาล้มเหลว: {reason}",
    },
    "error.not_found": {
        Language.EN: "The requested resource was not found.",
        Language.ZH_CN: "未找到请求的资源。",
        Language.ZH_TW: "找不到請求的資源。",
        Language.TH: "ไม่พบทรัพยากรที่ร้องขอ",
    },
    "error.unauthorized": {
        Language.EN: "You are not authorized to perform this action.",
        Language.ZH_CN: "您无权执行此操作。",
        Language.ZH_TW: "您沒有權限執行此操作。",
        Language.TH: "คุณไม่ได้รับอนุญาตให้ดำเนินการนี้",
    },
    
    # Agent messages
    "agent.thinking": {
        Language.EN: "Analyzing your question...",
        Language.ZH_CN: "正在分析您的问题...",
        Language.ZH_TW: "正在分析您的問題...",
        Language.TH: "กำลังวิเคราะห์คำถามของคุณ...",
    },
    "agent.searching": {
        Language.EN: "Searching across {count} data sources...",
        Language.ZH_CN: "正在搜索 {count} 个数据源...",
        Language.ZH_TW: "正在搜尋 {count} 個資料來源...",
        Language.TH: "กำลังค้นหาจาก {count} แหล่งข้อมูล...",
    },
    "agent.generating_sql": {
        Language.EN: "Generating SQL query...",
        Language.ZH_CN: "正在生成SQL查询...",
        Language.ZH_TW: "正在產生SQL查詢...",
        Language.TH: "กำลังสร้างคำสั่ง SQL...",
    },
    "agent.executing_query": {
        Language.EN: "Executing query...",
        Language.ZH_CN: "正在执行查询...",
        Language.ZH_TW: "正在執行查詢...",
        Language.TH: "กำลังดำเนินการค้นหา...",
    },
    "agent.synthesizing": {
        Language.EN: "Synthesizing results...",
        Language.ZH_CN: "正在综合结果...",
        Language.ZH_TW: "正在綜合結果...",
        Language.TH: "กำลังสรุปผลลัพธ์...",
    },
    
    # Chat
    "chat.placeholder": {
        Language.EN: "Ask a question about your data...",
        Language.ZH_CN: "询问关于您数据的问题...",
        Language.ZH_TW: "詢問關於您資料的問題...",
        Language.TH: "ถามคำถามเกี่ยวกับข้อมูลของคุณ...",
    },
    "chat.send": {
        Language.EN: "Send",
        Language.ZH_CN: "发送",
        Language.ZH_TW: "傳送",
        Language.TH: "ส่ง",
    },
    "chat.sources": {
        Language.EN: "Sources",
        Language.ZH_CN: "数据来源",
        Language.ZH_TW: "資料來源",
        Language.TH: "แหล่งข้อมูล",
    },
    "chat.show_sql": {
        Language.EN: "Show SQL",
        Language.ZH_CN: "显示SQL",
        Language.ZH_TW: "顯示SQL",
        Language.TH: "แสดง SQL",
    },
    
    # Connectors
    "connector.connected": {
        Language.EN: "Connected",
        Language.ZH_CN: "已连接",
        Language.ZH_TW: "已連接",
        Language.TH: "เชื่อมต่อแล้ว",
    },
    "connector.disconnected": {
        Language.EN: "Disconnected",
        Language.ZH_CN: "已断开",
        Language.ZH_TW: "已斷開",
        Language.TH: "ยกเลิกการเชื่อมต่อ",
    },
    "connector.syncing": {
        Language.EN: "Syncing...",
        Language.ZH_CN: "同步中...",
        Language.ZH_TW: "同步中...",
        Language.TH: "กำลังซิงค์...",
    },
    "connector.last_sync": {
        Language.EN: "Last synced: {time}",
        Language.ZH_CN: "上次同步：{time}",
        Language.ZH_TW: "上次同步：{time}",
        Language.TH: "ซิงค์ล่าสุด: {time}",
    },
    
    # Reports
    "report.generated": {
        Language.EN: "Report generated successfully",
        Language.ZH_CN: "报告生成成功",
        Language.ZH_TW: "報告產生成功",
        Language.TH: "สร้างรายงานสำเร็จ",
    },
    "report.executive_summary": {
        Language.EN: "Executive Summary",
        Language.ZH_CN: "执行摘要",
        Language.ZH_TW: "執行摘要",
        Language.TH: "สรุปผู้บริหาร",
    },
    "report.key_findings": {
        Language.EN: "Key Findings",
        Language.ZH_CN: "主要发现",
        Language.ZH_TW: "主要發現",
        Language.TH: "ข้อค้นพบสำคัญ",
    },
    "report.recommendations": {
        Language.EN: "Recommendations",
        Language.ZH_CN: "建议",
        Language.ZH_TW: "建議",
        Language.TH: "ข้อเสนอแนะ",
    },
}


def t(key: str, lang: Language = Language.EN, **kwargs: str) -> str:
    """
    Translate a key to the specified language with interpolation.
    
    Args:
        key: Translation key (e.g., "error.connection_failed")
        lang: Target language
        **kwargs: Interpolation values
    
    Returns:
        Translated string, or key if not found
    
    Example:
        >>> t("error.connection_failed", Language.ZH_CN, source="MySQL")
        "无法连接到 MySQL。请检查您的凭据。"
    """
    translations = TRANSLATIONS.get(key, {})
    template = translations.get(lang)
    
    # Fallback to English
    if not template:
        template = translations.get(Language.EN, key)
    
    # Apply interpolation
    if kwargs:
        try:
            return template.format(**kwargs)
        except KeyError:
            return template
    
    return template


def get_translations_for_language(lang: Language) -> Dict[str, str]:
    """Get all translations for a specific language (for frontend export)."""
    result = {}
    for key, translations in TRANSLATIONS.items():
        result[key] = translations.get(lang, translations.get(Language.EN, key))
    return result


__all__ = ["Language", "t", "get_translations_for_language", "TRANSLATIONS"]
