# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeroleSessionuser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str'
    }

    attribute_map = {
        'name': 'name'
    }

    def __init__(self, name=None):
        """AssumeroleSessionuser

        The model defined in huaweicloud sdk

        :param name: 委托方对应的企业用户名。用户名需满足如下规则：长度5~64，只能包含大写字母、小写字母、数字（0-9）、特殊字符（\&quot;-\&quot;与\&quot;_\&quot;）且只能以字母开头。
        :type name: str
        """
        
        

        self._name = None
        self.discriminator = None

        if name is not None:
            self.name = name

    @property
    def name(self):
        """Gets the name of this AssumeroleSessionuser.

        委托方对应的企业用户名。用户名需满足如下规则：长度5~64，只能包含大写字母、小写字母、数字（0-9）、特殊字符（\"-\"与\"_\"）且只能以字母开头。

        :return: The name of this AssumeroleSessionuser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssumeroleSessionuser.

        委托方对应的企业用户名。用户名需满足如下规则：长度5~64，只能包含大写字母、小写字母、数字（0-9）、特殊字符（\"-\"与\"_\"）且只能以字母开头。

        :param name: The name of this AssumeroleSessionuser.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AssumeroleSessionuser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
