# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAsyncCommandResponse(SdkResponse):

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
        'paras': 'object',
        'expire_time': 'int',
        'status': 'str',
        'created_time': 'str',
        'send_strategy': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'command_id': 'command_id',
        'service_id': 'service_id',
        'command_name': 'command_name',
        'paras': 'paras',
        'expire_time': 'expire_time',
        'status': 'status',
        'created_time': 'created_time',
        'send_strategy': 'send_strategy'
    }

    def __init__(self, device_id=None, command_id=None, service_id=None, command_name=None, paras=None, expire_time=None, status=None, created_time=None, send_strategy=None):
        r"""CreateAsyncCommandResponse

        The model defined in huaweicloud sdk

        :param device_id: 设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。
        :type device_id: str
        :param command_id: 设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。
        :type command_id: str
        :param service_id: 设备命令所属的设备服务ID，在设备关联的产品模型中定义。
        :type service_id: str
        :param command_name: 设备命令名称，在设备关联的产品模型中定义。
        :type command_name: str
        :param paras: 设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\&quot;value\&quot;:\&quot;1\&quot;}，具体格式需要应用和设备约定。
        :type paras: object
        :param expire_time: 物联网平台缓存命令的时长， 单位秒。
        :type expire_time: int
        :param status: 设备命令状态,如果命令被缓存，返回PENDING, 如果命令下发给设备，返回SENT。
        :type status: str
        :param created_time: 命令的创建时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type created_time: str
        :param send_strategy: 下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。
        :type send_strategy: str
        """
        
        super(CreateAsyncCommandResponse, self).__init__()

        self._device_id = None
        self._command_id = None
        self._service_id = None
        self._command_name = None
        self._paras = None
        self._expire_time = None
        self._status = None
        self._created_time = None
        self._send_strategy = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if command_id is not None:
            self.command_id = command_id
        if service_id is not None:
            self.service_id = service_id
        if command_name is not None:
            self.command_name = command_name
        if paras is not None:
            self.paras = paras
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if send_strategy is not None:
            self.send_strategy = send_strategy

    @property
    def device_id(self):
        r"""Gets the device_id of this CreateAsyncCommandResponse.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :return: The device_id of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this CreateAsyncCommandResponse.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :param device_id: The device_id of this CreateAsyncCommandResponse.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def command_id(self):
        r"""Gets the command_id of this CreateAsyncCommandResponse.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :return: The command_id of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this CreateAsyncCommandResponse.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :param command_id: The command_id of this CreateAsyncCommandResponse.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def service_id(self):
        r"""Gets the service_id of this CreateAsyncCommandResponse.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this CreateAsyncCommandResponse.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this CreateAsyncCommandResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def command_name(self):
        r"""Gets the command_name of this CreateAsyncCommandResponse.

        设备命令名称，在设备关联的产品模型中定义。

        :return: The command_name of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        r"""Sets the command_name of this CreateAsyncCommandResponse.

        设备命令名称，在设备关联的产品模型中定义。

        :param command_name: The command_name of this CreateAsyncCommandResponse.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def paras(self):
        r"""Gets the paras of this CreateAsyncCommandResponse.

        设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\"value\":\"1\"}，具体格式需要应用和设备约定。

        :return: The paras of this CreateAsyncCommandResponse.
        :rtype: object
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        r"""Sets the paras of this CreateAsyncCommandResponse.

        设备执行的命令，Json格式，里面是一个个健值对，如果service_id不为空，每个健都是profile中命令的参数名（paraName）;如果service_id为空则由用户自定义命令格式。设备命令示例：{\"value\":\"1\"}，具体格式需要应用和设备约定。

        :param paras: The paras of this CreateAsyncCommandResponse.
        :type paras: object
        """
        self._paras = paras

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CreateAsyncCommandResponse.

        物联网平台缓存命令的时长， 单位秒。

        :return: The expire_time of this CreateAsyncCommandResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CreateAsyncCommandResponse.

        物联网平台缓存命令的时长， 单位秒。

        :param expire_time: The expire_time of this CreateAsyncCommandResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def status(self):
        r"""Gets the status of this CreateAsyncCommandResponse.

        设备命令状态,如果命令被缓存，返回PENDING, 如果命令下发给设备，返回SENT。

        :return: The status of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAsyncCommandResponse.

        设备命令状态,如果命令被缓存，返回PENDING, 如果命令下发给设备，返回SENT。

        :param status: The status of this CreateAsyncCommandResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateAsyncCommandResponse.

        命令的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateAsyncCommandResponse.

        命令的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this CreateAsyncCommandResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def send_strategy(self):
        r"""Gets the send_strategy of this CreateAsyncCommandResponse.

        下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。

        :return: The send_strategy of this CreateAsyncCommandResponse.
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        r"""Sets the send_strategy of this CreateAsyncCommandResponse.

        下发策略， immediately表示立即下发，delay表示缓存起来，等数据上报或者设备上线之后下发。

        :param send_strategy: The send_strategy of this CreateAsyncCommandResponse.
        :type send_strategy: str
        """
        self._send_strategy = send_strategy

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
        if not isinstance(other, CreateAsyncCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
