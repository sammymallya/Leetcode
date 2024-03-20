#Solution for List problem:List Operations:
#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
#Code:
if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        m = input().split()
        command = m[0]
        if command == "append":
            ans.append(int(m[1]))
        elif command == 'insert':
            ans.insert(int(m[1]), int(m[2]))
        elif command == "remove":
            ans.remove(int(m[1]))
        elif command == "sort":
            ans.sort()
        elif command == "pop":
            ans.pop()
        elif command == "reverse":
            ans = ans[::-1]
        else:
            print(ans)
