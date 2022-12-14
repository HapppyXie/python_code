# Athour:Mr Xie
# 开发时间:2021/10/22 19:42
'''
哈希：把任意长度的输入通过散列算法变换成固定长度的的输出，该输出就是散列值  （本质为一种算法）
            可以输入字符串，数据，文件，经过哈希运算后，变成一个固定长度的输出，该输出就是哈希值
            特点：不能从结果推出输入，所以也称不可逆算法
     特性：不可逆，计算极快
     用途：1.密码，基于hash,并保证同样的输入得到的结果一直一致,加了一些其他的算法
                    md5加密算法
               如用户输入明文abc123  加密后->  密文5093119263450728215 <-管理人员看到
              支付宝中再次输入 abc123  ->  5093119263450728215   通行
          2.文件的完整性校验：
                   发布20GB文件 hash后   ->   758403783477246198
                    下载后hash -> 758403783477246198 下载正确，没有被别人调包
          3.数字签名：
                   A --------> B  (A被C模仿,发信息给B
                   C -------->
                但 A 私钥  原文件hash后->  生成一段hash值（摘要信息），再加密
                     把原文+摘要一起发给B
                  B  公钥  -> 解密， 把摘要解密，得到 hash值
                         对原文件进行hash,也得到hash值，A的hash值跟B的hash值比较，一致，则是A本人

    基于hash的数据类型：
                    dict 1.key唯一，不可变，速度极快，不受dict大小影响
                         dict的key都要经过hash 变成数字储存，查找时使用二分法，
                    set  两个相同数据hash后，存储时系统默认已经存了一个相同的，不会再存一个
'''
print(hash('小旺旺'))
#其输出为散列值，而且每次运算都会改变，故无法推断输出,在IDLE中一直处于运行状态，输出值一样
print(hash(9456))
print(hash('intersted'))
print(hash('abc123'))
print(hash('20GB'))
