# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWeeklyReportsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_start_date': 'str'
    }

    attribute_map = {
        'period_start_date': 'period_start_date'
    }

    def __init__(self, period_start_date=None):
        r"""ListWeeklyReportsRequest

        The model defined in huaweicloud sdk

        :param period_start_date: 每周的起始时间
        :type period_start_date: str
        """
        
        

        self._period_start_date = None
        self.discriminator = None

        if period_start_date is not None:
            self.period_start_date = period_start_date

    @property
    def period_start_date(self):
        r"""Gets the period_start_date of this ListWeeklyReportsRequest.

        每周的起始时间

        :return: The period_start_date of this ListWeeklyReportsRequest.
        :rtype: str
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        r"""Sets the period_start_date of this ListWeeklyReportsRequest.

        每周的起始时间

        :param period_start_date: The period_start_date of this ListWeeklyReportsRequest.
        :type period_start_date: str
        """
        self._period_start_date = period_start_date

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
        if not isinstance(other, ListWeeklyReportsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
