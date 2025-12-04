# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoCesAlarmResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entities': 'list[AutoCesAlarmInfo]',
        'count': 'int'
    }

    attribute_map = {
        'entities': 'entities',
        'count': 'count'
    }

    def __init__(self, entities=None, count=None):
        r"""ShowAutoCesAlarmResponse

        The model defined in huaweicloud sdk

        :param entities: **参数解释**：  自动告警列表  **约束限制**：  不涉及。
        :type entities: list[:class:`huaweicloudsdkrds.v3.AutoCesAlarmInfo`]
        :param count: **参数解释**：  总数量。  **约束限制**：  不涉及。
        :type count: int
        """
        
        super().__init__()

        self._entities = None
        self._count = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if count is not None:
            self.count = count

    @property
    def entities(self):
        r"""Gets the entities of this ShowAutoCesAlarmResponse.

        **参数解释**：  自动告警列表  **约束限制**：  不涉及。

        :return: The entities of this ShowAutoCesAlarmResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.AutoCesAlarmInfo`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ShowAutoCesAlarmResponse.

        **参数解释**：  自动告警列表  **约束限制**：  不涉及。

        :param entities: The entities of this ShowAutoCesAlarmResponse.
        :type entities: list[:class:`huaweicloudsdkrds.v3.AutoCesAlarmInfo`]
        """
        self._entities = entities

    @property
    def count(self):
        r"""Gets the count of this ShowAutoCesAlarmResponse.

        **参数解释**：  总数量。  **约束限制**：  不涉及。

        :return: The count of this ShowAutoCesAlarmResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowAutoCesAlarmResponse.

        **参数解释**：  总数量。  **约束限制**：  不涉及。

        :param count: The count of this ShowAutoCesAlarmResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ShowAutoCesAlarmResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAutoCesAlarmResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
