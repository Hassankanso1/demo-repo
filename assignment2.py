def reverse(text,i)
    reversed=""
    for index in range(1,len(text),+1):
        reversed+=(len(text)-1)
    result=""
    for index in range(i):
        result+=reversed
    print(result)
reverse("kanso",2)