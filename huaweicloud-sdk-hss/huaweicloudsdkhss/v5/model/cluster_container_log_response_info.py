# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterContainerLogResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'time': 'int',
        'namespace': 'str',
        'pod_name': 'str',
        'pod_id': 'str',
        'pod_ip': 'str',
        'host_ip': 'str',
        'container_name': 'str',
        'container_id': 'str',
        'content': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'time': 'time',
        'namespace': 'namespace',
        'pod_name': 'pod_name',
        'pod_id': 'pod_id',
        'pod_ip': 'pod_ip',
        'host_ip': 'host_ip',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'content': 'content',
        'line_num': 'line_num'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cluster_type=None, time=None, namespace=None, pod_name=None, pod_id=None, pod_ip=None, host_ip=None, container_name=None, container_id=None, content=None, line_num=None):
        r"""ClusterContainerLogResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param time: 日志产生的时间
        :type time: int
        :param namespace: 容器日志所属的命名空间
        :type namespace: str
        :param pod_name: 产生日志的容器所属pod的名称
        :type pod_name: str
        :param pod_id: 产生日志的容器所属pod的id
        :type pod_id: str
        :param pod_ip: 产生日志的容器所属pod的ip
        :type pod_ip: str
        :param host_ip: 产生日志的容器所在的主机ip
        :type host_ip: str
        :param container_name: 产生日志的容器名称
        :type container_name: str
        :param container_id: 产生日志的容器id
        :type container_id: str
        :param content: 日志的内容
        :type content: str
        :param line_num: cce集群容器日志的行号
        :type line_num: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._time = None
        self._namespace = None
        self._pod_name = None
        self._pod_id = None
        self._pod_ip = None
        self._host_ip = None
        self._container_name = None
        self._container_id = None
        self._content = None
        self._line_num = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if time is not None:
            self.time = time
        if namespace is not None:
            self.namespace = namespace
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if host_ip is not None:
            self.host_ip = host_ip
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if content is not None:
            self.content = content
        if line_num is not None:
            self.line_num = line_num

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterContainerLogResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterContainerLogResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterContainerLogResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterContainerLogResponseInfo.

        集群id

        :return: The cluster_id of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterContainerLogResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterContainerLogResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterContainerLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterContainerLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ClusterContainerLogResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def time(self):
        r"""Gets the time of this ClusterContainerLogResponseInfo.

        日志产生的时间

        :return: The time of this ClusterContainerLogResponseInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ClusterContainerLogResponseInfo.

        日志产生的时间

        :param time: The time of this ClusterContainerLogResponseInfo.
        :type time: int
        """
        self._time = time

    @property
    def namespace(self):
        r"""Gets the namespace of this ClusterContainerLogResponseInfo.

        容器日志所属的命名空间

        :return: The namespace of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ClusterContainerLogResponseInfo.

        容器日志所属的命名空间

        :param namespace: The namespace of this ClusterContainerLogResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的名称

        :return: The pod_name of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的名称

        :param pod_name: The pod_name of this ClusterContainerLogResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的id

        :return: The pod_id of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的id

        :param pod_id: The pod_id of this ClusterContainerLogResponseInfo.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的ip

        :return: The pod_ip of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this ClusterContainerLogResponseInfo.

        产生日志的容器所属pod的ip

        :param pod_ip: The pod_ip of this ClusterContainerLogResponseInfo.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ClusterContainerLogResponseInfo.

        产生日志的容器所在的主机ip

        :return: The host_ip of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ClusterContainerLogResponseInfo.

        产生日志的容器所在的主机ip

        :param host_ip: The host_ip of this ClusterContainerLogResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ClusterContainerLogResponseInfo.

        产生日志的容器名称

        :return: The container_name of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ClusterContainerLogResponseInfo.

        产生日志的容器名称

        :param container_name: The container_name of this ClusterContainerLogResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ClusterContainerLogResponseInfo.

        产生日志的容器id

        :return: The container_id of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ClusterContainerLogResponseInfo.

        产生日志的容器id

        :param container_id: The container_id of this ClusterContainerLogResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def content(self):
        r"""Gets the content of this ClusterContainerLogResponseInfo.

        日志的内容

        :return: The content of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ClusterContainerLogResponseInfo.

        日志的内容

        :param content: The content of this ClusterContainerLogResponseInfo.
        :type content: str
        """
        self._content = content

    @property
    def line_num(self):
        r"""Gets the line_num of this ClusterContainerLogResponseInfo.

        cce集群容器日志的行号

        :return: The line_num of this ClusterContainerLogResponseInfo.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ClusterContainerLogResponseInfo.

        cce集群容器日志的行号

        :param line_num: The line_num of this ClusterContainerLogResponseInfo.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, ClusterContainerLogResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
