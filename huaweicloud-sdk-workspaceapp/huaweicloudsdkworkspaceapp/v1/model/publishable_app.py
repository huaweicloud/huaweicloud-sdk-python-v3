# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishableApp:

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
        'version': 'str',
        'command_param': 'str',
        'execute_path': 'str',
        'work_path': 'str',
        'icon_path': 'str',
        'icon_index': 'int',
        'description': 'str',
        'app_group_id': 'str',
        'state': 'AppStateEnum',
        'tenant_id': 'str',
        'publish_at': 'datetime',
        'source_type': 'int',
        'publisher': 'str',
        'icon_url': 'str',
        'publishable': 'bool',
        'sandbox_enable': 'bool',
        'source_image_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'command_param': 'command_param',
        'execute_path': 'execute_path',
        'work_path': 'work_path',
        'icon_path': 'icon_path',
        'icon_index': 'icon_index',
        'description': 'description',
        'app_group_id': 'app_group_id',
        'state': 'state',
        'tenant_id': 'tenant_id',
        'publish_at': 'publish_at',
        'source_type': 'source_type',
        'publisher': 'publisher',
        'icon_url': 'icon_url',
        'publishable': 'publishable',
        'sandbox_enable': 'sandbox_enable',
        'source_image_ids': 'source_image_ids'
    }

    def __init__(self, id=None, name=None, version=None, command_param=None, execute_path=None, work_path=None, icon_path=None, icon_index=None, description=None, app_group_id=None, state=None, tenant_id=None, publish_at=None, source_type=None, publisher=None, icon_url=None, publishable=None, sandbox_enable=None, source_image_ids=None):
        r"""PublishableApp

        The model defined in huaweicloud sdk

        :param id: 应用ID。
        :type id: str
        :param name: 应用名称。
        :type name: str
        :param version: 应用版本号。
        :type version: str
        :param command_param: 启动命令行参数。
        :type command_param: str
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
        :param app_group_id: 应用组标识Id。
        :type app_group_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        :param tenant_id: 所在的租户ID。
        :type tenant_id: str
        :param publish_at: 发布时间。
        :type publish_at: datetime
        :param source_type: 应用类型： - &#39;1&#39;:系统内置应用 - &#39;2&#39;:镜像应用 - &#39;3&#39;:自定义应用
        :type source_type: int
        :param publisher: 应用发布者。
        :type publisher: str
        :param icon_url: 图标url。
        :type icon_url: str
        :param publishable: 是否可发布应用： - true: 可发布。 - false: 不可发布。
        :type publishable: bool
        :param sandbox_enable: 是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。
        :type sandbox_enable: bool
        :param source_image_ids: 镜像ids。
        :type source_image_ids: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self._command_param = None
        self._execute_path = None
        self._work_path = None
        self._icon_path = None
        self._icon_index = None
        self._description = None
        self._app_group_id = None
        self._state = None
        self._tenant_id = None
        self._publish_at = None
        self._source_type = None
        self._publisher = None
        self._icon_url = None
        self._publishable = None
        self._sandbox_enable = None
        self._source_image_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if command_param is not None:
            self.command_param = command_param
        if execute_path is not None:
            self.execute_path = execute_path
        if work_path is not None:
            self.work_path = work_path
        if icon_path is not None:
            self.icon_path = icon_path
        if icon_index is not None:
            self.icon_index = icon_index
        if description is not None:
            self.description = description
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if state is not None:
            self.state = state
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if publish_at is not None:
            self.publish_at = publish_at
        if source_type is not None:
            self.source_type = source_type
        if publisher is not None:
            self.publisher = publisher
        if icon_url is not None:
            self.icon_url = icon_url
        if publishable is not None:
            self.publishable = publishable
        if sandbox_enable is not None:
            self.sandbox_enable = sandbox_enable
        if source_image_ids is not None:
            self.source_image_ids = source_image_ids

    @property
    def id(self):
        r"""Gets the id of this PublishableApp.

        应用ID。

        :return: The id of this PublishableApp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublishableApp.

        应用ID。

        :param id: The id of this PublishableApp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PublishableApp.

        应用名称。

        :return: The name of this PublishableApp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublishableApp.

        应用名称。

        :param name: The name of this PublishableApp.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this PublishableApp.

        应用版本号。

        :return: The version of this PublishableApp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PublishableApp.

        应用版本号。

        :param version: The version of this PublishableApp.
        :type version: str
        """
        self._version = version

    @property
    def command_param(self):
        r"""Gets the command_param of this PublishableApp.

        启动命令行参数。

        :return: The command_param of this PublishableApp.
        :rtype: str
        """
        return self._command_param

    @command_param.setter
    def command_param(self, command_param):
        r"""Sets the command_param of this PublishableApp.

        启动命令行参数。

        :param command_param: The command_param of this PublishableApp.
        :type command_param: str
        """
        self._command_param = command_param

    @property
    def execute_path(self):
        r"""Gets the execute_path of this PublishableApp.

        执行路径。

        :return: The execute_path of this PublishableApp.
        :rtype: str
        """
        return self._execute_path

    @execute_path.setter
    def execute_path(self, execute_path):
        r"""Sets the execute_path of this PublishableApp.

        执行路径。

        :param execute_path: The execute_path of this PublishableApp.
        :type execute_path: str
        """
        self._execute_path = execute_path

    @property
    def work_path(self):
        r"""Gets the work_path of this PublishableApp.

        应用工作目录。

        :return: The work_path of this PublishableApp.
        :rtype: str
        """
        return self._work_path

    @work_path.setter
    def work_path(self, work_path):
        r"""Sets the work_path of this PublishableApp.

        应用工作目录。

        :param work_path: The work_path of this PublishableApp.
        :type work_path: str
        """
        self._work_path = work_path

    @property
    def icon_path(self):
        r"""Gets the icon_path of this PublishableApp.

        应用图标的路径。

        :return: The icon_path of this PublishableApp.
        :rtype: str
        """
        return self._icon_path

    @icon_path.setter
    def icon_path(self, icon_path):
        r"""Sets the icon_path of this PublishableApp.

        应用图标的路径。

        :param icon_path: The icon_path of this PublishableApp.
        :type icon_path: str
        """
        self._icon_path = icon_path

    @property
    def icon_index(self):
        r"""Gets the icon_index of this PublishableApp.

        应用图标的索引。

        :return: The icon_index of this PublishableApp.
        :rtype: int
        """
        return self._icon_index

    @icon_index.setter
    def icon_index(self, icon_index):
        r"""Sets the icon_index of this PublishableApp.

        应用图标的索引。

        :param icon_index: The icon_index of this PublishableApp.
        :type icon_index: int
        """
        self._icon_index = icon_index

    @property
    def description(self):
        r"""Gets the description of this PublishableApp.

        应用描述。

        :return: The description of this PublishableApp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishableApp.

        应用描述。

        :param description: The description of this PublishableApp.
        :type description: str
        """
        self._description = description

    @property
    def app_group_id(self):
        r"""Gets the app_group_id of this PublishableApp.

        应用组标识Id。

        :return: The app_group_id of this PublishableApp.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        r"""Sets the app_group_id of this PublishableApp.

        应用组标识Id。

        :param app_group_id: The app_group_id of this PublishableApp.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def state(self):
        r"""Gets the state of this PublishableApp.

        :return: The state of this PublishableApp.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this PublishableApp.

        :param state: The state of this PublishableApp.
        :type state: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        """
        self._state = state

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this PublishableApp.

        所在的租户ID。

        :return: The tenant_id of this PublishableApp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this PublishableApp.

        所在的租户ID。

        :param tenant_id: The tenant_id of this PublishableApp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def publish_at(self):
        r"""Gets the publish_at of this PublishableApp.

        发布时间。

        :return: The publish_at of this PublishableApp.
        :rtype: datetime
        """
        return self._publish_at

    @publish_at.setter
    def publish_at(self, publish_at):
        r"""Sets the publish_at of this PublishableApp.

        发布时间。

        :param publish_at: The publish_at of this PublishableApp.
        :type publish_at: datetime
        """
        self._publish_at = publish_at

    @property
    def source_type(self):
        r"""Gets the source_type of this PublishableApp.

        应用类型： - '1':系统内置应用 - '2':镜像应用 - '3':自定义应用

        :return: The source_type of this PublishableApp.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this PublishableApp.

        应用类型： - '1':系统内置应用 - '2':镜像应用 - '3':自定义应用

        :param source_type: The source_type of this PublishableApp.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def publisher(self):
        r"""Gets the publisher of this PublishableApp.

        应用发布者。

        :return: The publisher of this PublishableApp.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        r"""Sets the publisher of this PublishableApp.

        应用发布者。

        :param publisher: The publisher of this PublishableApp.
        :type publisher: str
        """
        self._publisher = publisher

    @property
    def icon_url(self):
        r"""Gets the icon_url of this PublishableApp.

        图标url。

        :return: The icon_url of this PublishableApp.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this PublishableApp.

        图标url。

        :param icon_url: The icon_url of this PublishableApp.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def publishable(self):
        r"""Gets the publishable of this PublishableApp.

        是否可发布应用： - true: 可发布。 - false: 不可发布。

        :return: The publishable of this PublishableApp.
        :rtype: bool
        """
        return self._publishable

    @publishable.setter
    def publishable(self, publishable):
        r"""Sets the publishable of this PublishableApp.

        是否可发布应用： - true: 可发布。 - false: 不可发布。

        :param publishable: The publishable of this PublishableApp.
        :type publishable: bool
        """
        self._publishable = publishable

    @property
    def sandbox_enable(self):
        r"""Gets the sandbox_enable of this PublishableApp.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。

        :return: The sandbox_enable of this PublishableApp.
        :rtype: bool
        """
        return self._sandbox_enable

    @sandbox_enable.setter
    def sandbox_enable(self, sandbox_enable):
        r"""Sets the sandbox_enable of this PublishableApp.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行。 - true: 表示以沙箱模式运行。

        :param sandbox_enable: The sandbox_enable of this PublishableApp.
        :type sandbox_enable: bool
        """
        self._sandbox_enable = sandbox_enable

    @property
    def source_image_ids(self):
        r"""Gets the source_image_ids of this PublishableApp.

        镜像ids。

        :return: The source_image_ids of this PublishableApp.
        :rtype: list[str]
        """
        return self._source_image_ids

    @source_image_ids.setter
    def source_image_ids(self, source_image_ids):
        r"""Sets the source_image_ids of this PublishableApp.

        镜像ids。

        :param source_image_ids: The source_image_ids of this PublishableApp.
        :type source_image_ids: list[str]
        """
        self._source_image_ids = source_image_ids

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
        if not isinstance(other, PublishableApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
