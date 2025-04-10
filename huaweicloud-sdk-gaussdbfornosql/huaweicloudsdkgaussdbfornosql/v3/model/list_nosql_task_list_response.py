# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNosqlTaskListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'str',
        'schedules': 'list[ScheduleDetailInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'schedules': 'schedules'
    }

    def __init__(self, total_count=None, schedules=None):
        r"""ListNosqlTaskListResponse

        The model defined in huaweicloud sdk

        :param total_count: 记录总数。
        :type total_count: str
        :param schedules: 任务详情。
        :type schedules: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ScheduleDetailInfo`]
        """
        
        super(ListNosqlTaskListResponse, self).__init__()

        self._total_count = None
        self._schedules = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if schedules is not None:
            self.schedules = schedules

    @property
    def total_count(self):
        r"""Gets the total_count of this ListNosqlTaskListResponse.

        记录总数。

        :return: The total_count of this ListNosqlTaskListResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListNosqlTaskListResponse.

        记录总数。

        :param total_count: The total_count of this ListNosqlTaskListResponse.
        :type total_count: str
        """
        self._total_count = total_count

    @property
    def schedules(self):
        r"""Gets the schedules of this ListNosqlTaskListResponse.

        任务详情。

        :return: The schedules of this ListNosqlTaskListResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ScheduleDetailInfo`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        r"""Sets the schedules of this ListNosqlTaskListResponse.

        任务详情。

        :param schedules: The schedules of this ListNosqlTaskListResponse.
        :type schedules: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ScheduleDetailInfo`]
        """
        self._schedules = schedules

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
        if not isinstance(other, ListNosqlTaskListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
