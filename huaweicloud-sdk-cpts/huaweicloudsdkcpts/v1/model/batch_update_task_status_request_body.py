# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateTaskStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'project_id': 'int',
        'task_id_list': 'list[int]',
        'cluster_id': 'int',
        'cluster_type': 'str',
        'without_package': 'int',
        'network_info': 'NetworkInfo',
        'status': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'project_id': 'project_id',
        'task_id_list': 'task_id_list',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'without_package': 'without_package',
        'network_info': 'network_info',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, type=None, project_id=None, task_id_list=None, cluster_id=None, cluster_type=None, without_package=None, network_info=None, status=None, enterprise_project_id=None):
        """BatchUpdateTaskStatusRequestBody

        The model defined in huaweicloud sdk

        :param type: 类型（0-旧版本任务；1-新版本任务）
        :type type: int
        :param project_id: 所属工程id
        :type project_id: int
        :param task_id_list: 任务id列表
        :type task_id_list: list[int]
        :param cluster_id: 资源组id
        :type cluster_id: int
        :param cluster_type: 资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）
        :type cluster_type: str
        :param without_package: 套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）
        :type without_package: int
        :param network_info: 
        :type network_info: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        :param status: 状态（9：启动任务；2：停止任务）
        :type status: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._type = None
        self._project_id = None
        self._task_id_list = None
        self._cluster_id = None
        self._cluster_type = None
        self._without_package = None
        self._network_info = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.project_id = project_id
        self.task_id_list = task_id_list
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        if without_package is not None:
            self.without_package = without_package
        if network_info is not None:
            self.network_info = network_info
        self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this BatchUpdateTaskStatusRequestBody.

        类型（0-旧版本任务；1-新版本任务）

        :return: The type of this BatchUpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchUpdateTaskStatusRequestBody.

        类型（0-旧版本任务；1-新版本任务）

        :param type: The type of this BatchUpdateTaskStatusRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def project_id(self):
        """Gets the project_id of this BatchUpdateTaskStatusRequestBody.

        所属工程id

        :return: The project_id of this BatchUpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchUpdateTaskStatusRequestBody.

        所属工程id

        :param project_id: The project_id of this BatchUpdateTaskStatusRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def task_id_list(self):
        """Gets the task_id_list of this BatchUpdateTaskStatusRequestBody.

        任务id列表

        :return: The task_id_list of this BatchUpdateTaskStatusRequestBody.
        :rtype: list[int]
        """
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, task_id_list):
        """Sets the task_id_list of this BatchUpdateTaskStatusRequestBody.

        任务id列表

        :param task_id_list: The task_id_list of this BatchUpdateTaskStatusRequestBody.
        :type task_id_list: list[int]
        """
        self._task_id_list = task_id_list

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BatchUpdateTaskStatusRequestBody.

        资源组id

        :return: The cluster_id of this BatchUpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BatchUpdateTaskStatusRequestBody.

        资源组id

        :param cluster_id: The cluster_id of this BatchUpdateTaskStatusRequestBody.
        :type cluster_id: int
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this BatchUpdateTaskStatusRequestBody.

        资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）

        :return: The cluster_type of this BatchUpdateTaskStatusRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this BatchUpdateTaskStatusRequestBody.

        资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）

        :param cluster_type: The cluster_type of this BatchUpdateTaskStatusRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def without_package(self):
        """Gets the without_package of this BatchUpdateTaskStatusRequestBody.

        套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）

        :return: The without_package of this BatchUpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._without_package

    @without_package.setter
    def without_package(self, without_package):
        """Sets the without_package of this BatchUpdateTaskStatusRequestBody.

        套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）

        :param without_package: The without_package of this BatchUpdateTaskStatusRequestBody.
        :type without_package: int
        """
        self._without_package = without_package

    @property
    def network_info(self):
        """Gets the network_info of this BatchUpdateTaskStatusRequestBody.

        :return: The network_info of this BatchUpdateTaskStatusRequestBody.
        :rtype: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        """Sets the network_info of this BatchUpdateTaskStatusRequestBody.

        :param network_info: The network_info of this BatchUpdateTaskStatusRequestBody.
        :type network_info: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        """
        self._network_info = network_info

    @property
    def status(self):
        """Gets the status of this BatchUpdateTaskStatusRequestBody.

        状态（9：启动任务；2：停止任务）

        :return: The status of this BatchUpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpdateTaskStatusRequestBody.

        状态（9：启动任务；2：停止任务）

        :param status: The status of this BatchUpdateTaskStatusRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BatchUpdateTaskStatusRequestBody.

        企业项目id

        :return: The enterprise_project_id of this BatchUpdateTaskStatusRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BatchUpdateTaskStatusRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this BatchUpdateTaskStatusRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, BatchUpdateTaskStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
