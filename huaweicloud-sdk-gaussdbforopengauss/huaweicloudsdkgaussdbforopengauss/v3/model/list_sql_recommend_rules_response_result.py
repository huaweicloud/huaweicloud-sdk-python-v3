# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlRecommendRulesResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommend_type': 'str',
        'sql_id': 'str',
        'sql_model': 'str',
        'sql_keyword': 'str',
        'sql_type': 'str',
        'database': 'str',
        'avg_exec_time': 'float',
        'max_exec_time': 'float',
        'exec_count': 'int'
    }

    attribute_map = {
        'recommend_type': 'recommend_type',
        'sql_id': 'sql_id',
        'sql_model': 'sql_model',
        'sql_keyword': 'sql_keyword',
        'sql_type': 'sql_type',
        'database': 'database',
        'avg_exec_time': 'avg_exec_time',
        'max_exec_time': 'max_exec_time',
        'exec_count': 'exec_count'
    }

    def __init__(self, recommend_type=None, sql_id=None, sql_model=None, sql_keyword=None, sql_type=None, database=None, avg_exec_time=None, max_exec_time=None, exec_count=None):
        r"""ListSqlRecommendRulesResponseResult

        The model defined in huaweicloud sdk

        :param recommend_type: **参数解释**: 推荐类型。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间
        :type recommend_type: str
        :param sql_id: **参数解释**: SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param sql_model: **参数解释**: SQL模板。 **取值范围**: 不涉及。
        :type sql_model: str
        :param sql_keyword: **参数解释**: SQL关键字。 **取值范围**: 不涉及。
        :type sql_keyword: str
        :param sql_type: **参数解释**: SQL类型。 **取值范围**: - SELECT - INSERT - UPDATE - DELETE - MERGE - OTHER
        :type sql_type: str
        :param database: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type database: str
        :param avg_exec_time: **参数解释**: 平均执行时间。 **取值范围**: 不涉及。
        :type avg_exec_time: float
        :param max_exec_time: **参数解释**: 最长执行时间。 **取值范围**: 不涉及。
        :type max_exec_time: float
        :param exec_count: **参数解释**: 执行次数。 **取值范围**: 不涉及。
        :type exec_count: int
        """
        
        

        self._recommend_type = None
        self._sql_id = None
        self._sql_model = None
        self._sql_keyword = None
        self._sql_type = None
        self._database = None
        self._avg_exec_time = None
        self._max_exec_time = None
        self._exec_count = None
        self.discriminator = None

        if recommend_type is not None:
            self.recommend_type = recommend_type
        if sql_id is not None:
            self.sql_id = sql_id
        if sql_model is not None:
            self.sql_model = sql_model
        if sql_keyword is not None:
            self.sql_keyword = sql_keyword
        if sql_type is not None:
            self.sql_type = sql_type
        if database is not None:
            self.database = database
        if avg_exec_time is not None:
            self.avg_exec_time = avg_exec_time
        if max_exec_time is not None:
            self.max_exec_time = max_exec_time
        if exec_count is not None:
            self.exec_count = exec_count

    @property
    def recommend_type(self):
        r"""Gets the recommend_type of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 推荐类型。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间

        :return: The recommend_type of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._recommend_type

    @recommend_type.setter
    def recommend_type(self, recommend_type):
        r"""Sets the recommend_type of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 推荐类型。 **取值范围**: - all：全部 - exec_count：执行次数 - avg_exec_time：平均执行时间 - max_exec_time：最大执行时间

        :param recommend_type: The recommend_type of this ListSqlRecommendRulesResponseResult.
        :type recommend_type: str
        """
        self._recommend_type = recommend_type

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this ListSqlRecommendRulesResponseResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_model(self):
        r"""Gets the sql_model of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL模板。 **取值范围**: 不涉及。

        :return: The sql_model of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._sql_model

    @sql_model.setter
    def sql_model(self, sql_model):
        r"""Sets the sql_model of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL模板。 **取值范围**: 不涉及。

        :param sql_model: The sql_model of this ListSqlRecommendRulesResponseResult.
        :type sql_model: str
        """
        self._sql_model = sql_model

    @property
    def sql_keyword(self):
        r"""Gets the sql_keyword of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL关键字。 **取值范围**: 不涉及。

        :return: The sql_keyword of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._sql_keyword

    @sql_keyword.setter
    def sql_keyword(self, sql_keyword):
        r"""Sets the sql_keyword of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL关键字。 **取值范围**: 不涉及。

        :param sql_keyword: The sql_keyword of this ListSqlRecommendRulesResponseResult.
        :type sql_keyword: str
        """
        self._sql_keyword = sql_keyword

    @property
    def sql_type(self):
        r"""Gets the sql_type of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL类型。 **取值范围**: - SELECT - INSERT - UPDATE - DELETE - MERGE - OTHER

        :return: The sql_type of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this ListSqlRecommendRulesResponseResult.

        **参数解释**: SQL类型。 **取值范围**: - SELECT - INSERT - UPDATE - DELETE - MERGE - OTHER

        :param sql_type: The sql_type of this ListSqlRecommendRulesResponseResult.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def database(self):
        r"""Gets the database of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The database of this ListSqlRecommendRulesResponseResult.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param database: The database of this ListSqlRecommendRulesResponseResult.
        :type database: str
        """
        self._database = database

    @property
    def avg_exec_time(self):
        r"""Gets the avg_exec_time of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 平均执行时间。 **取值范围**: 不涉及。

        :return: The avg_exec_time of this ListSqlRecommendRulesResponseResult.
        :rtype: float
        """
        return self._avg_exec_time

    @avg_exec_time.setter
    def avg_exec_time(self, avg_exec_time):
        r"""Sets the avg_exec_time of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 平均执行时间。 **取值范围**: 不涉及。

        :param avg_exec_time: The avg_exec_time of this ListSqlRecommendRulesResponseResult.
        :type avg_exec_time: float
        """
        self._avg_exec_time = avg_exec_time

    @property
    def max_exec_time(self):
        r"""Gets the max_exec_time of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 最长执行时间。 **取值范围**: 不涉及。

        :return: The max_exec_time of this ListSqlRecommendRulesResponseResult.
        :rtype: float
        """
        return self._max_exec_time

    @max_exec_time.setter
    def max_exec_time(self, max_exec_time):
        r"""Sets the max_exec_time of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 最长执行时间。 **取值范围**: 不涉及。

        :param max_exec_time: The max_exec_time of this ListSqlRecommendRulesResponseResult.
        :type max_exec_time: float
        """
        self._max_exec_time = max_exec_time

    @property
    def exec_count(self):
        r"""Gets the exec_count of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 执行次数。 **取值范围**: 不涉及。

        :return: The exec_count of this ListSqlRecommendRulesResponseResult.
        :rtype: int
        """
        return self._exec_count

    @exec_count.setter
    def exec_count(self, exec_count):
        r"""Sets the exec_count of this ListSqlRecommendRulesResponseResult.

        **参数解释**: 执行次数。 **取值范围**: 不涉及。

        :param exec_count: The exec_count of this ListSqlRecommendRulesResponseResult.
        :type exec_count: int
        """
        self._exec_count = exec_count

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
        if not isinstance(other, ListSqlRecommendRulesResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
