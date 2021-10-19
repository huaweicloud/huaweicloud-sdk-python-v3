# coding: utf-8

import re
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
        'type': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'href': 'href',
        'type': 'type',
        'rel': 'rel'
    }

    def __init__(self, href=None, type=None, rel=None):
        """Links - a model defined in huaweicloud sdk"""
        
        

        self._href = None
        self._type = None
        self._rel = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if type is not None:
            self.type = type
        if rel is not None:
            self.rel = rel

    @property
    def href(self):
        """Gets the href of this Links.

        当前API版本的引用地址。

        :return: The href of this Links.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Links.

        当前API版本的引用地址。

        :param href: The href of this Links.
        :type: str
        """
        self._href = href

    @property
    def type(self):
        """Gets the type of this Links.

        发送的实体的MIME类型，取值为application/json。

        :return: The type of this Links.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Links.

        发送的实体的MIME类型，取值为application/json。

        :param type: The type of this Links.
        :type: str
        """
        self._type = type

    @property
    def rel(self):
        """Gets the rel of this Links.

        当前API版本和被引用地址的关系。

        :return: The rel of this Links.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Links.

        当前API版本和被引用地址的关系。

        :param rel: The rel of this Links.
        :type: str
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
