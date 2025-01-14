import os
from datetime import datetime
from netmiko import ConnectHandler

def connect_to_switch(switch, commands):
    """
    使用 netmiko 连接到交换机，先执行配置模式命令，再执行普通模式命令。
    """
    try:
        connection = ConnectHandler(**switch)
        output = ""

        # 明确的普通模式命令（可扩展）
        predefined_exec_commands = [
            "sh",
            "end",
            "wr me",
            "write memory",
            "exit",
            "telnet",
            "ssh",
        ]

        # 分类命令
        exec_commands = []
        config_commands = []

        for command in commands:
            # 如果是预定义的普通模式命令，或以 'show' 开头，则归类为普通模式
            if command in predefined_exec_commands or command.startswith("show"):
                exec_commands.append(command)
            else:
                # 默认归类为配置模式命令
                config_commands.append(command)

        # 执行配置模式命令
        if config_commands:
            output += "\n执行配置模式命令:\n"
            output += connection.send_config_set(config_commands)

        # 执行普通模式命令
        for command in exec_commands:
            output += f"\n命令: {command}\n{connection.send_command(command, delay_factor=2)}"

        connection.disconnect()
        return output

    except Exception as e:
        return f"连接到交换机 {switch['host']} 时出错: {e}"


def batch_execute(switches, credentials, commands):
    """
    批量连接到交换机并执行命令。
    """
    results = {}
    for switch in switches:
        switch.update(credentials)  # 添加用户名和密码
        print(f"正在连接到交换机 {switch['host']}...")
        output = connect_to_switch(switch, commands)
        results[switch['host']] = output
        print(f"交换机 {switch['host']} 的命令输出已完成。\n")
    return results

if __name__ == "__main__":
    # 用户名和密码直接在代码中定义
    credentials = {
        "device_type": "cisco_ios",  # 设备类型
        "username": "",        # 替换为你的用户名
        "password": "",     # 替换为你的密码
    }

    # 定义交换机信息（只需指定 IP）
    switches = [
        {"host": "ncnex072"},  # 替换为你的交换机 IP
      #  {"host": "ncnex041"},
      #  {"host": "ncnex042"},
    ]

    # 要执行的命令列表
    commands = [
    #    "show ip int br",  # 显示接口信息
    #    "conf t",          # 进入全局配置模式
        "wr me",
        "show run | se ISE",

    ]

    # 批量执行命令
    results = batch_execute(switches, credentials, commands)

    # 输出结果到控制台
    for host, output in results.items():
        print(f"交换机 {host} 的输出:\n{output}\n{'-' * 60}")

    # 获取当前日期时间，生成时间戳文件名
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"C:\\Temp\\results_{timestamp}.txt"

    # 确保目录存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 保存结果到文件_日期时间
    with open(output_file, "w") as f:
        for host, output in results.items():
            f.write(f"交换机 {host} 的输出:\n{output}\n{'-'*60}\n")

    print(f"所有结果已保存到文件: {output_file}")
