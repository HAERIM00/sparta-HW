#사용자의 점수를 입력받아 등급 출력 

def get_grade(score):
    if score >= 91:
        return ("A")
    elif score >= 81:
        return ("B")
    elif score >= 71:
        return ("c")
    elif score <= 70:
        return ("F")

score = int(input())
grade = get_grade(score)
print(grade) # A ~ F

