
class Solution:
    def intToRoman(num):
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol=["M","CM","D","CD","C","XC","X","XL","X","IX","V","IV","I"]
        res,i="",0
        while num:
            res+=num//values[i]*symbol[i]
            num%=values[i]
            i+=1
        return res
    def romanToInt(s):
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans,prev=0,0
        for i in s[::-1]:
            if prev<=dic[i]:
                ans+=dic[i]
            else:
                ans-=dic[i]
            prev=dic[i]
        return ans
num=int(input("enter one word:"))
s=input("enter one Roman:")
response1=Solution.romanToInt(s)
response=Solution.intToRoman(num)
print(response)
print(response1)
