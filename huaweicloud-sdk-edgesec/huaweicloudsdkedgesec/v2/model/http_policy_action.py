# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpPolicyAction:

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
        'followed_action_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'followed_action_id': 'followed_action_id'
    }

    def __init__(self, category=None, followed_action_id=None):
        r"""HttpPolicyAction

        The model defined in huaweicloud sdk

        :param category: 防护等级
        :type category: str
        :param followed_action_id: 攻击惩罚规则ID
        :type followed_action_id: str
        """
        
        

        self._category = None
        self._followed_action_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if followed_action_id is not None:
            self.followed_action_id = followed_action_id

    @property
    def category(self):
        r"""Gets the category of this HttpPolicyAction.

        防护等级

        :return: The category of this HttpPolicyAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this HttpPolicyAction.

        防护等级

        :param category: The category of this HttpPolicyAction.
        :type category: str
        """
        self._category = category

    @property
    def followed_action_id(self):
        r"""Gets the followed_action_id of this HttpPolicyAction.

        攻击惩罚规则ID

        :return: The followed_action_id of this HttpPolicyAction.
        :rtype: str
        """
        return self._followed_action_id

    @followed_action_id.setter
    def followed_action_id(self, followed_action_id):
        r"""Sets the followed_action_id of this HttpPolicyAction.

        攻击惩罚规则ID

        :param followed_action_id: The followed_action_id of this HttpPolicyAction.
        :type followed_action_id: str
        """
        self._followed_action_id = followed_action_id

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
        if not isinstance(other, HttpPolicyAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
