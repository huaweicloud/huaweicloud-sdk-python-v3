# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'version': 'str',
        'description': 'str',
        'app_file_store': 'FileStoreLink',
        'app_icon_url': 'str',
        'install_type': 'InstallType',
        'authorization_type': 'AssignType',
        'install_command': 'str',
        'uninstall_command': 'str',
        'support_os': 'OsTypeEnum',
        'catalog_id': 'str',
        'status': 'AppStatusEnum',
        'install_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'description': 'description',
        'app_file_store': 'app_file_store',
        'app_icon_url': 'app_icon_url',
        'install_type': 'install_type',
        'authorization_type': 'authorization_type',
        'install_command': 'install_command',
        'uninstall_command': 'uninstall_command',
        'support_os': 'support_os',
        'catalog_id': 'catalog_id',
        'status': 'status',
        'install_info': 'install_info'
    }

    def __init__(self, name=None, version=None, description=None, app_file_store=None, app_icon_url=None, install_type=None, authorization_type=None, install_command=None, uninstall_command=None, support_os=None, catalog_id=None, status=None, install_info=None):
        r"""UpdateAppReq

        The model defined in huaweicloud sdk

        :param name: 应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~128个字符。
        :type name: str
        :param version: 版本号。
        :type version: str
        :param description: 描述。
        :type description: str
        :param app_file_store: 
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        :param app_icon_url: 图片的路径,支持使用可访问的URL地址或DataURIscheme。 * &#x60;可访问的URL&#x60; - https://xxx.x.xx.x/xxx/xx.jpg。 * &#x60;DataURIscheme&#x60; -  data;image/png;base64,iVBORw0KGgoAAAANS; 注意使用dataURLStream时，最多支持约xxKB大小的图片，且必须是png格式。
        :type app_icon_url: str
        :param install_type: 
        :type install_type: :class:`huaweicloudsdkworkspace.v2.InstallType`
        :param authorization_type: 
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        :param install_command: 安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type install_command: str
        :param uninstall_command: 卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type uninstall_command: str
        :param support_os: 
        :type support_os: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        :param catalog_id: 分类ID。
        :type catalog_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        :param install_info: 安装信息。
        :type install_info: str
        """
        
        

        self._name = None
        self._version = None
        self._description = None
        self._app_file_store = None
        self._app_icon_url = None
        self._install_type = None
        self._authorization_type = None
        self._install_command = None
        self._uninstall_command = None
        self._support_os = None
        self._catalog_id = None
        self._status = None
        self._install_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if app_file_store is not None:
            self.app_file_store = app_file_store
        if app_icon_url is not None:
            self.app_icon_url = app_icon_url
        if install_type is not None:
            self.install_type = install_type
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if install_command is not None:
            self.install_command = install_command
        if uninstall_command is not None:
            self.uninstall_command = uninstall_command
        if support_os is not None:
            self.support_os = support_os
        if catalog_id is not None:
            self.catalog_id = catalog_id
        if status is not None:
            self.status = status
        if install_info is not None:
            self.install_info = install_info

    @property
    def name(self):
        r"""Gets the name of this UpdateAppReq.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~128个字符。

        :return: The name of this UpdateAppReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAppReq.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~128个字符。

        :param name: The name of this UpdateAppReq.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this UpdateAppReq.

        版本号。

        :return: The version of this UpdateAppReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateAppReq.

        版本号。

        :param version: The version of this UpdateAppReq.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this UpdateAppReq.

        描述。

        :return: The description of this UpdateAppReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAppReq.

        描述。

        :param description: The description of this UpdateAppReq.
        :type description: str
        """
        self._description = description

    @property
    def app_file_store(self):
        r"""Gets the app_file_store of this UpdateAppReq.

        :return: The app_file_store of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        return self._app_file_store

    @app_file_store.setter
    def app_file_store(self, app_file_store):
        r"""Sets the app_file_store of this UpdateAppReq.

        :param app_file_store: The app_file_store of this UpdateAppReq.
        :type app_file_store: :class:`huaweicloudsdkworkspace.v2.FileStoreLink`
        """
        self._app_file_store = app_file_store

    @property
    def app_icon_url(self):
        r"""Gets the app_icon_url of this UpdateAppReq.

        图片的路径,支持使用可访问的URL地址或DataURIscheme。 * `可访问的URL` - https://xxx.x.xx.x/xxx/xx.jpg。 * `DataURIscheme` -  data;image/png;base64,iVBORw0KGgoAAAANS; 注意使用dataURLStream时，最多支持约xxKB大小的图片，且必须是png格式。

        :return: The app_icon_url of this UpdateAppReq.
        :rtype: str
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        r"""Sets the app_icon_url of this UpdateAppReq.

        图片的路径,支持使用可访问的URL地址或DataURIscheme。 * `可访问的URL` - https://xxx.x.xx.x/xxx/xx.jpg。 * `DataURIscheme` -  data;image/png;base64,iVBORw0KGgoAAAANS; 注意使用dataURLStream时，最多支持约xxKB大小的图片，且必须是png格式。

        :param app_icon_url: The app_icon_url of this UpdateAppReq.
        :type app_icon_url: str
        """
        self._app_icon_url = app_icon_url

    @property
    def install_type(self):
        r"""Gets the install_type of this UpdateAppReq.

        :return: The install_type of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InstallType`
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        r"""Sets the install_type of this UpdateAppReq.

        :param install_type: The install_type of this UpdateAppReq.
        :type install_type: :class:`huaweicloudsdkworkspace.v2.InstallType`
        """
        self._install_type = install_type

    @property
    def authorization_type(self):
        r"""Gets the authorization_type of this UpdateAppReq.

        :return: The authorization_type of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        r"""Sets the authorization_type of this UpdateAppReq.

        :param authorization_type: The authorization_type of this UpdateAppReq.
        :type authorization_type: :class:`huaweicloudsdkworkspace.v2.AssignType`
        """
        self._authorization_type = authorization_type

    @property
    def install_command(self):
        r"""Gets the install_command of this UpdateAppReq.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The install_command of this UpdateAppReq.
        :rtype: str
        """
        return self._install_command

    @install_command.setter
    def install_command(self, install_command):
        r"""Sets the install_command of this UpdateAppReq.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param install_command: The install_command of this UpdateAppReq.
        :type install_command: str
        """
        self._install_command = install_command

    @property
    def uninstall_command(self):
        r"""Gets the uninstall_command of this UpdateAppReq.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The uninstall_command of this UpdateAppReq.
        :rtype: str
        """
        return self._uninstall_command

    @uninstall_command.setter
    def uninstall_command(self, uninstall_command):
        r"""Sets the uninstall_command of this UpdateAppReq.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param uninstall_command: The uninstall_command of this UpdateAppReq.
        :type uninstall_command: str
        """
        self._uninstall_command = uninstall_command

    @property
    def support_os(self):
        r"""Gets the support_os of this UpdateAppReq.

        :return: The support_os of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this UpdateAppReq.

        :param support_os: The support_os of this UpdateAppReq.
        :type support_os: :class:`huaweicloudsdkworkspace.v2.OsTypeEnum`
        """
        self._support_os = support_os

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this UpdateAppReq.

        分类ID。

        :return: The catalog_id of this UpdateAppReq.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this UpdateAppReq.

        分类ID。

        :param catalog_id: The catalog_id of this UpdateAppReq.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def status(self):
        r"""Gets the status of this UpdateAppReq.

        :return: The status of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAppReq.

        :param status: The status of this UpdateAppReq.
        :type status: :class:`huaweicloudsdkworkspace.v2.AppStatusEnum`
        """
        self._status = status

    @property
    def install_info(self):
        r"""Gets the install_info of this UpdateAppReq.

        安装信息。

        :return: The install_info of this UpdateAppReq.
        :rtype: str
        """
        return self._install_info

    @install_info.setter
    def install_info(self, install_info):
        r"""Sets the install_info of this UpdateAppReq.

        安装信息。

        :param install_info: The install_info of this UpdateAppReq.
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
        if not isinstance(other, UpdateAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
