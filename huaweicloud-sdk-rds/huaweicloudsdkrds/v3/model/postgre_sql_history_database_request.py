# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLHistoryDatabaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'restore_time': 'int',
        'database_name_like': 'str',
        'instance_name_like': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'restore_time': 'restore_time',
        'database_name_like': 'database_name_like',
        'instance_name_like': 'instance_name_like'
    }

    def __init__(self, instance_ids=None, restore_time=None, database_name_like=None, instance_name_like=None):
        """PostgreSQLHistoryDatabaseRequest

        The model defined in huaweicloud sdk

        :param instance_ids: 实例ID集合
        :type instance_ids: list[str]
        :param restore_time: 恢复时间点
        :type restore_time: int
        :param database_name_like: 数据库名，模糊查询
        :type database_name_like: str
        :param instance_name_like: 实例名称，模糊查询
        :type instance_name_like: str
        """
        
        

        self._instance_ids = None
        self._restore_time = None
        self._database_name_like = None
        self._instance_name_like = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.restore_time = restore_time
        if database_name_like is not None:
            self.database_name_like = database_name_like
        if instance_name_like is not None:
            self.instance_name_like = instance_name_like

    @property
    def instance_ids(self):
        """Gets the instance_ids of this PostgreSQLHistoryDatabaseRequest.

        实例ID集合

        :return: The instance_ids of this PostgreSQLHistoryDatabaseRequest.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this PostgreSQLHistoryDatabaseRequest.

        实例ID集合

        :param instance_ids: The instance_ids of this PostgreSQLHistoryDatabaseRequest.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def restore_time(self):
        """Gets the restore_time of this PostgreSQLHistoryDatabaseRequest.

        恢复时间点

        :return: The restore_time of this PostgreSQLHistoryDatabaseRequest.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this PostgreSQLHistoryDatabaseRequest.

        恢复时间点

        :param restore_time: The restore_time of this PostgreSQLHistoryDatabaseRequest.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def database_name_like(self):
        """Gets the database_name_like of this PostgreSQLHistoryDatabaseRequest.

        数据库名，模糊查询

        :return: The database_name_like of this PostgreSQLHistoryDatabaseRequest.
        :rtype: str
        """
        return self._database_name_like

    @database_name_like.setter
    def database_name_like(self, database_name_like):
        """Sets the database_name_like of this PostgreSQLHistoryDatabaseRequest.

        数据库名，模糊查询

        :param database_name_like: The database_name_like of this PostgreSQLHistoryDatabaseRequest.
        :type database_name_like: str
        """
        self._database_name_like = database_name_like

    @property
    def instance_name_like(self):
        """Gets the instance_name_like of this PostgreSQLHistoryDatabaseRequest.

        实例名称，模糊查询

        :return: The instance_name_like of this PostgreSQLHistoryDatabaseRequest.
        :rtype: str
        """
        return self._instance_name_like

    @instance_name_like.setter
    def instance_name_like(self, instance_name_like):
        """Sets the instance_name_like of this PostgreSQLHistoryDatabaseRequest.

        实例名称，模糊查询

        :param instance_name_like: The instance_name_like of this PostgreSQLHistoryDatabaseRequest.
        :type instance_name_like: str
        """
        self._instance_name_like = instance_name_like

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
        if not isinstance(other, PostgreSQLHistoryDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
