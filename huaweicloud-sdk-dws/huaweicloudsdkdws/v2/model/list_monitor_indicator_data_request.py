# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitorIndicatorDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'str',
        'to': 'str',
        'function': 'str',
        'period': 'str',
        'indicator_name': 'str',
        'dim0': 'str',
        'dim1': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'function': 'function',
        'period': 'period',
        'indicator_name': 'indicator_name',
        'dim0': 'dim0',
        'dim1': 'dim1'
    }

    def __init__(self, _from=None, to=None, function=None, period=None, indicator_name=None, dim0=None, dim1=None):
        """ListMonitorIndicatorDataRequest

        The model defined in huaweicloud sdk

        :param _from: 开始时间。
        :type _from: str
        :param to: 结束时间。
        :type to: str
        :param function: 取值方法。
        :type function: str
        :param period: 取值周期。
        :type period: str
        :param indicator_name: 指标名称。
        :type indicator_name: str
        :param dim0: 第一层级。
        :type dim0: str
        :param dim1: 第二层级。
        :type dim1: str
        """
        
        

        self.__from = None
        self._to = None
        self._function = None
        self._period = None
        self._indicator_name = None
        self._dim0 = None
        self._dim1 = None
        self.discriminator = None

        self._from = _from
        self.to = to
        if function is not None:
            self.function = function
        if period is not None:
            self.period = period
        self.indicator_name = indicator_name
        self.dim0 = dim0
        if dim1 is not None:
            self.dim1 = dim1

    @property
    def _from(self):
        """Gets the _from of this ListMonitorIndicatorDataRequest.

        开始时间。

        :return: The _from of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListMonitorIndicatorDataRequest.

        开始时间。

        :param _from: The _from of this ListMonitorIndicatorDataRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListMonitorIndicatorDataRequest.

        结束时间。

        :return: The to of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListMonitorIndicatorDataRequest.

        结束时间。

        :param to: The to of this ListMonitorIndicatorDataRequest.
        :type to: str
        """
        self._to = to

    @property
    def function(self):
        """Gets the function of this ListMonitorIndicatorDataRequest.

        取值方法。

        :return: The function of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this ListMonitorIndicatorDataRequest.

        取值方法。

        :param function: The function of this ListMonitorIndicatorDataRequest.
        :type function: str
        """
        self._function = function

    @property
    def period(self):
        """Gets the period of this ListMonitorIndicatorDataRequest.

        取值周期。

        :return: The period of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListMonitorIndicatorDataRequest.

        取值周期。

        :param period: The period of this ListMonitorIndicatorDataRequest.
        :type period: str
        """
        self._period = period

    @property
    def indicator_name(self):
        """Gets the indicator_name of this ListMonitorIndicatorDataRequest.

        指标名称。

        :return: The indicator_name of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this ListMonitorIndicatorDataRequest.

        指标名称。

        :param indicator_name: The indicator_name of this ListMonitorIndicatorDataRequest.
        :type indicator_name: str
        """
        self._indicator_name = indicator_name

    @property
    def dim0(self):
        """Gets the dim0 of this ListMonitorIndicatorDataRequest.

        第一层级。

        :return: The dim0 of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._dim0

    @dim0.setter
    def dim0(self, dim0):
        """Sets the dim0 of this ListMonitorIndicatorDataRequest.

        第一层级。

        :param dim0: The dim0 of this ListMonitorIndicatorDataRequest.
        :type dim0: str
        """
        self._dim0 = dim0

    @property
    def dim1(self):
        """Gets the dim1 of this ListMonitorIndicatorDataRequest.

        第二层级。

        :return: The dim1 of this ListMonitorIndicatorDataRequest.
        :rtype: str
        """
        return self._dim1

    @dim1.setter
    def dim1(self, dim1):
        """Sets the dim1 of this ListMonitorIndicatorDataRequest.

        第二层级。

        :param dim1: The dim1 of this ListMonitorIndicatorDataRequest.
        :type dim1: str
        """
        self._dim1 = dim1

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
        if not isinstance(other, ListMonitorIndicatorDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
