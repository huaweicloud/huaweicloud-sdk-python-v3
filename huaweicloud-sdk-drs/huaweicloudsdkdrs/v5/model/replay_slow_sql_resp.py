# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaySlowSqlResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'slow_sql': 'str',
        'old_time': 'str',
        'replay_time': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'slow_sql': 'slow_sql',
        'old_time': 'old_time',
        'replay_time': 'replay_time'
    }

    def __init__(self, object_type=None, slow_sql=None, old_time=None, replay_time=None):
        """ReplaySlowSqlResp

        The model defined in huaweicloud sdk

        :param object_type: SQL语句类型
        :type object_type: str
        :param slow_sql: SQL语句
        :type slow_sql: str
        :param old_time: 源库执行耗时
        :type old_time: str
        :param replay_time: 目标库回放执行耗时
        :type replay_time: str
        """
        
        

        self._object_type = None
        self._slow_sql = None
        self._old_time = None
        self._replay_time = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        if slow_sql is not None:
            self.slow_sql = slow_sql
        if old_time is not None:
            self.old_time = old_time
        if replay_time is not None:
            self.replay_time = replay_time

    @property
    def object_type(self):
        """Gets the object_type of this ReplaySlowSqlResp.

        SQL语句类型

        :return: The object_type of this ReplaySlowSqlResp.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ReplaySlowSqlResp.

        SQL语句类型

        :param object_type: The object_type of this ReplaySlowSqlResp.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def slow_sql(self):
        """Gets the slow_sql of this ReplaySlowSqlResp.

        SQL语句

        :return: The slow_sql of this ReplaySlowSqlResp.
        :rtype: str
        """
        return self._slow_sql

    @slow_sql.setter
    def slow_sql(self, slow_sql):
        """Sets the slow_sql of this ReplaySlowSqlResp.

        SQL语句

        :param slow_sql: The slow_sql of this ReplaySlowSqlResp.
        :type slow_sql: str
        """
        self._slow_sql = slow_sql

    @property
    def old_time(self):
        """Gets the old_time of this ReplaySlowSqlResp.

        源库执行耗时

        :return: The old_time of this ReplaySlowSqlResp.
        :rtype: str
        """
        return self._old_time

    @old_time.setter
    def old_time(self, old_time):
        """Sets the old_time of this ReplaySlowSqlResp.

        源库执行耗时

        :param old_time: The old_time of this ReplaySlowSqlResp.
        :type old_time: str
        """
        self._old_time = old_time

    @property
    def replay_time(self):
        """Gets the replay_time of this ReplaySlowSqlResp.

        目标库回放执行耗时

        :return: The replay_time of this ReplaySlowSqlResp.
        :rtype: str
        """
        return self._replay_time

    @replay_time.setter
    def replay_time(self, replay_time):
        """Sets the replay_time of this ReplaySlowSqlResp.

        目标库回放执行耗时

        :param replay_time: The replay_time of this ReplaySlowSqlResp.
        :type replay_time: str
        """
        self._replay_time = replay_time

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
        if not isinstance(other, ReplaySlowSqlResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
