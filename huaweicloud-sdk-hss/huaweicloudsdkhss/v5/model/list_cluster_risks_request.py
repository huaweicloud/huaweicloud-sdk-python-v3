# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterRisksRequest:

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
        'risk_type': 'str',
        'risk_status': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'risk_name': 'str',
        'risk_level': 'str',
        'risk_category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'risk_type': 'risk_type',
        'risk_status': 'risk_status',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'risk_name': 'risk_name',
        'risk_level': 'risk_level',
        'risk_category': 'risk_category'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, risk_type=None, risk_status=None, cluster_id=None, cluster_name=None, risk_name=None, risk_level=None, risk_category=None):
        r"""ListClusterRisksRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param risk_type: 风险类型，包含如下   - risk_assessment : 风险评估   - benchmark ：安全合规
        :type risk_type: str
        :param risk_status: 风险状态，包含如下，该字段不传值则查询全部数据：   - risky：有风险
        :type risk_status: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param risk_name: 风险名称
        :type risk_name: str
        :param risk_level: 风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示
        :type risk_level: str
        :param risk_category: 风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸
        :type risk_category: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._risk_type = None
        self._risk_status = None
        self._cluster_id = None
        self._cluster_name = None
        self._risk_name = None
        self._risk_level = None
        self._risk_category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if risk_type is not None:
            self.risk_type = risk_type
        if risk_status is not None:
            self.risk_status = risk_status
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if risk_name is not None:
            self.risk_name = risk_name
        if risk_level is not None:
            self.risk_level = risk_level
        if risk_category is not None:
            self.risk_category = risk_category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClusterRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClusterRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListClusterRisksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListClusterRisksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListClusterRisksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListClusterRisksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListClusterRisksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def risk_type(self):
        r"""Gets the risk_type of this ListClusterRisksRequest.

        风险类型，包含如下   - risk_assessment : 风险评估   - benchmark ：安全合规

        :return: The risk_type of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        r"""Sets the risk_type of this ListClusterRisksRequest.

        风险类型，包含如下   - risk_assessment : 风险评估   - benchmark ：安全合规

        :param risk_type: The risk_type of this ListClusterRisksRequest.
        :type risk_type: str
        """
        self._risk_type = risk_type

    @property
    def risk_status(self):
        r"""Gets the risk_status of this ListClusterRisksRequest.

        风险状态，包含如下，该字段不传值则查询全部数据：   - risky：有风险

        :return: The risk_status of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._risk_status

    @risk_status.setter
    def risk_status(self, risk_status):
        r"""Sets the risk_status of this ListClusterRisksRequest.

        风险状态，包含如下，该字段不传值则查询全部数据：   - risky：有风险

        :param risk_status: The risk_status of this ListClusterRisksRequest.
        :type risk_status: str
        """
        self._risk_status = risk_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListClusterRisksRequest.

        集群id

        :return: The cluster_id of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListClusterRisksRequest.

        集群id

        :param cluster_id: The cluster_id of this ListClusterRisksRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListClusterRisksRequest.

        集群名称

        :return: The cluster_name of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListClusterRisksRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListClusterRisksRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def risk_name(self):
        r"""Gets the risk_name of this ListClusterRisksRequest.

        风险名称

        :return: The risk_name of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this ListClusterRisksRequest.

        风险名称

        :param risk_name: The risk_name of this ListClusterRisksRequest.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListClusterRisksRequest.

        风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示

        :return: The risk_level of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListClusterRisksRequest.

        风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示

        :param risk_level: The risk_level of this ListClusterRisksRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def risk_category(self):
        r"""Gets the risk_category of this ListClusterRisksRequest.

        风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸

        :return: The risk_category of this ListClusterRisksRequest.
        :rtype: str
        """
        return self._risk_category

    @risk_category.setter
    def risk_category(self, risk_category):
        r"""Sets the risk_category of this ListClusterRisksRequest.

        风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸

        :param risk_category: The risk_category of this ListClusterRisksRequest.
        :type risk_category: str
        """
        self._risk_category = risk_category

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
        if not isinstance(other, ListClusterRisksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
