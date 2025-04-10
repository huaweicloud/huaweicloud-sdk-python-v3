# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlLimitRuleReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'id': 'str',
        'max_concurrency': 'int',
        'max_waiting': 'int'
    }

    attribute_map = {
        'db_name': 'db_name',
        'id': 'id',
        'max_concurrency': 'max_concurrency',
        'max_waiting': 'max_waiting'
    }

    def __init__(self, db_name=None, id=None, max_concurrency=None, max_waiting=None):
        r"""UpdateSqlLimitRuleReqV3

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。
        :type db_name: str
        :param id: SQL限流ID。
        :type id: str
        :param max_concurrency: 同时执行的sql数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。
        :type max_concurrency: int
        :param max_waiting: 最大等待时间，单位为秒。
        :type max_waiting: int
        """
        
        

        self._db_name = None
        self._id = None
        self._max_concurrency = None
        self._max_waiting = None
        self.discriminator = None

        self.db_name = db_name
        self.id = id
        self.max_concurrency = max_concurrency
        self.max_waiting = max_waiting

    @property
    def db_name(self):
        r"""Gets the db_name of this UpdateSqlLimitRuleReqV3.

        数据库名称。

        :return: The db_name of this UpdateSqlLimitRuleReqV3.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this UpdateSqlLimitRuleReqV3.

        数据库名称。

        :param db_name: The db_name of this UpdateSqlLimitRuleReqV3.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def id(self):
        r"""Gets the id of this UpdateSqlLimitRuleReqV3.

        SQL限流ID。

        :return: The id of this UpdateSqlLimitRuleReqV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSqlLimitRuleReqV3.

        SQL限流ID。

        :param id: The id of this UpdateSqlLimitRuleReqV3.
        :type id: str
        """
        self._id = id

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this UpdateSqlLimitRuleReqV3.

        同时执行的sql数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。

        :return: The max_concurrency of this UpdateSqlLimitRuleReqV3.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this UpdateSqlLimitRuleReqV3.

        同时执行的sql数量，小于等于0表示不限制，默认为0，取值范围（-1~50000）。

        :param max_concurrency: The max_concurrency of this UpdateSqlLimitRuleReqV3.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def max_waiting(self):
        r"""Gets the max_waiting of this UpdateSqlLimitRuleReqV3.

        最大等待时间，单位为秒。

        :return: The max_waiting of this UpdateSqlLimitRuleReqV3.
        :rtype: int
        """
        return self._max_waiting

    @max_waiting.setter
    def max_waiting(self, max_waiting):
        r"""Sets the max_waiting of this UpdateSqlLimitRuleReqV3.

        最大等待时间，单位为秒。

        :param max_waiting: The max_waiting of this UpdateSqlLimitRuleReqV3.
        :type max_waiting: int
        """
        self._max_waiting = max_waiting

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
        if not isinstance(other, UpdateSqlLimitRuleReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
