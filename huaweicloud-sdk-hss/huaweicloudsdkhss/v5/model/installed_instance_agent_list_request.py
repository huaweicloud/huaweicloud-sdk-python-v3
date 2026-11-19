# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstalledInstanceAgentListRequest:

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
        'limit': 'int',
        'offset': 'int',
        'type': 'str',
        'workload_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'type': 'type',
        'workload_id': 'workload_id'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, type=None, workload_id=None):
        r"""InstalledInstanceAgentListRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param type: **参数解释**： 接入后展示维度 **约束限制**： 不涉及 **取值范围**： - workload：工作负载。 - cluster：集群。  **默认取值**： cluster 
        :type type: str
        :param workload_id: **参数解释**： 工作负载ID，type为cluster时传参为集群ID，展示该集群下工作负载详情；type为workload时传参为工作负载ID，展示该工作负载详情；不传参时，展示type类型所有详情。 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type workload_id: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._type = None
        self._workload_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.limit = limit
        self.offset = offset
        self.type = type
        if workload_id is not None:
            self.workload_id = workload_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstalledInstanceAgentListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this InstalledInstanceAgentListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstalledInstanceAgentListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this InstalledInstanceAgentListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this InstalledInstanceAgentListRequest.

        **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this InstalledInstanceAgentListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this InstalledInstanceAgentListRequest.

        **参数解释**: 每页显示个数 **约束限制**: 必填 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this InstalledInstanceAgentListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this InstalledInstanceAgentListRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this InstalledInstanceAgentListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this InstalledInstanceAgentListRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this InstalledInstanceAgentListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def type(self):
        r"""Gets the type of this InstalledInstanceAgentListRequest.

        **参数解释**： 接入后展示维度 **约束限制**： 不涉及 **取值范围**： - workload：工作负载。 - cluster：集群。  **默认取值**： cluster 

        :return: The type of this InstalledInstanceAgentListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstalledInstanceAgentListRequest.

        **参数解释**： 接入后展示维度 **约束限制**： 不涉及 **取值范围**： - workload：工作负载。 - cluster：集群。  **默认取值**： cluster 

        :param type: The type of this InstalledInstanceAgentListRequest.
        :type type: str
        """
        self._type = type

    @property
    def workload_id(self):
        r"""Gets the workload_id of this InstalledInstanceAgentListRequest.

        **参数解释**： 工作负载ID，type为cluster时传参为集群ID，展示该集群下工作负载详情；type为workload时传参为工作负载ID，展示该工作负载详情；不传参时，展示type类型所有详情。 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The workload_id of this InstalledInstanceAgentListRequest.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this InstalledInstanceAgentListRequest.

        **参数解释**： 工作负载ID，type为cluster时传参为集群ID，展示该集群下工作负载详情；type为workload时传参为工作负载ID，展示该工作负载详情；不传参时，展示type类型所有详情。 **约束限制**： 不涉及 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param workload_id: The workload_id of this InstalledInstanceAgentListRequest.
        :type workload_id: str
        """
        self._workload_id = workload_id

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
        if not isinstance(other, InstalledInstanceAgentListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
