# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'password': 'password'
    }

    def __init__(self, id=None, user=None, password=None):
        r"""DataNode

        The model defined in huaweicloud sdk

        :param id: 实例id。
        :type id: str
        :param user: 实例账号。
        :type user: str
        :param password: 实例账号密码。
        :type password: str
        """
        
        

        self._id = None
        self._user = None
        self._password = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password

    @property
    def id(self):
        r"""Gets the id of this DataNode.

        实例id。

        :return: The id of this DataNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataNode.

        实例id。

        :param id: The id of this DataNode.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this DataNode.

        实例账号。

        :return: The user of this DataNode.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this DataNode.

        实例账号。

        :param user: The user of this DataNode.
        :type user: str
        """
        self._user = user

    @property
    def password(self):
        r"""Gets the password of this DataNode.

        实例账号密码。

        :return: The password of this DataNode.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this DataNode.

        实例账号密码。

        :param password: The password of this DataNode.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, DataNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
