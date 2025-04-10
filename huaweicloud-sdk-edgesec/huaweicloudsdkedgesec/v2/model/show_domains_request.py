# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'domain_name': 'str',
        'policy_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'domain_name': 'domain_name',
        'policy_name': 'policy_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, domain_name=None, policy_name=None, enterprise_project_id=None):
        r"""ShowDomainsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询列表的偏移量
        :type offset: int
        :param limit: 查询列表每一页的条数
        :type limit: int
        :param domain_name: 域名
        :type domain_name: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._domain_name = None
        self._policy_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if domain_name is not None:
            self.domain_name = domain_name
        if policy_name is not None:
            self.policy_name = policy_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowDomainsRequest.

        查询列表的偏移量

        :return: The offset of this ShowDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDomainsRequest.

        查询列表的偏移量

        :param offset: The offset of this ShowDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDomainsRequest.

        查询列表每一页的条数

        :return: The limit of this ShowDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDomainsRequest.

        查询列表每一页的条数

        :param limit: The limit of this ShowDomainsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainsRequest.

        域名

        :return: The domain_name of this ShowDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainsRequest.

        域名

        :param domain_name: The domain_name of this ShowDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowDomainsRequest.

        策略名称

        :return: The policy_name of this ShowDomainsRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowDomainsRequest.

        策略名称

        :param policy_name: The policy_name of this ShowDomainsRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this ShowDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
