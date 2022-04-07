# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceTypesRequest:


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
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, limit=None, offset=None):
        """ListServiceTypesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        """Gets the x_language of this ListServiceTypesRequest.

        |缺省为zh_CN。 zh_CN：中文 en_US：英文|

        :return: The x_language of this ListServiceTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListServiceTypesRequest.

        |缺省为zh_CN。 zh_CN：中文 en_US：英文|

        :param x_language: The x_language of this ListServiceTypesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        """Gets the limit of this ListServiceTypesRequest.

        |参数名称：每次查询的数量。默认值为10。| |参数的约束及描述：每页大小，缺省为1000。|

        :return: The limit of this ListServiceTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServiceTypesRequest.

        |参数名称：每次查询的数量。默认值为10。| |参数的约束及描述：每页大小，缺省为1000。|

        :param limit: The limit of this ListServiceTypesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServiceTypesRequest.

        |参数名称：页数，从0开始。默认值为0。| |参数的约束及描述：从0开始。默认值为0。|

        :return: The offset of this ListServiceTypesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServiceTypesRequest.

        |参数名称：页数，从0开始。默认值为0。| |参数的约束及描述：从0开始。默认值为0。|

        :param offset: The offset of this ListServiceTypesRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListServiceTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
