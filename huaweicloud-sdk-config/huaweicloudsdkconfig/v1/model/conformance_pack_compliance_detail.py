# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConformancePackComplianceDetail:

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
        'resource_id': 'str',
        'compliance_state': 'str',
        'evaluation_time': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'policy_assignment_name': 'policy_assignment_name',
        'resource_id': 'resource_id',
        'compliance_state': 'compliance_state',
        'evaluation_time': 'evaluation_time'
    }

    def __init__(self, policy_assignment_id=None, policy_assignment_name=None, resource_id=None, compliance_state=None, evaluation_time=None):
        """ConformancePackComplianceDetail

        The model defined in huaweicloud sdk

        :param policy_assignment_id: 合规规则ID。
        :type policy_assignment_id: str
        :param policy_assignment_name: 合规规则名称。
        :type policy_assignment_name: str
        :param resource_id: 评估资源ID。
        :type resource_id: str
        :param compliance_state: 合规规则合规结果。
        :type compliance_state: str
        :param evaluation_time: 资源评估时间。
        :type evaluation_time: str
        """
        
        

        self._policy_assignment_id = None
        self._policy_assignment_name = None
        self._resource_id = None
        self._compliance_state = None
        self._evaluation_time = None
        self.discriminator = None

        if policy_assignment_id is not None:
            self.policy_assignment_id = policy_assignment_id
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name
        if resource_id is not None:
            self.resource_id = resource_id
        if compliance_state is not None:
            self.compliance_state = compliance_state
        if evaluation_time is not None:
            self.evaluation_time = evaluation_time

    @property
    def policy_assignment_id(self):
        """Gets the policy_assignment_id of this ConformancePackComplianceDetail.

        合规规则ID。

        :return: The policy_assignment_id of this ConformancePackComplianceDetail.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        """Sets the policy_assignment_id of this ConformancePackComplianceDetail.

        合规规则ID。

        :param policy_assignment_id: The policy_assignment_id of this ConformancePackComplianceDetail.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def policy_assignment_name(self):
        """Gets the policy_assignment_name of this ConformancePackComplianceDetail.

        合规规则名称。

        :return: The policy_assignment_name of this ConformancePackComplianceDetail.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        """Sets the policy_assignment_name of this ConformancePackComplianceDetail.

        合规规则名称。

        :param policy_assignment_name: The policy_assignment_name of this ConformancePackComplianceDetail.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ConformancePackComplianceDetail.

        评估资源ID。

        :return: The resource_id of this ConformancePackComplianceDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ConformancePackComplianceDetail.

        评估资源ID。

        :param resource_id: The resource_id of this ConformancePackComplianceDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def compliance_state(self):
        """Gets the compliance_state of this ConformancePackComplianceDetail.

        合规规则合规结果。

        :return: The compliance_state of this ConformancePackComplianceDetail.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this ConformancePackComplianceDetail.

        合规规则合规结果。

        :param compliance_state: The compliance_state of this ConformancePackComplianceDetail.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def evaluation_time(self):
        """Gets the evaluation_time of this ConformancePackComplianceDetail.

        资源评估时间。

        :return: The evaluation_time of this ConformancePackComplianceDetail.
        :rtype: str
        """
        return self._evaluation_time

    @evaluation_time.setter
    def evaluation_time(self, evaluation_time):
        """Sets the evaluation_time of this ConformancePackComplianceDetail.

        资源评估时间。

        :param evaluation_time: The evaluation_time of this ConformancePackComplianceDetail.
        :type evaluation_time: str
        """
        self._evaluation_time = evaluation_time

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
        if not isinstance(other, ConformancePackComplianceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
