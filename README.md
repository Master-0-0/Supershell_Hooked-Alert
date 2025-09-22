##使用方法
<img width="1204" height="560" alt="1" src="https://github.com/user-attachments/assets/4d9c3e76-e1d2-4187-9184-0bad6d526085" />
<img width="1685" height="438" alt="2" src="https://github.com/user-attachments/assets/461b2ebb-3b27-49f5-8a89-306c273261a6" />


##linux 后台运行（重要）
##使用 screen或 tmux终端复用工具
原理：创建独立会话，即使断开连接，会话仍保留在后台。  
```screen -S mysession  # 创建新会话
python3 your_script.py  # 运行程序
Ctrl+A → D            # 分离会话（程序继续运行）```
退出后ps aux 查看进程 是否有脚本运行
恢复会话：  screen -r mysession  # 重新连接

###微信&QQ启用邮箱提醒
https://mp.weixin.qq.com/s/cGjlGYaEdfj79JXyMMliTg


