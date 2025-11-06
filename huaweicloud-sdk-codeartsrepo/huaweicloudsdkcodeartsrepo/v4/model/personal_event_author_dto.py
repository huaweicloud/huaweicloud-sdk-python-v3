# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersonalEventAuthorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username'
    }

    def __init__(self, id=None, username=None):
        r"""PersonalEventAuthorDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 用户id。 **约束限制：** 不涉及。
        :type id: int
        :param username: **参数解释：** 用户名。 **约束限制：** 不涉及。
        :type username: str
        """
        
        

        self._id = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username

    @property
    def id(self):
        r"""Gets the id of this PersonalEventAuthorDto.

        **参数解释：** 用户id。 **约束限制：** 不涉及。

        :return: The id of this PersonalEventAuthorDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PersonalEventAuthorDto.

        **参数解释：** 用户id。 **约束限制：** 不涉及。

        :param id: The id of this PersonalEventAuthorDto.
        :type id: int
        """
        self._id = id

    @property
    def username(self):
        r"""Gets the username of this PersonalEventAuthorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。

        :return: The username of this PersonalEventAuthorDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this PersonalEventAuthorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。

        :param username: The username of this PersonalEventAuthorDto.
        :type username: str
        """
        self._username = username

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
        if not isinstance(other, PersonalEventAuthorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
