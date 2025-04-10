# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'master_node_id': 'str',
        'instance_name': 'str',
        'cpu': 'int',
        'mem': 'int',
        'disk_size': 'int',
        'disk_type': 'str',
        'engine': 'str',
        'engine_version': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'master_node_id': 'master_node_id',
        'instance_name': 'instance_name',
        'cpu': 'cpu',
        'mem': 'mem',
        'disk_size': 'disk_size',
        'disk_type': 'disk_type',
        'engine': 'engine',
        'engine_version': 'engine_version'
    }

    def __init__(self, tenant_id=None, project_id=None, instance_id=None, master_node_id=None, instance_name=None, cpu=None, mem=None, disk_size=None, disk_type=None, engine=None, engine_version=None):
        r"""HealthReportInstanceInfo

        The model defined in huaweicloud sdk

        :param tenant_id: 账号ID。
        :type tenant_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param master_node_id: 主节点ID。
        :type master_node_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param cpu: 实例cpu核数。
        :type cpu: int
        :param mem: 实例内存大小。
        :type mem: int
        :param disk_size: 磁盘大小。
        :type disk_size: int
        :param disk_type: 磁盘类型。
        :type disk_type: str
        :param engine: 实例引擎类型。
        :type engine: str
        :param engine_version: 引擎内核版本。
        :type engine_version: str
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._instance_id = None
        self._master_node_id = None
        self._instance_name = None
        self._cpu = None
        self._mem = None
        self._disk_size = None
        self._disk_type = None
        self._engine = None
        self._engine_version = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        self.instance_id = instance_id
        self.master_node_id = master_node_id
        self.instance_name = instance_name
        self.cpu = cpu
        self.mem = mem
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.engine = engine
        self.engine_version = engine_version

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this HealthReportInstanceInfo.

        账号ID。

        :return: The tenant_id of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this HealthReportInstanceInfo.

        账号ID。

        :param tenant_id: The tenant_id of this HealthReportInstanceInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this HealthReportInstanceInfo.

        项目ID。

        :return: The project_id of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HealthReportInstanceInfo.

        项目ID。

        :param project_id: The project_id of this HealthReportInstanceInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this HealthReportInstanceInfo.

        实例ID。

        :return: The instance_id of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this HealthReportInstanceInfo.

        实例ID。

        :param instance_id: The instance_id of this HealthReportInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def master_node_id(self):
        r"""Gets the master_node_id of this HealthReportInstanceInfo.

        主节点ID。

        :return: The master_node_id of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._master_node_id

    @master_node_id.setter
    def master_node_id(self, master_node_id):
        r"""Sets the master_node_id of this HealthReportInstanceInfo.

        主节点ID。

        :param master_node_id: The master_node_id of this HealthReportInstanceInfo.
        :type master_node_id: str
        """
        self._master_node_id = master_node_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this HealthReportInstanceInfo.

        实例名称。

        :return: The instance_name of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this HealthReportInstanceInfo.

        实例名称。

        :param instance_name: The instance_name of this HealthReportInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def cpu(self):
        r"""Gets the cpu of this HealthReportInstanceInfo.

        实例cpu核数。

        :return: The cpu of this HealthReportInstanceInfo.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this HealthReportInstanceInfo.

        实例cpu核数。

        :param cpu: The cpu of this HealthReportInstanceInfo.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this HealthReportInstanceInfo.

        实例内存大小。

        :return: The mem of this HealthReportInstanceInfo.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this HealthReportInstanceInfo.

        实例内存大小。

        :param mem: The mem of this HealthReportInstanceInfo.
        :type mem: int
        """
        self._mem = mem

    @property
    def disk_size(self):
        r"""Gets the disk_size of this HealthReportInstanceInfo.

        磁盘大小。

        :return: The disk_size of this HealthReportInstanceInfo.
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        r"""Sets the disk_size of this HealthReportInstanceInfo.

        磁盘大小。

        :param disk_size: The disk_size of this HealthReportInstanceInfo.
        :type disk_size: int
        """
        self._disk_size = disk_size

    @property
    def disk_type(self):
        r"""Gets the disk_type of this HealthReportInstanceInfo.

        磁盘类型。

        :return: The disk_type of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        r"""Sets the disk_type of this HealthReportInstanceInfo.

        磁盘类型。

        :param disk_type: The disk_type of this HealthReportInstanceInfo.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def engine(self):
        r"""Gets the engine of this HealthReportInstanceInfo.

        实例引擎类型。

        :return: The engine of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this HealthReportInstanceInfo.

        实例引擎类型。

        :param engine: The engine of this HealthReportInstanceInfo.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this HealthReportInstanceInfo.

        引擎内核版本。

        :return: The engine_version of this HealthReportInstanceInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this HealthReportInstanceInfo.

        引擎内核版本。

        :param engine_version: The engine_version of this HealthReportInstanceInfo.
        :type engine_version: str
        """
        self._engine_version = engine_version

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
        if not isinstance(other, HealthReportInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
