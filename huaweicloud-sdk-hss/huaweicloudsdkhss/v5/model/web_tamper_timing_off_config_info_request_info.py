# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperTimingOffConfigInfoRequestInfo:

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
        'timing_range_list': 'list[TimingRangeConfigRequestInfo]'
    }

    attribute_map = {
        'week_off_list': 'week_off_list',
        'timing_range_list': 'timing_range_list'
    }

    def __init__(self, week_off_list=None, timing_range_list=None):
        r"""WebTamperTimingOffConfigInfoRequestInfo

        The model defined in huaweicloud sdk

        :param week_off_list: 关闭防护周期
        :type week_off_list: list[int]
        :param timing_range_list: 时间段
        :type timing_range_list: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigRequestInfo`]
        """
        
        

        self._week_off_list = None
        self._timing_range_list = None
        self.discriminator = None

        if week_off_list is not None:
            self.week_off_list = week_off_list
        if timing_range_list is not None:
            self.timing_range_list = timing_range_list

    @property
    def week_off_list(self):
        r"""Gets the week_off_list of this WebTamperTimingOffConfigInfoRequestInfo.

        关闭防护周期

        :return: The week_off_list of this WebTamperTimingOffConfigInfoRequestInfo.
        :rtype: list[int]
        """
        return self._week_off_list

    @week_off_list.setter
    def week_off_list(self, week_off_list):
        r"""Sets the week_off_list of this WebTamperTimingOffConfigInfoRequestInfo.

        关闭防护周期

        :param week_off_list: The week_off_list of this WebTamperTimingOffConfigInfoRequestInfo.
        :type week_off_list: list[int]
        """
        self._week_off_list = week_off_list

    @property
    def timing_range_list(self):
        r"""Gets the timing_range_list of this WebTamperTimingOffConfigInfoRequestInfo.

        时间段

        :return: The timing_range_list of this WebTamperTimingOffConfigInfoRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigRequestInfo`]
        """
        return self._timing_range_list

    @timing_range_list.setter
    def timing_range_list(self, timing_range_list):
        r"""Sets the timing_range_list of this WebTamperTimingOffConfigInfoRequestInfo.

        时间段

        :param timing_range_list: The timing_range_list of this WebTamperTimingOffConfigInfoRequestInfo.
        :type timing_range_list: list[:class:`huaweicloudsdkhss.v5.TimingRangeConfigRequestInfo`]
        """
        self._timing_range_list = timing_range_list

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
        if not isinstance(other, WebTamperTimingOffConfigInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
