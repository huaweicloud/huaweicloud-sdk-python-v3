# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type_code': 'str',
        'code': 'str',
        'iaas_code': 'str',
        'cpu': 'str',
        'mem': 'str',
        'max_connections': 'str',
        'server_type': 'str',
        'architecture': 'str',
        'az_status': 'object',
        'region_status': 'str',
        'group_type': 'str',
        'db_type': 'str',
        'extend_fields': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type_code': 'typeCode',
        'code': 'code',
        'iaas_code': 'iaasCode',
        'cpu': 'cpu',
        'mem': 'mem',
        'max_connections': 'maxConnections',
        'server_type': 'serverType',
        'architecture': 'architecture',
        'az_status': 'azStatus',
        'region_status': 'regionStatus',
        'group_type': 'groupType',
        'db_type': 'dbType',
        'extend_fields': 'extendFields'
    }

    def __init__(self, id=None, type_code=None, code=None, iaas_code=None, cpu=None, mem=None, max_connections=None, server_type=None, architecture=None, az_status=None, region_status=None, group_type=None, db_type=None, extend_fields=None):
        """ComputeFlavors

        The model defined in huaweicloud sdk

        :param id: 规格id。
        :type id: str
        :param type_code: 资源类型编码。
        :type type_code: str
        :param code: DDM内部记录的虚机规格类型。
        :type code: str
        :param iaas_code: iaas记录的虚机规格类型。
        :type iaas_code: str
        :param cpu: cpu核数。
        :type cpu: str
        :param mem: 内存大小,单位:G。
        :type mem: str
        :param max_connections: 最大连接数。
        :type max_connections: str
        :param server_type: 计算资源服务类型。
        :type server_type: str
        :param architecture: 计算资源架构类型，目前分X86和ARM两种。
        :type architecture: str
        :param az_status: 可用区状态。
        :type az_status: object
        :param region_status: 局点状态。
        :type region_status: str
        :param group_type: 计算资源架构类型，目前分X86和ARM两种。
        :type group_type: str
        :param db_type: 服务引擎类型。
        :type db_type: str
        :param extend_fields: 扩展字段，目前存储可用区相关信息。
        :type extend_fields: object
        """
        
        

        self._id = None
        self._type_code = None
        self._code = None
        self._iaas_code = None
        self._cpu = None
        self._mem = None
        self._max_connections = None
        self._server_type = None
        self._architecture = None
        self._az_status = None
        self._region_status = None
        self._group_type = None
        self._db_type = None
        self._extend_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type_code is not None:
            self.type_code = type_code
        if code is not None:
            self.code = code
        if iaas_code is not None:
            self.iaas_code = iaas_code
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if max_connections is not None:
            self.max_connections = max_connections
        if server_type is not None:
            self.server_type = server_type
        if architecture is not None:
            self.architecture = architecture
        if az_status is not None:
            self.az_status = az_status
        if region_status is not None:
            self.region_status = region_status
        if group_type is not None:
            self.group_type = group_type
        if db_type is not None:
            self.db_type = db_type
        if extend_fields is not None:
            self.extend_fields = extend_fields

    @property
    def id(self):
        """Gets the id of this ComputeFlavors.

        规格id。

        :return: The id of this ComputeFlavors.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComputeFlavors.

        规格id。

        :param id: The id of this ComputeFlavors.
        :type id: str
        """
        self._id = id

    @property
    def type_code(self):
        """Gets the type_code of this ComputeFlavors.

        资源类型编码。

        :return: The type_code of this ComputeFlavors.
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this ComputeFlavors.

        资源类型编码。

        :param type_code: The type_code of this ComputeFlavors.
        :type type_code: str
        """
        self._type_code = type_code

    @property
    def code(self):
        """Gets the code of this ComputeFlavors.

        DDM内部记录的虚机规格类型。

        :return: The code of this ComputeFlavors.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ComputeFlavors.

        DDM内部记录的虚机规格类型。

        :param code: The code of this ComputeFlavors.
        :type code: str
        """
        self._code = code

    @property
    def iaas_code(self):
        """Gets the iaas_code of this ComputeFlavors.

        iaas记录的虚机规格类型。

        :return: The iaas_code of this ComputeFlavors.
        :rtype: str
        """
        return self._iaas_code

    @iaas_code.setter
    def iaas_code(self, iaas_code):
        """Sets the iaas_code of this ComputeFlavors.

        iaas记录的虚机规格类型。

        :param iaas_code: The iaas_code of this ComputeFlavors.
        :type iaas_code: str
        """
        self._iaas_code = iaas_code

    @property
    def cpu(self):
        """Gets the cpu of this ComputeFlavors.

        cpu核数。

        :return: The cpu of this ComputeFlavors.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ComputeFlavors.

        cpu核数。

        :param cpu: The cpu of this ComputeFlavors.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this ComputeFlavors.

        内存大小,单位:G。

        :return: The mem of this ComputeFlavors.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this ComputeFlavors.

        内存大小,单位:G。

        :param mem: The mem of this ComputeFlavors.
        :type mem: str
        """
        self._mem = mem

    @property
    def max_connections(self):
        """Gets the max_connections of this ComputeFlavors.

        最大连接数。

        :return: The max_connections of this ComputeFlavors.
        :rtype: str
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this ComputeFlavors.

        最大连接数。

        :param max_connections: The max_connections of this ComputeFlavors.
        :type max_connections: str
        """
        self._max_connections = max_connections

    @property
    def server_type(self):
        """Gets the server_type of this ComputeFlavors.

        计算资源服务类型。

        :return: The server_type of this ComputeFlavors.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this ComputeFlavors.

        计算资源服务类型。

        :param server_type: The server_type of this ComputeFlavors.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def architecture(self):
        """Gets the architecture of this ComputeFlavors.

        计算资源架构类型，目前分X86和ARM两种。

        :return: The architecture of this ComputeFlavors.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ComputeFlavors.

        计算资源架构类型，目前分X86和ARM两种。

        :param architecture: The architecture of this ComputeFlavors.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def az_status(self):
        """Gets the az_status of this ComputeFlavors.

        可用区状态。

        :return: The az_status of this ComputeFlavors.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this ComputeFlavors.

        可用区状态。

        :param az_status: The az_status of this ComputeFlavors.
        :type az_status: object
        """
        self._az_status = az_status

    @property
    def region_status(self):
        """Gets the region_status of this ComputeFlavors.

        局点状态。

        :return: The region_status of this ComputeFlavors.
        :rtype: str
        """
        return self._region_status

    @region_status.setter
    def region_status(self, region_status):
        """Sets the region_status of this ComputeFlavors.

        局点状态。

        :param region_status: The region_status of this ComputeFlavors.
        :type region_status: str
        """
        self._region_status = region_status

    @property
    def group_type(self):
        """Gets the group_type of this ComputeFlavors.

        计算资源架构类型，目前分X86和ARM两种。

        :return: The group_type of this ComputeFlavors.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this ComputeFlavors.

        计算资源架构类型，目前分X86和ARM两种。

        :param group_type: The group_type of this ComputeFlavors.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def db_type(self):
        """Gets the db_type of this ComputeFlavors.

        服务引擎类型。

        :return: The db_type of this ComputeFlavors.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this ComputeFlavors.

        服务引擎类型。

        :param db_type: The db_type of this ComputeFlavors.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def extend_fields(self):
        """Gets the extend_fields of this ComputeFlavors.

        扩展字段，目前存储可用区相关信息。

        :return: The extend_fields of this ComputeFlavors.
        :rtype: object
        """
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, extend_fields):
        """Sets the extend_fields of this ComputeFlavors.

        扩展字段，目前存储可用区相关信息。

        :param extend_fields: The extend_fields of this ComputeFlavors.
        :type extend_fields: object
        """
        self._extend_fields = extend_fields

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
        if not isinstance(other, ComputeFlavors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
