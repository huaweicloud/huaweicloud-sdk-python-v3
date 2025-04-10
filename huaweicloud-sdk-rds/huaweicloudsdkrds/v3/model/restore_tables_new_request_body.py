# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreTablesNewRequestBody:

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
        'restore_tables': 'list[RestoreDatabasesInfoNew]',
        'is_fast_restore': 'bool'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'restore_tables': 'restore_tables',
        'is_fast_restore': 'is_fast_restore'
    }

    def __init__(self, restore_time=None, restore_tables=None, is_fast_restore=None):
        r"""RestoreTablesNewRequestBody

        The model defined in huaweicloud sdk

        :param restore_time: 恢复时间戳
        :type restore_time: int
        :param restore_tables: 表信息
        :type restore_tables: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfoNew`]
        :param is_fast_restore: 是否使用极速恢复，可先根据“获取实例是否能使用极速恢复”接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！
        :type is_fast_restore: bool
        """
        
        

        self._restore_time = None
        self._restore_tables = None
        self._is_fast_restore = None
        self.discriminator = None

        self.restore_time = restore_time
        self.restore_tables = restore_tables
        if is_fast_restore is not None:
            self.is_fast_restore = is_fast_restore

    @property
    def restore_time(self):
        r"""Gets the restore_time of this RestoreTablesNewRequestBody.

        恢复时间戳

        :return: The restore_time of this RestoreTablesNewRequestBody.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this RestoreTablesNewRequestBody.

        恢复时间戳

        :param restore_time: The restore_time of this RestoreTablesNewRequestBody.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def restore_tables(self):
        r"""Gets the restore_tables of this RestoreTablesNewRequestBody.

        表信息

        :return: The restore_tables of this RestoreTablesNewRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfoNew`]
        """
        return self._restore_tables

    @restore_tables.setter
    def restore_tables(self, restore_tables):
        r"""Sets the restore_tables of this RestoreTablesNewRequestBody.

        表信息

        :param restore_tables: The restore_tables of this RestoreTablesNewRequestBody.
        :type restore_tables: list[:class:`huaweicloudsdkrds.v3.RestoreDatabasesInfoNew`]
        """
        self._restore_tables = restore_tables

    @property
    def is_fast_restore(self):
        r"""Gets the is_fast_restore of this RestoreTablesNewRequestBody.

        是否使用极速恢复，可先根据“获取实例是否能使用极速恢复”接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！

        :return: The is_fast_restore of this RestoreTablesNewRequestBody.
        :rtype: bool
        """
        return self._is_fast_restore

    @is_fast_restore.setter
    def is_fast_restore(self, is_fast_restore):
        r"""Sets the is_fast_restore of this RestoreTablesNewRequestBody.

        是否使用极速恢复，可先根据“获取实例是否能使用极速恢复”接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！

        :param is_fast_restore: The is_fast_restore of this RestoreTablesNewRequestBody.
        :type is_fast_restore: bool
        """
        self._is_fast_restore = is_fast_restore

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
        if not isinstance(other, RestoreTablesNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
