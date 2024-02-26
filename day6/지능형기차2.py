passenger = 0 # 현재 기차에 있는 사람 수는 0으로 두라함.
in_passenger = [] # 정거장당 사람 수를 리스트로 저장.

for i in range(1,11):
    out_passenger, in_passenger = list(map(int,input().split())) #내린사람 탄사람 비교
    passenger -= out_passenger + in_passenger #전체 승객에서 내린사람 탄사람을 더해주고 기차 인원에서 뺌 왜 냐면 다 내린다니까..ㅎ
    in_passenger.append(passenger) # 그 인원수룰 더함

print(max(in_passenger))
#print(in_passenger[-1]) # 가장 많았던 사람수