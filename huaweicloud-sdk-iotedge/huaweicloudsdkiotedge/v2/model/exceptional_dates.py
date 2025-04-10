# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceptionalDates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'valid_dates': 'list[str]',
        'invalid_dates': 'list[str]'
    }

    attribute_map = {
        'valid_dates': 'valid_dates',
        'invalid_dates': 'invalid_dates'
    }

    def __init__(self, valid_dates=None, invalid_dates=None):
        r"""ExceptionalDates

        The model defined in huaweicloud sdk

        :param valid_dates: 例外日期
        :type valid_dates: list[str]
        :param invalid_dates: 无效日期
        :type invalid_dates: list[str]
        """
        
        

        self._valid_dates = None
        self._invalid_dates = None
        self.discriminator = None

        if valid_dates is not None:
            self.valid_dates = valid_dates
        if invalid_dates is not None:
            self.invalid_dates = invalid_dates

    @property
    def valid_dates(self):
        r"""Gets the valid_dates of this ExceptionalDates.

        例外日期

        :return: The valid_dates of this ExceptionalDates.
        :rtype: list[str]
        """
        return self._valid_dates

    @valid_dates.setter
    def valid_dates(self, valid_dates):
        r"""Sets the valid_dates of this ExceptionalDates.

        例外日期

        :param valid_dates: The valid_dates of this ExceptionalDates.
        :type valid_dates: list[str]
        """
        self._valid_dates = valid_dates

    @property
    def invalid_dates(self):
        r"""Gets the invalid_dates of this ExceptionalDates.

        无效日期

        :return: The invalid_dates of this ExceptionalDates.
        :rtype: list[str]
        """
        return self._invalid_dates

    @invalid_dates.setter
    def invalid_dates(self, invalid_dates):
        r"""Sets the invalid_dates of this ExceptionalDates.

        无效日期

        :param invalid_dates: The invalid_dates of this ExceptionalDates.
        :type invalid_dates: list[str]
        """
        self._invalid_dates = invalid_dates

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
        if not isinstance(other, ExceptionalDates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
