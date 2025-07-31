# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKubernetesClusterDetailsRequest:

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
        'cluster_name': 'str',
        'load_agent_info': 'bool',
        'scene': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'cluster_name': 'cluster_name',
        'load_agent_info': 'load_agent_info',
        'scene': 'scene'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, cluster_name=None, load_agent_info=None, scene=None):
        r"""ListKubernetesClusterDetailsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param load_agent_info: 是否加载agent相关信息，默认false
        :type load_agent_info: bool
        :param scene: 查询场景类型，包含如下：   -cluster_risk : 集群风险场景
        :type scene: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._cluster_name = None
        self._load_agent_info = None
        self._scene = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if load_agent_info is not None:
            self.load_agent_info = load_agent_info
        if scene is not None:
            self.scene = scene

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListKubernetesClusterDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListKubernetesClusterDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListKubernetesClusterDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListKubernetesClusterDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListKubernetesClusterDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListKubernetesClusterDetailsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListKubernetesClusterDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListKubernetesClusterDetailsRequest.

        集群名称

        :return: The cluster_name of this ListKubernetesClusterDetailsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListKubernetesClusterDetailsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListKubernetesClusterDetailsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def load_agent_info(self):
        r"""Gets the load_agent_info of this ListKubernetesClusterDetailsRequest.

        是否加载agent相关信息，默认false

        :return: The load_agent_info of this ListKubernetesClusterDetailsRequest.
        :rtype: bool
        """
        return self._load_agent_info

    @load_agent_info.setter
    def load_agent_info(self, load_agent_info):
        r"""Sets the load_agent_info of this ListKubernetesClusterDetailsRequest.

        是否加载agent相关信息，默认false

        :param load_agent_info: The load_agent_info of this ListKubernetesClusterDetailsRequest.
        :type load_agent_info: bool
        """
        self._load_agent_info = load_agent_info

    @property
    def scene(self):
        r"""Gets the scene of this ListKubernetesClusterDetailsRequest.

        查询场景类型，包含如下：   -cluster_risk : 集群风险场景

        :return: The scene of this ListKubernetesClusterDetailsRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListKubernetesClusterDetailsRequest.

        查询场景类型，包含如下：   -cluster_risk : 集群风险场景

        :param scene: The scene of this ListKubernetesClusterDetailsRequest.
        :type scene: str
        """
        self._scene = scene

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
        if not isinstance(other, ListKubernetesClusterDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
