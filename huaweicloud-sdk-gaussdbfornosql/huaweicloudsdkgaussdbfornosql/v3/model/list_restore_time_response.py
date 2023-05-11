# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRestoreTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'restorable_time_periods': 'list[RestorableTime]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'restorable_time_periods': 'restorable_time_periods'
    }

    def __init__(self, total_count=None, restorable_time_periods=None):
        """ListRestoreTimeResponse

        The model defined in huaweicloud sdk

        :param total_count: 实例可恢复时间段总数
        :type total_count: int
        :param restorable_time_periods: 实例可恢复的时间段
        :type restorable_time_periods: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RestorableTime`]
        """
        
        super(ListRestoreTimeResponse, self).__init__()

        self._total_count = None
        self._restorable_time_periods = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if restorable_time_periods is not None:
            self.restorable_time_periods = restorable_time_periods

    @property
    def total_count(self):
        """Gets the total_count of this ListRestoreTimeResponse.

        实例可恢复时间段总数

        :return: The total_count of this ListRestoreTimeResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListRestoreTimeResponse.

        实例可恢复时间段总数

        :param total_count: The total_count of this ListRestoreTimeResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def restorable_time_periods(self):
        """Gets the restorable_time_periods of this ListRestoreTimeResponse.

        实例可恢复的时间段

        :return: The restorable_time_periods of this ListRestoreTimeResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RestorableTime`]
        """
        return self._restorable_time_periods

    @restorable_time_periods.setter
    def restorable_time_periods(self, restorable_time_periods):
        """Sets the restorable_time_periods of this ListRestoreTimeResponse.

        实例可恢复的时间段

        :param restorable_time_periods: The restorable_time_periods of this ListRestoreTimeResponse.
        :type restorable_time_periods: list[:class:`huaweicloudsdkgaussdbfornosql.v3.RestorableTime`]
        """
        self._restorable_time_periods = restorable_time_periods

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
        if not isinstance(other, ListRestoreTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
