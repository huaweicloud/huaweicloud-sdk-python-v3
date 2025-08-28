# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPageNoticesRequest:

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
        'page_location': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page_location': 'page_location'
    }

    def __init__(self, enterprise_project_id=None, page_location=None):
        r"""ShowPageNoticesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param page_location: **参数解释** 访问页面位置 **取值范围** - hostMgmt：主机管理-云服务器 - hostProtectQuota：主机管理-防护配额 - containerNodeList：容器管理-容器节点管理 - containerProtectQuota：容器管理-容器防护配额 - containerMirror：容器管理-容器镜像 - container：容器管理-容器 - clusterAgent：容器管理-集群Agent管理 - vulView：漏洞管理-漏洞视图 - vulHostView：漏洞管理-主机视图 - ransomwareProtection：勒索病毒防护 - policyMgmt：策略管理 - antiVirus：病毒查杀 - hostAlarm：安全告警事件-主机安全告警 - containerAlarm：安全告警事件-容器安全告警
        :type page_location: str
        """
        
        

        self._enterprise_project_id = None
        self._page_location = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page_location is not None:
            self.page_location = page_location

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowPageNoticesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowPageNoticesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowPageNoticesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowPageNoticesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page_location(self):
        r"""Gets the page_location of this ShowPageNoticesRequest.

        **参数解释** 访问页面位置 **取值范围** - hostMgmt：主机管理-云服务器 - hostProtectQuota：主机管理-防护配额 - containerNodeList：容器管理-容器节点管理 - containerProtectQuota：容器管理-容器防护配额 - containerMirror：容器管理-容器镜像 - container：容器管理-容器 - clusterAgent：容器管理-集群Agent管理 - vulView：漏洞管理-漏洞视图 - vulHostView：漏洞管理-主机视图 - ransomwareProtection：勒索病毒防护 - policyMgmt：策略管理 - antiVirus：病毒查杀 - hostAlarm：安全告警事件-主机安全告警 - containerAlarm：安全告警事件-容器安全告警

        :return: The page_location of this ShowPageNoticesRequest.
        :rtype: str
        """
        return self._page_location

    @page_location.setter
    def page_location(self, page_location):
        r"""Sets the page_location of this ShowPageNoticesRequest.

        **参数解释** 访问页面位置 **取值范围** - hostMgmt：主机管理-云服务器 - hostProtectQuota：主机管理-防护配额 - containerNodeList：容器管理-容器节点管理 - containerProtectQuota：容器管理-容器防护配额 - containerMirror：容器管理-容器镜像 - container：容器管理-容器 - clusterAgent：容器管理-集群Agent管理 - vulView：漏洞管理-漏洞视图 - vulHostView：漏洞管理-主机视图 - ransomwareProtection：勒索病毒防护 - policyMgmt：策略管理 - antiVirus：病毒查杀 - hostAlarm：安全告警事件-主机安全告警 - containerAlarm：安全告警事件-容器安全告警

        :param page_location: The page_location of this ShowPageNoticesRequest.
        :type page_location: str
        """
        self._page_location = page_location

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
        if not isinstance(other, ShowPageNoticesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
