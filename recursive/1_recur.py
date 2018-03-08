# -*- coding:utf-8 -*-

def  to_str(n, base):
    """
    采用递归实现进制转换
    实现十进制转换2-16进制的数字
    """
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n /base, base) + convert_string[n % base]


print to_str(10, 16)

def reverse(s):
    """
    递归实现字符串翻转
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print reverse('abcdefg')

def cycle_word(s):
    """
    采用递归检测是否是回文
    如果是回文，name去掉收尾字符任然是回文
    验证前先去除空格和符号
    """
    s = s.replace(' ', '').lower()
    print s

    length = len(s)

    if length <= 1:
        return True
    else:
        return (s[0] == s[-1]) and cycle_word(s[1: -1])

print cycle_word('Live not on evil')
print cycle_word('Wassamassaw')
