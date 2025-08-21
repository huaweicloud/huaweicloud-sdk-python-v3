# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserPhone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'country_code': 'str',
        'phone': 'str',
        'default_option': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'country_code': 'country_code',
        'phone': 'phone',
        'default_option': 'default_option'
    }

    def __init__(self, id=None, country_code=None, phone=None, default_option=None):
        r"""UserPhone

        The model defined in huaweicloud sdk

        :param id: 唯一标识
        :type id: str
        :param country_code: 国家码
        :type country_code: str
        :param phone: 电话号码
        :type phone: str
        :param default_option: 是否默认
        :type default_option: bool
        """
        
        

        self._id = None
        self._country_code = None
        self._phone = None
        self._default_option = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone
        if default_option is not None:
            self.default_option = default_option

    @property
    def id(self):
        r"""Gets the id of this UserPhone.

        唯一标识

        :return: The id of this UserPhone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserPhone.

        唯一标识

        :param id: The id of this UserPhone.
        :type id: str
        """
        self._id = id

    @property
    def country_code(self):
        r"""Gets the country_code of this UserPhone.

        国家码

        :return: The country_code of this UserPhone.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        r"""Sets the country_code of this UserPhone.

        国家码

        :param country_code: The country_code of this UserPhone.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def phone(self):
        r"""Gets the phone of this UserPhone.

        电话号码

        :return: The phone of this UserPhone.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this UserPhone.

        电话号码

        :param phone: The phone of this UserPhone.
        :type phone: str
        """
        self._phone = phone

    @property
    def default_option(self):
        r"""Gets the default_option of this UserPhone.

        是否默认

        :return: The default_option of this UserPhone.
        :rtype: bool
        """
        return self._default_option

    @default_option.setter
    def default_option(self, default_option):
        r"""Sets the default_option of this UserPhone.

        是否默认

        :param default_option: The default_option of this UserPhone.
        :type default_option: bool
        """
        self._default_option = default_option

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
        if not isinstance(other, UserPhone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
