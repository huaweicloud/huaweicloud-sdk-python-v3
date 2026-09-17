# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogDetailSampleRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'db_name': 'str',
        'sql_template_id': 'str',
        'with_db': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'db_name': 'db_name',
        'sql_template_id': 'sql_template_id',
        'with_db': 'with_db'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None, db_name=None, sql_template_id=None, with_db=None):
        r"""ShowSlowLogDetailSampleRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param db_name: 数据库名称
        :type db_name: str
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param with_db: 是否需要数据库名
        :type with_db: str
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._db_name = None
        self._sql_template_id = None
        self._with_db = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        if db_name is not None:
            self.db_name = db_name
        self.sql_template_id = sql_template_id
        if with_db is not None:
            self.with_db = with_db

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSlowLogDetailSampleRequest.

        实例ID

        :return: The instance_id of this ShowSlowLogDetailSampleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSlowLogDetailSampleRequest.

        实例ID

        :param instance_id: The instance_id of this ShowSlowLogDetailSampleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSlowLogDetailSampleRequest.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this ShowSlowLogDetailSampleRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSlowLogDetailSampleRequest.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this ShowSlowLogDetailSampleRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSlowLogDetailSampleRequest.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowSlowLogDetailSampleRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSlowLogDetailSampleRequest.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowSlowLogDetailSampleRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def db_name(self):
        r"""Gets the db_name of this ShowSlowLogDetailSampleRequest.

        数据库名称

        :return: The db_name of this ShowSlowLogDetailSampleRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ShowSlowLogDetailSampleRequest.

        数据库名称

        :param db_name: The db_name of this ShowSlowLogDetailSampleRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ShowSlowLogDetailSampleRequest.

        SQL模板ID

        :return: The sql_template_id of this ShowSlowLogDetailSampleRequest.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ShowSlowLogDetailSampleRequest.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this ShowSlowLogDetailSampleRequest.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def with_db(self):
        r"""Gets the with_db of this ShowSlowLogDetailSampleRequest.

        是否需要数据库名

        :return: The with_db of this ShowSlowLogDetailSampleRequest.
        :rtype: str
        """
        return self._with_db

    @with_db.setter
    def with_db(self, with_db):
        r"""Sets the with_db of this ShowSlowLogDetailSampleRequest.

        是否需要数据库名

        :param with_db: The with_db of this ShowSlowLogDetailSampleRequest.
        :type with_db: str
        """
        self._with_db = with_db

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
        if not isinstance(other, ShowSlowLogDetailSampleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
