# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeWafDomainsRequestBody:

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
        'certificate_id': 'str',
        'web_tag': 'str',
        'description': 'str',
        'area_type': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'certificate_id': 'certificate_id',
        'web_tag': 'web_tag',
        'description': 'description',
        'area_type': 'area_type'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, policy_id=None, certificate_id=None, web_tag=None, description=None, area_type=None):
        """CreateEdgeWafDomainsRequestBody

        The model defined in huaweicloud sdk

        :param domain_name: 防护域名（可带端口），通过查询CDN域名接口获取
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param policy_id: 防护域名关联的策略id，通过查询WAF防护策略接口获取
        :type policy_id: str
        :param certificate_id: 证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台-&gt;边缘WAF-&gt;证书管理获取
        :type certificate_id: str
        :param web_tag: 域名名称
        :type web_tag: str
        :param description: 域名描述
        :type description: str
        :param area_type: 域名在CDN所属区域，通过查询CDN域名接口获取
        :type area_type: str
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._policy_id = None
        self._certificate_id = None
        self._web_tag = None
        self._description = None
        self._area_type = None
        self.discriminator = None

        self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if policy_id is not None:
            self.policy_id = policy_id
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if web_tag is not None:
            self.web_tag = web_tag
        if description is not None:
            self.description = description
        self.area_type = area_type

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateEdgeWafDomainsRequestBody.

        防护域名（可带端口），通过查询CDN域名接口获取

        :return: The domain_name of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateEdgeWafDomainsRequestBody.

        防护域名（可带端口），通过查询CDN域名接口获取

        :param domain_name: The domain_name of this CreateEdgeWafDomainsRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateEdgeWafDomainsRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateEdgeWafDomainsRequestBody.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateEdgeWafDomainsRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        """Gets the policy_id of this CreateEdgeWafDomainsRequestBody.

        防护域名关联的策略id，通过查询WAF防护策略接口获取

        :return: The policy_id of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this CreateEdgeWafDomainsRequestBody.

        防护域名关联的策略id，通过查询WAF防护策略接口获取

        :param policy_id: The policy_id of this CreateEdgeWafDomainsRequestBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this CreateEdgeWafDomainsRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台->边缘WAF->证书管理获取

        :return: The certificate_id of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this CreateEdgeWafDomainsRequestBody.

        证书id，通过查询证书列表接口（ListCertificates）接口获取证书id   - 对外协议为HTTP时不需要填写   - 对外协议HTTPS时为必填参数   - 查询证书列表接口未开放时，从边缘安全控制台->边缘WAF->证书管理获取

        :param certificate_id: The certificate_id of this CreateEdgeWafDomainsRequestBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def web_tag(self):
        """Gets the web_tag of this CreateEdgeWafDomainsRequestBody.

        域名名称

        :return: The web_tag of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this CreateEdgeWafDomainsRequestBody.

        域名名称

        :param web_tag: The web_tag of this CreateEdgeWafDomainsRequestBody.
        :type web_tag: str
        """
        self._web_tag = web_tag

    @property
    def description(self):
        """Gets the description of this CreateEdgeWafDomainsRequestBody.

        域名描述

        :return: The description of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeWafDomainsRequestBody.

        域名描述

        :param description: The description of this CreateEdgeWafDomainsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def area_type(self):
        """Gets the area_type of this CreateEdgeWafDomainsRequestBody.

        域名在CDN所属区域，通过查询CDN域名接口获取

        :return: The area_type of this CreateEdgeWafDomainsRequestBody.
        :rtype: str
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this CreateEdgeWafDomainsRequestBody.

        域名在CDN所属区域，通过查询CDN域名接口获取

        :param area_type: The area_type of this CreateEdgeWafDomainsRequestBody.
        :type area_type: str
        """
        self._area_type = area_type

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
        if not isinstance(other, CreateEdgeWafDomainsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
