# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRomaAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'favorite': 'bool',
        'auth_role': 'str',
        'name': 'str',
        'owner': 'bool',
        'user_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'favorite': 'favorite',
        'auth_role': 'auth_role',
        'name': 'name',
        'owner': 'owner',
        'user_name': 'user_name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, favorite=None, auth_role=None, name=None, owner=None, user_name=None):
        """ListRomaAppRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param favorite: 查询收藏的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，获取收藏的应用 - 为false时，获取未被收藏的应用
        :type favorite: bool
        :param auth_role: 获取拥有指定权限应用
        :type auth_role: str
        :param name: 应用名称，模糊匹配
        :type name: str
        :param owner: 查询有权限访问的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，查询当前用户创建的应用 - 为false时，查询非当前用户创建的有权限的应用，比如其它人共享的应用
        :type owner: bool
        :param user_name: 从当前调用者有权限的所有应用中过滤出指定用户名有权限的应用
        :type user_name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._favorite = None
        self._auth_role = None
        self._name = None
        self._owner = None
        self._user_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if favorite is not None:
            self.favorite = favorite
        if auth_role is not None:
            self.auth_role = auth_role
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if user_name is not None:
            self.user_name = user_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRomaAppRequest.

        实例ID

        :return: The instance_id of this ListRomaAppRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRomaAppRequest.

        实例ID

        :param instance_id: The instance_id of this ListRomaAppRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListRomaAppRequest.

        偏移量，大于等于0

        :return: The offset of this ListRomaAppRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRomaAppRequest.

        偏移量，大于等于0

        :param offset: The offset of this ListRomaAppRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRomaAppRequest.

        每页显示的条目数量

        :return: The limit of this ListRomaAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRomaAppRequest.

        每页显示的条目数量

        :param limit: The limit of this ListRomaAppRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def favorite(self):
        """Gets the favorite of this ListRomaAppRequest.

        查询收藏的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，获取收藏的应用 - 为false时，获取未被收藏的应用

        :return: The favorite of this ListRomaAppRequest.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this ListRomaAppRequest.

        查询收藏的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，获取收藏的应用 - 为false时，获取未被收藏的应用

        :param favorite: The favorite of this ListRomaAppRequest.
        :type favorite: bool
        """
        self._favorite = favorite

    @property
    def auth_role(self):
        """Gets the auth_role of this ListRomaAppRequest.

        获取拥有指定权限应用

        :return: The auth_role of this ListRomaAppRequest.
        :rtype: str
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        """Sets the auth_role of this ListRomaAppRequest.

        获取拥有指定权限应用

        :param auth_role: The auth_role of this ListRomaAppRequest.
        :type auth_role: str
        """
        self._auth_role = auth_role

    @property
    def name(self):
        """Gets the name of this ListRomaAppRequest.

        应用名称，模糊匹配

        :return: The name of this ListRomaAppRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRomaAppRequest.

        应用名称，模糊匹配

        :param name: The name of this ListRomaAppRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ListRomaAppRequest.

        查询有权限访问的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，查询当前用户创建的应用 - 为false时，查询非当前用户创建的有权限的应用，比如其它人共享的应用

        :return: The owner of this ListRomaAppRequest.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListRomaAppRequest.

        查询有权限访问的应用 - 未提供时，查询当前用户有权限的所有应用 - 为true时，查询当前用户创建的应用 - 为false时，查询非当前用户创建的有权限的应用，比如其它人共享的应用

        :param owner: The owner of this ListRomaAppRequest.
        :type owner: bool
        """
        self._owner = owner

    @property
    def user_name(self):
        """Gets the user_name of this ListRomaAppRequest.

        从当前调用者有权限的所有应用中过滤出指定用户名有权限的应用

        :return: The user_name of this ListRomaAppRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListRomaAppRequest.

        从当前调用者有权限的所有应用中过滤出指定用户名有权限的应用

        :param user_name: The user_name of this ListRomaAppRequest.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ListRomaAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
