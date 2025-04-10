# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddIssueWorkHoursResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added_work_hours': 'list[AddIssueWorkHoursResponseBodyAddedWorkHours]'
    }

    attribute_map = {
        'added_work_hours': 'added_work_hours'
    }

    def __init__(self, added_work_hours=None):
        r"""AddIssueWorkHoursResponse

        The model defined in huaweicloud sdk

        :param added_work_hours: 已添加的工时列表
        :type added_work_hours: list[:class:`huaweicloudsdkprojectman.v4.AddIssueWorkHoursResponseBodyAddedWorkHours`]
        """
        
        super(AddIssueWorkHoursResponse, self).__init__()

        self._added_work_hours = None
        self.discriminator = None

        if added_work_hours is not None:
            self.added_work_hours = added_work_hours

    @property
    def added_work_hours(self):
        r"""Gets the added_work_hours of this AddIssueWorkHoursResponse.

        已添加的工时列表

        :return: The added_work_hours of this AddIssueWorkHoursResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.AddIssueWorkHoursResponseBodyAddedWorkHours`]
        """
        return self._added_work_hours

    @added_work_hours.setter
    def added_work_hours(self, added_work_hours):
        r"""Sets the added_work_hours of this AddIssueWorkHoursResponse.

        已添加的工时列表

        :param added_work_hours: The added_work_hours of this AddIssueWorkHoursResponse.
        :type added_work_hours: list[:class:`huaweicloudsdkprojectman.v4.AddIssueWorkHoursResponseBodyAddedWorkHours`]
        """
        self._added_work_hours = added_work_hours

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
        if not isinstance(other, AddIssueWorkHoursResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
