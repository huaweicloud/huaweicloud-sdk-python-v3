# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectWorkHoursResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_hours': 'list[ShowProjectWorkHoursResponseBodyWorkHours]',
        'total': 'int'
    }

    attribute_map = {
        'work_hours': 'work_hours',
        'total': 'total'
    }

    def __init__(self, work_hours=None, total=None):
        r"""ShowProjectWorkHoursResponse

        The model defined in huaweicloud sdk

        :param work_hours: 工时列表
        :type work_hours: list[:class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursResponseBodyWorkHours`]
        :param total: 总数
        :type total: int
        """
        
        super(ShowProjectWorkHoursResponse, self).__init__()

        self._work_hours = None
        self._total = None
        self.discriminator = None

        if work_hours is not None:
            self.work_hours = work_hours
        if total is not None:
            self.total = total

    @property
    def work_hours(self):
        r"""Gets the work_hours of this ShowProjectWorkHoursResponse.

        工时列表

        :return: The work_hours of this ShowProjectWorkHoursResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursResponseBodyWorkHours`]
        """
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        r"""Sets the work_hours of this ShowProjectWorkHoursResponse.

        工时列表

        :param work_hours: The work_hours of this ShowProjectWorkHoursResponse.
        :type work_hours: list[:class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursResponseBodyWorkHours`]
        """
        self._work_hours = work_hours

    @property
    def total(self):
        r"""Gets the total of this ShowProjectWorkHoursResponse.

        总数

        :return: The total of this ShowProjectWorkHoursResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowProjectWorkHoursResponse.

        总数

        :param total: The total of this ShowProjectWorkHoursResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowProjectWorkHoursResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
