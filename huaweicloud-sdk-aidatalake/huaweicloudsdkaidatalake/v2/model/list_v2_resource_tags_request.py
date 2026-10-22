# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ResourceTagsRequest:

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
        'resource_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, resource_type=None, resource_id=None, offset=None, limit=None):
        r"""ListV2ResourceTagsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type project_id: str
        :param resource_type: **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        :param resource_id: **参数解释**：标签关联的资源ID。 **约束限制**：不能为空。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type resource_id: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：查询记录数。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。 
        :type limit: int
        """
        
        

        self._project_id = None
        self._resource_type = None
        self._resource_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListV2ResourceTagsRequest.

        **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The project_id of this ListV2ResourceTagsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListV2ResourceTagsRequest.

        **参数解释**：项目ID。获取方法，请参见[获取项目ID](aidatalake_02_0029.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param project_id: The project_id of this ListV2ResourceTagsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListV2ResourceTagsRequest.

        **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 

        :return: The resource_type of this ListV2ResourceTagsRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListV2ResourceTagsRequest.

        **参数解释**：端点引擎类型列表。 **约束限制**：不能为空。 **取值范围**：   - aidatalake-workspace：工作空间。   - aidatalake-endpoint-ray：Ray引擎端点。   - aidatalake-endpoint-aura：Aura引擎端点。   - aidatalake-endpoint-spark：Spark引擎端点。   - aidatalake-endpoint-flink：Flink引擎端点。   - aidatalake-compute：计算资源。 **默认取值**：不涉及。 

        :param resource_type: The resource_type of this ListV2ResourceTagsRequest.
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.TagResourceType`
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListV2ResourceTagsRequest.

        **参数解释**：标签关联的资源ID。 **约束限制**：不能为空。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The resource_id of this ListV2ResourceTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListV2ResourceTagsRequest.

        **参数解释**：标签关联的资源ID。 **约束限制**：不能为空。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param resource_id: The resource_id of this ListV2ResourceTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def offset(self):
        r"""Gets the offset of this ListV2ResourceTagsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2ResourceTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2ResourceTagsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2ResourceTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2ResourceTagsRequest.

        **参数解释**：查询记录数。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。 

        :return: The limit of this ListV2ResourceTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2ResourceTagsRequest.

        **参数解释**：查询记录数。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。 

        :param limit: The limit of this ListV2ResourceTagsRequest.
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
        if not isinstance(other, ListV2ResourceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
