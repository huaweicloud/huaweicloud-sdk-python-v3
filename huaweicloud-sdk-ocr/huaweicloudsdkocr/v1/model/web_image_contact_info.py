# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebImageContactInfo:

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
        'phone': 'str',
        'province': 'str',
        'city': 'str',
        'district': 'str',
        'detail_address': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'province': 'province',
        'city': 'city',
        'district': 'district',
        'detail_address': 'detail_address'
    }

    def __init__(self, name=None, phone=None, province=None, city=None, district=None, detail_address=None):
        r"""WebImageContactInfo

        The model defined in huaweicloud sdk

        :param name: 传入contact_info时的返回，为姓名。 
        :type name: str
        :param phone: 传入contact_info时的返回，联系电话。 
        :type phone: str
        :param province: 传入contact_info时的返回，省。 
        :type province: str
        :param city: 传入contact_info时的返回，市。 
        :type city: str
        :param district: 传入contact_info时的返回，县区。 
        :type district: str
        :param detail_address: 传入contact_info时的返回，详细地址（不含省市区）。 
        :type detail_address: str
        """
        
        

        self._name = None
        self._phone = None
        self._province = None
        self._city = None
        self._district = None
        self._detail_address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if district is not None:
            self.district = district
        if detail_address is not None:
            self.detail_address = detail_address

    @property
    def name(self):
        r"""Gets the name of this WebImageContactInfo.

        传入contact_info时的返回，为姓名。 

        :return: The name of this WebImageContactInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WebImageContactInfo.

        传入contact_info时的返回，为姓名。 

        :param name: The name of this WebImageContactInfo.
        :type name: str
        """
        self._name = name

    @property
    def phone(self):
        r"""Gets the phone of this WebImageContactInfo.

        传入contact_info时的返回，联系电话。 

        :return: The phone of this WebImageContactInfo.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this WebImageContactInfo.

        传入contact_info时的返回，联系电话。 

        :param phone: The phone of this WebImageContactInfo.
        :type phone: str
        """
        self._phone = phone

    @property
    def province(self):
        r"""Gets the province of this WebImageContactInfo.

        传入contact_info时的返回，省。 

        :return: The province of this WebImageContactInfo.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this WebImageContactInfo.

        传入contact_info时的返回，省。 

        :param province: The province of this WebImageContactInfo.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this WebImageContactInfo.

        传入contact_info时的返回，市。 

        :return: The city of this WebImageContactInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this WebImageContactInfo.

        传入contact_info时的返回，市。 

        :param city: The city of this WebImageContactInfo.
        :type city: str
        """
        self._city = city

    @property
    def district(self):
        r"""Gets the district of this WebImageContactInfo.

        传入contact_info时的返回，县区。 

        :return: The district of this WebImageContactInfo.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        r"""Sets the district of this WebImageContactInfo.

        传入contact_info时的返回，县区。 

        :param district: The district of this WebImageContactInfo.
        :type district: str
        """
        self._district = district

    @property
    def detail_address(self):
        r"""Gets the detail_address of this WebImageContactInfo.

        传入contact_info时的返回，详细地址（不含省市区）。 

        :return: The detail_address of this WebImageContactInfo.
        :rtype: str
        """
        return self._detail_address

    @detail_address.setter
    def detail_address(self, detail_address):
        r"""Sets the detail_address of this WebImageContactInfo.

        传入contact_info时的返回，详细地址（不含省市区）。 

        :param detail_address: The detail_address of this WebImageContactInfo.
        :type detail_address: str
        """
        self._detail_address = detail_address

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
        if not isinstance(other, WebImageContactInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
