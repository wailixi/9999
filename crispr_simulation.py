Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def generate_dna_sequence(length=100):
...     import random
...     bases = ['A', 'T', 'C', 'G']
...     return ''.join(random.choice(bases) for _ in range(length))
... 
... dna_sequence = generate_dna_sequence()
... print("DNA Sequence:", dna_sequence)
... def design_guide_rna(target_sequence, length=20):
...     return target_sequence[:length]
... 
... target = "AGCTTAGCTAAGCTTAGCTA"
... gRNA = design_guide_rna(target)
... print("Guide RNA:", gRNA)
... def find_target_sequence(dna_sequence, target_sequence):
...     return dna_sequence.find(target_sequence)
... 
... target_position = find_target_sequence(dna_sequence, target)
... print("Target Position:", target_position)
... def simulate_dna_cut(dna_sequence, target_position, gRNA_length):
...     cut_position = target_position + gRNA_length // 2
...     return dna_sequence[:cut_position] + "|" + dna_sequence[cut_position:]
... 
... cut_dna = simulate_dna_cut(dna_sequence, target_position, len(gRNA))
... print("Cut DNA Sequence:", cut_dna)
... def crispr_simulation(dna_sequence, target_sequence):
...     gRNA = design_guide_rna(target_sequence)
...     target_position = find_target_sequence(dna_sequence, target_sequence)
...     if target_position == -1:
...         return "Target sequence not found in DNA."
...     return simulate_dna_cut(dna_sequence, target_position, len(gRNA))
... dna_sequence = generate_dna_sequence()
... target_sequence = "AGCTTAGCTAAGCTTAGCTA"
... result = crispr_simulation(dna_sequence, target_sequence)
... print("CRISPR Simulation Result:", result)
