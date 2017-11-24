import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import  Axes3D
import matplotlib.cm
frame1= pd.DataFrame({
    'id':['ball','pencil','pen','mug','ashtray'],
    'price':[12.33,11.44,33.21,13.23,33.62]

})
frame2=pd.DataFrame({
    'id':['pencil','pencil','ball','pen'],
    'color':['white','red','red','black']})
'''
      id  price  color
0    ball  12.33    red
1  pencil  11.44  white
2  pencil  11.44    red
3     pen  33.21  black
'''
#frame1和frame2 只有一个相同的列，合并之后，同时存在的行被保留
print(pd.merge(frame1,frame2))

frame3= pd.DataFrame({
    'id':['ball','pencil','pen','mug','ashtray'],
    'color':['white','red','red','black','green'],
    'brand':['OMG','ABC','ABC','POD','POD']

})
frame4=pd.DataFrame({
    'id':['pencil','pencil','ball','pen'],
    'brand':['OMG','POD','ABC','POD']})
'''
frame3和frame4 有2列名字相同，返回空。因为不知道在那列上做链接
Empty DataFrame
Columns: [brand, color, id]
Index: []

'''
print(pd.merge(frame3,frame4))
'''
在之前的基础上选择2列中的一列(id)做连接
 brand_x  color      id brand_y
0     OMG  white    ball     ABC
1     ABC    red  pencil     OMG
2     ABC    red  pencil     POD
3     ABC    red     pen     POD
在之前的基础上选择2列中的一列(brand)做连接
  brand  color     id_x    id_y
0   OMG  white     ball  pencil
1   ABC    red   pencil    ball
2   ABC    red      pen    ball
3   POD  black      mug  pencil
4   POD  black      mug     pen
5   POD  green  ashtray  pencil
6   POD  green  ashtray     pen
'''
print(pd.merge(frame3,frame4,on='brand'))

frame4.columns=['brand','sid']
'''
  brand     sid
0   OMG  pencil
1   POD  pencil
2   ABC    ball
3   POD     pen
换id 的名称 id--》sid
'''
print(frame4)
'''
pd.merge(frame3,frame4,left_on='id',right_on='sid'左边的 id列匹配右边的 sid列
 brand_x  color      id brand_y     sid
0     OMG  white    ball     ABC    ball
1     ABC    red  pencil     OMG  pencil
2     ABC    red  pencil     POD  pencil
3     ABC    red     pen     POD     pen
'''
print(pd.merge(frame3,frame4,left_on='id',right_on='sid'))

'''
  brand_x  color      id brand_y
0     OMG  white    ball     ABC
1     ABC    red  pencil     OMG
2     ABC    red  pencil     POD
3     ABC    red     pen     POD
'''
frame4.columns=['brand','id']
print(pd.merge(frame3,frame4,on='id'))

'''
pd.DataFrame的拼接
'''
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
array1= np.arange(9).reshape(3,3)
print(array1)
'''
array1=array1+6
[[ 6  7  8]
 [ 9 10 11]
 [12 13 14]]
 数组加一个数字，这种加法会被广播
'''
array2=array1+6
print(array2)
'''
np.concatenate([array1,array2],axis=1)
在列这个维度拼接数组
[[ 0  1  2  6  7  8]
 [ 3  4  5  9 10 11]
 [ 6  7  8 12 13 14]]
'''
print(np.concatenate([array1,array2],axis=1))
'''
axis=0说明在行这个维度拼接
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]]
'''
print(np.concatenate([array1,array2],axis=0))
'''
pandas库S使用concat函数，实现拼接m默认axis=0,mm默认外联操作。可以用jion属性设置为内联
1    0.578150
2    0.231132
3    0.495588
4    0.847514
5    0.270132
6    0.499404
7    0.187187
8    0.202712
dtype: float64
          0         1
1  0.007719       NaN
2  0.758962       NaN
3  0.797474       NaN
4  0.597090       NaN
5       NaN  0.499476
6       NaN  0.663254
7       NaN  0.296893
8       NaN  0.358735
'''
ser1=pd.Series(np.random.rand(4),index=[1,2,3,4])
ser2=pd.Series(np.random.rand(4),index=[5,6,7,8])
print(pd.concat([ser1,ser2],axis=1,join='inner'))
'''
DataFrame的连接操作：
          A         B         C
1  0.477172  0.821841  0.249565
2  0.124310  0.787697  0.653929
3  0.646169  0.311578  0.657806
4  0.171987  0.663678  0.834123
5  0.907069  0.947338  0.825815
6  0.417903  0.701007  0.496995
在列上连接
          A         B         C         A         B         C
1  0.023462  0.934919  0.577923       NaN       NaN       NaN
2  0.040049  0.937090  0.243661       NaN       NaN       NaN
3  0.887609  0.644117  0.283225       NaN       NaN       NaN
4       NaN       NaN       NaN  0.525157  0.320823  0.143438
5       NaN       NaN       NaN  0.504218  0.841718  0.028816
6       NaN       NaN       NaN  0.804849  0.211699  0.787572
'''
framex=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[1,2,3],columns=['A','B','C'])
framex2=pd.DataFrame(np.random.rand(9).reshape(3,3),index=[4,5,6],columns=['A','B','C'])
print(pd.concat([framex,framex2],axis=1))
#删除frame中的重复元素
'''
     color  value
0  white      2
1  white      1
2    red      3
3    red      3
4  white      2
dframe.duplicated()看是不是重复出现的
'''
dframe =pd.DataFrame({'color':['white','white','red','red','white'],'value':[2,1,3,3,2]})
print(dframe)
print(dframe[dframe.duplicated()])
new_col={'red':'red1','verde':'green'}
print(dframe.replace(new_col))
'''
0    1.0
1    3.0
2    NaN
3    4.0
4    6.0
5    NaN
6    3.0
dtype: float64
'''
ser=pd.Series([1,3,np.nan,4,6,np.nan,3])
print(ser)
#用0替代 np.nan
ser.replace(np.nan,0)
framem= pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow']
                      })
print(framem)
price={
    'ball':5.56,
    'mug':4.20,
    'bottle':1.30,
    'scissors':3.14,
    'pen':1.30,
    'pencil':0.56,
    'ashtray':2.75
}
'''
    color     item  price
0   white     ball   5.56
1     red      mug   4.20
2   green      pen   1.30
3   black   pencil   0.56
4  yellow  ashtray   2.75

'''
framem['price']=framem['item'].map(price)
print(framem)

#matplotlib 数据可视化

'''绘制图形属性'''
t=np.arange(0,2.5,0.1)
print(len(t))
y1=list(map(math.sin,math.pi*t))
y2=list(map(math.sin,math.pi*t+math.pi/2))
y3=list(map(math.sin,math.pi*t-math.pi/2))
t=np.arange(0,2.5,0.1)
print(len(y1))
#plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r--')
plt.plot(t,y1,linewidth=2.0)
plt.show()


'''
给图标添加文本：

'''
plt.axis([0,5,0,20])
plt.title("my plot:")
plt.xlabel("counting")
plt.ylabel("square values")
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
plt.title('my first plot',fontsize=20,fontname='times new roman')
plt.xlabel("counting",color='gray')
plt.ylabel("square values",color='gray')#添加y轴说明
plt.axis([0,5,0,20])
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.text(1,1.5,"first")
plt.text(2,4.5,"second")#添加文本
plt.text(3,9.5,"third")
plt.text(4,16.5,"four")
plt.grid(True)#添加网格
plt.legend('ooooooo',loc=2)
plt.savefig('my_matplotlib.png')
plt.show()
#线形图：
x=np.arange(-2*np.pi,2*np.pi,0.01)
y=np.sin(3*x)/x
y1=np.sin(2*x)/x
y2=np.sin(x)/x
plt.plot(x,y)
plt.plot(x,y1,linewidth=2)
plt.plot(x,y2,'--')
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$-\pi$',r'$0$',r'$\pi$',r'$2\pi$'])
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
pop = np.random.randint(0,100,100)
n,bins,patches= plt.hist(pop,bins=20)
plt.show()
data={'data1':[1,3,4,3,5],
      'data2':[2,4,5,2,4],
      'data3':[3,2,3,1,3]
      }
df= pd.DataFrame(data)
df.plot(kind='bar')
plt.show()

lables=['nokia','samsung','apple','lumia']
values=[10,30,45,15]
color=['blue','green','red','yellow']
explode=[0.1,0.2,0,0]
plt.pie(values,labels=lables,colors=color,explode=explode,startangle=180,shadow=True,autopct='%1.1f%%')
plt.axis('equal')
plt.show()

'''
#高级图标，等值线：
X,Y=np.meshgrid(x,y)之后
[[-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]
 [-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]
 [-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]
 ..., 
 [-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]
 [-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]
 [-2.   -1.99 -1.98 ...,  1.97  1.98  1.99]]
plt.contourf 与 plt.contour 区别：
f：filled，也即对等高线间的填充区域进行填充（使用不同的颜色）；
contourf：将不会再绘制等高线（显然不同的颜色分界就表示等高线本身），
'''
dx=0.01
dy=0.01
x=np.arange(-2.0,2.0,dx)
y=np.arange(-2.0,2.0,dy)
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
def f(x,y):
    return ((1-y**5 +x**5)*np.exp(-x**2-y**2))
c=plt.contour(X,Y,f(X,Y),8,color='black')
plt.contourf(X,Y,f(X,Y),8)
plt.clabel(c,inline=1,fomtzise=10)
plt.colorbar()
plt.show()

'''
绘制极区图（）就是极坐标表示
'''
theta=np.arange(0,2*np.pi,2*np.pi/8)
radii=np.array([4,7,5,3,1,5,6,7])#每个扇区的值
plt.axes([0.0025,0.0025,0.95,0.95],polar =True)
colors=np.array(['red','green','blue','gray','pink','black','yellow','orange'])
bars=plt.bar(theta,radii,width=(2*np.pi/8),bottom=0.0,color=colors)
plt.show()
'''
绘制3d曲面：
mplot3d
'''

fig= plt.figure()
ax=Axes3D(fig)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X1,Y1=np.meshgrid(X,Y)
def f(x,y):
    return ((1-y**5 +x**5)*np.exp(-x**2-y**2))
ax.plot_surface(X1,Y1,f(X1,Y1),rstride=1,cstride=1,cmap=plt.cm.hot)
ax.view_init(elev=30,azim=125)
plt.show()