# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendCommandRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'command_id': 'int',
        'is_sync': 'bool',
        'requests': 'list[RequestParameter]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'command_id': 'command_id',
        'is_sync': 'is_sync',
        'requests': 'requests'
    }

    def __init__(self, service_id=None, command_id=None, is_sync=None, requests=None):
        """SendCommandRequestBody

        The model defined in huaweicloud sdk

        :param service_id: 服务ID，自动向下取整
        :type service_id: int
        :param command_id: 命令ID，自动向下取整
        :type command_id: int
        :param is_sync: 命令是否同步 true-同步 false-异步 同步命令会将命令以MQTT消息发送给设备后等待设备的MQTT命令响应，收到响应后再回复响应（默认超时5秒），异步命令则以立即返回响应
        :type is_sync: bool
        :param requests: 请求参数列表
        :type requests: list[:class:`huaweicloudsdkroma.v2.RequestParameter`]
        """
        
        

        self._service_id = None
        self._command_id = None
        self._is_sync = None
        self._requests = None
        self.discriminator = None

        self.service_id = service_id
        self.command_id = command_id
        self.is_sync = is_sync
        if requests is not None:
            self.requests = requests

    @property
    def service_id(self):
        """Gets the service_id of this SendCommandRequestBody.

        服务ID，自动向下取整

        :return: The service_id of this SendCommandRequestBody.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this SendCommandRequestBody.

        服务ID，自动向下取整

        :param service_id: The service_id of this SendCommandRequestBody.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def command_id(self):
        """Gets the command_id of this SendCommandRequestBody.

        命令ID，自动向下取整

        :return: The command_id of this SendCommandRequestBody.
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this SendCommandRequestBody.

        命令ID，自动向下取整

        :param command_id: The command_id of this SendCommandRequestBody.
        :type command_id: int
        """
        self._command_id = command_id

    @property
    def is_sync(self):
        """Gets the is_sync of this SendCommandRequestBody.

        命令是否同步 true-同步 false-异步 同步命令会将命令以MQTT消息发送给设备后等待设备的MQTT命令响应，收到响应后再回复响应（默认超时5秒），异步命令则以立即返回响应

        :return: The is_sync of this SendCommandRequestBody.
        :rtype: bool
        """
        return self._is_sync

    @is_sync.setter
    def is_sync(self, is_sync):
        """Sets the is_sync of this SendCommandRequestBody.

        命令是否同步 true-同步 false-异步 同步命令会将命令以MQTT消息发送给设备后等待设备的MQTT命令响应，收到响应后再回复响应（默认超时5秒），异步命令则以立即返回响应

        :param is_sync: The is_sync of this SendCommandRequestBody.
        :type is_sync: bool
        """
        self._is_sync = is_sync

    @property
    def requests(self):
        """Gets the requests of this SendCommandRequestBody.

        请求参数列表

        :return: The requests of this SendCommandRequestBody.
        :rtype: list[:class:`huaweicloudsdkroma.v2.RequestParameter`]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this SendCommandRequestBody.

        请求参数列表

        :param requests: The requests of this SendCommandRequestBody.
        :type requests: list[:class:`huaweicloudsdkroma.v2.RequestParameter`]
        """
        self._requests = requests

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
        if not isinstance(other, SendCommandRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
