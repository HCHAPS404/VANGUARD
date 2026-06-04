# VANGUARD

Sistema multi-agente para procesamiento y validación de documentos.

## Estructura

```
agents/
  intake/     # Recepción e ingesta de documentos
  lexis/      # Análisis léxico y semántico
  sentinel/   # Detección de anomalías
  ledger/     # Registro y trazabilidad
  arbiter/    # Resolución de conflictos
  truthlock/  # Verificación de veracidad
  forge/      # Generación y transformación
  herald/     # Notificaciones y reportes
core/         # Lógica compartida
docs/
  prompts/    # Prompts de los agentes
  config/     # Configuraciones del sistema
tests/
  documents/  # Documentos de prueba
```

## Requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Configuración

```bash
# Crear entorno virtual
uv venv --python 3.12

# Activar entorno (Windows)
.venv\Scripts\activate

# Instalar dependencias
uv sync
```
