# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulAffectedStaticsRequest:

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
        'select_type': 'str',
        'type': 'str',
        'cluster_id': 'str',
        'container_ids': 'list[str]',
        'is_container': 'bool',
        'vul_ids': 'list[str]',
        'host_ids': 'list[str]',
        'category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'select_type': 'select_type',
        'type': 'type',
        'cluster_id': 'cluster_id',
        'container_ids': 'container_ids',
        'is_container': 'is_container',
        'vul_ids': 'vul_ids',
        'host_ids': 'host_ids',
        'category': 'category'
    }

    def __init__(self, enterprise_project_id=None, select_type=None, type=None, cluster_id=None, container_ids=None, is_container=None, vul_ids=None, host_ids=None, category=None):
        r"""ShowVulAffectedStaticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param select_type: **参数解释**: 选择全部漏洞类型 **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 
        :type select_type: str
        :param type: **参数解释**: 漏洞类型，当前select_type为all_vul此字段为必选 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 - cluster_vul：集群漏洞  **默认取值**: 不涉及 
        :type type: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type cluster_id: str
        :param container_ids: **参数解释**: 容器id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 
        :type container_ids: list[str]
        :param is_container: **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 
        :type is_container: bool
        :param vul_ids: **参数解释**: 漏洞id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 
        :type vul_ids: list[str]
        :param host_ids: **参数解释**: 主机id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 
        :type host_ids: list[str]
        :param category: **参数解释**: 类别，默认为host **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器 - serverless：serverless场景  **默认取值**: host 
        :type category: str
        """
        
        

        self._enterprise_project_id = None
        self._select_type = None
        self._type = None
        self._cluster_id = None
        self._container_ids = None
        self._is_container = None
        self._vul_ids = None
        self._host_ids = None
        self._category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if select_type is not None:
            self.select_type = select_type
        if type is not None:
            self.type = type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if container_ids is not None:
            self.container_ids = container_ids
        if is_container is not None:
            self.is_container = is_container
        if vul_ids is not None:
            self.vul_ids = vul_ids
        if host_ids is not None:
            self.host_ids = host_ids
        if category is not None:
            self.category = category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowVulAffectedStaticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowVulAffectedStaticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowVulAffectedStaticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowVulAffectedStaticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def select_type(self):
        r"""Gets the select_type of this ShowVulAffectedStaticsRequest.

        **参数解释**: 选择全部漏洞类型 **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 

        :return: The select_type of this ShowVulAffectedStaticsRequest.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        r"""Sets the select_type of this ShowVulAffectedStaticsRequest.

        **参数解释**: 选择全部漏洞类型 **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞  **默认取值**: 不涉及 

        :param select_type: The select_type of this ShowVulAffectedStaticsRequest.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def type(self):
        r"""Gets the type of this ShowVulAffectedStaticsRequest.

        **参数解释**: 漏洞类型，当前select_type为all_vul此字段为必选 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 - cluster_vul：集群漏洞  **默认取值**: 不涉及 

        :return: The type of this ShowVulAffectedStaticsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowVulAffectedStaticsRequest.

        **参数解释**: 漏洞类型，当前select_type为all_vul此字段为必选 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：应急漏洞 - cluster_vul：集群漏洞  **默认取值**: 不涉及 

        :param type: The type of this ShowVulAffectedStaticsRequest.
        :type type: str
        """
        self._type = type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowVulAffectedStaticsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The cluster_id of this ShowVulAffectedStaticsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowVulAffectedStaticsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ShowVulAffectedStaticsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def container_ids(self):
        r"""Gets the container_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 容器id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :return: The container_ids of this ShowVulAffectedStaticsRequest.
        :rtype: list[str]
        """
        return self._container_ids

    @container_ids.setter
    def container_ids(self, container_ids):
        r"""Sets the container_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 容器id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :param container_ids: The container_ids of this ShowVulAffectedStaticsRequest.
        :type container_ids: list[str]
        """
        self._container_ids = container_ids

    @property
    def is_container(self):
        r"""Gets the is_container of this ShowVulAffectedStaticsRequest.

        **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 

        :return: The is_container of this ShowVulAffectedStaticsRequest.
        :rtype: bool
        """
        return self._is_container

    @is_container.setter
    def is_container(self, is_container):
        r"""Sets the is_container of this ShowVulAffectedStaticsRequest.

        **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 

        :param is_container: The is_container of this ShowVulAffectedStaticsRequest.
        :type is_container: bool
        """
        self._is_container = is_container

    @property
    def vul_ids(self):
        r"""Gets the vul_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 漏洞id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :return: The vul_ids of this ShowVulAffectedStaticsRequest.
        :rtype: list[str]
        """
        return self._vul_ids

    @vul_ids.setter
    def vul_ids(self, vul_ids):
        r"""Sets the vul_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 漏洞id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :param vul_ids: The vul_ids of this ShowVulAffectedStaticsRequest.
        :type vul_ids: list[str]
        """
        self._vul_ids = vul_ids

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 主机id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :return: The host_ids of this ShowVulAffectedStaticsRequest.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ShowVulAffectedStaticsRequest.

        **参数解释**: 主机id集合 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值1000 **默认取值**: 不涉及 

        :param host_ids: The host_ids of this ShowVulAffectedStaticsRequest.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def category(self):
        r"""Gets the category of this ShowVulAffectedStaticsRequest.

        **参数解释**: 类别，默认为host **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器 - serverless：serverless场景  **默认取值**: host 

        :return: The category of this ShowVulAffectedStaticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowVulAffectedStaticsRequest.

        **参数解释**: 类别，默认为host **约束限制**: 不涉及 **取值范围**: - host：主机 - container：容器 - serverless：serverless场景  **默认取值**: host 

        :param category: The category of this ShowVulAffectedStaticsRequest.
        :type category: str
        """
        self._category = category

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowVulAffectedStaticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
