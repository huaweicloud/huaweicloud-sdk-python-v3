# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSharedInfoNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'new_user_name': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'new_user_name': 'new_user_name'
    }

    def __init__(self, user_id=None, new_user_name=None):
        r"""UpdateSharedInfoNewRequestBody

        The model defined in huaweicloud sdk

        :param user_id: 修改后共享的新用户ID
        :type user_id: str
        :param new_user_name: 修改后共享的新用户名
        :type new_user_name: str
        """
        
        

        self._user_id = None
        self._new_user_name = None
        self.discriminator = None

        self.user_id = user_id
        self.new_user_name = new_user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateSharedInfoNewRequestBody.

        修改后共享的新用户ID

        :return: The user_id of this UpdateSharedInfoNewRequestBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateSharedInfoNewRequestBody.

        修改后共享的新用户ID

        :param user_id: The user_id of this UpdateSharedInfoNewRequestBody.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def new_user_name(self):
        r"""Gets the new_user_name of this UpdateSharedInfoNewRequestBody.

        修改后共享的新用户名

        :return: The new_user_name of this UpdateSharedInfoNewRequestBody.
        :rtype: str
        """
        return self._new_user_name

    @new_user_name.setter
    def new_user_name(self, new_user_name):
        r"""Sets the new_user_name of this UpdateSharedInfoNewRequestBody.

        修改后共享的新用户名

        :param new_user_name: The new_user_name of this UpdateSharedInfoNewRequestBody.
        :type new_user_name: str
        """
        self._new_user_name = new_user_name

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
        if not isinstance(other, UpdateSharedInfoNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
