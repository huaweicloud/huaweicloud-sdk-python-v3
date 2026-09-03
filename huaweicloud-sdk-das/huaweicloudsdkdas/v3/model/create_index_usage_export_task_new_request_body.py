# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIndexUsageExportTaskNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_type': 'str',
        'collect_time': 'int',
        'bucket_name': 'str',
        'conditions': 'list[IndexUsageCondition]',
        'object_name': 'str',
        'sort_field': 'str',
        'sort_asc': 'bool',
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'export_type': 'export_type',
        'collect_time': 'collect_time',
        'bucket_name': 'bucket_name',
        'conditions': 'conditions',
        'object_name': 'object_name',
        'sort_field': 'sort_field',
        'sort_asc': 'sort_asc',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, export_type=None, collect_time=None, bucket_name=None, conditions=None, object_name=None, sort_field=None, sort_asc=None, cur_page=None, per_page=None):
        r"""CreateIndexUsageExportTaskNewRequestBody

        The model defined in huaweicloud sdk

        :param export_type: 导出类型。取值范围：missingindex（导出表数据）、missingindexscript（导出脚本）
        :type export_type: str
        :param collect_time: 采集时间
        :type collect_time: int
        :param bucket_name: 桶名
        :type bucket_name: str
        :param conditions: 过滤条件
        :type conditions: list[:class:`huaweicloudsdkdas.v3.IndexUsageCondition`]
        :param object_name: 表名称
        :type object_name: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_asc: 排序是否升序
        :type sort_asc: bool
        :param cur_page: 当前页
        :type cur_page: int
        :param per_page: 页大小
        :type per_page: int
        """
        
        

        self._export_type = None
        self._collect_time = None
        self._bucket_name = None
        self._conditions = None
        self._object_name = None
        self._sort_field = None
        self._sort_asc = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.export_type = export_type
        self.collect_time = collect_time
        self.bucket_name = bucket_name
        if conditions is not None:
            self.conditions = conditions
        if object_name is not None:
            self.object_name = object_name
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_asc is not None:
            self.sort_asc = sort_asc
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def export_type(self):
        r"""Gets the export_type of this CreateIndexUsageExportTaskNewRequestBody.

        导出类型。取值范围：missingindex（导出表数据）、missingindexscript（导出脚本）

        :return: The export_type of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        r"""Sets the export_type of this CreateIndexUsageExportTaskNewRequestBody.

        导出类型。取值范围：missingindex（导出表数据）、missingindexscript（导出脚本）

        :param export_type: The export_type of this CreateIndexUsageExportTaskNewRequestBody.
        :type export_type: str
        """
        self._export_type = export_type

    @property
    def collect_time(self):
        r"""Gets the collect_time of this CreateIndexUsageExportTaskNewRequestBody.

        采集时间

        :return: The collect_time of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this CreateIndexUsageExportTaskNewRequestBody.

        采集时间

        :param collect_time: The collect_time of this CreateIndexUsageExportTaskNewRequestBody.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateIndexUsageExportTaskNewRequestBody.

        桶名

        :return: The bucket_name of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateIndexUsageExportTaskNewRequestBody.

        桶名

        :param bucket_name: The bucket_name of this CreateIndexUsageExportTaskNewRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def conditions(self):
        r"""Gets the conditions of this CreateIndexUsageExportTaskNewRequestBody.

        过滤条件

        :return: The conditions of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.IndexUsageCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CreateIndexUsageExportTaskNewRequestBody.

        过滤条件

        :param conditions: The conditions of this CreateIndexUsageExportTaskNewRequestBody.
        :type conditions: list[:class:`huaweicloudsdkdas.v3.IndexUsageCondition`]
        """
        self._conditions = conditions

    @property
    def object_name(self):
        r"""Gets the object_name of this CreateIndexUsageExportTaskNewRequestBody.

        表名称

        :return: The object_name of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this CreateIndexUsageExportTaskNewRequestBody.

        表名称

        :param object_name: The object_name of this CreateIndexUsageExportTaskNewRequestBody.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def sort_field(self):
        r"""Gets the sort_field of this CreateIndexUsageExportTaskNewRequestBody.

        排序字段

        :return: The sort_field of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this CreateIndexUsageExportTaskNewRequestBody.

        排序字段

        :param sort_field: The sort_field of this CreateIndexUsageExportTaskNewRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_asc(self):
        r"""Gets the sort_asc of this CreateIndexUsageExportTaskNewRequestBody.

        排序是否升序

        :return: The sort_asc of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: bool
        """
        return self._sort_asc

    @sort_asc.setter
    def sort_asc(self, sort_asc):
        r"""Sets the sort_asc of this CreateIndexUsageExportTaskNewRequestBody.

        排序是否升序

        :param sort_asc: The sort_asc of this CreateIndexUsageExportTaskNewRequestBody.
        :type sort_asc: bool
        """
        self._sort_asc = sort_asc

    @property
    def cur_page(self):
        r"""Gets the cur_page of this CreateIndexUsageExportTaskNewRequestBody.

        当前页

        :return: The cur_page of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this CreateIndexUsageExportTaskNewRequestBody.

        当前页

        :param cur_page: The cur_page of this CreateIndexUsageExportTaskNewRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this CreateIndexUsageExportTaskNewRequestBody.

        页大小

        :return: The per_page of this CreateIndexUsageExportTaskNewRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this CreateIndexUsageExportTaskNewRequestBody.

        页大小

        :param per_page: The per_page of this CreateIndexUsageExportTaskNewRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, CreateIndexUsageExportTaskNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
