# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainerCmdLogsRequest:

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
        'host_name': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'cmd': 'str',
        'path': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'cmd': 'cmd',
        'path': 'path',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, cluster_id=None, cluster_name=None, host_name=None, host_id=None, host_ip=None, container_id=None, container_name=None, cmd=None, path=None, start_time=None, end_time=None, limit=None, offset=None):
        r"""ListContainerCmdLogsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param host_name: 产生日志的容器所在主机的名称
        :type host_name: str
        :param host_id: 产生日志的容器所在主机的id
        :type host_id: str
        :param host_ip: 产生日志的容器所在主机的ip
        :type host_ip: str
        :param container_id: 容器id
        :type container_id: str
        :param container_name: 产生日志的容器名称
        :type container_name: str
        :param cmd: 运行的命令行
        :type cmd: str
        :param path: 命令行对应的进程路径
        :type path: str
        :param start_time: 查询日志范围的最小时间
        :type start_time: int
        :param end_time: 查询日志范围的最大时间
        :type end_time: int
        :param limit: 每页显示个数，默认为10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._cluster_id = None
        self._cluster_name = None
        self._host_name = None
        self._host_id = None
        self._host_ip = None
        self._container_id = None
        self._container_name = None
        self._cmd = None
        self._path = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if cmd is not None:
            self.cmd = cmd
        if path is not None:
            self.path = path
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.limit = limit
        self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListContainerCmdLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListContainerCmdLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListContainerCmdLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListContainerCmdLogsRequest.

        集群id

        :return: The cluster_id of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListContainerCmdLogsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListContainerCmdLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListContainerCmdLogsRequest.

        集群名称

        :return: The cluster_name of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListContainerCmdLogsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListContainerCmdLogsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的名称

        :return: The host_name of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的名称

        :param host_name: The host_name of this ListContainerCmdLogsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的id

        :return: The host_id of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的id

        :param host_id: The host_id of this ListContainerCmdLogsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的ip

        :return: The host_ip of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListContainerCmdLogsRequest.

        产生日志的容器所在主机的ip

        :param host_ip: The host_ip of this ListContainerCmdLogsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def container_id(self):
        r"""Gets the container_id of this ListContainerCmdLogsRequest.

        容器id

        :return: The container_id of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListContainerCmdLogsRequest.

        容器id

        :param container_id: The container_id of this ListContainerCmdLogsRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ListContainerCmdLogsRequest.

        产生日志的容器名称

        :return: The container_name of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListContainerCmdLogsRequest.

        产生日志的容器名称

        :param container_name: The container_name of this ListContainerCmdLogsRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def cmd(self):
        r"""Gets the cmd of this ListContainerCmdLogsRequest.

        运行的命令行

        :return: The cmd of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this ListContainerCmdLogsRequest.

        运行的命令行

        :param cmd: The cmd of this ListContainerCmdLogsRequest.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def path(self):
        r"""Gets the path of this ListContainerCmdLogsRequest.

        命令行对应的进程路径

        :return: The path of this ListContainerCmdLogsRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListContainerCmdLogsRequest.

        命令行对应的进程路径

        :param path: The path of this ListContainerCmdLogsRequest.
        :type path: str
        """
        self._path = path

    @property
    def start_time(self):
        r"""Gets the start_time of this ListContainerCmdLogsRequest.

        查询日志范围的最小时间

        :return: The start_time of this ListContainerCmdLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListContainerCmdLogsRequest.

        查询日志范围的最小时间

        :param start_time: The start_time of this ListContainerCmdLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListContainerCmdLogsRequest.

        查询日志范围的最大时间

        :return: The end_time of this ListContainerCmdLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListContainerCmdLogsRequest.

        查询日志范围的最大时间

        :param end_time: The end_time of this ListContainerCmdLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListContainerCmdLogsRequest.

        每页显示个数，默认为10

        :return: The limit of this ListContainerCmdLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContainerCmdLogsRequest.

        每页显示个数，默认为10

        :param limit: The limit of this ListContainerCmdLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContainerCmdLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListContainerCmdLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContainerCmdLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListContainerCmdLogsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListContainerCmdLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
