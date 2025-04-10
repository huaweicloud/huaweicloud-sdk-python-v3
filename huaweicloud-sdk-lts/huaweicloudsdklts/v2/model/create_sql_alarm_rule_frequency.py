# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlAlarmRuleFrequency:

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
        'cron_expr': 'str',
        'hour_of_day': 'int',
        'day_of_week': 'int',
        'fixed_rate': 'int',
        'fixed_rate_unit': 'str'
    }

    attribute_map = {
        'type': 'type',
        'cron_expr': 'cron_expr',
        'hour_of_day': 'hour_of_day',
        'day_of_week': 'day_of_week',
        'fixed_rate': 'fixed_rate',
        'fixed_rate_unit': 'fixed_rate_unit'
    }

    def __init__(self, type=None, cron_expr=None, hour_of_day=None, day_of_week=None, fixed_rate=None, fixed_rate_unit=None):
        r"""CreateSqlAlarmRuleFrequency

        The model defined in huaweicloud sdk

        :param type: 时间类型。
        :type type: str
        :param cron_expr: 当字段type为\&quot;CRON\&quot;时取该字段。
        :type cron_expr: str
        :param hour_of_day: 当字段type为\&quot;DAILY\&quot;或者\&quot;WEEKLY\&quot;时取该字段。  DAILY：最小值：0，最大值：23 WEEKLY：最小值：0，最大值：23
        :type hour_of_day: int
        :param day_of_week: 当字段type为\&quot;WEEKLY\&quot;时取该字段（周日~周六）。
        :type day_of_week: int
        :param fixed_rate: 当字段type为\&quot;FIXED_RATE\&quot;时取该字段（当fixed_rate_unit单位为minute，最大值60；当fixed_rate_unit单位为hour，最大值24）。
        :type fixed_rate: int
        :param fixed_rate_unit: 时间单位。
        :type fixed_rate_unit: str
        """
        
        

        self._type = None
        self._cron_expr = None
        self._hour_of_day = None
        self._day_of_week = None
        self._fixed_rate = None
        self._fixed_rate_unit = None
        self.discriminator = None

        self.type = type
        if cron_expr is not None:
            self.cron_expr = cron_expr
        if hour_of_day is not None:
            self.hour_of_day = hour_of_day
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if fixed_rate is not None:
            self.fixed_rate = fixed_rate
        if fixed_rate_unit is not None:
            self.fixed_rate_unit = fixed_rate_unit

    @property
    def type(self):
        r"""Gets the type of this CreateSqlAlarmRuleFrequency.

        时间类型。

        :return: The type of this CreateSqlAlarmRuleFrequency.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateSqlAlarmRuleFrequency.

        时间类型。

        :param type: The type of this CreateSqlAlarmRuleFrequency.
        :type type: str
        """
        self._type = type

    @property
    def cron_expr(self):
        r"""Gets the cron_expr of this CreateSqlAlarmRuleFrequency.

        当字段type为\"CRON\"时取该字段。

        :return: The cron_expr of this CreateSqlAlarmRuleFrequency.
        :rtype: str
        """
        return self._cron_expr

    @cron_expr.setter
    def cron_expr(self, cron_expr):
        r"""Sets the cron_expr of this CreateSqlAlarmRuleFrequency.

        当字段type为\"CRON\"时取该字段。

        :param cron_expr: The cron_expr of this CreateSqlAlarmRuleFrequency.
        :type cron_expr: str
        """
        self._cron_expr = cron_expr

    @property
    def hour_of_day(self):
        r"""Gets the hour_of_day of this CreateSqlAlarmRuleFrequency.

        当字段type为\"DAILY\"或者\"WEEKLY\"时取该字段。  DAILY：最小值：0，最大值：23 WEEKLY：最小值：0，最大值：23

        :return: The hour_of_day of this CreateSqlAlarmRuleFrequency.
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        r"""Sets the hour_of_day of this CreateSqlAlarmRuleFrequency.

        当字段type为\"DAILY\"或者\"WEEKLY\"时取该字段。  DAILY：最小值：0，最大值：23 WEEKLY：最小值：0，最大值：23

        :param hour_of_day: The hour_of_day of this CreateSqlAlarmRuleFrequency.
        :type hour_of_day: int
        """
        self._hour_of_day = hour_of_day

    @property
    def day_of_week(self):
        r"""Gets the day_of_week of this CreateSqlAlarmRuleFrequency.

        当字段type为\"WEEKLY\"时取该字段（周日~周六）。

        :return: The day_of_week of this CreateSqlAlarmRuleFrequency.
        :rtype: int
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        r"""Sets the day_of_week of this CreateSqlAlarmRuleFrequency.

        当字段type为\"WEEKLY\"时取该字段（周日~周六）。

        :param day_of_week: The day_of_week of this CreateSqlAlarmRuleFrequency.
        :type day_of_week: int
        """
        self._day_of_week = day_of_week

    @property
    def fixed_rate(self):
        r"""Gets the fixed_rate of this CreateSqlAlarmRuleFrequency.

        当字段type为\"FIXED_RATE\"时取该字段（当fixed_rate_unit单位为minute，最大值60；当fixed_rate_unit单位为hour，最大值24）。

        :return: The fixed_rate of this CreateSqlAlarmRuleFrequency.
        :rtype: int
        """
        return self._fixed_rate

    @fixed_rate.setter
    def fixed_rate(self, fixed_rate):
        r"""Sets the fixed_rate of this CreateSqlAlarmRuleFrequency.

        当字段type为\"FIXED_RATE\"时取该字段（当fixed_rate_unit单位为minute，最大值60；当fixed_rate_unit单位为hour，最大值24）。

        :param fixed_rate: The fixed_rate of this CreateSqlAlarmRuleFrequency.
        :type fixed_rate: int
        """
        self._fixed_rate = fixed_rate

    @property
    def fixed_rate_unit(self):
        r"""Gets the fixed_rate_unit of this CreateSqlAlarmRuleFrequency.

        时间单位。

        :return: The fixed_rate_unit of this CreateSqlAlarmRuleFrequency.
        :rtype: str
        """
        return self._fixed_rate_unit

    @fixed_rate_unit.setter
    def fixed_rate_unit(self, fixed_rate_unit):
        r"""Sets the fixed_rate_unit of this CreateSqlAlarmRuleFrequency.

        时间单位。

        :param fixed_rate_unit: The fixed_rate_unit of this CreateSqlAlarmRuleFrequency.
        :type fixed_rate_unit: str
        """
        self._fixed_rate_unit = fixed_rate_unit

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
        if not isinstance(other, CreateSqlAlarmRuleFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
