# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructProcessVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'int',
        'src_count': 'int',
        'dst_count': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'src_count': 'src_count',
        'dst_count': 'dst_count',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, type=None, status=None, src_count=None, dst_count=None, start_time=None, end_time=None):
        r"""StructProcessVO

        The model defined in huaweicloud sdk

        :param type: 对象类型 DATABASE：数据库 SCHEMA：SCHEMA PACKAGE：package TABLE：数据表 COLUMN：列 VIEW：视图 FUNCTION：函数 PROCEDURE：存储过程 ROUTINE：routine TRIGGER：触发器 INDEX：索引 TABLE_INDEX：普通索引，根据表汇聚 TABLE_RENAME_OR_COPY：表重命名或复制 TABLE_STRUCTURE：表结构 EVENT：事件 SYNONYM：同义词,sqlserver特有 TYPE：自定义类型,sqlserver特有 RULE：规则,sqlserver特有 DEFAULT：缺省值,sqlserver特有 PLAN_GUIDE：执行计划,sqlserver特有 FILE_GROUP：文件组,sqlserver特有 PARTITION_FUNCTION：分区函数,sqlserver特有 SHARD_KEY：mongo特有 VALIDATOR：mongo特有 SEQUENCE：序列 MATVIEW：物化视图 PARTITION_SCHEME：分区方案,sqlserver特有 ACCOUNT：账户 EXTENSION：PG 特有的一些对象:插件 AGGREGATE：PG 特有的一些对象:聚合函数 MATERIALIZED_VIEW：PG 特有的一些对象:物化视图 TEXT_SEARCH_DICTIONARY：PG 特有的一些对象:文本搜索字典 CONVERSION：PG 特有的一些对象:类型转换 DATA_TYPE：PG 特有的一些对象:数据类型 TEXT_SEARCH_CONFIGURATION：PG 特有的一些对象:文本搜索配置 STATISTICS_EXTENSION：PG 特有的一些对象:插件统计 MEMBERSHIP：PG 特有的一些对象:用户成员关系 EVENT_TRIGGER：PG 特有的一些对象:事件触发器 COLLATION：PG 特有的一些对象:排序规则 TEXT_SEARCH_PARSER：PG 特有的一些对象:文本搜索解析器 PRIVILEGES：PG 特有的一些对象:权限 FOREIGN_KEY：PG 特有的一些对象:外键 ROLE：权限
        :type type: str
        :param status: 状态 1：正在对比中，2：对比完成
        :type status: int
        :param src_count: 源对象数量
        :type src_count: int
        :param dst_count: 目标对象数量
        :type dst_count: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._type = None
        self._status = None
        self._src_count = None
        self._dst_count = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.type = type
        self.status = status
        self.src_count = src_count
        self.dst_count = dst_count
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def type(self):
        r"""Gets the type of this StructProcessVO.

        对象类型 DATABASE：数据库 SCHEMA：SCHEMA PACKAGE：package TABLE：数据表 COLUMN：列 VIEW：视图 FUNCTION：函数 PROCEDURE：存储过程 ROUTINE：routine TRIGGER：触发器 INDEX：索引 TABLE_INDEX：普通索引，根据表汇聚 TABLE_RENAME_OR_COPY：表重命名或复制 TABLE_STRUCTURE：表结构 EVENT：事件 SYNONYM：同义词,sqlserver特有 TYPE：自定义类型,sqlserver特有 RULE：规则,sqlserver特有 DEFAULT：缺省值,sqlserver特有 PLAN_GUIDE：执行计划,sqlserver特有 FILE_GROUP：文件组,sqlserver特有 PARTITION_FUNCTION：分区函数,sqlserver特有 SHARD_KEY：mongo特有 VALIDATOR：mongo特有 SEQUENCE：序列 MATVIEW：物化视图 PARTITION_SCHEME：分区方案,sqlserver特有 ACCOUNT：账户 EXTENSION：PG 特有的一些对象:插件 AGGREGATE：PG 特有的一些对象:聚合函数 MATERIALIZED_VIEW：PG 特有的一些对象:物化视图 TEXT_SEARCH_DICTIONARY：PG 特有的一些对象:文本搜索字典 CONVERSION：PG 特有的一些对象:类型转换 DATA_TYPE：PG 特有的一些对象:数据类型 TEXT_SEARCH_CONFIGURATION：PG 特有的一些对象:文本搜索配置 STATISTICS_EXTENSION：PG 特有的一些对象:插件统计 MEMBERSHIP：PG 特有的一些对象:用户成员关系 EVENT_TRIGGER：PG 特有的一些对象:事件触发器 COLLATION：PG 特有的一些对象:排序规则 TEXT_SEARCH_PARSER：PG 特有的一些对象:文本搜索解析器 PRIVILEGES：PG 特有的一些对象:权限 FOREIGN_KEY：PG 特有的一些对象:外键 ROLE：权限

        :return: The type of this StructProcessVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StructProcessVO.

        对象类型 DATABASE：数据库 SCHEMA：SCHEMA PACKAGE：package TABLE：数据表 COLUMN：列 VIEW：视图 FUNCTION：函数 PROCEDURE：存储过程 ROUTINE：routine TRIGGER：触发器 INDEX：索引 TABLE_INDEX：普通索引，根据表汇聚 TABLE_RENAME_OR_COPY：表重命名或复制 TABLE_STRUCTURE：表结构 EVENT：事件 SYNONYM：同义词,sqlserver特有 TYPE：自定义类型,sqlserver特有 RULE：规则,sqlserver特有 DEFAULT：缺省值,sqlserver特有 PLAN_GUIDE：执行计划,sqlserver特有 FILE_GROUP：文件组,sqlserver特有 PARTITION_FUNCTION：分区函数,sqlserver特有 SHARD_KEY：mongo特有 VALIDATOR：mongo特有 SEQUENCE：序列 MATVIEW：物化视图 PARTITION_SCHEME：分区方案,sqlserver特有 ACCOUNT：账户 EXTENSION：PG 特有的一些对象:插件 AGGREGATE：PG 特有的一些对象:聚合函数 MATERIALIZED_VIEW：PG 特有的一些对象:物化视图 TEXT_SEARCH_DICTIONARY：PG 特有的一些对象:文本搜索字典 CONVERSION：PG 特有的一些对象:类型转换 DATA_TYPE：PG 特有的一些对象:数据类型 TEXT_SEARCH_CONFIGURATION：PG 特有的一些对象:文本搜索配置 STATISTICS_EXTENSION：PG 特有的一些对象:插件统计 MEMBERSHIP：PG 特有的一些对象:用户成员关系 EVENT_TRIGGER：PG 特有的一些对象:事件触发器 COLLATION：PG 特有的一些对象:排序规则 TEXT_SEARCH_PARSER：PG 特有的一些对象:文本搜索解析器 PRIVILEGES：PG 特有的一些对象:权限 FOREIGN_KEY：PG 特有的一些对象:外键 ROLE：权限

        :param type: The type of this StructProcessVO.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this StructProcessVO.

        状态 1：正在对比中，2：对比完成

        :return: The status of this StructProcessVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StructProcessVO.

        状态 1：正在对比中，2：对比完成

        :param status: The status of this StructProcessVO.
        :type status: int
        """
        self._status = status

    @property
    def src_count(self):
        r"""Gets the src_count of this StructProcessVO.

        源对象数量

        :return: The src_count of this StructProcessVO.
        :rtype: int
        """
        return self._src_count

    @src_count.setter
    def src_count(self, src_count):
        r"""Sets the src_count of this StructProcessVO.

        源对象数量

        :param src_count: The src_count of this StructProcessVO.
        :type src_count: int
        """
        self._src_count = src_count

    @property
    def dst_count(self):
        r"""Gets the dst_count of this StructProcessVO.

        目标对象数量

        :return: The dst_count of this StructProcessVO.
        :rtype: int
        """
        return self._dst_count

    @dst_count.setter
    def dst_count(self, dst_count):
        r"""Sets the dst_count of this StructProcessVO.

        目标对象数量

        :param dst_count: The dst_count of this StructProcessVO.
        :type dst_count: int
        """
        self._dst_count = dst_count

    @property
    def start_time(self):
        r"""Gets the start_time of this StructProcessVO.

        开始时间

        :return: The start_time of this StructProcessVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StructProcessVO.

        开始时间

        :param start_time: The start_time of this StructProcessVO.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StructProcessVO.

        结束时间

        :return: The end_time of this StructProcessVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StructProcessVO.

        结束时间

        :param end_time: The end_time of this StructProcessVO.
        :type end_time: int
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StructProcessVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
