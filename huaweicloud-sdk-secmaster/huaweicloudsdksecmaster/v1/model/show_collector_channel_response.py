# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCollectorChannelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_by': 'str',
        'description': 'str',
        'error': 'str',
        'group_id': 'str',
        'input': 'list[ShowModuleVo]',
        'nodes': 'list[NodeVo]',
        'operation_status': 'str',
        'output': 'list[ShowModuleVo]',
        'parser_id': 'str',
        'parser_name': 'str',
        'title': 'str'
    }

    attribute_map = {
        'create_by': 'create_by',
        'description': 'description',
        'error': 'error',
        'group_id': 'group_id',
        'input': 'input',
        'nodes': 'nodes',
        'operation_status': 'operation_status',
        'output': 'output',
        'parser_id': 'parser_id',
        'parser_name': 'parser_name',
        'title': 'title'
    }

    def __init__(self, create_by=None, description=None, error=None, group_id=None, input=None, nodes=None, operation_status=None, output=None, parser_id=None, parser_name=None, title=None):
        r"""ShowCollectorChannelResponse

        The model defined in huaweicloud sdk

        :param create_by: Iam用户ID
        :type create_by: str
        :param description: 描述信息
        :type description: str
        :param error: **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及
        :type error: str
        :param group_id: UUID
        :type group_id: str
        :param input: 相关描述信息
        :type input: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        :param nodes: 相关描述信息
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        :param operation_status: **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及
        :type operation_status: str
        :param output: 相关描述信息
        :type output: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        :param parser_id: UUID
        :type parser_id: str
        :param parser_name: 所属租户名称
        :type parser_name: str
        :param title: 相关标题
        :type title: str
        """
        
        super().__init__()

        self._create_by = None
        self._description = None
        self._error = None
        self._group_id = None
        self._input = None
        self._nodes = None
        self._operation_status = None
        self._output = None
        self._parser_id = None
        self._parser_name = None
        self._title = None
        self.discriminator = None

        if create_by is not None:
            self.create_by = create_by
        if description is not None:
            self.description = description
        if error is not None:
            self.error = error
        if group_id is not None:
            self.group_id = group_id
        if input is not None:
            self.input = input
        if nodes is not None:
            self.nodes = nodes
        if operation_status is not None:
            self.operation_status = operation_status
        if output is not None:
            self.output = output
        if parser_id is not None:
            self.parser_id = parser_id
        if parser_name is not None:
            self.parser_name = parser_name
        if title is not None:
            self.title = title

    @property
    def create_by(self):
        r"""Gets the create_by of this ShowCollectorChannelResponse.

        Iam用户ID

        :return: The create_by of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ShowCollectorChannelResponse.

        Iam用户ID

        :param create_by: The create_by of this ShowCollectorChannelResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def description(self):
        r"""Gets the description of this ShowCollectorChannelResponse.

        描述信息

        :return: The description of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCollectorChannelResponse.

        描述信息

        :param description: The description of this ShowCollectorChannelResponse.
        :type description: str
        """
        self._description = description

    @property
    def error(self):
        r"""Gets the error of this ShowCollectorChannelResponse.

        **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及

        :return: The error of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowCollectorChannelResponse.

        **参数解释**: 采集通道失败类型 - SUCCESS 成功 - FILE_UPLOAD_ERROR 文件上传失败 - FILE_COPY_ERROR 文件复制失败 - FILE_ZIP_ERROR 文件压缩失败 - SALT_EXECUTE_ERROR Salt执行出错  **约束限制** 不涉及 **取值范围**: - SUCCESS - FILE_UPLOAD_ERROR - FILE_COPY_ERROR - FILE_ZIP_ERROR - SALT_EXECUTE_ERROR  **默认值** 不涉及

        :param error: The error of this ShowCollectorChannelResponse.
        :type error: str
        """
        self._error = error

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowCollectorChannelResponse.

        UUID

        :return: The group_id of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowCollectorChannelResponse.

        UUID

        :param group_id: The group_id of this ShowCollectorChannelResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def input(self):
        r"""Gets the input of this ShowCollectorChannelResponse.

        相关描述信息

        :return: The input of this ShowCollectorChannelResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ShowCollectorChannelResponse.

        相关描述信息

        :param input: The input of this ShowCollectorChannelResponse.
        :type input: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        self._input = input

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowCollectorChannelResponse.

        相关描述信息

        :return: The nodes of this ShowCollectorChannelResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowCollectorChannelResponse.

        相关描述信息

        :param nodes: The nodes of this ShowCollectorChannelResponse.
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        """
        self._nodes = nodes

    @property
    def operation_status(self):
        r"""Gets the operation_status of this ShowCollectorChannelResponse.

        **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及

        :return: The operation_status of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this ShowCollectorChannelResponse.

        **参数解释**: 采集通道部署的进度 - READY 等待部署 - START 开始部署 - SUCCESS 部署成功 - FAIL 部署失败  **约束限制** 不涉及 **取值范围**: - READY - START - SUCCESS - FAIL  **默认值** 不涉及

        :param operation_status: The operation_status of this ShowCollectorChannelResponse.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def output(self):
        r"""Gets the output of this ShowCollectorChannelResponse.

        相关描述信息

        :return: The output of this ShowCollectorChannelResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ShowCollectorChannelResponse.

        相关描述信息

        :param output: The output of this ShowCollectorChannelResponse.
        :type output: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        self._output = output

    @property
    def parser_id(self):
        r"""Gets the parser_id of this ShowCollectorChannelResponse.

        UUID

        :return: The parser_id of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this ShowCollectorChannelResponse.

        UUID

        :param parser_id: The parser_id of this ShowCollectorChannelResponse.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def parser_name(self):
        r"""Gets the parser_name of this ShowCollectorChannelResponse.

        所属租户名称

        :return: The parser_name of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        r"""Sets the parser_name of this ShowCollectorChannelResponse.

        所属租户名称

        :param parser_name: The parser_name of this ShowCollectorChannelResponse.
        :type parser_name: str
        """
        self._parser_name = parser_name

    @property
    def title(self):
        r"""Gets the title of this ShowCollectorChannelResponse.

        相关标题

        :return: The title of this ShowCollectorChannelResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowCollectorChannelResponse.

        相关标题

        :param title: The title of this ShowCollectorChannelResponse.
        :type title: str
        """
        self._title = title

    def to_dict(self):
        import warnings
        warnings.warn("ShowCollectorChannelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCollectorChannelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
