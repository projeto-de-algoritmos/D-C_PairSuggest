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

    for i, person1 in enumerate(persons_list):
        found_pair = False 

        for j, person2 in enumerate(persons_list):
            if i < j and not found_pair:  
                if are_similar_taste(person1, person2, threshold):
                    similar_pairs.append((person1['name'], person2['name']))
                    found_pair = True  

    return similar_pairs

persons_list = [
    {'name': 'Alice', 'preferences': [1, 3, 5, 2, 4, 6]},
    {'name': 'Bob', 'preferences': [1, 2, 3, 4, 5, 6]},
    {'name': 'Charlie', 'preferences': [6, 5, 4, 3, 2, 1]},
]


threshold = 1200

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
        #Score 1
        score = input('score 1')
        new_person_scores.append(score)
        #Score 2
        score = input('score 2')
        new_person_scores.append(score)
        #Score 3
        score = input('score 3')
        new_person_scores.append(score)
        #Score 4
        score = input('score 4')
        new_person_scores.append(score)
        #Score 5
        score = input('score 5')
        new_person_scores.append(score)
        #Score 6
        score = input('score 6')
        new_person_scores.append(score)

        new_person_format = {'name': new_person,'preferences': new_person_scores}
        persons_list.append(new_person_format)
    elif option == '2':
        for person in persons_list:
            print(f"{person['name']}: {person['preferences']}")
    elif option == '3':
        print("wip")
    elif option == '4':
        persons_list_c = persons_list.copy()
        similar_pairs = find_similar_pairs(persons_list, threshold)

        print(f"Pairs of employees:")
        for pair in similar_pairs:
            print(f"{pair[0]} and {pair[1]}")
    elif option == '5':
        break