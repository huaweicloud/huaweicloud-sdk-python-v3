# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSqlsRequestBody:

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
        'node_ids': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'start_time_utc': 'str',
        'end_time_utc': 'str',
        'user_name': 'str',
        'sql_text': 'str',
        'sql_id': 'str',
        'db_name': 'str',
        'support_system': 'bool',
        'multi_queries': 'list[MultiQueryConditionOption]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_ids': 'node_ids',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'start_time_utc': 'start_time_utc',
        'end_time_utc': 'end_time_utc',
        'user_name': 'user_name',
        'sql_text': 'sql_text',
        'sql_id': 'sql_id',
        'db_name': 'db_name',
        'support_system': 'support_system',
        'multi_queries': 'multi_queries'
    }

    def __init__(self, instance_id=None, node_ids=None, start_time=None, end_time=None, start_time_utc=None, end_time_utc=None, user_name=None, sql_text=None, sql_id=None, db_name=None, support_system=None, multi_queries=None):
        r"""ListTopSqlsRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_ids: **参数解释**: 所选实例节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_ids: list[str]
        :param start_time: **参数解释**: 起始时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type start_time: int
        :param end_time: **参数解释**: 结束时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type end_time: int
        :param start_time_utc: **参数解释**: 起始时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type start_time_utc: str
        :param end_time_utc: **参数解释**: 结束时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type end_time_utc: str
        :param user_name: **参数解释**: Top SQL的用户名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type user_name: str
        :param sql_text: **参数解释**: Top SQL的SQL文本，例如 select pg_sleep(5)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_text: str
        :param sql_id: **参数解释**: Top SQL的归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        :param db_name: **参数解释**: Top SQL的数据库名。 **约束限制**: 引擎版本8.200及以上显示。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type db_name: str
        :param support_system: **参数解释**: 是否支持展示系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：支持展示系统用户。 - false：不支持展示系统用户。  **默认取值**: 不涉及
        :type support_system: bool
        :param multi_queries: **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        
        

        self._instance_id = None
        self._node_ids = None
        self._start_time = None
        self._end_time = None
        self._start_time_utc = None
        self._end_time_utc = None
        self._user_name = None
        self._sql_text = None
        self._sql_id = None
        self._db_name = None
        self._support_system = None
        self._multi_queries = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_ids = node_ids
        self.start_time = start_time
        self.end_time = end_time
        if start_time_utc is not None:
            self.start_time_utc = start_time_utc
        if end_time_utc is not None:
            self.end_time_utc = end_time_utc
        if user_name is not None:
            self.user_name = user_name
        if sql_text is not None:
            self.sql_text = sql_text
        if sql_id is not None:
            self.sql_id = sql_id
        if db_name is not None:
            self.db_name = db_name
        if support_system is not None:
            self.support_system = support_system
        if multi_queries is not None:
            self.multi_queries = multi_queries

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTopSqlsRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTopSqlsRequestBody.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListTopSqlsRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ListTopSqlsRequestBody.

        **参数解释**: 所选实例节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_ids of this ListTopSqlsRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ListTopSqlsRequestBody.

        **参数解释**: 所选实例节点ID列表。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_ids: The node_ids of this ListTopSqlsRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTopSqlsRequestBody.

        **参数解释**: 起始时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The start_time of this ListTopSqlsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTopSqlsRequestBody.

        **参数解释**: 起始时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param start_time: The start_time of this ListTopSqlsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTopSqlsRequestBody.

        **参数解释**: 结束时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The end_time of this ListTopSqlsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTopSqlsRequestBody.

        **参数解释**: 结束时间。 **约束限制**: 13位UNIX时间戳格式，单位是毫秒，时区是UTC。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param end_time: The end_time of this ListTopSqlsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def start_time_utc(self):
        r"""Gets the start_time_utc of this ListTopSqlsRequestBody.

        **参数解释**: 起始时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The start_time_utc of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._start_time_utc

    @start_time_utc.setter
    def start_time_utc(self, start_time_utc):
        r"""Sets the start_time_utc of this ListTopSqlsRequestBody.

        **参数解释**: 起始时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param start_time_utc: The start_time_utc of this ListTopSqlsRequestBody.
        :type start_time_utc: str
        """
        self._start_time_utc = start_time_utc

    @property
    def end_time_utc(self):
        r"""Gets the end_time_utc of this ListTopSqlsRequestBody.

        **参数解释**: 结束时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The end_time_utc of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._end_time_utc

    @end_time_utc.setter
    def end_time_utc(self, end_time_utc):
        r"""Sets the end_time_utc of this ListTopSqlsRequestBody.

        **参数解释**: 结束时间。 **约束限制**: UTC时间。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param end_time_utc: The end_time_utc of this ListTopSqlsRequestBody.
        :type end_time_utc: str
        """
        self._end_time_utc = end_time_utc

    @property
    def user_name(self):
        r"""Gets the user_name of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的用户名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The user_name of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的用户名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param user_name: The user_name of this ListTopSqlsRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sql_text(self):
        r"""Gets the sql_text of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的SQL文本，例如 select pg_sleep(5)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_text of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的SQL文本，例如 select pg_sleep(5)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_text: The sql_text of this ListTopSqlsRequestBody.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ListTopSqlsRequestBody.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的数据库名。 **约束限制**: 引擎版本8.200及以上显示。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The db_name of this ListTopSqlsRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListTopSqlsRequestBody.

        **参数解释**: Top SQL的数据库名。 **约束限制**: 引擎版本8.200及以上显示。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param db_name: The db_name of this ListTopSqlsRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def support_system(self):
        r"""Gets the support_system of this ListTopSqlsRequestBody.

        **参数解释**: 是否支持展示系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：支持展示系统用户。 - false：不支持展示系统用户。  **默认取值**: 不涉及

        :return: The support_system of this ListTopSqlsRequestBody.
        :rtype: bool
        """
        return self._support_system

    @support_system.setter
    def support_system(self, support_system):
        r"""Sets the support_system of this ListTopSqlsRequestBody.

        **参数解释**: 是否支持展示系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：支持展示系统用户。 - false：不支持展示系统用户。  **默认取值**: 不涉及

        :param support_system: The support_system of this ListTopSqlsRequestBody.
        :type support_system: bool
        """
        self._support_system = support_system

    @property
    def multi_queries(self):
        r"""Gets the multi_queries of this ListTopSqlsRequestBody.

        **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。

        :return: The multi_queries of this ListTopSqlsRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        return self._multi_queries

    @multi_queries.setter
    def multi_queries(self, multi_queries):
        r"""Sets the multi_queries of this ListTopSqlsRequestBody.

        **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。

        :param multi_queries: The multi_queries of this ListTopSqlsRequestBody.
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        self._multi_queries = multi_queries

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
        if not isinstance(other, ListTopSqlsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
