# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'risk_operation_num': 'int'
    }

    attribute_map = {
        'period': 'period',
        'risk_operation_num': 'risk_operation_num'
    }

    def __init__(self, period=None, risk_operation_num=None):
        r"""OperationStatisticsBean

        The model defined in huaweicloud sdk

        :param period: 周期
        :type period: str
        :param risk_operation_num: 风险操作数量
        :type risk_operation_num: int
        """
        
        

        self._period = None
        self._risk_operation_num = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if risk_operation_num is not None:
            self.risk_operation_num = risk_operation_num

    @property
    def period(self):
        r"""Gets the period of this OperationStatisticsBean.

        周期

        :return: The period of this OperationStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this OperationStatisticsBean.

        周期

        :param period: The period of this OperationStatisticsBean.
        :type period: str
        """
        self._period = period

    @property
    def risk_operation_num(self):
        r"""Gets the risk_operation_num of this OperationStatisticsBean.

        风险操作数量

        :return: The risk_operation_num of this OperationStatisticsBean.
        :rtype: int
        """
        return self._risk_operation_num

    @risk_operation_num.setter
    def risk_operation_num(self, risk_operation_num):
        r"""Sets the risk_operation_num of this OperationStatisticsBean.

        风险操作数量

        :param risk_operation_num: The risk_operation_num of this OperationStatisticsBean.
        :type risk_operation_num: int
        """
        self._risk_operation_num = risk_operation_num

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
        if not isinstance(other, OperationStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
