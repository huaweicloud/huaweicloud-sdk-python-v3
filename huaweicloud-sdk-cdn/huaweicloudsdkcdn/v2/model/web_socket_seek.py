# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebSocketSeek:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'status': 'status',
        'timeout': 'timeout'
    }

    def __init__(self, status=None, timeout=None):
        """WebSocketSeek

        The model defined in huaweicloud sdk

        :param status: 开关， on 开启，off 关闭。
        :type status: str
        :param timeout: 请求建立连接后，会话的保持时间：范围：1-300，单位：秒。
        :type timeout: int
        """
        
        

        self._status = None
        self._timeout = None
        self.discriminator = None

        self.status = status
        self.timeout = timeout

    @property
    def status(self):
        """Gets the status of this WebSocketSeek.

        开关， on 开启，off 关闭。

        :return: The status of this WebSocketSeek.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebSocketSeek.

        开关， on 开启，off 关闭。

        :param status: The status of this WebSocketSeek.
        :type status: str
        """
        self._status = status

    @property
    def timeout(self):
        """Gets the timeout of this WebSocketSeek.

        请求建立连接后，会话的保持时间：范围：1-300，单位：秒。

        :return: The timeout of this WebSocketSeek.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this WebSocketSeek.

        请求建立连接后，会话的保持时间：范围：1-300，单位：秒。

        :param timeout: The timeout of this WebSocketSeek.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, WebSocketSeek):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
