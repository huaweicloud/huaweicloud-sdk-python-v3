# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTableVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'schema_names': 'list[str]',
        'table_name': 'str',
        'user_name': 'str',
        'sort_key': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'schema_names': 'schema_names',
        'table_name': 'table_name',
        'user_name': 'user_name',
        'sort_key': 'sort_key',
        'sort_order': 'sort_order'
    }

    def __init__(self, database_name=None, schema_names=None, table_name=None, user_name=None, sort_key=None, sort_order=None):
        r"""ExportTableVolumeRequestBody

        The model defined in huaweicloud sdk

        :param database_name: **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type database_name: str
        :param schema_names: **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type schema_names: list[str]
        :param table_name: **参数解释**: 表名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type table_name: str
        :param user_name: **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type user_name: str
        :param sort_key: **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - table_size：表的大小。 - id：表ID。 - table_name：表名称。 - table_owner：表所属用户名称。 - database_name：数据库名称。 - schema_name：schema名称。 - is_part_type：表或者索引是否具有分区表的性质。 - is_hash_cluster_key：是否包含hash分区列信息。 - tuples：表中行的数目。 - create_time：创建时间。 - update_time：修改时间。 - average_size：表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 - max_ratio：单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 - min_ratio：单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 - skew_size：表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 - skew_ratio：表分布倾斜率（skewsize/totalsize）。 - skew_stddev：表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。  **默认取值** 不涉及。 
        :type sort_key: str
        :param sort_order: **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据sort_key值升序。 - DESC：根据sort_key值降序。  **默认取值** ASC 
        :type sort_order: str
        """
        
        

        self._database_name = None
        self._schema_names = None
        self._table_name = None
        self._user_name = None
        self._sort_key = None
        self._sort_order = None
        self.discriminator = None

        self.database_name = database_name
        self.schema_names = schema_names
        if table_name is not None:
            self.table_name = table_name
        if user_name is not None:
            self.user_name = user_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def database_name(self):
        r"""Gets the database_name of this ExportTableVolumeRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The database_name of this ExportTableVolumeRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ExportTableVolumeRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param database_name: The database_name of this ExportTableVolumeRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_names(self):
        r"""Gets the schema_names of this ExportTableVolumeRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The schema_names of this ExportTableVolumeRequestBody.
        :rtype: list[str]
        """
        return self._schema_names

    @schema_names.setter
    def schema_names(self, schema_names):
        r"""Sets the schema_names of this ExportTableVolumeRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param schema_names: The schema_names of this ExportTableVolumeRequestBody.
        :type schema_names: list[str]
        """
        self._schema_names = schema_names

    @property
    def table_name(self):
        r"""Gets the table_name of this ExportTableVolumeRequestBody.

        **参数解释**: 表名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The table_name of this ExportTableVolumeRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ExportTableVolumeRequestBody.

        **参数解释**: 表名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param table_name: The table_name of this ExportTableVolumeRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ExportTableVolumeRequestBody.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The user_name of this ExportTableVolumeRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExportTableVolumeRequestBody.

        **参数解释**: 表所属用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param user_name: The user_name of this ExportTableVolumeRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ExportTableVolumeRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - table_size：表的大小。 - id：表ID。 - table_name：表名称。 - table_owner：表所属用户名称。 - database_name：数据库名称。 - schema_name：schema名称。 - is_part_type：表或者索引是否具有分区表的性质。 - is_hash_cluster_key：是否包含hash分区列信息。 - tuples：表中行的数目。 - create_time：创建时间。 - update_time：修改时间。 - average_size：表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 - max_ratio：单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 - min_ratio：单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 - skew_size：表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 - skew_ratio：表分布倾斜率（skewsize/totalsize）。 - skew_stddev：表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。  **默认取值** 不涉及。 

        :return: The sort_key of this ExportTableVolumeRequestBody.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ExportTableVolumeRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - table_size：表的大小。 - id：表ID。 - table_name：表名称。 - table_owner：表所属用户名称。 - database_name：数据库名称。 - schema_name：schema名称。 - is_part_type：表或者索引是否具有分区表的性质。 - is_hash_cluster_key：是否包含hash分区列信息。 - tuples：表中行的数目。 - create_time：创建时间。 - update_time：修改时间。 - average_size：表大小平均值(totalsize/DN个数，该值为平均分布的理想情况下，表在各DN占用空间大小)。 - max_ratio：单DN表大小最大值占比（表在各DN占用空间的最大值/totalsize）。 - min_ratio：单DN表大小最小值占比（表在各DN占用空间的最小值/totalsize）。 - skew_size：表分布倾斜值（单DN表大小最大值 - 单DN表大小最小值）。 - skew_ratio：表分布倾斜率（skewsize/totalsize）。 - skew_stddev：表分布标准方差（在表大小一定的情况下，该值越大表明表的整体分布情况越倾斜）。  **默认取值** 不涉及。 

        :param sort_key: The sort_key of this ExportTableVolumeRequestBody.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ExportTableVolumeRequestBody.

        **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据sort_key值升序。 - DESC：根据sort_key值降序。  **默认取值** ASC 

        :return: The sort_order of this ExportTableVolumeRequestBody.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ExportTableVolumeRequestBody.

        **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据sort_key值升序。 - DESC：根据sort_key值降序。  **默认取值** ASC 

        :param sort_order: The sort_order of this ExportTableVolumeRequestBody.
        :type sort_order: str
        """
        self._sort_order = sort_order

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
        if not isinstance(other, ExportTableVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
