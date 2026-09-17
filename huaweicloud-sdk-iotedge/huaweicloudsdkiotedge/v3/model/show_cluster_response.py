# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'description': 'str',
        'version': 'str',
        'state': 'str',
        'os': 'str',
        'arch': 'str',
        'license': 'LicenseInfo',
        'resource_id': 'str',
        'cluster_type': 'str',
        'kubernetes_version': 'str',
        'license_status': 'str',
        'cluster_addr': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'description': 'description',
        'version': 'version',
        'state': 'state',
        'os': 'os',
        'arch': 'arch',
        'license': 'license',
        'resource_id': 'resource_id',
        'cluster_type': 'cluster_type',
        'kubernetes_version': 'kubernetes_version',
        'license_status': 'license_status',
        'cluster_addr': 'cluster_addr',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, cluster_id=None, cluster_name=None, description=None, version=None, state=None, os=None, arch=None, license=None, resource_id=None, cluster_type=None, kubernetes_version=None, license_status=None, cluster_addr=None, create_time=None, update_time=None):
        r"""ShowClusterResponse

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param description: 集群描述
        :type description: str
        :param version: 边缘集群版本
        :type version: str
        :param state: 边缘集群状态
        :type state: str
        :param os: 操作系统
        :type os: str
        :param arch: 集群架构
        :type arch: str
        :param license: 
        :type license: :class:`huaweicloudsdkiotedge.v3.LicenseInfo`
        :param resource_id: 资源id
        :type resource_id: str
        :param cluster_type: 集群类型
        :type cluster_type: str
        :param kubernetes_version: kubernetes版本
        :type kubernetes_version: str
        :param license_status: 集群license状态
        :type license_status: str
        :param cluster_addr: 集群地址
        :type cluster_addr: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        super().__init__()

        self._cluster_id = None
        self._cluster_name = None
        self._description = None
        self._version = None
        self._state = None
        self._os = None
        self._arch = None
        self._license = None
        self._resource_id = None
        self._cluster_type = None
        self._kubernetes_version = None
        self._license_status = None
        self._cluster_addr = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if state is not None:
            self.state = state
        if os is not None:
            self.os = os
        if arch is not None:
            self.arch = arch
        if license is not None:
            self.license = license
        if resource_id is not None:
            self.resource_id = resource_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if kubernetes_version is not None:
            self.kubernetes_version = kubernetes_version
        if license_status is not None:
            self.license_status = license_status
        if cluster_addr is not None:
            self.cluster_addr = cluster_addr
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterResponse.

        集群ID

        :return: The cluster_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterResponse.

        集群ID

        :param cluster_id: The cluster_id of this ShowClusterResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowClusterResponse.

        集群名称

        :return: The cluster_name of this ShowClusterResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowClusterResponse.

        集群名称

        :param cluster_name: The cluster_name of this ShowClusterResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def description(self):
        r"""Gets the description of this ShowClusterResponse.

        集群描述

        :return: The description of this ShowClusterResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowClusterResponse.

        集群描述

        :param description: The description of this ShowClusterResponse.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        r"""Gets the version of this ShowClusterResponse.

        边缘集群版本

        :return: The version of this ShowClusterResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowClusterResponse.

        边缘集群版本

        :param version: The version of this ShowClusterResponse.
        :type version: str
        """
        self._version = version

    @property
    def state(self):
        r"""Gets the state of this ShowClusterResponse.

        边缘集群状态

        :return: The state of this ShowClusterResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowClusterResponse.

        边缘集群状态

        :param state: The state of this ShowClusterResponse.
        :type state: str
        """
        self._state = state

    @property
    def os(self):
        r"""Gets the os of this ShowClusterResponse.

        操作系统

        :return: The os of this ShowClusterResponse.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ShowClusterResponse.

        操作系统

        :param os: The os of this ShowClusterResponse.
        :type os: str
        """
        self._os = os

    @property
    def arch(self):
        r"""Gets the arch of this ShowClusterResponse.

        集群架构

        :return: The arch of this ShowClusterResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ShowClusterResponse.

        集群架构

        :param arch: The arch of this ShowClusterResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def license(self):
        r"""Gets the license of this ShowClusterResponse.

        :return: The license of this ShowClusterResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v3.LicenseInfo`
        """
        return self._license

    @license.setter
    def license(self, license):
        r"""Sets the license of this ShowClusterResponse.

        :param license: The license of this ShowClusterResponse.
        :type license: :class:`huaweicloudsdkiotedge.v3.LicenseInfo`
        """
        self._license = license

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowClusterResponse.

        资源id

        :return: The resource_id of this ShowClusterResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowClusterResponse.

        资源id

        :param resource_id: The resource_id of this ShowClusterResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ShowClusterResponse.

        集群类型

        :return: The cluster_type of this ShowClusterResponse.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ShowClusterResponse.

        集群类型

        :param cluster_type: The cluster_type of this ShowClusterResponse.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def kubernetes_version(self):
        r"""Gets the kubernetes_version of this ShowClusterResponse.

        kubernetes版本

        :return: The kubernetes_version of this ShowClusterResponse.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        r"""Sets the kubernetes_version of this ShowClusterResponse.

        kubernetes版本

        :param kubernetes_version: The kubernetes_version of this ShowClusterResponse.
        :type kubernetes_version: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def license_status(self):
        r"""Gets the license_status of this ShowClusterResponse.

        集群license状态

        :return: The license_status of this ShowClusterResponse.
        :rtype: str
        """
        return self._license_status

    @license_status.setter
    def license_status(self, license_status):
        r"""Sets the license_status of this ShowClusterResponse.

        集群license状态

        :param license_status: The license_status of this ShowClusterResponse.
        :type license_status: str
        """
        self._license_status = license_status

    @property
    def cluster_addr(self):
        r"""Gets the cluster_addr of this ShowClusterResponse.

        集群地址

        :return: The cluster_addr of this ShowClusterResponse.
        :rtype: str
        """
        return self._cluster_addr

    @cluster_addr.setter
    def cluster_addr(self, cluster_addr):
        r"""Sets the cluster_addr of this ShowClusterResponse.

        集群地址

        :param cluster_addr: The cluster_addr of this ShowClusterResponse.
        :type cluster_addr: str
        """
        self._cluster_addr = cluster_addr

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowClusterResponse.

        创建时间

        :return: The create_time of this ShowClusterResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowClusterResponse.

        创建时间

        :param create_time: The create_time of this ShowClusterResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowClusterResponse.

        最后一次修改时间

        :return: The update_time of this ShowClusterResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowClusterResponse.

        最后一次修改时间

        :param update_time: The update_time of this ShowClusterResponse.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowClusterResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
