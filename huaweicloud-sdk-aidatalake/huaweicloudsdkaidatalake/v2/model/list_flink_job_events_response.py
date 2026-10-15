# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkJobEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'job_events': 'list[FlinkJobEvent]'
    }

    attribute_map = {
        'count': 'count',
        'job_events': 'job_events'
    }

    def __init__(self, count=None, job_events=None):
        r"""ListFlinkJobEventsResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**：作业事件总个数。 **取值范围**：0~2147483647。 
        :type count: int
        :param job_events: **参数解释**：Flink作业事件列表。可显示0~1000个FlinkJobEvent对象。 
        :type job_events: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobEvent`]
        """
        
        super().__init__()

        self._count = None
        self._job_events = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if job_events is not None:
            self.job_events = job_events

    @property
    def count(self):
        r"""Gets the count of this ListFlinkJobEventsResponse.

        **参数解释**：作业事件总个数。 **取值范围**：0~2147483647。 

        :return: The count of this ListFlinkJobEventsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFlinkJobEventsResponse.

        **参数解释**：作业事件总个数。 **取值范围**：0~2147483647。 

        :param count: The count of this ListFlinkJobEventsResponse.
        :type count: int
        """
        self._count = count

    @property
    def job_events(self):
        r"""Gets the job_events of this ListFlinkJobEventsResponse.

        **参数解释**：Flink作业事件列表。可显示0~1000个FlinkJobEvent对象。 

        :return: The job_events of this ListFlinkJobEventsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobEvent`]
        """
        return self._job_events

    @job_events.setter
    def job_events(self, job_events):
        r"""Sets the job_events of this ListFlinkJobEventsResponse.

        **参数解释**：Flink作业事件列表。可显示0~1000个FlinkJobEvent对象。 

        :param job_events: The job_events of this ListFlinkJobEventsResponse.
        :type job_events: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobEvent`]
        """
        self._job_events = job_events

    def to_dict(self):
        import warnings
        warnings.warn("ListFlinkJobEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFlinkJobEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
