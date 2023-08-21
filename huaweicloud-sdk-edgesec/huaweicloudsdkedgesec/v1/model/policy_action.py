# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str'
    }

    attribute_map = {
        'category': 'category'
    }

    def __init__(self, category=None):
        """PolicyAction

        The model defined in huaweicloud sdk

        :param category: web基础防护动作（log为仅记录、block为拦截）
        :type category: str
        """
        
        

        self._category = None
        self.discriminator = None

        if category is not None:
            self.category = category

    @property
    def category(self):
        """Gets the category of this PolicyAction.

        web基础防护动作（log为仅记录、block为拦截）

        :return: The category of this PolicyAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PolicyAction.

        web基础防护动作（log为仅记录、block为拦截）

        :param category: The category of this PolicyAction.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, PolicyAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
