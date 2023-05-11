# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCostsRequest:

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
        'body': 'ListCostsReq'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, x_language=None, body=None):
        """ListCostsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。中文：zh_CN英文：en_US。缺省为zh_CN。
        :type x_language: str
        :param body: Body of the ListCostsRequest
        :type body: :class:`huaweicloudsdkbssintl.v2.ListCostsReq`
        """
        
        

        self._x_language = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this ListCostsRequest.

        语言。中文：zh_CN英文：en_US。缺省为zh_CN。

        :return: The x_language of this ListCostsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCostsRequest.

        语言。中文：zh_CN英文：en_US。缺省为zh_CN。

        :param x_language: The x_language of this ListCostsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this ListCostsRequest.

        :return: The body of this ListCostsRequest.
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCostsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListCostsRequest.

        :param body: The body of this ListCostsRequest.
        :type body: :class:`huaweicloudsdkbssintl.v2.ListCostsReq`
        """
        self._body = body

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
        if not isinstance(other, ListCostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
