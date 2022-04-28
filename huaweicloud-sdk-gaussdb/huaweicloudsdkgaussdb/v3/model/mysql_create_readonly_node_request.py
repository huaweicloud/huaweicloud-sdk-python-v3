# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlCreateReadonlyNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'priorities': 'list[int]',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'priorities': 'priorities',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, priorities=None, is_auto_pay=None):
        """MysqlCreateReadonlyNodeRequest

        The model defined in huaweicloud sdk

        :param priorities: 指定创建的只读节点故障倒换优先级。 故障倒换优先级的取值范围为1~16(只读节点个数最大值)，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的备节点上，优先级相同的备节点选为主节点的概率相同。
        :type priorities: list[int]
        :param is_auto_pay: 创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。
        :type is_auto_pay: str
        """
        
        

        self._priorities = None
        self._is_auto_pay = None
        self.discriminator = None

        self.priorities = priorities
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def priorities(self):
        """Gets the priorities of this MysqlCreateReadonlyNodeRequest.

        指定创建的只读节点故障倒换优先级。 故障倒换优先级的取值范围为1~16(只读节点个数最大值)，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的备节点上，优先级相同的备节点选为主节点的概率相同。

        :return: The priorities of this MysqlCreateReadonlyNodeRequest.
        :rtype: list[int]
        """
        return self._priorities

    @priorities.setter
    def priorities(self, priorities):
        """Sets the priorities of this MysqlCreateReadonlyNodeRequest.

        指定创建的只读节点故障倒换优先级。 故障倒换优先级的取值范围为1~16(只读节点个数最大值)，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的备节点上，优先级相同的备节点选为主节点的概率相同。

        :param priorities: The priorities of this MysqlCreateReadonlyNodeRequest.
        :type priorities: list[int]
        """
        self._priorities = priorities

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this MysqlCreateReadonlyNodeRequest.

        创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。

        :return: The is_auto_pay of this MysqlCreateReadonlyNodeRequest.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this MysqlCreateReadonlyNodeRequest.

        创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。

        :param is_auto_pay: The is_auto_pay of this MysqlCreateReadonlyNodeRequest.
        :type is_auto_pay: str
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
        if not isinstance(other, MysqlCreateReadonlyNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
