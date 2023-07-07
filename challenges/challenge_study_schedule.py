def study_schedule(permanence_period: list[tuple], target_time):
    if not isinstance(target_time, int):
        return None

    total_students = 0
    for tupla in permanence_period:
        if not all(isinstance(element, int) for element in tupla):
            return None
        if target_time in tupla:
            total_students += 1

    return total_students

# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
