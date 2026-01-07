"""
SHEAIA - AI-Powered Enterprise Insights Platform

"Talk to your enterprise data" - Natural language access to CRM, ERP, MES, and documents
"""

__version__ = "0.1.0"
__author__ = "SHEAIA Team"

from sheaia.config.settings import Settings, get_settings

__all__ = ["Settings", "get_settings", "__version__"]
