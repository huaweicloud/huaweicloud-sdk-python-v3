# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoginResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login_id': 'int'
    }

    attribute_map = {
        'login_id': 'login_id'
    }

    def __init__(self, login_id=None):
        """CreateLoginResponse

        The model defined in huaweicloud sdk

        :param login_id: login_id
        :type login_id: int
        """
        
        super(CreateLoginResponse, self).__init__()

        self._login_id = None
        self.discriminator = None

        if login_id is not None:
            self.login_id = login_id

    @property
    def login_id(self):
        """Gets the login_id of this CreateLoginResponse.

        login_id

        :return: The login_id of this CreateLoginResponse.
        :rtype: int
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """Sets the login_id of this CreateLoginResponse.

        login_id

        :param login_id: The login_id of this CreateLoginResponse.
        :type login_id: int
        """
        self._login_id = login_id

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
        if not isinstance(other, CreateLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
