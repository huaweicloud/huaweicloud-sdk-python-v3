# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerGroupsRequest:

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
        'server_group_name': 'str',
        'server_group_id': 'str',
        'app_type': 'str',
        'tags': 'str',
        'enterprise_project_id': 'str',
        'is_secondary_server_group': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_group_name': 'server_group_name',
        'server_group_id': 'server_group_id',
        'app_type': 'app_type',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'is_secondary_server_group': 'is_secondary_server_group'
    }

    def __init__(self, offset=None, limit=None, server_group_name=None, server_group_id=None, app_type=None, tags=None, enterprise_project_id=None, is_secondary_server_group=None):
        """ListServerGroupsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]。
        :type limit: int
        :param server_group_name: 服务器组名称。
        :type server_group_name: str
        :param server_group_id: 服务器组唯一标识。
        :type server_group_id: str
        :param app_type: 应用组类型： * &#x60;SESSION_DESKTOP_APP&#x60; - 会话桌面app * &#x60;COMMON_APP&#x60; - 普通app
        :type app_type: str
        :param tags: 查询tag字段中包含该值的服务器组。
        :type tags: str
        :param enterprise_project_id: 企业项目ID(字段为空或者0表示使用默认default企业项目)
        :type enterprise_project_id: str
        :param is_secondary_server_group: 是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。
        :type is_secondary_server_group: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_group_name = None
        self._server_group_id = None
        self._app_type = None
        self._tags = None
        self._enterprise_project_id = None
        self._is_secondary_server_group = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if app_type is not None:
            self.app_type = app_type
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_secondary_server_group is not None:
            self.is_secondary_server_group = is_secondary_server_group

    @property
    def offset(self):
        """Gets the offset of this ListServerGroupsRequest.

        查询的偏移量。

        :return: The offset of this ListServerGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServerGroupsRequest.

        查询的偏移量。

        :param offset: The offset of this ListServerGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListServerGroupsRequest.

        查询的数量，值区间[1-100]。

        :return: The limit of this ListServerGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServerGroupsRequest.

        查询的数量，值区间[1-100]。

        :param limit: The limit of this ListServerGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_group_name(self):
        """Gets the server_group_name of this ListServerGroupsRequest.

        服务器组名称。

        :return: The server_group_name of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this ListServerGroupsRequest.

        服务器组名称。

        :param server_group_name: The server_group_name of this ListServerGroupsRequest.
        :type server_group_name: str
        """
        self._server_group_name = server_group_name

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ListServerGroupsRequest.

        服务器组唯一标识。

        :return: The server_group_id of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ListServerGroupsRequest.

        服务器组唯一标识。

        :param server_group_id: The server_group_id of this ListServerGroupsRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def app_type(self):
        """Gets the app_type of this ListServerGroupsRequest.

        应用组类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :return: The app_type of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListServerGroupsRequest.

        应用组类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :param app_type: The app_type of this ListServerGroupsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def tags(self):
        """Gets the tags of this ListServerGroupsRequest.

        查询tag字段中包含该值的服务器组。

        :return: The tags of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListServerGroupsRequest.

        查询tag字段中包含该值的服务器组。

        :param tags: The tags of this ListServerGroupsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListServerGroupsRequest.

        企业项目ID(字段为空或者0表示使用默认default企业项目)

        :return: The enterprise_project_id of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListServerGroupsRequest.

        企业项目ID(字段为空或者0表示使用默认default企业项目)

        :param enterprise_project_id: The enterprise_project_id of this ListServerGroupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_secondary_server_group(self):
        """Gets the is_secondary_server_group of this ListServerGroupsRequest.

        是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。

        :return: The is_secondary_server_group of this ListServerGroupsRequest.
        :rtype: str
        """
        return self._is_secondary_server_group

    @is_secondary_server_group.setter
    def is_secondary_server_group(self, is_secondary_server_group):
        """Sets the is_secondary_server_group of this ListServerGroupsRequest.

        是否为备服务器组，不传默认查所有： true : 是备服务器组。 false: 主服务器组，默认。

        :param is_secondary_server_group: The is_secondary_server_group of this ListServerGroupsRequest.
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
        if not isinstance(other, ListServerGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
