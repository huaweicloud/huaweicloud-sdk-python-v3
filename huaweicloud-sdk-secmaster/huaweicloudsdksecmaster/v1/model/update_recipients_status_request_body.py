# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecipientsStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'email_address': 'str'
    }

    attribute_map = {
        'email_address': 'email_address'
    }

    def __init__(self, email_address=None):
        r"""UpdateRecipientsStatusRequestBody

        The model defined in huaweicloud sdk

        :param email_address: 收件人邮箱
        :type email_address: str
        """
        
        

        self._email_address = None
        self.discriminator = None

        self.email_address = email_address

    @property
    def email_address(self):
        r"""Gets the email_address of this UpdateRecipientsStatusRequestBody.

        收件人邮箱

        :return: The email_address of this UpdateRecipientsStatusRequestBody.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        r"""Sets the email_address of this UpdateRecipientsStatusRequestBody.

        收件人邮箱

        :param email_address: The email_address of this UpdateRecipientsStatusRequestBody.
        :type email_address: str
        """
        self._email_address = email_address

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRecipientsStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
