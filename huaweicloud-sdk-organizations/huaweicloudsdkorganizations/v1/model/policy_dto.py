# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'policy_summary': 'PolicySummaryDto'
    }

    attribute_map = {
        'content': 'content',
        'policy_summary': 'policy_summary'
    }

    def __init__(self, content=None, policy_summary=None):
        """PolicyDto

        The model defined in huaweicloud sdk

        :param content: 策略的文本内容。
        :type content: str
        :param policy_summary: 
        :type policy_summary: :class:`huaweicloudsdkorganizations.v1.PolicySummaryDto`
        """
        
        

        self._content = None
        self._policy_summary = None
        self.discriminator = None

        self.content = content
        self.policy_summary = policy_summary

    @property
    def content(self):
        """Gets the content of this PolicyDto.

        策略的文本内容。

        :return: The content of this PolicyDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PolicyDto.

        策略的文本内容。

        :param content: The content of this PolicyDto.
        :type content: str
        """
        self._content = content

    @property
    def policy_summary(self):
        """Gets the policy_summary of this PolicyDto.

        :return: The policy_summary of this PolicyDto.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PolicySummaryDto`
        """
        return self._policy_summary

    @policy_summary.setter
    def policy_summary(self, policy_summary):
        """Sets the policy_summary of this PolicyDto.

        :param policy_summary: The policy_summary of this PolicyDto.
        :type policy_summary: :class:`huaweicloudsdkorganizations.v1.PolicySummaryDto`
        """
        self._policy_summary = policy_summary

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
        if not isinstance(other, PolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
