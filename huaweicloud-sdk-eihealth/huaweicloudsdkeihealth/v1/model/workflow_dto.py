# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowDto:

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
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'timeout': 'int',
        'output_dir': 'str',
        'tasks': 'list[TaskDto]'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels',
        'timeout': 'timeout',
        'output_dir': 'output_dir',
        'tasks': 'tasks'
    }

    def __init__(self, name=None, version=None, summary=None, description=None, labels=None, timeout=None, output_dir=None, tasks=None):
        """WorkflowDto

        The model defined in huaweicloud sdk

        :param name: 流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。
        :type name: str
        :param version: 流程版本，取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新流程时，流程版本不支持修改。
        :type version: str
        :param summary: 流程简述 取值范围[0,128]
        :type summary: str
        :param description: 流程描述 取值范围[0,65535]，后续支持markdown文本
        :type description: str
        :param labels: 流程标签，取值范围[0,5]，单个标签最大长度32字符，仅包含小写字母或数字或大写字母
        :type labels: list[str]
        :param timeout: 流程超时时间，取值范围[1,144000]，单位分钟，默认1440
        :type timeout: int
        :param output_dir: 流程的当前工作目录，默认为根目录，用户可显示指定;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?&lt;\&quot;&gt;|。
        :type output_dir: str
        :param tasks: 流程中子任务的描述信息，子任务数量取值范围:[1,64]
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDto`]
        """
        
        

        self._name = None
        self._version = None
        self._summary = None
        self._description = None
        self._labels = None
        self._timeout = None
        self._output_dir = None
        self._tasks = None
        self.discriminator = None

        self.name = name
        self.version = version
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if timeout is not None:
            self.timeout = timeout
        if output_dir is not None:
            self.output_dir = output_dir
        if tasks is not None:
            self.tasks = tasks

    @property
    def name(self):
        """Gets the name of this WorkflowDto.

        流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。

        :return: The name of this WorkflowDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowDto.

        流程名称，取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。更新流程时，流程名称不支持修改。

        :param name: The name of this WorkflowDto.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this WorkflowDto.

        流程版本，取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新流程时，流程版本不支持修改。

        :return: The version of this WorkflowDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkflowDto.

        流程版本，取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。更新流程时，流程版本不支持修改。

        :param version: The version of this WorkflowDto.
        :type version: str
        """
        self._version = version

    @property
    def summary(self):
        """Gets the summary of this WorkflowDto.

        流程简述 取值范围[0,128]

        :return: The summary of this WorkflowDto.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this WorkflowDto.

        流程简述 取值范围[0,128]

        :param summary: The summary of this WorkflowDto.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this WorkflowDto.

        流程描述 取值范围[0,65535]，后续支持markdown文本

        :return: The description of this WorkflowDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowDto.

        流程描述 取值范围[0,65535]，后续支持markdown文本

        :param description: The description of this WorkflowDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this WorkflowDto.

        流程标签，取值范围[0,5]，单个标签最大长度32字符，仅包含小写字母或数字或大写字母

        :return: The labels of this WorkflowDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this WorkflowDto.

        流程标签，取值范围[0,5]，单个标签最大长度32字符，仅包含小写字母或数字或大写字母

        :param labels: The labels of this WorkflowDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def timeout(self):
        """Gets the timeout of this WorkflowDto.

        流程超时时间，取值范围[1,144000]，单位分钟，默认1440

        :return: The timeout of this WorkflowDto.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this WorkflowDto.

        流程超时时间，取值范围[1,144000]，单位分钟，默认1440

        :param timeout: The timeout of this WorkflowDto.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        """Gets the output_dir of this WorkflowDto.

        流程的当前工作目录，默认为根目录，用户可显示指定;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?<\">|。

        :return: The output_dir of this WorkflowDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this WorkflowDto.

        流程的当前工作目录，默认为根目录，用户可显示指定;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?<\">|。

        :param output_dir: The output_dir of this WorkflowDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def tasks(self):
        """Gets the tasks of this WorkflowDto.

        流程中子任务的描述信息，子任务数量取值范围:[1,64]

        :return: The tasks of this WorkflowDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this WorkflowDto.

        流程中子任务的描述信息，子任务数量取值范围:[1,64]

        :param tasks: The tasks of this WorkflowDto.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDto`]
        """
        self._tasks = tasks

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
        if not isinstance(other, WorkflowDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
