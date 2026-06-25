# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparseBackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'period': 'str',
        'keep_days': 'int',
        'start_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'period': 'period',
        'keep_days': 'keep_days',
        'start_time': 'start_time'
    }

    def __init__(self, id=None, period=None, keep_days=None, start_time=None):
        r"""SparseBackupPolicy

        The model defined in huaweicloud sdk

        :param id: 参数解释：  备份策略ID。  取值范围：  不涉及。
        :type id: str
        :param period: 参数解释：  备份周期配置。  取值范围：  格式为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持范围为1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，以逗号隔开。 月份支持范围为1~12、特殊字符*（表示任意值）。 星期支持范围为1~7（1表示星期一，2表示星期二，依次类推）、特殊字符*（表示任意值）。填写1~7数字时支持填写多个，以逗号隔开。
        :type period: str
        :param keep_days: 参数解释：  备份文件可以保存的天数。  取值范围：  1~3660。
        :type keep_days: int
        :param start_time: 参数解释：  全量备份时间段。自动备份将在该时间段内触发。  取值范围：  格式为hh:mm-HH:MM，为UTC时间。 HH的值比hh大1。 mm和MM的值相同，且取值必须为00。
        :type start_time: str
        """
        
        

        self._id = None
        self._period = None
        self._keep_days = None
        self._start_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if period is not None:
            self.period = period
        if keep_days is not None:
            self.keep_days = keep_days
        if start_time is not None:
            self.start_time = start_time

    @property
    def id(self):
        r"""Gets the id of this SparseBackupPolicy.

        参数解释：  备份策略ID。  取值范围：  不涉及。

        :return: The id of this SparseBackupPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SparseBackupPolicy.

        参数解释：  备份策略ID。  取值范围：  不涉及。

        :param id: The id of this SparseBackupPolicy.
        :type id: str
        """
        self._id = id

    @property
    def period(self):
        r"""Gets the period of this SparseBackupPolicy.

        参数解释：  备份周期配置。  取值范围：  格式为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持范围为1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，以逗号隔开。 月份支持范围为1~12、特殊字符*（表示任意值）。 星期支持范围为1~7（1表示星期一，2表示星期二，依次类推）、特殊字符*（表示任意值）。填写1~7数字时支持填写多个，以逗号隔开。

        :return: The period of this SparseBackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SparseBackupPolicy.

        参数解释：  备份周期配置。  取值范围：  格式为“日期 月份 星期”形式的Cron表达式，时区为UTC时区。 日期支持范围为1~31、特殊字符*（表示任意值）、特殊字符L（表示最后一天）。填写1~31或L时支持填写多个，以逗号隔开。 月份支持范围为1~12、特殊字符*（表示任意值）。 星期支持范围为1~7（1表示星期一，2表示星期二，依次类推）、特殊字符*（表示任意值）。填写1~7数字时支持填写多个，以逗号隔开。

        :param period: The period of this SparseBackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SparseBackupPolicy.

        参数解释：  备份文件可以保存的天数。  取值范围：  1~3660。

        :return: The keep_days of this SparseBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SparseBackupPolicy.

        参数解释：  备份文件可以保存的天数。  取值范围：  1~3660。

        :param keep_days: The keep_days of this SparseBackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        r"""Gets the start_time of this SparseBackupPolicy.

        参数解释：  全量备份时间段。自动备份将在该时间段内触发。  取值范围：  格式为hh:mm-HH:MM，为UTC时间。 HH的值比hh大1。 mm和MM的值相同，且取值必须为00。

        :return: The start_time of this SparseBackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SparseBackupPolicy.

        参数解释：  全量备份时间段。自动备份将在该时间段内触发。  取值范围：  格式为hh:mm-HH:MM，为UTC时间。 HH的值比hh大1。 mm和MM的值相同，且取值必须为00。

        :param start_time: The start_time of this SparseBackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, SparseBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
