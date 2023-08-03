# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConformancePackCompliance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_id': 'str',
        'policy_assignment_name': 'str',
        'policy_assignment_compliance': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'policy_assignment_name': 'policy_assignment_name',
        'policy_assignment_compliance': 'policy_assignment_compliance'
    }

    def __init__(self, policy_assignment_id=None, policy_assignment_name=None, policy_assignment_compliance=None):
        """ConformancePackCompliance

        The model defined in huaweicloud sdk

        :param policy_assignment_id: 合规规则ID。
        :type policy_assignment_id: str
        :param policy_assignment_name: 合规规则名称。
        :type policy_assignment_name: str
        :param policy_assignment_compliance: 合规规则合规结果。
        :type policy_assignment_compliance: str
        """
        
        

        self._policy_assignment_id = None
        self._policy_assignment_name = None
        self._policy_assignment_compliance = None
        self.discriminator = None

        if policy_assignment_id is not None:
            self.policy_assignment_id = policy_assignment_id
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name
        if policy_assignment_compliance is not None:
            self.policy_assignment_compliance = policy_assignment_compliance

    @property
    def policy_assignment_id(self):
        """Gets the policy_assignment_id of this ConformancePackCompliance.

        合规规则ID。

        :return: The policy_assignment_id of this ConformancePackCompliance.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        """Sets the policy_assignment_id of this ConformancePackCompliance.

        合规规则ID。

        :param policy_assignment_id: The policy_assignment_id of this ConformancePackCompliance.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def policy_assignment_name(self):
        """Gets the policy_assignment_name of this ConformancePackCompliance.

        合规规则名称。

        :return: The policy_assignment_name of this ConformancePackCompliance.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        """Sets the policy_assignment_name of this ConformancePackCompliance.

        合规规则名称。

        :param policy_assignment_name: The policy_assignment_name of this ConformancePackCompliance.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

    @property
    def policy_assignment_compliance(self):
        """Gets the policy_assignment_compliance of this ConformancePackCompliance.

        合规规则合规结果。

        :return: The policy_assignment_compliance of this ConformancePackCompliance.
        :rtype: str
        """
        return self._policy_assignment_compliance

    @policy_assignment_compliance.setter
    def policy_assignment_compliance(self, policy_assignment_compliance):
        """Sets the policy_assignment_compliance of this ConformancePackCompliance.

        合规规则合规结果。

        :param policy_assignment_compliance: The policy_assignment_compliance of this ConformancePackCompliance.
        :type policy_assignment_compliance: str
        """
        self._policy_assignment_compliance = policy_assignment_compliance

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
        if not isinstance(other, ConformancePackCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
