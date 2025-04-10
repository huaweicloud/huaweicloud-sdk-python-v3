# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PGSQLInstanceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coordinator_resource_spec': 'str',
        'coordinator_pod_label': 'str',
        'worker_resource_spec': 'str',
        'worker_pod_label': 'str',
        'coordinator_port': 'int',
        'runtime_param': 'str'
    }

    attribute_map = {
        'coordinator_resource_spec': 'coordinator_resource_spec',
        'coordinator_pod_label': 'coordinator_pod_label',
        'worker_resource_spec': 'worker_resource_spec',
        'worker_pod_label': 'worker_pod_label',
        'coordinator_port': 'coordinator_port',
        'runtime_param': 'runtime_param'
    }

    def __init__(self, coordinator_resource_spec=None, coordinator_pod_label=None, worker_resource_spec=None, worker_pod_label=None, coordinator_port=None, runtime_param=None):
        r"""PGSQLInstanceConfig

        The model defined in huaweicloud sdk

        :param coordinator_resource_spec: 资源规格，从规格列表查询获取。
        :type coordinator_resource_spec: str
        :param coordinator_pod_label: Coordinator的POD标签
        :type coordinator_pod_label: str
        :param worker_resource_spec: 资源规格，从规格列表查询获取。
        :type worker_resource_spec: str
        :param worker_pod_label: Worker的POD标签
        :type worker_pod_label: str
        :param coordinator_port: Coordinator对外服务的端口
        :type coordinator_port: int
        :param runtime_param: json格式 元数据以及data位置信息
        :type runtime_param: str
        """
        
        

        self._coordinator_resource_spec = None
        self._coordinator_pod_label = None
        self._worker_resource_spec = None
        self._worker_pod_label = None
        self._coordinator_port = None
        self._runtime_param = None
        self.discriminator = None

        self.coordinator_resource_spec = coordinator_resource_spec
        self.coordinator_pod_label = coordinator_pod_label
        self.worker_resource_spec = worker_resource_spec
        self.worker_pod_label = worker_pod_label
        self.coordinator_port = coordinator_port
        self.runtime_param = runtime_param

    @property
    def coordinator_resource_spec(self):
        r"""Gets the coordinator_resource_spec of this PGSQLInstanceConfig.

        资源规格，从规格列表查询获取。

        :return: The coordinator_resource_spec of this PGSQLInstanceConfig.
        :rtype: str
        """
        return self._coordinator_resource_spec

    @coordinator_resource_spec.setter
    def coordinator_resource_spec(self, coordinator_resource_spec):
        r"""Sets the coordinator_resource_spec of this PGSQLInstanceConfig.

        资源规格，从规格列表查询获取。

        :param coordinator_resource_spec: The coordinator_resource_spec of this PGSQLInstanceConfig.
        :type coordinator_resource_spec: str
        """
        self._coordinator_resource_spec = coordinator_resource_spec

    @property
    def coordinator_pod_label(self):
        r"""Gets the coordinator_pod_label of this PGSQLInstanceConfig.

        Coordinator的POD标签

        :return: The coordinator_pod_label of this PGSQLInstanceConfig.
        :rtype: str
        """
        return self._coordinator_pod_label

    @coordinator_pod_label.setter
    def coordinator_pod_label(self, coordinator_pod_label):
        r"""Sets the coordinator_pod_label of this PGSQLInstanceConfig.

        Coordinator的POD标签

        :param coordinator_pod_label: The coordinator_pod_label of this PGSQLInstanceConfig.
        :type coordinator_pod_label: str
        """
        self._coordinator_pod_label = coordinator_pod_label

    @property
    def worker_resource_spec(self):
        r"""Gets the worker_resource_spec of this PGSQLInstanceConfig.

        资源规格，从规格列表查询获取。

        :return: The worker_resource_spec of this PGSQLInstanceConfig.
        :rtype: str
        """
        return self._worker_resource_spec

    @worker_resource_spec.setter
    def worker_resource_spec(self, worker_resource_spec):
        r"""Sets the worker_resource_spec of this PGSQLInstanceConfig.

        资源规格，从规格列表查询获取。

        :param worker_resource_spec: The worker_resource_spec of this PGSQLInstanceConfig.
        :type worker_resource_spec: str
        """
        self._worker_resource_spec = worker_resource_spec

    @property
    def worker_pod_label(self):
        r"""Gets the worker_pod_label of this PGSQLInstanceConfig.

        Worker的POD标签

        :return: The worker_pod_label of this PGSQLInstanceConfig.
        :rtype: str
        """
        return self._worker_pod_label

    @worker_pod_label.setter
    def worker_pod_label(self, worker_pod_label):
        r"""Sets the worker_pod_label of this PGSQLInstanceConfig.

        Worker的POD标签

        :param worker_pod_label: The worker_pod_label of this PGSQLInstanceConfig.
        :type worker_pod_label: str
        """
        self._worker_pod_label = worker_pod_label

    @property
    def coordinator_port(self):
        r"""Gets the coordinator_port of this PGSQLInstanceConfig.

        Coordinator对外服务的端口

        :return: The coordinator_port of this PGSQLInstanceConfig.
        :rtype: int
        """
        return self._coordinator_port

    @coordinator_port.setter
    def coordinator_port(self, coordinator_port):
        r"""Sets the coordinator_port of this PGSQLInstanceConfig.

        Coordinator对外服务的端口

        :param coordinator_port: The coordinator_port of this PGSQLInstanceConfig.
        :type coordinator_port: int
        """
        self._coordinator_port = coordinator_port

    @property
    def runtime_param(self):
        r"""Gets the runtime_param of this PGSQLInstanceConfig.

        json格式 元数据以及data位置信息

        :return: The runtime_param of this PGSQLInstanceConfig.
        :rtype: str
        """
        return self._runtime_param

    @runtime_param.setter
    def runtime_param(self, runtime_param):
        r"""Sets the runtime_param of this PGSQLInstanceConfig.

        json格式 元数据以及data位置信息

        :param runtime_param: The runtime_param of this PGSQLInstanceConfig.
        :type runtime_param: str
        """
        self._runtime_param = runtime_param

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
        if not isinstance(other, PGSQLInstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
