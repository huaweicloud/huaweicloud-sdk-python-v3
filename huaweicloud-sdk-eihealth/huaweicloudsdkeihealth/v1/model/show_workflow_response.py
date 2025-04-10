# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowResponse(SdkResponse):

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
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'timeout': 'int',
        'output_dir': 'str',
        'tasks': 'list[TaskDefinitionDto]',
        'app_snapshot_sign': 'dict(str, str)',
        'create_time': 'str',
        'update_time': 'str',
        'source_project_name': 'str',
        'source_resource_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels',
        'timeout': 'timeout',
        'output_dir': 'output_dir',
        'tasks': 'tasks',
        'app_snapshot_sign': 'app_snapshot_sign',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'source_project_name': 'source_project_name',
        'source_resource_id': 'source_resource_id'
    }

    def __init__(self, id=None, name=None, version=None, summary=None, description=None, labels=None, timeout=None, output_dir=None, tasks=None, app_snapshot_sign=None, create_time=None, update_time=None, source_project_name=None, source_resource_id=None):
        r"""ShowWorkflowResponse

        The model defined in huaweicloud sdk

        :param id: 流程id
        :type id: str
        :param name: 流程名称
        :type name: str
        :param version: 流程版本
        :type version: str
        :param summary: 流程简述
        :type summary: str
        :param description: 流程描述
        :type description: str
        :param labels: 流程标签
        :type labels: list[str]
        :param timeout: 超时时间
        :type timeout: int
        :param output_dir: 流程的输出路径
        :type output_dir: str
        :param tasks: 流程的子任务
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        :param app_snapshot_sign: 流程创建时刻的应用快照，当query填workflow_snapshot_sign有值;K为appId,V为sign
        :type app_snapshot_sign: dict(str, str)
        :param create_time: 流程的创建时间
        :type create_time: str
        :param update_time: 流程的更新时间
        :type update_time: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        """
        
        super(ShowWorkflowResponse, self).__init__()

        self._id = None
        self._name = None
        self._version = None
        self._summary = None
        self._description = None
        self._labels = None
        self._timeout = None
        self._output_dir = None
        self._tasks = None
        self._app_snapshot_sign = None
        self._create_time = None
        self._update_time = None
        self._source_project_name = None
        self._source_resource_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
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
        if app_snapshot_sign is not None:
            self.app_snapshot_sign = app_snapshot_sign
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id

    @property
    def id(self):
        r"""Gets the id of this ShowWorkflowResponse.

        流程id

        :return: The id of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowWorkflowResponse.

        流程id

        :param id: The id of this ShowWorkflowResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowWorkflowResponse.

        流程名称

        :return: The name of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowWorkflowResponse.

        流程名称

        :param name: The name of this ShowWorkflowResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ShowWorkflowResponse.

        流程版本

        :return: The version of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowWorkflowResponse.

        流程版本

        :param version: The version of this ShowWorkflowResponse.
        :type version: str
        """
        self._version = version

    @property
    def summary(self):
        r"""Gets the summary of this ShowWorkflowResponse.

        流程简述

        :return: The summary of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ShowWorkflowResponse.

        流程简述

        :param summary: The summary of this ShowWorkflowResponse.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        r"""Gets the description of this ShowWorkflowResponse.

        流程描述

        :return: The description of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowWorkflowResponse.

        流程描述

        :param description: The description of this ShowWorkflowResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this ShowWorkflowResponse.

        流程标签

        :return: The labels of this ShowWorkflowResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowWorkflowResponse.

        流程标签

        :param labels: The labels of this ShowWorkflowResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def timeout(self):
        r"""Gets the timeout of this ShowWorkflowResponse.

        超时时间

        :return: The timeout of this ShowWorkflowResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ShowWorkflowResponse.

        超时时间

        :param timeout: The timeout of this ShowWorkflowResponse.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        r"""Gets the output_dir of this ShowWorkflowResponse.

        流程的输出路径

        :return: The output_dir of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        r"""Sets the output_dir of this ShowWorkflowResponse.

        流程的输出路径

        :param output_dir: The output_dir of this ShowWorkflowResponse.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def tasks(self):
        r"""Gets the tasks of this ShowWorkflowResponse.

        流程的子任务

        :return: The tasks of this ShowWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ShowWorkflowResponse.

        流程的子任务

        :param tasks: The tasks of this ShowWorkflowResponse.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        """
        self._tasks = tasks

    @property
    def app_snapshot_sign(self):
        r"""Gets the app_snapshot_sign of this ShowWorkflowResponse.

        流程创建时刻的应用快照，当query填workflow_snapshot_sign有值;K为appId,V为sign

        :return: The app_snapshot_sign of this ShowWorkflowResponse.
        :rtype: dict(str, str)
        """
        return self._app_snapshot_sign

    @app_snapshot_sign.setter
    def app_snapshot_sign(self, app_snapshot_sign):
        r"""Sets the app_snapshot_sign of this ShowWorkflowResponse.

        流程创建时刻的应用快照，当query填workflow_snapshot_sign有值;K为appId,V为sign

        :param app_snapshot_sign: The app_snapshot_sign of this ShowWorkflowResponse.
        :type app_snapshot_sign: dict(str, str)
        """
        self._app_snapshot_sign = app_snapshot_sign

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowWorkflowResponse.

        流程的创建时间

        :return: The create_time of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowWorkflowResponse.

        流程的创建时间

        :param create_time: The create_time of this ShowWorkflowResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowWorkflowResponse.

        流程的更新时间

        :return: The update_time of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowWorkflowResponse.

        流程的更新时间

        :param update_time: The update_time of this ShowWorkflowResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def source_project_name(self):
        r"""Gets the source_project_name of this ShowWorkflowResponse.

        源项目名称

        :return: The source_project_name of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        r"""Sets the source_project_name of this ShowWorkflowResponse.

        源项目名称

        :param source_project_name: The source_project_name of this ShowWorkflowResponse.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_resource_id(self):
        r"""Gets the source_resource_id of this ShowWorkflowResponse.

        源资源id

        :return: The source_resource_id of this ShowWorkflowResponse.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        r"""Sets the source_resource_id of this ShowWorkflowResponse.

        源资源id

        :param source_resource_id: The source_resource_id of this ShowWorkflowResponse.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

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
        if not isinstance(other, ShowWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
