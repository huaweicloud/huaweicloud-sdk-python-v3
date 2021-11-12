# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ALSDatasDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'category': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'collect_time': 'str',
        'container_name': 'str',
        'host_ip': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'line_num': 'str',
        'log_content': 'str',
        'log_content_size': 'str',
        'loghash': 'str',
        'name_space': 'str',
        'path_file': 'str',
        'pod_name': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'app_name': 'appName',
        'category': 'category',
        'cluster_id': 'clusterId',
        'cluster_name': 'clusterName',
        'collect_time': 'collectTime',
        'container_name': 'containerName',
        'host_ip': 'hostIP',
        'host_id': 'hostId',
        'host_name': 'hostName',
        'line_num': 'lineNum',
        'log_content': 'logContent',
        'log_content_size': 'logContentSize',
        'loghash': 'loghash',
        'name_space': 'nameSpace',
        'path_file': 'pathFile',
        'pod_name': 'podName',
        'service_id': 'serviceID'
    }

    def __init__(self, app_name=None, category=None, cluster_id=None, cluster_name=None, collect_time=None, container_name=None, host_ip=None, host_id=None, host_name=None, line_num=None, log_content=None, log_content_size=None, loghash=None, name_space=None, path_file=None, pod_name=None, service_id=None):
        """ALSDatasDetail - a model defined in huaweicloud sdk"""
        
        

        self._app_name = None
        self._category = None
        self._cluster_id = None
        self._cluster_name = None
        self._collect_time = None
        self._container_name = None
        self._host_ip = None
        self._host_id = None
        self._host_name = None
        self._line_num = None
        self._log_content = None
        self._log_content_size = None
        self._loghash = None
        self._name_space = None
        self._path_file = None
        self._pod_name = None
        self._service_id = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if category is not None:
            self.category = category
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if collect_time is not None:
            self.collect_time = collect_time
        if container_name is not None:
            self.container_name = container_name
        if host_ip is not None:
            self.host_ip = host_ip
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if line_num is not None:
            self.line_num = line_num
        if log_content is not None:
            self.log_content = log_content
        if log_content_size is not None:
            self.log_content_size = log_content_size
        if loghash is not None:
            self.loghash = loghash
        if name_space is not None:
            self.name_space = name_space
        if path_file is not None:
            self.path_file = path_file
        if pod_name is not None:
            self.pod_name = pod_name
        if service_id is not None:
            self.service_id = service_id

    @property
    def app_name(self):
        """Gets the app_name of this ALSDatasDetail.

        服务名称。

        :return: The app_name of this ALSDatasDetail.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ALSDatasDetail.

        服务名称。

        :param app_name: The app_name of this ALSDatasDetail.
        :type: str
        """
        self._app_name = app_name

    @property
    def category(self):
        """Gets the category of this ALSDatasDetail.

        日志类型。

        :return: The category of this ALSDatasDetail.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ALSDatasDetail.

        日志类型。

        :param category: The category of this ALSDatasDetail.
        :type: str
        """
        self._category = category

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ALSDatasDetail.

        CCE集群ID。

        :return: The cluster_id of this ALSDatasDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ALSDatasDetail.

        CCE集群ID。

        :param cluster_id: The cluster_id of this ALSDatasDetail.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ALSDatasDetail.

        CCE集群名称。

        :return: The cluster_name of this ALSDatasDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ALSDatasDetail.

        CCE集群名称。

        :param cluster_name: The cluster_name of this ALSDatasDetail.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def collect_time(self):
        """Gets the collect_time of this ALSDatasDetail.

        日志采集时间，UTC时间，毫秒级。

        :return: The collect_time of this ALSDatasDetail.
        :rtype: str
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this ALSDatasDetail.

        日志采集时间，UTC时间，毫秒级。

        :param collect_time: The collect_time of this ALSDatasDetail.
        :type: str
        """
        self._collect_time = collect_time

    @property
    def container_name(self):
        """Gets the container_name of this ALSDatasDetail.

        CCE容器名称。

        :return: The container_name of this ALSDatasDetail.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ALSDatasDetail.

        CCE容器名称。

        :param container_name: The container_name of this ALSDatasDetail.
        :type: str
        """
        self._container_name = container_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ALSDatasDetail.

        日志文件所在虚拟机主机IP。

        :return: The host_ip of this ALSDatasDetail.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ALSDatasDetail.

        日志文件所在虚拟机主机IP。

        :param host_ip: The host_ip of this ALSDatasDetail.
        :type: str
        """
        self._host_ip = host_ip

    @property
    def host_id(self):
        """Gets the host_id of this ALSDatasDetail.

        主机在集群中的ID。

        :return: The host_id of this ALSDatasDetail.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ALSDatasDetail.

        主机在集群中的ID。

        :param host_id: The host_id of this ALSDatasDetail.
        :type: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ALSDatasDetail.

        日志所在虚拟机名称。

        :return: The host_name of this ALSDatasDetail.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ALSDatasDetail.

        日志所在虚拟机名称。

        :param host_name: The host_name of this ALSDatasDetail.
        :type: str
        """
        self._host_name = host_name

    @property
    def line_num(self):
        """Gets the line_num of this ALSDatasDetail.

        日志单序列号。

        :return: The line_num of this ALSDatasDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this ALSDatasDetail.

        日志单序列号。

        :param line_num: The line_num of this ALSDatasDetail.
        :type: str
        """
        self._line_num = line_num

    @property
    def log_content(self):
        """Gets the log_content of this ALSDatasDetail.

        日志原数据。

        :return: The log_content of this ALSDatasDetail.
        :rtype: str
        """
        return self._log_content

    @log_content.setter
    def log_content(self, log_content):
        """Sets the log_content of this ALSDatasDetail.

        日志原数据。

        :param log_content: The log_content of this ALSDatasDetail.
        :type: str
        """
        self._log_content = log_content

    @property
    def log_content_size(self):
        """Gets the log_content_size of this ALSDatasDetail.

        单行日志大小。

        :return: The log_content_size of this ALSDatasDetail.
        :rtype: str
        """
        return self._log_content_size

    @log_content_size.setter
    def log_content_size(self, log_content_size):
        """Sets the log_content_size of this ALSDatasDetail.

        单行日志大小。

        :param log_content_size: The log_content_size of this ALSDatasDetail.
        :type: str
        """
        self._log_content_size = log_content_size

    @property
    def loghash(self):
        """Gets the loghash of this ALSDatasDetail.

        日志来源HASH值。

        :return: The loghash of this ALSDatasDetail.
        :rtype: str
        """
        return self._loghash

    @loghash.setter
    def loghash(self, loghash):
        """Sets the loghash of this ALSDatasDetail.

        日志来源HASH值。

        :param loghash: The loghash of this ALSDatasDetail.
        :type: str
        """
        self._loghash = loghash

    @property
    def name_space(self):
        """Gets the name_space of this ALSDatasDetail.

        CCE集群命名空间。

        :return: The name_space of this ALSDatasDetail.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this ALSDatasDetail.

        CCE集群命名空间。

        :param name_space: The name_space of this ALSDatasDetail.
        :type: str
        """
        self._name_space = name_space

    @property
    def path_file(self):
        """Gets the path_file of this ALSDatasDetail.

        日志文件绝对路径。

        :return: The path_file of this ALSDatasDetail.
        :rtype: str
        """
        return self._path_file

    @path_file.setter
    def path_file(self, path_file):
        """Sets the path_file of this ALSDatasDetail.

        日志文件绝对路径。

        :param path_file: The path_file of this ALSDatasDetail.
        :type: str
        """
        self._path_file = path_file

    @property
    def pod_name(self):
        """Gets the pod_name of this ALSDatasDetail.

        CCE容器实例名称。

        :return: The pod_name of this ALSDatasDetail.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this ALSDatasDetail.

        CCE容器实例名称。

        :param pod_name: The pod_name of this ALSDatasDetail.
        :type: str
        """
        self._pod_name = pod_name

    @property
    def service_id(self):
        """Gets the service_id of this ALSDatasDetail.

        AOM资源—服务ID。

        :return: The service_id of this ALSDatasDetail.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ALSDatasDetail.

        AOM资源—服务ID。

        :param service_id: The service_id of this ALSDatasDetail.
        :type: str
        """
        self._service_id = service_id

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
        if not isinstance(other, ALSDatasDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
