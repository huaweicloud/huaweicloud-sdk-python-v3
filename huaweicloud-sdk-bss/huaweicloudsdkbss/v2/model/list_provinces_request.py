# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvincesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, offset=None, limit=None):
        r"""ListProvincesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，字段预留,目前仅支持中文。默认zh_cn，枚举：zh_cn：中文 en_us：英文
        :type x_language: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量，最大1000。
        :type limit: int
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListProvincesRequest.

        语言，字段预留,目前仅支持中文。默认zh_cn，枚举：zh_cn：中文 en_us：英文

        :return: The x_language of this ListProvincesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListProvincesRequest.

        语言，字段预留,目前仅支持中文。默认zh_cn，枚举：zh_cn：中文 en_us：英文

        :param x_language: The x_language of this ListProvincesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ListProvincesRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListProvincesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProvincesRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListProvincesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProvincesRequest.

        每次查询的数量，最大1000。

        :return: The limit of this ListProvincesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProvincesRequest.

        每次查询的数量，最大1000。

        :param limit: The limit of this ListProvincesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListProvincesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
