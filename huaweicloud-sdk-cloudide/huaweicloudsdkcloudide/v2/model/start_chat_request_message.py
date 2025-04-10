# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartChatRequestMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_type': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'user_type': 'user_type',
        'user_id': 'user_id'
    }

    def __init__(self, user_type=None, user_id=None):
        r"""StartChatRequestMessage

        The model defined in huaweicloud sdk

        :param user_type: user type
        :type user_type: str
        :param user_id: user id
        :type user_id: str
        """
        
        

        self._user_type = None
        self._user_id = None
        self.discriminator = None

        if user_type is not None:
            self.user_type = user_type
        if user_id is not None:
            self.user_id = user_id

    @property
    def user_type(self):
        r"""Gets the user_type of this StartChatRequestMessage.

        user type

        :return: The user_type of this StartChatRequestMessage.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this StartChatRequestMessage.

        user type

        :param user_type: The user_type of this StartChatRequestMessage.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def user_id(self):
        r"""Gets the user_id of this StartChatRequestMessage.

        user id

        :return: The user_id of this StartChatRequestMessage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this StartChatRequestMessage.

        user id

        :param user_id: The user_id of this StartChatRequestMessage.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, StartChatRequestMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
