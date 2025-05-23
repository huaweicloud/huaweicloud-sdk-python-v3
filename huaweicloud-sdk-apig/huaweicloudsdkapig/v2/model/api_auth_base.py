# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthBase:

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
        'api_id': 'str',
        'api_name': 'str',
        'group_name': 'str',
        'api_type': 'int',
        'api_remark': 'str',
        'env_id': 'str',
        'auth_role': 'str',
        'auth_time': 'datetime',
        'app_name': 'str',
        'app_remark': 'str',
        'app_type': 'str',
        'app_creator': 'str',
        'publish_id': 'str',
        'group_id': 'str',
        'auth_tunnel': 'str',
        'auth_whitelist': 'list[str]',
        'auth_blacklist': 'list[str]',
        'visit_param': 'str',
        'roma_app_type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'group_name': 'group_name',
        'api_type': 'api_type',
        'api_remark': 'api_remark',
        'env_id': 'env_id',
        'auth_role': 'auth_role',
        'auth_time': 'auth_time',
        'app_name': 'app_name',
        'app_remark': 'app_remark',
        'app_type': 'app_type',
        'app_creator': 'app_creator',
        'publish_id': 'publish_id',
        'group_id': 'group_id',
        'auth_tunnel': 'auth_tunnel',
        'auth_whitelist': 'auth_whitelist',
        'auth_blacklist': 'auth_blacklist',
        'visit_param': 'visit_param',
        'roma_app_type': 'roma_app_type',
        'tags': 'tags'
    }

    def __init__(self, id=None, api_id=None, api_name=None, group_name=None, api_type=None, api_remark=None, env_id=None, auth_role=None, auth_time=None, app_name=None, app_remark=None, app_type=None, app_creator=None, publish_id=None, group_id=None, auth_tunnel=None, auth_whitelist=None, auth_blacklist=None, visit_param=None, roma_app_type=None, tags=None):
        r"""ApiAuthBase

        The model defined in huaweicloud sdk

        :param id: 授权关系编号
        :type id: str
        :param api_id: API的编号
        :type api_id: str
        :param api_name: API的名称
        :type api_name: str
        :param group_name: API绑定的分组名称
        :type group_name: str
        :param api_type: API类型
        :type api_type: int
        :param api_remark: API的描述信息
        :type api_remark: str
        :param env_id: api授权绑定的环境ID
        :type env_id: str
        :param auth_role: 授权者
        :type auth_role: str
        :param auth_time: 授权创建的时间
        :type auth_time: datetime
        :param app_name: APP的名称
        :type app_name: str
        :param app_remark: APP的描述
        :type app_remark: str
        :param app_type: APP的类型：  默认为apig，暂不支持其他类型
        :type app_type: str
        :param app_creator: APP的创建者，取值如下： - USER：租户自己创建 - MARKET：API市场分配，暂不支持
        :type app_creator: str
        :param publish_id: API的发布编号
        :type publish_id: str
        :param group_id: API绑定的分组ID
        :type group_id: str
        :param auth_tunnel: 授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL
        :type auth_tunnel: str
        :param auth_whitelist: 绿色通道的白名单配置
        :type auth_whitelist: list[str]
        :param auth_blacklist: 绿色通道的黑名单配置
        :type auth_blacklist: list[str]
        :param visit_param: 访问参数。
        :type visit_param: str
        :param roma_app_type: ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用  暂不支持
        :type roma_app_type: str
        :param tags: API绑定的标签，标签配额默认10条，可以联系技术调整。
        :type tags: list[str]
        """
        
        

        self._id = None
        self._api_id = None
        self._api_name = None
        self._group_name = None
        self._api_type = None
        self._api_remark = None
        self._env_id = None
        self._auth_role = None
        self._auth_time = None
        self._app_name = None
        self._app_remark = None
        self._app_type = None
        self._app_creator = None
        self._publish_id = None
        self._group_id = None
        self._auth_tunnel = None
        self._auth_whitelist = None
        self._auth_blacklist = None
        self._visit_param = None
        self._roma_app_type = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if group_name is not None:
            self.group_name = group_name
        if api_type is not None:
            self.api_type = api_type
        if api_remark is not None:
            self.api_remark = api_remark
        if env_id is not None:
            self.env_id = env_id
        if auth_role is not None:
            self.auth_role = auth_role
        if auth_time is not None:
            self.auth_time = auth_time
        if app_name is not None:
            self.app_name = app_name
        if app_remark is not None:
            self.app_remark = app_remark
        if app_type is not None:
            self.app_type = app_type
        if app_creator is not None:
            self.app_creator = app_creator
        if publish_id is not None:
            self.publish_id = publish_id
        if group_id is not None:
            self.group_id = group_id
        if auth_tunnel is not None:
            self.auth_tunnel = auth_tunnel
        if auth_whitelist is not None:
            self.auth_whitelist = auth_whitelist
        if auth_blacklist is not None:
            self.auth_blacklist = auth_blacklist
        if visit_param is not None:
            self.visit_param = visit_param
        if roma_app_type is not None:
            self.roma_app_type = roma_app_type
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this ApiAuthBase.

        授权关系编号

        :return: The id of this ApiAuthBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApiAuthBase.

        授权关系编号

        :param id: The id of this ApiAuthBase.
        :type id: str
        """
        self._id = id

    @property
    def api_id(self):
        r"""Gets the api_id of this ApiAuthBase.

        API的编号

        :return: The api_id of this ApiAuthBase.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ApiAuthBase.

        API的编号

        :param api_id: The api_id of this ApiAuthBase.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        r"""Gets the api_name of this ApiAuthBase.

        API的名称

        :return: The api_name of this ApiAuthBase.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this ApiAuthBase.

        API的名称

        :param api_name: The api_name of this ApiAuthBase.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def group_name(self):
        r"""Gets the group_name of this ApiAuthBase.

        API绑定的分组名称

        :return: The group_name of this ApiAuthBase.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ApiAuthBase.

        API绑定的分组名称

        :param group_name: The group_name of this ApiAuthBase.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def api_type(self):
        r"""Gets the api_type of this ApiAuthBase.

        API类型

        :return: The api_type of this ApiAuthBase.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this ApiAuthBase.

        API类型

        :param api_type: The api_type of this ApiAuthBase.
        :type api_type: int
        """
        self._api_type = api_type

    @property
    def api_remark(self):
        r"""Gets the api_remark of this ApiAuthBase.

        API的描述信息

        :return: The api_remark of this ApiAuthBase.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        r"""Sets the api_remark of this ApiAuthBase.

        API的描述信息

        :param api_remark: The api_remark of this ApiAuthBase.
        :type api_remark: str
        """
        self._api_remark = api_remark

    @property
    def env_id(self):
        r"""Gets the env_id of this ApiAuthBase.

        api授权绑定的环境ID

        :return: The env_id of this ApiAuthBase.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ApiAuthBase.

        api授权绑定的环境ID

        :param env_id: The env_id of this ApiAuthBase.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def auth_role(self):
        r"""Gets the auth_role of this ApiAuthBase.

        授权者

        :return: The auth_role of this ApiAuthBase.
        :rtype: str
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        r"""Sets the auth_role of this ApiAuthBase.

        授权者

        :param auth_role: The auth_role of this ApiAuthBase.
        :type auth_role: str
        """
        self._auth_role = auth_role

    @property
    def auth_time(self):
        r"""Gets the auth_time of this ApiAuthBase.

        授权创建的时间

        :return: The auth_time of this ApiAuthBase.
        :rtype: datetime
        """
        return self._auth_time

    @auth_time.setter
    def auth_time(self, auth_time):
        r"""Sets the auth_time of this ApiAuthBase.

        授权创建的时间

        :param auth_time: The auth_time of this ApiAuthBase.
        :type auth_time: datetime
        """
        self._auth_time = auth_time

    @property
    def app_name(self):
        r"""Gets the app_name of this ApiAuthBase.

        APP的名称

        :return: The app_name of this ApiAuthBase.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ApiAuthBase.

        APP的名称

        :param app_name: The app_name of this ApiAuthBase.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_remark(self):
        r"""Gets the app_remark of this ApiAuthBase.

        APP的描述

        :return: The app_remark of this ApiAuthBase.
        :rtype: str
        """
        return self._app_remark

    @app_remark.setter
    def app_remark(self, app_remark):
        r"""Sets the app_remark of this ApiAuthBase.

        APP的描述

        :param app_remark: The app_remark of this ApiAuthBase.
        :type app_remark: str
        """
        self._app_remark = app_remark

    @property
    def app_type(self):
        r"""Gets the app_type of this ApiAuthBase.

        APP的类型：  默认为apig，暂不支持其他类型

        :return: The app_type of this ApiAuthBase.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ApiAuthBase.

        APP的类型：  默认为apig，暂不支持其他类型

        :param app_type: The app_type of this ApiAuthBase.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_creator(self):
        r"""Gets the app_creator of this ApiAuthBase.

        APP的创建者，取值如下： - USER：租户自己创建 - MARKET：API市场分配，暂不支持

        :return: The app_creator of this ApiAuthBase.
        :rtype: str
        """
        return self._app_creator

    @app_creator.setter
    def app_creator(self, app_creator):
        r"""Sets the app_creator of this ApiAuthBase.

        APP的创建者，取值如下： - USER：租户自己创建 - MARKET：API市场分配，暂不支持

        :param app_creator: The app_creator of this ApiAuthBase.
        :type app_creator: str
        """
        self._app_creator = app_creator

    @property
    def publish_id(self):
        r"""Gets the publish_id of this ApiAuthBase.

        API的发布编号

        :return: The publish_id of this ApiAuthBase.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        r"""Sets the publish_id of this ApiAuthBase.

        API的发布编号

        :param publish_id: The publish_id of this ApiAuthBase.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ApiAuthBase.

        API绑定的分组ID

        :return: The group_id of this ApiAuthBase.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ApiAuthBase.

        API绑定的分组ID

        :param group_id: The group_id of this ApiAuthBase.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def auth_tunnel(self):
        r"""Gets the auth_tunnel of this ApiAuthBase.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :return: The auth_tunnel of this ApiAuthBase.
        :rtype: str
        """
        return self._auth_tunnel

    @auth_tunnel.setter
    def auth_tunnel(self, auth_tunnel):
        r"""Sets the auth_tunnel of this ApiAuthBase.

        授权通道类型 - NORMAL：普通通道 - GREEN：绿色通道  暂不支持，默认NORMAL

        :param auth_tunnel: The auth_tunnel of this ApiAuthBase.
        :type auth_tunnel: str
        """
        self._auth_tunnel = auth_tunnel

    @property
    def auth_whitelist(self):
        r"""Gets the auth_whitelist of this ApiAuthBase.

        绿色通道的白名单配置

        :return: The auth_whitelist of this ApiAuthBase.
        :rtype: list[str]
        """
        return self._auth_whitelist

    @auth_whitelist.setter
    def auth_whitelist(self, auth_whitelist):
        r"""Sets the auth_whitelist of this ApiAuthBase.

        绿色通道的白名单配置

        :param auth_whitelist: The auth_whitelist of this ApiAuthBase.
        :type auth_whitelist: list[str]
        """
        self._auth_whitelist = auth_whitelist

    @property
    def auth_blacklist(self):
        r"""Gets the auth_blacklist of this ApiAuthBase.

        绿色通道的黑名单配置

        :return: The auth_blacklist of this ApiAuthBase.
        :rtype: list[str]
        """
        return self._auth_blacklist

    @auth_blacklist.setter
    def auth_blacklist(self, auth_blacklist):
        r"""Sets the auth_blacklist of this ApiAuthBase.

        绿色通道的黑名单配置

        :param auth_blacklist: The auth_blacklist of this ApiAuthBase.
        :type auth_blacklist: list[str]
        """
        self._auth_blacklist = auth_blacklist

    @property
    def visit_param(self):
        r"""Gets the visit_param of this ApiAuthBase.

        访问参数。

        :return: The visit_param of this ApiAuthBase.
        :rtype: str
        """
        return self._visit_param

    @visit_param.setter
    def visit_param(self, visit_param):
        r"""Sets the visit_param of this ApiAuthBase.

        访问参数。

        :param visit_param: The visit_param of this ApiAuthBase.
        :type visit_param: str
        """
        self._visit_param = visit_param

    @property
    def roma_app_type(self):
        r"""Gets the roma_app_type of this ApiAuthBase.

        ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用  暂不支持

        :return: The roma_app_type of this ApiAuthBase.
        :rtype: str
        """
        return self._roma_app_type

    @roma_app_type.setter
    def roma_app_type(self, roma_app_type):
        r"""Sets the roma_app_type of this ApiAuthBase.

        ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用  暂不支持

        :param roma_app_type: The roma_app_type of this ApiAuthBase.
        :type roma_app_type: str
        """
        self._roma_app_type = roma_app_type

    @property
    def tags(self):
        r"""Gets the tags of this ApiAuthBase.

        API绑定的标签，标签配额默认10条，可以联系技术调整。

        :return: The tags of this ApiAuthBase.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ApiAuthBase.

        API绑定的标签，标签配额默认10条，可以联系技术调整。

        :param tags: The tags of this ApiAuthBase.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, ApiAuthBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
