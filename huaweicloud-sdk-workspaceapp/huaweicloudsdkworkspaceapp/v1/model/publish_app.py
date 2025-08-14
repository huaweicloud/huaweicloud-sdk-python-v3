# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishApp:

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
        'command_param': 'str',
        'icon_uri': 'str',
        'execute_path': 'str',
        'work_path': 'str',
        'icon_path': 'str',
        'icon_index': 'int',
        'description': 'str',
        'source_type': 'int',
        'publisher': 'str',
        'source_image_ids': 'list[str]',
        'sandbox_enable': 'bool',
        'app_extended_info': 'AppExtendedInfo'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'command_param': 'command_param',
        'icon_uri': 'icon_uri',
        'execute_path': 'execute_path',
        'work_path': 'work_path',
        'icon_path': 'icon_path',
        'icon_index': 'icon_index',
        'description': 'description',
        'source_type': 'source_type',
        'publisher': 'publisher',
        'source_image_ids': 'source_image_ids',
        'sandbox_enable': 'sandbox_enable',
        'app_extended_info': 'app_extended_info'
    }

    def __init__(self, name=None, version=None, command_param=None, icon_uri=None, execute_path=None, work_path=None, icon_path=None, icon_index=None, description=None, source_type=None, publisher=None, source_image_ids=None, sandbox_enable=None, app_extended_info=None):
        r"""PublishApp

        The model defined in huaweicloud sdk

        :param name: 应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 不允许包含如下字符:^;|~&#x60;{}[]&lt;&gt;。 3. 长度1~64个字符。
        :type name: str
        :param version: 应用版本号。
        :type version: str
        :param command_param: 启动命令行参数。
        :type command_param: str
        :param icon_uri: 图标地址，该字段当前未使用。 &gt; - 图片的默认大小当前限制为8KB，即1024 * 8字节。 &gt; - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。
        :type icon_uri: str
        :param execute_path: 执行路径。
        :type execute_path: str
        :param work_path: 应用工作目录。
        :type work_path: str
        :param icon_path: 应用图标的路径。
        :type icon_path: str
        :param icon_index: 应用图标的索引。
        :type icon_index: int
        :param description: 应用描述。
        :type description: str
        :param source_type: 应用类型： - &#39;1&#39;:系统保留不可用。 - &#39;2&#39;:镜像应用。 - &#39;3&#39;:自定义应用。
        :type source_type: int
        :param publisher: 应用发布者。
        :type publisher: str
        :param source_image_ids: 镜像ids,最多20个。
        :type source_image_ids: list[str]
        :param sandbox_enable: 是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。
        :type sandbox_enable: bool
        :param app_extended_info: 
        :type app_extended_info: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        
        

        self._name = None
        self._version = None
        self._command_param = None
        self._icon_uri = None
        self._execute_path = None
        self._work_path = None
        self._icon_path = None
        self._icon_index = None
        self._description = None
        self._source_type = None
        self._publisher = None
        self._source_image_ids = None
        self._sandbox_enable = None
        self._app_extended_info = None
        self.discriminator = None

        self.name = name
        if version is not None:
            self.version = version
        if command_param is not None:
            self.command_param = command_param
        if icon_uri is not None:
            self.icon_uri = icon_uri
        self.execute_path = execute_path
        if work_path is not None:
            self.work_path = work_path
        if icon_path is not None:
            self.icon_path = icon_path
        if icon_index is not None:
            self.icon_index = icon_index
        if description is not None:
            self.description = description
        self.source_type = source_type
        if publisher is not None:
            self.publisher = publisher
        if source_image_ids is not None:
            self.source_image_ids = source_image_ids
        if sandbox_enable is not None:
            self.sandbox_enable = sandbox_enable
        if app_extended_info is not None:
            self.app_extended_info = app_extended_info

    @property
    def name(self):
        r"""Gets the name of this PublishApp.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 不允许包含如下字符:^;|~`{}[]<>。 3. 长度1~64个字符。

        :return: The name of this PublishApp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublishApp.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格。 2. 不允许包含如下字符:^;|~`{}[]<>。 3. 长度1~64个字符。

        :param name: The name of this PublishApp.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this PublishApp.

        应用版本号。

        :return: The version of this PublishApp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PublishApp.

        应用版本号。

        :param version: The version of this PublishApp.
        :type version: str
        """
        self._version = version

    @property
    def command_param(self):
        r"""Gets the command_param of this PublishApp.

        启动命令行参数。

        :return: The command_param of this PublishApp.
        :rtype: str
        """
        return self._command_param

    @command_param.setter
    def command_param(self, command_param):
        r"""Sets the command_param of this PublishApp.

        启动命令行参数。

        :param command_param: The command_param of this PublishApp.
        :type command_param: str
        """
        self._command_param = command_param

    @property
    def icon_uri(self):
        r"""Gets the icon_uri of this PublishApp.

        图标地址，该字段当前未使用。 > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :return: The icon_uri of this PublishApp.
        :rtype: str
        """
        return self._icon_uri

    @icon_uri.setter
    def icon_uri(self, icon_uri):
        r"""Sets the icon_uri of this PublishApp.

        图标地址，该字段当前未使用。 > - 图片的默认大小当前限制为8KB，即1024 * 8字节。 > - 如果数据格式为data;image/png;base64,iVBORw0KGgoAAAANS时实际大小约为字段约为：size * 4/3 + 4bytes。

        :param icon_uri: The icon_uri of this PublishApp.
        :type icon_uri: str
        """
        self._icon_uri = icon_uri

    @property
    def execute_path(self):
        r"""Gets the execute_path of this PublishApp.

        执行路径。

        :return: The execute_path of this PublishApp.
        :rtype: str
        """
        return self._execute_path

    @execute_path.setter
    def execute_path(self, execute_path):
        r"""Sets the execute_path of this PublishApp.

        执行路径。

        :param execute_path: The execute_path of this PublishApp.
        :type execute_path: str
        """
        self._execute_path = execute_path

    @property
    def work_path(self):
        r"""Gets the work_path of this PublishApp.

        应用工作目录。

        :return: The work_path of this PublishApp.
        :rtype: str
        """
        return self._work_path

    @work_path.setter
    def work_path(self, work_path):
        r"""Sets the work_path of this PublishApp.

        应用工作目录。

        :param work_path: The work_path of this PublishApp.
        :type work_path: str
        """
        self._work_path = work_path

    @property
    def icon_path(self):
        r"""Gets the icon_path of this PublishApp.

        应用图标的路径。

        :return: The icon_path of this PublishApp.
        :rtype: str
        """
        return self._icon_path

    @icon_path.setter
    def icon_path(self, icon_path):
        r"""Sets the icon_path of this PublishApp.

        应用图标的路径。

        :param icon_path: The icon_path of this PublishApp.
        :type icon_path: str
        """
        self._icon_path = icon_path

    @property
    def icon_index(self):
        r"""Gets the icon_index of this PublishApp.

        应用图标的索引。

        :return: The icon_index of this PublishApp.
        :rtype: int
        """
        return self._icon_index

    @icon_index.setter
    def icon_index(self, icon_index):
        r"""Sets the icon_index of this PublishApp.

        应用图标的索引。

        :param icon_index: The icon_index of this PublishApp.
        :type icon_index: int
        """
        self._icon_index = icon_index

    @property
    def description(self):
        r"""Gets the description of this PublishApp.

        应用描述。

        :return: The description of this PublishApp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishApp.

        应用描述。

        :param description: The description of this PublishApp.
        :type description: str
        """
        self._description = description

    @property
    def source_type(self):
        r"""Gets the source_type of this PublishApp.

        应用类型： - '1':系统保留不可用。 - '2':镜像应用。 - '3':自定义应用。

        :return: The source_type of this PublishApp.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this PublishApp.

        应用类型： - '1':系统保留不可用。 - '2':镜像应用。 - '3':自定义应用。

        :param source_type: The source_type of this PublishApp.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def publisher(self):
        r"""Gets the publisher of this PublishApp.

        应用发布者。

        :return: The publisher of this PublishApp.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        r"""Sets the publisher of this PublishApp.

        应用发布者。

        :param publisher: The publisher of this PublishApp.
        :type publisher: str
        """
        self._publisher = publisher

    @property
    def source_image_ids(self):
        r"""Gets the source_image_ids of this PublishApp.

        镜像ids,最多20个。

        :return: The source_image_ids of this PublishApp.
        :rtype: list[str]
        """
        return self._source_image_ids

    @source_image_ids.setter
    def source_image_ids(self, source_image_ids):
        r"""Sets the source_image_ids of this PublishApp.

        镜像ids,最多20个。

        :param source_image_ids: The source_image_ids of this PublishApp.
        :type source_image_ids: list[str]
        """
        self._source_image_ids = source_image_ids

    @property
    def sandbox_enable(self):
        r"""Gets the sandbox_enable of this PublishApp.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。

        :return: The sandbox_enable of this PublishApp.
        :rtype: bool
        """
        return self._sandbox_enable

    @sandbox_enable.setter
    def sandbox_enable(self, sandbox_enable):
        r"""Sets the sandbox_enable of this PublishApp.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。

        :param sandbox_enable: The sandbox_enable of this PublishApp.
        :type sandbox_enable: bool
        """
        self._sandbox_enable = sandbox_enable

    @property
    def app_extended_info(self):
        r"""Gets the app_extended_info of this PublishApp.

        :return: The app_extended_info of this PublishApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        return self._app_extended_info

    @app_extended_info.setter
    def app_extended_info(self, app_extended_info):
        r"""Sets the app_extended_info of this PublishApp.

        :param app_extended_info: The app_extended_info of this PublishApp.
        :type app_extended_info: :class:`huaweicloudsdkworkspaceapp.v1.AppExtendedInfo`
        """
        self._app_extended_info = app_extended_info

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
        if not isinstance(other, PublishApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
