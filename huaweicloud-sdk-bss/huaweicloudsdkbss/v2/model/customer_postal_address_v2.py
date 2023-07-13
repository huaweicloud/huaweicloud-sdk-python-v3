# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerPostalAddressV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_id': 'str',
        'recipient': 'str',
        'nationality': 'str',
        'province': 'str',
        'city': 'str',
        'district': 'str',
        'address': 'str',
        'zipcode': 'str',
        'areacode': 'str',
        'mobile_phone': 'str',
        'is_default': 'int'
    }

    attribute_map = {
        'address_id': 'address_id',
        'recipient': 'recipient',
        'nationality': 'nationality',
        'province': 'province',
        'city': 'city',
        'district': 'district',
        'address': 'address',
        'zipcode': 'zipcode',
        'areacode': 'areacode',
        'mobile_phone': 'mobile_phone',
        'is_default': 'is_default'
    }

    def __init__(self, address_id=None, recipient=None, nationality=None, province=None, city=None, district=None, address=None, zipcode=None, areacode=None, mobile_phone=None, is_default=None):
        """CustomerPostalAddressV2

        The model defined in huaweicloud sdk

        :param address_id: 邮寄地址ID。
        :type address_id: str
        :param recipient: 收件人姓名。
        :type recipient: str
        :param nationality: 国家。例如：中国
        :type nationality: str
        :param province: 省/自治区/直辖市。例如：江苏省。
        :type province: str
        :param city: 市/区。例如：南京市。
        :type city: str
        :param district: 区。例如：雨花区。
        :type district: str
        :param address: 邮寄详细地址。
        :type address: str
        :param zipcode: 邮编。
        :type zipcode: str
        :param areacode: 国家码。例如： 中国：0086
        :type areacode: str
        :param mobile_phone: 手机号码，不带国家码。
        :type mobile_phone: str
        :param is_default: 是否默认地址，默认值为“0：非默认地址”。 1：默认地址0：非默认地址
        :type is_default: int
        """
        
        

        self._address_id = None
        self._recipient = None
        self._nationality = None
        self._province = None
        self._city = None
        self._district = None
        self._address = None
        self._zipcode = None
        self._areacode = None
        self._mobile_phone = None
        self._is_default = None
        self.discriminator = None

        if address_id is not None:
            self.address_id = address_id
        if recipient is not None:
            self.recipient = recipient
        if nationality is not None:
            self.nationality = nationality
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if district is not None:
            self.district = district
        if address is not None:
            self.address = address
        if zipcode is not None:
            self.zipcode = zipcode
        if areacode is not None:
            self.areacode = areacode
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if is_default is not None:
            self.is_default = is_default

    @property
    def address_id(self):
        """Gets the address_id of this CustomerPostalAddressV2.

        邮寄地址ID。

        :return: The address_id of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this CustomerPostalAddressV2.

        邮寄地址ID。

        :param address_id: The address_id of this CustomerPostalAddressV2.
        :type address_id: str
        """
        self._address_id = address_id

    @property
    def recipient(self):
        """Gets the recipient of this CustomerPostalAddressV2.

        收件人姓名。

        :return: The recipient of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this CustomerPostalAddressV2.

        收件人姓名。

        :param recipient: The recipient of this CustomerPostalAddressV2.
        :type recipient: str
        """
        self._recipient = recipient

    @property
    def nationality(self):
        """Gets the nationality of this CustomerPostalAddressV2.

        国家。例如：中国

        :return: The nationality of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this CustomerPostalAddressV2.

        国家。例如：中国

        :param nationality: The nationality of this CustomerPostalAddressV2.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def province(self):
        """Gets the province of this CustomerPostalAddressV2.

        省/自治区/直辖市。例如：江苏省。

        :return: The province of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this CustomerPostalAddressV2.

        省/自治区/直辖市。例如：江苏省。

        :param province: The province of this CustomerPostalAddressV2.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this CustomerPostalAddressV2.

        市/区。例如：南京市。

        :return: The city of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerPostalAddressV2.

        市/区。例如：南京市。

        :param city: The city of this CustomerPostalAddressV2.
        :type city: str
        """
        self._city = city

    @property
    def district(self):
        """Gets the district of this CustomerPostalAddressV2.

        区。例如：雨花区。

        :return: The district of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this CustomerPostalAddressV2.

        区。例如：雨花区。

        :param district: The district of this CustomerPostalAddressV2.
        :type district: str
        """
        self._district = district

    @property
    def address(self):
        """Gets the address of this CustomerPostalAddressV2.

        邮寄详细地址。

        :return: The address of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerPostalAddressV2.

        邮寄详细地址。

        :param address: The address of this CustomerPostalAddressV2.
        :type address: str
        """
        self._address = address

    @property
    def zipcode(self):
        """Gets the zipcode of this CustomerPostalAddressV2.

        邮编。

        :return: The zipcode of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this CustomerPostalAddressV2.

        邮编。

        :param zipcode: The zipcode of this CustomerPostalAddressV2.
        :type zipcode: str
        """
        self._zipcode = zipcode

    @property
    def areacode(self):
        """Gets the areacode of this CustomerPostalAddressV2.

        国家码。例如： 中国：0086

        :return: The areacode of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this CustomerPostalAddressV2.

        国家码。例如： 中国：0086

        :param areacode: The areacode of this CustomerPostalAddressV2.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this CustomerPostalAddressV2.

        手机号码，不带国家码。

        :return: The mobile_phone of this CustomerPostalAddressV2.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this CustomerPostalAddressV2.

        手机号码，不带国家码。

        :param mobile_phone: The mobile_phone of this CustomerPostalAddressV2.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def is_default(self):
        """Gets the is_default of this CustomerPostalAddressV2.

        是否默认地址，默认值为“0：非默认地址”。 1：默认地址0：非默认地址

        :return: The is_default of this CustomerPostalAddressV2.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CustomerPostalAddressV2.

        是否默认地址，默认值为“0：非默认地址”。 1：默认地址0：非默认地址

        :param is_default: The is_default of this CustomerPostalAddressV2.
        :type is_default: int
        """
        self._is_default = is_default

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
        if not isinstance(other, CustomerPostalAddressV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
