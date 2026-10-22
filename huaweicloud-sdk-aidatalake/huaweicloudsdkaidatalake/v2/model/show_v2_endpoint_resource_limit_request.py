# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2EndpointResourceLimitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'engine_type': 'str',
        'id': 'str',
        'compute_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'engine_type': 'engine_type',
        'id': 'id',
        'compute_id': 'compute_id'
    }

    def __init__(self, workspace_id=None, engine_type=None, id=None, compute_id=None):
        r"""ShowV2EndpointResourceLimitRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type workspace_id: str
        :param engine_type: **参数解释**：端点引擎类型。 **约束限制**：不涉及。 **取值范围**：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2作业管理：AuraJobV2引擎。   - RayJob：RayJob引擎。   - RayCluster：RayCluster引擎。   - RayService：RayService引擎。 **默认取值**：不涉及。 
        :type engine_type: str
        :param id: **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type id: str
        :param compute_id: **参数解释**：计算资源ID，可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        """
        
        

        self._workspace_id = None
        self._engine_type = None
        self._id = None
        self._compute_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.engine_type = engine_type
        if id is not None:
            self.id = id
        self.compute_id = compute_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The workspace_id of this ShowV2EndpointResourceLimitRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ShowV2EndpointResourceLimitRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：端点引擎类型。 **约束限制**：不涉及。 **取值范围**：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2作业管理：AuraJobV2引擎。   - RayJob：RayJob引擎。   - RayCluster：RayCluster引擎。   - RayService：RayService引擎。 **默认取值**：不涉及。 

        :return: The engine_type of this ShowV2EndpointResourceLimitRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：端点引擎类型。 **约束限制**：不涉及。 **取值范围**：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2作业管理：AuraJobV2引擎。   - RayJob：RayJob引擎。   - RayCluster：RayCluster引擎。   - RayService：RayService引擎。 **默认取值**：不涉及。 

        :param engine_type: The engine_type of this ShowV2EndpointResourceLimitRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def id(self):
        r"""Gets the id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The id of this ShowV2EndpointResourceLimitRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param id: The id of this ShowV2EndpointResourceLimitRequest.
        :type id: str
        """
        self._id = id

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：计算资源ID，可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this ShowV2EndpointResourceLimitRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ShowV2EndpointResourceLimitRequest.

        **参数解释**：计算资源ID，可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this ShowV2EndpointResourceLimitRequest.
        :type compute_id: str
        """
        self._compute_id = compute_id

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
        if not isinstance(other, ShowV2EndpointResourceLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
