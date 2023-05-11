# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvidersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'track': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'track': 'track',
        'x_language': 'X-Language'
    }

    def __init__(self, offset=None, limit=None, track=None, x_language=None):
        """ListProvidersRequest

        The model defined in huaweicloud sdk

        :param offset: 分页偏移
        :type offset: int
        :param limit: 最大的返回数量
        :type limit: int
        :param track: 资源是否默认收集
        :type track: str
        :param x_language: 选择接口返回的信息的语言，默认为\&quot;zh-cn\&quot;中文
        :type x_language: str
        """
        
        

        self._offset = None
        self._limit = None
        self._track = None
        self._x_language = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if track is not None:
            self.track = track
        if x_language is not None:
            self.x_language = x_language

    @property
    def offset(self):
        """Gets the offset of this ListProvidersRequest.

        分页偏移

        :return: The offset of this ListProvidersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProvidersRequest.

        分页偏移

        :param offset: The offset of this ListProvidersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProvidersRequest.

        最大的返回数量

        :return: The limit of this ListProvidersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProvidersRequest.

        最大的返回数量

        :param limit: The limit of this ListProvidersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def track(self):
        """Gets the track of this ListProvidersRequest.

        资源是否默认收集

        :return: The track of this ListProvidersRequest.
        :rtype: str
        """
        return self._track

    @track.setter
    def track(self, track):
        """Sets the track of this ListProvidersRequest.

        资源是否默认收集

        :param track: The track of this ListProvidersRequest.
        :type track: str
        """
        self._track = track

    @property
    def x_language(self):
        """Gets the x_language of this ListProvidersRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :return: The x_language of this ListProvidersRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListProvidersRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :param x_language: The x_language of this ListProvidersRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListProvidersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
