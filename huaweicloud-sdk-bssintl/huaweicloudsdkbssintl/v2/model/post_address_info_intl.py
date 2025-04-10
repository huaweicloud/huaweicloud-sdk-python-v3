# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostAddressInfoIntl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'recipients': 'str',
        'zip_code': 'str',
        'mobile_phone': 'str'
    }

    attribute_map = {
        'address': 'address',
        'recipients': 'recipients',
        'zip_code': 'zipCode',
        'mobile_phone': 'mobilePhone'
    }

    def __init__(self, address=None, recipients=None, zip_code=None, mobile_phone=None):
        r"""PostAddressInfoIntl

        The model defined in huaweicloud sdk

        :param address: 收件人地址。
        :type address: str
        :param recipients: 收件人。
        :type recipients: str
        :param zip_code: 收件所在地邮政编码。
        :type zip_code: str
        :param mobile_phone: 收件人手机号码。
        :type mobile_phone: str
        """
        
        

        self._address = None
        self._recipients = None
        self._zip_code = None
        self._mobile_phone = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if recipients is not None:
            self.recipients = recipients
        if zip_code is not None:
            self.zip_code = zip_code
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone

    @property
    def address(self):
        r"""Gets the address of this PostAddressInfoIntl.

        收件人地址。

        :return: The address of this PostAddressInfoIntl.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this PostAddressInfoIntl.

        收件人地址。

        :param address: The address of this PostAddressInfoIntl.
        :type address: str
        """
        self._address = address

    @property
    def recipients(self):
        r"""Gets the recipients of this PostAddressInfoIntl.

        收件人。

        :return: The recipients of this PostAddressInfoIntl.
        :rtype: str
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        r"""Sets the recipients of this PostAddressInfoIntl.

        收件人。

        :param recipients: The recipients of this PostAddressInfoIntl.
        :type recipients: str
        """
        self._recipients = recipients

    @property
    def zip_code(self):
        r"""Gets the zip_code of this PostAddressInfoIntl.

        收件所在地邮政编码。

        :return: The zip_code of this PostAddressInfoIntl.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        r"""Sets the zip_code of this PostAddressInfoIntl.

        收件所在地邮政编码。

        :param zip_code: The zip_code of this PostAddressInfoIntl.
        :type zip_code: str
        """
        self._zip_code = zip_code

    @property
    def mobile_phone(self):
        r"""Gets the mobile_phone of this PostAddressInfoIntl.

        收件人手机号码。

        :return: The mobile_phone of this PostAddressInfoIntl.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        r"""Sets the mobile_phone of this PostAddressInfoIntl.

        收件人手机号码。

        :param mobile_phone: The mobile_phone of this PostAddressInfoIntl.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

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
        if not isinstance(other, PostAddressInfoIntl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
