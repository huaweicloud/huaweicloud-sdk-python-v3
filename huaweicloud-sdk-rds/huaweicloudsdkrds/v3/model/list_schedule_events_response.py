# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'inquiring_count': 'int',
        'schedule_count': 'int',
        'executing_count': 'int',
        'failed_count': 'int',
        'events': 'list[ScheduleEventInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'inquiring_count': 'inquiring_count',
        'schedule_count': 'schedule_count',
        'executing_count': 'executing_count',
        'failed_count': 'failed_count',
        'events': 'events'
    }

    def __init__(self, total_count=None, inquiring_count=None, schedule_count=None, executing_count=None, failed_count=None, events=None):
        r"""ListScheduleEventsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：  事件总数。  **约束限制**：  不涉及。
        :type total_count: int
        :param inquiring_count: **参数解释**：  待授权的事件数。  **约束限制**：  不涉及。
        :type inquiring_count: int
        :param schedule_count: **参数解释**：  待执行的事件数。  **约束限制**：  不涉及。
        :type schedule_count: int
        :param executing_count: **参数解释**：  正在执行的事件数。  **约束限制**：  不涉及。
        :type executing_count: int
        :param failed_count: **参数解释**：  执行失败的事件数。  **约束限制**：  不涉及。
        :type failed_count: int
        :param events: **参数解释**：  事件详情列表。  **约束限制**：  不涉及。
        :type events: list[:class:`huaweicloudsdkrds.v3.ScheduleEventInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._inquiring_count = None
        self._schedule_count = None
        self._executing_count = None
        self._failed_count = None
        self._events = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if inquiring_count is not None:
            self.inquiring_count = inquiring_count
        if schedule_count is not None:
            self.schedule_count = schedule_count
        if executing_count is not None:
            self.executing_count = executing_count
        if failed_count is not None:
            self.failed_count = failed_count
        if events is not None:
            self.events = events

    @property
    def total_count(self):
        r"""Gets the total_count of this ListScheduleEventsResponse.

        **参数解释**：  事件总数。  **约束限制**：  不涉及。

        :return: The total_count of this ListScheduleEventsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListScheduleEventsResponse.

        **参数解释**：  事件总数。  **约束限制**：  不涉及。

        :param total_count: The total_count of this ListScheduleEventsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def inquiring_count(self):
        r"""Gets the inquiring_count of this ListScheduleEventsResponse.

        **参数解释**：  待授权的事件数。  **约束限制**：  不涉及。

        :return: The inquiring_count of this ListScheduleEventsResponse.
        :rtype: int
        """
        return self._inquiring_count

    @inquiring_count.setter
    def inquiring_count(self, inquiring_count):
        r"""Sets the inquiring_count of this ListScheduleEventsResponse.

        **参数解释**：  待授权的事件数。  **约束限制**：  不涉及。

        :param inquiring_count: The inquiring_count of this ListScheduleEventsResponse.
        :type inquiring_count: int
        """
        self._inquiring_count = inquiring_count

    @property
    def schedule_count(self):
        r"""Gets the schedule_count of this ListScheduleEventsResponse.

        **参数解释**：  待执行的事件数。  **约束限制**：  不涉及。

        :return: The schedule_count of this ListScheduleEventsResponse.
        :rtype: int
        """
        return self._schedule_count

    @schedule_count.setter
    def schedule_count(self, schedule_count):
        r"""Sets the schedule_count of this ListScheduleEventsResponse.

        **参数解释**：  待执行的事件数。  **约束限制**：  不涉及。

        :param schedule_count: The schedule_count of this ListScheduleEventsResponse.
        :type schedule_count: int
        """
        self._schedule_count = schedule_count

    @property
    def executing_count(self):
        r"""Gets the executing_count of this ListScheduleEventsResponse.

        **参数解释**：  正在执行的事件数。  **约束限制**：  不涉及。

        :return: The executing_count of this ListScheduleEventsResponse.
        :rtype: int
        """
        return self._executing_count

    @executing_count.setter
    def executing_count(self, executing_count):
        r"""Sets the executing_count of this ListScheduleEventsResponse.

        **参数解释**：  正在执行的事件数。  **约束限制**：  不涉及。

        :param executing_count: The executing_count of this ListScheduleEventsResponse.
        :type executing_count: int
        """
        self._executing_count = executing_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this ListScheduleEventsResponse.

        **参数解释**：  执行失败的事件数。  **约束限制**：  不涉及。

        :return: The failed_count of this ListScheduleEventsResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this ListScheduleEventsResponse.

        **参数解释**：  执行失败的事件数。  **约束限制**：  不涉及。

        :param failed_count: The failed_count of this ListScheduleEventsResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def events(self):
        r"""Gets the events of this ListScheduleEventsResponse.

        **参数解释**：  事件详情列表。  **约束限制**：  不涉及。

        :return: The events of this ListScheduleEventsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ScheduleEventInfo`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListScheduleEventsResponse.

        **参数解释**：  事件详情列表。  **约束限制**：  不涉及。

        :param events: The events of this ListScheduleEventsResponse.
        :type events: list[:class:`huaweicloudsdkrds.v3.ScheduleEventInfo`]
        """
        self._events = events

    def to_dict(self):
        import warnings
        warnings.warn("ListScheduleEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListScheduleEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
