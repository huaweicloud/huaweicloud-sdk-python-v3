# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentDaemonsetInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'type': 'str',
        'show_cluster_log_status': 'bool',
        'access_status': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'show_cluster_log_status': 'show_cluster_log_status',
        'access_status': 'access_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region=None, enterprise_project_id=None, type=None, show_cluster_log_status=None, access_status=None, offset=None, limit=None):
        r"""ListAgentDaemonsetInfoRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**： 集群类型 **约束限制**： 不涉及 **取值范围**： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群  **默认取值**： 不涉及 
        :type type: str
        :param show_cluster_log_status: **参数解释**： 查询结果是否显示集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 
        :type show_cluster_log_status: bool
        :param access_status: **参数解释**： 按照集群的接入状态进行查询，true为已接入，false为未接入 **约束限制**： 不涉及 **取值范围**： - true：已接入。 - false：未接入。  **默认取值**： 不涉及 
        :type access_status: bool
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._type = None
        self._show_cluster_log_status = None
        self._access_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if show_cluster_log_status is not None:
            self.show_cluster_log_status = show_cluster_log_status
        if access_status is not None:
            self.access_status = access_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region(self):
        r"""Gets the region of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListAgentDaemonsetInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListAgentDaemonsetInfoRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAgentDaemonsetInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAgentDaemonsetInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 集群类型 **约束限制**： 不涉及 **取值范围**： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群  **默认取值**： 不涉及 

        :return: The type of this ListAgentDaemonsetInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 集群类型 **约束限制**： 不涉及 **取值范围**： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群  **默认取值**： 不涉及 

        :param type: The type of this ListAgentDaemonsetInfoRequest.
        :type type: str
        """
        self._type = type

    @property
    def show_cluster_log_status(self):
        r"""Gets the show_cluster_log_status of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 查询结果是否显示集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :return: The show_cluster_log_status of this ListAgentDaemonsetInfoRequest.
        :rtype: bool
        """
        return self._show_cluster_log_status

    @show_cluster_log_status.setter
    def show_cluster_log_status(self, show_cluster_log_status):
        r"""Sets the show_cluster_log_status of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 查询结果是否显示集群日志的接入状态 **约束限制**： 不涉及 **取值范围**： - true：是。 - false：否。  **默认取值**： false 

        :param show_cluster_log_status: The show_cluster_log_status of this ListAgentDaemonsetInfoRequest.
        :type show_cluster_log_status: bool
        """
        self._show_cluster_log_status = show_cluster_log_status

    @property
    def access_status(self):
        r"""Gets the access_status of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 按照集群的接入状态进行查询，true为已接入，false为未接入 **约束限制**： 不涉及 **取值范围**： - true：已接入。 - false：未接入。  **默认取值**： 不涉及 

        :return: The access_status of this ListAgentDaemonsetInfoRequest.
        :rtype: bool
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this ListAgentDaemonsetInfoRequest.

        **参数解释**： 按照集群的接入状态进行查询，true为已接入，false为未接入 **约束限制**： 不涉及 **取值范围**： - true：已接入。 - false：未接入。  **默认取值**： 不涉及 

        :param access_status: The access_status of this ListAgentDaemonsetInfoRequest.
        :type access_status: bool
        """
        self._access_status = access_status

    @property
    def offset(self):
        r"""Gets the offset of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListAgentDaemonsetInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListAgentDaemonsetInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAgentDaemonsetInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgentDaemonsetInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAgentDaemonsetInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAgentDaemonsetInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
