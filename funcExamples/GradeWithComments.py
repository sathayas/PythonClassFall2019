def Grade(testScore):
    '''
    Function Grade with comments.
    You can describe input parameters
    as well as the return variables associated
    with the function here.
    '''
    if testScore>=90:
        grade = 'A'
    elif testScore>=80:
        grade = 'B'
    elif testScore >=70:
        grade = 'C'
    elif testScore >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

yourGrade = Grade(55)
print('Your grade is ' + yourGrade)
