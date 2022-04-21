# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTopicAccessPolicyTopicsObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'policies': 'list[UpdateTopicAccessPolicyPoliciesObject]',
        'description': 'str',
        'sensitive_word': 'str'
    }

    attribute_map = {
        'name': 'name',
        'policies': 'policies',
        'description': 'description',
        'sensitive_word': 'sensitive_word'
    }

    def __init__(self, name=None, policies=None, description=None, sensitive_word=None):
        """UpdateTopicAccessPolicyTopicsObject

        The model defined in huaweicloud sdk

        :param name: topic名称。
        :type name: str
        :param policies: 权限列表。
        :type policies: list[:class:`huaweicloudsdkroma.v2.UpdateTopicAccessPolicyPoliciesObject`]
        :param description: 描述。
        :type description: str
        :param sensitive_word: 敏感字段。
        :type sensitive_word: str
        """
        
        

        self._name = None
        self._policies = None
        self._description = None
        self._sensitive_word = None
        self.discriminator = None

        self.name = name
        self.policies = policies
        if description is not None:
            self.description = description
        if sensitive_word is not None:
            self.sensitive_word = sensitive_word

    @property
    def name(self):
        """Gets the name of this UpdateTopicAccessPolicyTopicsObject.

        topic名称。

        :return: The name of this UpdateTopicAccessPolicyTopicsObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTopicAccessPolicyTopicsObject.

        topic名称。

        :param name: The name of this UpdateTopicAccessPolicyTopicsObject.
        :type name: str
        """
        self._name = name

    @property
    def policies(self):
        """Gets the policies of this UpdateTopicAccessPolicyTopicsObject.

        权限列表。

        :return: The policies of this UpdateTopicAccessPolicyTopicsObject.
        :rtype: list[:class:`huaweicloudsdkroma.v2.UpdateTopicAccessPolicyPoliciesObject`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this UpdateTopicAccessPolicyTopicsObject.

        权限列表。

        :param policies: The policies of this UpdateTopicAccessPolicyTopicsObject.
        :type policies: list[:class:`huaweicloudsdkroma.v2.UpdateTopicAccessPolicyPoliciesObject`]
        """
        self._policies = policies

    @property
    def description(self):
        """Gets the description of this UpdateTopicAccessPolicyTopicsObject.

        描述。

        :return: The description of this UpdateTopicAccessPolicyTopicsObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTopicAccessPolicyTopicsObject.

        描述。

        :param description: The description of this UpdateTopicAccessPolicyTopicsObject.
        :type description: str
        """
        self._description = description

    @property
    def sensitive_word(self):
        """Gets the sensitive_word of this UpdateTopicAccessPolicyTopicsObject.

        敏感字段。

        :return: The sensitive_word of this UpdateTopicAccessPolicyTopicsObject.
        :rtype: str
        """
        return self._sensitive_word

    @sensitive_word.setter
    def sensitive_word(self, sensitive_word):
        """Sets the sensitive_word of this UpdateTopicAccessPolicyTopicsObject.

        敏感字段。

        :param sensitive_word: The sensitive_word of this UpdateTopicAccessPolicyTopicsObject.
        :type sensitive_word: str
        """
        self._sensitive_word = sensitive_word

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
        if not isinstance(other, UpdateTopicAccessPolicyTopicsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
