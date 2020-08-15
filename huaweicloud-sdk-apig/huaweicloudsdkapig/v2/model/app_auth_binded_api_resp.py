# coding: utf-8

import pprint
import re

import six





class AppAuthBindedApiResp:


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
        'app_name': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'api_type': 'int',
        'api_name': 'str',
        'app_id': 'str',
        'auth_time': 'datetime',
        'app_creator': 'str',
        'app_type': 'str',
        'id': 'str',
        'api_remark': 'str',
        'auth_role': 'str',
        'auth_tunnel': 'str',
        'auth_whitelist': 'list[str]',
        'auth_blacklist': 'list[str]'
    }

    attribute_map = {
        'api_id': 'api_id',
        'app_name': 'app_name',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'api_type': 'api_type',
        'api_name': 'api_name',
        'app_id': 'app_id',
        'auth_time': 'auth_time',
        'app_creator': 'app_creator',
        'app_type': 'app_type',
        'id': 'id',
        'api_remark': 'api_remark',
        'auth_role': 'auth_role',
        'auth_tunnel': 'auth_tunnel',
        'auth_whitelist': 'auth_whitelist',
        'auth_blacklist': 'auth_blacklist'
    }

    def __init__(self, api_id=None, app_name=None, env_id=None, env_name=None, group_id=None, group_name=None, api_type=None, api_name=None, app_id=None, auth_time=None, app_creator=None, app_type=None, id=None, api_remark=None, auth_role=None, auth_tunnel=None, auth_whitelist=None, auth_blacklist=None):
        """AppAuthBindedApiResp - a model defined in huaweicloud sdk"""
        
        

        self._api_id = None
        self._app_name = None
        self._env_id = None
        self._env_name = None
        self._group_id = None
        self._group_name = None
        self._api_type = None
        self._api_name = None
        self._app_id = None
        self._auth_time = None
        self._app_creator = None
        self._app_type = None
        self._id = None
        self._api_remark = None
        self._auth_role = None
        self._auth_tunnel = None
        self._auth_whitelist = None
        self._auth_blacklist = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if app_name is not None:
            self.app_name = app_name
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if api_type is not None:
            self.api_type = api_type
        if api_name is not None:
            self.api_name = api_name
        if app_id is not None:
            self.app_id = app_id
        if auth_time is not None:
            self.auth_time = auth_time
        if app_creator is not None:
            self.app_creator = app_creator
        if app_type is not None:
            self.app_type = app_type
        if id is not None:
            self.id = id
        if api_remark is not None:
            self.api_remark = api_remark
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
        """Gets the api_id of this AppAuthBindedApiResp.

        API的编号

        :return: The api_id of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AppAuthBindedApiResp.

        API的编号

        :param api_id: The api_id of this AppAuthBindedApiResp.
        :type: str
        """
        self._api_id = api_id

    @property
    def app_name(self):
        """Gets the app_name of this AppAuthBindedApiResp.

        APP的名称

        :return: The app_name of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppAuthBindedApiResp.

        APP的名称

        :param app_name: The app_name of this AppAuthBindedApiResp.
        :type: str
        """
        self._app_name = app_name

    @property
    def env_id(self):
        """Gets the env_id of this AppAuthBindedApiResp.

        api授权绑定的环境ID

        :return: The env_id of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AppAuthBindedApiResp.

        api授权绑定的环境ID

        :param env_id: The env_id of this AppAuthBindedApiResp.
        :type: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this AppAuthBindedApiResp.

        api授权绑定的环境名称

        :return: The env_name of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this AppAuthBindedApiResp.

        api授权绑定的环境名称

        :param env_name: The env_name of this AppAuthBindedApiResp.
        :type: str
        """
        self._env_name = env_name

    @property
    def group_id(self):
        """Gets the group_id of this AppAuthBindedApiResp.

        API绑定的分组ID

        :return: The group_id of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AppAuthBindedApiResp.

        API绑定的分组ID

        :param group_id: The group_id of this AppAuthBindedApiResp.
        :type: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this AppAuthBindedApiResp.

        API绑定的分组名称

        :return: The group_name of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AppAuthBindedApiResp.

        API绑定的分组名称

        :param group_name: The group_name of this AppAuthBindedApiResp.
        :type: str
        """
        self._group_name = group_name

    @property
    def api_type(self):
        """Gets the api_type of this AppAuthBindedApiResp.

        API类型

        :return: The api_type of this AppAuthBindedApiResp.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this AppAuthBindedApiResp.

        API类型

        :param api_type: The api_type of this AppAuthBindedApiResp.
        :type: int
        """
        self._api_type = api_type

    @property
    def api_name(self):
        """Gets the api_name of this AppAuthBindedApiResp.

        API的名称

        :return: The api_name of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this AppAuthBindedApiResp.

        API的名称

        :param api_name: The api_name of this AppAuthBindedApiResp.
        :type: str
        """
        self._api_name = api_name

    @property
    def app_id(self):
        """Gets the app_id of this AppAuthBindedApiResp.

        APP的编号

        :return: The app_id of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppAuthBindedApiResp.

        APP的编号

        :param app_id: The app_id of this AppAuthBindedApiResp.
        :type: str
        """
        self._app_id = app_id

    @property
    def auth_time(self):
        """Gets the auth_time of this AppAuthBindedApiResp.

        授权创建的时间

        :return: The auth_time of this AppAuthBindedApiResp.
        :rtype: datetime
        """
        return self._auth_time

    @auth_time.setter
    def auth_time(self, auth_time):
        """Sets the auth_time of this AppAuthBindedApiResp.

        授权创建的时间

        :param auth_time: The auth_time of this AppAuthBindedApiResp.
        :type: datetime
        """
        self._auth_time = auth_time

    @property
    def app_creator(self):
        """Gets the app_creator of this AppAuthBindedApiResp.

        APP的创建者，取值如下： - USER：租户自己创建 - MARKET：API市场分配

        :return: The app_creator of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._app_creator

    @app_creator.setter
    def app_creator(self, app_creator):
        """Sets the app_creator of this AppAuthBindedApiResp.

        APP的创建者，取值如下： - USER：租户自己创建 - MARKET：API市场分配

        :param app_creator: The app_creator of this AppAuthBindedApiResp.
        :type: str
        """
        self._app_creator = app_creator

    @property
    def app_type(self):
        """Gets the app_type of this AppAuthBindedApiResp.

        APP的类型  默认为apig，暂不支持其他类型

        :return: The app_type of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppAuthBindedApiResp.

        APP的类型  默认为apig，暂不支持其他类型

        :param app_type: The app_type of this AppAuthBindedApiResp.
        :type: str
        """
        self._app_type = app_type

    @property
    def id(self):
        """Gets the id of this AppAuthBindedApiResp.

        授权关系编号

        :return: The id of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppAuthBindedApiResp.

        授权关系编号

        :param id: The id of this AppAuthBindedApiResp.
        :type: str
        """
        self._id = id

    @property
    def api_remark(self):
        """Gets the api_remark of this AppAuthBindedApiResp.

        API的描述信息

        :return: The api_remark of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        """Sets the api_remark of this AppAuthBindedApiResp.

        API的描述信息

        :param api_remark: The api_remark of this AppAuthBindedApiResp.
        :type: str
        """
        self._api_remark = api_remark

    @property
    def auth_role(self):
        """Gets the auth_role of this AppAuthBindedApiResp.

        授权者

        :return: The auth_role of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        """Sets the auth_role of this AppAuthBindedApiResp.

        授权者

        :param auth_role: The auth_role of this AppAuthBindedApiResp.
        :type: str
        """
        self._auth_role = auth_role

    @property
    def auth_tunnel(self):
        """Gets the auth_tunnel of this AppAuthBindedApiResp.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :return: The auth_tunnel of this AppAuthBindedApiResp.
        :rtype: str
        """
        return self._auth_tunnel

    @auth_tunnel.setter
    def auth_tunnel(self, auth_tunnel):
        """Sets the auth_tunnel of this AppAuthBindedApiResp.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :param auth_tunnel: The auth_tunnel of this AppAuthBindedApiResp.
        :type: str
        """
        self._auth_tunnel = auth_tunnel

    @property
    def auth_whitelist(self):
        """Gets the auth_whitelist of this AppAuthBindedApiResp.

        绿色通道的白名单配置

        :return: The auth_whitelist of this AppAuthBindedApiResp.
        :rtype: list[str]
        """
        return self._auth_whitelist

    @auth_whitelist.setter
    def auth_whitelist(self, auth_whitelist):
        """Sets the auth_whitelist of this AppAuthBindedApiResp.

        绿色通道的白名单配置

        :param auth_whitelist: The auth_whitelist of this AppAuthBindedApiResp.
        :type: list[str]
        """
        self._auth_whitelist = auth_whitelist

    @property
    def auth_blacklist(self):
        """Gets the auth_blacklist of this AppAuthBindedApiResp.

        绿色通道的黑名单配置

        :return: The auth_blacklist of this AppAuthBindedApiResp.
        :rtype: list[str]
        """
        return self._auth_blacklist

    @auth_blacklist.setter
    def auth_blacklist(self, auth_blacklist):
        """Sets the auth_blacklist of this AppAuthBindedApiResp.

        绿色通道的黑名单配置

        :param auth_blacklist: The auth_blacklist of this AppAuthBindedApiResp.
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
        if not isinstance(other, AppAuthBindedApiResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
