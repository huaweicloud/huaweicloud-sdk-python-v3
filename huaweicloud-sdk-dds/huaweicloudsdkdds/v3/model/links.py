# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Links:

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
        r"""Links

        The model defined in huaweicloud sdk

        :param href: 对应该API的URL，该字段为\&quot;\&quot;。
        :type href: str
        :param rel: 值为“self”，表示URL为本地链接。
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
        r"""Gets the href of this Links.

        对应该API的URL，该字段为\"\"。

        :return: The href of this Links.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        r"""Sets the href of this Links.

        对应该API的URL，该字段为\"\"。

        :param href: The href of this Links.
        :type href: str
        """
        self._href = href

    @property
    def rel(self):
        r"""Gets the rel of this Links.

        值为“self”，表示URL为本地链接。

        :return: The rel of this Links.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        r"""Sets the rel of this Links.

        值为“self”，表示URL为本地链接。

        :param rel: The rel of this Links.
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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
