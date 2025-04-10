# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationPolicyStatus:

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
        'domain_id': 'str',
        'project_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'status': 'status'
    }

    def __init__(self, policy_id=None, domain_id=None, project_id=None, status=None):
        r"""OrganizationPolicyStatus

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param status: 状态
        :type status: str
        """
        
        

        self._policy_id = None
        self._domain_id = None
        self._project_id = None
        self._status = None
        self.discriminator = None

        self.policy_id = policy_id
        self.domain_id = domain_id
        self.project_id = project_id
        self.status = status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this OrganizationPolicyStatus.

        策略ID

        :return: The policy_id of this OrganizationPolicyStatus.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this OrganizationPolicyStatus.

        策略ID

        :param policy_id: The policy_id of this OrganizationPolicyStatus.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this OrganizationPolicyStatus.

        账号ID

        :return: The domain_id of this OrganizationPolicyStatus.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this OrganizationPolicyStatus.

        账号ID

        :param domain_id: The domain_id of this OrganizationPolicyStatus.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this OrganizationPolicyStatus.

        项目ID

        :return: The project_id of this OrganizationPolicyStatus.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this OrganizationPolicyStatus.

        项目ID

        :param project_id: The project_id of this OrganizationPolicyStatus.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this OrganizationPolicyStatus.

        状态

        :return: The status of this OrganizationPolicyStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OrganizationPolicyStatus.

        状态

        :param status: The status of this OrganizationPolicyStatus.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, OrganizationPolicyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
