#CTI-110
#P4HW1 - Score List
#Kyle Blanchard
#06/27/2022
#Adjusting P2HW2 to ask a user for the number of grade they will enter, that number of grades, then display the lowest score, a list of the grades with the lowest score excluded, an average of that list, and the letter grade

letter_grade = {
    'A':90,
    'B':80,
    'C':70,
    'D':60
}
grade_list = []
list_size = int(input("How many scores do you want to enter? "))
lowest_score = 101.0
average = 0
letter = ''
for i in range(list_size):
    score = float(input(f"Enter score #{i+1}: "))
    while score < 0 or score > 100:
        print(f"\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))
    grade_list.append(score)
    if score < lowest_score:
        lowest_score = score
grade_list.pop(grade_list.index(lowest_score))
for grade in grade_list:
    average+=grade
average/=len(grade_list)
for key in letter_grade:
    if average >= letter_grade[key]:
        letter = key
        break
    else:
        letter = 'F'
print("\n\n-----------------------Results-----------------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {grade_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {letter}")
print("-----------------------------------------------------")
