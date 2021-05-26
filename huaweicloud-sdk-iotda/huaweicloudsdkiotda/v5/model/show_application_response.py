# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowApplicationResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'create_time': 'str',
        'default_app': 'bool',
        'app_type': 'str',
        'username': 'str',
        'permission': 'str',
        'last_instance_id': 'str',
        'current_instance_id': 'str',
        'service_name': 'str',
        'freezed': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'create_time': 'create_time',
        'default_app': 'default_app',
        'app_type': 'app_type',
        'username': 'username',
        'permission': 'permission',
        'last_instance_id': 'last_instance_id',
        'current_instance_id': 'current_instance_id',
        'service_name': 'service_name',
        'freezed': 'freezed'
    }

    def __init__(self, app_id=None, app_name=None, create_time=None, default_app=None, app_type=None, username=None, permission=None, last_instance_id=None, current_instance_id=None, service_name=None, freezed=None):
        """ShowApplicationResponse - a model defined in huaweicloud sdk"""
        
        super(ShowApplicationResponse, self).__init__()

        self._app_id = None
        self._app_name = None
        self._create_time = None
        self._default_app = None
        self._app_type = None
        self._username = None
        self._permission = None
        self._last_instance_id = None
        self._current_instance_id = None
        self._service_name = None
        self._freezed = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if create_time is not None:
            self.create_time = create_time
        if default_app is not None:
            self.default_app = default_app
        if app_type is not None:
            self.app_type = app_type
        if username is not None:
            self.username = username
        if permission is not None:
            self.permission = permission
        if last_instance_id is not None:
            self.last_instance_id = last_instance_id
        if current_instance_id is not None:
            self.current_instance_id = current_instance_id
        if service_name is not None:
            self.service_name = service_name
        if freezed is not None:
            self.freezed = freezed

    @property
    def app_id(self):
        """Gets the app_id of this ShowApplicationResponse.

        资源空间ID，唯一标识一个资源空间，由物联网平台在创建资源空间时分配。资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。

        :return: The app_id of this ShowApplicationResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowApplicationResponse.

        资源空间ID，唯一标识一个资源空间，由物联网平台在创建资源空间时分配。资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。

        :param app_id: The app_id of this ShowApplicationResponse.
        :type: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ShowApplicationResponse.

        资源空间名称。

        :return: The app_name of this ShowApplicationResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowApplicationResponse.

        资源空间名称。

        :param app_name: The app_name of this ShowApplicationResponse.
        :type: str
        """
        self._app_name = app_name

    @property
    def create_time(self):
        """Gets the create_time of this ShowApplicationResponse.

        资源空间创建时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this ShowApplicationResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowApplicationResponse.

        资源空间创建时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this ShowApplicationResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def default_app(self):
        """Gets the default_app of this ShowApplicationResponse.

        是否为默认资源空间

        :return: The default_app of this ShowApplicationResponse.
        :rtype: bool
        """
        return self._default_app

    @default_app.setter
    def default_app(self, default_app):
        """Sets the default_app of this ShowApplicationResponse.

        是否为默认资源空间

        :param default_app: The default_app of this ShowApplicationResponse.
        :type: bool
        """
        self._default_app = default_app

    @property
    def app_type(self):
        """Gets the app_type of this ShowApplicationResponse.

        app的类型，标准版：Junior | 高级版：Normal

        :return: The app_type of this ShowApplicationResponse.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ShowApplicationResponse.

        app的类型，标准版：Junior | 高级版：Normal

        :param app_type: The app_type of this ShowApplicationResponse.
        :type: str
        """
        self._app_type = app_type

    @property
    def username(self):
        """Gets the username of this ShowApplicationResponse.

        用户名。

        :return: The username of this ShowApplicationResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ShowApplicationResponse.

        用户名。

        :param username: The username of this ShowApplicationResponse.
        :type: str
        """
        self._username = username

    @property
    def permission(self):
        """Gets the permission of this ShowApplicationResponse.

        app与用户的授权关系时，响应为：all | bind | edit | query ，其中bind权限类似于ALL权限，属于子用户权限。

        :return: The permission of this ShowApplicationResponse.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ShowApplicationResponse.

        app与用户的授权关系时，响应为：all | bind | edit | query ，其中bind权限类似于ALL权限，属于子用户权限。

        :param permission: The permission of this ShowApplicationResponse.
        :type: str
        """
        self._permission = permission

    @property
    def last_instance_id(self):
        """Gets the last_instance_id of this ShowApplicationResponse.

        迁移前实例ID。

        :return: The last_instance_id of this ShowApplicationResponse.
        :rtype: str
        """
        return self._last_instance_id

    @last_instance_id.setter
    def last_instance_id(self, last_instance_id):
        """Sets the last_instance_id of this ShowApplicationResponse.

        迁移前实例ID。

        :param last_instance_id: The last_instance_id of this ShowApplicationResponse.
        :type: str
        """
        self._last_instance_id = last_instance_id

    @property
    def current_instance_id(self):
        """Gets the current_instance_id of this ShowApplicationResponse.

        当前实例ID。

        :return: The current_instance_id of this ShowApplicationResponse.
        :rtype: str
        """
        return self._current_instance_id

    @current_instance_id.setter
    def current_instance_id(self, current_instance_id):
        """Sets the current_instance_id of this ShowApplicationResponse.

        当前实例ID。

        :param current_instance_id: The current_instance_id of this ShowApplicationResponse.
        :type: str
        """
        self._current_instance_id = current_instance_id

    @property
    def service_name(self):
        """Gets the service_name of this ShowApplicationResponse.

        对接的服务名

        :return: The service_name of this ShowApplicationResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ShowApplicationResponse.

        对接的服务名

        :param service_name: The service_name of this ShowApplicationResponse.
        :type: str
        """
        self._service_name = service_name

    @property
    def freezed(self):
        """Gets the freezed of this ShowApplicationResponse.

        是否冻结

        :return: The freezed of this ShowApplicationResponse.
        :rtype: bool
        """
        return self._freezed

    @freezed.setter
    def freezed(self, freezed):
        """Sets the freezed of this ShowApplicationResponse.

        是否冻结

        :param freezed: The freezed of this ShowApplicationResponse.
        :type: bool
        """
        self._freezed = freezed

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
