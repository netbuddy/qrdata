import random
import secrets
import string

def generate_random_string(type, length):
    # 基于生成不同类型的随机字符串 type值 1-纯数字，2-数字+大写字母，3-中英文混合，4-全英文，5-全中文(UTF-8)，6-全中文(GBK)，7-二进制数据
    if type == 1:
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    elif type == 2:
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    elif type == 3:
        characters = ''
        # 生成length长度的随机中文字符串
        for _ in range(length):
            #随机生成1-3的数字
            num = random.randint(1, 3)
            if num == 1:
                #生成随机的0-9的数字
                character = random.choice(string.digits)
                characters += character
            elif num == 2:
                #生成随机的字母
                character = random.choice(string.ascii_letters)
                characters += character
            elif num == 3:
                #生成随机的中文字符
                character = chr(random.randint(0x4e00, 0x9fbf))
                characters += character
        return characters
    elif type == 4:
        characters = string.digits + string.ascii_letters + string.punctuation + ' \t\n\r'
        return ''.join(random.choice(characters) for _ in range(length))
    elif type == 5:
        characters = ''
        for _ in range(length):
            #生成随机的中文字符
            character = chr(random.randint(0x4e00, 0x9fbf))
            characters += character
        return characters
    elif type == 6:
        characters = b''
        for _ in range(length):
            #生成随机的中文字符
            character = b''
            while character == b'':
                try:
                    character = chr(random.randint(0x4e00, 0x9fbf)).encode("gbk")
                except UnicodeEncodeError:
                    print("unsupported character")
            characters += character
        return characters
    elif type == 7:
        random_bytes = secrets.token_bytes(length)
        return random_bytes


def write_to_file(filename, content):
    """将内容写入文件"""
    #如果content是字符串类型
    if isinstance(content, str):
        with open(filename, 'w') as file:
            file.write(content)
    #如果content是bytes类型
    elif isinstance(content, bytes):
        with open(filename, 'wb') as file:
            file.write(content)

def main():
    # 获取用户输入的字符数量
    length = int(input("请输入你想要生成的随机字符串的长度: "))
    
    type = int(input("请选择生成类型 (1-纯数字，2-数字+大写字母，3-中英文混合，4-全英文，5-全中文(UTF-8)，6-全中文(GBK)，7-二进制数据): "))
    random_string = generate_random_string(type, length)
    
    # 选择文件名并写入文件
    filename = input("请输入文件名 (包括扩展名): ")
    write_to_file(filename, random_string)
    
    print(f"已生成长度为 {length} 的随机字符串，并保存到文件 {filename}")

if __name__ == '__main__':
    main()