# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncDeviceListCommand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'command_id': 'str',
        'service_id': 'str',
        'command_name': 'str',
        'expire_time': 'int',
        'status': 'str',
        'created_time': 'str',
        'sent_time': 'str',
        'delivered_time': 'str',
        'send_strategy': 'str',
        'response_time': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'command_id': 'command_id',
        'service_id': 'service_id',
        'command_name': 'command_name',
        'expire_time': 'expire_time',
        'status': 'status',
        'created_time': 'created_time',
        'sent_time': 'sent_time',
        'delivered_time': 'delivered_time',
        'send_strategy': 'send_strategy',
        'response_time': 'response_time'
    }

    def __init__(self, device_id=None, command_id=None, service_id=None, command_name=None, expire_time=None, status=None, created_time=None, sent_time=None, delivered_time=None, send_strategy=None, response_time=None):
        r"""AsyncDeviceListCommand

        The model defined in huaweicloud sdk

        :param device_id: 设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。
        :type device_id: str
        :param command_id: 设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。
        :type command_id: str
        :param service_id: 设备命令所属的设备服务ID，在设备关联的产品模型中定义。
        :type service_id: str
        :param command_name: 设备命令名称，在设备关联的产品模型中定义。
        :type command_name: str
        :param expire_time: 物联网平台缓存命令的时长， 单位秒。
        :type expire_time: int
        :param status: 下发命令的状态。 ·PENDING表示未下发,在物联网平台缓存着 ·EXPIRED表示命令已经过期，即缓存的时间超过设定的expire_time ·SENT表示命令正在下发 ·DELIVERED表示命令已送达设备 ·SUCCESSFUL表示命令已经成功执行 ·FAILED表示命令执行失败 ·TIMEOUT表示命令下发之后，没有收到设备确认或者响应结果一定时间后超时 
        :type status: str
        :param created_time: 命令的创建时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type created_time: str
        :param sent_time: 物联网平台发送命令的时间，如果命令是立即下发， 则该时间与命令创建时间一致， 如果是缓存命令， 则是命令实际下发的时间。\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type sent_time: str
        :param delivered_time: 物联网平台将命令送达到设备的时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type delivered_time: str
        :param send_strategy: 下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。
        :type send_strategy: str
        :param response_time: 设备响应命令的时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type response_time: str
        """
        
        

        self._device_id = None
        self._command_id = None
        self._service_id = None
        self._command_name = None
        self._expire_time = None
        self._status = None
        self._created_time = None
        self._sent_time = None
        self._delivered_time = None
        self._send_strategy = None
        self._response_time = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if command_id is not None:
            self.command_id = command_id
        if service_id is not None:
            self.service_id = service_id
        if command_name is not None:
            self.command_name = command_name
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if sent_time is not None:
            self.sent_time = sent_time
        if delivered_time is not None:
            self.delivered_time = delivered_time
        if send_strategy is not None:
            self.send_strategy = send_strategy
        if response_time is not None:
            self.response_time = response_time

    @property
    def device_id(self):
        r"""Gets the device_id of this AsyncDeviceListCommand.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :return: The device_id of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this AsyncDeviceListCommand.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :param device_id: The device_id of this AsyncDeviceListCommand.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def command_id(self):
        r"""Gets the command_id of this AsyncDeviceListCommand.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :return: The command_id of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this AsyncDeviceListCommand.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :param command_id: The command_id of this AsyncDeviceListCommand.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def service_id(self):
        r"""Gets the service_id of this AsyncDeviceListCommand.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this AsyncDeviceListCommand.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this AsyncDeviceListCommand.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def command_name(self):
        r"""Gets the command_name of this AsyncDeviceListCommand.

        设备命令名称，在设备关联的产品模型中定义。

        :return: The command_name of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        r"""Sets the command_name of this AsyncDeviceListCommand.

        设备命令名称，在设备关联的产品模型中定义。

        :param command_name: The command_name of this AsyncDeviceListCommand.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def expire_time(self):
        r"""Gets the expire_time of this AsyncDeviceListCommand.

        物联网平台缓存命令的时长， 单位秒。

        :return: The expire_time of this AsyncDeviceListCommand.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this AsyncDeviceListCommand.

        物联网平台缓存命令的时长， 单位秒。

        :param expire_time: The expire_time of this AsyncDeviceListCommand.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def status(self):
        r"""Gets the status of this AsyncDeviceListCommand.

        下发命令的状态。 ·PENDING表示未下发,在物联网平台缓存着 ·EXPIRED表示命令已经过期，即缓存的时间超过设定的expire_time ·SENT表示命令正在下发 ·DELIVERED表示命令已送达设备 ·SUCCESSFUL表示命令已经成功执行 ·FAILED表示命令执行失败 ·TIMEOUT表示命令下发之后，没有收到设备确认或者响应结果一定时间后超时 

        :return: The status of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AsyncDeviceListCommand.

        下发命令的状态。 ·PENDING表示未下发,在物联网平台缓存着 ·EXPIRED表示命令已经过期，即缓存的时间超过设定的expire_time ·SENT表示命令正在下发 ·DELIVERED表示命令已送达设备 ·SUCCESSFUL表示命令已经成功执行 ·FAILED表示命令执行失败 ·TIMEOUT表示命令下发之后，没有收到设备确认或者响应结果一定时间后超时 

        :param status: The status of this AsyncDeviceListCommand.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this AsyncDeviceListCommand.

        命令的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this AsyncDeviceListCommand.

        命令的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this AsyncDeviceListCommand.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def sent_time(self):
        r"""Gets the sent_time of this AsyncDeviceListCommand.

        物联网平台发送命令的时间，如果命令是立即下发， 则该时间与命令创建时间一致， 如果是缓存命令， 则是命令实际下发的时间。\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The sent_time of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        r"""Sets the sent_time of this AsyncDeviceListCommand.

        物联网平台发送命令的时间，如果命令是立即下发， 则该时间与命令创建时间一致， 如果是缓存命令， 则是命令实际下发的时间。\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param sent_time: The sent_time of this AsyncDeviceListCommand.
        :type sent_time: str
        """
        self._sent_time = sent_time

    @property
    def delivered_time(self):
        r"""Gets the delivered_time of this AsyncDeviceListCommand.

        物联网平台将命令送达到设备的时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The delivered_time of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._delivered_time

    @delivered_time.setter
    def delivered_time(self, delivered_time):
        r"""Sets the delivered_time of this AsyncDeviceListCommand.

        物联网平台将命令送达到设备的时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param delivered_time: The delivered_time of this AsyncDeviceListCommand.
        :type delivered_time: str
        """
        self._delivered_time = delivered_time

    @property
    def send_strategy(self):
        r"""Gets the send_strategy of this AsyncDeviceListCommand.

        下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。

        :return: The send_strategy of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        r"""Sets the send_strategy of this AsyncDeviceListCommand.

        下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。

        :param send_strategy: The send_strategy of this AsyncDeviceListCommand.
        :type send_strategy: str
        """
        self._send_strategy = send_strategy

    @property
    def response_time(self):
        r"""Gets the response_time of this AsyncDeviceListCommand.

        设备响应命令的时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The response_time of this AsyncDeviceListCommand.
        :rtype: str
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        r"""Sets the response_time of this AsyncDeviceListCommand.

        设备响应命令的时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param response_time: The response_time of this AsyncDeviceListCommand.
        :type response_time: str
        """
        self._response_time = response_time

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
        if not isinstance(other, AsyncDeviceListCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
