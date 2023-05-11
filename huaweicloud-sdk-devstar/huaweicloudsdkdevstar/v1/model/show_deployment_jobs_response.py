# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'job_id': 'str',
        'status': 'int',
        'address': 'str',
        'deploy_parameters': 'str',
        'time': 'int',
        'creator_name': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'status': 'status',
        'address': 'address',
        'deploy_parameters': 'deploy_parameters',
        'time': 'time',
        'creator_name': 'creator_name',
        'created_time': 'created_time'
    }

    def __init__(self, id=None, job_id=None, status=None, address=None, deploy_parameters=None, time=None, creator_name=None, created_time=None):
        """ShowDeploymentJobsResponse

        The model defined in huaweicloud sdk

        :param id: 部署任务编号
        :type id: int
        :param job_id: 任务ID
        :type job_id: str
        :param status: 部署状态,-2：环境准备未就绪 -1 资源准备就绪 0 部署中 1：成功 2：失败
        :type status: int
        :param address: 访问地址
        :type address: str
        :param deploy_parameters: 部署参数
        :type deploy_parameters: str
        :param time: 部署耗时
        :type time: int
        :param creator_name: 创建人
        :type creator_name: str
        :param created_time: 创建时间
        :type created_time: str
        """
        
        super(ShowDeploymentJobsResponse, self).__init__()

        self._id = None
        self._job_id = None
        self._status = None
        self._address = None
        self._deploy_parameters = None
        self._time = None
        self._creator_name = None
        self._created_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if address is not None:
            self.address = address
        if deploy_parameters is not None:
            self.deploy_parameters = deploy_parameters
        if time is not None:
            self.time = time
        if creator_name is not None:
            self.creator_name = creator_name
        if created_time is not None:
            self.created_time = created_time

    @property
    def id(self):
        """Gets the id of this ShowDeploymentJobsResponse.

        部署任务编号

        :return: The id of this ShowDeploymentJobsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDeploymentJobsResponse.

        部署任务编号

        :param id: The id of this ShowDeploymentJobsResponse.
        :type id: int
        """
        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this ShowDeploymentJobsResponse.

        任务ID

        :return: The job_id of this ShowDeploymentJobsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowDeploymentJobsResponse.

        任务ID

        :param job_id: The job_id of this ShowDeploymentJobsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ShowDeploymentJobsResponse.

        部署状态,-2：环境准备未就绪 -1 资源准备就绪 0 部署中 1：成功 2：失败

        :return: The status of this ShowDeploymentJobsResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDeploymentJobsResponse.

        部署状态,-2：环境准备未就绪 -1 资源准备就绪 0 部署中 1：成功 2：失败

        :param status: The status of this ShowDeploymentJobsResponse.
        :type status: int
        """
        self._status = status

    @property
    def address(self):
        """Gets the address of this ShowDeploymentJobsResponse.

        访问地址

        :return: The address of this ShowDeploymentJobsResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ShowDeploymentJobsResponse.

        访问地址

        :param address: The address of this ShowDeploymentJobsResponse.
        :type address: str
        """
        self._address = address

    @property
    def deploy_parameters(self):
        """Gets the deploy_parameters of this ShowDeploymentJobsResponse.

        部署参数

        :return: The deploy_parameters of this ShowDeploymentJobsResponse.
        :rtype: str
        """
        return self._deploy_parameters

    @deploy_parameters.setter
    def deploy_parameters(self, deploy_parameters):
        """Sets the deploy_parameters of this ShowDeploymentJobsResponse.

        部署参数

        :param deploy_parameters: The deploy_parameters of this ShowDeploymentJobsResponse.
        :type deploy_parameters: str
        """
        self._deploy_parameters = deploy_parameters

    @property
    def time(self):
        """Gets the time of this ShowDeploymentJobsResponse.

        部署耗时

        :return: The time of this ShowDeploymentJobsResponse.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ShowDeploymentJobsResponse.

        部署耗时

        :param time: The time of this ShowDeploymentJobsResponse.
        :type time: int
        """
        self._time = time

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowDeploymentJobsResponse.

        创建人

        :return: The creator_name of this ShowDeploymentJobsResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowDeploymentJobsResponse.

        创建人

        :param creator_name: The creator_name of this ShowDeploymentJobsResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def created_time(self):
        """Gets the created_time of this ShowDeploymentJobsResponse.

        创建时间

        :return: The created_time of this ShowDeploymentJobsResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDeploymentJobsResponse.

        创建时间

        :param created_time: The created_time of this ShowDeploymentJobsResponse.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, ShowDeploymentJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
