# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoCCECreate:

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
        'namespace': 'str',
        'workload_type': 'str',
        'app_name': 'str',
        'label_key': 'str',
        'label_value': 'str',
        'version': 'str',
        'port': 'int',
        'labels': 'list[MicroserviceLabel]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'namespace': 'namespace',
        'workload_type': 'workload_type',
        'app_name': 'app_name',
        'label_key': 'label_key',
        'label_value': 'label_value',
        'version': 'version',
        'port': 'port',
        'labels': 'labels'
    }

    def __init__(self, cluster_id=None, namespace=None, workload_type=None, app_name=None, label_key=None, label_value=None, version=None, port=None, labels=None):
        """MicroServiceInfoCCECreate

        The model defined in huaweicloud sdk

        :param cluster_id: 云容器引擎集群编号
        :type cluster_id: str
        :param namespace: 命名空间
        :type namespace: str
        :param workload_type: 工作负载类型  - deployment：无状态负载  - statefulset：有状态负载  - daemonset：守护进程集
        :type workload_type: str
        :param app_name: APP名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type app_name: str
        :param label_key: 服务标识名。支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号，且只能以英文、汉字和数字开头，1-64个字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type label_key: str
        :param label_value: 服务标识值。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type label_value: str
        :param version: 工作负载的版本
        :type version: str
        :param port: 工作负载的监听端口号
        :type port: int
        :param labels: 工作负载的标签列表。
        :type labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        
        

        self._cluster_id = None
        self._namespace = None
        self._workload_type = None
        self._app_name = None
        self._label_key = None
        self._label_value = None
        self._version = None
        self._port = None
        self._labels = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.namespace = namespace
        self.workload_type = workload_type
        if app_name is not None:
            self.app_name = app_name
        if label_key is not None:
            self.label_key = label_key
        if label_value is not None:
            self.label_value = label_value
        if version is not None:
            self.version = version
        self.port = port
        if labels is not None:
            self.labels = labels

    @property
    def cluster_id(self):
        """Gets the cluster_id of this MicroServiceInfoCCECreate.

        云容器引擎集群编号

        :return: The cluster_id of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this MicroServiceInfoCCECreate.

        云容器引擎集群编号

        :param cluster_id: The cluster_id of this MicroServiceInfoCCECreate.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        """Gets the namespace of this MicroServiceInfoCCECreate.

        命名空间

        :return: The namespace of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MicroServiceInfoCCECreate.

        命名空间

        :param namespace: The namespace of this MicroServiceInfoCCECreate.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def workload_type(self):
        """Gets the workload_type of this MicroServiceInfoCCECreate.

        工作负载类型  - deployment：无状态负载  - statefulset：有状态负载  - daemonset：守护进程集

        :return: The workload_type of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """Sets the workload_type of this MicroServiceInfoCCECreate.

        工作负载类型  - deployment：无状态负载  - statefulset：有状态负载  - daemonset：守护进程集

        :param workload_type: The workload_type of this MicroServiceInfoCCECreate.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def app_name(self):
        """Gets the app_name of this MicroServiceInfoCCECreate.

        APP名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The app_name of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this MicroServiceInfoCCECreate.

        APP名称。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param app_name: The app_name of this MicroServiceInfoCCECreate.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def label_key(self):
        """Gets the label_key of this MicroServiceInfoCCECreate.

        服务标识名。支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号，且只能以英文、汉字和数字开头，1-64个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The label_key of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._label_key

    @label_key.setter
    def label_key(self, label_key):
        """Sets the label_key of this MicroServiceInfoCCECreate.

        服务标识名。支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号，且只能以英文、汉字和数字开头，1-64个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param label_key: The label_key of this MicroServiceInfoCCECreate.
        :type label_key: str
        """
        self._label_key = label_key

    @property
    def label_value(self):
        """Gets the label_value of this MicroServiceInfoCCECreate.

        服务标识值。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The label_value of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._label_value

    @label_value.setter
    def label_value(self, label_value):
        """Sets the label_value of this MicroServiceInfoCCECreate.

        服务标识值。支持汉字，英文，数字，点，中划线，下划线，且只能以英文和汉字开头，1-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param label_value: The label_value of this MicroServiceInfoCCECreate.
        :type label_value: str
        """
        self._label_value = label_value

    @property
    def version(self):
        """Gets the version of this MicroServiceInfoCCECreate.

        工作负载的版本

        :return: The version of this MicroServiceInfoCCECreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MicroServiceInfoCCECreate.

        工作负载的版本

        :param version: The version of this MicroServiceInfoCCECreate.
        :type version: str
        """
        self._version = version

    @property
    def port(self):
        """Gets the port of this MicroServiceInfoCCECreate.

        工作负载的监听端口号

        :return: The port of this MicroServiceInfoCCECreate.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MicroServiceInfoCCECreate.

        工作负载的监听端口号

        :param port: The port of this MicroServiceInfoCCECreate.
        :type port: int
        """
        self._port = port

    @property
    def labels(self):
        """Gets the labels of this MicroServiceInfoCCECreate.

        工作负载的标签列表。

        :return: The labels of this MicroServiceInfoCCECreate.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MicroServiceInfoCCECreate.

        工作负载的标签列表。

        :param labels: The labels of this MicroServiceInfoCCECreate.
        :type labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        self._labels = labels

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
        if not isinstance(other, MicroServiceInfoCCECreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
