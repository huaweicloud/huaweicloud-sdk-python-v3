# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterSupportConfigurationRequest:

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
        'cluster_type': 'str',
        'cluster_version': 'str',
        'network_mode': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'cluster_version': 'cluster_version',
        'network_mode': 'network_mode'
    }

    def __init__(self, cluster_id=None, cluster_type=None, cluster_version=None, network_mode=None):
        r"""ShowClusterSupportConfigurationRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param cluster_type: 集群类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_type: str
        :param cluster_version: 集群版本，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_version: str
        :param network_mode: 集群网络类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type network_mode: str
        """
        
        

        self._cluster_id = None
        self._cluster_type = None
        self._cluster_version = None
        self._network_mode = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if network_mode is not None:
            self.network_mode = network_mode

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterSupportConfigurationRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterSupportConfigurationRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ShowClusterSupportConfigurationRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ShowClusterSupportConfigurationRequest.

        集群类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_type of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ShowClusterSupportConfigurationRequest.

        集群类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_type: The cluster_type of this ShowClusterSupportConfigurationRequest.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this ShowClusterSupportConfigurationRequest.

        集群版本，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_version of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this ShowClusterSupportConfigurationRequest.

        集群版本，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_version: The cluster_version of this ShowClusterSupportConfigurationRequest.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def network_mode(self):
        r"""Gets the network_mode of this ShowClusterSupportConfigurationRequest.

        集群网络类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The network_mode of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        r"""Sets the network_mode of this ShowClusterSupportConfigurationRequest.

        集群网络类型，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param network_mode: The network_mode of this ShowClusterSupportConfigurationRequest.
        :type network_mode: str
        """
        self._network_mode = network_mode

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
        if not isinstance(other, ShowClusterSupportConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
