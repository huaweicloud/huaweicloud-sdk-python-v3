# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_id': 'str',
        'branch_name': 'str',
        'create_by': 'str',
        'iteration_uri': 'str',
        'project_id': 'str',
        'protocols': 'list[str]',
        'service_id': 'str',
        'stage': 'int',
        'stage_name': 'str',
        'task_id': 'str',
        'version_uri': 'str'
    }

    attribute_map = {
        'branch_id': 'branch_id',
        'branch_name': 'branch_name',
        'create_by': 'create_by',
        'iteration_uri': 'iteration_uri',
        'project_id': 'project_id',
        'protocols': 'protocols',
        'service_id': 'service_id',
        'stage': 'stage',
        'stage_name': 'stage_name',
        'task_id': 'task_id',
        'version_uri': 'version_uri'
    }

    def __init__(self, branch_id=None, branch_name=None, create_by=None, iteration_uri=None, project_id=None, protocols=None, service_id=None, stage=None, stage_name=None, task_id=None, version_uri=None):
        r"""TaskBasicAttribute

        The model defined in huaweicloud sdk

        :param branch_id: 分支ID
        :type branch_id: str
        :param branch_name: 分支名
        :type branch_name: str
        :param create_by: 创建人的工号
        :type create_by: str
        :param iteration_uri: 迭代url
        :type iteration_uri: str
        :param project_id: 工程id
        :type project_id: str
        :param protocols: 协议
        :type protocols: list[str]
        :param service_id: 服务id
        :type service_id: str
        :param stage: 阶段
        :type stage: int
        :param stage_name: 阶段名称
        :type stage_name: str
        :param task_id: 任务id
        :type task_id: str
        :param version_uri: 版本uri
        :type version_uri: str
        """
        
        

        self._branch_id = None
        self._branch_name = None
        self._create_by = None
        self._iteration_uri = None
        self._project_id = None
        self._protocols = None
        self._service_id = None
        self._stage = None
        self._stage_name = None
        self._task_id = None
        self._version_uri = None
        self.discriminator = None

        if branch_id is not None:
            self.branch_id = branch_id
        if branch_name is not None:
            self.branch_name = branch_name
        if create_by is not None:
            self.create_by = create_by
        if iteration_uri is not None:
            self.iteration_uri = iteration_uri
        if project_id is not None:
            self.project_id = project_id
        if protocols is not None:
            self.protocols = protocols
        if service_id is not None:
            self.service_id = service_id
        if stage is not None:
            self.stage = stage
        if stage_name is not None:
            self.stage_name = stage_name
        if task_id is not None:
            self.task_id = task_id
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def branch_id(self):
        r"""Gets the branch_id of this TaskBasicAttribute.

        分支ID

        :return: The branch_id of this TaskBasicAttribute.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        r"""Sets the branch_id of this TaskBasicAttribute.

        分支ID

        :param branch_id: The branch_id of this TaskBasicAttribute.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this TaskBasicAttribute.

        分支名

        :return: The branch_name of this TaskBasicAttribute.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this TaskBasicAttribute.

        分支名

        :param branch_name: The branch_name of this TaskBasicAttribute.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def create_by(self):
        r"""Gets the create_by of this TaskBasicAttribute.

        创建人的工号

        :return: The create_by of this TaskBasicAttribute.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this TaskBasicAttribute.

        创建人的工号

        :param create_by: The create_by of this TaskBasicAttribute.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def iteration_uri(self):
        r"""Gets the iteration_uri of this TaskBasicAttribute.

        迭代url

        :return: The iteration_uri of this TaskBasicAttribute.
        :rtype: str
        """
        return self._iteration_uri

    @iteration_uri.setter
    def iteration_uri(self, iteration_uri):
        r"""Sets the iteration_uri of this TaskBasicAttribute.

        迭代url

        :param iteration_uri: The iteration_uri of this TaskBasicAttribute.
        :type iteration_uri: str
        """
        self._iteration_uri = iteration_uri

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskBasicAttribute.

        工程id

        :return: The project_id of this TaskBasicAttribute.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskBasicAttribute.

        工程id

        :param project_id: The project_id of this TaskBasicAttribute.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocols(self):
        r"""Gets the protocols of this TaskBasicAttribute.

        协议

        :return: The protocols of this TaskBasicAttribute.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        r"""Sets the protocols of this TaskBasicAttribute.

        协议

        :param protocols: The protocols of this TaskBasicAttribute.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def service_id(self):
        r"""Gets the service_id of this TaskBasicAttribute.

        服务id

        :return: The service_id of this TaskBasicAttribute.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this TaskBasicAttribute.

        服务id

        :param service_id: The service_id of this TaskBasicAttribute.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def stage(self):
        r"""Gets the stage of this TaskBasicAttribute.

        阶段

        :return: The stage of this TaskBasicAttribute.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this TaskBasicAttribute.

        阶段

        :param stage: The stage of this TaskBasicAttribute.
        :type stage: int
        """
        self._stage = stage

    @property
    def stage_name(self):
        r"""Gets the stage_name of this TaskBasicAttribute.

        阶段名称

        :return: The stage_name of this TaskBasicAttribute.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this TaskBasicAttribute.

        阶段名称

        :param stage_name: The stage_name of this TaskBasicAttribute.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskBasicAttribute.

        任务id

        :return: The task_id of this TaskBasicAttribute.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskBasicAttribute.

        任务id

        :param task_id: The task_id of this TaskBasicAttribute.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TaskBasicAttribute.

        版本uri

        :return: The version_uri of this TaskBasicAttribute.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TaskBasicAttribute.

        版本uri

        :param version_uri: The version_uri of this TaskBasicAttribute.
        :type version_uri: str
        """
        self._version_uri = version_uri

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
        if not isinstance(other, TaskBasicAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
