# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'group_id': 'str',
        'policy_name': 'str',
        'feature_name': 'str',
        'policy_category': 'str',
        'policy_status': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'group_id': 'group_id',
        'policy_name': 'policy_name',
        'feature_name': 'feature_name',
        'policy_category': 'policy_category',
        'policy_status': 'policy_status'
    }

    def __init__(self, policy_id=None, group_id=None, policy_name=None, feature_name=None, policy_category=None, policy_status=None):
        r"""AgentPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param group_id: 策略组ID
        :type group_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param feature_name: feature名称
        :type feature_name: str
        :param policy_category: 策略类别
        :type policy_category: str
        :param policy_status: 策略应用状态:not_applied-未应用、protection_degradation_not_applied-防护降级未应用、processing-应用中、applied-已应用
        :type policy_status: str
        """
        
        

        self._policy_id = None
        self._group_id = None
        self._policy_name = None
        self._feature_name = None
        self._policy_category = None
        self._policy_status = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if group_id is not None:
            self.group_id = group_id
        if policy_name is not None:
            self.policy_name = policy_name
        if feature_name is not None:
            self.feature_name = feature_name
        if policy_category is not None:
            self.policy_category = policy_category
        if policy_status is not None:
            self.policy_status = policy_status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AgentPolicyInfo.

        策略ID

        :return: The policy_id of this AgentPolicyInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AgentPolicyInfo.

        策略ID

        :param policy_id: The policy_id of this AgentPolicyInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def group_id(self):
        r"""Gets the group_id of this AgentPolicyInfo.

        策略组ID

        :return: The group_id of this AgentPolicyInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AgentPolicyInfo.

        策略组ID

        :param group_id: The group_id of this AgentPolicyInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AgentPolicyInfo.

        策略名称

        :return: The policy_name of this AgentPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AgentPolicyInfo.

        策略名称

        :param policy_name: The policy_name of this AgentPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def feature_name(self):
        r"""Gets the feature_name of this AgentPolicyInfo.

        feature名称

        :return: The feature_name of this AgentPolicyInfo.
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        r"""Sets the feature_name of this AgentPolicyInfo.

        feature名称

        :param feature_name: The feature_name of this AgentPolicyInfo.
        :type feature_name: str
        """
        self._feature_name = feature_name

    @property
    def policy_category(self):
        r"""Gets the policy_category of this AgentPolicyInfo.

        策略类别

        :return: The policy_category of this AgentPolicyInfo.
        :rtype: str
        """
        return self._policy_category

    @policy_category.setter
    def policy_category(self, policy_category):
        r"""Sets the policy_category of this AgentPolicyInfo.

        策略类别

        :param policy_category: The policy_category of this AgentPolicyInfo.
        :type policy_category: str
        """
        self._policy_category = policy_category

    @property
    def policy_status(self):
        r"""Gets the policy_status of this AgentPolicyInfo.

        策略应用状态:not_applied-未应用、protection_degradation_not_applied-防护降级未应用、processing-应用中、applied-已应用

        :return: The policy_status of this AgentPolicyInfo.
        :rtype: str
        """
        return self._policy_status

    @policy_status.setter
    def policy_status(self, policy_status):
        r"""Sets the policy_status of this AgentPolicyInfo.

        策略应用状态:not_applied-未应用、protection_degradation_not_applied-防护降级未应用、processing-应用中、applied-已应用

        :param policy_status: The policy_status of this AgentPolicyInfo.
        :type policy_status: str
        """
        self._policy_status = policy_status

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
        if not isinstance(other, AgentPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
