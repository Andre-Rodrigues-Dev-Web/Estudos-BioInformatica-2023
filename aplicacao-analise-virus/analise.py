# Criação do arquivo virus_genome.fasta
with open("virus_genome.fasta", "w") as file:
    file.write(">virus_genome\n")
    file.write("AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT\n")


# Ler o arquivo FASTA
with open("virus_genome.fasta", "r") as file:
    genome = ""
    for line in file:
        if not line.startswith(">"):
            genome += line.strip()

# Calcular a frequência de cada base
base_count = {"A": 0, "C": 0, "G": 0, "T": 0}
for base in genome:
    base_count[base] += 1

# Imprimir a frequência de cada base
print("A:", base_count["A"] / len(genome))
print("C:", base_count["C"] / len(genome))
print("G:", base_count["G"] / len(genome))
print("T:", base_count["T"] / len(genome))

