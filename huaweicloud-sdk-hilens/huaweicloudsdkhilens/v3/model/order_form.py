# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderForm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'amount': 'int',
        'used_amount': 'int',
        'cbc_order_id': 'str',
        'device_type': 'str',
        'id': 'str',
        'order_update_time': 'str',
        'status': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'used_amount': 'used_amount',
        'cbc_order_id': 'cbc_order_id',
        'device_type': 'device_type',
        'id': 'id',
        'order_update_time': 'order_update_time',
        'status': 'status'
    }

    def __init__(self, amount=None, used_amount=None, cbc_order_id=None, device_type=None, id=None, order_update_time=None, status=None):
        """OrderForm

        The model defined in huaweicloud sdk

        :param amount: 订单数量
        :type amount: int
        :param used_amount: 订到已使用数量
        :type used_amount: int
        :param cbc_order_id: cbc订单Id
        :type cbc_order_id: str
        :param device_type: 设备类别
        :type device_type: str
        :param id: 订单Id
        :type id: str
        :param order_update_time: 订单更新时间
        :type order_update_time: str
        :param status: 订单状态
        :type status: int
        """
        
        

        self._amount = None
        self._used_amount = None
        self._cbc_order_id = None
        self._device_type = None
        self._id = None
        self._order_update_time = None
        self._status = None
        self.discriminator = None

        self.amount = amount
        self.used_amount = used_amount
        self.cbc_order_id = cbc_order_id
        self.device_type = device_type
        self.id = id
        self.order_update_time = order_update_time
        self.status = status

    @property
    def amount(self):
        """Gets the amount of this OrderForm.

        订单数量

        :return: The amount of this OrderForm.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderForm.

        订单数量

        :param amount: The amount of this OrderForm.
        :type amount: int
        """
        self._amount = amount

    @property
    def used_amount(self):
        """Gets the used_amount of this OrderForm.

        订到已使用数量

        :return: The used_amount of this OrderForm.
        :rtype: int
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """Sets the used_amount of this OrderForm.

        订到已使用数量

        :param used_amount: The used_amount of this OrderForm.
        :type used_amount: int
        """
        self._used_amount = used_amount

    @property
    def cbc_order_id(self):
        """Gets the cbc_order_id of this OrderForm.

        cbc订单Id

        :return: The cbc_order_id of this OrderForm.
        :rtype: str
        """
        return self._cbc_order_id

    @cbc_order_id.setter
    def cbc_order_id(self, cbc_order_id):
        """Sets the cbc_order_id of this OrderForm.

        cbc订单Id

        :param cbc_order_id: The cbc_order_id of this OrderForm.
        :type cbc_order_id: str
        """
        self._cbc_order_id = cbc_order_id

    @property
    def device_type(self):
        """Gets the device_type of this OrderForm.

        设备类别

        :return: The device_type of this OrderForm.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this OrderForm.

        设备类别

        :param device_type: The device_type of this OrderForm.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def id(self):
        """Gets the id of this OrderForm.

        订单Id

        :return: The id of this OrderForm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderForm.

        订单Id

        :param id: The id of this OrderForm.
        :type id: str
        """
        self._id = id

    @property
    def order_update_time(self):
        """Gets the order_update_time of this OrderForm.

        订单更新时间

        :return: The order_update_time of this OrderForm.
        :rtype: str
        """
        return self._order_update_time

    @order_update_time.setter
    def order_update_time(self, order_update_time):
        """Sets the order_update_time of this OrderForm.

        订单更新时间

        :param order_update_time: The order_update_time of this OrderForm.
        :type order_update_time: str
        """
        self._order_update_time = order_update_time

    @property
    def status(self):
        """Gets the status of this OrderForm.

        订单状态

        :return: The status of this OrderForm.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderForm.

        订单状态

        :param status: The status of this OrderForm.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, OrderForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
