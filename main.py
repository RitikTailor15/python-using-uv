import json

students = [
    {"name": "Amit", "scores": [78, 85, 92]},
    {"name": "Priya", "scores": [55, 60, 45]},
    {"name": "Ritik", "scores": [88, 91, 95]},
    {"name": "Neha", "scores": [30, 40, 25]},
    {"name": "Karan", "scores": [70, 72, 68]},
]

def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg, strict = False):
    threshold = 0
    if strict:
        threshold = 5

    if avg >= (90 + threshold):
        return "A"
    elif avg >= (75 + threshold):
        return "B"
    elif avg >= (60 + threshold):
        return "C"
    elif avg >= (40 + threshold):
        return "D"
    else:
        return "F"

def main():

    for student in students:
        # Average score
        average_score = get_average(student['scores'])
        student['average'] = round(average_score, 1)

        # Grade
        grade = get_grade(student["average"], True)
        student['grade'] = grade

        # print formatted
        # print(f"{student["name"]} -> Avg. {student['average']} Grade: {student["grade"]}")

    sorted_student = sorted(students, key= lambda student : student['average'], reverse=True)
    # print(json.dumps(sorted_student, indent=4))
    topper = sorted_student[0]
    # print(f"{topper["name"]} : {topper["grade"]}")

    # Get all the student which are failed

    failed_student  = [student for student in students if student['grade'] == "F"]
    # print(failed_student)

    all_student_averages = [student['average'] for student in students]
    lowest_average = min(all_student_averages)
    highest_average = max(all_student_averages)
    class_average = round(sum(all_student_averages) / len(all_student_averages), 1)

    # print(f"Class Average : {class_average}, Lowest Average : {lowest_average}, Highest Average : {highest_average}")

    name_and_grade_dic = {student["name"] : student["grade"] for student in students}
    print(json.dumps(name_and_grade_dic, indent=4))

if __name__ == "__main__":
    main()