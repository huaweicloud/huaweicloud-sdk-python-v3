# coding: utf-8

import pprint
import re

import six





class AppAuthResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'auth_result': 'AuthResultResp',
        'auth_time': 'datetime',
        'id': 'str',
        'app_id': 'str',
        'auth_role': 'str',
        'auth_tunnel': 'str',
        'auth_whitelist': 'list[str]',
        'auth_blacklist': 'list[str]'
    }

    attribute_map = {
        'api_id': 'api_id',
        'auth_result': 'auth_result',
        'auth_time': 'auth_time',
        'id': 'id',
        'app_id': 'app_id',
        'auth_role': 'auth_role',
        'auth_tunnel': 'auth_tunnel',
        'auth_whitelist': 'auth_whitelist',
        'auth_blacklist': 'auth_blacklist'
    }

    def __init__(self, api_id=None, auth_result=None, auth_time=None, id=None, app_id=None, auth_role=None, auth_tunnel=None, auth_whitelist=None, auth_blacklist=None):
        """AppAuthResp - a model defined in huaweicloud sdk"""
        
        

        self._api_id = None
        self._auth_result = None
        self._auth_time = None
        self._id = None
        self._app_id = None
        self._auth_role = None
        self._auth_tunnel = None
        self._auth_whitelist = None
        self._auth_blacklist = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if auth_result is not None:
            self.auth_result = auth_result
        if auth_time is not None:
            self.auth_time = auth_time
        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if auth_role is not None:
            self.auth_role = auth_role
        if auth_tunnel is not None:
            self.auth_tunnel = auth_tunnel
        if auth_whitelist is not None:
            self.auth_whitelist = auth_whitelist
        if auth_blacklist is not None:
            self.auth_blacklist = auth_blacklist

    @property
    def api_id(self):
        """Gets the api_id of this AppAuthResp.

        API编号

        :return: The api_id of this AppAuthResp.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AppAuthResp.

        API编号

        :param api_id: The api_id of this AppAuthResp.
        :type: str
        """
        self._api_id = api_id

    @property
    def auth_result(self):
        """Gets the auth_result of this AppAuthResp.


        :return: The auth_result of this AppAuthResp.
        :rtype: AuthResultResp
        """
        return self._auth_result

    @auth_result.setter
    def auth_result(self, auth_result):
        """Sets the auth_result of this AppAuthResp.


        :param auth_result: The auth_result of this AppAuthResp.
        :type: AuthResultResp
        """
        self._auth_result = auth_result

    @property
    def auth_time(self):
        """Gets the auth_time of this AppAuthResp.

        授权时间

        :return: The auth_time of this AppAuthResp.
        :rtype: datetime
        """
        return self._auth_time

    @auth_time.setter
    def auth_time(self, auth_time):
        """Sets the auth_time of this AppAuthResp.

        授权时间

        :param auth_time: The auth_time of this AppAuthResp.
        :type: datetime
        """
        self._auth_time = auth_time

    @property
    def id(self):
        """Gets the id of this AppAuthResp.

        授权关系编号

        :return: The id of this AppAuthResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppAuthResp.

        授权关系编号

        :param id: The id of this AppAuthResp.
        :type: str
        """
        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this AppAuthResp.

        APP编号

        :return: The app_id of this AppAuthResp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppAuthResp.

        APP编号

        :param app_id: The app_id of this AppAuthResp.
        :type: str
        """
        self._app_id = app_id

    @property
    def auth_role(self):
        """Gets the auth_role of this AppAuthResp.

        授权者 - PROVIDER：API提供者授权 - CONSUMER：API消费者授权

        :return: The auth_role of this AppAuthResp.
        :rtype: str
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        """Sets the auth_role of this AppAuthResp.

        授权者 - PROVIDER：API提供者授权 - CONSUMER：API消费者授权

        :param auth_role: The auth_role of this AppAuthResp.
        :type: str
        """
        self._auth_role = auth_role

    @property
    def auth_tunnel(self):
        """Gets the auth_tunnel of this AppAuthResp.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :return: The auth_tunnel of this AppAuthResp.
        :rtype: str
        """
        return self._auth_tunnel

    @auth_tunnel.setter
    def auth_tunnel(self, auth_tunnel):
        """Sets the auth_tunnel of this AppAuthResp.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :param auth_tunnel: The auth_tunnel of this AppAuthResp.
        :type: str
        """
        self._auth_tunnel = auth_tunnel

    @property
    def auth_whitelist(self):
        """Gets the auth_whitelist of this AppAuthResp.

        绿色通道的白名单配置

        :return: The auth_whitelist of this AppAuthResp.
        :rtype: list[str]
        """
        return self._auth_whitelist

    @auth_whitelist.setter
    def auth_whitelist(self, auth_whitelist):
        """Sets the auth_whitelist of this AppAuthResp.

        绿色通道的白名单配置

        :param auth_whitelist: The auth_whitelist of this AppAuthResp.
        :type: list[str]
        """
        self._auth_whitelist = auth_whitelist

    @property
    def auth_blacklist(self):
        """Gets the auth_blacklist of this AppAuthResp.

        绿色通道的黑名单配置

        :return: The auth_blacklist of this AppAuthResp.
        :rtype: list[str]
        """
        return self._auth_blacklist

    @auth_blacklist.setter
    def auth_blacklist(self, auth_blacklist):
        """Sets the auth_blacklist of this AppAuthResp.

        绿色通道的黑名单配置

        :param auth_blacklist: The auth_blacklist of this AppAuthResp.
        :type: list[str]
        """
        self._auth_blacklist = auth_blacklist

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppAuthResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
