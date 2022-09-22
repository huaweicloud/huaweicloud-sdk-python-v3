# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateWeakPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_weak_password': 'bool'
    }

    attribute_map = {
        'is_weak_password': 'is_weak_password'
    }

    def __init__(self, is_weak_password=None):
        """ValidateWeakPasswordResponse

        The model defined in huaweicloud sdk

        :param is_weak_password: 是否是弱密码。true为弱密码，不建议使用。false为非弱密码，可以使用。
        :type is_weak_password: bool
        """
        
        super(ValidateWeakPasswordResponse, self).__init__()

        self._is_weak_password = None
        self.discriminator = None

        if is_weak_password is not None:
            self.is_weak_password = is_weak_password

    @property
    def is_weak_password(self):
        """Gets the is_weak_password of this ValidateWeakPasswordResponse.

        是否是弱密码。true为弱密码，不建议使用。false为非弱密码，可以使用。

        :return: The is_weak_password of this ValidateWeakPasswordResponse.
        :rtype: bool
        """
        return self._is_weak_password

    @is_weak_password.setter
    def is_weak_password(self, is_weak_password):
        """Sets the is_weak_password of this ValidateWeakPasswordResponse.

        是否是弱密码。true为弱密码，不建议使用。false为非弱密码，可以使用。

        :param is_weak_password: The is_weak_password of this ValidateWeakPasswordResponse.
        :type is_weak_password: bool
        """
        self._is_weak_password = is_weak_password

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
        if not isinstance(other, ValidateWeakPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
