def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)

    inversions = inv_left + inv_right + inv_split
    return merged, inversions


def merge(left, right):
    result = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, inversions


def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

def are_similar_taste(person1, person2, threshold):
    combined_preferences = person1['preferences'] + person2['preferences']
    inversions = count_inversions(combined_preferences)
    return inversions <= threshold

def find_similar_pairs(persons_list, threshold):
    similar_pairs = []
    unpaired_indices = list(range(len(persons_list)))

    for i, person1 in enumerate(persons_list):
        for j, person2 in enumerate(persons_list):
            if i < j:  
                if are_similar_taste(person1, person2, threshold):
                    similar_pairs.append((person1['name'], person2['name']))

                    if i in unpaired_indices:
                        unpaired_indices.remove(i)
                    if j in unpaired_indices:
                        unpaired_indices.remove(j)

    return similar_pairs, unpaired_indices

def delete_person(person_name, persons_list):
    for person in persons_list:
        if person['name'] == person_name:
            persons_list.remove(person)
            print(f"{person_name} removido.")
            return
    print(f"{person_name} não encontrado.")

def validate_score(message):
    while True:
        try:
            score = int(input(message))
            if 1 <= score <= 10:
                return score
            else:
                print("Valor deve estar entre 1 e 10.")
        except ValueError:
            print("Input inválido.")

persons_list = [
    {'name': 'Alice', 'preferences': [1, 3, 5, 2, 4, 6]},
    {'name': 'Bob', 'preferences': [1, 2, 3, 4, 5, 6]},
    {'name': 'Charlie', 'preferences': [6, 5, 4, 3, 2, 1]},
]


threshold = 20

while True:
    print('######Temporary Menu#######')
    print('Selecione uma opção')
    print('1.- Inserir um trabalhador')
    print('2.- Mostrar trabalhadores')
    print('3.- Eliminar trabalhador')
    print('4.- Fazer pares')
    print('5.- Sair')

    option = input()
    
    if option == '1':
        new_person = input('Insere nome de trabalhador')
        new_person_scores = []
        
        print("Insira o gosto que o empregado tem pelos seguintes temas (1 a 10):")
        
        score = validate_score("Esporte: ")
        new_person_scores.append(score)
        
        score = validate_score("Cinema")
        new_person_scores.append(score)
        
        score = validate_score("Cozinha")
        new_person_scores.append(score)
        
        score = validate_score("Leitura")
        new_person_scores.append(score)
        
        score = validate_score("Jogos")
        new_person_scores.append(score)
        
        score = validate_score("Música")
        new_person_scores.append(score)

        new_person_format = {'name': new_person, 'preferences': new_person_scores}
        persons_list.append(new_person_format)
    elif option == '2':
        for person in persons_list:
            print(f"{person['name']}: {person['preferences']}")
    elif option == '3':
        person_to_delete = input("Insira o nome do trabalhador a remover: ")
        delete_person(person_to_delete, persons_list)
    elif option == '4':
        similar_pairs, unpaired_indices = find_similar_pairs(persons_list, threshold)

        print("Duplas de empregados:")
        for pair in similar_pairs:
            print(f"{pair[0]} e {pair[1]}")

        if len(unpaired_indices) > 0:
            print("Empregados sem dupla:")
            for idx in unpaired_indices:
                print(f"{persons_list[idx]['name']} não conseguiu obter dupla.")
    elif option == '5':
        break