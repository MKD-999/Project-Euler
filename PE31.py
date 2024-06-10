cnt = 1

for a in range(3):
    for b in range(1+int((200-100*a)/50)):
        for c in range(1+int((200-100*a-50*b)/20)):
            for d in range(1+int((200-100*a-50*b-20*c)/10)):
                for e in range(1+int((200-100*a-50*b-20*c-10*d)/5)):
                    for f in range(1+int((200-100*a-50*b-20*c-10*d-5*e)/2)):
                        for g in range(1+int((200-100*a-50*b-20*c-10*d-5*e-2*f))):
                            if a*100+b*50+c*20+d*10+e*5+f*2+g*1 == 200:
                                cnt += 1


print(cnt)