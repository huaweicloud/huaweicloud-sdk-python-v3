# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MaintainWindow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'day': 'day',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, day=None, start_time=None, end_time=None):
        r"""MaintainWindow

        The model defined in huaweicloud sdk

        :param day: **参数解释**： 每周的维护时间，以天为粒度。 **取值范围**： - Mon：星期一 - Tue：星期二 - Wed：星期三 - Thu：星期四 - Fri：星期五 - Sat：星期六 - Sun：星期日
        :type day: str
        :param start_time: **参数解释**： 维护开始时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 维护结束时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。
        :type end_time: str
        """
        
        

        self._day = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def day(self):
        r"""Gets the day of this MaintainWindow.

        **参数解释**： 每周的维护时间，以天为粒度。 **取值范围**： - Mon：星期一 - Tue：星期二 - Wed：星期三 - Thu：星期四 - Fri：星期五 - Sat：星期六 - Sun：星期日

        :return: The day of this MaintainWindow.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this MaintainWindow.

        **参数解释**： 每周的维护时间，以天为粒度。 **取值范围**： - Mon：星期一 - Tue：星期二 - Wed：星期三 - Thu：星期四 - Fri：星期五 - Sat：星期六 - Sun：星期日

        :param day: The day of this MaintainWindow.
        :type day: str
        """
        self._day = day

    @property
    def start_time(self):
        r"""Gets the start_time of this MaintainWindow.

        **参数解释**： 维护开始时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。

        :return: The start_time of this MaintainWindow.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this MaintainWindow.

        **参数解释**： 维护开始时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。

        :param start_time: The start_time of this MaintainWindow.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this MaintainWindow.

        **参数解释**： 维护结束时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。

        :return: The end_time of this MaintainWindow.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this MaintainWindow.

        **参数解释**： 维护结束时间，显示格式为 HH：mm，时区为GMT+0。 **取值范围**： 不涉及。

        :param end_time: The end_time of this MaintainWindow.
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
        if not isinstance(other, MaintainWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
