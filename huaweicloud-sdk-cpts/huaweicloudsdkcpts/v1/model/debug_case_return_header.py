# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugCaseReturnHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection': 'str',
        'content_length': 'str',
        'content_type': 'str',
        'date': 'str',
        'vary': 'str'
    }

    attribute_map = {
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'content_type': 'Content-Type',
        'date': 'Date',
        'vary': 'Vary'
    }

    def __init__(self, connection=None, content_length=None, content_type=None, date=None, vary=None):
        """DebugCaseReturnHeader

        The model defined in huaweicloud sdk

        :param connection: 连接
        :type connection: str
        :param content_length: 内容长度
        :type content_length: str
        :param content_type: 内容类型
        :type content_type: str
        :param date: 时间
        :type date: str
        :param vary: 兼容性保留，当前版本未使用
        :type vary: str
        """
        
        

        self._connection = None
        self._content_length = None
        self._content_type = None
        self._date = None
        self._vary = None
        self.discriminator = None

        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if content_type is not None:
            self.content_type = content_type
        if date is not None:
            self.date = date
        if vary is not None:
            self.vary = vary

    @property
    def connection(self):
        """Gets the connection of this DebugCaseReturnHeader.

        连接

        :return: The connection of this DebugCaseReturnHeader.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this DebugCaseReturnHeader.

        连接

        :param connection: The connection of this DebugCaseReturnHeader.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this DebugCaseReturnHeader.

        内容长度

        :return: The content_length of this DebugCaseReturnHeader.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this DebugCaseReturnHeader.

        内容长度

        :param content_length: The content_length of this DebugCaseReturnHeader.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this DebugCaseReturnHeader.

        内容类型

        :return: The content_type of this DebugCaseReturnHeader.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this DebugCaseReturnHeader.

        内容类型

        :param content_type: The content_type of this DebugCaseReturnHeader.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def date(self):
        """Gets the date of this DebugCaseReturnHeader.

        时间

        :return: The date of this DebugCaseReturnHeader.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DebugCaseReturnHeader.

        时间

        :param date: The date of this DebugCaseReturnHeader.
        :type date: str
        """
        self._date = date

    @property
    def vary(self):
        """Gets the vary of this DebugCaseReturnHeader.

        兼容性保留，当前版本未使用

        :return: The vary of this DebugCaseReturnHeader.
        :rtype: str
        """
        return self._vary

    @vary.setter
    def vary(self, vary):
        """Sets the vary of this DebugCaseReturnHeader.

        兼容性保留，当前版本未使用

        :param vary: The vary of this DebugCaseReturnHeader.
        :type vary: str
        """
        self._vary = vary

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
        if not isinstance(other, DebugCaseReturnHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
