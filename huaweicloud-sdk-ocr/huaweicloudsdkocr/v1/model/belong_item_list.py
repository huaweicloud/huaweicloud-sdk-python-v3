# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BelongItemList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'item_number': 'str',
        'specification': 'str',
        'unit': 'str',
        'quantity': 'str',
        'unit_price': 'str',
        'amount': 'str',
        'tax_rate': 'str',
        'tax': 'str'
    }

    attribute_map = {
        'name': 'name',
        'item_number': 'item_number',
        'specification': 'specification',
        'unit': 'unit',
        'quantity': 'quantity',
        'unit_price': 'unit_price',
        'amount': 'amount',
        'tax_rate': 'tax_rate',
        'tax': 'tax'
    }

    def __init__(self, name=None, item_number=None, specification=None, unit=None, quantity=None, unit_price=None, amount=None, tax_rate=None, tax=None):
        r"""BelongItemList

        The model defined in huaweicloud sdk

        :param name: 货物或应税劳务、服务名称。 
        :type name: str
        :param item_number: 序号。 
        :type item_number: str
        :param specification: 规格型号。 
        :type specification: str
        :param unit: 单位。 
        :type unit: str
        :param quantity: 数量。 
        :type quantity: str
        :param unit_price: 单价。 
        :type unit_price: str
        :param amount: 金额。 
        :type amount: str
        :param tax_rate: 税率。 
        :type tax_rate: str
        :param tax: 税额。 
        :type tax: str
        """
        
        

        self._name = None
        self._item_number = None
        self._specification = None
        self._unit = None
        self._quantity = None
        self._unit_price = None
        self._amount = None
        self._tax_rate = None
        self._tax = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if item_number is not None:
            self.item_number = item_number
        if specification is not None:
            self.specification = specification
        if unit is not None:
            self.unit = unit
        if quantity is not None:
            self.quantity = quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if amount is not None:
            self.amount = amount
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax is not None:
            self.tax = tax

    @property
    def name(self):
        r"""Gets the name of this BelongItemList.

        货物或应税劳务、服务名称。 

        :return: The name of this BelongItemList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BelongItemList.

        货物或应税劳务、服务名称。 

        :param name: The name of this BelongItemList.
        :type name: str
        """
        self._name = name

    @property
    def item_number(self):
        r"""Gets the item_number of this BelongItemList.

        序号。 

        :return: The item_number of this BelongItemList.
        :rtype: str
        """
        return self._item_number

    @item_number.setter
    def item_number(self, item_number):
        r"""Sets the item_number of this BelongItemList.

        序号。 

        :param item_number: The item_number of this BelongItemList.
        :type item_number: str
        """
        self._item_number = item_number

    @property
    def specification(self):
        r"""Gets the specification of this BelongItemList.

        规格型号。 

        :return: The specification of this BelongItemList.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this BelongItemList.

        规格型号。 

        :param specification: The specification of this BelongItemList.
        :type specification: str
        """
        self._specification = specification

    @property
    def unit(self):
        r"""Gets the unit of this BelongItemList.

        单位。 

        :return: The unit of this BelongItemList.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this BelongItemList.

        单位。 

        :param unit: The unit of this BelongItemList.
        :type unit: str
        """
        self._unit = unit

    @property
    def quantity(self):
        r"""Gets the quantity of this BelongItemList.

        数量。 

        :return: The quantity of this BelongItemList.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this BelongItemList.

        数量。 

        :param quantity: The quantity of this BelongItemList.
        :type quantity: str
        """
        self._quantity = quantity

    @property
    def unit_price(self):
        r"""Gets the unit_price of this BelongItemList.

        单价。 

        :return: The unit_price of this BelongItemList.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        r"""Sets the unit_price of this BelongItemList.

        单价。 

        :param unit_price: The unit_price of this BelongItemList.
        :type unit_price: str
        """
        self._unit_price = unit_price

    @property
    def amount(self):
        r"""Gets the amount of this BelongItemList.

        金额。 

        :return: The amount of this BelongItemList.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this BelongItemList.

        金额。 

        :param amount: The amount of this BelongItemList.
        :type amount: str
        """
        self._amount = amount

    @property
    def tax_rate(self):
        r"""Gets the tax_rate of this BelongItemList.

        税率。 

        :return: The tax_rate of this BelongItemList.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        r"""Sets the tax_rate of this BelongItemList.

        税率。 

        :param tax_rate: The tax_rate of this BelongItemList.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def tax(self):
        r"""Gets the tax of this BelongItemList.

        税额。 

        :return: The tax of this BelongItemList.
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        r"""Sets the tax of this BelongItemList.

        税额。 

        :param tax: The tax of this BelongItemList.
        :type tax: str
        """
        self._tax = tax

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
        if not isinstance(other, BelongItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
