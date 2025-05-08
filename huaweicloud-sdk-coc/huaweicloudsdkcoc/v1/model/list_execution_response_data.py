# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecutionResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_id': 'str',
        'document_name': 'str',
        'document_id': 'str',
        'document_version_id': 'str',
        'document_version': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'update_time': 'int',
        'creator': 'str',
        'status': 'str',
        'description': 'str',
        'parameters': 'list[ListExecutionResponseParameters]',
        'sys_tags': 'list[CreateDocumentRequestBodyTags]',
        'tags': 'list[CreateDocumentRequestBodyTags]',
        'type': 'str',
        'target_parameter_name': 'str',
        'targets': 'list[Target]'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'document_name': 'document_name',
        'document_id': 'document_id',
        'document_version_id': 'document_version_id',
        'document_version': 'document_version',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'update_time': 'update_time',
        'creator': 'creator',
        'status': 'status',
        'description': 'description',
        'parameters': 'parameters',
        'sys_tags': 'sys_tags',
        'tags': 'tags',
        'type': 'type',
        'target_parameter_name': 'target_parameter_name',
        'targets': 'targets'
    }

    def __init__(self, execution_id=None, document_name=None, document_id=None, document_version_id=None, document_version=None, start_time=None, end_time=None, update_time=None, creator=None, status=None, description=None, parameters=None, sys_tags=None, tags=None, type=None, target_parameter_name=None, targets=None):
        r"""ListExecutionResponseData

        The model defined in huaweicloud sdk

        :param execution_id: 工单唯一id
        :type execution_id: str
        :param document_name: 作业名称
        :type document_name: str
        :param document_id: 作业id
        :type document_id: str
        :param document_version_id: 作业版本id
        :type document_version_id: str
        :param document_version: 作业版本号
        :type document_version: str
        :param start_time: 工单执行开始时间
        :type start_time: int
        :param end_time: 工单执行结束时间
        :type end_time: int
        :param update_time: 工单更新时间
        :type update_time: int
        :param creator: 工单创建时间
        :type creator: str
        :param status: 工单状态
        :type status: str
        :param description: 工单执行描述
        :type description: str
        :param parameters: 工单执行全局参数
        :type parameters: list[:class:`huaweicloudsdkcoc.v1.ListExecutionResponseParameters`]
        :param sys_tags: 系统标签列表
        :type sys_tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        :param tags: 自定义标签列表
        :type tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        :param type: 工单类型：BATCH、RATE_CONTROL、NORMAL
        :type type: str
        :param target_parameter_name: 速率模式执行指定参数
        :type target_parameter_name: str
        :param targets: 速率模式执行指定元素
        :type targets: list[:class:`huaweicloudsdkcoc.v1.Target`]
        """
        
        

        self._execution_id = None
        self._document_name = None
        self._document_id = None
        self._document_version_id = None
        self._document_version = None
        self._start_time = None
        self._end_time = None
        self._update_time = None
        self._creator = None
        self._status = None
        self._description = None
        self._parameters = None
        self._sys_tags = None
        self._tags = None
        self._type = None
        self._target_parameter_name = None
        self._targets = None
        self.discriminator = None

        if execution_id is not None:
            self.execution_id = execution_id
        if document_name is not None:
            self.document_name = document_name
        if document_id is not None:
            self.document_id = document_id
        if document_version_id is not None:
            self.document_version_id = document_version_id
        if document_version is not None:
            self.document_version = document_version
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if parameters is not None:
            self.parameters = parameters
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if target_parameter_name is not None:
            self.target_parameter_name = target_parameter_name
        if targets is not None:
            self.targets = targets

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ListExecutionResponseData.

        工单唯一id

        :return: The execution_id of this ListExecutionResponseData.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ListExecutionResponseData.

        工单唯一id

        :param execution_id: The execution_id of this ListExecutionResponseData.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def document_name(self):
        r"""Gets the document_name of this ListExecutionResponseData.

        作业名称

        :return: The document_name of this ListExecutionResponseData.
        :rtype: str
        """
        return self._document_name

    @document_name.setter
    def document_name(self, document_name):
        r"""Sets the document_name of this ListExecutionResponseData.

        作业名称

        :param document_name: The document_name of this ListExecutionResponseData.
        :type document_name: str
        """
        self._document_name = document_name

    @property
    def document_id(self):
        r"""Gets the document_id of this ListExecutionResponseData.

        作业id

        :return: The document_id of this ListExecutionResponseData.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this ListExecutionResponseData.

        作业id

        :param document_id: The document_id of this ListExecutionResponseData.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def document_version_id(self):
        r"""Gets the document_version_id of this ListExecutionResponseData.

        作业版本id

        :return: The document_version_id of this ListExecutionResponseData.
        :rtype: str
        """
        return self._document_version_id

    @document_version_id.setter
    def document_version_id(self, document_version_id):
        r"""Sets the document_version_id of this ListExecutionResponseData.

        作业版本id

        :param document_version_id: The document_version_id of this ListExecutionResponseData.
        :type document_version_id: str
        """
        self._document_version_id = document_version_id

    @property
    def document_version(self):
        r"""Gets the document_version of this ListExecutionResponseData.

        作业版本号

        :return: The document_version of this ListExecutionResponseData.
        :rtype: str
        """
        return self._document_version

    @document_version.setter
    def document_version(self, document_version):
        r"""Sets the document_version of this ListExecutionResponseData.

        作业版本号

        :param document_version: The document_version of this ListExecutionResponseData.
        :type document_version: str
        """
        self._document_version = document_version

    @property
    def start_time(self):
        r"""Gets the start_time of this ListExecutionResponseData.

        工单执行开始时间

        :return: The start_time of this ListExecutionResponseData.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListExecutionResponseData.

        工单执行开始时间

        :param start_time: The start_time of this ListExecutionResponseData.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListExecutionResponseData.

        工单执行结束时间

        :return: The end_time of this ListExecutionResponseData.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListExecutionResponseData.

        工单执行结束时间

        :param end_time: The end_time of this ListExecutionResponseData.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListExecutionResponseData.

        工单更新时间

        :return: The update_time of this ListExecutionResponseData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListExecutionResponseData.

        工单更新时间

        :param update_time: The update_time of this ListExecutionResponseData.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def creator(self):
        r"""Gets the creator of this ListExecutionResponseData.

        工单创建时间

        :return: The creator of this ListExecutionResponseData.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListExecutionResponseData.

        工单创建时间

        :param creator: The creator of this ListExecutionResponseData.
        :type creator: str
        """
        self._creator = creator

    @property
    def status(self):
        r"""Gets the status of this ListExecutionResponseData.

        工单状态

        :return: The status of this ListExecutionResponseData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListExecutionResponseData.

        工单状态

        :param status: The status of this ListExecutionResponseData.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ListExecutionResponseData.

        工单执行描述

        :return: The description of this ListExecutionResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListExecutionResponseData.

        工单执行描述

        :param description: The description of this ListExecutionResponseData.
        :type description: str
        """
        self._description = description

    @property
    def parameters(self):
        r"""Gets the parameters of this ListExecutionResponseData.

        工单执行全局参数

        :return: The parameters of this ListExecutionResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ListExecutionResponseParameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ListExecutionResponseData.

        工单执行全局参数

        :param parameters: The parameters of this ListExecutionResponseData.
        :type parameters: list[:class:`huaweicloudsdkcoc.v1.ListExecutionResponseParameters`]
        """
        self._parameters = parameters

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListExecutionResponseData.

        系统标签列表

        :return: The sys_tags of this ListExecutionResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListExecutionResponseData.

        系统标签列表

        :param sys_tags: The sys_tags of this ListExecutionResponseData.
        :type sys_tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        self._sys_tags = sys_tags

    @property
    def tags(self):
        r"""Gets the tags of this ListExecutionResponseData.

        自定义标签列表

        :return: The tags of this ListExecutionResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListExecutionResponseData.

        自定义标签列表

        :param tags: The tags of this ListExecutionResponseData.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.CreateDocumentRequestBodyTags`]
        """
        self._tags = tags

    @property
    def type(self):
        r"""Gets the type of this ListExecutionResponseData.

        工单类型：BATCH、RATE_CONTROL、NORMAL

        :return: The type of this ListExecutionResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListExecutionResponseData.

        工单类型：BATCH、RATE_CONTROL、NORMAL

        :param type: The type of this ListExecutionResponseData.
        :type type: str
        """
        self._type = type

    @property
    def target_parameter_name(self):
        r"""Gets the target_parameter_name of this ListExecutionResponseData.

        速率模式执行指定参数

        :return: The target_parameter_name of this ListExecutionResponseData.
        :rtype: str
        """
        return self._target_parameter_name

    @target_parameter_name.setter
    def target_parameter_name(self, target_parameter_name):
        r"""Sets the target_parameter_name of this ListExecutionResponseData.

        速率模式执行指定参数

        :param target_parameter_name: The target_parameter_name of this ListExecutionResponseData.
        :type target_parameter_name: str
        """
        self._target_parameter_name = target_parameter_name

    @property
    def targets(self):
        r"""Gets the targets of this ListExecutionResponseData.

        速率模式执行指定元素

        :return: The targets of this ListExecutionResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this ListExecutionResponseData.

        速率模式执行指定元素

        :param targets: The targets of this ListExecutionResponseData.
        :type targets: list[:class:`huaweicloudsdkcoc.v1.Target`]
        """
        self._targets = targets

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
        if not isinstance(other, ListExecutionResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
