# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebSiteInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'domain': 'str',
        'category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'domain': 'domain',
        'category': 'category'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, domain=None, category=None):
        r"""ListWebSiteInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param domain: **参数解释**: 域名 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 
        :type domain: str
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 
        :type category: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._domain = None
        self._category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        if domain is not None:
            self.domain = domain
        self.category = category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebSiteInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebSiteInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebSiteInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebSiteInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWebSiteInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListWebSiteInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWebSiteInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListWebSiteInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def domain(self):
        r"""Gets the domain of this ListWebSiteInfoRequest.

        **参数解释**: 域名 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 

        :return: The domain of this ListWebSiteInfoRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListWebSiteInfoRequest.

        **参数解释**: 域名 **约束限制**: 不涉及 **取值范围**: 字符长度1-256 **默认取值**: 不涉及 

        :param domain: The domain of this ListWebSiteInfoRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def category(self):
        r"""Gets the category of this ListWebSiteInfoRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 

        :return: The category of this ListWebSiteInfoRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListWebSiteInfoRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: - host : 主机 - container : 容器  **默认取值**: 不涉及 

        :param category: The category of this ListWebSiteInfoRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListWebSiteInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
