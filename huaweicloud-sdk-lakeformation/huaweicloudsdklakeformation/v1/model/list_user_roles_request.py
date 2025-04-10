# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserRolesRequest:

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
        'role_pattern': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'user_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'role_pattern': 'role_pattern',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'user_name': 'user_name'
    }

    def __init__(self, instance_id=None, role_pattern=None, limit=None, marker=None, reverse_page=None, user_name=None):
        r"""ListUserRolesRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param role_pattern: 模糊匹配角色名称。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。
        :type role_pattern: str
        :param limit: 查询返回条数。默认值为100。最小值为1，最大值为1000。
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0，最大长度为1024。
        :type marker: str
        :param reverse_page: 是否查询上一页。默认为false。
        :type reverse_page: bool
        :param user_name: 用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。
        :type user_name: str
        """
        
        

        self._instance_id = None
        self._role_pattern = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._user_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if role_pattern is not None:
            self.role_pattern = role_pattern
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page
        self.user_name = user_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListUserRolesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListUserRolesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListUserRolesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListUserRolesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def role_pattern(self):
        r"""Gets the role_pattern of this ListUserRolesRequest.

        模糊匹配角色名称。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。

        :return: The role_pattern of this ListUserRolesRequest.
        :rtype: str
        """
        return self._role_pattern

    @role_pattern.setter
    def role_pattern(self, role_pattern):
        r"""Sets the role_pattern of this ListUserRolesRequest.

        模糊匹配角色名称。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。

        :param role_pattern: The role_pattern of this ListUserRolesRequest.
        :type role_pattern: str
        """
        self._role_pattern = role_pattern

    @property
    def limit(self):
        r"""Gets the limit of this ListUserRolesRequest.

        查询返回条数。默认值为100。最小值为1，最大值为1000。

        :return: The limit of this ListUserRolesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserRolesRequest.

        查询返回条数。默认值为100。最小值为1，最大值为1000。

        :param limit: The limit of this ListUserRolesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListUserRolesRequest.

        查询的起始记录ID。最小长度为0，最大长度为1024。

        :return: The marker of this ListUserRolesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListUserRolesRequest.

        查询的起始记录ID。最小长度为0，最大长度为1024。

        :param marker: The marker of this ListUserRolesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        r"""Gets the reverse_page of this ListUserRolesRequest.

        是否查询上一页。默认为false。

        :return: The reverse_page of this ListUserRolesRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        r"""Sets the reverse_page of this ListUserRolesRequest.

        是否查询上一页。默认为false。

        :param reverse_page: The reverse_page of this ListUserRolesRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def user_name(self):
        r"""Gets the user_name of this ListUserRolesRequest.

        用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。

        :return: The user_name of this ListUserRolesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListUserRolesRequest.

        用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。

        :param user_name: The user_name of this ListUserRolesRequest.
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
        if not isinstance(other, ListUserRolesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
