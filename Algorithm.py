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

def find_similar_tastes(person, persons_list, threshold):
    similar_tastes = []
    for other_person in persons_list:
        if person != other_person and are_similar_taste(person, other_person, threshold):
            similar_tastes.append(other_person)
    return similar_tastes

persons_list = [
    {'name': 'Alice', 'preferences': [1, 3, 5, 2, 4, 6]},
    {'name': 'Bob', 'preferences': [1, 2, 3, 4, 5, 6]},
    {'name': 'Charlie', 'preferences': [6, 5, 4, 3, 2, 1]},
]


threshold = 5

for person in persons_list:
    similar_tastes = find_similar_tastes(person, persons_list, threshold)
    print(f"{person['name']}'s similar tastes: {[p['name'] for p in similar_tastes]}")