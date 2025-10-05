from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

in_fasta = "dna_seqs.fasta"
out_fasta = "proteins.fasta"

protein_records = []

registros = SeqIO.parse(in_fasta, "fasta")

try:
    while True:
        registro_secuencia = next(registros)
        print(f"\nID: {registro_secuencia.id}")

        seq = registro_secuencia.seq.upper()
        total = len(seq)
        count_GC = seq.count("G") + seq.count("C")
        porcentaje_GC = (count_GC / total) * 100 if total > 0 else 0

        protein_seq = registro_secuencia.seq.translate(table=1, to_stop=True)

        print(f"Cadena de aminoácidos: {protein_seq}")
        print(f"Longitud: {total}")
        print(f"GC count: {count_GC}")
        print(f"GC%: {porcentaje_GC:.2f}")

        prot_record = SeqRecord(
            protein_seq,
            id=registro_secuencia.id,
            description=registro_secuencia.description
        )
        protein_records.append(prot_record)

except StopIteration:
    print("\nNo hay más secuencias en el fichero")

SeqIO.write(protein_records, out_fasta, "fasta")
print(f"\nSe escribieron {len(protein_records)} secuencias de proteínas en {out_fasta}")