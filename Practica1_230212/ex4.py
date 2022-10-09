
print('Sequence: ')
sequence = input()


def run_length_encoding(seq):
    compressed = []
    count = 1
    char = seq[0]
    # se recorre la secuencia, si el elemento es igual al que estamos mirando, sumamos uno al contador y analizamos
    # al siguiente. Si no es igual, pasamos directamente al siguiente elemento de la secuencia y empezamos de nuevo con
    #el contador a 1.
    for i in range(1, len(seq)):
        if seq[i] == char:
            count = count + 1
        else:
            compressed.append([char, count])
            char = seq[i]
            count = 1
    compressed.append([char, count])
    return compressed


print(run_length_encoding(sequence))

