# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTtscVocabularyConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'x_app_user_id': 'str',
        'type': 'str',
        'limit': 'int',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'search_key': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'x_app_user_id': 'X-App-UserId',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'search_key': 'search_key'
    }

    def __init__(self, x_request_id=None, x_app_user_id=None, type=None, limit=None, offset=None, start_time=None, end_time=None, search_key=None):
        """ListTtscVocabularyConfigsRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成
        :type x_request_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param type: 自定义读法类型 CHINESE_G2P：拼音
        :type type: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param start_time: 起始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;。
        :type end_time: str
        :param search_key: 搜索条件
        :type search_key: str
        """
        
        

        self._x_request_id = None
        self._x_app_user_id = None
        self._type = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self._search_key = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if search_key is not None:
            self.search_key = search_key

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListTtscVocabularyConfigsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :return: The x_request_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListTtscVocabularyConfigsRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :param x_request_id: The x_request_id of this ListTtscVocabularyConfigsRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ListTtscVocabularyConfigsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ListTtscVocabularyConfigsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListTtscVocabularyConfigsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def type(self):
        """Gets the type of this ListTtscVocabularyConfigsRequest.

        自定义读法类型 CHINESE_G2P：拼音

        :return: The type of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListTtscVocabularyConfigsRequest.

        自定义读法类型 CHINESE_G2P：拼音

        :param type: The type of this ListTtscVocabularyConfigsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListTtscVocabularyConfigsRequest.

        每页显示的条目数量。

        :return: The limit of this ListTtscVocabularyConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTtscVocabularyConfigsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListTtscVocabularyConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTtscVocabularyConfigsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListTtscVocabularyConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTtscVocabularyConfigsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListTtscVocabularyConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this ListTtscVocabularyConfigsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListTtscVocabularyConfigsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ListTtscVocabularyConfigsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListTtscVocabularyConfigsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :return: The end_time of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListTtscVocabularyConfigsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :param end_time: The end_time of this ListTtscVocabularyConfigsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def search_key(self):
        """Gets the search_key of this ListTtscVocabularyConfigsRequest.

        搜索条件

        :return: The search_key of this ListTtscVocabularyConfigsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ListTtscVocabularyConfigsRequest.

        搜索条件

        :param search_key: The search_key of this ListTtscVocabularyConfigsRequest.
        :type search_key: str
        """
        self._search_key = search_key

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
        if not isinstance(other, ListTtscVocabularyConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
