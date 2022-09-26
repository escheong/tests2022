import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    y = int(today.split('.')[0])
    m = int(today.split('.')[1])
    d = int(today.split('.')[2])
    now = datetime.date(y,m,d)
    
    term_dict = dict()
    for i in range(len(terms)):
        a, b = terms[i].split()
        term_dict[a] = int(b)

    for i in range(len(privacies)):
        a, b = privacies[i].split()
        yy = int(a.split('.')[0])
        mm = int(a.split('.')[1])
        dd = int(a.split('.')[2])
        expiry_date = datetime.date(yy,mm,dd) + relativedelta(months=term_dict[b])
        
        if now >= expiry_date:
            answer.append(i+1)    
       
    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])