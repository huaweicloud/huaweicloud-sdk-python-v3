# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBotMTimelineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'tenant_id': 'str',
        'enterprise_project_id': 'str',
        'hosts': 'list[str]',
        'domain': 'str',
        'region': 'str',
        'site': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'tenant_id': 'tenant_id',
        'enterprise_project_id': 'enterprise_project_id',
        'hosts': 'hosts',
        'domain': 'domain',
        'region': 'region',
        'site': 'site'
    }

    def __init__(self, start_time=None, end_time=None, tenant_id=None, enterprise_project_id=None, hosts=None, domain=None, region=None, site=None):
        r"""ListBotMTimelineRequest

        The model defined in huaweicloud sdk

        :param start_time: **参数解释：** 开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type start_time: int
        :param end_time: **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type end_time: int
        :param tenant_id: **参数解释：** 租户Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tenant_id: str
        :param enterprise_project_id: **参数解释：** 企业项目Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enterprise_project_id: str
        :param hosts: **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: list[str]
        :param domain: **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain: str
        :param region: **参数解释：** 区域 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type region: str
        :param site: **参数解释：** 站点 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type site: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._tenant_id = None
        self._enterprise_project_id = None
        self._hosts = None
        self._domain = None
        self._region = None
        self._site = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if hosts is not None:
            self.hosts = hosts
        if domain is not None:
            self.domain = domain
        if region is not None:
            self.region = region
        if site is not None:
            self.site = site

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBotMTimelineRequest.

        **参数解释：** 开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The start_time of this ListBotMTimelineRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBotMTimelineRequest.

        **参数解释：** 开始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param start_time: The start_time of this ListBotMTimelineRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBotMTimelineRequest.

        **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The end_time of this ListBotMTimelineRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBotMTimelineRequest.

        **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param end_time: The end_time of this ListBotMTimelineRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListBotMTimelineRequest.

        **参数解释：** 租户Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tenant_id of this ListBotMTimelineRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListBotMTimelineRequest.

        **参数解释：** 租户Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tenant_id: The tenant_id of this ListBotMTimelineRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBotMTimelineRequest.

        **参数解释：** 企业项目Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enterprise_project_id of this ListBotMTimelineRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBotMTimelineRequest.

        **参数解释：** 企业项目Id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListBotMTimelineRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def hosts(self):
        r"""Gets the hosts of this ListBotMTimelineRequest.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this ListBotMTimelineRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListBotMTimelineRequest.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this ListBotMTimelineRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def domain(self):
        r"""Gets the domain of this ListBotMTimelineRequest.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain of this ListBotMTimelineRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListBotMTimelineRequest.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain: The domain of this ListBotMTimelineRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def region(self):
        r"""Gets the region of this ListBotMTimelineRequest.

        **参数解释：** 区域 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The region of this ListBotMTimelineRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListBotMTimelineRequest.

        **参数解释：** 区域 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param region: The region of this ListBotMTimelineRequest.
        :type region: str
        """
        self._region = region

    @property
    def site(self):
        r"""Gets the site of this ListBotMTimelineRequest.

        **参数解释：** 站点 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The site of this ListBotMTimelineRequest.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        r"""Sets the site of this ListBotMTimelineRequest.

        **参数解释：** 站点 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param site: The site of this ListBotMTimelineRequest.
        :type site: str
        """
        self._site = site

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
        if not isinstance(other, ListBotMTimelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
