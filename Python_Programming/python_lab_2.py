
'''
N = int(input("Enter a number of items : "))
total_tokens = 0
item_more_than_one_token = 0
max_tokens = 0 

for i in range(N):

    price = int(input("Enter the price : "))
    
'''
def solve():
    n = int(input("Enter a number of items : " ))

    tokens = input().strip().split()
   # tokens = [int(x) for x in tokens]

    total_tokens = 0
    item_more_than_one_token = 0
    max_tokens = 0

    for i in range(n):
        price = int(tokens[i])
        total = ( price + 9 ) // 10 
        # total = price // 10 + ( 1 if price % 10 != 0 else 0 )
        total_tokens = total_tokens + total

        if total > 1:
            item_more_than_one_token += 1
        if total > max_tokens:
            max_tokens = total
    print(total_tokens, item_more_than_one_token, max_tokens)

if __name__ == "__main__":
    solve()



