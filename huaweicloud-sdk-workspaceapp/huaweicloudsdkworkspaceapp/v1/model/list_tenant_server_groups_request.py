# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantServerGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sever_group_name': 'str',
        'app_type': 'str',
        'is_secondary_server_group': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sever_group_name': 'sever_group_name',
        'app_type': 'app_type',
        'is_secondary_server_group': 'is_secondary_server_group'
    }

    def __init__(self, offset=None, limit=None, sever_group_name=None, app_type=None, is_secondary_server_group=None):
        r"""ListTenantServerGroupsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]，默认值10。
        :type limit: int
        :param sever_group_name: 服务器组名称。
        :type sever_group_name: str
        :param app_type: 应用组类型： * &#x60;SESSION_DESKTOP_APP&#x60; - 会话桌面app * &#x60;COMMON_APP&#x60; - 普通app
        :type app_type: str
        :param is_secondary_server_group: 是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。
        :type is_secondary_server_group: str
        """
        
        

        self._offset = None
        self._limit = None
        self._sever_group_name = None
        self._app_type = None
        self._is_secondary_server_group = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sever_group_name is not None:
            self.sever_group_name = sever_group_name
        if app_type is not None:
            self.app_type = app_type
        if is_secondary_server_group is not None:
            self.is_secondary_server_group = is_secondary_server_group

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantServerGroupsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListTenantServerGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantServerGroupsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListTenantServerGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantServerGroupsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :return: The limit of this ListTenantServerGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantServerGroupsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :param limit: The limit of this ListTenantServerGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sever_group_name(self):
        r"""Gets the sever_group_name of this ListTenantServerGroupsRequest.

        服务器组名称。

        :return: The sever_group_name of this ListTenantServerGroupsRequest.
        :rtype: str
        """
        return self._sever_group_name

    @sever_group_name.setter
    def sever_group_name(self, sever_group_name):
        r"""Sets the sever_group_name of this ListTenantServerGroupsRequest.

        服务器组名称。

        :param sever_group_name: The sever_group_name of this ListTenantServerGroupsRequest.
        :type sever_group_name: str
        """
        self._sever_group_name = sever_group_name

    @property
    def app_type(self):
        r"""Gets the app_type of this ListTenantServerGroupsRequest.

        应用组类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :return: The app_type of this ListTenantServerGroupsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListTenantServerGroupsRequest.

        应用组类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :param app_type: The app_type of this ListTenantServerGroupsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def is_secondary_server_group(self):
        r"""Gets the is_secondary_server_group of this ListTenantServerGroupsRequest.

        是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。

        :return: The is_secondary_server_group of this ListTenantServerGroupsRequest.
        :rtype: str
        """
        return self._is_secondary_server_group

    @is_secondary_server_group.setter
    def is_secondary_server_group(self, is_secondary_server_group):
        r"""Sets the is_secondary_server_group of this ListTenantServerGroupsRequest.

        是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。

        :param is_secondary_server_group: The is_secondary_server_group of this ListTenantServerGroupsRequest.
        :type is_secondary_server_group: str
        """
        self._is_secondary_server_group = is_secondary_server_group

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
        if not isinstance(other, ListTenantServerGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
