# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'contents': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'contents': 'contents'
    }

    def __init__(self, category=None, contents=None):
        r"""TagCondition

        The model defined in huaweicloud sdk

        :param category: 防护动作
        :type category: str
        :param contents: 字段内容
        :type contents: list[str]
        """
        
        

        self._category = None
        self._contents = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents

    @property
    def category(self):
        r"""Gets the category of this TagCondition.

        防护动作

        :return: The category of this TagCondition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TagCondition.

        防护动作

        :param category: The category of this TagCondition.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this TagCondition.

        字段内容

        :return: The contents of this TagCondition.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this TagCondition.

        字段内容

        :param contents: The contents of this TagCondition.
        :type contents: list[str]
        """
        self._contents = contents

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
        if not isinstance(other, TagCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
