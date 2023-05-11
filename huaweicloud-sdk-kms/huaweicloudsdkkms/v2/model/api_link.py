# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiLink:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'href': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel'
    }

    def __init__(self, href=None, rel=None):
        """ApiLink

        The model defined in huaweicloud sdk

        :param href: API的URL地址。
        :type href: str
        :param rel: 默认值self。
        :type rel: str
        """
        
        

        self._href = None
        self._rel = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel

    @property
    def href(self):
        """Gets the href of this ApiLink.

        API的URL地址。

        :return: The href of this ApiLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ApiLink.

        API的URL地址。

        :param href: The href of this ApiLink.
        :type href: str
        """
        self._href = href

    @property
    def rel(self):
        """Gets the rel of this ApiLink.

        默认值self。

        :return: The rel of this ApiLink.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this ApiLink.

        默认值self。

        :param rel: The rel of this ApiLink.
        :type rel: str
        """
        self._rel = rel

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
        if not isinstance(other, ApiLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
