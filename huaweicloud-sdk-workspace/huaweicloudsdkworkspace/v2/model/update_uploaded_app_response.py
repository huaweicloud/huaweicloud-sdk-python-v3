# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUploadedAppResponse(SdkResponse):

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
        'authorization_type': 'str',
        'app_file_store': 'FileStoreLink',
        'app_icon_url': 'str',
        'install_type': 'str',
        'install_command': 'str',
        'uninstall_command': 'str',
        'support_os': 'str',
        'status': 'str',
        'application_source': 'str',
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
        r"""UpdateUploadedAppResponse

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
        :param authorization_type: * &#x60;ALL_USER&#x60; - 全部用户 * &#x60;ASSIGN_USER&#x60; - 授权指定用户
        :type authorization_type: str
        :param app_file_store: 
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        :param app_icon_url: 应用图标路径。
        :type app_icon_url: str
        :param install_type: 安装方式：   * &#x60;QUIET_INSTALL&#x60; - 静默安装。     安装命令(静默安装命令)，例: ${FILE_PATH} /S。   * &#x60;UNZIP_INSTALL&#x60; - 解压安装。     例: unzip ${FILE_PATH}。   * &#x60;GUI_INSTALL&#x60; - 用户通过GUI界面安装。 install_type为QUIET_INSTALL、UNZIP_INSTALL时install_command非空。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type install_type: str
        :param install_command: 安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type install_command: str
        :param uninstall_command: 卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type uninstall_command: str
        :param support_os: 系统类型： * &#x60;Linux&#x60; - * &#x60;Windows&#x60; - * &#x60;Other&#x60; -
        :type support_os: str
        :param status: 应用状态(正常、禁用) * &#39;NORMAL&#39; - 正常 * &#39;FORBIDDEN&#39; - 禁用状态
        :type status: str
        :param application_source: 应用来源： * &#x60;CUSTOM&#x60; - 用户上传 * &#x60;SYSTEM&#x60; - 内置应用 * &#x60;MARKET&#x60; - 市场应用
        :type application_source: str
        :param create_time: 应用创建时间。
        :type create_time: datetime
        :param catalog_id: 分类ID。
        :type catalog_id: str
        :param catalog: 分类名称。
        :type catalog: str
        :param install_info: 安装信息。
        :type install_info: str
        """
        
        super().__init__()

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
        r"""Gets the id of this UpdateUploadedAppResponse.

        唯一标识。

        :return: The id of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateUploadedAppResponse.

        唯一标识。

        :param id: The id of this UpdateUploadedAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this UpdateUploadedAppResponse.

        租户id。

        :return: The tenant_id of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this UpdateUploadedAppResponse.

        租户id。

        :param tenant_id: The tenant_id of this UpdateUploadedAppResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this UpdateUploadedAppResponse.

        应用名称。

        :return: The name of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateUploadedAppResponse.

        应用名称。

        :param name: The name of this UpdateUploadedAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this UpdateUploadedAppResponse.

        版本号。

        :return: The version of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateUploadedAppResponse.

        版本号。

        :param version: The version of this UpdateUploadedAppResponse.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this UpdateUploadedAppResponse.

        描述。

        :return: The description of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateUploadedAppResponse.

        描述。

        :param description: The description of this UpdateUploadedAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def authorization_type(self):
        r"""Gets the authorization_type of this UpdateUploadedAppResponse.

        * `ALL_USER` - 全部用户 * `ASSIGN_USER` - 授权指定用户

        :return: The authorization_type of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        r"""Sets the authorization_type of this UpdateUploadedAppResponse.

        * `ALL_USER` - 全部用户 * `ASSIGN_USER` - 授权指定用户

        :param authorization_type: The authorization_type of this UpdateUploadedAppResponse.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def app_file_store(self):
        r"""Gets the app_file_store of this UpdateUploadedAppResponse.

        :return: The app_file_store of this UpdateUploadedAppResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        return self._app_file_store

    @app_file_store.setter
    def app_file_store(self, app_file_store):
        r"""Sets the app_file_store of this UpdateUploadedAppResponse.

        :param app_file_store: The app_file_store of this UpdateUploadedAppResponse.
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        self._app_file_store = app_file_store

    @property
    def app_icon_url(self):
        r"""Gets the app_icon_url of this UpdateUploadedAppResponse.

        应用图标路径。

        :return: The app_icon_url of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        r"""Sets the app_icon_url of this UpdateUploadedAppResponse.

        应用图标路径。

        :param app_icon_url: The app_icon_url of this UpdateUploadedAppResponse.
        :type app_icon_url: str
        """
        self._app_icon_url = app_icon_url

    @property
    def install_type(self):
        r"""Gets the install_type of this UpdateUploadedAppResponse.

        安装方式：   * `QUIET_INSTALL` - 静默安装。     安装命令(静默安装命令)，例: ${FILE_PATH} /S。   * `UNZIP_INSTALL` - 解压安装。     例: unzip ${FILE_PATH}。   * `GUI_INSTALL` - 用户通过GUI界面安装。 install_type为QUIET_INSTALL、UNZIP_INSTALL时install_command非空。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The install_type of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        r"""Sets the install_type of this UpdateUploadedAppResponse.

        安装方式：   * `QUIET_INSTALL` - 静默安装。     安装命令(静默安装命令)，例: ${FILE_PATH} /S。   * `UNZIP_INSTALL` - 解压安装。     例: unzip ${FILE_PATH}。   * `GUI_INSTALL` - 用户通过GUI界面安装。 install_type为QUIET_INSTALL、UNZIP_INSTALL时install_command非空。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param install_type: The install_type of this UpdateUploadedAppResponse.
        :type install_type: str
        """
        self._install_type = install_type

    @property
    def install_command(self):
        r"""Gets the install_command of this UpdateUploadedAppResponse.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The install_command of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._install_command

    @install_command.setter
    def install_command(self, install_command):
        r"""Sets the install_command of this UpdateUploadedAppResponse.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param install_command: The install_command of this UpdateUploadedAppResponse.
        :type install_command: str
        """
        self._install_command = install_command

    @property
    def uninstall_command(self):
        r"""Gets the uninstall_command of this UpdateUploadedAppResponse.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The uninstall_command of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._uninstall_command

    @uninstall_command.setter
    def uninstall_command(self, uninstall_command):
        r"""Sets the uninstall_command of this UpdateUploadedAppResponse.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param uninstall_command: The uninstall_command of this UpdateUploadedAppResponse.
        :type uninstall_command: str
        """
        self._uninstall_command = uninstall_command

    @property
    def support_os(self):
        r"""Gets the support_os of this UpdateUploadedAppResponse.

        系统类型： * `Linux` - * `Windows` - * `Other` -

        :return: The support_os of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this UpdateUploadedAppResponse.

        系统类型： * `Linux` - * `Windows` - * `Other` -

        :param support_os: The support_os of this UpdateUploadedAppResponse.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def status(self):
        r"""Gets the status of this UpdateUploadedAppResponse.

        应用状态(正常、禁用) * 'NORMAL' - 正常 * 'FORBIDDEN' - 禁用状态

        :return: The status of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateUploadedAppResponse.

        应用状态(正常、禁用) * 'NORMAL' - 正常 * 'FORBIDDEN' - 禁用状态

        :param status: The status of this UpdateUploadedAppResponse.
        :type status: str
        """
        self._status = status

    @property
    def application_source(self):
        r"""Gets the application_source of this UpdateUploadedAppResponse.

        应用来源： * `CUSTOM` - 用户上传 * `SYSTEM` - 内置应用 * `MARKET` - 市场应用

        :return: The application_source of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._application_source

    @application_source.setter
    def application_source(self, application_source):
        r"""Sets the application_source of this UpdateUploadedAppResponse.

        应用来源： * `CUSTOM` - 用户上传 * `SYSTEM` - 内置应用 * `MARKET` - 市场应用

        :param application_source: The application_source of this UpdateUploadedAppResponse.
        :type application_source: str
        """
        self._application_source = application_source

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateUploadedAppResponse.

        应用创建时间。

        :return: The create_time of this UpdateUploadedAppResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateUploadedAppResponse.

        应用创建时间。

        :param create_time: The create_time of this UpdateUploadedAppResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this UpdateUploadedAppResponse.

        分类ID。

        :return: The catalog_id of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this UpdateUploadedAppResponse.

        分类ID。

        :param catalog_id: The catalog_id of this UpdateUploadedAppResponse.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def catalog(self):
        r"""Gets the catalog of this UpdateUploadedAppResponse.

        分类名称。

        :return: The catalog of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this UpdateUploadedAppResponse.

        分类名称。

        :param catalog: The catalog of this UpdateUploadedAppResponse.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def install_info(self):
        r"""Gets the install_info of this UpdateUploadedAppResponse.

        安装信息。

        :return: The install_info of this UpdateUploadedAppResponse.
        :rtype: str
        """
        return self._install_info

    @install_info.setter
    def install_info(self, install_info):
        r"""Sets the install_info of this UpdateUploadedAppResponse.

        安装信息。

        :param install_info: The install_info of this UpdateUploadedAppResponse.
        :type install_info: str
        """
        self._install_info = install_info

    def to_dict(self):
        import warnings
        warnings.warn("UpdateUploadedAppResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateUploadedAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
