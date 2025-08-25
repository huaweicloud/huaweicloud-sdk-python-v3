# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCcspClusterResponse(SdkResponse):

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
        'project_id': 'str',
        'domain_id': 'str',
        'task_details': 'list[object]',
        'ccsp_id': 'str',
        'distributed_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'service_type': 'str',
        'type': 'str',
        'instance_num': 'int',
        'status': 'str',
        'progress_info': 'str',
        'vsm_num': 'int',
        'create_time': 'int',
        'shared_ccsp': 'bool',
        'enterprise_project_id': 'str',
        'az': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'task_details': 'task_details',
        'ccsp_id': 'ccsp_id',
        'distributed_type': 'distributed_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'service_type': 'service_type',
        'type': 'type',
        'instance_num': 'instance_num',
        'status': 'status',
        'progress_info': 'progress_info',
        'vsm_num': 'vsm_num',
        'create_time': 'create_time',
        'shared_ccsp': 'shared_ccsp',
        'enterprise_project_id': 'enterprise_project_id',
        'az': 'az'
    }

    def __init__(self, task_id=None, project_id=None, domain_id=None, task_details=None, ccsp_id=None, distributed_type=None, cluster_id=None, cluster_name=None, service_type=None, type=None, instance_num=None, status=None, progress_info=None, vsm_num=None, create_time=None, shared_ccsp=None, enterprise_project_id=None, az=None):
        r"""ShowCcspClusterResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param task_details: 任务详情
        :type task_details: list[object]
        :param ccsp_id: ccsp集群id
        :type ccsp_id: str
        :param distributed_type: 分布类型
        :type distributed_type: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param service_type: 集群所属的服务
        :type service_type: str
        :param type: 集群的类型： - **SHARED** : 应用共享； - **EXCLUSIVE** : 应用独享
        :type type: str
        :param instance_num: 集群中包含的服务实例数量
        :type instance_num: int
        :param status: 集群状态
        :type status: str
        :param progress_info: 进度信息
        :type progress_info: str
        :param vsm_num: 集群使用VSM集群的vsm实例数量
        :type vsm_num: int
        :param create_time: 集群的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        :param shared_ccsp: 是否共享ccsp
        :type shared_ccsp: bool
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param az: az
        :type az: str
        """
        
        super(ShowCcspClusterResponse, self).__init__()

        self._task_id = None
        self._project_id = None
        self._domain_id = None
        self._task_details = None
        self._ccsp_id = None
        self._distributed_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._service_type = None
        self._type = None
        self._instance_num = None
        self._status = None
        self._progress_info = None
        self._vsm_num = None
        self._create_time = None
        self._shared_ccsp = None
        self._enterprise_project_id = None
        self._az = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if task_details is not None:
            self.task_details = task_details
        if ccsp_id is not None:
            self.ccsp_id = ccsp_id
        if distributed_type is not None:
            self.distributed_type = distributed_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if service_type is not None:
            self.service_type = service_type
        if type is not None:
            self.type = type
        if instance_num is not None:
            self.instance_num = instance_num
        if status is not None:
            self.status = status
        if progress_info is not None:
            self.progress_info = progress_info
        if vsm_num is not None:
            self.vsm_num = vsm_num
        if create_time is not None:
            self.create_time = create_time
        if shared_ccsp is not None:
            self.shared_ccsp = shared_ccsp
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if az is not None:
            self.az = az

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowCcspClusterResponse.

        任务ID

        :return: The task_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowCcspClusterResponse.

        任务ID

        :param task_id: The task_id of this ShowCcspClusterResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowCcspClusterResponse.

        项目ID

        :return: The project_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowCcspClusterResponse.

        项目ID

        :param project_id: The project_id of this ShowCcspClusterResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowCcspClusterResponse.

        账号ID

        :return: The domain_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowCcspClusterResponse.

        账号ID

        :param domain_id: The domain_id of this ShowCcspClusterResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def task_details(self):
        r"""Gets the task_details of this ShowCcspClusterResponse.

        任务详情

        :return: The task_details of this ShowCcspClusterResponse.
        :rtype: list[object]
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        r"""Sets the task_details of this ShowCcspClusterResponse.

        任务详情

        :param task_details: The task_details of this ShowCcspClusterResponse.
        :type task_details: list[object]
        """
        self._task_details = task_details

    @property
    def ccsp_id(self):
        r"""Gets the ccsp_id of this ShowCcspClusterResponse.

        ccsp集群id

        :return: The ccsp_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._ccsp_id

    @ccsp_id.setter
    def ccsp_id(self, ccsp_id):
        r"""Sets the ccsp_id of this ShowCcspClusterResponse.

        ccsp集群id

        :param ccsp_id: The ccsp_id of this ShowCcspClusterResponse.
        :type ccsp_id: str
        """
        self._ccsp_id = ccsp_id

    @property
    def distributed_type(self):
        r"""Gets the distributed_type of this ShowCcspClusterResponse.

        分布类型

        :return: The distributed_type of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._distributed_type

    @distributed_type.setter
    def distributed_type(self, distributed_type):
        r"""Sets the distributed_type of this ShowCcspClusterResponse.

        分布类型

        :param distributed_type: The distributed_type of this ShowCcspClusterResponse.
        :type distributed_type: str
        """
        self._distributed_type = distributed_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowCcspClusterResponse.

        集群ID

        :return: The cluster_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowCcspClusterResponse.

        集群ID

        :param cluster_id: The cluster_id of this ShowCcspClusterResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowCcspClusterResponse.

        集群名称

        :return: The cluster_name of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowCcspClusterResponse.

        集群名称

        :param cluster_name: The cluster_name of this ShowCcspClusterResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def service_type(self):
        r"""Gets the service_type of this ShowCcspClusterResponse.

        集群所属的服务

        :return: The service_type of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ShowCcspClusterResponse.

        集群所属的服务

        :param service_type: The service_type of this ShowCcspClusterResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def type(self):
        r"""Gets the type of this ShowCcspClusterResponse.

        集群的类型： - **SHARED** : 应用共享； - **EXCLUSIVE** : 应用独享

        :return: The type of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowCcspClusterResponse.

        集群的类型： - **SHARED** : 应用共享； - **EXCLUSIVE** : 应用独享

        :param type: The type of this ShowCcspClusterResponse.
        :type type: str
        """
        self._type = type

    @property
    def instance_num(self):
        r"""Gets the instance_num of this ShowCcspClusterResponse.

        集群中包含的服务实例数量

        :return: The instance_num of this ShowCcspClusterResponse.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this ShowCcspClusterResponse.

        集群中包含的服务实例数量

        :param instance_num: The instance_num of this ShowCcspClusterResponse.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def status(self):
        r"""Gets the status of this ShowCcspClusterResponse.

        集群状态

        :return: The status of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCcspClusterResponse.

        集群状态

        :param status: The status of this ShowCcspClusterResponse.
        :type status: str
        """
        self._status = status

    @property
    def progress_info(self):
        r"""Gets the progress_info of this ShowCcspClusterResponse.

        进度信息

        :return: The progress_info of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._progress_info

    @progress_info.setter
    def progress_info(self, progress_info):
        r"""Sets the progress_info of this ShowCcspClusterResponse.

        进度信息

        :param progress_info: The progress_info of this ShowCcspClusterResponse.
        :type progress_info: str
        """
        self._progress_info = progress_info

    @property
    def vsm_num(self):
        r"""Gets the vsm_num of this ShowCcspClusterResponse.

        集群使用VSM集群的vsm实例数量

        :return: The vsm_num of this ShowCcspClusterResponse.
        :rtype: int
        """
        return self._vsm_num

    @vsm_num.setter
    def vsm_num(self, vsm_num):
        r"""Sets the vsm_num of this ShowCcspClusterResponse.

        集群使用VSM集群的vsm实例数量

        :param vsm_num: The vsm_num of this ShowCcspClusterResponse.
        :type vsm_num: int
        """
        self._vsm_num = vsm_num

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowCcspClusterResponse.

        集群的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this ShowCcspClusterResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowCcspClusterResponse.

        集群的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this ShowCcspClusterResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def shared_ccsp(self):
        r"""Gets the shared_ccsp of this ShowCcspClusterResponse.

        是否共享ccsp

        :return: The shared_ccsp of this ShowCcspClusterResponse.
        :rtype: bool
        """
        return self._shared_ccsp

    @shared_ccsp.setter
    def shared_ccsp(self, shared_ccsp):
        r"""Sets the shared_ccsp of this ShowCcspClusterResponse.

        是否共享ccsp

        :param shared_ccsp: The shared_ccsp of this ShowCcspClusterResponse.
        :type shared_ccsp: bool
        """
        self._shared_ccsp = shared_ccsp

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowCcspClusterResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowCcspClusterResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowCcspClusterResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def az(self):
        r"""Gets the az of this ShowCcspClusterResponse.

        az

        :return: The az of this ShowCcspClusterResponse.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this ShowCcspClusterResponse.

        az

        :param az: The az of this ShowCcspClusterResponse.
        :type az: str
        """
        self._az = az

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
        if not isinstance(other, ShowCcspClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
