# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshCluster:

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
        'project_id': 'str',
        'injection': 'InjectionConfig',
        'installation': 'InstallationConfig'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'project_id': 'projectID',
        'injection': 'injection',
        'installation': 'installation'
    }

    def __init__(self, cluster_id=None, project_id=None, injection=None, installation=None):
        r"""MeshCluster

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，资源唯一标识，通过该ID查询需要添加的集群
        :type cluster_id: str
        :param project_id: 集群所属的projectID
        :type project_id: str
        :param injection: 
        :type injection: :class:`huaweicloudsdkasm.v1.InjectionConfig`
        :param installation: 
        :type installation: :class:`huaweicloudsdkasm.v1.InstallationConfig`
        """
        
        

        self._cluster_id = None
        self._project_id = None
        self._injection = None
        self._installation = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.project_id = project_id
        if injection is not None:
            self.injection = injection
        self.installation = installation

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this MeshCluster.

        集群ID，资源唯一标识，通过该ID查询需要添加的集群

        :return: The cluster_id of this MeshCluster.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this MeshCluster.

        集群ID，资源唯一标识，通过该ID查询需要添加的集群

        :param cluster_id: The cluster_id of this MeshCluster.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def project_id(self):
        r"""Gets the project_id of this MeshCluster.

        集群所属的projectID

        :return: The project_id of this MeshCluster.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MeshCluster.

        集群所属的projectID

        :param project_id: The project_id of this MeshCluster.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def injection(self):
        r"""Gets the injection of this MeshCluster.

        :return: The injection of this MeshCluster.
        :rtype: :class:`huaweicloudsdkasm.v1.InjectionConfig`
        """
        return self._injection

    @injection.setter
    def injection(self, injection):
        r"""Sets the injection of this MeshCluster.

        :param injection: The injection of this MeshCluster.
        :type injection: :class:`huaweicloudsdkasm.v1.InjectionConfig`
        """
        self._injection = injection

    @property
    def installation(self):
        r"""Gets the installation of this MeshCluster.

        :return: The installation of this MeshCluster.
        :rtype: :class:`huaweicloudsdkasm.v1.InstallationConfig`
        """
        return self._installation

    @installation.setter
    def installation(self, installation):
        r"""Sets the installation of this MeshCluster.

        :param installation: The installation of this MeshCluster.
        :type installation: :class:`huaweicloudsdkasm.v1.InstallationConfig`
        """
        self._installation = installation

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
        if not isinstance(other, MeshCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
