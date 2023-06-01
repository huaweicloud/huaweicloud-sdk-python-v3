# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineFlavorData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'str',
        'ram': 'str',
        'spec_code': 'str',
        'is_ipv6_supported': 'bool',
        'type_code': 'str',
        'az_status': 'dict(str, str)',
        'group_type': 'str',
        'max_connection': 'str',
        'tps': 'str',
        'qps': 'str',
        'min_volume_size': 'str',
        'max_volume_size': 'str'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'is_ipv6_supported': 'is_ipv6_supported',
        'type_code': 'type_code',
        'az_status': 'az_status',
        'group_type': 'group_type',
        'max_connection': 'max_connection',
        'tps': 'tps',
        'qps': 'qps',
        'min_volume_size': 'min_volume_size',
        'max_volume_size': 'max_volume_size'
    }

    def __init__(self, vcpus=None, ram=None, spec_code=None, is_ipv6_supported=None, type_code=None, az_status=None, group_type=None, max_connection=None, tps=None, qps=None, min_volume_size=None, max_volume_size=None):
        """EngineFlavorData

        The model defined in huaweicloud sdk

        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param spec_code: 资源规格编码。例如：rds.mysql.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “mysql”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。 “rha.rr”表示高可用只读实例，规格编码示例：rds.mysql.n1.large.4.rha.rr。 具有公测权限的用户才可选择高可用，您可联系华为云客服人员申请。 高可用只读功能介绍请参见高可用只读简介。
        :type spec_code: str
        :param is_ipv6_supported: 是否支持ipv6。
        :type is_ipv6_supported: bool
        :param type_code: 资源类型
        :type type_code: str
        :param az_status: 规格所在az的状态，包含以下状态： normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。 abandon：未启用
        :type az_status: dict(str, str)
        :param group_type: 性能规格，包含以下状态： normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于MySQL引擎：独享型。 对于PostgreSQL和SQL Server引擎：独享型，仅云盘SSD支持。 rapid 对于MySQL引擎：独享型（已下线）。 对于PostgreSQL和SQL Server引擎：独享型，仅极速型SSD支持。 bigmem：超大内存型。 highPerformancePrivilegeEdition：超高IO 尊享版
        :type group_type: str
        :param max_connection: 最大连接数
        :type max_connection: str
        :param tps: 数据库每秒执行的事务数，每个事务中包含18条SQL语句。
        :type tps: str
        :param qps: 数据库每秒执行的SQL数，包含insert、select、update、delete等。
        :type qps: str
        :param min_volume_size: 最小磁盘容量，单位G
        :type min_volume_size: str
        :param max_volume_size: 最大磁盘容量，单位G
        :type max_volume_size: str
        """
        
        

        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._is_ipv6_supported = None
        self._type_code = None
        self._az_status = None
        self._group_type = None
        self._max_connection = None
        self._tps = None
        self._qps = None
        self._min_volume_size = None
        self._max_volume_size = None
        self.discriminator = None

        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if spec_code is not None:
            self.spec_code = spec_code
        if is_ipv6_supported is not None:
            self.is_ipv6_supported = is_ipv6_supported
        if type_code is not None:
            self.type_code = type_code
        if az_status is not None:
            self.az_status = az_status
        if group_type is not None:
            self.group_type = group_type
        if max_connection is not None:
            self.max_connection = max_connection
        if tps is not None:
            self.tps = tps
        if qps is not None:
            self.qps = qps
        if min_volume_size is not None:
            self.min_volume_size = min_volume_size
        if max_volume_size is not None:
            self.max_volume_size = max_volume_size

    @property
    def vcpus(self):
        """Gets the vcpus of this EngineFlavorData.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this EngineFlavorData.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this EngineFlavorData.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this EngineFlavorData.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this EngineFlavorData.

        内存大小，单位为GB。

        :return: The ram of this EngineFlavorData.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this EngineFlavorData.

        内存大小，单位为GB。

        :param ram: The ram of this EngineFlavorData.
        :type ram: str
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this EngineFlavorData.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “mysql”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。 “rha.rr”表示高可用只读实例，规格编码示例：rds.mysql.n1.large.4.rha.rr。 具有公测权限的用户才可选择高可用，您可联系华为云客服人员申请。 高可用只读功能介绍请参见高可用只读简介。

        :return: The spec_code of this EngineFlavorData.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this EngineFlavorData.

        资源规格编码。例如：rds.mysql.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “mysql”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。 “rha.rr”表示高可用只读实例，规格编码示例：rds.mysql.n1.large.4.rha.rr。 具有公测权限的用户才可选择高可用，您可联系华为云客服人员申请。 高可用只读功能介绍请参见高可用只读简介。

        :param spec_code: The spec_code of this EngineFlavorData.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def is_ipv6_supported(self):
        """Gets the is_ipv6_supported of this EngineFlavorData.

        是否支持ipv6。

        :return: The is_ipv6_supported of this EngineFlavorData.
        :rtype: bool
        """
        return self._is_ipv6_supported

    @is_ipv6_supported.setter
    def is_ipv6_supported(self, is_ipv6_supported):
        """Sets the is_ipv6_supported of this EngineFlavorData.

        是否支持ipv6。

        :param is_ipv6_supported: The is_ipv6_supported of this EngineFlavorData.
        :type is_ipv6_supported: bool
        """
        self._is_ipv6_supported = is_ipv6_supported

    @property
    def type_code(self):
        """Gets the type_code of this EngineFlavorData.

        资源类型

        :return: The type_code of this EngineFlavorData.
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this EngineFlavorData.

        资源类型

        :param type_code: The type_code of this EngineFlavorData.
        :type type_code: str
        """
        self._type_code = type_code

    @property
    def az_status(self):
        """Gets the az_status of this EngineFlavorData.

        规格所在az的状态，包含以下状态： normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。 abandon：未启用

        :return: The az_status of this EngineFlavorData.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this EngineFlavorData.

        规格所在az的状态，包含以下状态： normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。 abandon：未启用

        :param az_status: The az_status of this EngineFlavorData.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def group_type(self):
        """Gets the group_type of this EngineFlavorData.

        性能规格，包含以下状态： normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于MySQL引擎：独享型。 对于PostgreSQL和SQL Server引擎：独享型，仅云盘SSD支持。 rapid 对于MySQL引擎：独享型（已下线）。 对于PostgreSQL和SQL Server引擎：独享型，仅极速型SSD支持。 bigmem：超大内存型。 highPerformancePrivilegeEdition：超高IO 尊享版

        :return: The group_type of this EngineFlavorData.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this EngineFlavorData.

        性能规格，包含以下状态： normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于MySQL引擎：独享型。 对于PostgreSQL和SQL Server引擎：独享型，仅云盘SSD支持。 rapid 对于MySQL引擎：独享型（已下线）。 对于PostgreSQL和SQL Server引擎：独享型，仅极速型SSD支持。 bigmem：超大内存型。 highPerformancePrivilegeEdition：超高IO 尊享版

        :param group_type: The group_type of this EngineFlavorData.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def max_connection(self):
        """Gets the max_connection of this EngineFlavorData.

        最大连接数

        :return: The max_connection of this EngineFlavorData.
        :rtype: str
        """
        return self._max_connection

    @max_connection.setter
    def max_connection(self, max_connection):
        """Sets the max_connection of this EngineFlavorData.

        最大连接数

        :param max_connection: The max_connection of this EngineFlavorData.
        :type max_connection: str
        """
        self._max_connection = max_connection

    @property
    def tps(self):
        """Gets the tps of this EngineFlavorData.

        数据库每秒执行的事务数，每个事务中包含18条SQL语句。

        :return: The tps of this EngineFlavorData.
        :rtype: str
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this EngineFlavorData.

        数据库每秒执行的事务数，每个事务中包含18条SQL语句。

        :param tps: The tps of this EngineFlavorData.
        :type tps: str
        """
        self._tps = tps

    @property
    def qps(self):
        """Gets the qps of this EngineFlavorData.

        数据库每秒执行的SQL数，包含insert、select、update、delete等。

        :return: The qps of this EngineFlavorData.
        :rtype: str
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this EngineFlavorData.

        数据库每秒执行的SQL数，包含insert、select、update、delete等。

        :param qps: The qps of this EngineFlavorData.
        :type qps: str
        """
        self._qps = qps

    @property
    def min_volume_size(self):
        """Gets the min_volume_size of this EngineFlavorData.

        最小磁盘容量，单位G

        :return: The min_volume_size of this EngineFlavorData.
        :rtype: str
        """
        return self._min_volume_size

    @min_volume_size.setter
    def min_volume_size(self, min_volume_size):
        """Sets the min_volume_size of this EngineFlavorData.

        最小磁盘容量，单位G

        :param min_volume_size: The min_volume_size of this EngineFlavorData.
        :type min_volume_size: str
        """
        self._min_volume_size = min_volume_size

    @property
    def max_volume_size(self):
        """Gets the max_volume_size of this EngineFlavorData.

        最大磁盘容量，单位G

        :return: The max_volume_size of this EngineFlavorData.
        :rtype: str
        """
        return self._max_volume_size

    @max_volume_size.setter
    def max_volume_size(self, max_volume_size):
        """Sets the max_volume_size of this EngineFlavorData.

        最大磁盘容量，单位G

        :param max_volume_size: The max_volume_size of this EngineFlavorData.
        :type max_volume_size: str
        """
        self._max_volume_size = max_volume_size

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
        if not isinstance(other, EngineFlavorData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
