# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTtsPhoneticSymbolRequest:

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
        'offset': 'int',
        'limit': 'int',
        'word': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'word': 'word'
    }

    def __init__(self, x_request_id=None, x_app_user_id=None, offset=None, limit=None, word=None):
        r"""ShowTtsPhoneticSymbolRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成
        :type x_request_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页
        :type offset: int
        :param limit: 查询数量
        :type limit: int
        :param word: 英文单词
        :type word: str
        """
        
        

        self._x_request_id = None
        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._word = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.word = word

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowTtsPhoneticSymbolRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :return: The x_request_id of this ShowTtsPhoneticSymbolRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowTtsPhoneticSymbolRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :param x_request_id: The x_request_id of this ShowTtsPhoneticSymbolRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ShowTtsPhoneticSymbolRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ShowTtsPhoneticSymbolRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ShowTtsPhoneticSymbolRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ShowTtsPhoneticSymbolRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowTtsPhoneticSymbolRequest.

        查询偏移量,若超过最大数量，则返回最后一页

        :return: The offset of this ShowTtsPhoneticSymbolRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTtsPhoneticSymbolRequest.

        查询偏移量,若超过最大数量，则返回最后一页

        :param offset: The offset of this ShowTtsPhoneticSymbolRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowTtsPhoneticSymbolRequest.

        查询数量

        :return: The limit of this ShowTtsPhoneticSymbolRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTtsPhoneticSymbolRequest.

        查询数量

        :param limit: The limit of this ShowTtsPhoneticSymbolRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def word(self):
        r"""Gets the word of this ShowTtsPhoneticSymbolRequest.

        英文单词

        :return: The word of this ShowTtsPhoneticSymbolRequest.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        r"""Sets the word of this ShowTtsPhoneticSymbolRequest.

        英文单词

        :param word: The word of this ShowTtsPhoneticSymbolRequest.
        :type word: str
        """
        self._word = word

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
        if not isinstance(other, ShowTtsPhoneticSymbolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
