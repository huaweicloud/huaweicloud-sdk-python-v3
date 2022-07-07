# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemList:

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
        'specification': 'str',
        'unit': 'str',
        'quantity': 'str',
        'unit_price': 'str',
        'license_plate_number': 'str',
        'amount': 'str',
        'tax_rate': 'str',
        'tax': 'str',
        'end_date': 'str',
        'start_date': 'str',
        'vehicle_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'specification': 'specification',
        'unit': 'unit',
        'quantity': 'quantity',
        'unit_price': 'unit_price',
        'license_plate_number': 'license_plate_number',
        'amount': 'amount',
        'tax_rate': 'tax_rate',
        'tax': 'tax',
        'end_date': 'end_date',
        'start_date': 'start_date',
        'vehicle_type': 'vehicle_type'
    }

    def __init__(self, name=None, specification=None, unit=None, quantity=None, unit_price=None, license_plate_number=None, amount=None, tax_rate=None, tax=None, end_date=None, start_date=None, vehicle_type=None):
        """ItemList

        The model defined in huaweicloud sdk

        :param name: 货物或应税劳务、服务名称。 
        :type name: str
        :param specification: 规格型号。 
        :type specification: str
        :param unit: 单位。 
        :type unit: str
        :param quantity: 数量。 
        :type quantity: str
        :param unit_price: 单价。 
        :type unit_price: str
        :param license_plate_number: 车牌号码。 当“type”被识别为“toll”且 “advanced_mode”设置为“true” 时才返回。 
        :type license_plate_number: str
        :param amount: 金额。 
        :type amount: str
        :param tax_rate: 税率。 
        :type tax_rate: str
        :param tax: 税额。 
        :type tax: str
        :param end_date: 通行日期止。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 
        :type end_date: str
        :param start_date: 通行日期起。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 
        :type start_date: str
        :param vehicle_type: 车辆类型。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 
        :type vehicle_type: str
        """
        
        

        self._name = None
        self._specification = None
        self._unit = None
        self._quantity = None
        self._unit_price = None
        self._license_plate_number = None
        self._amount = None
        self._tax_rate = None
        self._tax = None
        self._end_date = None
        self._start_date = None
        self._vehicle_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if specification is not None:
            self.specification = specification
        if unit is not None:
            self.unit = unit
        if quantity is not None:
            self.quantity = quantity
        if unit_price is not None:
            self.unit_price = unit_price
        if license_plate_number is not None:
            self.license_plate_number = license_plate_number
        if amount is not None:
            self.amount = amount
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax is not None:
            self.tax = tax
        if end_date is not None:
            self.end_date = end_date
        if start_date is not None:
            self.start_date = start_date
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type

    @property
    def name(self):
        """Gets the name of this ItemList.

        货物或应税劳务、服务名称。 

        :return: The name of this ItemList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemList.

        货物或应税劳务、服务名称。 

        :param name: The name of this ItemList.
        :type name: str
        """
        self._name = name

    @property
    def specification(self):
        """Gets the specification of this ItemList.

        规格型号。 

        :return: The specification of this ItemList.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ItemList.

        规格型号。 

        :param specification: The specification of this ItemList.
        :type specification: str
        """
        self._specification = specification

    @property
    def unit(self):
        """Gets the unit of this ItemList.

        单位。 

        :return: The unit of this ItemList.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ItemList.

        单位。 

        :param unit: The unit of this ItemList.
        :type unit: str
        """
        self._unit = unit

    @property
    def quantity(self):
        """Gets the quantity of this ItemList.

        数量。 

        :return: The quantity of this ItemList.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ItemList.

        数量。 

        :param quantity: The quantity of this ItemList.
        :type quantity: str
        """
        self._quantity = quantity

    @property
    def unit_price(self):
        """Gets the unit_price of this ItemList.

        单价。 

        :return: The unit_price of this ItemList.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ItemList.

        单价。 

        :param unit_price: The unit_price of this ItemList.
        :type unit_price: str
        """
        self._unit_price = unit_price

    @property
    def license_plate_number(self):
        """Gets the license_plate_number of this ItemList.

        车牌号码。 当“type”被识别为“toll”且 “advanced_mode”设置为“true” 时才返回。 

        :return: The license_plate_number of this ItemList.
        :rtype: str
        """
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, license_plate_number):
        """Sets the license_plate_number of this ItemList.

        车牌号码。 当“type”被识别为“toll”且 “advanced_mode”设置为“true” 时才返回。 

        :param license_plate_number: The license_plate_number of this ItemList.
        :type license_plate_number: str
        """
        self._license_plate_number = license_plate_number

    @property
    def amount(self):
        """Gets the amount of this ItemList.

        金额。 

        :return: The amount of this ItemList.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ItemList.

        金额。 

        :param amount: The amount of this ItemList.
        :type amount: str
        """
        self._amount = amount

    @property
    def tax_rate(self):
        """Gets the tax_rate of this ItemList.

        税率。 

        :return: The tax_rate of this ItemList.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this ItemList.

        税率。 

        :param tax_rate: The tax_rate of this ItemList.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def tax(self):
        """Gets the tax of this ItemList.

        税额。 

        :return: The tax of this ItemList.
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this ItemList.

        税额。 

        :param tax: The tax of this ItemList.
        :type tax: str
        """
        self._tax = tax

    @property
    def end_date(self):
        """Gets the end_date of this ItemList.

        通行日期止。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :return: The end_date of this ItemList.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ItemList.

        通行日期止。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :param end_date: The end_date of this ItemList.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this ItemList.

        通行日期起。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :return: The start_date of this ItemList.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ItemList.

        通行日期起。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :param start_date: The start_date of this ItemList.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this ItemList.

        车辆类型。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :return: The vehicle_type of this ItemList.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this ItemList.

        车辆类型。 当“type”被识别为“toll”且“advanced_mode”设置为“true”时才返回。 

        :param vehicle_type: The vehicle_type of this ItemList.
        :type vehicle_type: str
        """
        self._vehicle_type = vehicle_type

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
        if not isinstance(other, ItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
