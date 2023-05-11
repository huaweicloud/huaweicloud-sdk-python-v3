# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'blacklist_type': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'blacklist_type': 'blacklist_type'
    }

    def __init__(self, policy_name=None, blacklist_type=None):
        """AccessPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_name: 策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入
        :type policy_name: str
        :param blacklist_type: 黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网
        :type blacklist_type: str
        """
        
        

        self._policy_name = None
        self._blacklist_type = None
        self.discriminator = None

        self.policy_name = policy_name
        self.blacklist_type = blacklist_type

    @property
    def policy_name(self):
        """Gets the policy_name of this AccessPolicyInfo.

        策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入

        :return: The policy_name of this AccessPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AccessPolicyInfo.

        策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入

        :param policy_name: The policy_name of this AccessPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def blacklist_type(self):
        """Gets the blacklist_type of this AccessPolicyInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :return: The blacklist_type of this AccessPolicyInfo.
        :rtype: str
        """
        return self._blacklist_type

    @blacklist_type.setter
    def blacklist_type(self, blacklist_type):
        """Sets the blacklist_type of this AccessPolicyInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :param blacklist_type: The blacklist_type of this AccessPolicyInfo.
        :type blacklist_type: str
        """
        self._blacklist_type = blacklist_type

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
        if not isinstance(other, AccessPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
