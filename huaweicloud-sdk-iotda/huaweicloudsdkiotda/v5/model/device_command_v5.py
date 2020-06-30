# coding: utf-8

import pprint
import re

import six


class DeviceCommandV5(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'command_id': 'str',
        'command_name': 'str',
        'service_id': 'str',
        'paras': 'object',
        'status': 'str',
        'created_time': 'str',
        'finished_time': 'str',
        'response': 'object'
    }

    attribute_map = {
        'command_id': 'command_id',
        'command_name': 'command_name',
        'service_id': 'service_id',
        'paras': 'paras',
        'status': 'status',
        'created_time': 'created_time',
        'finished_time': 'finished_time',
        'response': 'response'
    }

    def __init__(self, command_id=None, command_name=None, service_id=None, paras=None, status=None, created_time=None, finished_time=None, response=None):  # noqa: E501
        """DeviceCommandV5 - a model defined in huaweicloud sdk"""

        self._command_id = None
        self._command_name = None
        self._service_id = None
        self._paras = None
        self._status = None
        self._created_time = None
        self._finished_time = None
        self._response = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name
        if service_id is not None:
            self.service_id = service_id
        if paras is not None:
            self.paras = paras
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if finished_time is not None:
            self.finished_time = finished_time
        if response is not None:
            self.response = response

    @property
    def command_id(self):
        """Gets the command_id of this DeviceCommandV5.

        设备命令ID，用于唯一标识一条消息，在下发设备消息时由物联网平台分配获得。

        :return: The command_id of this DeviceCommandV5.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this DeviceCommandV5.

        设备命令ID，用于唯一标识一条消息，在下发设备消息时由物联网平台分配获得。

        :param command_id: The command_id of this DeviceCommandV5.
        :type: str
        """
        self._command_id = command_id

    @property
    def command_name(self):
        """Gets the command_name of this DeviceCommandV5.

        命令名称,在下发命令时由用户指定。

        :return: The command_name of this DeviceCommandV5.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this DeviceCommandV5.

        命令名称,在下发命令时由用户指定。

        :param command_name: The command_name of this DeviceCommandV5.
        :type: str
        """
        self._command_name = command_name

    @property
    def service_id(self):
        """Gets the service_id of this DeviceCommandV5.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this DeviceCommandV5.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DeviceCommandV5.

        设备命令所属的设备服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this DeviceCommandV5.
        :type: str
        """
        self._service_id = service_id

    @property
    def paras(self):
        """Gets the paras of this DeviceCommandV5.

        命令内容

        :return: The paras of this DeviceCommandV5.
        :rtype: object
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this DeviceCommandV5.

        命令内容

        :param paras: The paras of this DeviceCommandV5.
        :type: object
        """
        self._paras = paras

    @property
    def status(self):
        """Gets the status of this DeviceCommandV5.

        命令状态，包含FAILED, SUCCESSFUL和TIMEOUT几种。

        :return: The status of this DeviceCommandV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceCommandV5.

        命令状态，包含FAILED, SUCCESSFUL和TIMEOUT几种。

        :param status: The status of this DeviceCommandV5.
        :type: str
        """
        self._status = status

    @property
    def created_time(self):
        """Gets the created_time of this DeviceCommandV5.

        命令创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this DeviceCommandV5.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DeviceCommandV5.

        命令创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this DeviceCommandV5.
        :type: str
        """
        self._created_time = created_time

    @property
    def finished_time(self):
        """Gets the finished_time of this DeviceCommandV5.

        命令结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The finished_time of this DeviceCommandV5.
        :rtype: str
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        """Sets the finished_time of this DeviceCommandV5.

        命令结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param finished_time: The finished_time of this DeviceCommandV5.
        :type: str
        """
        self._finished_time = finished_time

    @property
    def response(self):
        """Gets the response of this DeviceCommandV5.

        设备上报给平台的命令响应结果。

        :return: The response of this DeviceCommandV5.
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this DeviceCommandV5.

        设备上报给平台的命令响应结果。

        :param response: The response of this DeviceCommandV5.
        :type: object
        """
        self._response = response

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceCommandV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
