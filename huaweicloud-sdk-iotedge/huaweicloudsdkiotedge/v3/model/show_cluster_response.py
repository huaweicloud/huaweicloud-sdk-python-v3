# coding: utf-8

import six

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
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, cluster_id=None, cluster_name=None, description=None, version=None, state=None, os=None, arch=None, create_time=None, update_time=None):
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
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        super(ShowClusterResponse, self).__init__()

        self._cluster_id = None
        self._cluster_name = None
        self._description = None
        self._version = None
        self._state = None
        self._os = None
        self._arch = None
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
        if not isinstance(other, ShowClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
