# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebSiteHostInfoRequest:

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
        'offset': 'int',
        'limit': 'int',
        'category': 'str',
        'domain': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'part_match': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'category': 'category',
        'domain': 'domain',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'part_match': 'part_match'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, category=None, domain=None, host_name=None, host_ip=None, part_match=None):
        r"""ListWebSiteHostInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param category: 返回的资产类别 - 0: 主机 - 1: 容器
        :type category: str
        :param domain: 域名
        :type domain: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器IP
        :type host_ip: str
        :param part_match: 是否模糊匹配，默认false表示精确匹配
        :type part_match: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._category = None
        self._domain = None
        self._host_name = None
        self._host_ip = None
        self._part_match = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.category = category
        self.domain = domain
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if part_match is not None:
            self.part_match = part_match

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebSiteHostInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebSiteHostInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebSiteHostInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebSiteHostInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebSiteHostInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebSiteHostInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebSiteHostInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebSiteHostInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebSiteHostInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebSiteHostInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebSiteHostInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebSiteHostInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def category(self):
        r"""Gets the category of this ListWebSiteHostInfoRequest.

        返回的资产类别 - 0: 主机 - 1: 容器

        :return: The category of this ListWebSiteHostInfoRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListWebSiteHostInfoRequest.

        返回的资产类别 - 0: 主机 - 1: 容器

        :param category: The category of this ListWebSiteHostInfoRequest.
        :type category: str
        """
        self._category = category

    @property
    def domain(self):
        r"""Gets the domain of this ListWebSiteHostInfoRequest.

        域名

        :return: The domain of this ListWebSiteHostInfoRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListWebSiteHostInfoRequest.

        域名

        :param domain: The domain of this ListWebSiteHostInfoRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWebSiteHostInfoRequest.

        服务器名称

        :return: The host_name of this ListWebSiteHostInfoRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWebSiteHostInfoRequest.

        服务器名称

        :param host_name: The host_name of this ListWebSiteHostInfoRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListWebSiteHostInfoRequest.

        服务器IP

        :return: The host_ip of this ListWebSiteHostInfoRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListWebSiteHostInfoRequest.

        服务器IP

        :param host_ip: The host_ip of this ListWebSiteHostInfoRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def part_match(self):
        r"""Gets the part_match of this ListWebSiteHostInfoRequest.

        是否模糊匹配，默认false表示精确匹配

        :return: The part_match of this ListWebSiteHostInfoRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        r"""Sets the part_match of this ListWebSiteHostInfoRequest.

        是否模糊匹配，默认false表示精确匹配

        :param part_match: The part_match of this ListWebSiteHostInfoRequest.
        :type part_match: bool
        """
        self._part_match = part_match

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
        if not isinstance(other, ListWebSiteHostInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
