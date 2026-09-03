# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SQLTplCmp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_tpl_dto1': 'TplCmp',
        'sql_tpl_dto2': 'TplCmp',
        'new': 'bool',
        'execute_time_increase': 'bool',
        'lock_wait_increase': 'bool'
    }

    attribute_map = {
        'sql_tpl_dto1': 'sql_tpl_dto1',
        'sql_tpl_dto2': 'sql_tpl_dto2',
        'new': 'new',
        'execute_time_increase': 'execute_time_increase',
        'lock_wait_increase': 'lock_wait_increase'
    }

    def __init__(self, sql_tpl_dto1=None, sql_tpl_dto2=None, new=None, execute_time_increase=None, lock_wait_increase=None):
        r"""SQLTplCmp

        The model defined in huaweicloud sdk

        :param sql_tpl_dto1: 
        :type sql_tpl_dto1: :class:`huaweicloudsdkdas.v3.TplCmp`
        :param sql_tpl_dto2: 
        :type sql_tpl_dto2: :class:`huaweicloudsdkdas.v3.TplCmp`
        :param new: 是否为新增数据
        :type new: bool
        :param execute_time_increase: 是否有执行时间增长
        :type execute_time_increase: bool
        :param lock_wait_increase: 是否有锁等待时间增长
        :type lock_wait_increase: bool
        """
        
        

        self._sql_tpl_dto1 = None
        self._sql_tpl_dto2 = None
        self._new = None
        self._execute_time_increase = None
        self._lock_wait_increase = None
        self.discriminator = None

        if sql_tpl_dto1 is not None:
            self.sql_tpl_dto1 = sql_tpl_dto1
        if sql_tpl_dto2 is not None:
            self.sql_tpl_dto2 = sql_tpl_dto2
        if new is not None:
            self.new = new
        if execute_time_increase is not None:
            self.execute_time_increase = execute_time_increase
        if lock_wait_increase is not None:
            self.lock_wait_increase = lock_wait_increase

    @property
    def sql_tpl_dto1(self):
        r"""Gets the sql_tpl_dto1 of this SQLTplCmp.

        :return: The sql_tpl_dto1 of this SQLTplCmp.
        :rtype: :class:`huaweicloudsdkdas.v3.TplCmp`
        """
        return self._sql_tpl_dto1

    @sql_tpl_dto1.setter
    def sql_tpl_dto1(self, sql_tpl_dto1):
        r"""Sets the sql_tpl_dto1 of this SQLTplCmp.

        :param sql_tpl_dto1: The sql_tpl_dto1 of this SQLTplCmp.
        :type sql_tpl_dto1: :class:`huaweicloudsdkdas.v3.TplCmp`
        """
        self._sql_tpl_dto1 = sql_tpl_dto1

    @property
    def sql_tpl_dto2(self):
        r"""Gets the sql_tpl_dto2 of this SQLTplCmp.

        :return: The sql_tpl_dto2 of this SQLTplCmp.
        :rtype: :class:`huaweicloudsdkdas.v3.TplCmp`
        """
        return self._sql_tpl_dto2

    @sql_tpl_dto2.setter
    def sql_tpl_dto2(self, sql_tpl_dto2):
        r"""Sets the sql_tpl_dto2 of this SQLTplCmp.

        :param sql_tpl_dto2: The sql_tpl_dto2 of this SQLTplCmp.
        :type sql_tpl_dto2: :class:`huaweicloudsdkdas.v3.TplCmp`
        """
        self._sql_tpl_dto2 = sql_tpl_dto2

    @property
    def new(self):
        r"""Gets the new of this SQLTplCmp.

        是否为新增数据

        :return: The new of this SQLTplCmp.
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        r"""Sets the new of this SQLTplCmp.

        是否为新增数据

        :param new: The new of this SQLTplCmp.
        :type new: bool
        """
        self._new = new

    @property
    def execute_time_increase(self):
        r"""Gets the execute_time_increase of this SQLTplCmp.

        是否有执行时间增长

        :return: The execute_time_increase of this SQLTplCmp.
        :rtype: bool
        """
        return self._execute_time_increase

    @execute_time_increase.setter
    def execute_time_increase(self, execute_time_increase):
        r"""Sets the execute_time_increase of this SQLTplCmp.

        是否有执行时间增长

        :param execute_time_increase: The execute_time_increase of this SQLTplCmp.
        :type execute_time_increase: bool
        """
        self._execute_time_increase = execute_time_increase

    @property
    def lock_wait_increase(self):
        r"""Gets the lock_wait_increase of this SQLTplCmp.

        是否有锁等待时间增长

        :return: The lock_wait_increase of this SQLTplCmp.
        :rtype: bool
        """
        return self._lock_wait_increase

    @lock_wait_increase.setter
    def lock_wait_increase(self, lock_wait_increase):
        r"""Sets the lock_wait_increase of this SQLTplCmp.

        是否有锁等待时间增长

        :param lock_wait_increase: The lock_wait_increase of this SQLTplCmp.
        :type lock_wait_increase: bool
        """
        self._lock_wait_increase = lock_wait_increase

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
        if not isinstance(other, SQLTplCmp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
