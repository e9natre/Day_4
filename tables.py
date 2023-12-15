def mtables(n):
    length = len(str(n*20))
    for i in range(1, 21): 
        print(f"{n} x {i:2} = {n*i :{length}}")

if __name__ == "__main__":
    mtables(5)

    


