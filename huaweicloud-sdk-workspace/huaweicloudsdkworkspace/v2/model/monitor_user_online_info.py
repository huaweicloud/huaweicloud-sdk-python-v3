# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonitorUserOnlineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'encoded_authorization_message': 'str',
        'connection_setup_time': 'str',
        'connection_end_time': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'encoded_authorization_message': 'encoded_authorization_message',
        'connection_setup_time': 'connection_setup_time',
        'connection_end_time': 'connection_end_time'
    }

    def __init__(self, error_code=None, error_msg=None, encoded_authorization_message=None, connection_setup_time=None, connection_end_time=None):
        r"""MonitorUserOnlineInfo

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param encoded_authorization_message: 加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。
        :type encoded_authorization_message: str
        :param connection_setup_time: 建立连接时间。
        :type connection_setup_time: str
        :param connection_end_time: 结束连接时间。
        :type connection_end_time: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._encoded_authorization_message = None
        self._connection_setup_time = None
        self._connection_end_time = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if encoded_authorization_message is not None:
            self.encoded_authorization_message = encoded_authorization_message
        if connection_setup_time is not None:
            self.connection_setup_time = connection_setup_time
        if connection_end_time is not None:
            self.connection_end_time = connection_end_time

    @property
    def error_code(self):
        r"""Gets the error_code of this MonitorUserOnlineInfo.

        错误码。

        :return: The error_code of this MonitorUserOnlineInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this MonitorUserOnlineInfo.

        错误码。

        :param error_code: The error_code of this MonitorUserOnlineInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this MonitorUserOnlineInfo.

        错误描述。

        :return: The error_msg of this MonitorUserOnlineInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this MonitorUserOnlineInfo.

        错误描述。

        :param error_msg: The error_msg of this MonitorUserOnlineInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def encoded_authorization_message(self):
        r"""Gets the encoded_authorization_message of this MonitorUserOnlineInfo.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :return: The encoded_authorization_message of this MonitorUserOnlineInfo.
        :rtype: str
        """
        return self._encoded_authorization_message

    @encoded_authorization_message.setter
    def encoded_authorization_message(self, encoded_authorization_message):
        r"""Sets the encoded_authorization_message of this MonitorUserOnlineInfo.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :param encoded_authorization_message: The encoded_authorization_message of this MonitorUserOnlineInfo.
        :type encoded_authorization_message: str
        """
        self._encoded_authorization_message = encoded_authorization_message

    @property
    def connection_setup_time(self):
        r"""Gets the connection_setup_time of this MonitorUserOnlineInfo.

        建立连接时间。

        :return: The connection_setup_time of this MonitorUserOnlineInfo.
        :rtype: str
        """
        return self._connection_setup_time

    @connection_setup_time.setter
    def connection_setup_time(self, connection_setup_time):
        r"""Sets the connection_setup_time of this MonitorUserOnlineInfo.

        建立连接时间。

        :param connection_setup_time: The connection_setup_time of this MonitorUserOnlineInfo.
        :type connection_setup_time: str
        """
        self._connection_setup_time = connection_setup_time

    @property
    def connection_end_time(self):
        r"""Gets the connection_end_time of this MonitorUserOnlineInfo.

        结束连接时间。

        :return: The connection_end_time of this MonitorUserOnlineInfo.
        :rtype: str
        """
        return self._connection_end_time

    @connection_end_time.setter
    def connection_end_time(self, connection_end_time):
        r"""Sets the connection_end_time of this MonitorUserOnlineInfo.

        结束连接时间。

        :param connection_end_time: The connection_end_time of this MonitorUserOnlineInfo.
        :type connection_end_time: str
        """
        self._connection_end_time = connection_end_time

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
        if not isinstance(other, MonitorUserOnlineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
