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
        'subnet_id': 'str',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'num': 'num',
        'subnet_id': 'subnet_id',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, num=None, subnet_id=None, is_auto_pay=None):
        """ExpandInstanceNodeRequestBody

        The model defined in huaweicloud sdk

        :param num: 新增加的节点数量。
        :type num: int
        :param subnet_id: 扩容的节点所使用的子网的ID。 - 该参数仅只支持GaussDB(for Cassandra)数据库实例扩容节点时传入。 - 所传入的子网ID必须属于实例当前所在的VPC。 - 不传该参数时，系统会在当前实例所使用的子网中为当前扩容的节点选择一个IP容量较为充足的子网。
        :type subnet_id: str
        :param is_auto_pay: 创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: str
        """
        
        

        self._num = None
        self._subnet_id = None
        self._is_auto_pay = None
        self.discriminator = None

        self.num = num
        if subnet_id is not None:
            self.subnet_id = subnet_id
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
        :type num: int
        """
        self._num = num

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ExpandInstanceNodeRequestBody.

        扩容的节点所使用的子网的ID。 - 该参数仅只支持GaussDB(for Cassandra)数据库实例扩容节点时传入。 - 所传入的子网ID必须属于实例当前所在的VPC。 - 不传该参数时，系统会在当前实例所使用的子网中为当前扩容的节点选择一个IP容量较为充足的子网。

        :return: The subnet_id of this ExpandInstanceNodeRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ExpandInstanceNodeRequestBody.

        扩容的节点所使用的子网的ID。 - 该参数仅只支持GaussDB(for Cassandra)数据库实例扩容节点时传入。 - 所传入的子网ID必须属于实例当前所在的VPC。 - 不传该参数时，系统会在当前实例所使用的子网中为当前扩容的节点选择一个IP容量较为充足的子网。

        :param subnet_id: The subnet_id of this ExpandInstanceNodeRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ExpandInstanceNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
