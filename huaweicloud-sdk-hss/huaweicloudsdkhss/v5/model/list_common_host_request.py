# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommonHostRequest:

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
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'feature_name': 'str',
        'group_id': 'str',
        'asset_value': 'str',
        'agent_status': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'version_name_upper': 'str',
        'version_name_lower': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'feature_name': 'feature_name',
        'group_id': 'group_id',
        'asset_value': 'asset_value',
        'agent_status': 'agent_status',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'version_name_upper': 'version_name_upper',
        'version_name_lower': 'version_name_lower'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_id=None, host_name=None, private_ip=None, public_ip=None, feature_name=None, group_id=None, asset_value=None, agent_status=None, cluster_id=None, cluster_name=None, version_name_upper=None, version_name_lower=None):
        r"""ListCommonHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 
        :type public_ip: str
        :param feature_name: **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: **取值范围**: - av_detect_feature：AV策略  **默认取值**: 无 
        :type feature_name: str
        :param group_id: **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type group_id: str
        :param asset_value: **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 
        :type asset_value: str
        :param agent_status: **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 
        :type agent_status: str
        :param cluster_id: **参数解释**: 集群ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type cluster_id: str
        :param cluster_name: **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type cluster_name: str
        :param version_name_upper: **参数解释**： 主机开通的版本,高于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及
        :type version_name_upper: str
        :param version_name_lower: **参数解释**： 主机开通的版本,低于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及
        :type version_name_lower: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._feature_name = None
        self._group_id = None
        self._asset_value = None
        self._agent_status = None
        self._cluster_id = None
        self._cluster_name = None
        self._version_name_upper = None
        self._version_name_lower = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if feature_name is not None:
            self.feature_name = feature_name
        if group_id is not None:
            self.group_id = group_id
        if asset_value is not None:
            self.asset_value = asset_value
        if agent_status is not None:
            self.agent_status = agent_status
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if version_name_upper is not None:
            self.version_name_upper = version_name_upper
        if version_name_lower is not None:
            self.version_name_lower = version_name_lower

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCommonHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListCommonHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCommonHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListCommonHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCommonHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListCommonHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCommonHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListCommonHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCommonHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListCommonHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCommonHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListCommonHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_id(self):
        r"""Gets the host_id of this ListCommonHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListCommonHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListCommonHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListCommonHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListCommonHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListCommonHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListCommonHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListCommonHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListCommonHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListCommonHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListCommonHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListCommonHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListCommonHostRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :return: The public_ip of this ListCommonHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListCommonHostRequest.

        **参数解释**: 服务器弹性IP地址 **约束限制**: 不涉及 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） **默认取值**: 无 

        :param public_ip: The public_ip of this ListCommonHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def feature_name(self):
        r"""Gets the feature_name of this ListCommonHostRequest.

        **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: **取值范围**: - av_detect_feature：AV策略  **默认取值**: 无 

        :return: The feature_name of this ListCommonHostRequest.
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        r"""Sets the feature_name of this ListCommonHostRequest.

        **参数解释**: 策略名称 **约束限制**: 不涉及 **取值范围**: **取值范围**: - av_detect_feature：AV策略  **默认取值**: 无 

        :param feature_name: The feature_name of this ListCommonHostRequest.
        :type feature_name: str
        """
        self._feature_name = feature_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ListCommonHostRequest.

        **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The group_id of this ListCommonHostRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListCommonHostRequest.

        **参数解释**: 服务器组的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param group_id: The group_id of this ListCommonHostRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListCommonHostRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :return: The asset_value of this ListCommonHostRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListCommonHostRequest.

        **参数解释**: 资产重要性 **约束限制**: 不涉及 **取值范围**： - important：重要资产 - common：一般资产 - test：测试资产  **默认取值**: 不涉及 

        :param asset_value: The asset_value of this ListCommonHostRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListCommonHostRequest.

        **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 

        :return: The agent_status of this ListCommonHostRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListCommonHostRequest.

        **参数解释**： Agent状态 **约束限制**: 不涉及 **取值范围**： - installed：已安装 - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中  **默认取值**: 不涉及 

        :param agent_status: The agent_status of this ListCommonHostRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListCommonHostRequest.

        **参数解释**: 集群ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The cluster_id of this ListCommonHostRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListCommonHostRequest.

        **参数解释**: 集群ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ListCommonHostRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListCommonHostRequest.

        **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The cluster_name of this ListCommonHostRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListCommonHostRequest.

        **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param cluster_name: The cluster_name of this ListCommonHostRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def version_name_upper(self):
        r"""Gets the version_name_upper of this ListCommonHostRequest.

        **参数解释**： 主机开通的版本,高于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及

        :return: The version_name_upper of this ListCommonHostRequest.
        :rtype: str
        """
        return self._version_name_upper

    @version_name_upper.setter
    def version_name_upper(self, version_name_upper):
        r"""Sets the version_name_upper of this ListCommonHostRequest.

        **参数解释**： 主机开通的版本,高于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及

        :param version_name_upper: The version_name_upper of this ListCommonHostRequest.
        :type version_name_upper: str
        """
        self._version_name_upper = version_name_upper

    @property
    def version_name_lower(self):
        r"""Gets the version_name_lower of this ListCommonHostRequest.

        **参数解释**： 主机开通的版本,低于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及

        :return: The version_name_lower of this ListCommonHostRequest.
        :rtype: str
        """
        return self._version_name_lower

    @version_name_lower.setter
    def version_name_lower(self, version_name_lower):
        r"""Sets the version_name_lower of this ListCommonHostRequest.

        **参数解释**： 主机开通的版本,低于该版本 **约束限制**: 不涉及 **取值范围**： - hss.version.basic：基础版。 - hss.version.advanced：专业版。 - hss.version.enterprise：企业版。 - hss.version.premium：旗舰版。 - hss.version.wtp：网页防篡改版。 - hss.version.container.enterprise：容器版。  **默认取值**: 不涉及

        :param version_name_lower: The version_name_lower of this ListCommonHostRequest.
        :type version_name_lower: str
        """
        self._version_name_lower = version_name_lower

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
        if not isinstance(other, ListCommonHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
