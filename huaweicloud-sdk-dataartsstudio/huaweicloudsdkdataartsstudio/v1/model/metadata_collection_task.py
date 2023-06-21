# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetadataCollectionTask:

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
        'description': 'str',
        'user_id': 'str',
        'create_time': 'str',
        'project_id': 'str',
        'dir_id': 'str',
        'schedule_config': 'SchedulerInfo',
        'parameter_config': 'list[CustomMetadata]',
        'update_time': 'str',
        'user_name': 'str',
        'path': 'str',
        'last_run_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'next_run_time': 'str',
        'duty_person': 'str',
        'update_type': 'str',
        'data_source_type': 'str',
        'task_config': 'object',
        'data_source_workspace_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'user_id': 'user_id',
        'create_time': 'create_time',
        'project_id': 'project_id',
        'dir_id': 'dir_id',
        'schedule_config': 'schedule_config',
        'parameter_config': 'parameter_config',
        'update_time': 'update_time',
        'user_name': 'user_name',
        'path': 'path',
        'last_run_time': 'last_run_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'next_run_time': 'next_run_time',
        'duty_person': 'duty_person',
        'update_type': 'update_type',
        'data_source_type': 'data_source_type',
        'task_config': 'task_config',
        'data_source_workspace_id': 'data_source_workspace_id'
    }

    def __init__(self, id=None, name=None, description=None, user_id=None, create_time=None, project_id=None, dir_id=None, schedule_config=None, parameter_config=None, update_time=None, user_name=None, path=None, last_run_time=None, start_time=None, end_time=None, next_run_time=None, duty_person=None, update_type=None, data_source_type=None, task_config=None, data_source_workspace_id=None):
        """MetadataCollectionTask

        The model defined in huaweicloud sdk

        :param id: 任务id
        :type id: str
        :param name: 任务名称
        :type name: str
        :param description: 任务描述
        :type description: str
        :param user_id: 用户id
        :type user_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param project_id: 产品id
        :type project_id: str
        :param dir_id: 目录id
        :type dir_id: str
        :param schedule_config: 
        :type schedule_config: :class:`huaweicloudsdkdataartsstudio.v1.SchedulerInfo`
        :param parameter_config: 自定义元数据信息
        :type parameter_config: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomMetadata`]
        :param update_time: 修改时间
        :type update_time: str
        :param user_name: 用户名
        :type user_name: str
        :param path: 路径
        :type path: str
        :param last_run_time: 最后一次执行时间
        :type last_run_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param next_run_time: 下一次执行时间
        :type next_run_time: str
        :param duty_person: 责任人
        :type duty_person: str
        :param update_type: 修改类型
        :type update_type: str
        :param data_source_type: 数据来源类型
        :type data_source_type: str
        :param task_config: 任务信息Map&lt;String, Object&gt;
        :type task_config: object
        :param data_source_workspace_id: 数据来源工作空间id
        :type data_source_workspace_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._user_id = None
        self._create_time = None
        self._project_id = None
        self._dir_id = None
        self._schedule_config = None
        self._parameter_config = None
        self._update_time = None
        self._user_name = None
        self._path = None
        self._last_run_time = None
        self._start_time = None
        self._end_time = None
        self._next_run_time = None
        self._duty_person = None
        self._update_type = None
        self._data_source_type = None
        self._task_config = None
        self._data_source_workspace_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.user_id = user_id
        if create_time is not None:
            self.create_time = create_time
        if project_id is not None:
            self.project_id = project_id
        self.dir_id = dir_id
        self.schedule_config = schedule_config
        if parameter_config is not None:
            self.parameter_config = parameter_config
        if update_time is not None:
            self.update_time = update_time
        if user_name is not None:
            self.user_name = user_name
        if path is not None:
            self.path = path
        if last_run_time is not None:
            self.last_run_time = last_run_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if next_run_time is not None:
            self.next_run_time = next_run_time
        if duty_person is not None:
            self.duty_person = duty_person
        if update_type is not None:
            self.update_type = update_type
        self.data_source_type = data_source_type
        self.task_config = task_config
        if data_source_workspace_id is not None:
            self.data_source_workspace_id = data_source_workspace_id

    @property
    def id(self):
        """Gets the id of this MetadataCollectionTask.

        任务id

        :return: The id of this MetadataCollectionTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetadataCollectionTask.

        任务id

        :param id: The id of this MetadataCollectionTask.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MetadataCollectionTask.

        任务名称

        :return: The name of this MetadataCollectionTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetadataCollectionTask.

        任务名称

        :param name: The name of this MetadataCollectionTask.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this MetadataCollectionTask.

        任务描述

        :return: The description of this MetadataCollectionTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetadataCollectionTask.

        任务描述

        :param description: The description of this MetadataCollectionTask.
        :type description: str
        """
        self._description = description

    @property
    def user_id(self):
        """Gets the user_id of this MetadataCollectionTask.

        用户id

        :return: The user_id of this MetadataCollectionTask.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MetadataCollectionTask.

        用户id

        :param user_id: The user_id of this MetadataCollectionTask.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def create_time(self):
        """Gets the create_time of this MetadataCollectionTask.

        创建时间

        :return: The create_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this MetadataCollectionTask.

        创建时间

        :param create_time: The create_time of this MetadataCollectionTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def project_id(self):
        """Gets the project_id of this MetadataCollectionTask.

        产品id

        :return: The project_id of this MetadataCollectionTask.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MetadataCollectionTask.

        产品id

        :param project_id: The project_id of this MetadataCollectionTask.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dir_id(self):
        """Gets the dir_id of this MetadataCollectionTask.

        目录id

        :return: The dir_id of this MetadataCollectionTask.
        :rtype: str
        """
        return self._dir_id

    @dir_id.setter
    def dir_id(self, dir_id):
        """Sets the dir_id of this MetadataCollectionTask.

        目录id

        :param dir_id: The dir_id of this MetadataCollectionTask.
        :type dir_id: str
        """
        self._dir_id = dir_id

    @property
    def schedule_config(self):
        """Gets the schedule_config of this MetadataCollectionTask.

        :return: The schedule_config of this MetadataCollectionTask.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SchedulerInfo`
        """
        return self._schedule_config

    @schedule_config.setter
    def schedule_config(self, schedule_config):
        """Sets the schedule_config of this MetadataCollectionTask.

        :param schedule_config: The schedule_config of this MetadataCollectionTask.
        :type schedule_config: :class:`huaweicloudsdkdataartsstudio.v1.SchedulerInfo`
        """
        self._schedule_config = schedule_config

    @property
    def parameter_config(self):
        """Gets the parameter_config of this MetadataCollectionTask.

        自定义元数据信息

        :return: The parameter_config of this MetadataCollectionTask.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomMetadata`]
        """
        return self._parameter_config

    @parameter_config.setter
    def parameter_config(self, parameter_config):
        """Sets the parameter_config of this MetadataCollectionTask.

        自定义元数据信息

        :param parameter_config: The parameter_config of this MetadataCollectionTask.
        :type parameter_config: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomMetadata`]
        """
        self._parameter_config = parameter_config

    @property
    def update_time(self):
        """Gets the update_time of this MetadataCollectionTask.

        修改时间

        :return: The update_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this MetadataCollectionTask.

        修改时间

        :param update_time: The update_time of this MetadataCollectionTask.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def user_name(self):
        """Gets the user_name of this MetadataCollectionTask.

        用户名

        :return: The user_name of this MetadataCollectionTask.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this MetadataCollectionTask.

        用户名

        :param user_name: The user_name of this MetadataCollectionTask.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def path(self):
        """Gets the path of this MetadataCollectionTask.

        路径

        :return: The path of this MetadataCollectionTask.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MetadataCollectionTask.

        路径

        :param path: The path of this MetadataCollectionTask.
        :type path: str
        """
        self._path = path

    @property
    def last_run_time(self):
        """Gets the last_run_time of this MetadataCollectionTask.

        最后一次执行时间

        :return: The last_run_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        """Sets the last_run_time of this MetadataCollectionTask.

        最后一次执行时间

        :param last_run_time: The last_run_time of this MetadataCollectionTask.
        :type last_run_time: str
        """
        self._last_run_time = last_run_time

    @property
    def start_time(self):
        """Gets the start_time of this MetadataCollectionTask.

        开始时间

        :return: The start_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MetadataCollectionTask.

        开始时间

        :param start_time: The start_time of this MetadataCollectionTask.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this MetadataCollectionTask.

        结束时间

        :return: The end_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this MetadataCollectionTask.

        结束时间

        :param end_time: The end_time of this MetadataCollectionTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def next_run_time(self):
        """Gets the next_run_time of this MetadataCollectionTask.

        下一次执行时间

        :return: The next_run_time of this MetadataCollectionTask.
        :rtype: str
        """
        return self._next_run_time

    @next_run_time.setter
    def next_run_time(self, next_run_time):
        """Sets the next_run_time of this MetadataCollectionTask.

        下一次执行时间

        :param next_run_time: The next_run_time of this MetadataCollectionTask.
        :type next_run_time: str
        """
        self._next_run_time = next_run_time

    @property
    def duty_person(self):
        """Gets the duty_person of this MetadataCollectionTask.

        责任人

        :return: The duty_person of this MetadataCollectionTask.
        :rtype: str
        """
        return self._duty_person

    @duty_person.setter
    def duty_person(self, duty_person):
        """Sets the duty_person of this MetadataCollectionTask.

        责任人

        :param duty_person: The duty_person of this MetadataCollectionTask.
        :type duty_person: str
        """
        self._duty_person = duty_person

    @property
    def update_type(self):
        """Gets the update_type of this MetadataCollectionTask.

        修改类型

        :return: The update_type of this MetadataCollectionTask.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """Sets the update_type of this MetadataCollectionTask.

        修改类型

        :param update_type: The update_type of this MetadataCollectionTask.
        :type update_type: str
        """
        self._update_type = update_type

    @property
    def data_source_type(self):
        """Gets the data_source_type of this MetadataCollectionTask.

        数据来源类型

        :return: The data_source_type of this MetadataCollectionTask.
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this MetadataCollectionTask.

        数据来源类型

        :param data_source_type: The data_source_type of this MetadataCollectionTask.
        :type data_source_type: str
        """
        self._data_source_type = data_source_type

    @property
    def task_config(self):
        """Gets the task_config of this MetadataCollectionTask.

        任务信息Map<String, Object>

        :return: The task_config of this MetadataCollectionTask.
        :rtype: object
        """
        return self._task_config

    @task_config.setter
    def task_config(self, task_config):
        """Sets the task_config of this MetadataCollectionTask.

        任务信息Map<String, Object>

        :param task_config: The task_config of this MetadataCollectionTask.
        :type task_config: object
        """
        self._task_config = task_config

    @property
    def data_source_workspace_id(self):
        """Gets the data_source_workspace_id of this MetadataCollectionTask.

        数据来源工作空间id

        :return: The data_source_workspace_id of this MetadataCollectionTask.
        :rtype: str
        """
        return self._data_source_workspace_id

    @data_source_workspace_id.setter
    def data_source_workspace_id(self, data_source_workspace_id):
        """Sets the data_source_workspace_id of this MetadataCollectionTask.

        数据来源工作空间id

        :param data_source_workspace_id: The data_source_workspace_id of this MetadataCollectionTask.
        :type data_source_workspace_id: str
        """
        self._data_source_workspace_id = data_source_workspace_id

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
        if not isinstance(other, MetadataCollectionTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
