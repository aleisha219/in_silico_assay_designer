from Bio.SeqUtils import GC
import primer3.bindings

def analyze_sequence(seq: str) -> dict:
    return {
        'gc_content': GC(seq),
        'tm': primer3.bindings.calcTm(seq)
    }
