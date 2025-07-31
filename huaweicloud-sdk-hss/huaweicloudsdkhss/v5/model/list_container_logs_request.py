# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainerLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'namespace': 'str',
        'pod_name': 'str',
        'pod_id': 'str',
        'pod_ip': 'str',
        'host_ip': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'content': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'line_num': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'namespace': 'namespace',
        'pod_name': 'pod_name',
        'pod_id': 'pod_id',
        'pod_ip': 'pod_ip',
        'host_ip': 'host_ip',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'content': 'content',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'line_num': 'line_num'
    }

    def __init__(self, enterprise_project_id=None, cluster_id=None, cluster_name=None, namespace=None, pod_name=None, pod_id=None, pod_ip=None, host_ip=None, container_id=None, container_name=None, content=None, start_time=None, end_time=None, limit=None, offset=None, line_num=None):
        r"""ListContainerLogsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param namespace: 产生日志的容器所属的命名空间
        :type namespace: str
        :param pod_name: 产生日志的容器所属pod的名称
        :type pod_name: str
        :param pod_id: 产生日志的容器所属pod的id
        :type pod_id: str
        :param pod_ip: 产生日志的容器所属pod的ip
        :type pod_ip: str
        :param host_ip: 产生日志的容器所在主机的ip
        :type host_ip: str
        :param container_id: 容器id
        :type container_id: str
        :param container_name: 产生日志的容器名称
        :type container_name: str
        :param content: 日志内容
        :type content: str
        :param start_time: 查询日志范围的最小时间
        :type start_time: int
        :param end_time: 查询日志范围的最大时间
        :type end_time: int
        :param limit: 每页显示个数，默认为10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param line_num: 查询cce集群容器日志时需要传的分页行号
        :type line_num: str
        """
        
        

        self._enterprise_project_id = None
        self._cluster_id = None
        self._cluster_name = None
        self._namespace = None
        self._pod_name = None
        self._pod_id = None
        self._pod_ip = None
        self._host_ip = None
        self._container_id = None
        self._container_name = None
        self._content = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._line_num = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
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
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if content is not None:
            self.content = content
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if line_num is not None:
            self.line_num = line_num

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListContainerLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListContainerLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListContainerLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListContainerLogsRequest.

        集群id

        :return: The cluster_id of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListContainerLogsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListContainerLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListContainerLogsRequest.

        集群名称

        :return: The cluster_name of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListContainerLogsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListContainerLogsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ListContainerLogsRequest.

        产生日志的容器所属的命名空间

        :return: The namespace of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListContainerLogsRequest.

        产生日志的容器所属的命名空间

        :param namespace: The namespace of this ListContainerLogsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListContainerLogsRequest.

        产生日志的容器所属pod的名称

        :return: The pod_name of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListContainerLogsRequest.

        产生日志的容器所属pod的名称

        :param pod_name: The pod_name of this ListContainerLogsRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ListContainerLogsRequest.

        产生日志的容器所属pod的id

        :return: The pod_id of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ListContainerLogsRequest.

        产生日志的容器所属pod的id

        :param pod_id: The pod_id of this ListContainerLogsRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this ListContainerLogsRequest.

        产生日志的容器所属pod的ip

        :return: The pod_ip of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this ListContainerLogsRequest.

        产生日志的容器所属pod的ip

        :param pod_ip: The pod_ip of this ListContainerLogsRequest.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListContainerLogsRequest.

        产生日志的容器所在主机的ip

        :return: The host_ip of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListContainerLogsRequest.

        产生日志的容器所在主机的ip

        :param host_ip: The host_ip of this ListContainerLogsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def container_id(self):
        r"""Gets the container_id of this ListContainerLogsRequest.

        容器id

        :return: The container_id of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListContainerLogsRequest.

        容器id

        :param container_id: The container_id of this ListContainerLogsRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ListContainerLogsRequest.

        产生日志的容器名称

        :return: The container_name of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListContainerLogsRequest.

        产生日志的容器名称

        :param container_name: The container_name of this ListContainerLogsRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def content(self):
        r"""Gets the content of this ListContainerLogsRequest.

        日志内容

        :return: The content of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ListContainerLogsRequest.

        日志内容

        :param content: The content of this ListContainerLogsRequest.
        :type content: str
        """
        self._content = content

    @property
    def start_time(self):
        r"""Gets the start_time of this ListContainerLogsRequest.

        查询日志范围的最小时间

        :return: The start_time of this ListContainerLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListContainerLogsRequest.

        查询日志范围的最小时间

        :param start_time: The start_time of this ListContainerLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListContainerLogsRequest.

        查询日志范围的最大时间

        :return: The end_time of this ListContainerLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListContainerLogsRequest.

        查询日志范围的最大时间

        :param end_time: The end_time of this ListContainerLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListContainerLogsRequest.

        每页显示个数，默认为10

        :return: The limit of this ListContainerLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContainerLogsRequest.

        每页显示个数，默认为10

        :param limit: The limit of this ListContainerLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContainerLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListContainerLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContainerLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListContainerLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def line_num(self):
        r"""Gets the line_num of this ListContainerLogsRequest.

        查询cce集群容器日志时需要传的分页行号

        :return: The line_num of this ListContainerLogsRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListContainerLogsRequest.

        查询cce集群容器日志时需要传的分页行号

        :param line_num: The line_num of this ListContainerLogsRequest.
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
        if not isinstance(other, ListContainerLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
