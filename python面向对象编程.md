#### python面向对象编程  

```python
class Cat:       #定义名称
    
   #定义属性
    def __init__(self, new_name, new_age):   #初始化对象
        self.name = new_name       #属性
        self.age = new_age         #属性

    def __str__(self):    #引用和说明
        return "%s's age is: %d"%(self.name,self.age)

    #定义方法
    def eat(self):
        print("cat is eating fish")

    def drink(self):
        print("cat is drinking cola")

    def introduce(self):
        print("%s's age is: %d"%(self.name,self.age))

#creat a object
tom = Cat("Tom",40)
lanmao = Cat("Lanmao",10)

print(tom)
print(lanmao)

```
#### 实例
1.烤地瓜
```
class SweetPotato:

    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜 状态：%s(%d),添加的佐料有%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):
        self.cookedLevel +=cooked_time

        if self.cookedLevel >=0 and self.cookedLevel<3:
            self.cookedString = "raw"
        elif self.cookedLevel >=3 and self.cookedLevel<5:
            self.cookedString = "half raw"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString = "mature"
        elif self.cookedLevel>=8:
            self. cookedString = "over mature"
    def addCondiments(self,item):
        self.condiments.append(item)
#创建一个digua对象
di_gua = SweetPotato()
print(di_gua)
#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("onion")
print(di_gua)
di_gua.cook(1)
print(di_gua)
```
1.1. 为了能够储存多个数据，往往在开发中让一个属性是列表。  
1.2. 对象的属性不会随着方法的调用而结束，一个方法被调用的时候是可以用局部变量来保存数据的。  
  
2.存放家具

```
class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        msg = "房子的面积是：%d，可用面积是：%d，户型是：%s，地址是：%s"%(self.area,self.left_area,self.info,self.addr)
        msg += ",当前房子里的物品有%s"%(str(self.contain_items))
        return msg 
   
    def add_item(self,item):                  #python类中的self等同于C++中的this指针
        #self.left_area -= item.area
        #self.contain_items.append(item.name)

        self.left_area -= item.get_area()     #尽量不要直接调用属性，通过一个简单的get函数来实现更好的控制权限，比如可增加判断语句，添加隐藏属性
        self.contain_items.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s的面积是：%d"%(self.name,self.area)

    def get_area(self):
        return self.area
    def get_name(self):
        return self.name

fangzi = Home(129,"三室一厅","北京市 朝阳街 长安街 666号")
print(fangzi)
bed1 = Bed("Simons",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)

bed2 = Bed("三人床",3)
fangzi.add_item(bed2)
print(fangzi)

```

##### 补充知识
1. [vi保存退出":x"与":wq"的区别](https://blog.csdn.net/wuxiaobingandbob/article/details/48809873)
2. vi设置python格式的自动缩进
> 在终端输入 vim ~/.vimrc  , 并设置
```
     set tabstop=9
     set expandtab
     set shiftwidth=4
     set softtabstop=4
     filetype indent on
```

3. vi自动补全命令： ctrl+N或ctrl+P
