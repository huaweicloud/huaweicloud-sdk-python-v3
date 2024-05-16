# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'engine_type': 'str',
        'current_catalog': 'str',
        'currentdb': 'str',
        'queue_name': 'str',
        'conf': 'list[str]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'sql': 'sql',
        'engine_type': 'engine_type',
        'current_catalog': 'current_catalog',
        'currentdb': 'currentdb',
        'queue_name': 'queue_name',
        'conf': 'conf',
        'tags': 'tags'
    }

    def __init__(self, sql=None, engine_type=None, current_catalog=None, currentdb=None, queue_name=None, conf=None, tags=None):
        """CreateSqlJobRequestBody

        The model defined in huaweicloud sdk

        :param sql: 待执行的SQL语句。
        :type sql: str
        :param engine_type: 待提交作业的队列引擎名称，名称只能包含英文字母。
        :type engine_type: str
        :param current_catalog: 待提交作业的表默认catalog。
        :type current_catalog: str
        :param currentdb: SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。
        :type currentdb: str
        :param queue_name: 待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。
        :type queue_name: str
        :param conf: 用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。
        :type conf: list[str]
        :param tags: 作业标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        

        self._sql = None
        self._engine_type = None
        self._current_catalog = None
        self._currentdb = None
        self._queue_name = None
        self._conf = None
        self._tags = None
        self.discriminator = None

        self.sql = sql
        if engine_type is not None:
            self.engine_type = engine_type
        if current_catalog is not None:
            self.current_catalog = current_catalog
        if currentdb is not None:
            self.currentdb = currentdb
        if queue_name is not None:
            self.queue_name = queue_name
        if conf is not None:
            self.conf = conf
        if tags is not None:
            self.tags = tags

    @property
    def sql(self):
        """Gets the sql of this CreateSqlJobRequestBody.

        待执行的SQL语句。

        :return: The sql of this CreateSqlJobRequestBody.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this CreateSqlJobRequestBody.

        待执行的SQL语句。

        :param sql: The sql of this CreateSqlJobRequestBody.
        :type sql: str
        """
        self._sql = sql

    @property
    def engine_type(self):
        """Gets the engine_type of this CreateSqlJobRequestBody.

        待提交作业的队列引擎名称，名称只能包含英文字母。

        :return: The engine_type of this CreateSqlJobRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this CreateSqlJobRequestBody.

        待提交作业的队列引擎名称，名称只能包含英文字母。

        :param engine_type: The engine_type of this CreateSqlJobRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def current_catalog(self):
        """Gets the current_catalog of this CreateSqlJobRequestBody.

        待提交作业的表默认catalog。

        :return: The current_catalog of this CreateSqlJobRequestBody.
        :rtype: str
        """
        return self._current_catalog

    @current_catalog.setter
    def current_catalog(self, current_catalog):
        """Sets the current_catalog of this CreateSqlJobRequestBody.

        待提交作业的表默认catalog。

        :param current_catalog: The current_catalog of this CreateSqlJobRequestBody.
        :type current_catalog: str
        """
        self._current_catalog = current_catalog

    @property
    def currentdb(self):
        """Gets the currentdb of this CreateSqlJobRequestBody.

        SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。

        :return: The currentdb of this CreateSqlJobRequestBody.
        :rtype: str
        """
        return self._currentdb

    @currentdb.setter
    def currentdb(self, currentdb):
        """Sets the currentdb of this CreateSqlJobRequestBody.

        SQL语句执行所在的数据库。当创建新数据库时，不需要提供此参数。

        :param currentdb: The currentdb of this CreateSqlJobRequestBody.
        :type currentdb: str
        """
        self._currentdb = currentdb

    @property
    def queue_name(self):
        """Gets the queue_name of this CreateSqlJobRequestBody.

        待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。

        :return: The queue_name of this CreateSqlJobRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this CreateSqlJobRequestBody.

        待提交作业的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。

        :param queue_name: The queue_name of this CreateSqlJobRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def conf(self):
        """Gets the conf of this CreateSqlJobRequestBody.

        用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。

        :return: The conf of this CreateSqlJobRequestBody.
        :rtype: list[str]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this CreateSqlJobRequestBody.

        用户以“key/value”的形式设置用于此作业的配置参数。目前支持的配置项请参考表3。

        :param conf: The conf of this CreateSqlJobRequestBody.
        :type conf: list[str]
        """
        self._conf = conf

    @property
    def tags(self):
        """Gets the tags of this CreateSqlJobRequestBody.

        作业标签

        :return: The tags of this CreateSqlJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSqlJobRequestBody.

        作业标签

        :param tags: The tags of this CreateSqlJobRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateSqlJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
