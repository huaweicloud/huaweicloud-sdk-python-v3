# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthRelations:

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
        'auth_result': 'AuthResult',
        'auth_time': 'datetime',
        'id': 'str',
        'app_id': 'str',
        'auth_role': 'str',
        'auth_tunnel': 'str',
        'auth_whitelist': 'list[str]',
        'auth_blacklist': 'list[str]',
        'visit_params': 'str'
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
        'auth_blacklist': 'auth_blacklist',
        'visit_params': 'visit_params'
    }

    def __init__(self, api_id=None, auth_result=None, auth_time=None, id=None, app_id=None, auth_role=None, auth_tunnel=None, auth_whitelist=None, auth_blacklist=None, visit_params=None):
        r"""ApiAuthRelations

        The model defined in huaweicloud sdk

        :param api_id: API编号
        :type api_id: str
        :param auth_result: 
        :type auth_result: :class:`huaweicloudsdkroma.v2.AuthResult`
        :param auth_time: 授权时间
        :type auth_time: datetime
        :param id: 授权关系编号
        :type id: str
        :param app_id: APP编号
        :type app_id: str
        :param auth_role: 授权者 - PROVIDER：API提供者授权 - CONSUMER：API消费者授权
        :type auth_role: str
        :param auth_tunnel: 授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  此字段不填默认为不使用绿色通道
        :type auth_tunnel: str
        :param auth_whitelist: 绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问
        :type auth_whitelist: list[str]
        :param auth_blacklist: 绿色通道授权黑名单
        :type auth_blacklist: list[str]
        :param visit_params: 访问参数。
        :type visit_params: str
        """
        
        

        self._api_id = None
        self._auth_result = None
        self._auth_time = None
        self._id = None
        self._app_id = None
        self._auth_role = None
        self._auth_tunnel = None
        self._auth_whitelist = None
        self._auth_blacklist = None
        self._visit_params = None
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
        if visit_params is not None:
            self.visit_params = visit_params

    @property
    def api_id(self):
        r"""Gets the api_id of this ApiAuthRelations.

        API编号

        :return: The api_id of this ApiAuthRelations.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ApiAuthRelations.

        API编号

        :param api_id: The api_id of this ApiAuthRelations.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def auth_result(self):
        r"""Gets the auth_result of this ApiAuthRelations.

        :return: The auth_result of this ApiAuthRelations.
        :rtype: :class:`huaweicloudsdkroma.v2.AuthResult`
        """
        return self._auth_result

    @auth_result.setter
    def auth_result(self, auth_result):
        r"""Sets the auth_result of this ApiAuthRelations.

        :param auth_result: The auth_result of this ApiAuthRelations.
        :type auth_result: :class:`huaweicloudsdkroma.v2.AuthResult`
        """
        self._auth_result = auth_result

    @property
    def auth_time(self):
        r"""Gets the auth_time of this ApiAuthRelations.

        授权时间

        :return: The auth_time of this ApiAuthRelations.
        :rtype: datetime
        """
        return self._auth_time

    @auth_time.setter
    def auth_time(self, auth_time):
        r"""Sets the auth_time of this ApiAuthRelations.

        授权时间

        :param auth_time: The auth_time of this ApiAuthRelations.
        :type auth_time: datetime
        """
        self._auth_time = auth_time

    @property
    def id(self):
        r"""Gets the id of this ApiAuthRelations.

        授权关系编号

        :return: The id of this ApiAuthRelations.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApiAuthRelations.

        授权关系编号

        :param id: The id of this ApiAuthRelations.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        r"""Gets the app_id of this ApiAuthRelations.

        APP编号

        :return: The app_id of this ApiAuthRelations.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ApiAuthRelations.

        APP编号

        :param app_id: The app_id of this ApiAuthRelations.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def auth_role(self):
        r"""Gets the auth_role of this ApiAuthRelations.

        授权者 - PROVIDER：API提供者授权 - CONSUMER：API消费者授权

        :return: The auth_role of this ApiAuthRelations.
        :rtype: str
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        r"""Sets the auth_role of this ApiAuthRelations.

        授权者 - PROVIDER：API提供者授权 - CONSUMER：API消费者授权

        :param auth_role: The auth_role of this ApiAuthRelations.
        :type auth_role: str
        """
        self._auth_role = auth_role

    @property
    def auth_tunnel(self):
        r"""Gets the auth_tunnel of this ApiAuthRelations.

        授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  此字段不填默认为不使用绿色通道

        :return: The auth_tunnel of this ApiAuthRelations.
        :rtype: str
        """
        return self._auth_tunnel

    @auth_tunnel.setter
    def auth_tunnel(self, auth_tunnel):
        r"""Sets the auth_tunnel of this ApiAuthRelations.

        授权通道类型： - GREEN：绿色通道 - NORMAL：非绿色通道  此字段不填默认为不使用绿色通道

        :param auth_tunnel: The auth_tunnel of this ApiAuthRelations.
        :type auth_tunnel: str
        """
        self._auth_tunnel = auth_tunnel

    @property
    def auth_whitelist(self):
        r"""Gets the auth_whitelist of this ApiAuthRelations.

        绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问

        :return: The auth_whitelist of this ApiAuthRelations.
        :rtype: list[str]
        """
        return self._auth_whitelist

    @auth_whitelist.setter
    def auth_whitelist(self, auth_whitelist):
        r"""Sets the auth_whitelist of this ApiAuthRelations.

        绿色通道授权白名单。  允许白名单中的IP不使用认证信息访问

        :param auth_whitelist: The auth_whitelist of this ApiAuthRelations.
        :type auth_whitelist: list[str]
        """
        self._auth_whitelist = auth_whitelist

    @property
    def auth_blacklist(self):
        r"""Gets the auth_blacklist of this ApiAuthRelations.

        绿色通道授权黑名单

        :return: The auth_blacklist of this ApiAuthRelations.
        :rtype: list[str]
        """
        return self._auth_blacklist

    @auth_blacklist.setter
    def auth_blacklist(self, auth_blacklist):
        r"""Sets the auth_blacklist of this ApiAuthRelations.

        绿色通道授权黑名单

        :param auth_blacklist: The auth_blacklist of this ApiAuthRelations.
        :type auth_blacklist: list[str]
        """
        self._auth_blacklist = auth_blacklist

    @property
    def visit_params(self):
        r"""Gets the visit_params of this ApiAuthRelations.

        访问参数。

        :return: The visit_params of this ApiAuthRelations.
        :rtype: str
        """
        return self._visit_params

    @visit_params.setter
    def visit_params(self, visit_params):
        r"""Sets the visit_params of this ApiAuthRelations.

        访问参数。

        :param visit_params: The visit_params of this ApiAuthRelations.
        :type visit_params: str
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
        if not isinstance(other, ApiAuthRelations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
