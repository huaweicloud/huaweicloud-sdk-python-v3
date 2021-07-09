# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateUsersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'users': 'list[CreateUsersDetailResponses]'
    }

    attribute_map = {
        'users': 'users'
    }

    def __init__(self, users=None):
        """CreateUsersResponse - a model defined in huaweicloud sdk"""
        
        super(CreateUsersResponse, self).__init__()

        self._users = None
        self.discriminator = None

        if users is not None:
            self.users = users

    @property
    def users(self):
        """Gets the users of this CreateUsersResponse.

        DDM实例帐号相关信息的集合。

        :return: The users of this CreateUsersResponse.
        :rtype: list[CreateUsersDetailResponses]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CreateUsersResponse.

        DDM实例帐号相关信息的集合。

        :param users: The users of this CreateUsersResponse.
        :type: list[CreateUsersDetailResponses]
        """
        self._users = users

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
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
