# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCountiesRequest:

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
        'city_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'city_code': 'city_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, city_code=None, offset=None, limit=None):
        """ListCountiesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。zh_CN：中文en_us：英文缺省为zh_CN。
        :type x_language: str
        :param city_code: 城市的编码。
        :type city_code: str
        :param offset: 偏移量，从0开始。默认值为0。此参数不携带或携带值为null时，取默认值0；不支持携带值为空。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量，最大1000。默认值为10。此参数不携带，取默认值10；不支持携带值为空和携带值为null。
        :type limit: int
        """
        
        

        self._x_language = None
        self._city_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.city_code = city_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListCountiesRequest.

        语言。zh_CN：中文en_us：英文缺省为zh_CN。

        :return: The x_language of this ListCountiesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCountiesRequest.

        语言。zh_CN：中文en_us：英文缺省为zh_CN。

        :param x_language: The x_language of this ListCountiesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def city_code(self):
        """Gets the city_code of this ListCountiesRequest.

        城市的编码。

        :return: The city_code of this ListCountiesRequest.
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        """Sets the city_code of this ListCountiesRequest.

        城市的编码。

        :param city_code: The city_code of this ListCountiesRequest.
        :type city_code: str
        """
        self._city_code = city_code

    @property
    def offset(self):
        """Gets the offset of this ListCountiesRequest.

        偏移量，从0开始。默认值为0。此参数不携带或携带值为null时，取默认值0；不支持携带值为空。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListCountiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCountiesRequest.

        偏移量，从0开始。默认值为0。此参数不携带或携带值为null时，取默认值0；不支持携带值为空。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListCountiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCountiesRequest.

        每次查询的数量，最大1000。默认值为10。此参数不携带，取默认值10；不支持携带值为空和携带值为null。

        :return: The limit of this ListCountiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCountiesRequest.

        每次查询的数量，最大1000。默认值为10。此参数不携带，取默认值10；不支持携带值为空和携带值为null。

        :param limit: The limit of this ListCountiesRequest.
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
        if not isinstance(other, ListCountiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
