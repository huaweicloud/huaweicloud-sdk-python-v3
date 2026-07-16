# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceExtendParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_base_size': 'str',
        'post_install': 'str',
        'runtime': 'str',
        'label_policy_on_existing_nodes': 'str',
        'taint_policy_on_existing_nodes': 'str',
        'tag_policy_on_existing_nodes': 'str',
        'x_parameter_plane_subnet': 'str',
        'node_pool_name': 'str'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize',
        'post_install': 'postInstall',
        'runtime': 'runtime',
        'label_policy_on_existing_nodes': 'labelPolicyOnExistingNodes',
        'taint_policy_on_existing_nodes': 'taintPolicyOnExistingNodes',
        'tag_policy_on_existing_nodes': 'tagPolicyOnExistingNodes',
        'x_parameter_plane_subnet': 'XParameterPlaneSubnet',
        'node_pool_name': 'nodePoolName'
    }

    def __init__(self, docker_base_size=None, post_install=None, runtime=None, label_policy_on_existing_nodes=None, taint_policy_on_existing_nodes=None, tag_policy_on_existing_nodes=None, x_parameter_plane_subnet=None, node_pool_name=None):
        r"""ResourceExtendParams

        The model defined in huaweicloud sdk

        :param docker_base_size: **参数解释**：节点的容器镜像空间大小。 **取值范围**：可选值如下： - 指定大小：dockerBaseSize的大小范围默认为50-500，但实际上限受到节点的容器数据盘大小约束。 - 不限制：dockerBaseSize&#x3D;\\\&quot;0\\\&quot;，表示不限制容器镜像空间大小。
        :type docker_base_size: str
        :param post_install: **参数解释**：安装后执行脚本，输入的值需要经过Base64编码。 **取值范围**：不涉及。
        :type post_install: str
        :param runtime: **参数解释**：容器运行时。 **取值范围**：可选值如下： - docker：容器运行时，是目前最常用的容器化引擎，基于容器镜像创建和管理容器实例。 - containerd：工业级的容器运行时，专注于容器的生命周期管理，是 Docker 底层核心组件之一，也可独立部署使用。
        :type runtime: str
        :param label_policy_on_existing_nodes: **参数解释**：存量节点k8s标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。
        :type label_policy_on_existing_nodes: str
        :param taint_policy_on_existing_nodes: **参数解释**：存量节点k8s污点更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。
        :type taint_policy_on_existing_nodes: str
        :param tag_policy_on_existing_nodes: **参数解释**：存量节点资源标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。
        :type tag_policy_on_existing_nodes: str
        :param x_parameter_plane_subnet: **参数解释**：跨物理集群之间进行参数面数据传输使用的子网id。不可与节点子网和容器子网重复。 **取值范围**：不涉及。
        :type x_parameter_plane_subnet: str
        :param node_pool_name: **参数解释**：用户指定的节点池名称。最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能以-，-default结尾。 **取值范围**：不涉及
        :type node_pool_name: str
        """
        
        

        self._docker_base_size = None
        self._post_install = None
        self._runtime = None
        self._label_policy_on_existing_nodes = None
        self._taint_policy_on_existing_nodes = None
        self._tag_policy_on_existing_nodes = None
        self._x_parameter_plane_subnet = None
        self._node_pool_name = None
        self.discriminator = None

        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if post_install is not None:
            self.post_install = post_install
        if runtime is not None:
            self.runtime = runtime
        if label_policy_on_existing_nodes is not None:
            self.label_policy_on_existing_nodes = label_policy_on_existing_nodes
        if taint_policy_on_existing_nodes is not None:
            self.taint_policy_on_existing_nodes = taint_policy_on_existing_nodes
        if tag_policy_on_existing_nodes is not None:
            self.tag_policy_on_existing_nodes = tag_policy_on_existing_nodes
        if x_parameter_plane_subnet is not None:
            self.x_parameter_plane_subnet = x_parameter_plane_subnet
        if node_pool_name is not None:
            self.node_pool_name = node_pool_name

    @property
    def docker_base_size(self):
        r"""Gets the docker_base_size of this ResourceExtendParams.

        **参数解释**：节点的容器镜像空间大小。 **取值范围**：可选值如下： - 指定大小：dockerBaseSize的大小范围默认为50-500，但实际上限受到节点的容器数据盘大小约束。 - 不限制：dockerBaseSize=\\\"0\\\"，表示不限制容器镜像空间大小。

        :return: The docker_base_size of this ResourceExtendParams.
        :rtype: str
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        r"""Sets the docker_base_size of this ResourceExtendParams.

        **参数解释**：节点的容器镜像空间大小。 **取值范围**：可选值如下： - 指定大小：dockerBaseSize的大小范围默认为50-500，但实际上限受到节点的容器数据盘大小约束。 - 不限制：dockerBaseSize=\\\"0\\\"，表示不限制容器镜像空间大小。

        :param docker_base_size: The docker_base_size of this ResourceExtendParams.
        :type docker_base_size: str
        """
        self._docker_base_size = docker_base_size

    @property
    def post_install(self):
        r"""Gets the post_install of this ResourceExtendParams.

        **参数解释**：安装后执行脚本，输入的值需要经过Base64编码。 **取值范围**：不涉及。

        :return: The post_install of this ResourceExtendParams.
        :rtype: str
        """
        return self._post_install

    @post_install.setter
    def post_install(self, post_install):
        r"""Sets the post_install of this ResourceExtendParams.

        **参数解释**：安装后执行脚本，输入的值需要经过Base64编码。 **取值范围**：不涉及。

        :param post_install: The post_install of this ResourceExtendParams.
        :type post_install: str
        """
        self._post_install = post_install

    @property
    def runtime(self):
        r"""Gets the runtime of this ResourceExtendParams.

        **参数解释**：容器运行时。 **取值范围**：可选值如下： - docker：容器运行时，是目前最常用的容器化引擎，基于容器镜像创建和管理容器实例。 - containerd：工业级的容器运行时，专注于容器的生命周期管理，是 Docker 底层核心组件之一，也可独立部署使用。

        :return: The runtime of this ResourceExtendParams.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ResourceExtendParams.

        **参数解释**：容器运行时。 **取值范围**：可选值如下： - docker：容器运行时，是目前最常用的容器化引擎，基于容器镜像创建和管理容器实例。 - containerd：工业级的容器运行时，专注于容器的生命周期管理，是 Docker 底层核心组件之一，也可独立部署使用。

        :param runtime: The runtime of this ResourceExtendParams.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def label_policy_on_existing_nodes(self):
        r"""Gets the label_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点k8s标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :return: The label_policy_on_existing_nodes of this ResourceExtendParams.
        :rtype: str
        """
        return self._label_policy_on_existing_nodes

    @label_policy_on_existing_nodes.setter
    def label_policy_on_existing_nodes(self, label_policy_on_existing_nodes):
        r"""Sets the label_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点k8s标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :param label_policy_on_existing_nodes: The label_policy_on_existing_nodes of this ResourceExtendParams.
        :type label_policy_on_existing_nodes: str
        """
        self._label_policy_on_existing_nodes = label_policy_on_existing_nodes

    @property
    def taint_policy_on_existing_nodes(self):
        r"""Gets the taint_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点k8s污点更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :return: The taint_policy_on_existing_nodes of this ResourceExtendParams.
        :rtype: str
        """
        return self._taint_policy_on_existing_nodes

    @taint_policy_on_existing_nodes.setter
    def taint_policy_on_existing_nodes(self, taint_policy_on_existing_nodes):
        r"""Sets the taint_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点k8s污点更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :param taint_policy_on_existing_nodes: The taint_policy_on_existing_nodes of this ResourceExtendParams.
        :type taint_policy_on_existing_nodes: str
        """
        self._taint_policy_on_existing_nodes = taint_policy_on_existing_nodes

    @property
    def tag_policy_on_existing_nodes(self):
        r"""Gets the tag_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点资源标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :return: The tag_policy_on_existing_nodes of this ResourceExtendParams.
        :rtype: str
        """
        return self._tag_policy_on_existing_nodes

    @tag_policy_on_existing_nodes.setter
    def tag_policy_on_existing_nodes(self, tag_policy_on_existing_nodes):
        r"""Sets the tag_policy_on_existing_nodes of this ResourceExtendParams.

        **参数解释**：存量节点资源标签更新策略，值为空时默认更新存量节点。 **取值范围**：可选值如下： - refresh：更新。 - ignore：不更新。

        :param tag_policy_on_existing_nodes: The tag_policy_on_existing_nodes of this ResourceExtendParams.
        :type tag_policy_on_existing_nodes: str
        """
        self._tag_policy_on_existing_nodes = tag_policy_on_existing_nodes

    @property
    def x_parameter_plane_subnet(self):
        r"""Gets the x_parameter_plane_subnet of this ResourceExtendParams.

        **参数解释**：跨物理集群之间进行参数面数据传输使用的子网id。不可与节点子网和容器子网重复。 **取值范围**：不涉及。

        :return: The x_parameter_plane_subnet of this ResourceExtendParams.
        :rtype: str
        """
        return self._x_parameter_plane_subnet

    @x_parameter_plane_subnet.setter
    def x_parameter_plane_subnet(self, x_parameter_plane_subnet):
        r"""Sets the x_parameter_plane_subnet of this ResourceExtendParams.

        **参数解释**：跨物理集群之间进行参数面数据传输使用的子网id。不可与节点子网和容器子网重复。 **取值范围**：不涉及。

        :param x_parameter_plane_subnet: The x_parameter_plane_subnet of this ResourceExtendParams.
        :type x_parameter_plane_subnet: str
        """
        self._x_parameter_plane_subnet = x_parameter_plane_subnet

    @property
    def node_pool_name(self):
        r"""Gets the node_pool_name of this ResourceExtendParams.

        **参数解释**：用户指定的节点池名称。最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能以-，-default结尾。 **取值范围**：不涉及

        :return: The node_pool_name of this ResourceExtendParams.
        :rtype: str
        """
        return self._node_pool_name

    @node_pool_name.setter
    def node_pool_name(self, node_pool_name):
        r"""Sets the node_pool_name of this ResourceExtendParams.

        **参数解释**：用户指定的节点池名称。最小长度为2，最大长度为50的小写字母、中划线-、数字组成，由小写字母开头，不能以-，-default结尾。 **取值范围**：不涉及

        :param node_pool_name: The node_pool_name of this ResourceExtendParams.
        :type node_pool_name: str
        """
        self._node_pool_name = node_pool_name

    def to_dict(self):
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
        if not isinstance(other, ResourceExtendParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
