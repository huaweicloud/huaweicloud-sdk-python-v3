# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessDeploymentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace_name': 'str',
        'cluster_name': 'str',
        'status': 'str',
        'protect_status': 'str',
        'pods_num': 'int',
        'image_name': 'str',
        'match_labels': 'list[LabelInfo]',
        'create_time': 'int',
        'agent_installed_num': 'int',
        'agent_install_failed_num': 'int',
        'agent_not_install_num': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'status': 'status',
        'protect_status': 'protect_status',
        'pods_num': 'pods_num',
        'image_name': 'image_name',
        'match_labels': 'match_labels',
        'create_time': 'create_time',
        'agent_installed_num': 'agent_installed_num',
        'agent_install_failed_num': 'agent_install_failed_num',
        'agent_not_install_num': 'agent_not_install_num'
    }

    def __init__(self, name=None, namespace_name=None, cluster_name=None, status=None, protect_status=None, pods_num=None, image_name=None, match_labels=None, create_time=None, agent_installed_num=None, agent_install_failed_num=None, agent_not_install_num=None):
        r"""ServerlessDeploymentInfo

        The model defined in huaweicloud sdk

        :param name: deployment名称
        :type name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param cluster_name: 所属集群
        :type cluster_name: str
        :param status: 状态，包含以下几种 -Running：正常运行 -Failed：存在异常
        :type status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param pods_num: 实例总数
        :type pods_num: int
        :param image_name: 镜像名称
        :type image_name: str
        :param match_labels: 标签
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        :param create_time: 创建时间
        :type create_time: int
        :param agent_installed_num: 工作负载下已安装agent实例数
        :type agent_installed_num: int
        :param agent_install_failed_num: 工作负载下安装失败实例数
        :type agent_install_failed_num: int
        :param agent_not_install_num: 工作负载下未安装agent实例数
        :type agent_not_install_num: int
        """
        
        

        self._name = None
        self._namespace_name = None
        self._cluster_name = None
        self._status = None
        self._protect_status = None
        self._pods_num = None
        self._image_name = None
        self._match_labels = None
        self._create_time = None
        self._agent_installed_num = None
        self._agent_install_failed_num = None
        self._agent_not_install_num = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if status is not None:
            self.status = status
        if protect_status is not None:
            self.protect_status = protect_status
        if pods_num is not None:
            self.pods_num = pods_num
        if image_name is not None:
            self.image_name = image_name
        if match_labels is not None:
            self.match_labels = match_labels
        if create_time is not None:
            self.create_time = create_time
        if agent_installed_num is not None:
            self.agent_installed_num = agent_installed_num
        if agent_install_failed_num is not None:
            self.agent_install_failed_num = agent_install_failed_num
        if agent_not_install_num is not None:
            self.agent_not_install_num = agent_not_install_num

    @property
    def name(self):
        r"""Gets the name of this ServerlessDeploymentInfo.

        deployment名称

        :return: The name of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerlessDeploymentInfo.

        deployment名称

        :param name: The name of this ServerlessDeploymentInfo.
        :type name: str
        """
        self._name = name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ServerlessDeploymentInfo.

        命名空间名称

        :return: The namespace_name of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ServerlessDeploymentInfo.

        命名空间名称

        :param namespace_name: The namespace_name of this ServerlessDeploymentInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ServerlessDeploymentInfo.

        所属集群

        :return: The cluster_name of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ServerlessDeploymentInfo.

        所属集群

        :param cluster_name: The cluster_name of this ServerlessDeploymentInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def status(self):
        r"""Gets the status of this ServerlessDeploymentInfo.

        状态，包含以下几种 -Running：正常运行 -Failed：存在异常

        :return: The status of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerlessDeploymentInfo.

        状态，包含以下几种 -Running：正常运行 -Failed：存在异常

        :param status: The status of this ServerlessDeploymentInfo.
        :type status: str
        """
        self._status = status

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ServerlessDeploymentInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ServerlessDeploymentInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ServerlessDeploymentInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def pods_num(self):
        r"""Gets the pods_num of this ServerlessDeploymentInfo.

        实例总数

        :return: The pods_num of this ServerlessDeploymentInfo.
        :rtype: int
        """
        return self._pods_num

    @pods_num.setter
    def pods_num(self, pods_num):
        r"""Sets the pods_num of this ServerlessDeploymentInfo.

        实例总数

        :param pods_num: The pods_num of this ServerlessDeploymentInfo.
        :type pods_num: int
        """
        self._pods_num = pods_num

    @property
    def image_name(self):
        r"""Gets the image_name of this ServerlessDeploymentInfo.

        镜像名称

        :return: The image_name of this ServerlessDeploymentInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ServerlessDeploymentInfo.

        镜像名称

        :param image_name: The image_name of this ServerlessDeploymentInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def match_labels(self):
        r"""Gets the match_labels of this ServerlessDeploymentInfo.

        标签

        :return: The match_labels of this ServerlessDeploymentInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        r"""Sets the match_labels of this ServerlessDeploymentInfo.

        标签

        :param match_labels: The match_labels of this ServerlessDeploymentInfo.
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        self._match_labels = match_labels

    @property
    def create_time(self):
        r"""Gets the create_time of this ServerlessDeploymentInfo.

        创建时间

        :return: The create_time of this ServerlessDeploymentInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ServerlessDeploymentInfo.

        创建时间

        :param create_time: The create_time of this ServerlessDeploymentInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def agent_installed_num(self):
        r"""Gets the agent_installed_num of this ServerlessDeploymentInfo.

        工作负载下已安装agent实例数

        :return: The agent_installed_num of this ServerlessDeploymentInfo.
        :rtype: int
        """
        return self._agent_installed_num

    @agent_installed_num.setter
    def agent_installed_num(self, agent_installed_num):
        r"""Sets the agent_installed_num of this ServerlessDeploymentInfo.

        工作负载下已安装agent实例数

        :param agent_installed_num: The agent_installed_num of this ServerlessDeploymentInfo.
        :type agent_installed_num: int
        """
        self._agent_installed_num = agent_installed_num

    @property
    def agent_install_failed_num(self):
        r"""Gets the agent_install_failed_num of this ServerlessDeploymentInfo.

        工作负载下安装失败实例数

        :return: The agent_install_failed_num of this ServerlessDeploymentInfo.
        :rtype: int
        """
        return self._agent_install_failed_num

    @agent_install_failed_num.setter
    def agent_install_failed_num(self, agent_install_failed_num):
        r"""Sets the agent_install_failed_num of this ServerlessDeploymentInfo.

        工作负载下安装失败实例数

        :param agent_install_failed_num: The agent_install_failed_num of this ServerlessDeploymentInfo.
        :type agent_install_failed_num: int
        """
        self._agent_install_failed_num = agent_install_failed_num

    @property
    def agent_not_install_num(self):
        r"""Gets the agent_not_install_num of this ServerlessDeploymentInfo.

        工作负载下未安装agent实例数

        :return: The agent_not_install_num of this ServerlessDeploymentInfo.
        :rtype: int
        """
        return self._agent_not_install_num

    @agent_not_install_num.setter
    def agent_not_install_num(self, agent_not_install_num):
        r"""Sets the agent_not_install_num of this ServerlessDeploymentInfo.

        工作负载下未安装agent实例数

        :param agent_not_install_num: The agent_not_install_num of this ServerlessDeploymentInfo.
        :type agent_not_install_num: int
        """
        self._agent_not_install_num = agent_not_install_num

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
        if not isinstance(other, ServerlessDeploymentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
