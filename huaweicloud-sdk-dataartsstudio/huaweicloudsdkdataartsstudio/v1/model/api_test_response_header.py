# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiTestResponseHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_status': 'str',
        'content_length': 'int',
        'connection': 'str',
        'cache_control': 'str',
        'content_type': 'str',
        'date': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result_status': 'result_status',
        'content_length': 'content_length',
        'connection': 'connection',
        'cache_control': 'cache_control',
        'content_type': 'content_type',
        'date': 'date',
        'x_request_id': 'x_request_id'
    }

    def __init__(self, result_status=None, content_length=None, connection=None, cache_control=None, content_type=None, date=None, x_request_id=None):
        r"""ApiTestResponseHeader

        The model defined in huaweicloud sdk

        :param result_status: 是否成功
        :type result_status: str
        :param content_length: 内容大小
        :type content_length: int
        :param connection: 连接状态
        :type connection: str
        :param cache_control: 缓存控制（固定值）
        :type cache_control: str
        :param content_type: 内容类型 （固定值）
        :type content_type: str
        :param date: 日期
        :type date: str
        :param x_request_id: 请求ID
        :type x_request_id: str
        """
        
        

        self._result_status = None
        self._content_length = None
        self._connection = None
        self._cache_control = None
        self._content_type = None
        self._date = None
        self._x_request_id = None
        self.discriminator = None

        if result_status is not None:
            self.result_status = result_status
        if content_length is not None:
            self.content_length = content_length
        if connection is not None:
            self.connection = connection
        if cache_control is not None:
            self.cache_control = cache_control
        if content_type is not None:
            self.content_type = content_type
        if date is not None:
            self.date = date
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result_status(self):
        r"""Gets the result_status of this ApiTestResponseHeader.

        是否成功

        :return: The result_status of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._result_status

    @result_status.setter
    def result_status(self, result_status):
        r"""Sets the result_status of this ApiTestResponseHeader.

        是否成功

        :param result_status: The result_status of this ApiTestResponseHeader.
        :type result_status: str
        """
        self._result_status = result_status

    @property
    def content_length(self):
        r"""Gets the content_length of this ApiTestResponseHeader.

        内容大小

        :return: The content_length of this ApiTestResponseHeader.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ApiTestResponseHeader.

        内容大小

        :param content_length: The content_length of this ApiTestResponseHeader.
        :type content_length: int
        """
        self._content_length = content_length

    @property
    def connection(self):
        r"""Gets the connection of this ApiTestResponseHeader.

        连接状态

        :return: The connection of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ApiTestResponseHeader.

        连接状态

        :param connection: The connection of this ApiTestResponseHeader.
        :type connection: str
        """
        self._connection = connection

    @property
    def cache_control(self):
        r"""Gets the cache_control of this ApiTestResponseHeader.

        缓存控制（固定值）

        :return: The cache_control of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._cache_control

    @cache_control.setter
    def cache_control(self, cache_control):
        r"""Sets the cache_control of this ApiTestResponseHeader.

        缓存控制（固定值）

        :param cache_control: The cache_control of this ApiTestResponseHeader.
        :type cache_control: str
        """
        self._cache_control = cache_control

    @property
    def content_type(self):
        r"""Gets the content_type of this ApiTestResponseHeader.

        内容类型 （固定值）

        :return: The content_type of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ApiTestResponseHeader.

        内容类型 （固定值）

        :param content_type: The content_type of this ApiTestResponseHeader.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def date(self):
        r"""Gets the date of this ApiTestResponseHeader.

        日期

        :return: The date of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ApiTestResponseHeader.

        日期

        :param date: The date of this ApiTestResponseHeader.
        :type date: str
        """
        self._date = date

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ApiTestResponseHeader.

        请求ID

        :return: The x_request_id of this ApiTestResponseHeader.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ApiTestResponseHeader.

        请求ID

        :param x_request_id: The x_request_id of this ApiTestResponseHeader.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ApiTestResponseHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
