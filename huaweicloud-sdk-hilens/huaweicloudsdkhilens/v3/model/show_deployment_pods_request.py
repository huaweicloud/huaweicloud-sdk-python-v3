# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentPodsRequest:

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
        'node_id': 'str',
        'provider': 'str',
        'deployment_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_id': 'node_id',
        'provider': 'provider',
        'deployment_id': 'deployment_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, cluster_id=None, node_id=None, provider=None, deployment_id=None, workspace_id=None):
        """ShowDeploymentPodsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求
        :type cluster_id: str
        :param node_id: 节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求
        :type node_id: str
        :param provider: 平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据
        :type provider: str
        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param workspace_id: 工作空间ID，默认为注册账号/子账号的default工作空间。主账号默认ID为0，子账号默认空间id为该子账号user_id
        :type workspace_id: str
        """
        
        

        self._cluster_id = None
        self._node_id = None
        self._provider = None
        self._deployment_id = None
        self._workspace_id = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if node_id is not None:
            self.node_id = node_id
        if provider is not None:
            self.provider = provider
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowDeploymentPodsRequest.

        集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :return: The cluster_id of this ShowDeploymentPodsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowDeploymentPodsRequest.

        集群ID，查询部署在该节点组的应用列表，和node_id不可同时请求

        :param cluster_id: The cluster_id of this ShowDeploymentPodsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_id(self):
        """Gets the node_id of this ShowDeploymentPodsRequest.

        节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求

        :return: The node_id of this ShowDeploymentPodsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowDeploymentPodsRequest.

        节点ID，查询部署在该节点下的应用列表，和cluster_id不可同时请求

        :param node_id: The node_id of this ShowDeploymentPodsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def provider(self):
        """Gets the provider of this ShowDeploymentPodsRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :return: The provider of this ShowDeploymentPodsRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowDeploymentPodsRequest.

        平台提供者，分别为hilens及ief。当为hilens时，请求部署在hilens平台的相关数据

        :param provider: The provider of this ShowDeploymentPodsRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def deployment_id(self):
        """Gets the deployment_id of this ShowDeploymentPodsRequest.

        应用部署ID

        :return: The deployment_id of this ShowDeploymentPodsRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this ShowDeploymentPodsRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this ShowDeploymentPodsRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ShowDeploymentPodsRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间。主账号默认ID为0，子账号默认空间id为该子账号user_id

        :return: The workspace_id of this ShowDeploymentPodsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ShowDeploymentPodsRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间。主账号默认ID为0，子账号默认空间id为该子账号user_id

        :param workspace_id: The workspace_id of this ShowDeploymentPodsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ShowDeploymentPodsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
