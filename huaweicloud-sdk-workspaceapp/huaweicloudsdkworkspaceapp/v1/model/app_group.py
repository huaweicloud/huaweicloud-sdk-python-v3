# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppGroup:

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
        'name': 'str',
        'app_server_group_id': 'str',
        'app_server_group_name': 'str',
        'description': 'str',
        'authorization_type': 'AuthorizationTypeEnum',
        'tenant_id': 'str',
        'app_type': 'AppTypeEnum',
        'create_at': 'datetime',
        'app_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'app_server_group_id': 'app_server_group_id',
        'app_server_group_name': 'app_server_group_name',
        'description': 'description',
        'authorization_type': 'authorization_type',
        'tenant_id': 'tenant_id',
        'app_type': 'app_type',
        'create_at': 'create_at',
        'app_count': 'app_count'
    }

    def __init__(self, id=None, name=None, app_server_group_id=None, app_server_group_name=None, description=None, authorization_type=None, tenant_id=None, app_type=None, create_at=None, app_count=None):
        """AppGroup

        The model defined in huaweicloud sdk

        :param id: 应用组ID
        :type id: str
        :param name: 应用组名称
        :type name: str
        :param app_server_group_id: 应用服务器组ID
        :type app_server_group_id: str
        :param app_server_group_name: 应用服务器组名称
        :type app_server_group_name: str
        :param description: 应用组描述
        :type description: str
        :param authorization_type: 
        :type authorization_type: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param app_type: 
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        :param create_at: 发布时间
        :type create_at: datetime
        :param app_count: 应用数量
        :type app_count: int
        """
        
        

        self._id = None
        self._name = None
        self._app_server_group_id = None
        self._app_server_group_name = None
        self._description = None
        self._authorization_type = None
        self._tenant_id = None
        self._app_type = None
        self._create_at = None
        self._app_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if app_server_group_id is not None:
            self.app_server_group_id = app_server_group_id
        if app_server_group_name is not None:
            self.app_server_group_name = app_server_group_name
        if description is not None:
            self.description = description
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if app_type is not None:
            self.app_type = app_type
        if create_at is not None:
            self.create_at = create_at
        if app_count is not None:
            self.app_count = app_count

    @property
    def id(self):
        """Gets the id of this AppGroup.

        应用组ID

        :return: The id of this AppGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppGroup.

        应用组ID

        :param id: The id of this AppGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppGroup.

        应用组名称

        :return: The name of this AppGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppGroup.

        应用组名称

        :param name: The name of this AppGroup.
        :type name: str
        """
        self._name = name

    @property
    def app_server_group_id(self):
        """Gets the app_server_group_id of this AppGroup.

        应用服务器组ID

        :return: The app_server_group_id of this AppGroup.
        :rtype: str
        """
        return self._app_server_group_id

    @app_server_group_id.setter
    def app_server_group_id(self, app_server_group_id):
        """Sets the app_server_group_id of this AppGroup.

        应用服务器组ID

        :param app_server_group_id: The app_server_group_id of this AppGroup.
        :type app_server_group_id: str
        """
        self._app_server_group_id = app_server_group_id

    @property
    def app_server_group_name(self):
        """Gets the app_server_group_name of this AppGroup.

        应用服务器组名称

        :return: The app_server_group_name of this AppGroup.
        :rtype: str
        """
        return self._app_server_group_name

    @app_server_group_name.setter
    def app_server_group_name(self, app_server_group_name):
        """Sets the app_server_group_name of this AppGroup.

        应用服务器组名称

        :param app_server_group_name: The app_server_group_name of this AppGroup.
        :type app_server_group_name: str
        """
        self._app_server_group_name = app_server_group_name

    @property
    def description(self):
        """Gets the description of this AppGroup.

        应用组描述

        :return: The description of this AppGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppGroup.

        应用组描述

        :param description: The description of this AppGroup.
        :type description: str
        """
        self._description = description

    @property
    def authorization_type(self):
        """Gets the authorization_type of this AppGroup.

        :return: The authorization_type of this AppGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this AppGroup.

        :param authorization_type: The authorization_type of this AppGroup.
        :type authorization_type: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizationTypeEnum`
        """
        self._authorization_type = authorization_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AppGroup.

        租户ID

        :return: The tenant_id of this AppGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AppGroup.

        租户ID

        :param tenant_id: The tenant_id of this AppGroup.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def app_type(self):
        """Gets the app_type of this AppGroup.

        :return: The app_type of this AppGroup.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppGroup.

        :param app_type: The app_type of this AppGroup.
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        self._app_type = app_type

    @property
    def create_at(self):
        """Gets the create_at of this AppGroup.

        发布时间

        :return: The create_at of this AppGroup.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this AppGroup.

        发布时间

        :param create_at: The create_at of this AppGroup.
        :type create_at: datetime
        """
        self._create_at = create_at

    @property
    def app_count(self):
        """Gets the app_count of this AppGroup.

        应用数量

        :return: The app_count of this AppGroup.
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        """Sets the app_count of this AppGroup.

        应用数量

        :param app_count: The app_count of this AppGroup.
        :type app_count: int
        """
        self._app_count = app_count

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
        if not isinstance(other, AppGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
