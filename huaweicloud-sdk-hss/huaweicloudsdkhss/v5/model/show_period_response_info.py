# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPeriodResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_vals': 'str',
        'period_unit': 'str'
    }

    attribute_map = {
        'period_vals': 'period_vals',
        'period_unit': 'period_unit'
    }

    def __init__(self, period_vals=None, period_unit=None):
        r"""ShowPeriodResponseInfo

        The model defined in huaweicloud sdk

        :param period_vals: 购买时长数值串，多个用逗号分隔，如1,2,3,4,5,6,7,8,9
        :type period_vals: str
        :param period_unit: 购买时长单位   - year ：年   - month ：月   - day ：日
        :type period_unit: str
        """
        
        

        self._period_vals = None
        self._period_unit = None
        self.discriminator = None

        if period_vals is not None:
            self.period_vals = period_vals
        if period_unit is not None:
            self.period_unit = period_unit

    @property
    def period_vals(self):
        r"""Gets the period_vals of this ShowPeriodResponseInfo.

        购买时长数值串，多个用逗号分隔，如1,2,3,4,5,6,7,8,9

        :return: The period_vals of this ShowPeriodResponseInfo.
        :rtype: str
        """
        return self._period_vals

    @period_vals.setter
    def period_vals(self, period_vals):
        r"""Sets the period_vals of this ShowPeriodResponseInfo.

        购买时长数值串，多个用逗号分隔，如1,2,3,4,5,6,7,8,9

        :param period_vals: The period_vals of this ShowPeriodResponseInfo.
        :type period_vals: str
        """
        self._period_vals = period_vals

    @property
    def period_unit(self):
        r"""Gets the period_unit of this ShowPeriodResponseInfo.

        购买时长单位   - year ：年   - month ：月   - day ：日

        :return: The period_unit of this ShowPeriodResponseInfo.
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        r"""Sets the period_unit of this ShowPeriodResponseInfo.

        购买时长单位   - year ：年   - month ：月   - day ：日

        :param period_unit: The period_unit of this ShowPeriodResponseInfo.
        :type period_unit: str
        """
        self._period_unit = period_unit

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
        if not isinstance(other, ShowPeriodResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
