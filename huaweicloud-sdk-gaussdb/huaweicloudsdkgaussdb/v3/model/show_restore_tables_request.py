# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRestoreTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'restore_time': 'str',
        'last_table_info': 'str',
        'database_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'restore_time': 'restore_time',
        'last_table_info': 'last_table_info',
        'database_name': 'database_name',
        'table_name': 'table_name'
    }

    def __init__(self, x_language=None, instance_id=None, restore_time=None, last_table_info=None, database_name=None, table_name=None):
        """ShowRestoreTablesRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param restore_time: 备份时间点，时间戳格式。  通过[查询可恢复时间段](https://support.huaweicloud.com/api-gaussdbformysql/ShowBackupRestoreTime.html)获取。
        :type restore_time: str
        :param last_table_info: 是否是最新库表。 - true：是最新库表。 - false：是恢复时间点库表。
        :type last_table_info: str
        :param database_name: 数据库名称，模糊匹配。
        :type database_name: str
        :param table_name: 表名称，模糊匹配。
        :type table_name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._restore_time = None
        self._last_table_info = None
        self._database_name = None
        self._table_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.restore_time = restore_time
        self.last_table_info = last_table_info
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name

    @property
    def x_language(self):
        """Gets the x_language of this ShowRestoreTablesRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowRestoreTablesRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowRestoreTablesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowRestoreTablesRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowRestoreTablesRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowRestoreTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def restore_time(self):
        """Gets the restore_time of this ShowRestoreTablesRequest.

        备份时间点，时间戳格式。  通过[查询可恢复时间段](https://support.huaweicloud.com/api-gaussdbformysql/ShowBackupRestoreTime.html)获取。

        :return: The restore_time of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this ShowRestoreTablesRequest.

        备份时间点，时间戳格式。  通过[查询可恢复时间段](https://support.huaweicloud.com/api-gaussdbformysql/ShowBackupRestoreTime.html)获取。

        :param restore_time: The restore_time of this ShowRestoreTablesRequest.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def last_table_info(self):
        """Gets the last_table_info of this ShowRestoreTablesRequest.

        是否是最新库表。 - true：是最新库表。 - false：是恢复时间点库表。

        :return: The last_table_info of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._last_table_info

    @last_table_info.setter
    def last_table_info(self, last_table_info):
        """Sets the last_table_info of this ShowRestoreTablesRequest.

        是否是最新库表。 - true：是最新库表。 - false：是恢复时间点库表。

        :param last_table_info: The last_table_info of this ShowRestoreTablesRequest.
        :type last_table_info: str
        """
        self._last_table_info = last_table_info

    @property
    def database_name(self):
        """Gets the database_name of this ShowRestoreTablesRequest.

        数据库名称，模糊匹配。

        :return: The database_name of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ShowRestoreTablesRequest.

        数据库名称，模糊匹配。

        :param database_name: The database_name of this ShowRestoreTablesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ShowRestoreTablesRequest.

        表名称，模糊匹配。

        :return: The table_name of this ShowRestoreTablesRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ShowRestoreTablesRequest.

        表名称，模糊匹配。

        :param table_name: The table_name of this ShowRestoreTablesRequest.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, ShowRestoreTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
