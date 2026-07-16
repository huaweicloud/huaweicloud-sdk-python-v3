# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'int',
        'gid': 'int',
        'user_name': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'gid': 'gid',
        'user_name': 'user_name',
        'group_name': 'group_name'
    }

    def __init__(self, uid=None, gid=None, user_name=None, group_name=None):
        r"""RunUserInfo

        The model defined in huaweicloud sdk

        :param uid: 容器启动用户的user id
        :type uid: int
        :param gid: 容器启动用户的group id
        :type gid: int
        :param user_name: 容器启动用户的user name
        :type user_name: str
        :param group_name: 容器启动用户的group name
        :type group_name: str
        """
        
        

        self._uid = None
        self._gid = None
        self._user_name = None
        self._group_name = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if user_name is not None:
            self.user_name = user_name
        if group_name is not None:
            self.group_name = group_name

    @property
    def uid(self):
        r"""Gets the uid of this RunUserInfo.

        容器启动用户的user id

        :return: The uid of this RunUserInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this RunUserInfo.

        容器启动用户的user id

        :param uid: The uid of this RunUserInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this RunUserInfo.

        容器启动用户的group id

        :return: The gid of this RunUserInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this RunUserInfo.

        容器启动用户的group id

        :param gid: The gid of this RunUserInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def user_name(self):
        r"""Gets the user_name of this RunUserInfo.

        容器启动用户的user name

        :return: The user_name of this RunUserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RunUserInfo.

        容器启动用户的user name

        :param user_name: The user_name of this RunUserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def group_name(self):
        r"""Gets the group_name of this RunUserInfo.

        容器启动用户的group name

        :return: The group_name of this RunUserInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this RunUserInfo.

        容器启动用户的group name

        :param group_name: The group_name of this RunUserInfo.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, RunUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
