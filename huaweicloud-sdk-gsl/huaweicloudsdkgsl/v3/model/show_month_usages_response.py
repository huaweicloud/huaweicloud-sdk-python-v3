# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonthUsagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'month_usages': 'list[MonthUsageVo]'
    }

    attribute_map = {
        'month_usages': 'month_usages'
    }

    def __init__(self, month_usages=None):
        """ShowMonthUsagesResponse

        The model defined in huaweicloud sdk

        :param month_usages: 月用量列表
        :type month_usages: list[:class:`huaweicloudsdkgsl.v3.MonthUsageVo`]
        """
        
        super(ShowMonthUsagesResponse, self).__init__()

        self._month_usages = None
        self.discriminator = None

        if month_usages is not None:
            self.month_usages = month_usages

    @property
    def month_usages(self):
        """Gets the month_usages of this ShowMonthUsagesResponse.

        月用量列表

        :return: The month_usages of this ShowMonthUsagesResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.MonthUsageVo`]
        """
        return self._month_usages

    @month_usages.setter
    def month_usages(self, month_usages):
        """Sets the month_usages of this ShowMonthUsagesResponse.

        月用量列表

        :param month_usages: The month_usages of this ShowMonthUsagesResponse.
        :type month_usages: list[:class:`huaweicloudsdkgsl.v3.MonthUsageVo`]
        """
        self._month_usages = month_usages

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
        if not isinstance(other, ShowMonthUsagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
