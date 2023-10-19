# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersRequest:

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
        'user_source': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'user_name_pattern': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user_source': 'user_source',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'user_name_pattern': 'user_name_pattern'
    }

    def __init__(self, instance_id=None, user_source=None, limit=None, marker=None, reverse_page=None, user_name_pattern=None):
        """ListUsersRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param user_source: 查询的用户来源。只能为IAM或SAML或LDAP或LOCAL或AGENTTENANT或OTHER。默认为IAM。
        :type user_source: str
        :param limit: 查询返回条数。默认值为1000。最小值为1，最大值为2000。
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0，最大长度为256。
        :type marker: str
        :param reverse_page: 是否查询上一页。默认为false。
        :type reverse_page: bool
        :param user_name_pattern: 用户模糊查询。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。
        :type user_name_pattern: str
        """
        
        

        self._instance_id = None
        self._user_source = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._user_name_pattern = None
        self.discriminator = None

        self.instance_id = instance_id
        if user_source is not None:
            self.user_source = user_source
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page
        if user_name_pattern is not None:
            self.user_name_pattern = user_name_pattern

    @property
    def instance_id(self):
        """Gets the instance_id of this ListUsersRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListUsersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListUsersRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListUsersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_source(self):
        """Gets the user_source of this ListUsersRequest.

        查询的用户来源。只能为IAM或SAML或LDAP或LOCAL或AGENTTENANT或OTHER。默认为IAM。

        :return: The user_source of this ListUsersRequest.
        :rtype: str
        """
        return self._user_source

    @user_source.setter
    def user_source(self, user_source):
        """Sets the user_source of this ListUsersRequest.

        查询的用户来源。只能为IAM或SAML或LDAP或LOCAL或AGENTTENANT或OTHER。默认为IAM。

        :param user_source: The user_source of this ListUsersRequest.
        :type user_source: str
        """
        self._user_source = user_source

    @property
    def limit(self):
        """Gets the limit of this ListUsersRequest.

        查询返回条数。默认值为1000。最小值为1，最大值为2000。

        :return: The limit of this ListUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsersRequest.

        查询返回条数。默认值为1000。最小值为1，最大值为2000。

        :param limit: The limit of this ListUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListUsersRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :return: The marker of this ListUsersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListUsersRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :param marker: The marker of this ListUsersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        """Gets the reverse_page of this ListUsersRequest.

        是否查询上一页。默认为false。

        :return: The reverse_page of this ListUsersRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        """Sets the reverse_page of this ListUsersRequest.

        是否查询上一页。默认为false。

        :param reverse_page: The reverse_page of this ListUsersRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def user_name_pattern(self):
        """Gets the user_name_pattern of this ListUsersRequest.

        用户模糊查询。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。

        :return: The user_name_pattern of this ListUsersRequest.
        :rtype: str
        """
        return self._user_name_pattern

    @user_name_pattern.setter
    def user_name_pattern(self, user_name_pattern):
        """Sets the user_name_pattern of this ListUsersRequest.

        用户模糊查询。只能包含字母、数字和_|*.特殊字符，且长度为1~255个字符。

        :param user_name_pattern: The user_name_pattern of this ListUsersRequest.
        :type user_name_pattern: str
        """
        self._user_name_pattern = user_name_pattern

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
        if not isinstance(other, ListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
