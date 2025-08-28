# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTimingOffConfigInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'week_off_list': 'list[int]',
        'timing_range_list': 'list[TimingRangeConfigInfo]',
        'total_num': 'int'
    }

    attribute_map = {
        'week_off_list': 'week_off_list',
        'timing_range_list': 'timing_range_list',
        'total_num': 'total_num'
    }

    def __init__(self, week_off_list=None, timing_range_list=None, total_num=None):
        r"""ListTimingOffConfigInfoResponseInfo

        The model defined in huaweicloud sdk

        :param week_off_list: **参数解释**: 自动关闭防护周期列表 **取值范围**: 最少0条，最多7条 
        :type week_off_list: list[int]
        :param timing_range_list: **参数解释**: 自动关闭防护时间段 **取值范围**: 最少0条，最多5条 
        :type timing_range_list: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigInfo`]
        :param total_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        """
        
        

        self._week_off_list = None
        self._timing_range_list = None
        self._total_num = None
        self.discriminator = None

        if week_off_list is not None:
            self.week_off_list = week_off_list
        if timing_range_list is not None:
            self.timing_range_list = timing_range_list
        if total_num is not None:
            self.total_num = total_num

    @property
    def week_off_list(self):
        r"""Gets the week_off_list of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 自动关闭防护周期列表 **取值范围**: 最少0条，最多7条 

        :return: The week_off_list of this ListTimingOffConfigInfoResponseInfo.
        :rtype: list[int]
        """
        return self._week_off_list

    @week_off_list.setter
    def week_off_list(self, week_off_list):
        r"""Sets the week_off_list of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 自动关闭防护周期列表 **取值范围**: 最少0条，最多7条 

        :param week_off_list: The week_off_list of this ListTimingOffConfigInfoResponseInfo.
        :type week_off_list: list[int]
        """
        self._week_off_list = week_off_list

    @property
    def timing_range_list(self):
        r"""Gets the timing_range_list of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 自动关闭防护时间段 **取值范围**: 最少0条，最多5条 

        :return: The timing_range_list of this ListTimingOffConfigInfoResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigInfo`]
        """
        return self._timing_range_list

    @timing_range_list.setter
    def timing_range_list(self, timing_range_list):
        r"""Sets the timing_range_list of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 自动关闭防护时间段 **取值范围**: 最少0条，最多5条 

        :param timing_range_list: The timing_range_list of this ListTimingOffConfigInfoResponseInfo.
        :type timing_range_list: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigInfo`]
        """
        self._timing_range_list = timing_range_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ListTimingOffConfigInfoResponseInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListTimingOffConfigInfoResponseInfo.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ListTimingOffConfigInfoResponseInfo.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ListTimingOffConfigInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
