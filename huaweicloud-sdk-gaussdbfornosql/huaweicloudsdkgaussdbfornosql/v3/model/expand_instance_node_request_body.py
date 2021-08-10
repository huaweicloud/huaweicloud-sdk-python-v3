# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandInstanceNodeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'num': 'num',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, num=None, is_auto_pay=None):
        """ExpandInstanceNodeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._num = None
        self._is_auto_pay = None
        self.discriminator = None

        self.num = num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def num(self):
        """Gets the num of this ExpandInstanceNodeRequestBody.

        新增加的节点数量。

        :return: The num of this ExpandInstanceNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this ExpandInstanceNodeRequestBody.

        新增加的节点数量。

        :param num: The num of this ExpandInstanceNodeRequestBody.
        :type: int
        """
        self._num = num

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ExpandInstanceNodeRequestBody.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ExpandInstanceNodeRequestBody.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ExpandInstanceNodeRequestBody.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ExpandInstanceNodeRequestBody.
        :type: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ExpandInstanceNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
