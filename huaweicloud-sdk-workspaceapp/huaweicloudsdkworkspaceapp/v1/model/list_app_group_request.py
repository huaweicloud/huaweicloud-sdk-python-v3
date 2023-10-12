# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'app_server_group_id': 'str',
        'app_group_id': 'str',
        'name': 'str',
        'authorization_type': 'str',
        'app_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'app_server_group_id': 'app_server_group_id',
        'app_group_id': 'app_group_id',
        'name': 'name',
        'authorization_type': 'authorization_type',
        'app_type': 'app_type'
    }

    def __init__(self, limit=None, offset=None, app_server_group_id=None, app_group_id=None, name=None, authorization_type=None, app_type=None):
        """ListAppGroupRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]
        :type limit: int
        :param offset: 查询的偏移量
        :type offset: int
        :param app_server_group_id: 应用服务器组ID
        :type app_server_group_id: str
        :param app_group_id: 应用组ID
        :type app_group_id: str
        :param name: 应用组名称
        :type name: str
        :param authorization_type: 授权类型(APP、APP_GROUP)
        :type authorization_type: str
        :param app_type: 应用组类型(SESSION_DESKTOP_APP、COMMON_APP)
        :type app_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._app_server_group_id = None
        self._app_group_id = None
        self._name = None
        self._authorization_type = None
        self._app_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if app_server_group_id is not None:
            self.app_server_group_id = app_server_group_id
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if name is not None:
            self.name = name
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if app_type is not None:
            self.app_type = app_type

    @property
    def limit(self):
        """Gets the limit of this ListAppGroupRequest.

        单次查询的大小[1-100]

        :return: The limit of this ListAppGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppGroupRequest.

        单次查询的大小[1-100]

        :param limit: The limit of this ListAppGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppGroupRequest.

        查询的偏移量

        :return: The offset of this ListAppGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppGroupRequest.

        查询的偏移量

        :param offset: The offset of this ListAppGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_server_group_id(self):
        """Gets the app_server_group_id of this ListAppGroupRequest.

        应用服务器组ID

        :return: The app_server_group_id of this ListAppGroupRequest.
        :rtype: str
        """
        return self._app_server_group_id

    @app_server_group_id.setter
    def app_server_group_id(self, app_server_group_id):
        """Sets the app_server_group_id of this ListAppGroupRequest.

        应用服务器组ID

        :param app_server_group_id: The app_server_group_id of this ListAppGroupRequest.
        :type app_server_group_id: str
        """
        self._app_server_group_id = app_server_group_id

    @property
    def app_group_id(self):
        """Gets the app_group_id of this ListAppGroupRequest.

        应用组ID

        :return: The app_group_id of this ListAppGroupRequest.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this ListAppGroupRequest.

        应用组ID

        :param app_group_id: The app_group_id of this ListAppGroupRequest.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def name(self):
        """Gets the name of this ListAppGroupRequest.

        应用组名称

        :return: The name of this ListAppGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAppGroupRequest.

        应用组名称

        :param name: The name of this ListAppGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def authorization_type(self):
        """Gets the authorization_type of this ListAppGroupRequest.

        授权类型(APP、APP_GROUP)

        :return: The authorization_type of this ListAppGroupRequest.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this ListAppGroupRequest.

        授权类型(APP、APP_GROUP)

        :param authorization_type: The authorization_type of this ListAppGroupRequest.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def app_type(self):
        """Gets the app_type of this ListAppGroupRequest.

        应用组类型(SESSION_DESKTOP_APP、COMMON_APP)

        :return: The app_type of this ListAppGroupRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListAppGroupRequest.

        应用组类型(SESSION_DESKTOP_APP、COMMON_APP)

        :param app_type: The app_type of this ListAppGroupRequest.
        :type app_type: str
        """
        self._app_type = app_type

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
        if not isinstance(other, ListAppGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
