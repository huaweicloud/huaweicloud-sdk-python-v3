# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvalibleTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restorable_time_intervals': 'list[RestoreTimeInterval]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'restorable_time_intervals': 'restorable_time_intervals',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, restorable_time_intervals=None, offset=None, limit=None, total=None):
        r"""ShowAvalibleTimeResponse

        The model defined in huaweicloud sdk

        :param restorable_time_intervals: 可恢复时间点。
        :type restorable_time_intervals: list[:class:`huaweicloudsdkddm.v1.RestoreTimeInterval`]
        :param offset: **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。
        :type offset: int
        :param limit: **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。
        :type limit: int
        :param total: **参数解释**：  总记录数。  **参数范围**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._restorable_time_intervals = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if restorable_time_intervals is not None:
            self.restorable_time_intervals = restorable_time_intervals
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def restorable_time_intervals(self):
        r"""Gets the restorable_time_intervals of this ShowAvalibleTimeResponse.

        可恢复时间点。

        :return: The restorable_time_intervals of this ShowAvalibleTimeResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.RestoreTimeInterval`]
        """
        return self._restorable_time_intervals

    @restorable_time_intervals.setter
    def restorable_time_intervals(self, restorable_time_intervals):
        r"""Sets the restorable_time_intervals of this ShowAvalibleTimeResponse.

        可恢复时间点。

        :param restorable_time_intervals: The restorable_time_intervals of this ShowAvalibleTimeResponse.
        :type restorable_time_intervals: list[:class:`huaweicloudsdkddm.v1.RestoreTimeInterval`]
        """
        self._restorable_time_intervals = restorable_time_intervals

    @property
    def offset(self):
        r"""Gets the offset of this ShowAvalibleTimeResponse.

        **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。

        :return: The offset of this ShowAvalibleTimeResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAvalibleTimeResponse.

        **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。

        :param offset: The offset of this ShowAvalibleTimeResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowAvalibleTimeResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。

        :return: The limit of this ShowAvalibleTimeResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAvalibleTimeResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。

        :param limit: The limit of this ShowAvalibleTimeResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ShowAvalibleTimeResponse.

        **参数解释**：  总记录数。  **参数范围**：  不涉及。

        :return: The total of this ShowAvalibleTimeResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowAvalibleTimeResponse.

        **参数解释**：  总记录数。  **参数范围**：  不涉及。

        :param total: The total of this ShowAvalibleTimeResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowAvalibleTimeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAvalibleTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
