# SHEAIA

> **AI-Powered Enterprise Insights Platform**
> 
> "Talk to your enterprise data" - Natural language access to CRM, ERP, MES, and documents

![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

SHEAIA is an on-premise AI appliance that provides enterprise customers with natural language access to their business data. Built on LangGraph multi-agent architecture and self-hosted LLMs, it connects to enterprise systems (CRM, ERP, MES), documents, and databases to deliver unified insights through a conversational interface.

### Key Features

- 🔒 **100% Local & Secure** - All data stays on-premise, air-gapped capable
- 💬 **AI-Native Data Access** - Ask questions in natural language, get answers with citations
- 🔗 **Cross-System Intelligence** - Correlate data across CRM, ERP, MES seamlessly
- 🧠 **Self-Learning** - AI agents continuously discover and index data sources
- 🌐 **Multilingual** - English, Simplified Chinese, Traditional Chinese, Thai

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  UI Layer: Web App | WeChat | Feishu | API                      │
├─────────────────────────────────────────────────────────────────┤
│  Agent Layer: Coordinator | Query | Document | Connector        │
├─────────────────────────────────────────────────────────────────┤
│  Model Layer: Qwen2.5 (LLM) | bge-m3 (Embeddings) | Milvus     │
├─────────────────────────────────────────────────────────────────┤
│  Data Layer: ClickHouse | Schema Graph | Credential Vault       │
├─────────────────────────────────────────────────────────────────┤
│  Connector Layer: CRM | ERP | MES | Files | ODBC | REST API     │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.11+
- NVIDIA GPU with CUDA 12.x (development) or AMD GPU with ROCm (production)
- 64GB+ RAM recommended

### Installation

```bash
# Clone the repository
git clone https://github.com/unergybot/SHEAIA.git
cd sheaia

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -e ".[dev]"

# Copy and configure settings
cp config/settings.example.yaml config/settings.yaml
# Edit config/settings.yaml with your settings

# Download models (or use your own)
python -m sheaia.cli download-models

# Start the server
python -m sheaia.cli serve
```

### Docker (Recommended)

```bash
# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up -d
```

## Project Structure

```
sheaia/
├── sheaia/                 # Main Python package
│   ├── agents/             # LangGraph agents
│   ├── api/                # FastAPI routes
│   ├── bots/               # Messaging bots
│   ├── config/             # Configuration
│   ├── connectors/         # Data connectors
│   ├── core/               # Core services
│   ├── i18n/               # Internationalization
│   └── knowledge/          # Knowledge base
├── frontend/               # React web app
├── models/                 # LLM & embedding models
├── tests/                  # Test suite
├── docs/                   # Documentation
└── config/                 # Configuration files
```

## Documentation

- [Platform Design](docs/plans/2026-01-07-sheaia-platform-design.md)
- [API Reference](https://github.com/unergybot/SHEAIA/tree/main/docs/api)
- [User Guide](https://github.com/unergybot/SHEAIA/tree/main/docs/user-guide)
- [Admin Guide](https://github.com/unergybot/SHEAIA/tree/main/docs/admin-guide)

## Development

```bash
# Run tests
pytest

# Code formatting
ruff format .

# Linting
ruff check .

# Type checking
mypy sheaia
```

## License

MIT License - see [LICENSE](LICENSE) for details.
