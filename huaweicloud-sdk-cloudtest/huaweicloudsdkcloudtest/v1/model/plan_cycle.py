# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanCycle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, start_date=None, end_date=None):
        r"""PlanCycle

        The model defined in huaweicloud sdk

        :param start_date: 计划开始时间，要求用UTC时间表示。如2020-03-04
        :type start_date: str
        :param end_date: 计划结束时间，要求用UTC时间表示。如2020-03-31
        :type end_date: str
        """
        
        

        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def start_date(self):
        r"""Gets the start_date of this PlanCycle.

        计划开始时间，要求用UTC时间表示。如2020-03-04

        :return: The start_date of this PlanCycle.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this PlanCycle.

        计划开始时间，要求用UTC时间表示。如2020-03-04

        :param start_date: The start_date of this PlanCycle.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this PlanCycle.

        计划结束时间，要求用UTC时间表示。如2020-03-31

        :return: The end_date of this PlanCycle.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this PlanCycle.

        计划结束时间，要求用UTC时间表示。如2020-03-31

        :param end_date: The end_date of this PlanCycle.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, PlanCycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
