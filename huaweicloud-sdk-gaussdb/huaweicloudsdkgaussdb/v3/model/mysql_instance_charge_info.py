# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceChargeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'order_id': 'order_id'
    }

    def __init__(self, charge_mode=None, order_id=None):
        """MysqlInstanceChargeInfo

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式。
        :type charge_mode: str
        :param order_id: 订单号。
        :type order_id: str
        """
        
        

        self._charge_mode = None
        self._order_id = None
        self.discriminator = None

        self.charge_mode = charge_mode
        if order_id is not None:
            self.order_id = order_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this MysqlInstanceChargeInfo.

        计费模式。

        :return: The charge_mode of this MysqlInstanceChargeInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this MysqlInstanceChargeInfo.

        计费模式。

        :param charge_mode: The charge_mode of this MysqlInstanceChargeInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def order_id(self):
        """Gets the order_id of this MysqlInstanceChargeInfo.

        订单号。

        :return: The order_id of this MysqlInstanceChargeInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MysqlInstanceChargeInfo.

        订单号。

        :param order_id: The order_id of this MysqlInstanceChargeInfo.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, MysqlInstanceChargeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
