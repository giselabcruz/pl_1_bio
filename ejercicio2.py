from Bio import SeqIO
from pathlib import Path

protein_dir = Path("proteins")

proteins = {
    "Oxitocina": protein_dir / "oxytocin.fasta",
    "Colágeno": protein_dir / "collagen.fasta",
    "Queratina": protein_dir / "keratin.fasta"
}

print("Se han tomado como proteínas las siguientes:")
print("- Oxitocina: hormona relacionada con el afecto, el parto y la lactancia.")
print("- Colágeno: proteína estructural que da soporte y resistencia a tejidos.")
print("- Queratina: proteína fibrosa que forma parte del cabello, uñas y piel.\n")

for name, filepath in proteins.items():
    record = SeqIO.read(filepath, "fasta")
    print(f"> {name}")
    print(record.seq)
    print()