
#----------------18870. 좌표 압축 ---------------------------#
# 수직선 위에 x1,x2,...xn. 이걸 좌표 압축하려고 함
# xi를 좌표 압축한 결과 x'i는 xi>xj만족하는 서로 다른 좌표 개수와 같아야함
# 첫째 줄에 N
# 둘째 줄엔 공백으로 구분된 x1,x2,...xn 주어짐
# x'1,x'2,...x'n 을 공백으로 구분되게 프린트
N=int(input())
X=list(map(int,input().split()))

sX=sorted(set(X))     #중복되는 값 삭제하고 순서대로 정렬
dictionary={sX[i] : i for i in range(len(sX))}   # 다른 사람 코드 참고,,

for i in X:
    print(dictionary[i], end=' ')


