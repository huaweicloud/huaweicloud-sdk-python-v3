# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterInstallCmdRequest:

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
        'arch': 'str',
        'os': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'arch': 'arch',
        'os': 'os'
    }

    def __init__(self, cluster_id=None, arch=None, os=None):
        """CreateClusterInstallCmdRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 边缘集群ID
        :type cluster_id: str
        :param arch: 边缘集群架构
        :type arch: str
        :param os: 集群操作系统内核
        :type os: str
        """
        
        

        self._cluster_id = None
        self._arch = None
        self._os = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.arch = arch
        if os is not None:
            self.os = os

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateClusterInstallCmdRequest.

        边缘集群ID

        :return: The cluster_id of this CreateClusterInstallCmdRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateClusterInstallCmdRequest.

        边缘集群ID

        :param cluster_id: The cluster_id of this CreateClusterInstallCmdRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def arch(self):
        """Gets the arch of this CreateClusterInstallCmdRequest.

        边缘集群架构

        :return: The arch of this CreateClusterInstallCmdRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateClusterInstallCmdRequest.

        边缘集群架构

        :param arch: The arch of this CreateClusterInstallCmdRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def os(self):
        """Gets the os of this CreateClusterInstallCmdRequest.

        集群操作系统内核

        :return: The os of this CreateClusterInstallCmdRequest.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this CreateClusterInstallCmdRequest.

        集群操作系统内核

        :param os: The os of this CreateClusterInstallCmdRequest.
        :type os: str
        """
        self._os = os

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
        if not isinstance(other, CreateClusterInstallCmdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
