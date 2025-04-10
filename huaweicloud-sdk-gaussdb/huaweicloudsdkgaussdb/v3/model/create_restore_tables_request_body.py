# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRestoreTablesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'str',
        'last_table_info': 'str',
        'restore_tables': 'list[CreateRestoreDatabaseTableInfo]'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'last_table_info': 'last_table_info',
        'restore_tables': 'restore_tables'
    }

    def __init__(self, restore_time=None, last_table_info=None, restore_tables=None):
        r"""CreateRestoreTablesRequestBody

        The model defined in huaweicloud sdk

        :param restore_time: 备份时间点，时间戳格式。
        :type restore_time: str
        :param last_table_info: 是否是最新库表。默认为false。 - true：是最新库表。 - false：是恢复时间点库表。
        :type last_table_info: str
        :param restore_tables: 数据库信息。
        :type restore_tables: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreDatabaseTableInfo`]
        """
        
        

        self._restore_time = None
        self._last_table_info = None
        self._restore_tables = None
        self.discriminator = None

        self.restore_time = restore_time
        if last_table_info is not None:
            self.last_table_info = last_table_info
        self.restore_tables = restore_tables

    @property
    def restore_time(self):
        r"""Gets the restore_time of this CreateRestoreTablesRequestBody.

        备份时间点，时间戳格式。

        :return: The restore_time of this CreateRestoreTablesRequestBody.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this CreateRestoreTablesRequestBody.

        备份时间点，时间戳格式。

        :param restore_time: The restore_time of this CreateRestoreTablesRequestBody.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def last_table_info(self):
        r"""Gets the last_table_info of this CreateRestoreTablesRequestBody.

        是否是最新库表。默认为false。 - true：是最新库表。 - false：是恢复时间点库表。

        :return: The last_table_info of this CreateRestoreTablesRequestBody.
        :rtype: str
        """
        return self._last_table_info

    @last_table_info.setter
    def last_table_info(self, last_table_info):
        r"""Sets the last_table_info of this CreateRestoreTablesRequestBody.

        是否是最新库表。默认为false。 - true：是最新库表。 - false：是恢复时间点库表。

        :param last_table_info: The last_table_info of this CreateRestoreTablesRequestBody.
        :type last_table_info: str
        """
        self._last_table_info = last_table_info

    @property
    def restore_tables(self):
        r"""Gets the restore_tables of this CreateRestoreTablesRequestBody.

        数据库信息。

        :return: The restore_tables of this CreateRestoreTablesRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreDatabaseTableInfo`]
        """
        return self._restore_tables

    @restore_tables.setter
    def restore_tables(self, restore_tables):
        r"""Sets the restore_tables of this CreateRestoreTablesRequestBody.

        数据库信息。

        :param restore_tables: The restore_tables of this CreateRestoreTablesRequestBody.
        :type restore_tables: list[:class:`huaweicloudsdkgaussdb.v3.CreateRestoreDatabaseTableInfo`]
        """
        self._restore_tables = restore_tables

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
        if not isinstance(other, CreateRestoreTablesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
