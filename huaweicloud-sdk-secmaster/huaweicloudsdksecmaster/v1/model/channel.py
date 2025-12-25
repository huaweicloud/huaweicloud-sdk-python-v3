# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Channel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'channel_id': 'str',
        'config_status': 'str',
        'create_by': 'str',
        'create_by_user': 'str',
        'description': 'str',
        'error_type': 'str',
        'health_status': 'str',
        'input_id': 'str',
        'input_name': 'str',
        'install_status': 'str',
        'install_time': 'int',
        'node_refer_count': 'int',
        'operation_status': 'str',
        'output_id': 'str',
        'output_name': 'str',
        'parser_id': 'str',
        'parser_name': 'str',
        'read_write': 'ReadWrite',
        'title': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'action': 'action',
        'channel_id': 'channel_id',
        'config_status': 'config_status',
        'create_by': 'create_by',
        'create_by_user': 'create_by_user',
        'description': 'description',
        'error_type': 'error_type',
        'health_status': 'health_status',
        'input_id': 'input_id',
        'input_name': 'input_name',
        'install_status': 'install_status',
        'install_time': 'install_time',
        'node_refer_count': 'node_refer_count',
        'operation_status': 'operation_status',
        'output_id': 'output_id',
        'output_name': 'output_name',
        'parser_id': 'parser_id',
        'parser_name': 'parser_name',
        'read_write': 'read_write',
        'title': 'title',
        'update_time': 'update_time'
    }

    def __init__(self, action=None, channel_id=None, config_status=None, create_by=None, create_by_user=None, description=None, error_type=None, health_status=None, input_id=None, input_name=None, install_status=None, install_time=None, node_refer_count=None, operation_status=None, output_id=None, output_name=None, parser_id=None, parser_name=None, read_write=None, title=None, update_time=None):
        r"""Channel

        The model defined in huaweicloud sdk

        :param action: **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及
        :type action: str
        :param channel_id: UUID
        :type channel_id: str
        :param config_status: **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及
        :type config_status: str
        :param create_by: Iam用户ID
        :type create_by: str
        :param create_by_user: Iam用户名称
        :type create_by_user: str
        :param description: 描述信息
        :type description: str
        :param error_type: **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及
        :type error_type: str
        :param health_status: **参数解释**: 采集通道监控状态 - SUCCESS_PART 部分运行 - SUCCESS_ALL 全部运行 - SUCCESS_NO 没有运行  **约束限制** 不涉及 **取值范围**: - SUCCESS_PART - SUCCESS_ALL - SUCCESS_NO  **默认值** 不涉及
        :type health_status: str
        :param input_id: UUID
        :type input_id: str
        :param input_name: 所属租户名称
        :type input_name: str
        :param install_status: **参数解释**: 采集通道下发 - READY 等待下发 - ALL_SUCCESS 全部成功 - PARTIAL_SUCCESS 部分成功 - EXCEPTION 异常  **约束限制** 不涉及 **取值范围**: - READY - ALL_SUCCESS - PARTIAL_SUCCESS - EXCEPTION  **默认值** 不涉及
        :type install_status: str
        :param install_time: 毫秒时间戳
        :type install_time: int
        :param node_refer_count: 关联的节点个数
        :type node_refer_count: int
        :param operation_status: **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及
        :type operation_status: str
        :param output_id: UUID
        :type output_id: str
        :param output_name: 所属租户名称
        :type output_name: str
        :param parser_id: UUID
        :type parser_id: str
        :param parser_name: 所属租户名称
        :type parser_name: str
        :param read_write: 
        :type read_write: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        :param title: 相关标题
        :type title: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        """
        
        

        self._action = None
        self._channel_id = None
        self._config_status = None
        self._create_by = None
        self._create_by_user = None
        self._description = None
        self._error_type = None
        self._health_status = None
        self._input_id = None
        self._input_name = None
        self._install_status = None
        self._install_time = None
        self._node_refer_count = None
        self._operation_status = None
        self._output_id = None
        self._output_name = None
        self._parser_id = None
        self._parser_name = None
        self._read_write = None
        self._title = None
        self._update_time = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if channel_id is not None:
            self.channel_id = channel_id
        if config_status is not None:
            self.config_status = config_status
        if create_by is not None:
            self.create_by = create_by
        if create_by_user is not None:
            self.create_by_user = create_by_user
        if description is not None:
            self.description = description
        if error_type is not None:
            self.error_type = error_type
        if health_status is not None:
            self.health_status = health_status
        if input_id is not None:
            self.input_id = input_id
        if input_name is not None:
            self.input_name = input_name
        if install_status is not None:
            self.install_status = install_status
        if install_time is not None:
            self.install_time = install_time
        if node_refer_count is not None:
            self.node_refer_count = node_refer_count
        if operation_status is not None:
            self.operation_status = operation_status
        if output_id is not None:
            self.output_id = output_id
        if output_name is not None:
            self.output_name = output_name
        if parser_id is not None:
            self.parser_id = parser_id
        if parser_name is not None:
            self.parser_name = parser_name
        if read_write is not None:
            self.read_write = read_write
        if title is not None:
            self.title = title
        if update_time is not None:
            self.update_time = update_time

    @property
    def action(self):
        r"""Gets the action of this Channel.

        **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及

        :return: The action of this Channel.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this Channel.

        **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及

        :param action: The action of this Channel.
        :type action: str
        """
        self._action = action

    @property
    def channel_id(self):
        r"""Gets the channel_id of this Channel.

        UUID

        :return: The channel_id of this Channel.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this Channel.

        UUID

        :param channel_id: The channel_id of this Channel.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def config_status(self):
        r"""Gets the config_status of this Channel.

        **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及

        :return: The config_status of this Channel.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this Channel.

        **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及

        :param config_status: The config_status of this Channel.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def create_by(self):
        r"""Gets the create_by of this Channel.

        Iam用户ID

        :return: The create_by of this Channel.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this Channel.

        Iam用户ID

        :param create_by: The create_by of this Channel.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_by_user(self):
        r"""Gets the create_by_user of this Channel.

        Iam用户名称

        :return: The create_by_user of this Channel.
        :rtype: str
        """
        return self._create_by_user

    @create_by_user.setter
    def create_by_user(self, create_by_user):
        r"""Sets the create_by_user of this Channel.

        Iam用户名称

        :param create_by_user: The create_by_user of this Channel.
        :type create_by_user: str
        """
        self._create_by_user = create_by_user

    @property
    def description(self):
        r"""Gets the description of this Channel.

        描述信息

        :return: The description of this Channel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Channel.

        描述信息

        :param description: The description of this Channel.
        :type description: str
        """
        self._description = description

    @property
    def error_type(self):
        r"""Gets the error_type of this Channel.

        **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及

        :return: The error_type of this Channel.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        r"""Sets the error_type of this Channel.

        **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及

        :param error_type: The error_type of this Channel.
        :type error_type: str
        """
        self._error_type = error_type

    @property
    def health_status(self):
        r"""Gets the health_status of this Channel.

        **参数解释**: 采集通道监控状态 - SUCCESS_PART 部分运行 - SUCCESS_ALL 全部运行 - SUCCESS_NO 没有运行  **约束限制** 不涉及 **取值范围**: - SUCCESS_PART - SUCCESS_ALL - SUCCESS_NO  **默认值** 不涉及

        :return: The health_status of this Channel.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this Channel.

        **参数解释**: 采集通道监控状态 - SUCCESS_PART 部分运行 - SUCCESS_ALL 全部运行 - SUCCESS_NO 没有运行  **约束限制** 不涉及 **取值范围**: - SUCCESS_PART - SUCCESS_ALL - SUCCESS_NO  **默认值** 不涉及

        :param health_status: The health_status of this Channel.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def input_id(self):
        r"""Gets the input_id of this Channel.

        UUID

        :return: The input_id of this Channel.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        r"""Sets the input_id of this Channel.

        UUID

        :param input_id: The input_id of this Channel.
        :type input_id: str
        """
        self._input_id = input_id

    @property
    def input_name(self):
        r"""Gets the input_name of this Channel.

        所属租户名称

        :return: The input_name of this Channel.
        :rtype: str
        """
        return self._input_name

    @input_name.setter
    def input_name(self, input_name):
        r"""Sets the input_name of this Channel.

        所属租户名称

        :param input_name: The input_name of this Channel.
        :type input_name: str
        """
        self._input_name = input_name

    @property
    def install_status(self):
        r"""Gets the install_status of this Channel.

        **参数解释**: 采集通道下发 - READY 等待下发 - ALL_SUCCESS 全部成功 - PARTIAL_SUCCESS 部分成功 - EXCEPTION 异常  **约束限制** 不涉及 **取值范围**: - READY - ALL_SUCCESS - PARTIAL_SUCCESS - EXCEPTION  **默认值** 不涉及

        :return: The install_status of this Channel.
        :rtype: str
        """
        return self._install_status

    @install_status.setter
    def install_status(self, install_status):
        r"""Sets the install_status of this Channel.

        **参数解释**: 采集通道下发 - READY 等待下发 - ALL_SUCCESS 全部成功 - PARTIAL_SUCCESS 部分成功 - EXCEPTION 异常  **约束限制** 不涉及 **取值范围**: - READY - ALL_SUCCESS - PARTIAL_SUCCESS - EXCEPTION  **默认值** 不涉及

        :param install_status: The install_status of this Channel.
        :type install_status: str
        """
        self._install_status = install_status

    @property
    def install_time(self):
        r"""Gets the install_time of this Channel.

        毫秒时间戳

        :return: The install_time of this Channel.
        :rtype: int
        """
        return self._install_time

    @install_time.setter
    def install_time(self, install_time):
        r"""Sets the install_time of this Channel.

        毫秒时间戳

        :param install_time: The install_time of this Channel.
        :type install_time: int
        """
        self._install_time = install_time

    @property
    def node_refer_count(self):
        r"""Gets the node_refer_count of this Channel.

        关联的节点个数

        :return: The node_refer_count of this Channel.
        :rtype: int
        """
        return self._node_refer_count

    @node_refer_count.setter
    def node_refer_count(self, node_refer_count):
        r"""Sets the node_refer_count of this Channel.

        关联的节点个数

        :param node_refer_count: The node_refer_count of this Channel.
        :type node_refer_count: int
        """
        self._node_refer_count = node_refer_count

    @property
    def operation_status(self):
        r"""Gets the operation_status of this Channel.

        **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及

        :return: The operation_status of this Channel.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this Channel.

        **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及

        :param operation_status: The operation_status of this Channel.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def output_id(self):
        r"""Gets the output_id of this Channel.

        UUID

        :return: The output_id of this Channel.
        :rtype: str
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        r"""Sets the output_id of this Channel.

        UUID

        :param output_id: The output_id of this Channel.
        :type output_id: str
        """
        self._output_id = output_id

    @property
    def output_name(self):
        r"""Gets the output_name of this Channel.

        所属租户名称

        :return: The output_name of this Channel.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        r"""Sets the output_name of this Channel.

        所属租户名称

        :param output_name: The output_name of this Channel.
        :type output_name: str
        """
        self._output_name = output_name

    @property
    def parser_id(self):
        r"""Gets the parser_id of this Channel.

        UUID

        :return: The parser_id of this Channel.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this Channel.

        UUID

        :param parser_id: The parser_id of this Channel.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def parser_name(self):
        r"""Gets the parser_name of this Channel.

        所属租户名称

        :return: The parser_name of this Channel.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        r"""Sets the parser_name of this Channel.

        所属租户名称

        :param parser_name: The parser_name of this Channel.
        :type parser_name: str
        """
        self._parser_name = parser_name

    @property
    def read_write(self):
        r"""Gets the read_write of this Channel.

        :return: The read_write of this Channel.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        """
        return self._read_write

    @read_write.setter
    def read_write(self, read_write):
        r"""Sets the read_write of this Channel.

        :param read_write: The read_write of this Channel.
        :type read_write: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        """
        self._read_write = read_write

    @property
    def title(self):
        r"""Gets the title of this Channel.

        相关标题

        :return: The title of this Channel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this Channel.

        相关标题

        :param title: The title of this Channel.
        :type title: str
        """
        self._title = title

    @property
    def update_time(self):
        r"""Gets the update_time of this Channel.

        毫秒时间戳

        :return: The update_time of this Channel.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Channel.

        毫秒时间戳

        :param update_time: The update_time of this Channel.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
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
        if not isinstance(other, Channel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
