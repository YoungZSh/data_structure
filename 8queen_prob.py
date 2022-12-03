def check(n,col,state):
    """
    检测此次摆放的棋子是否与前面的棋子冲突
    """
    if n==0:
        return False
    else:
        for i in range(n):
            if state[i]==col:#检测此次摆放的棋子是否与之前的棋子在同一竖线内
                return True
            elif abs(state[i]-col)==n-i:#检测此次摆放的棋子是否与之前的棋子在同一斜线内
                return True
        return False

def queen_prob(n,state,ans):
    """
    回溯法解决八皇后问题
    """
    for col in range(8):
        if check(n,col,state)==False:
            state[n]=col
            if n==7:
                ans.append(state.copy())
                state[n]=0
                return
            queen_prob(n+1,state,ans)
            state[n]=0            

if __name__=="__main__":
    state=[0]*8
    ans=[]
    queen_prob(0,state,ans)
    for _ in ans:
        print(_)
    print(len(ans))

