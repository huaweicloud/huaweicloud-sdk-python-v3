# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchKey:

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
        'cluster_id': 'str',
        'host_ip': 'str',
        'name_space': 'str',
        'path_file': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'app_name': 'appName',
        'cluster_id': 'clusterId',
        'host_ip': 'hostIP',
        'name_space': 'nameSpace',
        'path_file': 'pathFile',
        'pod_name': 'podName'
    }

    def __init__(self, app_name=None, cluster_id=None, host_ip=None, name_space=None, path_file=None, pod_name=None):
        r"""SearchKey

        The model defined in huaweicloud sdk

        :param app_name: 应用名称。
        :type app_name: str
        :param cluster_id: CCE集群ID。
        :type cluster_id: str
        :param host_ip: 日志所在虚拟机IP。
        :type host_ip: str
        :param name_space: CCE容器集群的命名空间。
        :type name_space: str
        :param path_file: 日志文件名称。
        :type path_file: str
        :param pod_name: 容器实例名称。
        :type pod_name: str
        """
        
        

        self._app_name = None
        self._cluster_id = None
        self._host_ip = None
        self._name_space = None
        self._path_file = None
        self._pod_name = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        self.cluster_id = cluster_id
        if host_ip is not None:
            self.host_ip = host_ip
        if name_space is not None:
            self.name_space = name_space
        if path_file is not None:
            self.path_file = path_file
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def app_name(self):
        r"""Gets the app_name of this SearchKey.

        应用名称。

        :return: The app_name of this SearchKey.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this SearchKey.

        应用名称。

        :param app_name: The app_name of this SearchKey.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this SearchKey.

        CCE集群ID。

        :return: The cluster_id of this SearchKey.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this SearchKey.

        CCE集群ID。

        :param cluster_id: The cluster_id of this SearchKey.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this SearchKey.

        日志所在虚拟机IP。

        :return: The host_ip of this SearchKey.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this SearchKey.

        日志所在虚拟机IP。

        :param host_ip: The host_ip of this SearchKey.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def name_space(self):
        r"""Gets the name_space of this SearchKey.

        CCE容器集群的命名空间。

        :return: The name_space of this SearchKey.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        r"""Sets the name_space of this SearchKey.

        CCE容器集群的命名空间。

        :param name_space: The name_space of this SearchKey.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def path_file(self):
        r"""Gets the path_file of this SearchKey.

        日志文件名称。

        :return: The path_file of this SearchKey.
        :rtype: str
        """
        return self._path_file

    @path_file.setter
    def path_file(self, path_file):
        r"""Sets the path_file of this SearchKey.

        日志文件名称。

        :param path_file: The path_file of this SearchKey.
        :type path_file: str
        """
        self._path_file = path_file

    @property
    def pod_name(self):
        r"""Gets the pod_name of this SearchKey.

        容器实例名称。

        :return: The pod_name of this SearchKey.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this SearchKey.

        容器实例名称。

        :param pod_name: The pod_name of this SearchKey.
        :type pod_name: str
        """
        self._pod_name = pod_name

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
        if not isinstance(other, SearchKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
