# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_order': 'int',
        'stages': 'list[StageInfoWithSub]'
    }

    attribute_map = {
        'record_order': 'record_order',
        'stages': 'stages'
    }

    def __init__(self, record_order=None, stages=None):
        r"""StageRecord

        The model defined in huaweicloud sdk

        :param record_order: **参数解释**：阶段记录序号，顺序递增，最大序号记录为当前最新记录。  **取值范围**：不涉及。
        :type record_order: int
        :param stages: **参数解释**：主阶段信息列表。
        :type stages: list[:class:`huaweicloudsdkmodelarts.v1.StageInfoWithSub`]
        """
        
        

        self._record_order = None
        self._stages = None
        self.discriminator = None

        if record_order is not None:
            self.record_order = record_order
        if stages is not None:
            self.stages = stages

    @property
    def record_order(self):
        r"""Gets the record_order of this StageRecord.

        **参数解释**：阶段记录序号，顺序递增，最大序号记录为当前最新记录。  **取值范围**：不涉及。

        :return: The record_order of this StageRecord.
        :rtype: int
        """
        return self._record_order

    @record_order.setter
    def record_order(self, record_order):
        r"""Sets the record_order of this StageRecord.

        **参数解释**：阶段记录序号，顺序递增，最大序号记录为当前最新记录。  **取值范围**：不涉及。

        :param record_order: The record_order of this StageRecord.
        :type record_order: int
        """
        self._record_order = record_order

    @property
    def stages(self):
        r"""Gets the stages of this StageRecord.

        **参数解释**：主阶段信息列表。

        :return: The stages of this StageRecord.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StageInfoWithSub`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this StageRecord.

        **参数解释**：主阶段信息列表。

        :param stages: The stages of this StageRecord.
        :type stages: list[:class:`huaweicloudsdkmodelarts.v1.StageInfoWithSub`]
        """
        self._stages = stages

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
        if not isinstance(other, StageRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
