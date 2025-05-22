# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobBuildSuccessRatioResultEveryDayReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'success_ratio': 'int'
    }

    attribute_map = {
        'date': 'date',
        'success_ratio': 'success_ratio'
    }

    def __init__(self, date=None, success_ratio=None):
        r"""ShowJobBuildSuccessRatioResultEveryDayReport

        The model defined in huaweicloud sdk

        :param date: 日期
        :type date: str
        :param success_ratio: 成功率
        :type success_ratio: int
        """
        
        

        self._date = None
        self._success_ratio = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if success_ratio is not None:
            self.success_ratio = success_ratio

    @property
    def date(self):
        r"""Gets the date of this ShowJobBuildSuccessRatioResultEveryDayReport.

        日期

        :return: The date of this ShowJobBuildSuccessRatioResultEveryDayReport.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ShowJobBuildSuccessRatioResultEveryDayReport.

        日期

        :param date: The date of this ShowJobBuildSuccessRatioResultEveryDayReport.
        :type date: str
        """
        self._date = date

    @property
    def success_ratio(self):
        r"""Gets the success_ratio of this ShowJobBuildSuccessRatioResultEveryDayReport.

        成功率

        :return: The success_ratio of this ShowJobBuildSuccessRatioResultEveryDayReport.
        :rtype: int
        """
        return self._success_ratio

    @success_ratio.setter
    def success_ratio(self, success_ratio):
        r"""Sets the success_ratio of this ShowJobBuildSuccessRatioResultEveryDayReport.

        成功率

        :param success_ratio: The success_ratio of this ShowJobBuildSuccessRatioResultEveryDayReport.
        :type success_ratio: int
        """
        self._success_ratio = success_ratio

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
        if not isinstance(other, ShowJobBuildSuccessRatioResultEveryDayReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
