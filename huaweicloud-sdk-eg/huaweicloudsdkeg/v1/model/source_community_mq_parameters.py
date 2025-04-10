# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceCommunityMQParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'instance_id': 'str',
        'addr': 'str',
        'group': 'str',
        'topic': 'str',
        'tag': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'ssl_enable': 'bool',
        'enable_acl': 'bool',
        'access_key': 'str',
        'secret_key': 'str',
        'message_type': 'str',
        'consume_timeout': 'int',
        'consumer_thread_nums': 'int',
        'consumer_batch_max_size': 'int',
        'max_reconsume_times': 'int',
        'suspend_current_queue_time_millis': 'int'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'addr': 'addr',
        'group': 'group',
        'topic': 'topic',
        'tag': 'tag',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'ssl_enable': 'ssl_enable',
        'enable_acl': 'enable_acl',
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'message_type': 'message_type',
        'consume_timeout': 'consume_timeout',
        'consumer_thread_nums': 'consumer_thread_nums',
        'consumer_batch_max_size': 'consumer_batch_max_size',
        'max_reconsume_times': 'max_reconsume_times',
        'suspend_current_queue_time_millis': 'suspend_current_queue_time_millis'
    }

    def __init__(self, instance_name=None, instance_id=None, addr=None, group=None, topic=None, tag=None, vpc_id=None, subnet_id=None, ssl_enable=None, enable_acl=None, access_key=None, secret_key=None, message_type=None, consume_timeout=None, consumer_thread_nums=None, consumer_batch_max_size=None, max_reconsume_times=None, suspend_current_queue_time_millis=None):
        r"""SourceCommunityMQParameters

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称，仅dms的rockectMq需要该字段
        :type instance_name: str
        :param instance_id: 实例ID，仅dms的rockectMq需要该字段
        :type instance_id: str
        :param addr: rockectMq连接地址
        :type addr: str
        :param group: 消费组
        :type group: str
        :param topic: topic名称
        :type topic: str
        :param tag: 标签
        :type tag: str
        :param vpc_id: 虚拟云id
        :type vpc_id: str
        :param subnet_id: 子网id
        :type subnet_id: str
        :param ssl_enable: 开启SSL
        :type ssl_enable: bool
        :param enable_acl: ACL访问控制
        :type enable_acl: bool
        :param access_key: 用户名
        :type access_key: str
        :param secret_key: 密码
        :type secret_key: str
        :param message_type: 消息类型
        :type message_type: str
        :param consume_timeout: 消费超时时间
        :type consume_timeout: int
        :param consumer_thread_nums: 线程消费数
        :type consumer_thread_nums: int
        :param consumer_batch_max_size: 批量消费最大消息数
        :type consumer_batch_max_size: int
        :param max_reconsume_times: 最大重试次数，-1表示一直重试
        :type max_reconsume_times: int
        :param suspend_current_queue_time_millis: 重试间隔，单位ms
        :type suspend_current_queue_time_millis: int
        """
        
        

        self._instance_name = None
        self._instance_id = None
        self._addr = None
        self._group = None
        self._topic = None
        self._tag = None
        self._vpc_id = None
        self._subnet_id = None
        self._ssl_enable = None
        self._enable_acl = None
        self._access_key = None
        self._secret_key = None
        self._message_type = None
        self._consume_timeout = None
        self._consumer_thread_nums = None
        self._consumer_batch_max_size = None
        self._max_reconsume_times = None
        self._suspend_current_queue_time_millis = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        self.addr = addr
        self.group = group
        self.topic = topic
        if tag is not None:
            self.tag = tag
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if message_type is not None:
            self.message_type = message_type
        if consume_timeout is not None:
            self.consume_timeout = consume_timeout
        if consumer_thread_nums is not None:
            self.consumer_thread_nums = consumer_thread_nums
        if consumer_batch_max_size is not None:
            self.consumer_batch_max_size = consumer_batch_max_size
        if max_reconsume_times is not None:
            self.max_reconsume_times = max_reconsume_times
        if suspend_current_queue_time_millis is not None:
            self.suspend_current_queue_time_millis = suspend_current_queue_time_millis

    @property
    def instance_name(self):
        r"""Gets the instance_name of this SourceCommunityMQParameters.

        实例名称，仅dms的rockectMq需要该字段

        :return: The instance_name of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this SourceCommunityMQParameters.

        实例名称，仅dms的rockectMq需要该字段

        :param instance_name: The instance_name of this SourceCommunityMQParameters.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SourceCommunityMQParameters.

        实例ID，仅dms的rockectMq需要该字段

        :return: The instance_id of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SourceCommunityMQParameters.

        实例ID，仅dms的rockectMq需要该字段

        :param instance_id: The instance_id of this SourceCommunityMQParameters.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def addr(self):
        r"""Gets the addr of this SourceCommunityMQParameters.

        rockectMq连接地址

        :return: The addr of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this SourceCommunityMQParameters.

        rockectMq连接地址

        :param addr: The addr of this SourceCommunityMQParameters.
        :type addr: str
        """
        self._addr = addr

    @property
    def group(self):
        r"""Gets the group of this SourceCommunityMQParameters.

        消费组

        :return: The group of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this SourceCommunityMQParameters.

        消费组

        :param group: The group of this SourceCommunityMQParameters.
        :type group: str
        """
        self._group = group

    @property
    def topic(self):
        r"""Gets the topic of this SourceCommunityMQParameters.

        topic名称

        :return: The topic of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SourceCommunityMQParameters.

        topic名称

        :param topic: The topic of this SourceCommunityMQParameters.
        :type topic: str
        """
        self._topic = topic

    @property
    def tag(self):
        r"""Gets the tag of this SourceCommunityMQParameters.

        标签

        :return: The tag of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this SourceCommunityMQParameters.

        标签

        :param tag: The tag of this SourceCommunityMQParameters.
        :type tag: str
        """
        self._tag = tag

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this SourceCommunityMQParameters.

        虚拟云id

        :return: The vpc_id of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this SourceCommunityMQParameters.

        虚拟云id

        :param vpc_id: The vpc_id of this SourceCommunityMQParameters.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this SourceCommunityMQParameters.

        子网id

        :return: The subnet_id of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this SourceCommunityMQParameters.

        子网id

        :param subnet_id: The subnet_id of this SourceCommunityMQParameters.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this SourceCommunityMQParameters.

        开启SSL

        :return: The ssl_enable of this SourceCommunityMQParameters.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this SourceCommunityMQParameters.

        开启SSL

        :param ssl_enable: The ssl_enable of this SourceCommunityMQParameters.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this SourceCommunityMQParameters.

        ACL访问控制

        :return: The enable_acl of this SourceCommunityMQParameters.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this SourceCommunityMQParameters.

        ACL访问控制

        :param enable_acl: The enable_acl of this SourceCommunityMQParameters.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def access_key(self):
        r"""Gets the access_key of this SourceCommunityMQParameters.

        用户名

        :return: The access_key of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this SourceCommunityMQParameters.

        用户名

        :param access_key: The access_key of this SourceCommunityMQParameters.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this SourceCommunityMQParameters.

        密码

        :return: The secret_key of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this SourceCommunityMQParameters.

        密码

        :param secret_key: The secret_key of this SourceCommunityMQParameters.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def message_type(self):
        r"""Gets the message_type of this SourceCommunityMQParameters.

        消息类型

        :return: The message_type of this SourceCommunityMQParameters.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        r"""Sets the message_type of this SourceCommunityMQParameters.

        消息类型

        :param message_type: The message_type of this SourceCommunityMQParameters.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def consume_timeout(self):
        r"""Gets the consume_timeout of this SourceCommunityMQParameters.

        消费超时时间

        :return: The consume_timeout of this SourceCommunityMQParameters.
        :rtype: int
        """
        return self._consume_timeout

    @consume_timeout.setter
    def consume_timeout(self, consume_timeout):
        r"""Sets the consume_timeout of this SourceCommunityMQParameters.

        消费超时时间

        :param consume_timeout: The consume_timeout of this SourceCommunityMQParameters.
        :type consume_timeout: int
        """
        self._consume_timeout = consume_timeout

    @property
    def consumer_thread_nums(self):
        r"""Gets the consumer_thread_nums of this SourceCommunityMQParameters.

        线程消费数

        :return: The consumer_thread_nums of this SourceCommunityMQParameters.
        :rtype: int
        """
        return self._consumer_thread_nums

    @consumer_thread_nums.setter
    def consumer_thread_nums(self, consumer_thread_nums):
        r"""Sets the consumer_thread_nums of this SourceCommunityMQParameters.

        线程消费数

        :param consumer_thread_nums: The consumer_thread_nums of this SourceCommunityMQParameters.
        :type consumer_thread_nums: int
        """
        self._consumer_thread_nums = consumer_thread_nums

    @property
    def consumer_batch_max_size(self):
        r"""Gets the consumer_batch_max_size of this SourceCommunityMQParameters.

        批量消费最大消息数

        :return: The consumer_batch_max_size of this SourceCommunityMQParameters.
        :rtype: int
        """
        return self._consumer_batch_max_size

    @consumer_batch_max_size.setter
    def consumer_batch_max_size(self, consumer_batch_max_size):
        r"""Sets the consumer_batch_max_size of this SourceCommunityMQParameters.

        批量消费最大消息数

        :param consumer_batch_max_size: The consumer_batch_max_size of this SourceCommunityMQParameters.
        :type consumer_batch_max_size: int
        """
        self._consumer_batch_max_size = consumer_batch_max_size

    @property
    def max_reconsume_times(self):
        r"""Gets the max_reconsume_times of this SourceCommunityMQParameters.

        最大重试次数，-1表示一直重试

        :return: The max_reconsume_times of this SourceCommunityMQParameters.
        :rtype: int
        """
        return self._max_reconsume_times

    @max_reconsume_times.setter
    def max_reconsume_times(self, max_reconsume_times):
        r"""Sets the max_reconsume_times of this SourceCommunityMQParameters.

        最大重试次数，-1表示一直重试

        :param max_reconsume_times: The max_reconsume_times of this SourceCommunityMQParameters.
        :type max_reconsume_times: int
        """
        self._max_reconsume_times = max_reconsume_times

    @property
    def suspend_current_queue_time_millis(self):
        r"""Gets the suspend_current_queue_time_millis of this SourceCommunityMQParameters.

        重试间隔，单位ms

        :return: The suspend_current_queue_time_millis of this SourceCommunityMQParameters.
        :rtype: int
        """
        return self._suspend_current_queue_time_millis

    @suspend_current_queue_time_millis.setter
    def suspend_current_queue_time_millis(self, suspend_current_queue_time_millis):
        r"""Sets the suspend_current_queue_time_millis of this SourceCommunityMQParameters.

        重试间隔，单位ms

        :param suspend_current_queue_time_millis: The suspend_current_queue_time_millis of this SourceCommunityMQParameters.
        :type suspend_current_queue_time_millis: int
        """
        self._suspend_current_queue_time_millis = suspend_current_queue_time_millis

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
        if not isinstance(other, SourceCommunityMQParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
