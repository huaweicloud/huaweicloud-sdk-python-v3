# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'artifact_namespace': 'str',
        'build_cmd': 'str',
        'cluster_id': 'str',
        'dockerfile_path': 'str',
        'environment_id': 'str',
        'node_label_selector': 'dict(str, str)'
    }

    attribute_map = {
        'artifact_namespace': 'artifact_namespace',
        'build_cmd': 'build_cmd',
        'cluster_id': 'cluster_id',
        'dockerfile_path': 'dockerfile_path',
        'environment_id': 'environment_id',
        'node_label_selector': 'node_label_selector'
    }

    def __init__(self, artifact_namespace=None, build_cmd=None, cluster_id=None, dockerfile_path=None, environment_id=None, node_label_selector=None):
        r"""BuildParameters

        The model defined in huaweicloud sdk

        :param artifact_namespace: 
        :type artifact_namespace: str
        :param build_cmd: 
        :type build_cmd: str
        :param cluster_id: 
        :type cluster_id: str
        :param dockerfile_path: 
        :type dockerfile_path: str
        :param environment_id: 构建环境，选择其中的k8s集群进行构建
        :type environment_id: str
        :param node_label_selector: 
        :type node_label_selector: dict(str, str)
        """
        
        

        self._artifact_namespace = None
        self._build_cmd = None
        self._cluster_id = None
        self._dockerfile_path = None
        self._environment_id = None
        self._node_label_selector = None
        self.discriminator = None

        if artifact_namespace is not None:
            self.artifact_namespace = artifact_namespace
        if build_cmd is not None:
            self.build_cmd = build_cmd
        self.cluster_id = cluster_id
        if dockerfile_path is not None:
            self.dockerfile_path = dockerfile_path
        if environment_id is not None:
            self.environment_id = environment_id
        if node_label_selector is not None:
            self.node_label_selector = node_label_selector

    @property
    def artifact_namespace(self):
        r"""Gets the artifact_namespace of this BuildParameters.

        :return: The artifact_namespace of this BuildParameters.
        :rtype: str
        """
        return self._artifact_namespace

    @artifact_namespace.setter
    def artifact_namespace(self, artifact_namespace):
        r"""Sets the artifact_namespace of this BuildParameters.

        :param artifact_namespace: The artifact_namespace of this BuildParameters.
        :type artifact_namespace: str
        """
        self._artifact_namespace = artifact_namespace

    @property
    def build_cmd(self):
        r"""Gets the build_cmd of this BuildParameters.

        :return: The build_cmd of this BuildParameters.
        :rtype: str
        """
        return self._build_cmd

    @build_cmd.setter
    def build_cmd(self, build_cmd):
        r"""Sets the build_cmd of this BuildParameters.

        :param build_cmd: The build_cmd of this BuildParameters.
        :type build_cmd: str
        """
        self._build_cmd = build_cmd

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this BuildParameters.

        :return: The cluster_id of this BuildParameters.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this BuildParameters.

        :param cluster_id: The cluster_id of this BuildParameters.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def dockerfile_path(self):
        r"""Gets the dockerfile_path of this BuildParameters.

        :return: The dockerfile_path of this BuildParameters.
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        r"""Sets the dockerfile_path of this BuildParameters.

        :param dockerfile_path: The dockerfile_path of this BuildParameters.
        :type dockerfile_path: str
        """
        self._dockerfile_path = dockerfile_path

    @property
    def environment_id(self):
        r"""Gets the environment_id of this BuildParameters.

        构建环境，选择其中的k8s集群进行构建

        :return: The environment_id of this BuildParameters.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this BuildParameters.

        构建环境，选择其中的k8s集群进行构建

        :param environment_id: The environment_id of this BuildParameters.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def node_label_selector(self):
        r"""Gets the node_label_selector of this BuildParameters.

        :return: The node_label_selector of this BuildParameters.
        :rtype: dict(str, str)
        """
        return self._node_label_selector

    @node_label_selector.setter
    def node_label_selector(self, node_label_selector):
        r"""Sets the node_label_selector of this BuildParameters.

        :param node_label_selector: The node_label_selector of this BuildParameters.
        :type node_label_selector: dict(str, str)
        """
        self._node_label_selector = node_label_selector

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
        if not isinstance(other, BuildParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
