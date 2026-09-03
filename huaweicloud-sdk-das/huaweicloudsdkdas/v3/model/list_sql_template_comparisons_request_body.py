# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlTemplateComparisonsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'compare_type': 'str',
        'node_id': 'str',
        'node_id1': 'str',
        'node_id2': 'str',
        'start_at1': 'int',
        'end_at1': 'int',
        'start_at2': 'int',
        'end_at2': 'int',
        'operation': 'str',
        'db_name_list': 'list[str]',
        'keyword': 'str',
        'sql_template_id': 'str',
        'sort': 'str',
        'asc': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'compare_type': 'compare_type',
        'node_id': 'node_id',
        'node_id1': 'node_id1',
        'node_id2': 'node_id2',
        'start_at1': 'start_at1',
        'end_at1': 'end_at1',
        'start_at2': 'start_at2',
        'end_at2': 'end_at2',
        'operation': 'operation',
        'db_name_list': 'db_name_list',
        'keyword': 'keyword',
        'sql_template_id': 'sql_template_id',
        'sort': 'sort',
        'asc': 'asc',
        'size': 'size'
    }

    def __init__(self, instance_id=None, compare_type=None, node_id=None, node_id1=None, node_id2=None, start_at1=None, end_at1=None, start_at2=None, end_at2=None, operation=None, db_name_list=None, keyword=None, sql_template_id=None, sort=None, asc=None, size=None):
        r"""ListSqlTemplateComparisonsRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param compare_type: 对比类型，time 时间段对比，node 节点对比，默认time
        :type compare_type: str
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param node_id1: 节点对比方1 ID， node模式必选
        :type node_id1: str
        :param node_id2: 节点对比方2 ID， node模式必选
        :type node_id2: str
        :param start_at1: 对比日期1开始时间，单位毫秒
        :type start_at1: int
        :param end_at1: 对比日期1结束时间，单位毫秒
        :type end_at1: int
        :param start_at2: 对比日期2开始时间，单位毫秒
        :type start_at2: int
        :param end_at2: 对比日期2结束时间，单位毫秒
        :type end_at2: int
        :param operation: 操作类型，可组合，用逗号分隔
        :type operation: str
        :param db_name_list: 数据库名称列表
        :type db_name_list: list[str]
        :param keyword: 关键字，模糊搜索
        :type keyword: str
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param sort: 排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）
        :type sort: str
        :param asc: 排序顺序，true（正序）、false（倒序）
        :type asc: bool
        :param size: 单次查询数量
        :type size: int
        """
        
        

        self._instance_id = None
        self._compare_type = None
        self._node_id = None
        self._node_id1 = None
        self._node_id2 = None
        self._start_at1 = None
        self._end_at1 = None
        self._start_at2 = None
        self._end_at2 = None
        self._operation = None
        self._db_name_list = None
        self._keyword = None
        self._sql_template_id = None
        self._sort = None
        self._asc = None
        self._size = None
        self.discriminator = None

        self.instance_id = instance_id
        if compare_type is not None:
            self.compare_type = compare_type
        if node_id is not None:
            self.node_id = node_id
        if node_id1 is not None:
            self.node_id1 = node_id1
        if node_id2 is not None:
            self.node_id2 = node_id2
        self.start_at1 = start_at1
        self.end_at1 = end_at1
        self.start_at2 = start_at2
        self.end_at2 = end_at2
        if operation is not None:
            self.operation = operation
        if db_name_list is not None:
            self.db_name_list = db_name_list
        if keyword is not None:
            self.keyword = keyword
        if sql_template_id is not None:
            self.sql_template_id = sql_template_id
        if sort is not None:
            self.sort = sort
        if asc is not None:
            self.asc = asc
        if size is not None:
            self.size = size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSqlTemplateComparisonsRequestBody.

        实例ID，实例的唯一标识

        :return: The instance_id of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSqlTemplateComparisonsRequestBody.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this ListSqlTemplateComparisonsRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ListSqlTemplateComparisonsRequestBody.

        对比类型，time 时间段对比，node 节点对比，默认time

        :return: The compare_type of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ListSqlTemplateComparisonsRequestBody.

        对比类型，time 时间段对比，node 节点对比，默认time

        :param compare_type: The compare_type of this ListSqlTemplateComparisonsRequestBody.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListSqlTemplateComparisonsRequestBody.

        节点ID，实例节点的唯一标识

        :return: The node_id of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListSqlTemplateComparisonsRequestBody.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ListSqlTemplateComparisonsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_id1(self):
        r"""Gets the node_id1 of this ListSqlTemplateComparisonsRequestBody.

        节点对比方1 ID， node模式必选

        :return: The node_id1 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._node_id1

    @node_id1.setter
    def node_id1(self, node_id1):
        r"""Sets the node_id1 of this ListSqlTemplateComparisonsRequestBody.

        节点对比方1 ID， node模式必选

        :param node_id1: The node_id1 of this ListSqlTemplateComparisonsRequestBody.
        :type node_id1: str
        """
        self._node_id1 = node_id1

    @property
    def node_id2(self):
        r"""Gets the node_id2 of this ListSqlTemplateComparisonsRequestBody.

        节点对比方2 ID， node模式必选

        :return: The node_id2 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._node_id2

    @node_id2.setter
    def node_id2(self, node_id2):
        r"""Sets the node_id2 of this ListSqlTemplateComparisonsRequestBody.

        节点对比方2 ID， node模式必选

        :param node_id2: The node_id2 of this ListSqlTemplateComparisonsRequestBody.
        :type node_id2: str
        """
        self._node_id2 = node_id2

    @property
    def start_at1(self):
        r"""Gets the start_at1 of this ListSqlTemplateComparisonsRequestBody.

        对比日期1开始时间，单位毫秒

        :return: The start_at1 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: int
        """
        return self._start_at1

    @start_at1.setter
    def start_at1(self, start_at1):
        r"""Sets the start_at1 of this ListSqlTemplateComparisonsRequestBody.

        对比日期1开始时间，单位毫秒

        :param start_at1: The start_at1 of this ListSqlTemplateComparisonsRequestBody.
        :type start_at1: int
        """
        self._start_at1 = start_at1

    @property
    def end_at1(self):
        r"""Gets the end_at1 of this ListSqlTemplateComparisonsRequestBody.

        对比日期1结束时间，单位毫秒

        :return: The end_at1 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: int
        """
        return self._end_at1

    @end_at1.setter
    def end_at1(self, end_at1):
        r"""Sets the end_at1 of this ListSqlTemplateComparisonsRequestBody.

        对比日期1结束时间，单位毫秒

        :param end_at1: The end_at1 of this ListSqlTemplateComparisonsRequestBody.
        :type end_at1: int
        """
        self._end_at1 = end_at1

    @property
    def start_at2(self):
        r"""Gets the start_at2 of this ListSqlTemplateComparisonsRequestBody.

        对比日期2开始时间，单位毫秒

        :return: The start_at2 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: int
        """
        return self._start_at2

    @start_at2.setter
    def start_at2(self, start_at2):
        r"""Sets the start_at2 of this ListSqlTemplateComparisonsRequestBody.

        对比日期2开始时间，单位毫秒

        :param start_at2: The start_at2 of this ListSqlTemplateComparisonsRequestBody.
        :type start_at2: int
        """
        self._start_at2 = start_at2

    @property
    def end_at2(self):
        r"""Gets the end_at2 of this ListSqlTemplateComparisonsRequestBody.

        对比日期2结束时间，单位毫秒

        :return: The end_at2 of this ListSqlTemplateComparisonsRequestBody.
        :rtype: int
        """
        return self._end_at2

    @end_at2.setter
    def end_at2(self, end_at2):
        r"""Sets the end_at2 of this ListSqlTemplateComparisonsRequestBody.

        对比日期2结束时间，单位毫秒

        :param end_at2: The end_at2 of this ListSqlTemplateComparisonsRequestBody.
        :type end_at2: int
        """
        self._end_at2 = end_at2

    @property
    def operation(self):
        r"""Gets the operation of this ListSqlTemplateComparisonsRequestBody.

        操作类型，可组合，用逗号分隔

        :return: The operation of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ListSqlTemplateComparisonsRequestBody.

        操作类型，可组合，用逗号分隔

        :param operation: The operation of this ListSqlTemplateComparisonsRequestBody.
        :type operation: str
        """
        self._operation = operation

    @property
    def db_name_list(self):
        r"""Gets the db_name_list of this ListSqlTemplateComparisonsRequestBody.

        数据库名称列表

        :return: The db_name_list of this ListSqlTemplateComparisonsRequestBody.
        :rtype: list[str]
        """
        return self._db_name_list

    @db_name_list.setter
    def db_name_list(self, db_name_list):
        r"""Sets the db_name_list of this ListSqlTemplateComparisonsRequestBody.

        数据库名称列表

        :param db_name_list: The db_name_list of this ListSqlTemplateComparisonsRequestBody.
        :type db_name_list: list[str]
        """
        self._db_name_list = db_name_list

    @property
    def keyword(self):
        r"""Gets the keyword of this ListSqlTemplateComparisonsRequestBody.

        关键字，模糊搜索

        :return: The keyword of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListSqlTemplateComparisonsRequestBody.

        关键字，模糊搜索

        :param keyword: The keyword of this ListSqlTemplateComparisonsRequestBody.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ListSqlTemplateComparisonsRequestBody.

        SQL模板ID

        :return: The sql_template_id of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ListSqlTemplateComparisonsRequestBody.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this ListSqlTemplateComparisonsRequestBody.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def sort(self):
        r"""Gets the sort of this ListSqlTemplateComparisonsRequestBody.

        排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）

        :return: The sort of this ListSqlTemplateComparisonsRequestBody.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListSqlTemplateComparisonsRequestBody.

        排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）

        :param sort: The sort of this ListSqlTemplateComparisonsRequestBody.
        :type sort: str
        """
        self._sort = sort

    @property
    def asc(self):
        r"""Gets the asc of this ListSqlTemplateComparisonsRequestBody.

        排序顺序，true（正序）、false（倒序）

        :return: The asc of this ListSqlTemplateComparisonsRequestBody.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListSqlTemplateComparisonsRequestBody.

        排序顺序，true（正序）、false（倒序）

        :param asc: The asc of this ListSqlTemplateComparisonsRequestBody.
        :type asc: bool
        """
        self._asc = asc

    @property
    def size(self):
        r"""Gets the size of this ListSqlTemplateComparisonsRequestBody.

        单次查询数量

        :return: The size of this ListSqlTemplateComparisonsRequestBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListSqlTemplateComparisonsRequestBody.

        单次查询数量

        :param size: The size of this ListSqlTemplateComparisonsRequestBody.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListSqlTemplateComparisonsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
