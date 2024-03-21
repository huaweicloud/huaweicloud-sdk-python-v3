# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortStatisticResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'type': 'str',
        'num': 'int',
        'status': 'str'
    }

    attribute_map = {
        'port': 'port',
        'type': 'type',
        'num': 'num',
        'status': 'status'
    }

    def __init__(self, port=None, type=None, num=None, status=None):
        """PortStatisticResponseInfo

        The model defined in huaweicloud sdk

        :param port: 端口号
        :type port: int
        :param type: 端口类型
        :type type: str
        :param num: 端口数量
        :type num: int
        :param status: 危险类型:danger/unknown
        :type status: str
        """
        
        

        self._port = None
        self._type = None
        self._num = None
        self._status = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if num is not None:
            self.num = num
        if status is not None:
            self.status = status

    @property
    def port(self):
        """Gets the port of this PortStatisticResponseInfo.

        端口号

        :return: The port of this PortStatisticResponseInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortStatisticResponseInfo.

        端口号

        :param port: The port of this PortStatisticResponseInfo.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this PortStatisticResponseInfo.

        端口类型

        :return: The type of this PortStatisticResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortStatisticResponseInfo.

        端口类型

        :param type: The type of this PortStatisticResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def num(self):
        """Gets the num of this PortStatisticResponseInfo.

        端口数量

        :return: The num of this PortStatisticResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this PortStatisticResponseInfo.

        端口数量

        :param num: The num of this PortStatisticResponseInfo.
        :type num: int
        """
        self._num = num

    @property
    def status(self):
        """Gets the status of this PortStatisticResponseInfo.

        危险类型:danger/unknown

        :return: The status of this PortStatisticResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortStatisticResponseInfo.

        危险类型:danger/unknown

        :param status: The status of this PortStatisticResponseInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PortStatisticResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
