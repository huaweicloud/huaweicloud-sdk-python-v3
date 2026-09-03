# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnSharedInfo:

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
        'user_name': 'str',
        'shared_time': 'int',
        'expired_time': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'shared_time': 'shared_time',
        'expired_time': 'expired_time'
    }

    def __init__(self, user_id=None, user_name=None, shared_time=None, expired_time=None):
        r"""ConnSharedInfo

        The model defined in huaweicloud sdk

        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param shared_time: 共享连接创建时间
        :type shared_time: int
        :param expired_time: 共享连接过期时间
        :type expired_time: int
        """
        
        

        self._user_id = None
        self._user_name = None
        self._shared_time = None
        self._expired_time = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if shared_time is not None:
            self.shared_time = shared_time
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def user_id(self):
        r"""Gets the user_id of this ConnSharedInfo.

        用户ID

        :return: The user_id of this ConnSharedInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ConnSharedInfo.

        用户ID

        :param user_id: The user_id of this ConnSharedInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ConnSharedInfo.

        用户名

        :return: The user_name of this ConnSharedInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ConnSharedInfo.

        用户名

        :param user_name: The user_name of this ConnSharedInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def shared_time(self):
        r"""Gets the shared_time of this ConnSharedInfo.

        共享连接创建时间

        :return: The shared_time of this ConnSharedInfo.
        :rtype: int
        """
        return self._shared_time

    @shared_time.setter
    def shared_time(self, shared_time):
        r"""Sets the shared_time of this ConnSharedInfo.

        共享连接创建时间

        :param shared_time: The shared_time of this ConnSharedInfo.
        :type shared_time: int
        """
        self._shared_time = shared_time

    @property
    def expired_time(self):
        r"""Gets the expired_time of this ConnSharedInfo.

        共享连接过期时间

        :return: The expired_time of this ConnSharedInfo.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this ConnSharedInfo.

        共享连接过期时间

        :param expired_time: The expired_time of this ConnSharedInfo.
        :type expired_time: int
        """
        self._expired_time = expired_time

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
        if not isinstance(other, ConnSharedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
