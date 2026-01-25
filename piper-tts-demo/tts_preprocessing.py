"""
TTS Preprocessing Demo - Simplified Version
Showcases: tables, citations, sections, abbreviations, markdown cleanup
"""

import re
import unicodedata
from typing import Tuple, Optional


# ═══════════════════════════════════════════════════════════════════════════
# CITATION PROCESSOR - Keep Introductory, Remove Standalone
# ═══════════════════════════════════════════════════════════════════════════

class CitationProcessor:
    """
    Smart citation handling:
    - Remove standalone: (Doc-1, Web-3) 
    - Keep introductory: "as explained in (Web-1)" → "as explained in web article one"
    """

    NUMBER_WORDS = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    }

    SOURCE_LABELS = {
        'Doc': 'document',
        'Web': 'web article',
        'Arxiv': 'arxiv paper',
    }

    def format_citation(self, cite_str: str) -> str:
        """Doc-5 → document five"""
        match = re.match(r'(Doc|Web|Arxiv)-(\d+)', cite_str.strip())
        if not match:
            return cite_str

        cite_type = match.group(1)
        cite_id = int(match.group(2))
        
        label = self.SOURCE_LABELS.get(cite_type, cite_type.lower())
        num_word = self.NUMBER_WORDS.get(cite_id, str(cite_id))
        
        return f"{label} {num_word}"

    def process_text(self, text: str) -> str:
        """Main processor"""
        
        # Handle introductory citations
        intro_pattern = r'(as\s+(?:explained|stated|noted)\s+in|according\s+to)\s+\(([^)]+)\)'
        
        def replace_intro(match):
            intro = match.group(1)
            citations = [c.strip() for c in match.group(2).split(',')]
            formatted = [self.format_citation(c) for c in citations]
            
            if len(formatted) == 1:
                return f"{intro} {formatted[0]}"
            elif len(formatted) == 2:
                return f"{intro} {formatted[0]} and {formatted[1]}"
            else:
                return f"{intro} {', '.join(formatted[:-1])}, and {formatted[-1]}"
        
        text = re.sub(intro_pattern, replace_intro, text, flags=re.IGNORECASE)
        
        # Remove standalone citations
        text = re.sub(r'\s*\((?:Doc|Web|Arxiv)-\d+(?:,\s*(?:Doc|Web|Arxiv)-\d+)*\)', '', text)
        
        return text


# ═══════════════════════════════════════════════════════════════════════════
# TABLE LINEARIZATION
# ═══════════════════════════════════════════════════════════════════════════

def linearize_tables(text: str) -> str:
    """Convert markdown tables to spoken format"""
    
    table_pattern = r'^\|.+\|[ \t]*\n\|[\s\-:|]+\|[ \t]*\n(\|.+\|[ \t]*\n?)+'
    
    def convert_table(match):
        table_text = match.group(0).strip()
        lines = [line.strip() for line in table_text.split('\n') if line.strip()]
        
        if len(lines) < 3:
            return table_text
        
        # Parse header
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        
        # Process data rows (skip separator row)
        spoken_rows = []
        for row_line in lines[2:]:
            cells = [c.strip() for c in row_line.split('|')[1:-1]]
            
            if len(cells) != len(headers):
                continue
            
            row_parts = []
            for header, cell in zip(headers, cells):
                if cell:
                    # Clean markdown formatting
                    cell = re.sub(r'\*\*(.+?)\*\*', r'\1', cell)
                    cell = re.sub(r'\*(.+?)\*', r'\1', cell)
                    row_parts.append(f"{header}: {cell}.")
            
            if row_parts:
                spoken_rows.append('\n'.join(row_parts))
        
        if spoken_rows:
            return '\n\n' + '\n\n'.join(spoken_rows) + '\n\n'
        return table_text
    
    return re.sub(table_pattern, convert_table, text, flags=re.MULTILINE)


# ═══════════════════════════════════════════════════════════════════════════
# UNICODE NORMALIZATION
# ═══════════════════════════════════════════════════════════════════════════

def normalize_unicode(text: str) -> str:
    """Normalize Unicode to ASCII-compatible form"""
    if not text:
        return ""
    
    text = unicodedata.normalize('NFKC', text)
    
    replacements = {
        '\u2013': '-', '\u2014': '-',  # Dashes
        '\u2018': "'", '\u2019': "'",  # Single quotes
        '\u201C': '"', '\u201D': '"',  # Double quotes
        '\u2026': '...',               # Ellipsis
        '\u00A0': ' ',                 # Non-breaking space
    }
    
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    
    return text


# ═══════════════════════════════════════════════════════════════════════════
# MAIN PREPROCESSING PIPELINE
# ═══════════════════════════════════════════════════════════════════════════

def preprocess_markdown_for_tts(text: str) -> str:
    """
    Clean TTS preprocessing pipeline
    
    Features:
    - Table linearization
    - Smart citation handling  
    - Section formatting
    - Abbreviation expansion
    - Markdown cleanup
    - Pause insertion for natural speech
    """
    
    # Phase 1: Normalization
    text = normalize_unicode(text)
    text = linearize_tables(text)
    
    # Phase 2: Sections
    # Numbered sections: ## 1. Title → Section 1. Title
    text = re.sub(r'^#{1,6}\s*(\d+)\.\s*(.+?)$', r'\n\nSection \1. \2.\n\n', text, flags=re.MULTILINE)
    # Other sections: ## Title → Title
    text = re.sub(r'^#{1,6}\s*(.+?)$', r'\n\n\1.\n\n', text, flags=re.MULTILINE)
    
    # Phase 3: Abbreviations (common AI/tech terms)
    abbreviations = {
        r'\bAI\b': 'A.I.',
        r'\bML\b': 'M.L.',
        r'\bNLP\b': 'N.L.P.',
        r'\bRL\b': 'R.L.',
        r'\bAPI\b': 'A.P.I.',
        r'\bvs\.': 'versus',
        r'\be\.g\.,': 'for example,',
        r'\bi\.e\.,': 'that is,',
    }
    
    for pattern, replacement in abbreviations.items():
        text = re.sub(pattern, replacement, text)
    
    # Phase 4: Numbers and lists
    text = re.sub(r'(\d+)%', r'\1 percent', text)
    text = re.sub(r'^\s*[-*]\s+', '\n• ', text, flags=re.MULTILINE)
    text = re.sub(r'^(\d+)\.\s+', r'\nPoint \1. ', text, flags=re.MULTILINE)
    
    # Phase 5: Pause patterns for natural speech
    pause_patterns = {
        r'\b(However|Therefore|Furthermore|Moreover),\s*': r'\n\n\1, ',
        r'\b(First|Second|Third|Finally),\s*': r'\n\1, ',
        r'([.!?])\s+([A-Z])': r'\1\n\n\2',  # Sentence breaks
    }
    
    for pattern, replacement in pause_patterns.items():
        text = re.sub(pattern, replacement, text)
    
    # Phase 6: Citation processing
    citation_processor = CitationProcessor()
    text = citation_processor.process_text(text)
    
    # Phase 7: Markdown cleanup
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Italic
    text = re.sub(r'`([^`]+)`', r'\1', text)        # Code
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # Links
    
    # Phase 8: Cleanup
    text = re.sub(r'\n{3,}', '\n\n', text)          # Max 2 newlines
    text = re.sub(r'  +', ' ', text)                # Multiple spaces
    text = text.strip()
    
    return text