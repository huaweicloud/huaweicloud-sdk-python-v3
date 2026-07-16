# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserInfoObj:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'user_id'
    }

    def __init__(self, name=None, user_id=None):
        r"""UserInfoObj

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 用户的显示名称。 **取值范围：** 任意字符串。 
        :type name: str
        :param user_id: **参数解释：** 用户在账号系统中的唯一身份ID。 **取值范围：** 不涉及 
        :type user_id: str
        """
        
        

        self._name = None
        self._user_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this UserInfoObj.

        **参数解释：** 用户的显示名称。 **取值范围：** 任意字符串。 

        :return: The name of this UserInfoObj.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserInfoObj.

        **参数解释：** 用户的显示名称。 **取值范围：** 任意字符串。 

        :param name: The name of this UserInfoObj.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        r"""Gets the user_id of this UserInfoObj.

        **参数解释：** 用户在账号系统中的唯一身份ID。 **取值范围：** 不涉及 

        :return: The user_id of this UserInfoObj.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UserInfoObj.

        **参数解释：** 用户在账号系统中的唯一身份ID。 **取值范围：** 不涉及 

        :param user_id: The user_id of this UserInfoObj.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, UserInfoObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
