import random
import string

def generate_random_string(length):
    """生成指定长度的随机字符串，包含字母和数字"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def write_to_file(filename, content):
    """将内容写入文件"""
    with open(filename, 'w') as file:
        file.write(content)

def main():
    # 获取用户输入的字符数量
    length = int(input("请输入你想要生成的随机字符串的长度: "))
    
    # 生成随机字符串
    random_string = generate_random_string(length)
    
    # 选择文件名并写入文件
    filename = input("请输入文件名 (包括扩展名): ")
    write_to_file(filename, random_string)
    
    print(f"已生成长度为 {length} 的随机字符串，并保存到文件 {filename}")

if __name__ == '__main__':
    main()