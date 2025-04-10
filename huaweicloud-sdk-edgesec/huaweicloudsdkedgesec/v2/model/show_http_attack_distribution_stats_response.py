# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpAttackDistributionStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stat_type': 'str',
        'group_by': 'str',
        'stat_num': 'int',
        'values': 'list[CommonStatItem]',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'stat_num': 'stat_num',
        'values': 'values',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, stat_type=None, group_by=None, stat_num=None, values=None, start_time=None, end_time=None):
        r"""ShowHttpAttackDistributionStatsResponse

        The model defined in huaweicloud sdk

        :param stat_type: 安全统计指标类型。
        :type stat_type: str
        :param group_by: 分组统计维度
        :type group_by: str
        :param stat_num: 统计数量
        :type stat_num: int
        :param values: 统计数组
        :type values: list[:class:`huaweicloudsdkedgesec.v2.CommonStatItem`]
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        super(ShowHttpAttackDistributionStatsResponse, self).__init__()

        self._stat_type = None
        self._group_by = None
        self._stat_num = None
        self._values = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if stat_type is not None:
            self.stat_type = stat_type
        if group_by is not None:
            self.group_by = group_by
        if stat_num is not None:
            self.stat_num = stat_num
        if values is not None:
            self.values = values
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowHttpAttackDistributionStatsResponse.

        安全统计指标类型。

        :return: The stat_type of this ShowHttpAttackDistributionStatsResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowHttpAttackDistributionStatsResponse.

        安全统计指标类型。

        :param stat_type: The stat_type of this ShowHttpAttackDistributionStatsResponse.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowHttpAttackDistributionStatsResponse.

        分组统计维度

        :return: The group_by of this ShowHttpAttackDistributionStatsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowHttpAttackDistributionStatsResponse.

        分组统计维度

        :param group_by: The group_by of this ShowHttpAttackDistributionStatsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def stat_num(self):
        r"""Gets the stat_num of this ShowHttpAttackDistributionStatsResponse.

        统计数量

        :return: The stat_num of this ShowHttpAttackDistributionStatsResponse.
        :rtype: int
        """
        return self._stat_num

    @stat_num.setter
    def stat_num(self, stat_num):
        r"""Sets the stat_num of this ShowHttpAttackDistributionStatsResponse.

        统计数量

        :param stat_num: The stat_num of this ShowHttpAttackDistributionStatsResponse.
        :type stat_num: int
        """
        self._stat_num = stat_num

    @property
    def values(self):
        r"""Gets the values of this ShowHttpAttackDistributionStatsResponse.

        统计数组

        :return: The values of this ShowHttpAttackDistributionStatsResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.CommonStatItem`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ShowHttpAttackDistributionStatsResponse.

        统计数组

        :param values: The values of this ShowHttpAttackDistributionStatsResponse.
        :type values: list[:class:`huaweicloudsdkedgesec.v2.CommonStatItem`]
        """
        self._values = values

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowHttpAttackDistributionStatsResponse.

        开始时间

        :return: The start_time of this ShowHttpAttackDistributionStatsResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowHttpAttackDistributionStatsResponse.

        开始时间

        :param start_time: The start_time of this ShowHttpAttackDistributionStatsResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowHttpAttackDistributionStatsResponse.

        结束时间

        :return: The end_time of this ShowHttpAttackDistributionStatsResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowHttpAttackDistributionStatsResponse.

        结束时间

        :param end_time: The end_time of this ShowHttpAttackDistributionStatsResponse.
        :type end_time: int
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
        if not isinstance(other, ShowHttpAttackDistributionStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
