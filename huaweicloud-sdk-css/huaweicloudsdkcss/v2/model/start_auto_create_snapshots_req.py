# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartAutoCreateSnapshotsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indices': 'str',
        'keepday': 'int',
        'frequency': 'str',
        'period': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'indices': 'indices',
        'keepday': 'keepday',
        'frequency': 'frequency',
        'period': 'period',
        'prefix': 'prefix'
    }

    def __init__(self, indices=None, keepday=None, frequency=None, period=None, prefix=None):
        r"""StartAutoCreateSnapshotsReq

        The model defined in huaweicloud sdk

        :param indices: 指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。 0～1024个字符，不能包含空格和大写字母，且不能包含\\\&quot;\\\\&lt;|&gt;/?特殊字符。 默认值为\\*，表示恢复所有索引。
        :type indices: str
        :param keepday: 设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。
        :type keepday: int
        :param frequency: 自动创建快照的执行频次。
        :type frequency: str
        :param period: 每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。
        :type period: str
        :param prefix: 自动创建的快照名称前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。
        :type prefix: str
        """
        
        

        self._indices = None
        self._keepday = None
        self._frequency = None
        self._period = None
        self._prefix = None
        self.discriminator = None

        if indices is not None:
            self.indices = indices
        self.keepday = keepday
        if frequency is not None:
            self.frequency = frequency
        self.period = period
        self.prefix = prefix

    @property
    def indices(self):
        r"""Gets the indices of this StartAutoCreateSnapshotsReq.

        指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。 0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。 默认值为\\*，表示恢复所有索引。

        :return: The indices of this StartAutoCreateSnapshotsReq.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        r"""Sets the indices of this StartAutoCreateSnapshotsReq.

        指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。 0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。 默认值为\\*，表示恢复所有索引。

        :param indices: The indices of this StartAutoCreateSnapshotsReq.
        :type indices: str
        """
        self._indices = indices

    @property
    def keepday(self):
        r"""Gets the keepday of this StartAutoCreateSnapshotsReq.

        设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。

        :return: The keepday of this StartAutoCreateSnapshotsReq.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        r"""Sets the keepday of this StartAutoCreateSnapshotsReq.

        设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。

        :param keepday: The keepday of this StartAutoCreateSnapshotsReq.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def frequency(self):
        r"""Gets the frequency of this StartAutoCreateSnapshotsReq.

        自动创建快照的执行频次。

        :return: The frequency of this StartAutoCreateSnapshotsReq.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this StartAutoCreateSnapshotsReq.

        自动创建快照的执行频次。

        :param frequency: The frequency of this StartAutoCreateSnapshotsReq.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def period(self):
        r"""Gets the period of this StartAutoCreateSnapshotsReq.

        每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :return: The period of this StartAutoCreateSnapshotsReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this StartAutoCreateSnapshotsReq.

        每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :param period: The period of this StartAutoCreateSnapshotsReq.
        :type period: str
        """
        self._period = period

    @property
    def prefix(self):
        r"""Gets the prefix of this StartAutoCreateSnapshotsReq.

        自动创建的快照名称前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :return: The prefix of this StartAutoCreateSnapshotsReq.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this StartAutoCreateSnapshotsReq.

        自动创建的快照名称前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :param prefix: The prefix of this StartAutoCreateSnapshotsReq.
        :type prefix: str
        """
        self._prefix = prefix

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
        if not isinstance(other, StartAutoCreateSnapshotsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
