has_owner = ''

while has_owner != '예':
    my_money = int(input('현재 가지고 있는 자산을 입력하세요: '))
    if my_money <= 0 :
        print('통행료를 지불할 수 없군요.')
        break
    is_space = input('우주 정거장에 도착했나요? (예/아니오)')
    if is_space == '예':
        print('다시 처음으로 돌아갑니다.')
        continue
    has_owner = input('땅 주인이 있나요? (예/아니오)')
    if has_owner == '예':
        print('통행료를 지불하세요!')
    else:
        print('야호! 그냥 통과!!')
        print('주사위를 던져서 다음 땅으로 이동하세요.')
print('프로그램을 종료합니다.')





import numpy as np        
import pandas as pd        
import matplotlib          

data = np.random.rand(50)

seri = pd.Series(data)

seri.plot()

matplotlib.pyplot.show()





import random                    

print('>> 숫자 맞추기 게임 <<')    

choice = random.randrange(100)   

while True:                    
    user_choice = int(input('정수를 입력하세요: '))
    if choice == user_choice:
        break
    if choice < user_choice:
        print('너무 높아요!')
    else:
        print('너무 낮아요!')

print('정답입니다! 프로그램을 종료합니다.')
