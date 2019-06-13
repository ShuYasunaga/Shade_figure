# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

def sun(height,time,ongitude,latitude,theta0_h,theta0_m,alpha0_h,alpha0_m,alpha1_h,alpha1_m,delta0_d,delta0_b,delta1_d,delta1_b):

    ans_division=int(longitude/15)
    ans_remainder=round(longitude%15, 2)

    f, i = math.modf(ans_remainder)

    anshour=ans_division
    ansmin=4*int(i)
    anssecmin=(4*int(round(f,2)*100))/60
    lamda_h=anshour
    lamda_m=ansmin+round(anssecmin,1)

    f, i = math.modf(latitude)
    param=i+(round(f,2)*100/60)
    sin_phi=math.sin(math.radians(param))
    cos_phi=math.cos(math.radians(param))

    alpha_h=alpha0_h
    alpha_m=(alpha1_m-alpha0_m)*3/24+alpha0_m#apparent declination　視赤経

    delta_d=delta0_d
    delta_b=(delta1_b-delta0_b)*3/24+delta0_b#apparent_right_ascension 視赤緯

    #param = (byo / 3600) + (delta_b / 60) + delta_d
    param = (delta_b / 60) + delta_d
    sin_delta=math.sin(math.radians(param))
    cos_delta=math.cos(math.radians(param))

    t=time-9

    d=theta0_h*15
    b=theta0_m*15
    theta0=(b/60)+d
    #print(theta0)
    t=t*15
    #print(t)

    d=lamda_h*15
    b=lamda_m*15
    lamda=(b/60)+d
    #print(lamda)

    d=alpha_h*15
    b=alpha_m*15
    alpha=(b/60)+d
    #print(alpha)

    H=theta0+(t*1.0027379)+lamda-alpha
    #print(round(H,1))

    sin_H=math.sin(math.radians(H))
    cos_H=math.cos(math.radians(H))

    """
    cos h sin A = －cos δ sin H ・・・(1)
    cos h cos A = cos φ sin δ －sin φ cos δ cos H ・・・(2)
    sin h = sin φ sin δ ＋cos φ cos δ cos H ・・・(3)

    A = arctan (－0.081829/－0.85584) = 5.5°

    """
    k1= -cos_delta*sin_H
    k2= (cos_phi*sin_delta)-(sin_phi*cos_delta*cos_H)

    A=math.degrees(math.atan(k1/k2))
    A=A+180

    k3=(round(sin_phi,5)*round(sin_delta,5))+(round(cos_phi,5)*round(cos_delta,5)*round(cos_H,5))
    print(k3)
    h=math.degrees(k3)

    cot_h=math.tan(math.radians(h))
    cot_h=1/cot_h
    cot_h=height*cot_h

    print("-----ANSSER-----")
    print("time:",end="")
    print(time)
    """
    print("東経λ",end=":")
    print(anshour,end="h")
    print(ansmin+round(anssecmin,1),end="min\n")
    print("東経λ",end=":\n")
    print("  sinφ",end=":")
    print(round(sin_phi,5))
    print("  cosφ",end=":")
    print(round(cos_phi,5))
    print("t",end=":")
    print(t,end="hour\n")
    print("グリニッジ視恒星時",end=":")
    print(theta0_h,end="h")
    print(theta0_m,end="min\n")
    print("視赤経",end=":")
    print(alpha_h,end="h")
    print(round(alpha_m,1),end="min\n")
    print("視赤緯",end=":")
    print(delta_d,end="°")
    print(round(delta_b,1),end="'\n")
    print("視赤緯sinδ",end=":")
    print(round(sin_delta,5))
    print("視赤緯cosδ",end=":")
    print(round(cos_delta,5))
    print("太陽の時角 ",end=":")
    print(round(H,1))
    print("sinH",end=":")
    print(sin_H)
    print("cosH",end=":")
    print(cos_H)
    """
    print("k1",end=":")
    print(k1)
    print("k2",end=":")
    print(k2)
    print("方位角A",end=":")
    print(round(A,1))
    print("影の方位角A",end=":")
    KA=round(A,1)+180
    if 360>KA:
        pass
    else:
        KA=KA-360
    print(round(KA,1))
    print("高度h",end=":")
    print(h)
    print("影の長さ",end=":")
    print(cot_h)
    """
    x=rcosθ
    y=rsinθ
    """
    x=cot_h*math.cos(math.radians(KA))
    y=cot_h*math.sin(math.radians(KA))
    print(x,y)
    return x,y,time


if __name__ == '__main__':
    #緯度経度、時間情報以外は理科年表を参照する必要あり。
    longitude=139.44
    latitude=35.39

    theta0_h=6
    theta0_m=2.6

    alpha0_h=18
    alpha0_m=1.0
    alpha1_h=18
    alpha1_m=5.4

    delta0_d=-23
    delta0_b=-26.4
    delta1_d=-23
    delta1_b=-26.1

    shadow=[]
    for i in range(8,17):
        x,y,time=sun(10,i,longitude,latitude,theta0_h,theta0_m,alpha0_h,alpha0_m,alpha1_h,alpha1_m,delta0_d,delta0_b,delta1_d,delta1_b)
        shadow.append([x,y,time])

    print("result")
    for i in shadow:
        print(i)

    fig=plt.figure(figsize=(5,5), dpi=300)
    ax=plt.gca()
    #setting_plot=[[0,0],[0,100],[50,100],[50,50],[150,50],[150,0]]
    setting_plot=[[0,0],[0,100],[100,100],[100,0]]
    for i in range(0,len(setting_plot)-1):
        plt.plot([setting_plot[i][0],setting_plot[i+1][0]],[setting_plot[i][1],setting_plot[i+1][1]],color='red',linewidth='0.5')
    plt.plot([setting_plot[0][0],setting_plot[-1][0]],[setting_plot[0][1],setting_plot[-1][1]],color='red',linewidth='0.5')

    for cm in range(5,11,5):
        for i in range(0,len(setting_plot)-1):
            if i==0:
                plt.plot([setting_plot[i][0]-cm,setting_plot[i+1][0]-cm],[setting_plot[i][1]-cm,setting_plot[i+1][1]+cm],color='green',linewidth='0.5', linestyle='dashed')
            elif setting_plot[i][1]==setting_plot[i+1][1]:
                plt.plot([setting_plot[i][0]-cm,setting_plot[i+1][0]+cm],[setting_plot[i][1]+cm,setting_plot[i+1][1]+cm],color='green',linewidth='0.5', linestyle='dashed')
            else:
                plt.plot([setting_plot[i][0]+cm,setting_plot[i+1][0]+cm],[setting_plot[i][1]+cm,setting_plot[i+1][1]-cm],color='green',linewidth='0.5', linestyle='dashed')
        if setting_plot[0][0]==setting_plot[-1][0]:
            plt.plot([setting_plot[0][0]-cm,setting_plot[-1][0]+cm],[setting_plot[0][1]+cm,setting_plot[-1][1]+cm],color='green',linewidth='0.5', linestyle='dashed')
        else:
            plt.plot([setting_plot[0][0]-cm,setting_plot[-1][0]+cm],[setting_plot[0][1]-cm,setting_plot[-1][1]-cm],color='green',linewidth='0.5', linestyle='dashed')


    for i in shadow:
        cnt=len(setting_plot)
        c=0
        buf=[]
        buf_p=[]
        if i[2]>12:
            for plot in setting_plot:
                plt.plot([plot[0],plot[0]+i[1]],[plot[1],plot[1]+i[0]],color='black',linewidth='0.5', linestyle='dashed')
                if cnt-1<c:
                    pass
                elif c==0:
                    pass
                elif c==1:
                    pass
                else:
                    if len(buf)!=0:
                        plt.plot([buf_p[0]+buf[1],plot[0]+i[1]],[buf_p[1]+buf[0],plot[1]+i[0]],color='blue',linewidth='0.5')
                buf=i
                buf_p=plot
                c=c+1
        elif i[2]==12:
            for plot in setting_plot:
                plt.plot([plot[0],plot[0]+i[1]],[plot[1],plot[1]+i[0]],color='black',linewidth='0.5', linestyle='dashed')
                if cnt-1<c:
                    pass
                else:
                    if len(buf)!=0:
                        plt.plot([buf_p[0]+buf[1],plot[0]+i[1]],[buf_p[1]+buf[0],plot[1]+i[0]],color='blue',linewidth='0.5')
                buf=i
                buf_p=plot
                c=c+1
        else:
            for plot in setting_plot:
                plt.plot([plot[0],plot[0]+i[1]],[plot[1],plot[1]+i[0]],color='black',linewidth='0.5', linestyle='dashed')
                if cnt-1<c:
                    pass
                elif c<3:
                    if len(buf)!=0:
                        plt.plot([buf_p[0]+buf[1],plot[0]+i[1]],[buf_p[1]+buf[0],plot[1]+i[0]],color='blue',linewidth='0.5')
                else:
                    pass
                buf=i
                buf_p=plot
                c=c+1
    plt.xlim([-100,300])
    plt.ylim([-100,300])



    #plt.text(i[1]+(i[1]/10),i[0]+(i[0]/10),str(i[2])+":00",size='10',ha='center')
    #plt.show()
    plt.savefig('figure.png')
