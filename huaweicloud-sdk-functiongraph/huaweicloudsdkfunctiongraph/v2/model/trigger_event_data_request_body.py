# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerEventDataRequestBody:

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
        'type': 'int',
        'path': 'str',
        'protocol': 'str',
        'req_method': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'match_mode': 'str',
        'env_name': 'str',
        'env_id': 'str',
        'auth': 'str',
        'func_info': 'ApigTriggerFuncInfo',
        'sl_domain': 'str',
        'backend_type': 'str',
        'operations': 'list[str]',
        'instance_id': 'str',
        'collection_name': 'str',
        'db_name': 'str',
        'db_password': 'str',
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
        'ssl_enable': 'bool',
        'key_encode': 'bool',
        'agency': 'str',
        'channel_name': 'str',
        'channel_id': 'str',
        'source_name': 'str',
        'created_time': 'datetime',
        'status': 'str',
        'trigger_name': 'str',
        'event_types': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'schedule_type': 'schedule_type',
        'schedule': 'schedule',
        'user_event': 'user_event',
        'type': 'type',
        'path': 'path',
        'protocol': 'protocol',
        'req_method': 'req_method',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'match_mode': 'match_mode',
        'env_name': 'env_name',
        'env_id': 'env_id',
        'auth': 'auth',
        'func_info': 'func_info',
        'sl_domain': 'sl_domain',
        'backend_type': 'backend_type',
        'operations': 'operations',
        'instance_id': 'instance_id',
        'collection_name': 'collection_name',
        'db_name': 'db_name',
        'db_password': 'db_password',
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
        'ssl_enable': 'ssl_enable',
        'key_encode': 'Key_encode',
        'agency': 'agency',
        'channel_name': 'channel_name',
        'channel_id': 'channel_id',
        'source_name': 'source_name',
        'created_time': 'created_time',
        'status': 'status',
        'trigger_name': 'trigger_name',
        'event_types': 'event_types'
    }

    def __init__(self, name=None, schedule_type=None, schedule=None, user_event=None, type=None, path=None, protocol=None, req_method=None, group_id=None, group_name=None, match_mode=None, env_name=None, env_id=None, auth=None, func_info=None, sl_domain=None, backend_type=None, operations=None, instance_id=None, collection_name=None, db_name=None, db_password=None, batch_size=None, queue_id=None, consumer_group_id=None, polling_interval=None, stream_name=None, sharditerator_type=None, polling_unit=None, max_fetch_bytes=None, is_serial=None, log_group_id=None, log_topic_id=None, bucket=None, prefix=None, suffix=None, events=None, topic_urn=None, topic_ids=None, kafka_user=None, kafka_password=None, kafka_connect_address=None, kafka_ssl_enable=None, access_password=None, access_user=None, connect_address=None, exchange_name=None, vhost=None, ssl_enable=None, key_encode=None, agency=None, channel_name=None, channel_id=None, source_name=None, created_time=None, status=None, trigger_name=None, event_types=None):
        r"""TriggerEventDataRequestBody

        The model defined in huaweicloud sdk

        :param name: - TIMER触发器：触发器名称 - APIG触发器：API名称 - CTS触发器：通知名称 - OBS触发器：事件通知名称，默认值为触发器id
        :type name: str
        :param schedule_type: 定时触发类型（TIMER触发器参数）。TIMER触发器此参数必填 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数
        :type schedule_type: str
        :param schedule: 定时触发规则（TIMER触发器参数）。TIMER触发器此参数必填。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式
        :type schedule: str
        :param user_event: 附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\&quot;version\&quot;: \&quot;v1.0\&quot;,   \&quot;time\&quot;: \&quot;2018-06-01T08:30:00+08:00\&quot;,   \&quot;trigger_type\&quot;: \&quot;TIMER\&quot;,   \&quot;trigger_name\&quot;: \&quot;Timer_001\&quot;,   \&quot;user_event\&quot;: \&quot;您输入的附加信息\&quot;}
        :type user_event: str
        :param type: API接口类型（APIG触发器参数）。APIG触发器此参数必填。 - 1：公有API - 2：私有API
        :type type: int
        :param path: APIG接口PATH路径（APIG触发器参数）。APIG触发器此参数必填。
        :type path: str
        :param protocol: API的请求协议（APIG触发器参数）。APIG触发器此参数必填。
        :type protocol: str
        :param req_method: API的请求方式（APIG触发器参数）。APIG触发器此参数必填。
        :type req_method: str
        :param group_id: API所属的分组编号（APIG触发器参数）。APIG触发器此参数必填。
        :type group_id: str
        :param group_name: API所属的分组名称
        :type group_name: str
        :param match_mode: API的匹配方式（APIG触发器参数）。APIG触发器此参数必填。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）
        :type match_mode: str
        :param env_name: API的发布环境（APIG触发器参数）。APIG触发器此参数必填。
        :type env_name: str
        :param env_id: API的发布环境id（APIG触发器参数）。APIG触发器此参数必填。
        :type env_id: str
        :param auth: API的认证方式（APIG触发器参数）。APIG触发器此参数必填。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&amp;Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用
        :type auth: str
        :param func_info: 
        :type func_info: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        :param sl_domain: APIG系统默认分配的子域名（APIG触发器参数）。
        :type sl_domain: str
        :param backend_type: API的后端类型（APIG触发器参数）。
        :type backend_type: str
        :param operations: 自定义操作（CTS触发器参数）。CTS触发器此参数必填。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。
        :type operations: list[str]
        :param instance_id: 实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id
        :type instance_id: str
        :param collection_name: 集合名称（DDS触发器参数）。DDS触发器此参数必填。
        :type collection_name: str
        :param db_name: 文档数据库名称（DDS触发器参数）。DDS触发器此参数必填。
        :type db_name: str
        :param db_password: 文档数据库密码（DDS触发器参数）。DDS触发器此参数必填。
        :type db_password: str
        :param batch_size: 批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内
        :type batch_size: int
        :param queue_id: 队列id（DMS触发器参数）。DMS触发器此参数必填。
        :type queue_id: str
        :param consumer_group_id: 消费组id（DMS触发器参数）。DMS触发器此参数必填。
        :type consumer_group_id: str
        :param polling_interval: 拉取周期。DIS、DMS触发器此参数必填。
        :type polling_interval: int
        :param stream_name: 通道名称（DIS触发器参数）。DIS触发器此参数必填。
        :type stream_name: str
        :param sharditerator_type: 起始位置（DIS触发器参数）。DIS触发器此参数必填。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。
        :type sharditerator_type: str
        :param polling_unit: 拉取周期单位（DIS触发器参数）。DIS触发器此参数必填。 - s：秒 - ms：毫秒
        :type polling_unit: str
        :param max_fetch_bytes: 最大提取字节数（DIS触发器参数）。
        :type max_fetch_bytes: int
        :param is_serial: 串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。DIS触发器此参数必填。
        :type is_serial: str
        :param log_group_id: 日志组id（LTS触发器参数）。LTS触发器此参数必填。
        :type log_group_id: str
        :param log_topic_id: 日志流id（LTS触发器参数）。LTS触发器此参数必填。
        :type log_topic_id: str
        :param bucket: 桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。OBS触发器此参数必填。
        :type bucket: str
        :param prefix: 前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。
        :type prefix: str
        :param suffix: 后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知
        :type suffix: str
        :param events: 触发事件（OBS触发器参数）。OBS触发器此参数必填。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象
        :type events: list[str]
        :param topic_urn: 主题URN（SMN触发器参数）。SMN触发器此参数必填。
        :type topic_urn: str
        :param topic_ids: KAFKA主题id列表（KAFKA触发器参数）。KAFKA触发器此参数必填。
        :type topic_ids: list[str]
        :param kafka_user: KAFKA账户名（KAFKA触发器参数）。
        :type kafka_user: str
        :param kafka_password: KAFKA账户密码（KAFKA触发器参数）。
        :type kafka_password: str
        :param kafka_connect_address: KAFKA实例连接IP地址（KAFKA触发器参数）。
        :type kafka_connect_address: str
        :param kafka_ssl_enable: KAFKA连接是否开启安全认证（KAFKA触发器参数）。
        :type kafka_ssl_enable: bool
        :param access_password: RABBITMQ账户密码（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。
        :type access_password: str
        :param access_user: RABBITMQ账户名（RABBITMQ触发器参数）。
        :type access_user: str
        :param connect_address: 实例连接IP地址（RABBITMQ触发器参数）。
        :type connect_address: str
        :param exchange_name: 交换机名称（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。
        :type exchange_name: str
        :param vhost: 虚拟机名称（RABBITMQ触发器参数）。
        :type vhost: str
        :param ssl_enable: RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。
        :type ssl_enable: bool
        :param key_encode: EG obs触发器是否对对象加密（EVENTGRID触发器参数）。
        :type key_encode: bool
        :param agency: 使用的代理（EVENTGRID触发器参数）。
        :type agency: str
        :param channel_name: 通道名称（EVENTGRID触发器参数）。
        :type channel_name: str
        :param channel_id: 通道id（EVENTGRID触发器参数）。
        :type channel_id: str
        :param source_name: 事件源名称（EVENTGRID触发器参数）。
        :type source_name: str
        :param created_time: 创建时间（EVENTGRID触发器参数）。
        :type created_time: datetime
        :param status: 触发器状态（EVENTGRID触发器参数）。
        :type status: str
        :param trigger_name: 触发器名称（EVENTGRID触发器参数）。
        :type trigger_name: str
        :param event_types: 事件类型（EVENTGRID触发器参数）。
        :type event_types: list[str]
        """
        
        

        self._name = None
        self._schedule_type = None
        self._schedule = None
        self._user_event = None
        self._type = None
        self._path = None
        self._protocol = None
        self._req_method = None
        self._group_id = None
        self._group_name = None
        self._match_mode = None
        self._env_name = None
        self._env_id = None
        self._auth = None
        self._func_info = None
        self._sl_domain = None
        self._backend_type = None
        self._operations = None
        self._instance_id = None
        self._collection_name = None
        self._db_name = None
        self._db_password = None
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
        self._key_encode = None
        self._agency = None
        self._channel_name = None
        self._channel_id = None
        self._source_name = None
        self._created_time = None
        self._status = None
        self._trigger_name = None
        self._event_types = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule is not None:
            self.schedule = schedule
        if user_event is not None:
            self.user_event = user_event
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
        if auth is not None:
            self.auth = auth
        if func_info is not None:
            self.func_info = func_info
        if sl_domain is not None:
            self.sl_domain = sl_domain
        if backend_type is not None:
            self.backend_type = backend_type
        if operations is not None:
            self.operations = operations
        if instance_id is not None:
            self.instance_id = instance_id
        if collection_name is not None:
            self.collection_name = collection_name
        if db_name is not None:
            self.db_name = db_name
        if db_password is not None:
            self.db_password = db_password
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
        if key_encode is not None:
            self.key_encode = key_encode
        if agency is not None:
            self.agency = agency
        if channel_name is not None:
            self.channel_name = channel_name
        if channel_id is not None:
            self.channel_id = channel_id
        if source_name is not None:
            self.source_name = source_name
        if created_time is not None:
            self.created_time = created_time
        if status is not None:
            self.status = status
        if trigger_name is not None:
            self.trigger_name = trigger_name
        if event_types is not None:
            self.event_types = event_types

    @property
    def name(self):
        r"""Gets the name of this TriggerEventDataRequestBody.

        - TIMER触发器：触发器名称 - APIG触发器：API名称 - CTS触发器：通知名称 - OBS触发器：事件通知名称，默认值为触发器id

        :return: The name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TriggerEventDataRequestBody.

        - TIMER触发器：触发器名称 - APIG触发器：API名称 - CTS触发器：通知名称 - OBS触发器：事件通知名称，默认值为触发器id

        :param name: The name of this TriggerEventDataRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this TriggerEventDataRequestBody.

        定时触发类型（TIMER触发器参数）。TIMER触发器此参数必填 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数

        :return: The schedule_type of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this TriggerEventDataRequestBody.

        定时触发类型（TIMER触发器参数）。TIMER触发器此参数必填 - Rate：指定固定频率（分钟、小时、天数）定期调用函数，单位为分钟时，输入值不能超过60；单位为小时时，输入值不能超过24；单位为天时，输入值不能超过30。 - Cron：指定Cron表达式定期调用函数

        :param schedule_type: The schedule_type of this TriggerEventDataRequestBody.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule(self):
        r"""Gets the schedule of this TriggerEventDataRequestBody.

        定时触发规则（TIMER触发器参数）。TIMER触发器此参数必填。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式

        :return: The schedule of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this TriggerEventDataRequestBody.

        定时触发规则（TIMER触发器参数）。TIMER触发器此参数必填。 - 触发类型为Rate时对应定时规则 - 触发类型为Cron时对应Cron表达式

        :param schedule: The schedule of this TriggerEventDataRequestBody.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def user_event(self):
        r"""Gets the user_event of this TriggerEventDataRequestBody.

        附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\"version\": \"v1.0\",   \"time\": \"2018-06-01T08:30:00+08:00\",   \"trigger_type\": \"TIMER\",   \"trigger_name\": \"Timer_001\",   \"user_event\": \"您输入的附加信息\"}

        :return: The user_event of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._user_event

    @user_event.setter
    def user_event(self, user_event):
        r"""Sets the user_event of this TriggerEventDataRequestBody.

        附加信息（TIMER触发器参数）。 当Timer触发器触发函数执行时，执行事件（函数的event参数）为： {\"version\": \"v1.0\",   \"time\": \"2018-06-01T08:30:00+08:00\",   \"trigger_type\": \"TIMER\",   \"trigger_name\": \"Timer_001\",   \"user_event\": \"您输入的附加信息\"}

        :param user_event: The user_event of this TriggerEventDataRequestBody.
        :type user_event: str
        """
        self._user_event = user_event

    @property
    def type(self):
        r"""Gets the type of this TriggerEventDataRequestBody.

        API接口类型（APIG触发器参数）。APIG触发器此参数必填。 - 1：公有API - 2：私有API

        :return: The type of this TriggerEventDataRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TriggerEventDataRequestBody.

        API接口类型（APIG触发器参数）。APIG触发器此参数必填。 - 1：公有API - 2：私有API

        :param type: The type of this TriggerEventDataRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def path(self):
        r"""Gets the path of this TriggerEventDataRequestBody.

        APIG接口PATH路径（APIG触发器参数）。APIG触发器此参数必填。

        :return: The path of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TriggerEventDataRequestBody.

        APIG接口PATH路径（APIG触发器参数）。APIG触发器此参数必填。

        :param path: The path of this TriggerEventDataRequestBody.
        :type path: str
        """
        self._path = path

    @property
    def protocol(self):
        r"""Gets the protocol of this TriggerEventDataRequestBody.

        API的请求协议（APIG触发器参数）。APIG触发器此参数必填。

        :return: The protocol of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this TriggerEventDataRequestBody.

        API的请求协议（APIG触发器参数）。APIG触发器此参数必填。

        :param protocol: The protocol of this TriggerEventDataRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def req_method(self):
        r"""Gets the req_method of this TriggerEventDataRequestBody.

        API的请求方式（APIG触发器参数）。APIG触发器此参数必填。

        :return: The req_method of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this TriggerEventDataRequestBody.

        API的请求方式（APIG触发器参数）。APIG触发器此参数必填。

        :param req_method: The req_method of this TriggerEventDataRequestBody.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def group_id(self):
        r"""Gets the group_id of this TriggerEventDataRequestBody.

        API所属的分组编号（APIG触发器参数）。APIG触发器此参数必填。

        :return: The group_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this TriggerEventDataRequestBody.

        API所属的分组编号（APIG触发器参数）。APIG触发器此参数必填。

        :param group_id: The group_id of this TriggerEventDataRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this TriggerEventDataRequestBody.

        API所属的分组名称

        :return: The group_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this TriggerEventDataRequestBody.

        API所属的分组名称

        :param group_name: The group_name of this TriggerEventDataRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def match_mode(self):
        r"""Gets the match_mode of this TriggerEventDataRequestBody.

        API的匹配方式（APIG触发器参数）。APIG触发器此参数必填。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）

        :return: The match_mode of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        r"""Sets the match_mode of this TriggerEventDataRequestBody.

        API的匹配方式（APIG触发器参数）。APIG触发器此参数必填。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配）

        :param match_mode: The match_mode of this TriggerEventDataRequestBody.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def env_name(self):
        r"""Gets the env_name of this TriggerEventDataRequestBody.

        API的发布环境（APIG触发器参数）。APIG触发器此参数必填。

        :return: The env_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this TriggerEventDataRequestBody.

        API的发布环境（APIG触发器参数）。APIG触发器此参数必填。

        :param env_name: The env_name of this TriggerEventDataRequestBody.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_id(self):
        r"""Gets the env_id of this TriggerEventDataRequestBody.

        API的发布环境id（APIG触发器参数）。APIG触发器此参数必填。

        :return: The env_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this TriggerEventDataRequestBody.

        API的发布环境id（APIG触发器参数）。APIG触发器此参数必填。

        :param env_id: The env_id of this TriggerEventDataRequestBody.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def auth(self):
        r"""Gets the auth of this TriggerEventDataRequestBody.

        API的认证方式（APIG触发器参数）。APIG触发器此参数必填。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用

        :return: The auth of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        r"""Sets the auth of this TriggerEventDataRequestBody.

        API的认证方式（APIG触发器参数）。APIG触发器此参数必填。 - IAM：IAM认证，只允许IAM用户能访问，安全级别中等 - APP：采用Appkey&Appsecret认证，安全级别高，推荐使用 - NONE：无认证模式，所有用户均可访问，不推荐使用

        :param auth: The auth of this TriggerEventDataRequestBody.
        :type auth: str
        """
        self._auth = auth

    @property
    def func_info(self):
        r"""Gets the func_info of this TriggerEventDataRequestBody.

        :return: The func_info of this TriggerEventDataRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        """
        return self._func_info

    @func_info.setter
    def func_info(self, func_info):
        r"""Sets the func_info of this TriggerEventDataRequestBody.

        :param func_info: The func_info of this TriggerEventDataRequestBody.
        :type func_info: :class:`huaweicloudsdkfunctiongraph.v2.ApigTriggerFuncInfo`
        """
        self._func_info = func_info

    @property
    def sl_domain(self):
        r"""Gets the sl_domain of this TriggerEventDataRequestBody.

        APIG系统默认分配的子域名（APIG触发器参数）。

        :return: The sl_domain of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        r"""Sets the sl_domain of this TriggerEventDataRequestBody.

        APIG系统默认分配的子域名（APIG触发器参数）。

        :param sl_domain: The sl_domain of this TriggerEventDataRequestBody.
        :type sl_domain: str
        """
        self._sl_domain = sl_domain

    @property
    def backend_type(self):
        r"""Gets the backend_type of this TriggerEventDataRequestBody.

        API的后端类型（APIG触发器参数）。

        :return: The backend_type of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        r"""Sets the backend_type of this TriggerEventDataRequestBody.

        API的后端类型（APIG触发器参数）。

        :param backend_type: The backend_type of this TriggerEventDataRequestBody.
        :type backend_type: str
        """
        self._backend_type = backend_type

    @property
    def operations(self):
        r"""Gets the operations of this TriggerEventDataRequestBody.

        自定义操作（CTS触发器参数）。CTS触发器此参数必填。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。

        :return: The operations of this TriggerEventDataRequestBody.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this TriggerEventDataRequestBody.

        自定义操作（CTS触发器参数）。CTS触发器此参数必填。 CTS云审计服务类型和操作订阅所需要的事件通知，当CTS云审计服务获取已订阅的操作记录后，通过CTS触发器将采集到的操作记录作为参数传递来调用FunctionGraph函数。

        :param operations: The operations of this TriggerEventDataRequestBody.
        :type operations: list[str]
        """
        self._operations = operations

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TriggerEventDataRequestBody.

        实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id

        :return: The instance_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TriggerEventDataRequestBody.

        实例id。DDS、KAFKA、RABBITMQ触发器此参数必填。 - APIG触发器：apig实例id - DDS触发器：文档数据库实例id - KAFKA触发器：KAFKA实例id - RABBITMQ触发器：RABBITMQ实例id

        :param instance_id: The instance_id of this TriggerEventDataRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def collection_name(self):
        r"""Gets the collection_name of this TriggerEventDataRequestBody.

        集合名称（DDS触发器参数）。DDS触发器此参数必填。

        :return: The collection_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this TriggerEventDataRequestBody.

        集合名称（DDS触发器参数）。DDS触发器此参数必填。

        :param collection_name: The collection_name of this TriggerEventDataRequestBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def db_name(self):
        r"""Gets the db_name of this TriggerEventDataRequestBody.

        文档数据库名称（DDS触发器参数）。DDS触发器此参数必填。

        :return: The db_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TriggerEventDataRequestBody.

        文档数据库名称（DDS触发器参数）。DDS触发器此参数必填。

        :param db_name: The db_name of this TriggerEventDataRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_password(self):
        r"""Gets the db_password of this TriggerEventDataRequestBody.

        文档数据库密码（DDS触发器参数）。DDS触发器此参数必填。

        :return: The db_password of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        r"""Sets the db_password of this TriggerEventDataRequestBody.

        文档数据库密码（DDS触发器参数）。DDS触发器此参数必填。

        :param db_password: The db_password of this TriggerEventDataRequestBody.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def batch_size(self):
        r"""Gets the batch_size of this TriggerEventDataRequestBody.

        批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内

        :return: The batch_size of this TriggerEventDataRequestBody.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        r"""Sets the batch_size of this TriggerEventDataRequestBody.

        批处理大小，单次函数执行处理的最大数据量。DIS、DDS、KAFKA、RABBITMQ触发器此参数必填。 - DDS触发器：批处理大小设置1-10,000的范围内 - DIS触发器：批处理大小设置1-10,000的范围内 - KAFKA触发器：批处理大小设置1-1,000的范围内 - RABBITMQ触发器：批处理大小设置1-1,000的范围内

        :param batch_size: The batch_size of this TriggerEventDataRequestBody.
        :type batch_size: int
        """
        self._batch_size = batch_size

    @property
    def queue_id(self):
        r"""Gets the queue_id of this TriggerEventDataRequestBody.

        队列id（DMS触发器参数）。DMS触发器此参数必填。

        :return: The queue_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        r"""Sets the queue_id of this TriggerEventDataRequestBody.

        队列id（DMS触发器参数）。DMS触发器此参数必填。

        :param queue_id: The queue_id of this TriggerEventDataRequestBody.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def consumer_group_id(self):
        r"""Gets the consumer_group_id of this TriggerEventDataRequestBody.

        消费组id（DMS触发器参数）。DMS触发器此参数必填。

        :return: The consumer_group_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._consumer_group_id

    @consumer_group_id.setter
    def consumer_group_id(self, consumer_group_id):
        r"""Sets the consumer_group_id of this TriggerEventDataRequestBody.

        消费组id（DMS触发器参数）。DMS触发器此参数必填。

        :param consumer_group_id: The consumer_group_id of this TriggerEventDataRequestBody.
        :type consumer_group_id: str
        """
        self._consumer_group_id = consumer_group_id

    @property
    def polling_interval(self):
        r"""Gets the polling_interval of this TriggerEventDataRequestBody.

        拉取周期。DIS、DMS触发器此参数必填。

        :return: The polling_interval of this TriggerEventDataRequestBody.
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        r"""Sets the polling_interval of this TriggerEventDataRequestBody.

        拉取周期。DIS、DMS触发器此参数必填。

        :param polling_interval: The polling_interval of this TriggerEventDataRequestBody.
        :type polling_interval: int
        """
        self._polling_interval = polling_interval

    @property
    def stream_name(self):
        r"""Gets the stream_name of this TriggerEventDataRequestBody.

        通道名称（DIS触发器参数）。DIS触发器此参数必填。

        :return: The stream_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this TriggerEventDataRequestBody.

        通道名称（DIS触发器参数）。DIS触发器此参数必填。

        :param stream_name: The stream_name of this TriggerEventDataRequestBody.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def sharditerator_type(self):
        r"""Gets the sharditerator_type of this TriggerEventDataRequestBody.

        起始位置（DIS触发器参数）。DIS触发器此参数必填。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。

        :return: The sharditerator_type of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._sharditerator_type

    @sharditerator_type.setter
    def sharditerator_type(self, sharditerator_type):
        r"""Sets the sharditerator_type of this TriggerEventDataRequestBody.

        起始位置（DIS触发器参数）。DIS触发器此参数必填。 - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。 - LATEST：从分区中的最新记录开始读取，此设置可以保证总是读到分区中最新记录。

        :param sharditerator_type: The sharditerator_type of this TriggerEventDataRequestBody.
        :type sharditerator_type: str
        """
        self._sharditerator_type = sharditerator_type

    @property
    def polling_unit(self):
        r"""Gets the polling_unit of this TriggerEventDataRequestBody.

        拉取周期单位（DIS触发器参数）。DIS触发器此参数必填。 - s：秒 - ms：毫秒

        :return: The polling_unit of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._polling_unit

    @polling_unit.setter
    def polling_unit(self, polling_unit):
        r"""Sets the polling_unit of this TriggerEventDataRequestBody.

        拉取周期单位（DIS触发器参数）。DIS触发器此参数必填。 - s：秒 - ms：毫秒

        :param polling_unit: The polling_unit of this TriggerEventDataRequestBody.
        :type polling_unit: str
        """
        self._polling_unit = polling_unit

    @property
    def max_fetch_bytes(self):
        r"""Gets the max_fetch_bytes of this TriggerEventDataRequestBody.

        最大提取字节数（DIS触发器参数）。

        :return: The max_fetch_bytes of this TriggerEventDataRequestBody.
        :rtype: int
        """
        return self._max_fetch_bytes

    @max_fetch_bytes.setter
    def max_fetch_bytes(self, max_fetch_bytes):
        r"""Sets the max_fetch_bytes of this TriggerEventDataRequestBody.

        最大提取字节数（DIS触发器参数）。

        :param max_fetch_bytes: The max_fetch_bytes of this TriggerEventDataRequestBody.
        :type max_fetch_bytes: int
        """
        self._max_fetch_bytes = max_fetch_bytes

    @property
    def is_serial(self):
        r"""Gets the is_serial of this TriggerEventDataRequestBody.

        串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。DIS触发器此参数必填。

        :return: The is_serial of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._is_serial

    @is_serial.setter
    def is_serial(self, is_serial):
        r"""Sets the is_serial of this TriggerEventDataRequestBody.

        串行处理数据（DIS触发器参数），如果开启该选项，取一次数据处理完之后才会取下一次数据；否则只要拉取周期到了就会取数据进行处理。DIS触发器此参数必填。

        :param is_serial: The is_serial of this TriggerEventDataRequestBody.
        :type is_serial: str
        """
        self._is_serial = is_serial

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this TriggerEventDataRequestBody.

        日志组id（LTS触发器参数）。LTS触发器此参数必填。

        :return: The log_group_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this TriggerEventDataRequestBody.

        日志组id（LTS触发器参数）。LTS触发器此参数必填。

        :param log_group_id: The log_group_id of this TriggerEventDataRequestBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        r"""Gets the log_topic_id of this TriggerEventDataRequestBody.

        日志流id（LTS触发器参数）。LTS触发器此参数必填。

        :return: The log_topic_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        r"""Sets the log_topic_id of this TriggerEventDataRequestBody.

        日志流id（LTS触发器参数）。LTS触发器此参数必填。

        :param log_topic_id: The log_topic_id of this TriggerEventDataRequestBody.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def bucket(self):
        r"""Gets the bucket of this TriggerEventDataRequestBody.

        桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。OBS触发器此参数必填。

        :return: The bucket of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this TriggerEventDataRequestBody.

        桶名称（OBS触发器参数），用作事件源的OBS存储桶，不能和本用户已有桶重名；不能和其他用户已有的桶重名；创建成功后不支持修改。OBS触发器此参数必填。

        :param bucket: The bucket of this TriggerEventDataRequestBody.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        r"""Gets the prefix of this TriggerEventDataRequestBody.

        前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。

        :return: The prefix of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this TriggerEventDataRequestBody.

        前缀（OBS触发器参数），输入一个可选性前缀来限制对以此关键字开头的对象的通知。

        :param prefix: The prefix of this TriggerEventDataRequestBody.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        r"""Gets the suffix of this TriggerEventDataRequestBody.

        后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知

        :return: The suffix of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        r"""Sets the suffix of this TriggerEventDataRequestBody.

        后缀（OBS触发器参数），输入一个可选性后缀来限制对以此关键字结尾的对象的通知

        :param suffix: The suffix of this TriggerEventDataRequestBody.
        :type suffix: str
        """
        self._suffix = suffix

    @property
    def events(self):
        r"""Gets the events of this TriggerEventDataRequestBody.

        触发事件（OBS触发器参数）。OBS触发器此参数必填。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象

        :return: The events of this TriggerEventDataRequestBody.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this TriggerEventDataRequestBody.

        触发事件（OBS触发器参数）。OBS触发器此参数必填。 - ObjectCreated：表示所有创建对象的操作，包含Put、Post、Copy对象以及合并段 - Put：使用Put方法上传对象 - Post：使用Post方法上传对象 - Copy：使用copy方法复制对象 - CompleteMultipartUpload：表示合并分段任务 - ObjectRemoved：表示删除对象 - Delete：指定对象版本号删除对象 - DeleteMarkerCreated：不指定对象版本号删除对象

        :param events: The events of this TriggerEventDataRequestBody.
        :type events: list[str]
        """
        self._events = events

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this TriggerEventDataRequestBody.

        主题URN（SMN触发器参数）。SMN触发器此参数必填。

        :return: The topic_urn of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this TriggerEventDataRequestBody.

        主题URN（SMN触发器参数）。SMN触发器此参数必填。

        :param topic_urn: The topic_urn of this TriggerEventDataRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def topic_ids(self):
        r"""Gets the topic_ids of this TriggerEventDataRequestBody.

        KAFKA主题id列表（KAFKA触发器参数）。KAFKA触发器此参数必填。

        :return: The topic_ids of this TriggerEventDataRequestBody.
        :rtype: list[str]
        """
        return self._topic_ids

    @topic_ids.setter
    def topic_ids(self, topic_ids):
        r"""Sets the topic_ids of this TriggerEventDataRequestBody.

        KAFKA主题id列表（KAFKA触发器参数）。KAFKA触发器此参数必填。

        :param topic_ids: The topic_ids of this TriggerEventDataRequestBody.
        :type topic_ids: list[str]
        """
        self._topic_ids = topic_ids

    @property
    def kafka_user(self):
        r"""Gets the kafka_user of this TriggerEventDataRequestBody.

        KAFKA账户名（KAFKA触发器参数）。

        :return: The kafka_user of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._kafka_user

    @kafka_user.setter
    def kafka_user(self, kafka_user):
        r"""Sets the kafka_user of this TriggerEventDataRequestBody.

        KAFKA账户名（KAFKA触发器参数）。

        :param kafka_user: The kafka_user of this TriggerEventDataRequestBody.
        :type kafka_user: str
        """
        self._kafka_user = kafka_user

    @property
    def kafka_password(self):
        r"""Gets the kafka_password of this TriggerEventDataRequestBody.

        KAFKA账户密码（KAFKA触发器参数）。

        :return: The kafka_password of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._kafka_password

    @kafka_password.setter
    def kafka_password(self, kafka_password):
        r"""Sets the kafka_password of this TriggerEventDataRequestBody.

        KAFKA账户密码（KAFKA触发器参数）。

        :param kafka_password: The kafka_password of this TriggerEventDataRequestBody.
        :type kafka_password: str
        """
        self._kafka_password = kafka_password

    @property
    def kafka_connect_address(self):
        r"""Gets the kafka_connect_address of this TriggerEventDataRequestBody.

        KAFKA实例连接IP地址（KAFKA触发器参数）。

        :return: The kafka_connect_address of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._kafka_connect_address

    @kafka_connect_address.setter
    def kafka_connect_address(self, kafka_connect_address):
        r"""Sets the kafka_connect_address of this TriggerEventDataRequestBody.

        KAFKA实例连接IP地址（KAFKA触发器参数）。

        :param kafka_connect_address: The kafka_connect_address of this TriggerEventDataRequestBody.
        :type kafka_connect_address: str
        """
        self._kafka_connect_address = kafka_connect_address

    @property
    def kafka_ssl_enable(self):
        r"""Gets the kafka_ssl_enable of this TriggerEventDataRequestBody.

        KAFKA连接是否开启安全认证（KAFKA触发器参数）。

        :return: The kafka_ssl_enable of this TriggerEventDataRequestBody.
        :rtype: bool
        """
        return self._kafka_ssl_enable

    @kafka_ssl_enable.setter
    def kafka_ssl_enable(self, kafka_ssl_enable):
        r"""Sets the kafka_ssl_enable of this TriggerEventDataRequestBody.

        KAFKA连接是否开启安全认证（KAFKA触发器参数）。

        :param kafka_ssl_enable: The kafka_ssl_enable of this TriggerEventDataRequestBody.
        :type kafka_ssl_enable: bool
        """
        self._kafka_ssl_enable = kafka_ssl_enable

    @property
    def access_password(self):
        r"""Gets the access_password of this TriggerEventDataRequestBody.

        RABBITMQ账户密码（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。

        :return: The access_password of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._access_password

    @access_password.setter
    def access_password(self, access_password):
        r"""Sets the access_password of this TriggerEventDataRequestBody.

        RABBITMQ账户密码（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。

        :param access_password: The access_password of this TriggerEventDataRequestBody.
        :type access_password: str
        """
        self._access_password = access_password

    @property
    def access_user(self):
        r"""Gets the access_user of this TriggerEventDataRequestBody.

        RABBITMQ账户名（RABBITMQ触发器参数）。

        :return: The access_user of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        r"""Sets the access_user of this TriggerEventDataRequestBody.

        RABBITMQ账户名（RABBITMQ触发器参数）。

        :param access_user: The access_user of this TriggerEventDataRequestBody.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def connect_address(self):
        r"""Gets the connect_address of this TriggerEventDataRequestBody.

        实例连接IP地址（RABBITMQ触发器参数）。

        :return: The connect_address of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        r"""Sets the connect_address of this TriggerEventDataRequestBody.

        实例连接IP地址（RABBITMQ触发器参数）。

        :param connect_address: The connect_address of this TriggerEventDataRequestBody.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def exchange_name(self):
        r"""Gets the exchange_name of this TriggerEventDataRequestBody.

        交换机名称（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。

        :return: The exchange_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        r"""Sets the exchange_name of this TriggerEventDataRequestBody.

        交换机名称（RABBITMQ触发器参数）。RABBITMQ触发器此参数必填。

        :param exchange_name: The exchange_name of this TriggerEventDataRequestBody.
        :type exchange_name: str
        """
        self._exchange_name = exchange_name

    @property
    def vhost(self):
        r"""Gets the vhost of this TriggerEventDataRequestBody.

        虚拟机名称（RABBITMQ触发器参数）。

        :return: The vhost of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this TriggerEventDataRequestBody.

        虚拟机名称（RABBITMQ触发器参数）。

        :param vhost: The vhost of this TriggerEventDataRequestBody.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this TriggerEventDataRequestBody.

        RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。

        :return: The ssl_enable of this TriggerEventDataRequestBody.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this TriggerEventDataRequestBody.

        RABBITMQ连接是否开启安全认证（RABBITMQ触发器参数）。

        :param ssl_enable: The ssl_enable of this TriggerEventDataRequestBody.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def key_encode(self):
        r"""Gets the key_encode of this TriggerEventDataRequestBody.

        EG obs触发器是否对对象加密（EVENTGRID触发器参数）。

        :return: The key_encode of this TriggerEventDataRequestBody.
        :rtype: bool
        """
        return self._key_encode

    @key_encode.setter
    def key_encode(self, key_encode):
        r"""Sets the key_encode of this TriggerEventDataRequestBody.

        EG obs触发器是否对对象加密（EVENTGRID触发器参数）。

        :param key_encode: The key_encode of this TriggerEventDataRequestBody.
        :type key_encode: bool
        """
        self._key_encode = key_encode

    @property
    def agency(self):
        r"""Gets the agency of this TriggerEventDataRequestBody.

        使用的代理（EVENTGRID触发器参数）。

        :return: The agency of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this TriggerEventDataRequestBody.

        使用的代理（EVENTGRID触发器参数）。

        :param agency: The agency of this TriggerEventDataRequestBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def channel_name(self):
        r"""Gets the channel_name of this TriggerEventDataRequestBody.

        通道名称（EVENTGRID触发器参数）。

        :return: The channel_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this TriggerEventDataRequestBody.

        通道名称（EVENTGRID触发器参数）。

        :param channel_name: The channel_name of this TriggerEventDataRequestBody.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def channel_id(self):
        r"""Gets the channel_id of this TriggerEventDataRequestBody.

        通道id（EVENTGRID触发器参数）。

        :return: The channel_id of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this TriggerEventDataRequestBody.

        通道id（EVENTGRID触发器参数）。

        :param channel_id: The channel_id of this TriggerEventDataRequestBody.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def source_name(self):
        r"""Gets the source_name of this TriggerEventDataRequestBody.

        事件源名称（EVENTGRID触发器参数）。

        :return: The source_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this TriggerEventDataRequestBody.

        事件源名称（EVENTGRID触发器参数）。

        :param source_name: The source_name of this TriggerEventDataRequestBody.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def created_time(self):
        r"""Gets the created_time of this TriggerEventDataRequestBody.

        创建时间（EVENTGRID触发器参数）。

        :return: The created_time of this TriggerEventDataRequestBody.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this TriggerEventDataRequestBody.

        创建时间（EVENTGRID触发器参数）。

        :param created_time: The created_time of this TriggerEventDataRequestBody.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def status(self):
        r"""Gets the status of this TriggerEventDataRequestBody.

        触发器状态（EVENTGRID触发器参数）。

        :return: The status of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TriggerEventDataRequestBody.

        触发器状态（EVENTGRID触发器参数）。

        :param status: The status of this TriggerEventDataRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def trigger_name(self):
        r"""Gets the trigger_name of this TriggerEventDataRequestBody.

        触发器名称（EVENTGRID触发器参数）。

        :return: The trigger_name of this TriggerEventDataRequestBody.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        r"""Sets the trigger_name of this TriggerEventDataRequestBody.

        触发器名称（EVENTGRID触发器参数）。

        :param trigger_name: The trigger_name of this TriggerEventDataRequestBody.
        :type trigger_name: str
        """
        self._trigger_name = trigger_name

    @property
    def event_types(self):
        r"""Gets the event_types of this TriggerEventDataRequestBody.

        事件类型（EVENTGRID触发器参数）。

        :return: The event_types of this TriggerEventDataRequestBody.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this TriggerEventDataRequestBody.

        事件类型（EVENTGRID触发器参数）。

        :param event_types: The event_types of this TriggerEventDataRequestBody.
        :type event_types: list[str]
        """
        self._event_types = event_types

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
        if not isinstance(other, TriggerEventDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
