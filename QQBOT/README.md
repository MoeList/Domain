1.���� �������(���԰�) 395 �� OneBot-YaYa 582 ����ѹ

2.��ѹ������ܵ��ļ��У�����������.exe 395��������ļ�������Ϻ󣬽�OneBot-YaYa.XQ.dll����.\Plugin�������������

3.�е��˺Ź�������¼�������˺�

4.��ϸ�������ļ�˵�� .\OneBot\config.yml

5.ÿ�������˶��������ö�� ����WS ����WS HTTP ����ʵ�ڲ�����Ⱥ 116�ʻ����� issue 38

6.�ٴ�����������ܣ�������ʲô�Ĺ��ˣ�

7.ע����Ҫʹ�����ز�����ܣ�����ᵼ�¿�����ˣ���Ϊ�����go����������

�������ӣ�https://discourse.xianqubot.com/t/topic/50/2

# �汾
version: 1.0.5
# ����QQ��
master: 8888888
# �Ƿ���DEBUG��־
debug: true
# �������ã�Ĭ�ϲ���
heratbeat:
  enable: true
  interval: 10000
# �������ã���δʵ��
cache:
  database: false
  image: false
  record: false
  video: false
# ��ͬ�����˵����ã�ע��yaml�� "-" ����һ�����ڵ��ж���ӽڵ�
bots:
# �����õļ�����QQ
- bot: 0
  # ����WS
  websocket:
  # ���ӵ��ķ�������֣��Լ���
  - name: WSS EXAMPLE
    # �Ƿ������÷�������ӣ�����Ϊ true
    enable: false
    # OneBot������������HOST������������һ��Ϊ 127.0.0.1
    host: 127.0.0.1
    # OneBot������������PORT�������Ķ˿�Ҫ��Ӧ
    port: 6700
    # OneBot������ Token ,һ�㲻��
    access_token: ""
    # OneBot�ϱ���ʽ����Ϊ string �� array ��һ�㲻��
    post_message_format: string
  # ����WS
  websocket_reverse:
  # ���ӵ��ķ�������֣��Լ���
  - name: WSC EXAMPLE
    # �Ƿ������÷�������ӣ�����Ϊ true
    enable: false
    # ����������ĵ�ַ��һ��ֻ��Ҫ�Ķ˿�
    url: ws://127.0.0.1:8080/ws
    # ��δʵ��
    api_url: ws://127.0.0.1:8080/api
    # ��δʵ��
    event_url: ws://127.0.0.1:8080/event
    # ��δʵ��
    use_universal_client: true
    # ������� Token ����ҲҪ��
    access_token: ""
    # OneBot�ϱ���ʽ����Ϊ string �� array ��һ�㲻��
    post_message_format: string
    # ����������ʱ��������λ����
    reconnect_interval: 3000
  # HTTP �� HTTP POST
  http:
  # ���ӵ��ķ�������֣��Լ���
  - name: HTTP EXAMPLE
    # �Ƿ������÷�������ӣ�����Ϊ true
    enable: true
    # OneBot������������HOST������������һ��Ϊ 127.0.0.1
    host: 127.0.0.1
    # OneBot������������PORT�������Ķ˿�Ҫ��Ӧ
    port: 5700
    # OneBot������ Token ,һ�㲻��
    token: ""
    # OneBot �ϱ��ĵ�ַ���������������ַ
    post_url: 
    # OneBot �ϱ��� Secret��һ�㲻��
    secret: ""
    # �ȴ���Ӧʱ�䣬һ�㲻��
    time_out: 0
    # OneBot�ϱ���ʽ����Ϊ string �� array ��һ�㲻��
    post_message_format: string