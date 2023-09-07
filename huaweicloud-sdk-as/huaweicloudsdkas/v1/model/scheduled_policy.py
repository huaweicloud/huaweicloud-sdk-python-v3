# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'launch_time': 'str',
        'recurrence_type': 'str',
        'recurrence_value': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'launch_time': 'launch_time',
        'recurrence_type': 'recurrence_type',
        'recurrence_value': 'recurrence_value',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, launch_time=None, recurrence_type=None, recurrence_value=None, start_time=None, end_time=None):
        """ScheduledPolicy

        The model defined in huaweicloud sdk

        :param launch_time: 触发时间，遵循UTC时间。如果scaling_policy_type为SCHEDULED，则格式为：YYYY-MM-DDThh:mmZ。如果scaling_policy_type为RECURRENCE，则格式为：hh:mm。
        :type launch_time: str
        :param recurrence_type: 周期触发类型，scaling_policy_type为RECURRENCE时该项必选。Daily：每天执行一次。Weekly：每周指定天执行一次。Monthly：每月指定天执行一次。
        :type recurrence_type: str
        :param recurrence_value: 周期触发任务数值，scaling_policy_type为RECURRENCE时该项必选。类型为Daily时，该字段为null，表示每天执行类型为Weekly时，该字段取值范围为1-7，1表示星期日，以此类推，以”,”分割，例如：1,3,5。类型为Monthly时，该字段取值范围为1-31，分别表示每月的日期，以“,”分割，例如：1,10,13,28。说明：- 当recurrence_type类型为Daily时，recurrence_value参数不生效。
        :type recurrence_value: str
        :param start_time: 周期策略重复执行开始时间，遵循UTC时间。默认为当前时间，格式为：YYYY-MM-DDThh：mZ
        :type start_time: str
        :param end_time: 周期策略重复执行结束时间，遵循UTC时间，scaling_policy_type为RECURRENCE时该项必选。当为周期类型策略时，不得早于当前时间和开始时间。格式为：YYYY-MM-DDThh：mmZ
        :type end_time: str
        """
        
        

        self._launch_time = None
        self._recurrence_type = None
        self._recurrence_value = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.launch_time = launch_time
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if recurrence_value is not None:
            self.recurrence_value = recurrence_value
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def launch_time(self):
        """Gets the launch_time of this ScheduledPolicy.

        触发时间，遵循UTC时间。如果scaling_policy_type为SCHEDULED，则格式为：YYYY-MM-DDThh:mmZ。如果scaling_policy_type为RECURRENCE，则格式为：hh:mm。

        :return: The launch_time of this ScheduledPolicy.
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this ScheduledPolicy.

        触发时间，遵循UTC时间。如果scaling_policy_type为SCHEDULED，则格式为：YYYY-MM-DDThh:mmZ。如果scaling_policy_type为RECURRENCE，则格式为：hh:mm。

        :param launch_time: The launch_time of this ScheduledPolicy.
        :type launch_time: str
        """
        self._launch_time = launch_time

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this ScheduledPolicy.

        周期触发类型，scaling_policy_type为RECURRENCE时该项必选。Daily：每天执行一次。Weekly：每周指定天执行一次。Monthly：每月指定天执行一次。

        :return: The recurrence_type of this ScheduledPolicy.
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this ScheduledPolicy.

        周期触发类型，scaling_policy_type为RECURRENCE时该项必选。Daily：每天执行一次。Weekly：每周指定天执行一次。Monthly：每月指定天执行一次。

        :param recurrence_type: The recurrence_type of this ScheduledPolicy.
        :type recurrence_type: str
        """
        self._recurrence_type = recurrence_type

    @property
    def recurrence_value(self):
        """Gets the recurrence_value of this ScheduledPolicy.

        周期触发任务数值，scaling_policy_type为RECURRENCE时该项必选。类型为Daily时，该字段为null，表示每天执行类型为Weekly时，该字段取值范围为1-7，1表示星期日，以此类推，以”,”分割，例如：1,3,5。类型为Monthly时，该字段取值范围为1-31，分别表示每月的日期，以“,”分割，例如：1,10,13,28。说明：- 当recurrence_type类型为Daily时，recurrence_value参数不生效。

        :return: The recurrence_value of this ScheduledPolicy.
        :rtype: str
        """
        return self._recurrence_value

    @recurrence_value.setter
    def recurrence_value(self, recurrence_value):
        """Sets the recurrence_value of this ScheduledPolicy.

        周期触发任务数值，scaling_policy_type为RECURRENCE时该项必选。类型为Daily时，该字段为null，表示每天执行类型为Weekly时，该字段取值范围为1-7，1表示星期日，以此类推，以”,”分割，例如：1,3,5。类型为Monthly时，该字段取值范围为1-31，分别表示每月的日期，以“,”分割，例如：1,10,13,28。说明：- 当recurrence_type类型为Daily时，recurrence_value参数不生效。

        :param recurrence_value: The recurrence_value of this ScheduledPolicy.
        :type recurrence_value: str
        """
        self._recurrence_value = recurrence_value

    @property
    def start_time(self):
        """Gets the start_time of this ScheduledPolicy.

        周期策略重复执行开始时间，遵循UTC时间。默认为当前时间，格式为：YYYY-MM-DDThh：mZ

        :return: The start_time of this ScheduledPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduledPolicy.

        周期策略重复执行开始时间，遵循UTC时间。默认为当前时间，格式为：YYYY-MM-DDThh：mZ

        :param start_time: The start_time of this ScheduledPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScheduledPolicy.

        周期策略重复执行结束时间，遵循UTC时间，scaling_policy_type为RECURRENCE时该项必选。当为周期类型策略时，不得早于当前时间和开始时间。格式为：YYYY-MM-DDThh：mmZ

        :return: The end_time of this ScheduledPolicy.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScheduledPolicy.

        周期策略重复执行结束时间，遵循UTC时间，scaling_policy_type为RECURRENCE时该项必选。当为周期类型策略时，不得早于当前时间和开始时间。格式为：YYYY-MM-DDThh：mmZ

        :param end_time: The end_time of this ScheduledPolicy.
        :type end_time: str
        """
        self._end_time = end_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduledPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
