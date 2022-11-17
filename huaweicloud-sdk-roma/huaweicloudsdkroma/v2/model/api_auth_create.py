# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'app_ids': 'list[str]',
        'api_ids': 'list[str]',
        'auth_tunnel': 'str',
        'auth_whitelist': 'list[str]',
        'auth_blacklist': 'list[str]',
        'visit_params': 'list[ApiAuthVisitParam]'
    }

    attribute_map = {
        'env_id': 'env_id',
        'app_ids': 'app_ids',
        'api_ids': 'api_ids',
        'auth_tunnel': 'auth_tunnel',
        'auth_whitelist': 'auth_whitelist',
        'auth_blacklist': 'auth_blacklist',
        'visit_params': 'visit_params'
    }

    def __init__(self, env_id=None, app_ids=None, api_ids=None, auth_tunnel=None, auth_whitelist=None, auth_blacklist=None, visit_params=None):
        """ApiAuthCreate

        The model defined in huaweicloud sdk

        :param env_id: 需要授权的环境编号
        :type env_id: str
        :param app_ids: APP的编号列表
        :type app_ids: list[str]
        :param api_ids: API的编号列表。
        :type api_ids: list[str]
        :param auth_tunnel: 授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  实例开启green_tunnel特性时可以开启绿色通道，此字段不填默认为不使用绿色通道
        :type auth_tunnel: str
        :param auth_whitelist: 绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问，auth_tunnel &#x3D; GREEN时生效
        :type auth_whitelist: list[str]
        :param auth_blacklist: 绿色通道授权黑名单。  auth_tunnel &#x3D; GREEN时生效
        :type auth_blacklist: list[str]
        :param visit_params: 访问参数列表。
        :type visit_params: list[:class:`huaweicloudsdkroma.v2.ApiAuthVisitParam`]
        """
        
        

        self._env_id = None
        self._app_ids = None
        self._api_ids = None
        self._auth_tunnel = None
        self._auth_whitelist = None
        self._auth_blacklist = None
        self._visit_params = None
        self.discriminator = None

        self.env_id = env_id
        self.app_ids = app_ids
        self.api_ids = api_ids
        if auth_tunnel is not None:
            self.auth_tunnel = auth_tunnel
        if auth_whitelist is not None:
            self.auth_whitelist = auth_whitelist
        if auth_blacklist is not None:
            self.auth_blacklist = auth_blacklist
        if visit_params is not None:
            self.visit_params = visit_params

    @property
    def env_id(self):
        """Gets the env_id of this ApiAuthCreate.

        需要授权的环境编号

        :return: The env_id of this ApiAuthCreate.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ApiAuthCreate.

        需要授权的环境编号

        :param env_id: The env_id of this ApiAuthCreate.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def app_ids(self):
        """Gets the app_ids of this ApiAuthCreate.

        APP的编号列表

        :return: The app_ids of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this ApiAuthCreate.

        APP的编号列表

        :param app_ids: The app_ids of this ApiAuthCreate.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

    @property
    def api_ids(self):
        """Gets the api_ids of this ApiAuthCreate.

        API的编号列表。

        :return: The api_ids of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._api_ids

    @api_ids.setter
    def api_ids(self, api_ids):
        """Sets the api_ids of this ApiAuthCreate.

        API的编号列表。

        :param api_ids: The api_ids of this ApiAuthCreate.
        :type api_ids: list[str]
        """
        self._api_ids = api_ids

    @property
    def auth_tunnel(self):
        """Gets the auth_tunnel of this ApiAuthCreate.

        授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  实例开启green_tunnel特性时可以开启绿色通道，此字段不填默认为不使用绿色通道

        :return: The auth_tunnel of this ApiAuthCreate.
        :rtype: str
        """
        return self._auth_tunnel

    @auth_tunnel.setter
    def auth_tunnel(self, auth_tunnel):
        """Sets the auth_tunnel of this ApiAuthCreate.

        授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  实例开启green_tunnel特性时可以开启绿色通道，此字段不填默认为不使用绿色通道

        :param auth_tunnel: The auth_tunnel of this ApiAuthCreate.
        :type auth_tunnel: str
        """
        self._auth_tunnel = auth_tunnel

    @property
    def auth_whitelist(self):
        """Gets the auth_whitelist of this ApiAuthCreate.

        绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问，auth_tunnel = GREEN时生效

        :return: The auth_whitelist of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._auth_whitelist

    @auth_whitelist.setter
    def auth_whitelist(self, auth_whitelist):
        """Sets the auth_whitelist of this ApiAuthCreate.

        绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问，auth_tunnel = GREEN时生效

        :param auth_whitelist: The auth_whitelist of this ApiAuthCreate.
        :type auth_whitelist: list[str]
        """
        self._auth_whitelist = auth_whitelist

    @property
    def auth_blacklist(self):
        """Gets the auth_blacklist of this ApiAuthCreate.

        绿色通道授权黑名单。  auth_tunnel = GREEN时生效

        :return: The auth_blacklist of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._auth_blacklist

    @auth_blacklist.setter
    def auth_blacklist(self, auth_blacklist):
        """Sets the auth_blacklist of this ApiAuthCreate.

        绿色通道授权黑名单。  auth_tunnel = GREEN时生效

        :param auth_blacklist: The auth_blacklist of this ApiAuthCreate.
        :type auth_blacklist: list[str]
        """
        self._auth_blacklist = auth_blacklist

    @property
    def visit_params(self):
        """Gets the visit_params of this ApiAuthCreate.

        访问参数列表。

        :return: The visit_params of this ApiAuthCreate.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ApiAuthVisitParam`]
        """
        return self._visit_params

    @visit_params.setter
    def visit_params(self, visit_params):
        """Sets the visit_params of this ApiAuthCreate.

        访问参数列表。

        :param visit_params: The visit_params of this ApiAuthCreate.
        :type visit_params: list[:class:`huaweicloudsdkroma.v2.ApiAuthVisitParam`]
        """
        self._visit_params = visit_params

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
        if not isinstance(other, ApiAuthCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
