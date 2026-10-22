# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountV2TagResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'resource_type': 'TagResourceType',
        'engine_types': 'list[EngineType]',
        'body': 'V2ListTagResourcesRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'engine_types': 'engine_types',
        'body': 'body'
    }

    def __init__(self, project_id=None, resource_type=None, engine_types=None, body=None):
        r"""CountV2TagResourcesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type project_id: str
        :param resource_type: **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        :param engine_types: **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 
        :type engine_types: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        :param body: Body of the CountV2TagResourcesRequest
        :type body: :class:`huaweicloudsdkaidatalake.v2.V2ListTagResourcesRequestBody`
        """
        
        

        self._project_id = None
        self._resource_type = None
        self._engine_types = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.resource_type = resource_type
        if engine_types is not None:
            self.engine_types = engine_types
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this CountV2TagResourcesRequest.

        **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The project_id of this CountV2TagResourcesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CountV2TagResourcesRequest.

        **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param project_id: The project_id of this CountV2TagResourcesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CountV2TagResourcesRequest.

        **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 

        :return: The resource_type of this CountV2TagResourcesRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CountV2TagResourcesRequest.

        **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 

        :param resource_type: The resource_type of this CountV2TagResourcesRequest.
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        """
        self._resource_type = resource_type

    @property
    def engine_types(self):
        r"""Gets the engine_types of this CountV2TagResourcesRequest.

        **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 

        :return: The engine_types of this CountV2TagResourcesRequest.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        """
        return self._engine_types

    @engine_types.setter
    def engine_types(self, engine_types):
        r"""Sets the engine_types of this CountV2TagResourcesRequest.

        **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 

        :param engine_types: The engine_types of this CountV2TagResourcesRequest.
        :type engine_types: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        """
        self._engine_types = engine_types

    @property
    def body(self):
        r"""Gets the body of this CountV2TagResourcesRequest.

        :return: The body of this CountV2TagResourcesRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ListTagResourcesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CountV2TagResourcesRequest.

        :param body: The body of this CountV2TagResourcesRequest.
        :type body: :class:`huaweicloudsdkaidatalake.v2.V2ListTagResourcesRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CountV2TagResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
