# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerEventDataResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'schedule_type': 'str',
        'schedule': 'str',
        'user_event': 'str',
        'triggerid': 'str',
        'type': 'int',
        'path': 'str',
        'protocol': 'str',
        'req_method': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'match_mode': 'str',
        'env_name': 'str',
        'env_id': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'auth': 'str',
        'invoke_url': 'str',
        'func_info': 'ApigTriggerFuncInfo',
        'sl_domain': 'str',
        'backend_type': 'str',
        'instance_id': 'str',
        'roma_app_id': 'str',
        'operations': 'list[str]',
        'collection_name': 'str',
        'db_name': 'str',
        'db_password': 'str',
        'db_user': 'str',
        'instance_addrs': 'list[str]',
        'mode': 'str',
        'batch_size': 'int',
        'queue_id': 'str',
        'consumer_group_id': 'str',
        'polling_interval': 'int',
        'stream_name': 'str',
        'sharditerator_type': 'str',
        'polling_unit': 'str',
        'max_fetch_bytes': 'int',
        'is_serial': 'str',
        'log_group_id': 'str',
        'log_topic_id': 'str',
        'bucket': 'str',
        'prefix': 'str',
        'suffix': 'str',
        'events': 'list[str]',
        'topic_urn': 'str',
        'topic_ids': 'list[str]',
        'kafka_user': 'str',
        'kafka_password': 'str',
        'kafka_connect_address': 'str',
        'kafka_ssl_enable': 'bool',
        'access_password': 'str',
        'access_user': 'str',
        'connect_address': 'str',
        'exchange_name': 'str',
        'vhost': 'str',
        'ssl_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'schedule_type': 'schedule_type',
        'schedule': 'schedule',
        'user_event': 'user_event',
        'triggerid': 'triggerid',
        'type': 'type',
        'path': 'path',
        'protocol': 'protocol',
        'req_method': 'req_method',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'match_mode': 'match_mode',
        'env_name': 'env_name',
        'env_id': 'env_id',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'auth': 'auth',
        'invoke_url': 'invoke_url',
        'func_info': 'func_info',
        'sl_domain': 'sl_domain',
        'backend_type': 'backend_type',
        'instance_id': 'instance_id',
        'roma_app_id': 'roma_app_id',
        'operations': 'operations',
        'collection_name': 'collection_name',
        'db_name': 'db_name',
        'db_password': 'db_password',
        'db_user': 'db_user',
        'instance_addrs': 'instance_addrs',
        'mode': 'mode',
        'batch_size': 'batch_size',
        'queue_id': 'queue_id',
        'consumer_group_id': 'consumer_group_id',
        'polling_interval': 'polling_interval',
        'stream_name': 'stream_name',
        'sharditerator_type': 'sharditerator_type',
        'polling_unit': 'polling_unit',
        'max_fetch_bytes': 'max_fetch_bytes',
        'is_serial': 'is_serial',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id',
        'bucket': 'bucket',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'events': 'events',
        'topic_urn': 'topic_urn',
        'topic_ids': 'topic_ids',
        'kafka_user': 'kafka_user',
        'kafka_password': 'kafka_password',
        'kafka_connect_address': 'kafka_connect_address',
        'kafka_ssl_enable': 'kafka_ssl_enable',
        'access_password': 'access_password',
        'access_user': 'access_user',
        'connect_address': 'connect_address',
        'exchange_name': 'exchange_name',
        'vhost': 'vhost',
        'ssl_enable': 'ssl_enable'
    }

    def __init__(self, name=None, schedule_type=None, schedule=None, user_event=None, triggerid=None, type=None, path=None, protocol=None, req_method=None, group_id=None, group_name=None, match_mode=None, env_name=None, env_id=None, api_id=None, api_name=None, auth=None, invoke_url=None, func_info=None, sl_domain=None, backend_type=None, instance_id=None, roma_app_id=None, operations=None, collection_name=None, db_name=None, db_password=None, db_user=None, instance_addrs=None, mode=None, batch_size=None, queue_id=None, consumer_group_id=None, polling_interval=None, stream_name=None, sharditerator_type=None, polling_unit=None, max_fetch_bytes=None, is_serial=None, log_group_id=None, log_topic_id=None, bucket=None, prefix=None, suffix=None, events=None, topic_urn=None, topic_ids=None, kafka_user=None, kafka_password=None, kafka_connect_address=None, kafka_ssl_enable=None, access_password=None, access_user=None, connect_address=None, exchange_name=None, vhost=None, ssl_enable=None):
        """TriggerEventDataResponseBody

        The model defined in huaweicloud sdk

        :param name: 触发器名称
        :type name: str
        :param schedule_type: 定时触发类型（TIMER触发器参数）。 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数
        :type schedule_type: str
        :param schedule: 定时触发规则（TIMER触发器参数）。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式
        :type schedule: str
        :param user_event: 附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\&quot;version\&quot;: \&quot;v1.0\&quot;,   \&quot;time\&quot;: \&quot;2018-06-01T08:30:00+08:00\&quot;,   \&quot;trigger_type\&quot;: \&quot;TIMER\&quot;,   \&quot;trigger_name\&quot;: \&quot;Timer_001\&quot;,   \&quot;user_event\&quot;: \&quot;您输入的附加信息\&quot;}
        :type user_event: str
        :param triggerid: APIG触发器id。（APIG触发器参数）
        :type triggerid: str
        :param type: API接口类型（APIG触发器参数）。 - 1：公有API - 2：私有API
        :type type: int
        :param path: APIG接口PATH路径（APIG触发器参数）。
        :type path: str
        :param protocol: API的请求协议（APIG触发器参数）。
        :type protocol: str
        :param req_method: API的请求方式（APIG触发器参数）。
        :type req_method: str
        :param group_id: API所属的分组编号（APIG触发器参数）。
        :type group_id: str
        :param group_name: API所属的分组名称（APIG触发器参数）。
        :type group_name: str
        :param match_mode: API的匹配方式（APIG触发器参数）。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）
        :type match_mode: str
        :param env_name: API的发布环境（APIG触发器参数）。
        :type env_name: str
        :param env_id: API的发布环境id（APIG触发器参数）。
        :type env_id: str
        :param api_id: API编号（APIG触发器参数）。
        :type api_id: str
        :param api_name: API名称（APIG触发器参数）。
        :type api_name: str
        :param auth: API的认证方式（APIG触发器参数）。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&amp;Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用
        :type auth: str
        :param invoke_url: API调用地址（APIG触发器参数）。
        :type invoke_url: str
        :param func_info: 
        :type func_info: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        :param sl_domain: APIG系统默认分配的子域名（APIG触发器参数）。
        :type sl_domain: str
        :param backend_type: API的后端类型（APIG触发器参数）。
        :type backend_type: str
        :param instance_id: 实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id
        :type instance_id: str
        :param roma_app_id: API归属的集成应用编号。（APIG触发器参数）
        :type roma_app_id: str
        :param operations: 自定义操作（CTS触发器参数）。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。
        :type operations: list[str]
        :param collection_name: 集合名称（DDS触发器参数）。
        :type collection_name: str
        :param db_name: 文档数据库名称（DDS触发器参数）。
        :type db_name: str
        :param db_password: 文档数据库密码（DDS触发器参数）。
        :type db_password: str
        :param db_user: 文档数据库用户名（DDS触发器参数）。
        :type db_user: str
        :param instance_addrs: 文档数据库实例地址（DDS触发器参数）。
        :type instance_addrs: list[str]
        :param mode: 文档数据库实例类型（DDS触发器参数）。 - Sharding：集群实例 - ReplicaSet：副本集实例 - Single：单节点实例
        :type mode: str
        :param batch_size: 批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内
        :type batch_size: int
        :param queue_id: 队列id（DMS触发器参数）。
        :type queue_id: str
        :param consumer_group_id: 消费组id（DMS触发器参数）。
        :type consumer_group_id: str
        :param polling_interval: 拉取周期。
        :type polling_interval: int
        :param stream_name: 通道名称（DIS触发器参数）。
        :type stream_name: str
        :param sharditerator_type: 起始位置（DIS触发器参数）。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。
        :type sharditerator_type: str
        :param polling_unit: 拉取周期单位（DIS触发器参数）。 - s：秒 - ms：毫秒
        :type polling_unit: str
        :param max_fetch_bytes: 最大提取字节数（DIS触发器参数）。
        :type max_fetch_bytes: int
        :param is_serial: 串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。
        :type is_serial: str
        :param log_group_id: 日志组id（LTS触发器参数）。
        :type log_group_id: str
        :param log_topic_id: 日志流id（LTS触发器参数）。
        :type log_topic_id: str
        :param bucket: 桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。
        :type bucket: str
        :param prefix: 前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。
        :type prefix: str
        :param suffix: 后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知
        :type suffix: str
        :param events: 触发事件（OBS触发器参数）。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象
        :type events: list[str]
        :param topic_urn: 主题URN（SMN触发器参数）。
        :type topic_urn: str
        :param topic_ids: KAFKA主题id列表（KAFKA触发器参数）。
        :type topic_ids: list[str]
        :param kafka_user: KAFKA账户名（KAFKA触发器参数）。
        :type kafka_user: str
        :param kafka_password: KAFKA账户密码（KAFKA触发器参数）。
        :type kafka_password: str
        :param kafka_connect_address: KAFKA实例连接IP地址（KAFKA触发器参数）。
        :type kafka_connect_address: str
        :param kafka_ssl_enable: KAFKA连接是否开启安全认证（KAFKA触发器参数）。
        :type kafka_ssl_enable: bool
        :param access_password: RABBITMQ账户密码（RABBITMQ触发器参数）。
        :type access_password: str
        :param access_user: RABBITMQ账户名（RABBITMQ触发器参数）。
        :type access_user: str
        :param connect_address: 实例连接IP地址（RABBITMQ触发器参数）。
        :type connect_address: str
        :param exchange_name: 交换机名称（RABBITMQ触发器参数）。
        :type exchange_name: str
        :param vhost: 虚拟机名称（RABBITMQ触发器参数）。
        :type vhost: str
        :param ssl_enable: RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。
        :type ssl_enable: bool
        """
        
        

        self._name = None
        self._schedule_type = None
        self._schedule = None
        self._user_event = None
        self._triggerid = None
        self._type = None
        self._path = None
        self._protocol = None
        self._req_method = None
        self._group_id = None
        self._group_name = None
        self._match_mode = None
        self._env_name = None
        self._env_id = None
        self._api_id = None
        self._api_name = None
        self._auth = None
        self._invoke_url = None
        self._func_info = None
        self._sl_domain = None
        self._backend_type = None
        self._instance_id = None
        self._roma_app_id = None
        self._operations = None
        self._collection_name = None
        self._db_name = None
        self._db_password = None
        self._db_user = None
        self._instance_addrs = None
        self._mode = None
        self._batch_size = None
        self._queue_id = None
        self._consumer_group_id = None
        self._polling_interval = None
        self._stream_name = None
        self._sharditerator_type = None
        self._polling_unit = None
        self._max_fetch_bytes = None
        self._is_serial = None
        self._log_group_id = None
        self._log_topic_id = None
        self._bucket = None
        self._prefix = None
        self._suffix = None
        self._events = None
        self._topic_urn = None
        self._topic_ids = None
        self._kafka_user = None
        self._kafka_password = None
        self._kafka_connect_address = None
        self._kafka_ssl_enable = None
        self._access_password = None
        self._access_user = None
        self._connect_address = None
        self._exchange_name = None
        self._vhost = None
        self._ssl_enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule is not None:
            self.schedule = schedule
        if user_event is not None:
            self.user_event = user_event
        if triggerid is not None:
            self.triggerid = triggerid
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if protocol is not None:
            self.protocol = protocol
        if req_method is not None:
            self.req_method = req_method
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if match_mode is not None:
            self.match_mode = match_mode
        if env_name is not None:
            self.env_name = env_name
        if env_id is not None:
            self.env_id = env_id
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if auth is not None:
            self.auth = auth
        if invoke_url is not None:
            self.invoke_url = invoke_url
        if func_info is not None:
            self.func_info = func_info
        if sl_domain is not None:
            self.sl_domain = sl_domain
        if backend_type is not None:
            self.backend_type = backend_type
        if instance_id is not None:
            self.instance_id = instance_id
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if operations is not None:
            self.operations = operations
        if collection_name is not None:
            self.collection_name = collection_name
        if db_name is not None:
            self.db_name = db_name
        if db_password is not None:
            self.db_password = db_password
        if db_user is not None:
            self.db_user = db_user
        if instance_addrs is not None:
            self.instance_addrs = instance_addrs
        if mode is not None:
            self.mode = mode
        if batch_size is not None:
            self.batch_size = batch_size
        if queue_id is not None:
            self.queue_id = queue_id
        if consumer_group_id is not None:
            self.consumer_group_id = consumer_group_id
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if stream_name is not None:
            self.stream_name = stream_name
        if sharditerator_type is not None:
            self.sharditerator_type = sharditerator_type
        if polling_unit is not None:
            self.polling_unit = polling_unit
        if max_fetch_bytes is not None:
            self.max_fetch_bytes = max_fetch_bytes
        if is_serial is not None:
            self.is_serial = is_serial
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id
        if bucket is not None:
            self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
        if events is not None:
            self.events = events
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if topic_ids is not None:
            self.topic_ids = topic_ids
        if kafka_user is not None:
            self.kafka_user = kafka_user
        if kafka_password is not None:
            self.kafka_password = kafka_password
        if kafka_connect_address is not None:
            self.kafka_connect_address = kafka_connect_address
        if kafka_ssl_enable is not None:
            self.kafka_ssl_enable = kafka_ssl_enable
        if access_password is not None:
            self.access_password = access_password
        if access_user is not None:
            self.access_user = access_user
        if connect_address is not None:
            self.connect_address = connect_address
        if exchange_name is not None:
            self.exchange_name = exchange_name
        if vhost is not None:
            self.vhost = vhost
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable

    @property
    def name(self):
        """Gets the name of this TriggerEventDataResponseBody.

        触发器名称

        :return: The name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TriggerEventDataResponseBody.

        触发器名称

        :param name: The name of this TriggerEventDataResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def schedule_type(self):
        """Gets the schedule_type of this TriggerEventDataResponseBody.

        定时触发类型（TIMER触发器参数）。 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数

        :return: The schedule_type of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this TriggerEventDataResponseBody.

        定时触发类型（TIMER触发器参数）。 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数

        :param schedule_type: The schedule_type of this TriggerEventDataResponseBody.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule(self):
        """Gets the schedule of this TriggerEventDataResponseBody.

        定时触发规则（TIMER触发器参数）。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式

        :return: The schedule of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this TriggerEventDataResponseBody.

        定时触发规则（TIMER触发器参数）。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式

        :param schedule: The schedule of this TriggerEventDataResponseBody.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def user_event(self):
        """Gets the user_event of this TriggerEventDataResponseBody.

        附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\"version\": \"v1.0\",   \"time\": \"2018-06-01T08:30:00+08:00\",   \"trigger_type\": \"TIMER\",   \"trigger_name\": \"Timer_001\",   \"user_event\": \"您输入的附加信息\"}

        :return: The user_event of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._user_event

    @user_event.setter
    def user_event(self, user_event):
        """Sets the user_event of this TriggerEventDataResponseBody.

        附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\"version\": \"v1.0\",   \"time\": \"2018-06-01T08:30:00+08:00\",   \"trigger_type\": \"TIMER\",   \"trigger_name\": \"Timer_001\",   \"user_event\": \"您输入的附加信息\"}

        :param user_event: The user_event of this TriggerEventDataResponseBody.
        :type user_event: str
        """
        self._user_event = user_event

    @property
    def triggerid(self):
        """Gets the triggerid of this TriggerEventDataResponseBody.

        APIG触发器id。（APIG触发器参数）

        :return: The triggerid of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._triggerid

    @triggerid.setter
    def triggerid(self, triggerid):
        """Sets the triggerid of this TriggerEventDataResponseBody.

        APIG触发器id。（APIG触发器参数）

        :param triggerid: The triggerid of this TriggerEventDataResponseBody.
        :type triggerid: str
        """
        self._triggerid = triggerid

    @property
    def type(self):
        """Gets the type of this TriggerEventDataResponseBody.

        API接口类型（APIG触发器参数）。 - 1：公有API - 2：私有API

        :return: The type of this TriggerEventDataResponseBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TriggerEventDataResponseBody.

        API接口类型（APIG触发器参数）。 - 1：公有API - 2：私有API

        :param type: The type of this TriggerEventDataResponseBody.
        :type type: int
        """
        self._type = type

    @property
    def path(self):
        """Gets the path of this TriggerEventDataResponseBody.

        APIG接口PATH路径（APIG触发器参数）。

        :return: The path of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TriggerEventDataResponseBody.

        APIG接口PATH路径（APIG触发器参数）。

        :param path: The path of this TriggerEventDataResponseBody.
        :type path: str
        """
        self._path = path

    @property
    def protocol(self):
        """Gets the protocol of this TriggerEventDataResponseBody.

        API的请求协议（APIG触发器参数）。

        :return: The protocol of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TriggerEventDataResponseBody.

        API的请求协议（APIG触发器参数）。

        :param protocol: The protocol of this TriggerEventDataResponseBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def req_method(self):
        """Gets the req_method of this TriggerEventDataResponseBody.

        API的请求方式（APIG触发器参数）。

        :return: The req_method of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this TriggerEventDataResponseBody.

        API的请求方式（APIG触发器参数）。

        :param req_method: The req_method of this TriggerEventDataResponseBody.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def group_id(self):
        """Gets the group_id of this TriggerEventDataResponseBody.

        API所属的分组编号（APIG触发器参数）。

        :return: The group_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TriggerEventDataResponseBody.

        API所属的分组编号（APIG触发器参数）。

        :param group_id: The group_id of this TriggerEventDataResponseBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this TriggerEventDataResponseBody.

        API所属的分组名称（APIG触发器参数）。

        :return: The group_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this TriggerEventDataResponseBody.

        API所属的分组名称（APIG触发器参数）。

        :param group_name: The group_name of this TriggerEventDataResponseBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def match_mode(self):
        """Gets the match_mode of this TriggerEventDataResponseBody.

        API的匹配方式（APIG触发器参数）。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）

        :return: The match_mode of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this TriggerEventDataResponseBody.

        API的匹配方式（APIG触发器参数）。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）

        :param match_mode: The match_mode of this TriggerEventDataResponseBody.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def env_name(self):
        """Gets the env_name of this TriggerEventDataResponseBody.

        API的发布环境（APIG触发器参数）。

        :return: The env_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this TriggerEventDataResponseBody.

        API的发布环境（APIG触发器参数）。

        :param env_name: The env_name of this TriggerEventDataResponseBody.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_id(self):
        """Gets the env_id of this TriggerEventDataResponseBody.

        API的发布环境id（APIG触发器参数）。

        :return: The env_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TriggerEventDataResponseBody.

        API的发布环境id（APIG触发器参数）。

        :param env_id: The env_id of this TriggerEventDataResponseBody.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def api_id(self):
        """Gets the api_id of this TriggerEventDataResponseBody.

        API编号（APIG触发器参数）。

        :return: The api_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this TriggerEventDataResponseBody.

        API编号（APIG触发器参数）。

        :param api_id: The api_id of this TriggerEventDataResponseBody.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this TriggerEventDataResponseBody.

        API名称（APIG触发器参数）。

        :return: The api_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this TriggerEventDataResponseBody.

        API名称（APIG触发器参数）。

        :param api_name: The api_name of this TriggerEventDataResponseBody.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def auth(self):
        """Gets the auth of this TriggerEventDataResponseBody.

        API的认证方式（APIG触发器参数）。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用

        :return: The auth of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this TriggerEventDataResponseBody.

        API的认证方式（APIG触发器参数）。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用

        :param auth: The auth of this TriggerEventDataResponseBody.
        :type auth: str
        """
        self._auth = auth

    @property
    def invoke_url(self):
        """Gets the invoke_url of this TriggerEventDataResponseBody.

        API调用地址（APIG触发器参数）。

        :return: The invoke_url of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._invoke_url

    @invoke_url.setter
    def invoke_url(self, invoke_url):
        """Sets the invoke_url of this TriggerEventDataResponseBody.

        API调用地址（APIG触发器参数）。

        :param invoke_url: The invoke_url of this TriggerEventDataResponseBody.
        :type invoke_url: str
        """
        self._invoke_url = invoke_url

    @property
    def func_info(self):
        """Gets the func_info of this TriggerEventDataResponseBody.

        :return: The func_info of this TriggerEventDataResponseBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        """
        return self._func_info

    @func_info.setter
    def func_info(self, func_info):
        """Sets the func_info of this TriggerEventDataResponseBody.

        :param func_info: The func_info of this TriggerEventDataResponseBody.
        :type func_info: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        """
        self._func_info = func_info

    @property
    def sl_domain(self):
        """Gets the sl_domain of this TriggerEventDataResponseBody.

        APIG系统默认分配的子域名（APIG触发器参数）。

        :return: The sl_domain of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        """Sets the sl_domain of this TriggerEventDataResponseBody.

        APIG系统默认分配的子域名（APIG触发器参数）。

        :param sl_domain: The sl_domain of this TriggerEventDataResponseBody.
        :type sl_domain: str
        """
        self._sl_domain = sl_domain

    @property
    def backend_type(self):
        """Gets the backend_type of this TriggerEventDataResponseBody.

        API的后端类型（APIG触发器参数）。

        :return: The backend_type of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """Sets the backend_type of this TriggerEventDataResponseBody.

        API的后端类型（APIG触发器参数）。

        :param backend_type: The backend_type of this TriggerEventDataResponseBody.
        :type backend_type: str
        """
        self._backend_type = backend_type

    @property
    def instance_id(self):
        """Gets the instance_id of this TriggerEventDataResponseBody.

        实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id

        :return: The instance_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this TriggerEventDataResponseBody.

        实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id

        :param instance_id: The instance_id of this TriggerEventDataResponseBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this TriggerEventDataResponseBody.

        API归属的集成应用编号。（APIG触发器参数）

        :return: The roma_app_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this TriggerEventDataResponseBody.

        API归属的集成应用编号。（APIG触发器参数）

        :param roma_app_id: The roma_app_id of this TriggerEventDataResponseBody.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def operations(self):
        """Gets the operations of this TriggerEventDataResponseBody.

        自定义操作（CTS触发器参数）。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。

        :return: The operations of this TriggerEventDataResponseBody.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this TriggerEventDataResponseBody.

        自定义操作（CTS触发器参数）。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。

        :param operations: The operations of this TriggerEventDataResponseBody.
        :type operations: list[str]
        """
        self._operations = operations

    @property
    def collection_name(self):
        """Gets the collection_name of this TriggerEventDataResponseBody.

        集合名称（DDS触发器参数）。

        :return: The collection_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """Sets the collection_name of this TriggerEventDataResponseBody.

        集合名称（DDS触发器参数）。

        :param collection_name: The collection_name of this TriggerEventDataResponseBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def db_name(self):
        """Gets the db_name of this TriggerEventDataResponseBody.

        文档数据库名称（DDS触发器参数）。

        :return: The db_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this TriggerEventDataResponseBody.

        文档数据库名称（DDS触发器参数）。

        :param db_name: The db_name of this TriggerEventDataResponseBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_password(self):
        """Gets the db_password of this TriggerEventDataResponseBody.

        文档数据库密码（DDS触发器参数）。

        :return: The db_password of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this TriggerEventDataResponseBody.

        文档数据库密码（DDS触发器参数）。

        :param db_password: The db_password of this TriggerEventDataResponseBody.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def db_user(self):
        """Gets the db_user of this TriggerEventDataResponseBody.

        文档数据库用户名（DDS触发器参数）。

        :return: The db_user of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this TriggerEventDataResponseBody.

        文档数据库用户名（DDS触发器参数）。

        :param db_user: The db_user of this TriggerEventDataResponseBody.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def instance_addrs(self):
        """Gets the instance_addrs of this TriggerEventDataResponseBody.

        文档数据库实例地址（DDS触发器参数）。

        :return: The instance_addrs of this TriggerEventDataResponseBody.
        :rtype: list[str]
        """
        return self._instance_addrs

    @instance_addrs.setter
    def instance_addrs(self, instance_addrs):
        """Sets the instance_addrs of this TriggerEventDataResponseBody.

        文档数据库实例地址（DDS触发器参数）。

        :param instance_addrs: The instance_addrs of this TriggerEventDataResponseBody.
        :type instance_addrs: list[str]
        """
        self._instance_addrs = instance_addrs

    @property
    def mode(self):
        """Gets the mode of this TriggerEventDataResponseBody.

        文档数据库实例类型（DDS触发器参数）。 - Sharding：集群实例 - ReplicaSet：副本集实例 - Single：单节点实例

        :return: The mode of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TriggerEventDataResponseBody.

        文档数据库实例类型（DDS触发器参数）。 - Sharding：集群实例 - ReplicaSet：副本集实例 - Single：单节点实例

        :param mode: The mode of this TriggerEventDataResponseBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def batch_size(self):
        """Gets the batch_size of this TriggerEventDataResponseBody.

        批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内

        :return: The batch_size of this TriggerEventDataResponseBody.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this TriggerEventDataResponseBody.

        批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内

        :param batch_size: The batch_size of this TriggerEventDataResponseBody.
        :type batch_size: int
        """
        self._batch_size = batch_size

    @property
    def queue_id(self):
        """Gets the queue_id of this TriggerEventDataResponseBody.

        队列id（DMS触发器参数）。

        :return: The queue_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this TriggerEventDataResponseBody.

        队列id（DMS触发器参数）。

        :param queue_id: The queue_id of this TriggerEventDataResponseBody.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def consumer_group_id(self):
        """Gets the consumer_group_id of this TriggerEventDataResponseBody.

        消费组id（DMS触发器参数）。

        :return: The consumer_group_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._consumer_group_id

    @consumer_group_id.setter
    def consumer_group_id(self, consumer_group_id):
        """Sets the consumer_group_id of this TriggerEventDataResponseBody.

        消费组id（DMS触发器参数）。

        :param consumer_group_id: The consumer_group_id of this TriggerEventDataResponseBody.
        :type consumer_group_id: str
        """
        self._consumer_group_id = consumer_group_id

    @property
    def polling_interval(self):
        """Gets the polling_interval of this TriggerEventDataResponseBody.

        拉取周期。

        :return: The polling_interval of this TriggerEventDataResponseBody.
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this TriggerEventDataResponseBody.

        拉取周期。

        :param polling_interval: The polling_interval of this TriggerEventDataResponseBody.
        :type polling_interval: int
        """
        self._polling_interval = polling_interval

    @property
    def stream_name(self):
        """Gets the stream_name of this TriggerEventDataResponseBody.

        通道名称（DIS触发器参数）。

        :return: The stream_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this TriggerEventDataResponseBody.

        通道名称（DIS触发器参数）。

        :param stream_name: The stream_name of this TriggerEventDataResponseBody.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def sharditerator_type(self):
        """Gets the sharditerator_type of this TriggerEventDataResponseBody.

        起始位置（DIS触发器参数）。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。

        :return: The sharditerator_type of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._sharditerator_type

    @sharditerator_type.setter
    def sharditerator_type(self, sharditerator_type):
        """Sets the sharditerator_type of this TriggerEventDataResponseBody.

        起始位置（DIS触发器参数）。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。

        :param sharditerator_type: The sharditerator_type of this TriggerEventDataResponseBody.
        :type sharditerator_type: str
        """
        self._sharditerator_type = sharditerator_type

    @property
    def polling_unit(self):
        """Gets the polling_unit of this TriggerEventDataResponseBody.

        拉取周期单位（DIS触发器参数）。 - s：秒 - ms：毫秒

        :return: The polling_unit of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._polling_unit

    @polling_unit.setter
    def polling_unit(self, polling_unit):
        """Sets the polling_unit of this TriggerEventDataResponseBody.

        拉取周期单位（DIS触发器参数）。 - s：秒 - ms：毫秒

        :param polling_unit: The polling_unit of this TriggerEventDataResponseBody.
        :type polling_unit: str
        """
        self._polling_unit = polling_unit

    @property
    def max_fetch_bytes(self):
        """Gets the max_fetch_bytes of this TriggerEventDataResponseBody.

        最大提取字节数（DIS触发器参数）。

        :return: The max_fetch_bytes of this TriggerEventDataResponseBody.
        :rtype: int
        """
        return self._max_fetch_bytes

    @max_fetch_bytes.setter
    def max_fetch_bytes(self, max_fetch_bytes):
        """Sets the max_fetch_bytes of this TriggerEventDataResponseBody.

        最大提取字节数（DIS触发器参数）。

        :param max_fetch_bytes: The max_fetch_bytes of this TriggerEventDataResponseBody.
        :type max_fetch_bytes: int
        """
        self._max_fetch_bytes = max_fetch_bytes

    @property
    def is_serial(self):
        """Gets the is_serial of this TriggerEventDataResponseBody.

        串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。

        :return: The is_serial of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._is_serial

    @is_serial.setter
    def is_serial(self, is_serial):
        """Sets the is_serial of this TriggerEventDataResponseBody.

        串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。

        :param is_serial: The is_serial of this TriggerEventDataResponseBody.
        :type is_serial: str
        """
        self._is_serial = is_serial

    @property
    def log_group_id(self):
        """Gets the log_group_id of this TriggerEventDataResponseBody.

        日志组id（LTS触发器参数）。

        :return: The log_group_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this TriggerEventDataResponseBody.

        日志组id（LTS触发器参数）。

        :param log_group_id: The log_group_id of this TriggerEventDataResponseBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this TriggerEventDataResponseBody.

        日志流id（LTS触发器参数）。

        :return: The log_topic_id of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this TriggerEventDataResponseBody.

        日志流id（LTS触发器参数）。

        :param log_topic_id: The log_topic_id of this TriggerEventDataResponseBody.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def bucket(self):
        """Gets the bucket of this TriggerEventDataResponseBody.

        桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。

        :return: The bucket of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TriggerEventDataResponseBody.

        桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。

        :param bucket: The bucket of this TriggerEventDataResponseBody.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this TriggerEventDataResponseBody.

        前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。

        :return: The prefix of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this TriggerEventDataResponseBody.

        前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。

        :param prefix: The prefix of this TriggerEventDataResponseBody.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this TriggerEventDataResponseBody.

        后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知

        :return: The suffix of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this TriggerEventDataResponseBody.

        后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知

        :param suffix: The suffix of this TriggerEventDataResponseBody.
        :type suffix: str
        """
        self._suffix = suffix

    @property
    def events(self):
        """Gets the events of this TriggerEventDataResponseBody.

        触发事件（OBS触发器参数）。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象

        :return: The events of this TriggerEventDataResponseBody.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this TriggerEventDataResponseBody.

        触发事件（OBS触发器参数）。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象

        :param events: The events of this TriggerEventDataResponseBody.
        :type events: list[str]
        """
        self._events = events

    @property
    def topic_urn(self):
        """Gets the topic_urn of this TriggerEventDataResponseBody.

        主题URN（SMN触发器参数）。

        :return: The topic_urn of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this TriggerEventDataResponseBody.

        主题URN（SMN触发器参数）。

        :param topic_urn: The topic_urn of this TriggerEventDataResponseBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def topic_ids(self):
        """Gets the topic_ids of this TriggerEventDataResponseBody.

        KAFKA主题id列表（KAFKA触发器参数）。

        :return: The topic_ids of this TriggerEventDataResponseBody.
        :rtype: list[str]
        """
        return self._topic_ids

    @topic_ids.setter
    def topic_ids(self, topic_ids):
        """Sets the topic_ids of this TriggerEventDataResponseBody.

        KAFKA主题id列表（KAFKA触发器参数）。

        :param topic_ids: The topic_ids of this TriggerEventDataResponseBody.
        :type topic_ids: list[str]
        """
        self._topic_ids = topic_ids

    @property
    def kafka_user(self):
        """Gets the kafka_user of this TriggerEventDataResponseBody.

        KAFKA账户名（KAFKA触发器参数）。

        :return: The kafka_user of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._kafka_user

    @kafka_user.setter
    def kafka_user(self, kafka_user):
        """Sets the kafka_user of this TriggerEventDataResponseBody.

        KAFKA账户名（KAFKA触发器参数）。

        :param kafka_user: The kafka_user of this TriggerEventDataResponseBody.
        :type kafka_user: str
        """
        self._kafka_user = kafka_user

    @property
    def kafka_password(self):
        """Gets the kafka_password of this TriggerEventDataResponseBody.

        KAFKA账户密码（KAFKA触发器参数）。

        :return: The kafka_password of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._kafka_password

    @kafka_password.setter
    def kafka_password(self, kafka_password):
        """Sets the kafka_password of this TriggerEventDataResponseBody.

        KAFKA账户密码（KAFKA触发器参数）。

        :param kafka_password: The kafka_password of this TriggerEventDataResponseBody.
        :type kafka_password: str
        """
        self._kafka_password = kafka_password

    @property
    def kafka_connect_address(self):
        """Gets the kafka_connect_address of this TriggerEventDataResponseBody.

        KAFKA实例连接IP地址（KAFKA触发器参数）。

        :return: The kafka_connect_address of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._kafka_connect_address

    @kafka_connect_address.setter
    def kafka_connect_address(self, kafka_connect_address):
        """Sets the kafka_connect_address of this TriggerEventDataResponseBody.

        KAFKA实例连接IP地址（KAFKA触发器参数）。

        :param kafka_connect_address: The kafka_connect_address of this TriggerEventDataResponseBody.
        :type kafka_connect_address: str
        """
        self._kafka_connect_address = kafka_connect_address

    @property
    def kafka_ssl_enable(self):
        """Gets the kafka_ssl_enable of this TriggerEventDataResponseBody.

        KAFKA连接是否开启安全认证（KAFKA触发器参数）。

        :return: The kafka_ssl_enable of this TriggerEventDataResponseBody.
        :rtype: bool
        """
        return self._kafka_ssl_enable

    @kafka_ssl_enable.setter
    def kafka_ssl_enable(self, kafka_ssl_enable):
        """Sets the kafka_ssl_enable of this TriggerEventDataResponseBody.

        KAFKA连接是否开启安全认证（KAFKA触发器参数）。

        :param kafka_ssl_enable: The kafka_ssl_enable of this TriggerEventDataResponseBody.
        :type kafka_ssl_enable: bool
        """
        self._kafka_ssl_enable = kafka_ssl_enable

    @property
    def access_password(self):
        """Gets the access_password of this TriggerEventDataResponseBody.

        RABBITMQ账户密码（RABBITMQ触发器参数）。

        :return: The access_password of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._access_password

    @access_password.setter
    def access_password(self, access_password):
        """Sets the access_password of this TriggerEventDataResponseBody.

        RABBITMQ账户密码（RABBITMQ触发器参数）。

        :param access_password: The access_password of this TriggerEventDataResponseBody.
        :type access_password: str
        """
        self._access_password = access_password

    @property
    def access_user(self):
        """Gets the access_user of this TriggerEventDataResponseBody.

        RABBITMQ账户名（RABBITMQ触发器参数）。

        :return: The access_user of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this TriggerEventDataResponseBody.

        RABBITMQ账户名（RABBITMQ触发器参数）。

        :param access_user: The access_user of this TriggerEventDataResponseBody.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def connect_address(self):
        """Gets the connect_address of this TriggerEventDataResponseBody.

        实例连接IP地址（RABBITMQ触发器参数）。

        :return: The connect_address of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        """Sets the connect_address of this TriggerEventDataResponseBody.

        实例连接IP地址（RABBITMQ触发器参数）。

        :param connect_address: The connect_address of this TriggerEventDataResponseBody.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def exchange_name(self):
        """Gets the exchange_name of this TriggerEventDataResponseBody.

        交换机名称（RABBITMQ触发器参数）。

        :return: The exchange_name of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this TriggerEventDataResponseBody.

        交换机名称（RABBITMQ触发器参数）。

        :param exchange_name: The exchange_name of this TriggerEventDataResponseBody.
        :type exchange_name: str
        """
        self._exchange_name = exchange_name

    @property
    def vhost(self):
        """Gets the vhost of this TriggerEventDataResponseBody.

        虚拟机名称（RABBITMQ触发器参数）。

        :return: The vhost of this TriggerEventDataResponseBody.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        """Sets the vhost of this TriggerEventDataResponseBody.

        虚拟机名称（RABBITMQ触发器参数）。

        :param vhost: The vhost of this TriggerEventDataResponseBody.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this TriggerEventDataResponseBody.

        RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。

        :return: The ssl_enable of this TriggerEventDataResponseBody.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this TriggerEventDataResponseBody.

        RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。

        :param ssl_enable: The ssl_enable of this TriggerEventDataResponseBody.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TriggerEventDataResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
