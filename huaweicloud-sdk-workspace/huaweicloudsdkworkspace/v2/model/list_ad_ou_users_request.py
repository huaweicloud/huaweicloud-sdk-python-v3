# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAdOuUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ou_dn': 'str',
        'user_name': 'str',
        'has_existed': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'ou_dn': 'ou_dn',
        'user_name': 'user_name',
        'has_existed': 'has_existed',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, ou_dn=None, user_name=None, has_existed=None, limit=None, offset=None):
        r"""ListAdOuUsersRequest

        The model defined in huaweicloud sdk

        :param ou_dn: OU的域名地址。
        :type ou_dn: str
        :param user_name: 用户名，支持模糊查询。
        :type user_name: str
        :param has_existed: 用户是否已存在。
        :type has_existed: bool
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._ou_dn = None
        self._user_name = None
        self._has_existed = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.ou_dn = ou_dn
        if user_name is not None:
            self.user_name = user_name
        if has_existed is not None:
            self.has_existed = has_existed
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def ou_dn(self):
        r"""Gets the ou_dn of this ListAdOuUsersRequest.

        OU的域名地址。

        :return: The ou_dn of this ListAdOuUsersRequest.
        :rtype: str
        """
        return self._ou_dn

    @ou_dn.setter
    def ou_dn(self, ou_dn):
        r"""Sets the ou_dn of this ListAdOuUsersRequest.

        OU的域名地址。

        :param ou_dn: The ou_dn of this ListAdOuUsersRequest.
        :type ou_dn: str
        """
        self._ou_dn = ou_dn

    @property
    def user_name(self):
        r"""Gets the user_name of this ListAdOuUsersRequest.

        用户名，支持模糊查询。

        :return: The user_name of this ListAdOuUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListAdOuUsersRequest.

        用户名，支持模糊查询。

        :param user_name: The user_name of this ListAdOuUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def has_existed(self):
        r"""Gets the has_existed of this ListAdOuUsersRequest.

        用户是否已存在。

        :return: The has_existed of this ListAdOuUsersRequest.
        :rtype: bool
        """
        return self._has_existed

    @has_existed.setter
    def has_existed(self, has_existed):
        r"""Sets the has_existed of this ListAdOuUsersRequest.

        用户是否已存在。

        :param has_existed: The has_existed of this ListAdOuUsersRequest.
        :type has_existed: bool
        """
        self._has_existed = has_existed

    @property
    def limit(self):
        r"""Gets the limit of this ListAdOuUsersRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。

        :return: The limit of this ListAdOuUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAdOuUsersRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的桌面。

        :param limit: The limit of this ListAdOuUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAdOuUsersRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListAdOuUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAdOuUsersRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListAdOuUsersRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAdOuUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
