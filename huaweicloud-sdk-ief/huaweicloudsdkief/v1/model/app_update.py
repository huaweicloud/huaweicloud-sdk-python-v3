# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'description': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'description': 'description'
    }

    def __init__(self, alias=None, description=None):
        r"""AppUpdate

        The model defined in huaweicloud sdk

        :param alias: 应用模板别名，中文、英文字母、数字、中划线、下划线，最大64字符
        :type alias: str
        :param description: 应用模板描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        """
        
        

        self._alias = None
        self._description = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description

    @property
    def alias(self):
        r"""Gets the alias of this AppUpdate.

        应用模板别名，中文、英文字母、数字、中划线、下划线，最大64字符

        :return: The alias of this AppUpdate.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AppUpdate.

        应用模板别名，中文、英文字母、数字、中划线、下划线，最大64字符

        :param alias: The alias of this AppUpdate.
        :type alias: str
        """
        self._alias = alias

    @property
    def description(self):
        r"""Gets the description of this AppUpdate.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this AppUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppUpdate.

        应用模板描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this AppUpdate.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AppUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
