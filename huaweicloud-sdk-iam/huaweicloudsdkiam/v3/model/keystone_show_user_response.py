# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneShowUserResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user': 'KeystoneShowUserResult'
    }

    attribute_map = {
        'user': 'user'
    }

    def __init__(self, user=None):
        """KeystoneShowUserResponse - a model defined in huaweicloud sdk"""
        
        super(KeystoneShowUserResponse, self).__init__()

        self._user = None
        self.discriminator = None

        if user is not None:
            self.user = user

    @property
    def user(self):
        """Gets the user of this KeystoneShowUserResponse.


        :return: The user of this KeystoneShowUserResponse.
        :rtype: KeystoneShowUserResult
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this KeystoneShowUserResponse.


        :param user: The user of this KeystoneShowUserResponse.
        :type: KeystoneShowUserResult
        """
        self._user = user

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
        if not isinstance(other, KeystoneShowUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
