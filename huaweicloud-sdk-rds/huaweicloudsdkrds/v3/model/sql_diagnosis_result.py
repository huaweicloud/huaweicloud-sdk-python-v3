# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlDiagnosisResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'start_time': 'int',
        'sql': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'start_time': 'start_time',
        'sql': 'sql'
    }

    def __init__(self, id=None, user=None, host=None, db=None, start_time=None, sql=None):
        r"""SqlDiagnosisResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  线程id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type id: int
        :param user: **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type user: str
        :param host: **参数解释**：  用户host信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type host: str
        :param db: **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type db: str
        :param start_time: **参数解释**：  执行开始时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type start_time: int
        :param sql: **参数解释**：  sql语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._db = None
        self._start_time = None
        self._sql = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if start_time is not None:
            self.start_time = start_time
        if sql is not None:
            self.sql = sql

    @property
    def id(self):
        r"""Gets the id of this SqlDiagnosisResult.

        **参数解释**：  线程id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The id of this SqlDiagnosisResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SqlDiagnosisResult.

        **参数解释**：  线程id。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param id: The id of this SqlDiagnosisResult.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this SqlDiagnosisResult.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The user of this SqlDiagnosisResult.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SqlDiagnosisResult.

        **参数解释**：  用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param user: The user of this SqlDiagnosisResult.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this SqlDiagnosisResult.

        **参数解释**：  用户host信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The host of this SqlDiagnosisResult.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SqlDiagnosisResult.

        **参数解释**：  用户host信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param host: The host of this SqlDiagnosisResult.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this SqlDiagnosisResult.

        **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The db of this SqlDiagnosisResult.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this SqlDiagnosisResult.

        **参数解释**：  数据库名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param db: The db of this SqlDiagnosisResult.
        :type db: str
        """
        self._db = db

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlDiagnosisResult.

        **参数解释**：  执行开始时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The start_time of this SqlDiagnosisResult.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlDiagnosisResult.

        **参数解释**：  执行开始时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param start_time: The start_time of this SqlDiagnosisResult.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def sql(self):
        r"""Gets the sql of this SqlDiagnosisResult.

        **参数解释**：  sql语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql of this SqlDiagnosisResult.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SqlDiagnosisResult.

        **参数解释**：  sql语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql: The sql of this SqlDiagnosisResult.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, SqlDiagnosisResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
