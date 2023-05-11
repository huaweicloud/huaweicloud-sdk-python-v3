# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InviteUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_exist': 'bool'
    }

    attribute_map = {
        'user_exist': 'userExist'
    }

    def __init__(self, user_exist=None):
        """InviteUserResponse

        The model defined in huaweicloud sdk

        :param user_exist: 用户是否存在
        :type user_exist: bool
        """
        
        super(InviteUserResponse, self).__init__()

        self._user_exist = None
        self.discriminator = None

        if user_exist is not None:
            self.user_exist = user_exist

    @property
    def user_exist(self):
        """Gets the user_exist of this InviteUserResponse.

        用户是否存在

        :return: The user_exist of this InviteUserResponse.
        :rtype: bool
        """
        return self._user_exist

    @user_exist.setter
    def user_exist(self, user_exist):
        """Sets the user_exist of this InviteUserResponse.

        用户是否存在

        :param user_exist: The user_exist of this InviteUserResponse.
        :type user_exist: bool
        """
        self._user_exist = user_exist

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
        if not isinstance(other, InviteUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
