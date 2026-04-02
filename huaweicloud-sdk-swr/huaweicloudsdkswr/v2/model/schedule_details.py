# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cron': 'str',
        'next_scheduled_time': 'str'
    }

    attribute_map = {
        'type': 'type',
        'cron': 'cron',
        'next_scheduled_time': 'next_scheduled_time'
    }

    def __init__(self, type=None, cron=None, next_scheduled_time=None):
        r"""ScheduleDetails

        The model defined in huaweicloud sdk

        :param type: 计划类型。有效值为&#39;None&#39;（无）和 &#39;Custom&#39;（自定义）。  Custom&#39; 表示按照指定的 cron 计划触发，而 &#39;None&#39; 则表示取消定时计划。 
        :type type: str
        :param cron: cron表达式，一种基于时间的任务调度器，type设置为Custom时，需要配置此值。
        :type cron: str
        :param next_scheduled_time: 下次执行任务的时间。
        :type next_scheduled_time: str
        """
        
        

        self._type = None
        self._cron = None
        self._next_scheduled_time = None
        self.discriminator = None

        self.type = type
        if cron is not None:
            self.cron = cron
        if next_scheduled_time is not None:
            self.next_scheduled_time = next_scheduled_time

    @property
    def type(self):
        r"""Gets the type of this ScheduleDetails.

        计划类型。有效值为'None'（无）和 'Custom'（自定义）。  Custom' 表示按照指定的 cron 计划触发，而 'None' 则表示取消定时计划。 

        :return: The type of this ScheduleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleDetails.

        计划类型。有效值为'None'（无）和 'Custom'（自定义）。  Custom' 表示按照指定的 cron 计划触发，而 'None' 则表示取消定时计划。 

        :param type: The type of this ScheduleDetails.
        :type type: str
        """
        self._type = type

    @property
    def cron(self):
        r"""Gets the cron of this ScheduleDetails.

        cron表达式，一种基于时间的任务调度器，type设置为Custom时，需要配置此值。

        :return: The cron of this ScheduleDetails.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this ScheduleDetails.

        cron表达式，一种基于时间的任务调度器，type设置为Custom时，需要配置此值。

        :param cron: The cron of this ScheduleDetails.
        :type cron: str
        """
        self._cron = cron

    @property
    def next_scheduled_time(self):
        r"""Gets the next_scheduled_time of this ScheduleDetails.

        下次执行任务的时间。

        :return: The next_scheduled_time of this ScheduleDetails.
        :rtype: str
        """
        return self._next_scheduled_time

    @next_scheduled_time.setter
    def next_scheduled_time(self, next_scheduled_time):
        r"""Sets the next_scheduled_time of this ScheduleDetails.

        下次执行任务的时间。

        :param next_scheduled_time: The next_scheduled_time of this ScheduleDetails.
        :type next_scheduled_time: str
        """
        self._next_scheduled_time = next_scheduled_time

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
        if not isinstance(other, ScheduleDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
