# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesConfigurationsResponse(SdkResponse):

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
        'total': 'int'
    }

    attribute_map = {
        'entities': 'entities',
        'total': 'total'
    }

    def __init__(self, entities=None, total=None):
        r"""ListInstancesConfigurationsResponse

        The model defined in huaweicloud sdk

        :param entities: **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。
        :type entities: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        :param total: **参数解释**：  分页参数: 每页记录数。  **参数范围**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._entities = None
        self._total = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if total is not None:
            self.total = total

    @property
    def entities(self):
        r"""Gets the entities of this ListInstancesConfigurationsResponse.

        **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。

        :return: The entities of this ListInstancesConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ListInstancesConfigurationsResponse.

        **参数解释**：  查询可应用的实例列表返回相关信息的集合。  **参数范围**：  不涉及。

        :param entities: The entities of this ListInstancesConfigurationsResponse.
        :type entities: list[:class:`huaweicloudsdkddm.v1.ApplicableInstance`]
        """
        self._entities = entities

    @property
    def total(self):
        r"""Gets the total of this ListInstancesConfigurationsResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  不涉及。

        :return: The total of this ListInstancesConfigurationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstancesConfigurationsResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  不涉及。

        :param total: The total of this ListInstancesConfigurationsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListInstancesConfigurationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstancesConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
