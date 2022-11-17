# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreTablesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'int',
        'restore_tables': 'list[RestoreDatabasesInfo]'
    }

    attribute_map = {
        'restore_time': 'restoreTime',
        'restore_tables': 'restoreTables'
    }

    def __init__(self, restore_time=None, restore_tables=None):
        """RestoreTablesRequestBody

        The model defined in huaweicloud sdk

        :param restore_time: 恢复时间戳
        :type restore_time: int
        :param restore_tables: 表信息
        :type restore_tables: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfo`]
        """
        
        

        self._restore_time = None
        self._restore_tables = None
        self.discriminator = None

        self.restore_time = restore_time
        self.restore_tables = restore_tables

    @property
    def restore_time(self):
        """Gets the restore_time of this RestoreTablesRequestBody.

        恢复时间戳

        :return: The restore_time of this RestoreTablesRequestBody.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestoreTablesRequestBody.

        恢复时间戳

        :param restore_time: The restore_time of this RestoreTablesRequestBody.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def restore_tables(self):
        """Gets the restore_tables of this RestoreTablesRequestBody.

        表信息

        :return: The restore_tables of this RestoreTablesRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfo`]
        """
        return self._restore_tables

    @restore_tables.setter
    def restore_tables(self, restore_tables):
        """Sets the restore_tables of this RestoreTablesRequestBody.

        表信息

        :param restore_tables: The restore_tables of this RestoreTablesRequestBody.
        :type restore_tables: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfo`]
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
        if not isinstance(other, RestoreTablesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
