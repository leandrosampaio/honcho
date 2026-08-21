"""
Shared constants for LLM prompts across Honcho components.
"""

import os

# Language instruction appended to all system prompts to ensure
# the LLM responds in the user's preferred language.
# Can be overridden via the LANGUAGE_INSTRUCTION environment variable.
_LANGUAGE_INSTRUCTION_DEFAULT = (
    "All responses, summaries, observations, and outputs must be written in "
    "Brazilian Portuguese (pt-BR). Use the Portuguese language for all content."
)

LANGUAGE_INSTRUCTION: str = os.environ.get(
    "LANGUAGE_INSTRUCTION", _LANGUAGE_INSTRUCTION_DEFAULT
)
