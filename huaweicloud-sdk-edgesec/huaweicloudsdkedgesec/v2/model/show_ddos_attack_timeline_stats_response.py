# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdosAttackTimelineStatsResponse(SdkResponse):

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
        'interval': 'int',
        'values': 'list[TimeStatItem]'
    }

    attribute_map = {
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'interval': 'interval',
        'values': 'values'
    }

    def __init__(self, stat_type=None, group_by=None, interval=None, values=None):
        r"""ShowDdosAttackTimelineStatsResponse

        The model defined in huaweicloud sdk

        :param stat_type: 指标类型
        :type stat_type: str
        :param group_by: 分组类型
        :type group_by: str
        :param interval: 时间粒度(单位：秒)
        :type interval: int
        :param values: 值数组
        :type values: list[:class:`huaweicloudsdkedgesec.v2.TimeStatItem`]
        """
        
        super(ShowDdosAttackTimelineStatsResponse, self).__init__()

        self._stat_type = None
        self._group_by = None
        self._interval = None
        self._values = None
        self.discriminator = None

        if stat_type is not None:
            self.stat_type = stat_type
        if group_by is not None:
            self.group_by = group_by
        if interval is not None:
            self.interval = interval
        if values is not None:
            self.values = values

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDdosAttackTimelineStatsResponse.

        指标类型

        :return: The stat_type of this ShowDdosAttackTimelineStatsResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDdosAttackTimelineStatsResponse.

        指标类型

        :param stat_type: The stat_type of this ShowDdosAttackTimelineStatsResponse.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowDdosAttackTimelineStatsResponse.

        分组类型

        :return: The group_by of this ShowDdosAttackTimelineStatsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowDdosAttackTimelineStatsResponse.

        分组类型

        :param group_by: The group_by of this ShowDdosAttackTimelineStatsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def interval(self):
        r"""Gets the interval of this ShowDdosAttackTimelineStatsResponse.

        时间粒度(单位：秒)

        :return: The interval of this ShowDdosAttackTimelineStatsResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDdosAttackTimelineStatsResponse.

        时间粒度(单位：秒)

        :param interval: The interval of this ShowDdosAttackTimelineStatsResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def values(self):
        r"""Gets the values of this ShowDdosAttackTimelineStatsResponse.

        值数组

        :return: The values of this ShowDdosAttackTimelineStatsResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.TimeStatItem`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ShowDdosAttackTimelineStatsResponse.

        值数组

        :param values: The values of this ShowDdosAttackTimelineStatsResponse.
        :type values: list[:class:`huaweicloudsdkedgesec.v2.TimeStatItem`]
        """
        self._values = values

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
        if not isinstance(other, ShowDdosAttackTimelineStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
