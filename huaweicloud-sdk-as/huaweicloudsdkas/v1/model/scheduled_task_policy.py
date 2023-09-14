# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'launch_time': 'str',
        'recurrence_type': 'str',
        'recurrence_value': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'launch_time': 'launch_time',
        'recurrence_type': 'recurrence_type',
        'recurrence_value': 'recurrence_value'
    }

    def __init__(self, start_time=None, end_time=None, launch_time=None, recurrence_type=None, recurrence_value=None):
        """ScheduledTaskPolicy

        The model defined in huaweicloud sdk

        :param start_time: 非必选，仅当recurrence_type不为空时生效，表示计划任务的生效开始时间，格式为yyyy-MM-ddTHH:mmZ，不填写时默认为任务创建成功的时间
        :type start_time: str
        :param end_time: 仅当recurrence_type不为空时生效且必选，表示计划任务的生效结束时间，格式为yyyy-MM-ddTHH:mmZ
        :type end_time: str
        :param launch_time: 必选，执行时间，采用UTC时间，recurrence_type不填写或为空时，格式为yyyy-MM-ddTHH:mmZ, recurrence_type不为空时，格式为 HH:mm
        :type launch_time: str
        :param recurrence_type: 非必选，不填写时计划任务为定时执行， 填写时，为周期执行，且只能填写DAILY，WEEKLY，MONTHLY 中的一种，分别为按天，按周，按月周期执行
        :type recurrence_type: str
        :param recurrence_value: 仅当recurrence_type为WEEKLY，MONTHLY时必选，表示周期执行的具体日期，多个日期用,分割。recurrence_type为WEEKLY时，可填入1-7， recurrence_type为MONTHLY时，可填入1-31
        :type recurrence_value: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._launch_time = None
        self._recurrence_type = None
        self._recurrence_value = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.launch_time = launch_time
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if recurrence_value is not None:
            self.recurrence_value = recurrence_value

    @property
    def start_time(self):
        """Gets the start_time of this ScheduledTaskPolicy.

        非必选，仅当recurrence_type不为空时生效，表示计划任务的生效开始时间，格式为yyyy-MM-ddTHH:mmZ，不填写时默认为任务创建成功的时间

        :return: The start_time of this ScheduledTaskPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduledTaskPolicy.

        非必选，仅当recurrence_type不为空时生效，表示计划任务的生效开始时间，格式为yyyy-MM-ddTHH:mmZ，不填写时默认为任务创建成功的时间

        :param start_time: The start_time of this ScheduledTaskPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScheduledTaskPolicy.

        仅当recurrence_type不为空时生效且必选，表示计划任务的生效结束时间，格式为yyyy-MM-ddTHH:mmZ

        :return: The end_time of this ScheduledTaskPolicy.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScheduledTaskPolicy.

        仅当recurrence_type不为空时生效且必选，表示计划任务的生效结束时间，格式为yyyy-MM-ddTHH:mmZ

        :param end_time: The end_time of this ScheduledTaskPolicy.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def launch_time(self):
        """Gets the launch_time of this ScheduledTaskPolicy.

        必选，执行时间，采用UTC时间，recurrence_type不填写或为空时，格式为yyyy-MM-ddTHH:mmZ, recurrence_type不为空时，格式为 HH:mm

        :return: The launch_time of this ScheduledTaskPolicy.
        :rtype: str
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this ScheduledTaskPolicy.

        必选，执行时间，采用UTC时间，recurrence_type不填写或为空时，格式为yyyy-MM-ddTHH:mmZ, recurrence_type不为空时，格式为 HH:mm

        :param launch_time: The launch_time of this ScheduledTaskPolicy.
        :type launch_time: str
        """
        self._launch_time = launch_time

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this ScheduledTaskPolicy.

        非必选，不填写时计划任务为定时执行， 填写时，为周期执行，且只能填写DAILY，WEEKLY，MONTHLY 中的一种，分别为按天，按周，按月周期执行

        :return: The recurrence_type of this ScheduledTaskPolicy.
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this ScheduledTaskPolicy.

        非必选，不填写时计划任务为定时执行， 填写时，为周期执行，且只能填写DAILY，WEEKLY，MONTHLY 中的一种，分别为按天，按周，按月周期执行

        :param recurrence_type: The recurrence_type of this ScheduledTaskPolicy.
        :type recurrence_type: str
        """
        self._recurrence_type = recurrence_type

    @property
    def recurrence_value(self):
        """Gets the recurrence_value of this ScheduledTaskPolicy.

        仅当recurrence_type为WEEKLY，MONTHLY时必选，表示周期执行的具体日期，多个日期用,分割。recurrence_type为WEEKLY时，可填入1-7， recurrence_type为MONTHLY时，可填入1-31

        :return: The recurrence_value of this ScheduledTaskPolicy.
        :rtype: str
        """
        return self._recurrence_value

    @recurrence_value.setter
    def recurrence_value(self, recurrence_value):
        """Sets the recurrence_value of this ScheduledTaskPolicy.

        仅当recurrence_type为WEEKLY，MONTHLY时必选，表示周期执行的具体日期，多个日期用,分割。recurrence_type为WEEKLY时，可填入1-7， recurrence_type为MONTHLY时，可填入1-31

        :param recurrence_value: The recurrence_value of this ScheduledTaskPolicy.
        :type recurrence_value: str
        """
        self._recurrence_value = recurrence_value

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
        if not isinstance(other, ScheduledTaskPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
