# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'start_time': 'str',
        'top_num': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'start_time': 'start_time',
        'top_num': 'top_num'
    }

    def __init__(self, x_language=None, start_time=None, top_num=None):
        r"""ShowAlarmStatisticsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param start_time: **参数解释**: 查询开始时间。 **约束限制**: 最多可以统计最近7天的数据。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **默认取值**: 不涉及。
        :type start_time: str
        :param top_num: **参数解释**: 告警数量最多的实例的个数。 **约束限制**: 不涉及。 **取值范围**: 取值必须大于0。 **默认取值**: 5
        :type top_num: int
        """
        
        

        self._x_language = None
        self._start_time = None
        self._top_num = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.start_time = start_time
        self.top_num = top_num

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowAlarmStatisticsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ShowAlarmStatisticsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowAlarmStatisticsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowAlarmStatisticsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAlarmStatisticsRequest.

        **参数解释**: 查询开始时间。 **约束限制**: 最多可以统计最近7天的数据。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **默认取值**: 不涉及。

        :return: The start_time of this ShowAlarmStatisticsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAlarmStatisticsRequest.

        **参数解释**: 查询开始时间。 **约束限制**: 最多可以统计最近7天的数据。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **默认取值**: 不涉及。

        :param start_time: The start_time of this ShowAlarmStatisticsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def top_num(self):
        r"""Gets the top_num of this ShowAlarmStatisticsRequest.

        **参数解释**: 告警数量最多的实例的个数。 **约束限制**: 不涉及。 **取值范围**: 取值必须大于0。 **默认取值**: 5

        :return: The top_num of this ShowAlarmStatisticsRequest.
        :rtype: int
        """
        return self._top_num

    @top_num.setter
    def top_num(self, top_num):
        r"""Sets the top_num of this ShowAlarmStatisticsRequest.

        **参数解释**: 告警数量最多的实例的个数。 **约束限制**: 不涉及。 **取值范围**: 取值必须大于0。 **默认取值**: 5

        :param top_num: The top_num of this ShowAlarmStatisticsRequest.
        :type top_num: int
        """
        self._top_num = top_num

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
        if not isinstance(other, ShowAlarmStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
