# coding: utf-8

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
        'is_auto_pay': 'str',
        'availability_zones': 'list[str]'
    }

    attribute_map = {
        'priorities': 'priorities',
        'is_auto_pay': 'is_auto_pay',
        'availability_zones': 'availability_zones'
    }

    def __init__(self, priorities=None, is_auto_pay=None, availability_zones=None):
        """MysqlCreateReadonlyNodeRequest

        The model defined in huaweicloud sdk

        :param priorities: 指定创建的只读节点故障倒换优先级。  故障倒换优先级的取值范围为1~16，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。最多支持9个只读节点设置故障倒换优先级，超过9个的只读节点优先级默认为-1，表示不会参与倒换。可通过修改节点的故障倒换优先级来进行调整。
        :type priorities: list[int]
        :param is_auto_pay: 创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。
        :type is_auto_pay: str
        :param availability_zones: 可用区。可指定可用区创建只读节点，不传该参数时默认为自动选择可用区。  调用[查询数据库规格](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlFlavors.html)获取，其中az_status中的key为availability_zone。  注：指定可用区创建只读节点，可能由于资源不足创建失败。
        :type availability_zones: list[str]
        """
        
        

        self._priorities = None
        self._is_auto_pay = None
        self._availability_zones = None
        self.discriminator = None

        self.priorities = priorities
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if availability_zones is not None:
            self.availability_zones = availability_zones

    @property
    def priorities(self):
        """Gets the priorities of this MysqlCreateReadonlyNodeRequest.

        指定创建的只读节点故障倒换优先级。  故障倒换优先级的取值范围为1~16，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。最多支持9个只读节点设置故障倒换优先级，超过9个的只读节点优先级默认为-1，表示不会参与倒换。可通过修改节点的故障倒换优先级来进行调整。

        :return: The priorities of this MysqlCreateReadonlyNodeRequest.
        :rtype: list[int]
        """
        return self._priorities

    @priorities.setter
    def priorities(self, priorities):
        """Sets the priorities of this MysqlCreateReadonlyNodeRequest.

        指定创建的只读节点故障倒换优先级。  故障倒换优先级的取值范围为1~16，数字越小，优先级越大，即故障倒换时，主节点会优先倒换到优先级高的只读节点上，优先级相同的只读节点选为主节点的概率相同。最多支持9个只读节点设置故障倒换优先级，超过9个的只读节点优先级默认为-1，表示不会参与倒换。可通过修改节点的故障倒换优先级来进行调整。

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

    @property
    def availability_zones(self):
        """Gets the availability_zones of this MysqlCreateReadonlyNodeRequest.

        可用区。可指定可用区创建只读节点，不传该参数时默认为自动选择可用区。  调用[查询数据库规格](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlFlavors.html)获取，其中az_status中的key为availability_zone。  注：指定可用区创建只读节点，可能由于资源不足创建失败。

        :return: The availability_zones of this MysqlCreateReadonlyNodeRequest.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this MysqlCreateReadonlyNodeRequest.

        可用区。可指定可用区创建只读节点，不传该参数时默认为自动选择可用区。  调用[查询数据库规格](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlFlavors.html)获取，其中az_status中的key为availability_zone。  注：指定可用区创建只读节点，可能由于资源不足创建失败。

        :param availability_zones: The availability_zones of this MysqlCreateReadonlyNodeRequest.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

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
