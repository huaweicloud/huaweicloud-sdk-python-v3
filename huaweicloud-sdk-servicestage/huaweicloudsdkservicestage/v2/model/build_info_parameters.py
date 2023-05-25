# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildInfoParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_cmd': 'str',
        'dockerfile_path': 'str',
        'artifact_namespace': 'str',
        'cluster_id': 'str',
        'node_label_selector': 'object'
    }

    attribute_map = {
        'build_cmd': 'build_cmd',
        'dockerfile_path': 'dockerfile_path',
        'artifact_namespace': 'artifact_namespace',
        'cluster_id': 'cluster_id',
        'node_label_selector': 'node_label_selector'
    }

    def __init__(self, build_cmd=None, dockerfile_path=None, artifact_namespace=None, cluster_id=None, node_label_selector=None):
        """BuildInfoParameters

        The model defined in huaweicloud sdk

        :param build_cmd: 编译命令。默认：  1、根目录存在build.sh：./build.sh  2、根据运行系统，示例如下：  Java和Tomcat：mvn clean package  Nodejs: npm build 
        :type build_cmd: str
        :param dockerfile_path: dockerfile地址。默认是根目录./。
        :type dockerfile_path: str
        :param artifact_namespace: 构建归档组织，默认cas_{project_id}。
        :type artifact_namespace: str
        :param cluster_id: 指定构建集群的id。
        :type cluster_id: str
        :param node_label_selector: key是标签的键，value是标签的值。
        :type node_label_selector: object
        """
        
        

        self._build_cmd = None
        self._dockerfile_path = None
        self._artifact_namespace = None
        self._cluster_id = None
        self._node_label_selector = None
        self.discriminator = None

        if build_cmd is not None:
            self.build_cmd = build_cmd
        if dockerfile_path is not None:
            self.dockerfile_path = dockerfile_path
        if artifact_namespace is not None:
            self.artifact_namespace = artifact_namespace
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if node_label_selector is not None:
            self.node_label_selector = node_label_selector

    @property
    def build_cmd(self):
        """Gets the build_cmd of this BuildInfoParameters.

        编译命令。默认：  1、根目录存在build.sh：./build.sh  2、根据运行系统，示例如下：  Java和Tomcat：mvn clean package  Nodejs: npm build 

        :return: The build_cmd of this BuildInfoParameters.
        :rtype: str
        """
        return self._build_cmd

    @build_cmd.setter
    def build_cmd(self, build_cmd):
        """Sets the build_cmd of this BuildInfoParameters.

        编译命令。默认：  1、根目录存在build.sh：./build.sh  2、根据运行系统，示例如下：  Java和Tomcat：mvn clean package  Nodejs: npm build 

        :param build_cmd: The build_cmd of this BuildInfoParameters.
        :type build_cmd: str
        """
        self._build_cmd = build_cmd

    @property
    def dockerfile_path(self):
        """Gets the dockerfile_path of this BuildInfoParameters.

        dockerfile地址。默认是根目录./。

        :return: The dockerfile_path of this BuildInfoParameters.
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        """Sets the dockerfile_path of this BuildInfoParameters.

        dockerfile地址。默认是根目录./。

        :param dockerfile_path: The dockerfile_path of this BuildInfoParameters.
        :type dockerfile_path: str
        """
        self._dockerfile_path = dockerfile_path

    @property
    def artifact_namespace(self):
        """Gets the artifact_namespace of this BuildInfoParameters.

        构建归档组织，默认cas_{project_id}。

        :return: The artifact_namespace of this BuildInfoParameters.
        :rtype: str
        """
        return self._artifact_namespace

    @artifact_namespace.setter
    def artifact_namespace(self, artifact_namespace):
        """Sets the artifact_namespace of this BuildInfoParameters.

        构建归档组织，默认cas_{project_id}。

        :param artifact_namespace: The artifact_namespace of this BuildInfoParameters.
        :type artifact_namespace: str
        """
        self._artifact_namespace = artifact_namespace

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BuildInfoParameters.

        指定构建集群的id。

        :return: The cluster_id of this BuildInfoParameters.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BuildInfoParameters.

        指定构建集群的id。

        :param cluster_id: The cluster_id of this BuildInfoParameters.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_label_selector(self):
        """Gets the node_label_selector of this BuildInfoParameters.

        key是标签的键，value是标签的值。

        :return: The node_label_selector of this BuildInfoParameters.
        :rtype: object
        """
        return self._node_label_selector

    @node_label_selector.setter
    def node_label_selector(self, node_label_selector):
        """Sets the node_label_selector of this BuildInfoParameters.

        key是标签的键，value是标签的值。

        :param node_label_selector: The node_label_selector of this BuildInfoParameters.
        :type node_label_selector: object
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
        if not isinstance(other, BuildInfoParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
