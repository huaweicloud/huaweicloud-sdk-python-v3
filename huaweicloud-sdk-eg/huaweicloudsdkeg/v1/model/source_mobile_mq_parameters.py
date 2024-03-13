# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceMobileMQParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'instance_id': 'str',
        'topic': 'str',
        'tag': 'str',
        'authentication_required': 'bool',
        'msg_trace_switch': 'bool',
        'access_key': 'str',
        'secret_key': 'str',
        'message_model': 'str',
        'addr_type': 'str',
        'addr': 'str',
        'sdk_url': 'str',
        'consume_timeout': 'int',
        'message_type': 'str',
        'suspend_time': 'int',
        'max_reconsumer_times': 'int',
        'consumer_thread_nums': 'int',
        'consumer_batch_max_size': 'int',
        'consumer_max_wait': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'instance_id': 'instance_id',
        'topic': 'topic',
        'tag': 'tag',
        'authentication_required': 'authentication_required',
        'msg_trace_switch': 'msg_trace_switch',
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'message_model': 'message_model',
        'addr_type': 'addr_type',
        'addr': 'addr',
        'sdk_url': 'sdk_url',
        'consume_timeout': 'consume_timeout',
        'message_type': 'message_type',
        'suspend_time': 'suspend_time',
        'max_reconsumer_times': 'max_reconsumer_times',
        'consumer_thread_nums': 'consumer_thread_nums',
        'consumer_batch_max_size': 'consumer_batch_max_size',
        'consumer_max_wait': 'consumer_max_wait',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, group_id=None, instance_id=None, topic=None, tag=None, authentication_required=None, msg_trace_switch=None, access_key=None, secret_key=None, message_model=None, addr_type=None, addr=None, sdk_url=None, consume_timeout=None, message_type=None, suspend_time=None, max_reconsumer_times=None, consumer_thread_nums=None, consumer_batch_max_size=None, consumer_max_wait=None, vpc_id=None, subnet_id=None):
        """SourceMobileMQParameters

        The model defined in huaweicloud sdk

        :param group_id: 消费组id
        :type group_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param topic: topic
        :type topic: str
        :param tag: 标签
        :type tag: str
        :param authentication_required: 鉴权认证
        :type authentication_required: bool
        :param msg_trace_switch: 保存消息轨迹
        :type msg_trace_switch: bool
        :param access_key: AccessKey
        :type access_key: str
        :param secret_key: SecretKey
        :type secret_key: str
        :param message_model: 订阅方式
        :type message_model: str
        :param addr_type: 接入点类型
        :type addr_type: str
        :param addr: 地址
        :type addr: str
        :param sdk_url: 依赖SDK
        :type sdk_url: str
        :param consume_timeout: 消费超时时间
        :type consume_timeout: int
        :param message_type: 消息类型
        :type message_type: str
        :param suspend_time: 失败重试的等待时间
        :type suspend_time: int
        :param max_reconsumer_times: 最大重试次数
        :type max_reconsumer_times: int
        :param consumer_thread_nums: 消费线程数
        :type consumer_thread_nums: int
        :param consumer_batch_max_size: 批量消费最大消息数
        :type consumer_batch_max_size: int
        :param consumer_max_wait: 批量消费最大等待时长，单位：秒
        :type consumer_max_wait: int
        :param vpc_id: 虚拟私有云
        :type vpc_id: str
        :param subnet_id: 子网
        :type subnet_id: str
        """
        
        

        self._group_id = None
        self._instance_id = None
        self._topic = None
        self._tag = None
        self._authentication_required = None
        self._msg_trace_switch = None
        self._access_key = None
        self._secret_key = None
        self._message_model = None
        self._addr_type = None
        self._addr = None
        self._sdk_url = None
        self._consume_timeout = None
        self._message_type = None
        self._suspend_time = None
        self._max_reconsumer_times = None
        self._consumer_thread_nums = None
        self._consumer_batch_max_size = None
        self._consumer_max_wait = None
        self._vpc_id = None
        self._subnet_id = None
        self.discriminator = None

        self.group_id = group_id
        self.instance_id = instance_id
        self.topic = topic
        if tag is not None:
            self.tag = tag
        if authentication_required is not None:
            self.authentication_required = authentication_required
        if msg_trace_switch is not None:
            self.msg_trace_switch = msg_trace_switch
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        self.message_model = message_model
        self.addr_type = addr_type
        self.addr = addr
        self.sdk_url = sdk_url
        self.consume_timeout = consume_timeout
        self.message_type = message_type
        if suspend_time is not None:
            self.suspend_time = suspend_time
        if max_reconsumer_times is not None:
            self.max_reconsumer_times = max_reconsumer_times
        if consumer_thread_nums is not None:
            self.consumer_thread_nums = consumer_thread_nums
        if consumer_batch_max_size is not None:
            self.consumer_batch_max_size = consumer_batch_max_size
        if consumer_max_wait is not None:
            self.consumer_max_wait = consumer_max_wait
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def group_id(self):
        """Gets the group_id of this SourceMobileMQParameters.

        消费组id

        :return: The group_id of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this SourceMobileMQParameters.

        消费组id

        :param group_id: The group_id of this SourceMobileMQParameters.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def instance_id(self):
        """Gets the instance_id of this SourceMobileMQParameters.

        实例id

        :return: The instance_id of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this SourceMobileMQParameters.

        实例id

        :param instance_id: The instance_id of this SourceMobileMQParameters.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this SourceMobileMQParameters.

        topic

        :return: The topic of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this SourceMobileMQParameters.

        topic

        :param topic: The topic of this SourceMobileMQParameters.
        :type topic: str
        """
        self._topic = topic

    @property
    def tag(self):
        """Gets the tag of this SourceMobileMQParameters.

        标签

        :return: The tag of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SourceMobileMQParameters.

        标签

        :param tag: The tag of this SourceMobileMQParameters.
        :type tag: str
        """
        self._tag = tag

    @property
    def authentication_required(self):
        """Gets the authentication_required of this SourceMobileMQParameters.

        鉴权认证

        :return: The authentication_required of this SourceMobileMQParameters.
        :rtype: bool
        """
        return self._authentication_required

    @authentication_required.setter
    def authentication_required(self, authentication_required):
        """Sets the authentication_required of this SourceMobileMQParameters.

        鉴权认证

        :param authentication_required: The authentication_required of this SourceMobileMQParameters.
        :type authentication_required: bool
        """
        self._authentication_required = authentication_required

    @property
    def msg_trace_switch(self):
        """Gets the msg_trace_switch of this SourceMobileMQParameters.

        保存消息轨迹

        :return: The msg_trace_switch of this SourceMobileMQParameters.
        :rtype: bool
        """
        return self._msg_trace_switch

    @msg_trace_switch.setter
    def msg_trace_switch(self, msg_trace_switch):
        """Sets the msg_trace_switch of this SourceMobileMQParameters.

        保存消息轨迹

        :param msg_trace_switch: The msg_trace_switch of this SourceMobileMQParameters.
        :type msg_trace_switch: bool
        """
        self._msg_trace_switch = msg_trace_switch

    @property
    def access_key(self):
        """Gets the access_key of this SourceMobileMQParameters.

        AccessKey

        :return: The access_key of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this SourceMobileMQParameters.

        AccessKey

        :param access_key: The access_key of this SourceMobileMQParameters.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this SourceMobileMQParameters.

        SecretKey

        :return: The secret_key of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this SourceMobileMQParameters.

        SecretKey

        :param secret_key: The secret_key of this SourceMobileMQParameters.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def message_model(self):
        """Gets the message_model of this SourceMobileMQParameters.

        订阅方式

        :return: The message_model of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._message_model

    @message_model.setter
    def message_model(self, message_model):
        """Sets the message_model of this SourceMobileMQParameters.

        订阅方式

        :param message_model: The message_model of this SourceMobileMQParameters.
        :type message_model: str
        """
        self._message_model = message_model

    @property
    def addr_type(self):
        """Gets the addr_type of this SourceMobileMQParameters.

        接入点类型

        :return: The addr_type of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._addr_type

    @addr_type.setter
    def addr_type(self, addr_type):
        """Sets the addr_type of this SourceMobileMQParameters.

        接入点类型

        :param addr_type: The addr_type of this SourceMobileMQParameters.
        :type addr_type: str
        """
        self._addr_type = addr_type

    @property
    def addr(self):
        """Gets the addr of this SourceMobileMQParameters.

        地址

        :return: The addr of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this SourceMobileMQParameters.

        地址

        :param addr: The addr of this SourceMobileMQParameters.
        :type addr: str
        """
        self._addr = addr

    @property
    def sdk_url(self):
        """Gets the sdk_url of this SourceMobileMQParameters.

        依赖SDK

        :return: The sdk_url of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._sdk_url

    @sdk_url.setter
    def sdk_url(self, sdk_url):
        """Sets the sdk_url of this SourceMobileMQParameters.

        依赖SDK

        :param sdk_url: The sdk_url of this SourceMobileMQParameters.
        :type sdk_url: str
        """
        self._sdk_url = sdk_url

    @property
    def consume_timeout(self):
        """Gets the consume_timeout of this SourceMobileMQParameters.

        消费超时时间

        :return: The consume_timeout of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._consume_timeout

    @consume_timeout.setter
    def consume_timeout(self, consume_timeout):
        """Sets the consume_timeout of this SourceMobileMQParameters.

        消费超时时间

        :param consume_timeout: The consume_timeout of this SourceMobileMQParameters.
        :type consume_timeout: int
        """
        self._consume_timeout = consume_timeout

    @property
    def message_type(self):
        """Gets the message_type of this SourceMobileMQParameters.

        消息类型

        :return: The message_type of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this SourceMobileMQParameters.

        消息类型

        :param message_type: The message_type of this SourceMobileMQParameters.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def suspend_time(self):
        """Gets the suspend_time of this SourceMobileMQParameters.

        失败重试的等待时间

        :return: The suspend_time of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._suspend_time

    @suspend_time.setter
    def suspend_time(self, suspend_time):
        """Sets the suspend_time of this SourceMobileMQParameters.

        失败重试的等待时间

        :param suspend_time: The suspend_time of this SourceMobileMQParameters.
        :type suspend_time: int
        """
        self._suspend_time = suspend_time

    @property
    def max_reconsumer_times(self):
        """Gets the max_reconsumer_times of this SourceMobileMQParameters.

        最大重试次数

        :return: The max_reconsumer_times of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._max_reconsumer_times

    @max_reconsumer_times.setter
    def max_reconsumer_times(self, max_reconsumer_times):
        """Sets the max_reconsumer_times of this SourceMobileMQParameters.

        最大重试次数

        :param max_reconsumer_times: The max_reconsumer_times of this SourceMobileMQParameters.
        :type max_reconsumer_times: int
        """
        self._max_reconsumer_times = max_reconsumer_times

    @property
    def consumer_thread_nums(self):
        """Gets the consumer_thread_nums of this SourceMobileMQParameters.

        消费线程数

        :return: The consumer_thread_nums of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._consumer_thread_nums

    @consumer_thread_nums.setter
    def consumer_thread_nums(self, consumer_thread_nums):
        """Sets the consumer_thread_nums of this SourceMobileMQParameters.

        消费线程数

        :param consumer_thread_nums: The consumer_thread_nums of this SourceMobileMQParameters.
        :type consumer_thread_nums: int
        """
        self._consumer_thread_nums = consumer_thread_nums

    @property
    def consumer_batch_max_size(self):
        """Gets the consumer_batch_max_size of this SourceMobileMQParameters.

        批量消费最大消息数

        :return: The consumer_batch_max_size of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._consumer_batch_max_size

    @consumer_batch_max_size.setter
    def consumer_batch_max_size(self, consumer_batch_max_size):
        """Sets the consumer_batch_max_size of this SourceMobileMQParameters.

        批量消费最大消息数

        :param consumer_batch_max_size: The consumer_batch_max_size of this SourceMobileMQParameters.
        :type consumer_batch_max_size: int
        """
        self._consumer_batch_max_size = consumer_batch_max_size

    @property
    def consumer_max_wait(self):
        """Gets the consumer_max_wait of this SourceMobileMQParameters.

        批量消费最大等待时长，单位：秒

        :return: The consumer_max_wait of this SourceMobileMQParameters.
        :rtype: int
        """
        return self._consumer_max_wait

    @consumer_max_wait.setter
    def consumer_max_wait(self, consumer_max_wait):
        """Sets the consumer_max_wait of this SourceMobileMQParameters.

        批量消费最大等待时长，单位：秒

        :param consumer_max_wait: The consumer_max_wait of this SourceMobileMQParameters.
        :type consumer_max_wait: int
        """
        self._consumer_max_wait = consumer_max_wait

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SourceMobileMQParameters.

        虚拟私有云

        :return: The vpc_id of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SourceMobileMQParameters.

        虚拟私有云

        :param vpc_id: The vpc_id of this SourceMobileMQParameters.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this SourceMobileMQParameters.

        子网

        :return: The subnet_id of this SourceMobileMQParameters.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this SourceMobileMQParameters.

        子网

        :param subnet_id: The subnet_id of this SourceMobileMQParameters.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, SourceMobileMQParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
