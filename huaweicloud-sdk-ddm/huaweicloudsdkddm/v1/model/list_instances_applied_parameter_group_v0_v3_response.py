# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesAppliedParameterGroupV0V3Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entities': 'list[ApplicableInstance]',
        'instance_count_limit': 'int'
    }

    attribute_map = {
        'entities': 'entities',
        'instance_count_limit': 'instance_count_limit'
    }

    def __init__(self, entities=None, instance_count_limit=None):
        r"""ListInstancesAppliedParameterGroupV0V3Response

        The model defined in huaweicloud sdk

        :param entities: **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。
        :type entities: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        :param instance_count_limit: **参数解释**：  分页参数: 每页记录数。  **约束限制**：  不涉及。  **取值范围**：  大于0且小于等于128。  **默认取值**：  默认值是10。
        :type instance_count_limit: int
        """
        
        super().__init__()

        self._entities = None
        self._instance_count_limit = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if instance_count_limit is not None:
            self.instance_count_limit = instance_count_limit

    @property
    def entities(self):
        r"""Gets the entities of this ListInstancesAppliedParameterGroupV0V3Response.

        **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。

        :return: The entities of this ListInstancesAppliedParameterGroupV0V3Response.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ListInstancesAppliedParameterGroupV0V3Response.

        **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。

        :param entities: The entities of this ListInstancesAppliedParameterGroupV0V3Response.
        :type entities: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        """
        self._entities = entities

    @property
    def instance_count_limit(self):
        r"""Gets the instance_count_limit of this ListInstancesAppliedParameterGroupV0V3Response.

        **参数解释**：  分页参数: 每页记录数。  **约束限制**：  不涉及。  **取值范围**：  大于0且小于等于128。  **默认取值**：  默认值是10。

        :return: The instance_count_limit of this ListInstancesAppliedParameterGroupV0V3Response.
        :rtype: int
        """
        return self._instance_count_limit

    @instance_count_limit.setter
    def instance_count_limit(self, instance_count_limit):
        r"""Sets the instance_count_limit of this ListInstancesAppliedParameterGroupV0V3Response.

        **参数解释**：  分页参数: 每页记录数。  **约束限制**：  不涉及。  **取值范围**：  大于0且小于等于128。  **默认取值**：  默认值是10。

        :param instance_count_limit: The instance_count_limit of this ListInstancesAppliedParameterGroupV0V3Response.
        :type instance_count_limit: int
        """
        self._instance_count_limit = instance_count_limit

    def to_dict(self):
        import warnings
        warnings.warn("ListInstancesAppliedParameterGroupV0V3Response.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListInstancesAppliedParameterGroupV0V3Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
