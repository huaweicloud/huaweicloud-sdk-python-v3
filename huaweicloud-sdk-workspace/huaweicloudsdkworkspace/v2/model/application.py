# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Application:

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
        'tenant_id': 'str',
        'name': 'str',
        'version': 'str',
        'description': 'str',
        'authorization_type': 'AssignType',
        'app_file_store': 'FileStoreLink',
        'app_icon_url': 'str',
        'install_type': 'InstallType',
        'install_command': 'str',
        'uninstall_command': 'str',
        'support_os': 'OsTypeEnum',
        'status': 'AppStatusEnum',
        'application_source': 'AppSourceType',
        'create_time': 'datetime',
        'catalog_id': 'str',
        'catalog': 'str',
        'install_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'version': 'version',
        'description': 'description',
        'authorization_type': 'authorization_type',
        'app_file_store': 'app_file_store',
        'app_icon_url': 'app_icon_url',
        'install_type': 'install_type',
        'install_command': 'install_command',
        'uninstall_command': 'uninstall_command',
        'support_os': 'support_os',
        'status': 'status',
        'application_source': 'application_source',
        'create_time': 'create_time',
        'catalog_id': 'catalog_id',
        'catalog': 'catalog',
        'install_info': 'install_info'
    }

    def __init__(self, id=None, tenant_id=None, name=None, version=None, description=None, authorization_type=None, app_file_store=None, app_icon_url=None, install_type=None, install_command=None, uninstall_command=None, support_os=None, status=None, application_source=None, create_time=None, catalog_id=None, catalog=None, install_info=None):
        """Application

        The model defined in huaweicloud sdk

        :param id: 唯一标识。
        :type id: str
        :param tenant_id: 租户id。
        :type tenant_id: str
        :param name: 应用名称。
        :type name: str
        :param version: 版本号。
        :type version: str
        :param description: 描述。
        :type description: str
        :param authorization_type: 
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        :param app_file_store: 
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        :param app_icon_url: 应用图标路径。
        :type app_icon_url: str
        :param install_type: 
        :type install_type: :class:`huaweicloudsdkworkspace.v2.InstallType`
        :param install_command: 安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type install_command: str
        :param uninstall_command: 卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type uninstall_command: str
        :param support_os: 
        :type support_os: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        :param status: 
        :type status: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        :param application_source: 
        :type application_source: :class:`huaweicloudsdkworkspace.v2.AppSourceType`
        :param create_time: 应用创建时间。
        :type create_time: datetime
        :param catalog_id: 分类ID。
        :type catalog_id: str
        :param catalog: 分类名称。
        :type catalog: str
        :param install_info: 安装信息。
        :type install_info: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._version = None
        self._description = None
        self._authorization_type = None
        self._app_file_store = None
        self._app_icon_url = None
        self._install_type = None
        self._install_command = None
        self._uninstall_command = None
        self._support_os = None
        self._status = None
        self._application_source = None
        self._create_time = None
        self._catalog_id = None
        self._catalog = None
        self._install_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if app_file_store is not None:
            self.app_file_store = app_file_store
        if app_icon_url is not None:
            self.app_icon_url = app_icon_url
        if install_type is not None:
            self.install_type = install_type
        if install_command is not None:
            self.install_command = install_command
        if uninstall_command is not None:
            self.uninstall_command = uninstall_command
        if support_os is not None:
            self.support_os = support_os
        if status is not None:
            self.status = status
        if application_source is not None:
            self.application_source = application_source
        if create_time is not None:
            self.create_time = create_time
        if catalog_id is not None:
            self.catalog_id = catalog_id
        if catalog is not None:
            self.catalog = catalog
        if install_info is not None:
            self.install_info = install_info

    @property
    def id(self):
        """Gets the id of this Application.

        唯一标识。

        :return: The id of this Application.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        唯一标识。

        :param id: The id of this Application.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Application.

        租户id。

        :return: The tenant_id of this Application.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Application.

        租户id。

        :param tenant_id: The tenant_id of this Application.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this Application.

        应用名称。

        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        应用名称。

        :param name: The name of this Application.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this Application.

        版本号。

        :return: The version of this Application.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Application.

        版本号。

        :param version: The version of this Application.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this Application.

        描述。

        :return: The description of this Application.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.

        描述。

        :param description: The description of this Application.
        :type description: str
        """
        self._description = description

    @property
    def authorization_type(self):
        """Gets the authorization_type of this Application.

        :return: The authorization_type of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this Application.

        :param authorization_type: The authorization_type of this Application.
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        self._authorization_type = authorization_type

    @property
    def app_file_store(self):
        """Gets the app_file_store of this Application.

        :return: The app_file_store of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        return self._app_file_store

    @app_file_store.setter
    def app_file_store(self, app_file_store):
        """Sets the app_file_store of this Application.

        :param app_file_store: The app_file_store of this Application.
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        self._app_file_store = app_file_store

    @property
    def app_icon_url(self):
        """Gets the app_icon_url of this Application.

        应用图标路径。

        :return: The app_icon_url of this Application.
        :rtype: str
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        """Sets the app_icon_url of this Application.

        应用图标路径。

        :param app_icon_url: The app_icon_url of this Application.
        :type app_icon_url: str
        """
        self._app_icon_url = app_icon_url

    @property
    def install_type(self):
        """Gets the install_type of this Application.

        :return: The install_type of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InstallType`
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        """Sets the install_type of this Application.

        :param install_type: The install_type of this Application.
        :type install_type: :class:`huaweicloudsdkworkspace.v2.InstallType`
        """
        self._install_type = install_type

    @property
    def install_command(self):
        """Gets the install_command of this Application.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The install_command of this Application.
        :rtype: str
        """
        return self._install_command

    @install_command.setter
    def install_command(self, install_command):
        """Sets the install_command of this Application.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param install_command: The install_command of this Application.
        :type install_command: str
        """
        self._install_command = install_command

    @property
    def uninstall_command(self):
        """Gets the uninstall_command of this Application.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The uninstall_command of this Application.
        :rtype: str
        """
        return self._uninstall_command

    @uninstall_command.setter
    def uninstall_command(self, uninstall_command):
        """Sets the uninstall_command of this Application.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param uninstall_command: The uninstall_command of this Application.
        :type uninstall_command: str
        """
        self._uninstall_command = uninstall_command

    @property
    def support_os(self):
        """Gets the support_os of this Application.

        :return: The support_os of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        """Sets the support_os of this Application.

        :param support_os: The support_os of this Application.
        :type support_os: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        """
        self._support_os = support_os

    @property
    def status(self):
        """Gets the status of this Application.

        :return: The status of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Application.

        :param status: The status of this Application.
        :type status: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        """
        self._status = status

    @property
    def application_source(self):
        """Gets the application_source of this Application.

        :return: The application_source of this Application.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AppSourceType`
        """
        return self._application_source

    @application_source.setter
    def application_source(self, application_source):
        """Sets the application_source of this Application.

        :param application_source: The application_source of this Application.
        :type application_source: :class:`huaweicloudsdkworkspace.v2.AppSourceType`
        """
        self._application_source = application_source

    @property
    def create_time(self):
        """Gets the create_time of this Application.

        应用创建时间。

        :return: The create_time of this Application.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Application.

        应用创建时间。

        :param create_time: The create_time of this Application.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def catalog_id(self):
        """Gets the catalog_id of this Application.

        分类ID。

        :return: The catalog_id of this Application.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this Application.

        分类ID。

        :param catalog_id: The catalog_id of this Application.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def catalog(self):
        """Gets the catalog of this Application.

        分类名称。

        :return: The catalog of this Application.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this Application.

        分类名称。

        :param catalog: The catalog of this Application.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def install_info(self):
        """Gets the install_info of this Application.

        安装信息。

        :return: The install_info of this Application.
        :rtype: str
        """
        return self._install_info

    @install_info.setter
    def install_info(self, install_info):
        """Sets the install_info of this Application.

        安装信息。

        :param install_info: The install_info of this Application.
        :type install_info: str
        """
        self._install_info = install_info

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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
