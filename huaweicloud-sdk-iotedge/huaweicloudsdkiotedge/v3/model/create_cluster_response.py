# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

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
        'create_time': 'str',
        'update_time': 'str',
        'is_upgradeable': 'bool'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'description': 'description',
        'version': 'version',
        'state': 'state',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_upgradeable': 'is_upgradeable'
    }

    def __init__(self, cluster_id=None, cluster_name=None, description=None, version=None, state=None, create_time=None, update_time=None, is_upgradeable=None):
        """CreateClusterResponse

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
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param is_upgradeable: 是否可升级
        :type is_upgradeable: bool
        """
        
        super(CreateClusterResponse, self).__init__()

        self._cluster_id = None
        self._cluster_name = None
        self._description = None
        self._version = None
        self._state = None
        self._create_time = None
        self._update_time = None
        self._is_upgradeable = None
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_upgradeable is not None:
            self.is_upgradeable = is_upgradeable

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateClusterResponse.

        集群ID

        :return: The cluster_id of this CreateClusterResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateClusterResponse.

        集群ID

        :param cluster_id: The cluster_id of this CreateClusterResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateClusterResponse.

        集群名称

        :return: The cluster_name of this CreateClusterResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateClusterResponse.

        集群名称

        :param cluster_name: The cluster_name of this CreateClusterResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def description(self):
        """Gets the description of this CreateClusterResponse.

        集群描述

        :return: The description of this CreateClusterResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateClusterResponse.

        集群描述

        :param description: The description of this CreateClusterResponse.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        """Gets the version of this CreateClusterResponse.

        边缘集群版本

        :return: The version of this CreateClusterResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateClusterResponse.

        边缘集群版本

        :param version: The version of this CreateClusterResponse.
        :type version: str
        """
        self._version = version

    @property
    def state(self):
        """Gets the state of this CreateClusterResponse.

        边缘集群状态

        :return: The state of this CreateClusterResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateClusterResponse.

        边缘集群状态

        :param state: The state of this CreateClusterResponse.
        :type state: str
        """
        self._state = state

    @property
    def create_time(self):
        """Gets the create_time of this CreateClusterResponse.

        创建时间

        :return: The create_time of this CreateClusterResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateClusterResponse.

        创建时间

        :param create_time: The create_time of this CreateClusterResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateClusterResponse.

        最后一次修改时间

        :return: The update_time of this CreateClusterResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateClusterResponse.

        最后一次修改时间

        :param update_time: The update_time of this CreateClusterResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def is_upgradeable(self):
        """Gets the is_upgradeable of this CreateClusterResponse.

        是否可升级

        :return: The is_upgradeable of this CreateClusterResponse.
        :rtype: bool
        """
        return self._is_upgradeable

    @is_upgradeable.setter
    def is_upgradeable(self, is_upgradeable):
        """Sets the is_upgradeable of this CreateClusterResponse.

        是否可升级

        :param is_upgradeable: The is_upgradeable of this CreateClusterResponse.
        :type is_upgradeable: bool
        """
        self._is_upgradeable = is_upgradeable

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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
