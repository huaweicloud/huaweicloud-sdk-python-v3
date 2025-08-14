# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserSessionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'int',
        'ip_address': 'str',
        'session_id': 'str',
        'session_not_valid_after': 'int',
        'user_agent': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'ip_address': 'ip_address',
        'session_id': 'session_id',
        'session_not_valid_after': 'session_not_valid_after',
        'user_agent': 'user_agent',
        'user_id': 'user_id'
    }

    def __init__(self, creation_time=None, ip_address=None, session_id=None, session_not_valid_after=None, user_agent=None, user_id=None):
        r"""UserSessionDto

        The model defined in huaweicloud sdk

        :param creation_time: 会话创建时间
        :type creation_time: int
        :param ip_address: 用户IP地址
        :type ip_address: str
        :param session_id: 会话ID
        :type session_id: str
        :param session_not_valid_after: 会话失效时间
        :type session_not_valid_after: int
        :param user_agent: 用户客户端信息
        :type user_agent: str
        :param user_id: 用户唯一标识ID
        :type user_id: str
        """
        
        

        self._creation_time = None
        self._ip_address = None
        self._session_id = None
        self._session_not_valid_after = None
        self._user_agent = None
        self._user_id = None
        self.discriminator = None

        self.creation_time = creation_time
        if ip_address is not None:
            self.ip_address = ip_address
        self.session_id = session_id
        self.session_not_valid_after = session_not_valid_after
        if user_agent is not None:
            self.user_agent = user_agent
        self.user_id = user_id

    @property
    def creation_time(self):
        r"""Gets the creation_time of this UserSessionDto.

        会话创建时间

        :return: The creation_time of this UserSessionDto.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this UserSessionDto.

        会话创建时间

        :param creation_time: The creation_time of this UserSessionDto.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def ip_address(self):
        r"""Gets the ip_address of this UserSessionDto.

        用户IP地址

        :return: The ip_address of this UserSessionDto.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this UserSessionDto.

        用户IP地址

        :param ip_address: The ip_address of this UserSessionDto.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def session_id(self):
        r"""Gets the session_id of this UserSessionDto.

        会话ID

        :return: The session_id of this UserSessionDto.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this UserSessionDto.

        会话ID

        :param session_id: The session_id of this UserSessionDto.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def session_not_valid_after(self):
        r"""Gets the session_not_valid_after of this UserSessionDto.

        会话失效时间

        :return: The session_not_valid_after of this UserSessionDto.
        :rtype: int
        """
        return self._session_not_valid_after

    @session_not_valid_after.setter
    def session_not_valid_after(self, session_not_valid_after):
        r"""Sets the session_not_valid_after of this UserSessionDto.

        会话失效时间

        :param session_not_valid_after: The session_not_valid_after of this UserSessionDto.
        :type session_not_valid_after: int
        """
        self._session_not_valid_after = session_not_valid_after

    @property
    def user_agent(self):
        r"""Gets the user_agent of this UserSessionDto.

        用户客户端信息

        :return: The user_agent of this UserSessionDto.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        r"""Sets the user_agent of this UserSessionDto.

        用户客户端信息

        :param user_agent: The user_agent of this UserSessionDto.
        :type user_agent: str
        """
        self._user_agent = user_agent

    @property
    def user_id(self):
        r"""Gets the user_id of this UserSessionDto.

        用户唯一标识ID

        :return: The user_id of this UserSessionDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UserSessionDto.

        用户唯一标识ID

        :param user_id: The user_id of this UserSessionDto.
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
        if not isinstance(other, UserSessionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
