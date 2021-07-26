# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWindowsBaremetalServerPwdResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'password': 'str'
    }

    attribute_map = {
        'password': 'password'
    }

    def __init__(self, password=None):
        """ShowWindowsBaremetalServerPwdResponse - a model defined in huaweicloud sdk"""
        
        super(ShowWindowsBaremetalServerPwdResponse, self).__init__()

        self._password = None
        self.discriminator = None

        if password is not None:
            self.password = password

    @property
    def password(self):
        """Gets the password of this ShowWindowsBaremetalServerPwdResponse.

        加密后的密码

        :return: The password of this ShowWindowsBaremetalServerPwdResponse.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ShowWindowsBaremetalServerPwdResponse.

        加密后的密码

        :param password: The password of this ShowWindowsBaremetalServerPwdResponse.
        :type: str
        """
        self._password = password

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowWindowsBaremetalServerPwdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
