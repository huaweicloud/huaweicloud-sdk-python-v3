# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelInstanceProcessInfo:

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
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user'
    }

    def __init__(self, id=None, user=None):
        r"""CancelInstanceProcessInfo

        The model defined in huaweicloud sdk

        :param id: 进程ID
        :type id: int
        :param user: 用户名
        :type user: str
        """
        
        

        self._id = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.user = user

    @property
    def id(self):
        r"""Gets the id of this CancelInstanceProcessInfo.

        进程ID

        :return: The id of this CancelInstanceProcessInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CancelInstanceProcessInfo.

        进程ID

        :param id: The id of this CancelInstanceProcessInfo.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this CancelInstanceProcessInfo.

        用户名

        :return: The user of this CancelInstanceProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this CancelInstanceProcessInfo.

        用户名

        :param user: The user of this CancelInstanceProcessInfo.
        :type user: str
        """
        self._user = user

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
        if not isinstance(other, CancelInstanceProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
