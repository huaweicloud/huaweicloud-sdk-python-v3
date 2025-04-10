# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'policy_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'description': 'description'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, policy_id=None, description=None):
        r"""CreateDomainRequestBody

        The model defined in huaweicloud sdk

        :param domain_name: 防护域名（可带端口）
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        :param policy_id: 防护域名关联的策略id
        :type policy_id: str
        :param description: 域名描述
        :type description: str
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._policy_id = None
        self._description = None
        self.discriminator = None

        self.domain_name = domain_name
        self.enterprise_project_id = enterprise_project_id
        if policy_id is not None:
            self.policy_id = policy_id
        if description is not None:
            self.description = description

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateDomainRequestBody.

        防护域名（可带端口）

        :return: The domain_name of this CreateDomainRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateDomainRequestBody.

        防护域名（可带端口）

        :param domain_name: The domain_name of this CreateDomainRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDomainRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this CreateDomainRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDomainRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this CreateDomainRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CreateDomainRequestBody.

        防护域名关联的策略id

        :return: The policy_id of this CreateDomainRequestBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CreateDomainRequestBody.

        防护域名关联的策略id

        :param policy_id: The policy_id of this CreateDomainRequestBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def description(self):
        r"""Gets the description of this CreateDomainRequestBody.

        域名描述

        :return: The description of this CreateDomainRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDomainRequestBody.

        域名描述

        :param description: The description of this CreateDomainRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
