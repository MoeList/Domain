1.下载 先驱框架(测试版) 395 与 OneBot-YaYa 582 并解压

2.解压先驱框架到文件夹，并运行先驱.exe 395，待相关文件生成完毕后，将OneBot-YaYa.XQ.dll放入.\Plugin，重启先驱框架

3.切到账号管理界面登录机器人账号

4.详细的配置文件说明 .\OneBot\config.yml

5.每个姬气人都可以设置多个 正向WS 反向WS HTTP 服务，实在不懂加群 116问或者提 issue 38

6.再次重启先驱框架（热重载什么的咕了）

7.注：不要使用重载插件功能，否则会导致框架闪退，此为框架与go不兼容问题

详情链接：https://discourse.xianqubot.com/t/topic/50/2

# 版本
version: 1.0.5
# 主人QQ号
master: 8888888
# 是否开启DEBUG日志
debug: true
# 心跳设置，默认不动
heratbeat:
  enable: true
  interval: 10000
# 缓存设置，暂未实现
cache:
  database: false
  image: false
  record: false
  video: false
# 不同姬气人的设置，注意yaml中 "-" 代表一个父节点有多个子节点
bots:
# 被设置的姬气人QQ
- bot: 0
  # 正向WS
  websocket:
  # 连接到的服务的名字，自己起
  - name: WSS EXAMPLE
    # 是否启动该服务的连接，连接为 true
    enable: false
    # OneBot建立服务器的HOST，无特殊需求一般为 127.0.0.1
    host: 127.0.0.1
    # OneBot建立服务器的PORT，与插件的端口要对应
    port: 6700
    # OneBot服务器 Token ,一般不动
    access_token: ""
    # OneBot上报格式，可为 string 或 array ，一般不动
    post_message_format: string
  # 反向WS
  websocket_reverse:
  # 连接到的服务的名字，自己起
  - name: WSC EXAMPLE
    # 是否启动该服务的连接，连接为 true
    enable: false
    # 插件服务器的地址，一般只需要改端口
    url: ws://127.0.0.1:8080/ws
    # 暂未实现
    api_url: ws://127.0.0.1:8080/api
    # 暂未实现
    event_url: ws://127.0.0.1:8080/event
    # 暂未实现
    use_universal_client: true
    # 插件填了 Token 这里也要填
    access_token: ""
    # OneBot上报格式，可为 string 或 array ，一般不动
    post_message_format: string
    # 掉线重连的时间间隔，单位毫秒
    reconnect_interval: 3000
  # HTTP 和 HTTP POST
  http:
  # 连接到的服务的名字，自己起
  - name: HTTP EXAMPLE
    # 是否启动该服务的连接，连接为 true
    enable: true
    # OneBot建立服务器的HOST，无特殊需求一般为 127.0.0.1
    host: 127.0.0.1
    # OneBot建立服务器的PORT，与插件的端口要对应
    port: 5700
    # OneBot服务器 Token ,一般不动
    token: ""
    # OneBot 上报的地址，即插件服务器地址
    post_url: 
    # OneBot 上报的 Secret，一般不填
    secret: ""
    # 等待响应时间，一般不动
    time_out: 0
    # OneBot上报格式，可为 string 或 array ，一般不动
    post_message_format: string