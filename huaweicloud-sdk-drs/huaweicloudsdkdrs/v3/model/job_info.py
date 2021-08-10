# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfo:


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
        'status': 'str',
        'description': 'str',
        'create_time': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'billing_tag': 'bool',
        'job_direction': 'str',
        'db_use_type': 'str',
        'task_type': 'str',
        'children': 'list[ChildrenJobInfo]',
        'node_new_framework': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'billing_tag': 'billing_tag',
        'job_direction': 'job_direction',
        'db_use_type': 'db_use_type',
        'task_type': 'task_type',
        'children': 'children',
        'node_new_framework': 'node_newFramework'
    }

    def __init__(self, id=None, name=None, status=None, description=None, create_time=None, engine_type=None, net_type=None, billing_tag=None, job_direction=None, db_use_type=None, task_type=None, children=None, node_new_framework=None):
        """JobInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._status = None
        self._description = None
        self._create_time = None
        self._engine_type = None
        self._net_type = None
        self._billing_tag = None
        self._job_direction = None
        self._db_use_type = None
        self._task_type = None
        self._children = None
        self._node_new_framework = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.create_time = create_time
        self.engine_type = engine_type
        self.net_type = net_type
        self.billing_tag = billing_tag
        self.job_direction = job_direction
        self.db_use_type = db_use_type
        self.task_type = task_type
        if children is not None:
            self.children = children
        self.node_new_framework = node_new_framework

    @property
    def id(self):
        """Gets the id of this JobInfo.

        任务id

        :return: The id of this JobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobInfo.

        任务id

        :param id: The id of this JobInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobInfo.

        任务名称

        :return: The name of this JobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobInfo.

        任务名称

        :param name: The name of this JobInfo.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this JobInfo.

        任务状态

        :return: The status of this JobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobInfo.

        任务状态

        :param status: The status of this JobInfo.
        :type: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this JobInfo.

        任务描述

        :return: The description of this JobInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobInfo.

        任务描述

        :param description: The description of this JobInfo.
        :type: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this JobInfo.

        任务创建时间

        :return: The create_time of this JobInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobInfo.

        任务创建时间

        :param create_time: The create_time of this JobInfo.
        :type: str
        """
        self._create_time = create_time

    @property
    def engine_type(self):
        """Gets the engine_type of this JobInfo.

        引擎类型

        :return: The engine_type of this JobInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this JobInfo.

        引擎类型

        :param engine_type: The engine_type of this JobInfo.
        :type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        """Gets the net_type of this JobInfo.

        网络类型

        :return: The net_type of this JobInfo.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this JobInfo.

        网络类型

        :param net_type: The net_type of this JobInfo.
        :type: str
        """
        self._net_type = net_type

    @property
    def billing_tag(self):
        """Gets the billing_tag of this JobInfo.

        计费字段

        :return: The billing_tag of this JobInfo.
        :rtype: bool
        """
        return self._billing_tag

    @billing_tag.setter
    def billing_tag(self, billing_tag):
        """Sets the billing_tag of this JobInfo.

        计费字段

        :param billing_tag: The billing_tag of this JobInfo.
        :type: bool
        """
        self._billing_tag = billing_tag

    @property
    def job_direction(self):
        """Gets the job_direction of this JobInfo.

        迁移方向

        :return: The job_direction of this JobInfo.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this JobInfo.

        迁移方向

        :param job_direction: The job_direction of this JobInfo.
        :type: str
        """
        self._job_direction = job_direction

    @property
    def db_use_type(self):
        """Gets the db_use_type of this JobInfo.

        迁移场景

        :return: The db_use_type of this JobInfo.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this JobInfo.

        迁移场景

        :param db_use_type: The db_use_type of this JobInfo.
        :type: str
        """
        self._db_use_type = db_use_type

    @property
    def task_type(self):
        """Gets the task_type of this JobInfo.

        迁移模式

        :return: The task_type of this JobInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this JobInfo.

        迁移模式

        :param task_type: The task_type of this JobInfo.
        :type: str
        """
        self._task_type = task_type

    @property
    def children(self):
        """Gets the children of this JobInfo.

        子任务信息体

        :return: The children of this JobInfo.
        :rtype: list[ChildrenJobInfo]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this JobInfo.

        子任务信息体

        :param children: The children of this JobInfo.
        :type: list[ChildrenJobInfo]
        """
        self._children = children

    @property
    def node_new_framework(self):
        """Gets the node_new_framework of this JobInfo.

        是否新框架

        :return: The node_new_framework of this JobInfo.
        :rtype: bool
        """
        return self._node_new_framework

    @node_new_framework.setter
    def node_new_framework(self, node_new_framework):
        """Sets the node_new_framework of this JobInfo.

        是否新框架

        :param node_new_framework: The node_new_framework of this JobInfo.
        :type: bool
        """
        self._node_new_framework = node_new_framework

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
