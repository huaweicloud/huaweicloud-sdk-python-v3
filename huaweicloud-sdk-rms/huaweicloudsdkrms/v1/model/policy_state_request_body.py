# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyStateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_resource': 'PolicyResource',
        'trigger_type': 'str',
        'compliance_state': 'str',
        'policy_assignment_id': 'str',
        'policy_assignment_name': 'str',
        'evaluation_time': 'str',
        'evaluation_hash': 'str'
    }

    attribute_map = {
        'policy_resource': 'policy_resource',
        'trigger_type': 'trigger_type',
        'compliance_state': 'compliance_state',
        'policy_assignment_id': 'policy_assignment_id',
        'policy_assignment_name': 'policy_assignment_name',
        'evaluation_time': 'evaluation_time',
        'evaluation_hash': 'evaluation_hash'
    }

    def __init__(self, policy_resource=None, trigger_type=None, compliance_state=None, policy_assignment_id=None, policy_assignment_name=None, evaluation_time=None, evaluation_hash=None):
        r"""PolicyStateRequestBody

        The model defined in huaweicloud sdk

        :param policy_resource: 
        :type policy_resource: :class:`huaweicloudsdkrms.v1.PolicyResource`
        :param trigger_type: 触发器类型
        :type trigger_type: str
        :param compliance_state: 合规状态
        :type compliance_state: str
        :param policy_assignment_id: 规则ID
        :type policy_assignment_id: str
        :param policy_assignment_name: 规则名称
        :type policy_assignment_name: str
        :param evaluation_time: 合规状态评估时间
        :type evaluation_time: str
        :param evaluation_hash: 评估校验码
        :type evaluation_hash: str
        """
        
        

        self._policy_resource = None
        self._trigger_type = None
        self._compliance_state = None
        self._policy_assignment_id = None
        self._policy_assignment_name = None
        self._evaluation_time = None
        self._evaluation_hash = None
        self.discriminator = None

        self.policy_resource = policy_resource
        self.trigger_type = trigger_type
        self.compliance_state = compliance_state
        self.policy_assignment_id = policy_assignment_id
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name
        self.evaluation_time = evaluation_time
        self.evaluation_hash = evaluation_hash

    @property
    def policy_resource(self):
        r"""Gets the policy_resource of this PolicyStateRequestBody.

        :return: The policy_resource of this PolicyStateRequestBody.
        :rtype: :class:`huaweicloudsdkrms.v1.PolicyResource`
        """
        return self._policy_resource

    @policy_resource.setter
    def policy_resource(self, policy_resource):
        r"""Sets the policy_resource of this PolicyStateRequestBody.

        :param policy_resource: The policy_resource of this PolicyStateRequestBody.
        :type policy_resource: :class:`huaweicloudsdkrms.v1.PolicyResource`
        """
        self._policy_resource = policy_resource

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this PolicyStateRequestBody.

        触发器类型

        :return: The trigger_type of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this PolicyStateRequestBody.

        触发器类型

        :param trigger_type: The trigger_type of this PolicyStateRequestBody.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def compliance_state(self):
        r"""Gets the compliance_state of this PolicyStateRequestBody.

        合规状态

        :return: The compliance_state of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        r"""Sets the compliance_state of this PolicyStateRequestBody.

        合规状态

        :param compliance_state: The compliance_state of this PolicyStateRequestBody.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def policy_assignment_id(self):
        r"""Gets the policy_assignment_id of this PolicyStateRequestBody.

        规则ID

        :return: The policy_assignment_id of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        r"""Sets the policy_assignment_id of this PolicyStateRequestBody.

        规则ID

        :param policy_assignment_id: The policy_assignment_id of this PolicyStateRequestBody.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def policy_assignment_name(self):
        r"""Gets the policy_assignment_name of this PolicyStateRequestBody.

        规则名称

        :return: The policy_assignment_name of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        r"""Sets the policy_assignment_name of this PolicyStateRequestBody.

        规则名称

        :param policy_assignment_name: The policy_assignment_name of this PolicyStateRequestBody.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

    @property
    def evaluation_time(self):
        r"""Gets the evaluation_time of this PolicyStateRequestBody.

        合规状态评估时间

        :return: The evaluation_time of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._evaluation_time

    @evaluation_time.setter
    def evaluation_time(self, evaluation_time):
        r"""Sets the evaluation_time of this PolicyStateRequestBody.

        合规状态评估时间

        :param evaluation_time: The evaluation_time of this PolicyStateRequestBody.
        :type evaluation_time: str
        """
        self._evaluation_time = evaluation_time

    @property
    def evaluation_hash(self):
        r"""Gets the evaluation_hash of this PolicyStateRequestBody.

        评估校验码

        :return: The evaluation_hash of this PolicyStateRequestBody.
        :rtype: str
        """
        return self._evaluation_hash

    @evaluation_hash.setter
    def evaluation_hash(self, evaluation_hash):
        r"""Sets the evaluation_hash of this PolicyStateRequestBody.

        评估校验码

        :param evaluation_hash: The evaluation_hash of this PolicyStateRequestBody.
        :type evaluation_hash: str
        """
        self._evaluation_hash = evaluation_hash

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
        if not isinstance(other, PolicyStateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
