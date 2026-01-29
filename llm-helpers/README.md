# Reasoning Capability Detection & Caching

A smart, production-ready utility for detecting whether Large Language Models (LLMs) support reasoning mode capabilities with intelligent caching to minimize redundant probes.

## Purpose

When working with LLMs through frameworks like LangChain and Ollama, not all models support advanced reasoning modes. This probe utility:

- **Automatically detects** whether a model supports reasoning mode
- **Caches results** to avoid repeated, expensive probe operations
- **Provides fast-path detection** for known reasoning models
- **Persists cache to disk** with TTL expiration for long-term efficiency

## Key Features

### 🚀 Intelligent Caching
- **Memory cache**: In-memory storage for instant lookups within the same session
- **Persistent disk cache**: JSON-based storage survives across program restarts
- **TTL expiration**: 480-hour (20-day) cache validity prevents stale data
- **Automatic invalidation**: Expired entries are re-probed transparently

### ⚡ Performance Optimization
- **Fast-path pattern matching**: Known reasoning models (deepseek-r1, qwen-qwq, o1, etc.) are identified instantly without probing
- **Minimal probe overhead**: Uses only 512 tokens for actual model testing
- **Cache keying**: Unique keys per model/temperature/context combination

### 🛡️ Production Ready
- **Comprehensive error handling**: Graceful fallbacks for probe failures
- **Detailed diagnostics**: Optional progress logging for debugging
- **Cache management**: Tools to clear cache, view statistics, and inspect entries
- **Type safety**: Clear return types and parameter validation

## How It Works

### Detection Flow

```
┌─────────────────────────────────────┐
│  check_reasoning_support(model)     │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Memory Cache?│────Yes────► Return cached result
        └──────┬───────┘
               │ No
               ▼
        ┌──────────────┐
        │ Disk Cache?  │────Yes────► Load & return
        └──────┬───────┘
               │ No
               ▼
        ┌──────────────────┐
        │ Known Pattern?   │────Yes────► Return True (fast path)
        └──────┬───────────┘
               │ No
               ▼
        ┌──────────────────┐
        │ Probe Model      │
        │ (reasoning=True) │
        └──────┬───────────┘
               │
               ▼
        ┌──────────────────┐
        │ Cache Result     │
        │ (Memory + Disk)  │
        └──────────────────┘
```

### Probe Strategy

1. **Pattern Matching**: Checks model name against known reasoning models
2. **Live Testing**: Attempts to initialize the model with `reasoning=True`
3. **Response Validation**: Sends a test prompt and validates the response
4. **Error Analysis**: Examines exceptions to determine if reasoning mode is unsupported

## Usage

### Basic Usage

```python
from reasoning_probe import ReasoningCapabilityProbe

# Initialize the probe
probe = ReasoningCapabilityProbe(show_progress=True)

# Check if a model supports reasoning
supports_reasoning, reason = probe.check_reasoning_support(
    model="gpt-oss:20b",
    temperature=0.0,
    context_window=512
)

print(f"Reasoning supported: {supports_reasoning}")
print(f"Reason: {reason}")
```

### Configuration Options

```python
# Disable progress logging
probe = ReasoningCapabilityProbe(show_progress=False)

# Disable persistent disk caching
probe = ReasoningCapabilityProbe(use_persistent_cache=False)

# Both options
probe = ReasoningCapabilityProbe(
    show_progress=False,
    use_persistent_cache=False
)
```

### Cache Management

```python
# View cache statistics
stats = probe.get_cache_stats()
print(f"Total cached models: {stats['total_entries']}")
print(f"Valid entries: {stats['valid_entries']}")
print(f"Supported models: {stats['supported_models']}")

# Clear cache for a specific model
probe.clear_cache(model="gpt-oss:20b")

# Clear entire cache
probe.clear_cache()
```

## Cache Structure

The cache is stored in `.cache/reasoning_capabilities.json`:

```json
{
  "timestamp": "2026-01-29T10:30:00.123456",
  "ttl_hours": 480,
  "capabilities": {
    "gpt-oss:20b#0#512": {
      "model": "gpt-oss:20b",
      "temperature": 0,
      "context_window": 512,
      "supports_reasoning": true,
      "reason": "Reasoning mode test passed",
      "timestamp": "2026-01-29T10:30:00.123456"
    }
  }
}
```

## Known Reasoning Models

The probe recognizes these patterns as reasoning-capable models (fast path):

- `deepseek-r1`
- `qwen-qwq`
- `qwen-r`
- `o1`
- `reasoning`
- `r1-preview`

Models matching these patterns skip the probe and immediately return `True`.

## Output Examples

### First Run (Probe Required)
```
🔍︎ Probing reasoning capability: gpt-oss:20b
  Temperature: 0
  Context window: 512
  ✓ SUPPORTED: Reasoning mode test passed
💾 Saved capability cache: .cache/reasoning_capabilities.json
```

### Subsequent Runs (Cached)
```
✓ Loaded capability cache: 1 models
  Cache file: .cache\reasoning_capabilities.json
📦 Reasoning capability [CACHED]: gpt-oss:20b
  Result: True
  Reason: Reasoning mode test passed
```

## Benefits

1. **Avoid Runtime Errors**: Detect unsupported parameters before attempting to use them
2. **Improve Performance**: Cache results eliminate repeated probe overhead (can save seconds per invocation)
3. **Better UX**: Inform users whether reasoning mode is available for their chosen model
4. **Conditional Logic**: Branch code paths based on reasoning capability
5. **Model Discovery**: Quickly test multiple models to find reasoning-capable ones

## Requirements

- `langchain-core`
- `langchain-ollama`
- Python 3.7+

## Integration Example

```python
from reasoning_probe import ReasoningCapabilityProbe
from langchain_ollama import ChatOllama

probe = ReasoningCapabilityProbe()
supports_reasoning, _ = probe.check_reasoning_support(
    model="gpt-oss:20b",
    temperature=0.0,
    context_window=4096
)

# Conditionally enable reasoning mode
llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0.0,
    num_ctx=4096,
    reasoning=supports_reasoning  # Only enable if supported
)
```

## License

This utility is designed as a practical tool for LLM development workflows. Feel free to adapt and extend for your needs.
