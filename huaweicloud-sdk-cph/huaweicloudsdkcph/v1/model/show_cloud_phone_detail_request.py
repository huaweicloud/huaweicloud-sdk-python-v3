# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id'
    }

    def __init__(self, phone_id=None):
        """ShowCloudPhoneDetailRequest

        The model defined in huaweicloud sdk

        :param phone_id: 云手机id。
        :type phone_id: str
        """
        
        

        self._phone_id = None
        self.discriminator = None

        self.phone_id = phone_id

    @property
    def phone_id(self):
        """Gets the phone_id of this ShowCloudPhoneDetailRequest.

        云手机id。

        :return: The phone_id of this ShowCloudPhoneDetailRequest.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """Sets the phone_id of this ShowCloudPhoneDetailRequest.

        云手机id。

        :param phone_id: The phone_id of this ShowCloudPhoneDetailRequest.
        :type phone_id: str
        """
        self._phone_id = phone_id

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
        if not isinstance(other, ShowCloudPhoneDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
