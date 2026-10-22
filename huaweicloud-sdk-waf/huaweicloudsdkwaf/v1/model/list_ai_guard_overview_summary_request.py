# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiGuardOverviewSummaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, _from=None, to=None):
        r"""ListAiGuardOverviewSummaryRequest

        The model defined in huaweicloud sdk

        :param _from: **参数解释：** 开始时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        """
        
        

        self.__from = None
        self._to = None
        self.discriminator = None

        self._from = _from
        self.to = to

    @property
    def _from(self):
        r"""Gets the _from of this ListAiGuardOverviewSummaryRequest.

        **参数解释：** 开始时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListAiGuardOverviewSummaryRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAiGuardOverviewSummaryRequest.

        **参数解释：** 开始时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListAiGuardOverviewSummaryRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAiGuardOverviewSummaryRequest.

        **参数解释：** 结束时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListAiGuardOverviewSummaryRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAiGuardOverviewSummaryRequest.

        **参数解释：** 结束时间戳（毫秒），必填。时间范围不超过1个月 **约束限制：** 必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListAiGuardOverviewSummaryRequest.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ListAiGuardOverviewSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
