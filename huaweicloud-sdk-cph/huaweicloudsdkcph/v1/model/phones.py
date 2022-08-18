# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Phones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'phones': 'list[PhonesPhones]'
    }

    attribute_map = {
        'phones': 'phones'
    }

    def __init__(self, phones=None):
        """Phones

        The model defined in huaweicloud sdk

        :param phones: 手机列表
        :type phones: list[:class:`huaweicloudsdkcph.v1.PhonesPhones`]
        """
        
        

        self._phones = None
        self.discriminator = None

        self.phones = phones

    @property
    def phones(self):
        """Gets the phones of this Phones.

        手机列表

        :return: The phones of this Phones.
        :rtype: list[:class:`huaweicloudsdkcph.v1.PhonesPhones`]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this Phones.

        手机列表

        :param phones: The phones of this Phones.
        :type phones: list[:class:`huaweicloudsdkcph.v1.PhonesPhones`]
        """
        self._phones = phones

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
        if not isinstance(other, Phones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
