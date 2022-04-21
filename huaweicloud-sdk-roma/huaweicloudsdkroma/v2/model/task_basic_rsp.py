# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'status': 'str',
        'project_id': 'str',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'source_datasource_name': 'str',
        'target_datasource_name': 'str',
        'source_app_id': 'str',
        'target_app_id': 'str',
        'source_app_name': 'str',
        'target_app_name': 'str',
        'created_date': 'int',
        'last_modified_date': 'int',
        'description': 'str',
        'task_tag': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'status': 'status',
        'project_id': 'project_id',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'source_datasource_name': 'source_datasource_name',
        'target_datasource_name': 'target_datasource_name',
        'source_app_id': 'source_app_id',
        'target_app_id': 'target_app_id',
        'source_app_name': 'source_app_name',
        'target_app_name': 'target_app_name',
        'created_date': 'created_date',
        'last_modified_date': 'last_modified_date',
        'description': 'description',
        'task_tag': 'task_tag',
        'created_by': 'created_by'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, status=None, project_id=None, source_datasource_id=None, target_datasource_id=None, source_datasource_name=None, target_datasource_name=None, source_app_id=None, target_app_id=None, source_app_name=None, target_app_name=None, created_date=None, last_modified_date=None, description=None, task_tag=None, created_by=None):
        """TaskBasicRsp

        The model defined in huaweicloud sdk

        :param task_id: 任务ID, 可为空
        :type task_id: str
        :param task_name: 任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符
        :type task_name: str
        :param task_type: 任务类型 - realtime (实时) - timing (定时)
        :type task_type: str
        :param status: 任务状态, - stop (0停止\\未启动) - running (1运行中)
        :type status: str
        :param project_id: 项目ID
        :type project_id: str
        :param source_datasource_id: 源端数据源ID
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID
        :type target_datasource_id: str
        :param source_datasource_name: 源端数据源的名称
        :type source_datasource_name: str
        :param target_datasource_name: 目标端数据源的名称
        :type target_datasource_name: str
        :param source_app_id: 源端数据源所属集成应用ID
        :type source_app_id: str
        :param target_app_id: 目标端数据源所属集成应用ID
        :type target_app_id: str
        :param source_app_name: 源端数据源所属集成应用名称
        :type source_app_name: str
        :param target_app_name: 目标端数据源所属集成应用名称
        :type target_app_name: str
        :param created_date: 创建时间
        :type created_date: int
        :param last_modified_date: 最近一次的修改时间
        :type last_modified_date: int
        :param description: 描述信息
        :type description: str
        :param task_tag: 任务标签,只能包含字母、数字、中划线、下划线
        :type task_tag: str
        :param created_by: 任务的创建者
        :type created_by: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._status = None
        self._project_id = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._source_datasource_name = None
        self._target_datasource_name = None
        self._source_app_id = None
        self._target_app_id = None
        self._source_app_name = None
        self._target_app_name = None
        self._created_date = None
        self._last_modified_date = None
        self._description = None
        self._task_tag = None
        self._created_by = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if project_id is not None:
            self.project_id = project_id
        if source_datasource_id is not None:
            self.source_datasource_id = source_datasource_id
        if target_datasource_id is not None:
            self.target_datasource_id = target_datasource_id
        if source_datasource_name is not None:
            self.source_datasource_name = source_datasource_name
        if target_datasource_name is not None:
            self.target_datasource_name = target_datasource_name
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if target_app_id is not None:
            self.target_app_id = target_app_id
        if source_app_name is not None:
            self.source_app_name = source_app_name
        if target_app_name is not None:
            self.target_app_name = target_app_name
        if created_date is not None:
            self.created_date = created_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if description is not None:
            self.description = description
        if task_tag is not None:
            self.task_tag = task_tag
        if created_by is not None:
            self.created_by = created_by

    @property
    def task_id(self):
        """Gets the task_id of this TaskBasicRsp.

        任务ID, 可为空

        :return: The task_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskBasicRsp.

        任务ID, 可为空

        :param task_id: The task_id of this TaskBasicRsp.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this TaskBasicRsp.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :return: The task_name of this TaskBasicRsp.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskBasicRsp.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :param task_name: The task_name of this TaskBasicRsp.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this TaskBasicRsp.

        任务类型 - realtime (实时) - timing (定时)

        :return: The task_type of this TaskBasicRsp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskBasicRsp.

        任务类型 - realtime (实时) - timing (定时)

        :param task_type: The task_type of this TaskBasicRsp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this TaskBasicRsp.

        任务状态, - stop (0停止\\未启动) - running (1运行中)

        :return: The status of this TaskBasicRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskBasicRsp.

        任务状态, - stop (0停止\\未启动) - running (1运行中)

        :param status: The status of this TaskBasicRsp.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        """Gets the project_id of this TaskBasicRsp.

        项目ID

        :return: The project_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TaskBasicRsp.

        项目ID

        :param project_id: The project_id of this TaskBasicRsp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def source_datasource_id(self):
        """Gets the source_datasource_id of this TaskBasicRsp.

        源端数据源ID

        :return: The source_datasource_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        """Sets the source_datasource_id of this TaskBasicRsp.

        源端数据源ID

        :param source_datasource_id: The source_datasource_id of this TaskBasicRsp.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        """Gets the target_datasource_id of this TaskBasicRsp.

        目标端数据源ID

        :return: The target_datasource_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        """Sets the target_datasource_id of this TaskBasicRsp.

        目标端数据源ID

        :param target_datasource_id: The target_datasource_id of this TaskBasicRsp.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def source_datasource_name(self):
        """Gets the source_datasource_name of this TaskBasicRsp.

        源端数据源的名称

        :return: The source_datasource_name of this TaskBasicRsp.
        :rtype: str
        """
        return self._source_datasource_name

    @source_datasource_name.setter
    def source_datasource_name(self, source_datasource_name):
        """Sets the source_datasource_name of this TaskBasicRsp.

        源端数据源的名称

        :param source_datasource_name: The source_datasource_name of this TaskBasicRsp.
        :type source_datasource_name: str
        """
        self._source_datasource_name = source_datasource_name

    @property
    def target_datasource_name(self):
        """Gets the target_datasource_name of this TaskBasicRsp.

        目标端数据源的名称

        :return: The target_datasource_name of this TaskBasicRsp.
        :rtype: str
        """
        return self._target_datasource_name

    @target_datasource_name.setter
    def target_datasource_name(self, target_datasource_name):
        """Sets the target_datasource_name of this TaskBasicRsp.

        目标端数据源的名称

        :param target_datasource_name: The target_datasource_name of this TaskBasicRsp.
        :type target_datasource_name: str
        """
        self._target_datasource_name = target_datasource_name

    @property
    def source_app_id(self):
        """Gets the source_app_id of this TaskBasicRsp.

        源端数据源所属集成应用ID

        :return: The source_app_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this TaskBasicRsp.

        源端数据源所属集成应用ID

        :param source_app_id: The source_app_id of this TaskBasicRsp.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def target_app_id(self):
        """Gets the target_app_id of this TaskBasicRsp.

        目标端数据源所属集成应用ID

        :return: The target_app_id of this TaskBasicRsp.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        """Sets the target_app_id of this TaskBasicRsp.

        目标端数据源所属集成应用ID

        :param target_app_id: The target_app_id of this TaskBasicRsp.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

    @property
    def source_app_name(self):
        """Gets the source_app_name of this TaskBasicRsp.

        源端数据源所属集成应用名称

        :return: The source_app_name of this TaskBasicRsp.
        :rtype: str
        """
        return self._source_app_name

    @source_app_name.setter
    def source_app_name(self, source_app_name):
        """Sets the source_app_name of this TaskBasicRsp.

        源端数据源所属集成应用名称

        :param source_app_name: The source_app_name of this TaskBasicRsp.
        :type source_app_name: str
        """
        self._source_app_name = source_app_name

    @property
    def target_app_name(self):
        """Gets the target_app_name of this TaskBasicRsp.

        目标端数据源所属集成应用名称

        :return: The target_app_name of this TaskBasicRsp.
        :rtype: str
        """
        return self._target_app_name

    @target_app_name.setter
    def target_app_name(self, target_app_name):
        """Sets the target_app_name of this TaskBasicRsp.

        目标端数据源所属集成应用名称

        :param target_app_name: The target_app_name of this TaskBasicRsp.
        :type target_app_name: str
        """
        self._target_app_name = target_app_name

    @property
    def created_date(self):
        """Gets the created_date of this TaskBasicRsp.

        创建时间

        :return: The created_date of this TaskBasicRsp.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this TaskBasicRsp.

        创建时间

        :param created_date: The created_date of this TaskBasicRsp.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this TaskBasicRsp.

        最近一次的修改时间

        :return: The last_modified_date of this TaskBasicRsp.
        :rtype: int
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this TaskBasicRsp.

        最近一次的修改时间

        :param last_modified_date: The last_modified_date of this TaskBasicRsp.
        :type last_modified_date: int
        """
        self._last_modified_date = last_modified_date

    @property
    def description(self):
        """Gets the description of this TaskBasicRsp.

        描述信息

        :return: The description of this TaskBasicRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskBasicRsp.

        描述信息

        :param description: The description of this TaskBasicRsp.
        :type description: str
        """
        self._description = description

    @property
    def task_tag(self):
        """Gets the task_tag of this TaskBasicRsp.

        任务标签,只能包含字母、数字、中划线、下划线

        :return: The task_tag of this TaskBasicRsp.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this TaskBasicRsp.

        任务标签,只能包含字母、数字、中划线、下划线

        :param task_tag: The task_tag of this TaskBasicRsp.
        :type task_tag: str
        """
        self._task_tag = task_tag

    @property
    def created_by(self):
        """Gets the created_by of this TaskBasicRsp.

        任务的创建者

        :return: The created_by of this TaskBasicRsp.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TaskBasicRsp.

        任务的创建者

        :param created_by: The created_by of this TaskBasicRsp.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, TaskBasicRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
