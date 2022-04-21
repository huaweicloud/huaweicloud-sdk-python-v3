# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostpaidBillSumRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle'
    }

    def __init__(self, bill_cycle=None):
        """ListPostpaidBillSumRequest

        The model defined in huaweicloud sdk

        :param bill_cycle: 账单所归属的月份。格式：YYYY-MM。
        :type bill_cycle: str
        """
        
        

        self._bill_cycle = None
        self.discriminator = None

        self.bill_cycle = bill_cycle

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListPostpaidBillSumRequest.

        账单所归属的月份。格式：YYYY-MM。

        :return: The bill_cycle of this ListPostpaidBillSumRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListPostpaidBillSumRequest.

        账单所归属的月份。格式：YYYY-MM。

        :param bill_cycle: The bill_cycle of this ListPostpaidBillSumRequest.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

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
        if not isinstance(other, ListPostpaidBillSumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
