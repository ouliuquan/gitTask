# 这是一个示例 Python 脚本。

# 按 Ctrl+F5 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import os


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 F9 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

    with open("repos.txt") as file:
        lines = file.readlines()

    for line in lines:
        # print(line)
        line = line.strip()
        # gitAddress = 'https://github.com/massiveflow/toml-nodejs.git'
        gitAddress = line
        gitPath = './'
        gitNameEnd = len(gitAddress)
        if gitAddress.endswith('.git'):
            gitNameEnd = gitAddress.find('.git')
        gitNameBegin = gitAddress.rfind('/')
        gitName = gitAddress[gitNameBegin:gitNameEnd]
        # print(gitName)

        cmdStr = 'git clone --progress -v ' + gitAddress + ' .' + gitName
        print(cmdStr)
        os.system(cmdStr)
