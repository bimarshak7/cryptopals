from set1c3 import bestmatch        
def main():
    with open('4.txt') as f:
        result=[]
        for line in f:
            res=bestmatch(bytes.fromhex(line))

            result.append(res)
        op=sorted(result, key=lambda c: c['score'], reverse=True)[0]
        print(op)

if __name__ == "__main__":
    main()