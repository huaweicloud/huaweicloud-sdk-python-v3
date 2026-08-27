# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxnItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trx_id': 'str',
        'estimated_remaining_time': 'int',
        'trx_mysql_thread_id': 'int',
        'trx_query': 'str',
        'trx_started': 'str',
        'trx_rows_modified': 'int'
    }

    attribute_map = {
        'trx_id': 'trx_id',
        'estimated_remaining_time': 'estimated_remaining_time',
        'trx_mysql_thread_id': 'trx_mysql_thread_id',
        'trx_query': 'trx_query',
        'trx_started': 'trx_started',
        'trx_rows_modified': 'trx_rows_modified'
    }

    def __init__(self, trx_id=None, estimated_remaining_time=None, trx_mysql_thread_id=None, trx_query=None, trx_started=None, trx_rows_modified=None):
        r"""TxnItem

        The model defined in huaweicloud sdk

        :param trx_id: **参数解释**： 事务的唯一标识。 **取值范围**： 不涉及。
        :type trx_id: str
        :param estimated_remaining_time: **参数解释**： 预计剩余完成时间（秒）。 **取值范围**： ＞0。 
        :type estimated_remaining_time: int
        :param trx_mysql_thread_id: **参数解释**： 用户会话线程ID。 **取值范围**： 不涉及。
        :type trx_mysql_thread_id: int
        :param trx_query: **参数解释**： 额外信息，通常是正在执行的语句。 **取值范围**： 不涉及。 
        :type trx_query: str
        :param trx_started: **参数解释**： 事务开始时间。 **取值范围**： 不涉及。 
        :type trx_started: str
        :param trx_rows_modified: **参数解释**： 事务修改的行数。 **取值范围**： ≥0。 
        :type trx_rows_modified: int
        """
        
        

        self._trx_id = None
        self._estimated_remaining_time = None
        self._trx_mysql_thread_id = None
        self._trx_query = None
        self._trx_started = None
        self._trx_rows_modified = None
        self.discriminator = None

        self.trx_id = trx_id
        self.estimated_remaining_time = estimated_remaining_time
        self.trx_mysql_thread_id = trx_mysql_thread_id
        self.trx_query = trx_query
        self.trx_started = trx_started
        self.trx_rows_modified = trx_rows_modified

    @property
    def trx_id(self):
        r"""Gets the trx_id of this TxnItem.

        **参数解释**： 事务的唯一标识。 **取值范围**： 不涉及。

        :return: The trx_id of this TxnItem.
        :rtype: str
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this TxnItem.

        **参数解释**： 事务的唯一标识。 **取值范围**： 不涉及。

        :param trx_id: The trx_id of this TxnItem.
        :type trx_id: str
        """
        self._trx_id = trx_id

    @property
    def estimated_remaining_time(self):
        r"""Gets the estimated_remaining_time of this TxnItem.

        **参数解释**： 预计剩余完成时间（秒）。 **取值范围**： ＞0。 

        :return: The estimated_remaining_time of this TxnItem.
        :rtype: int
        """
        return self._estimated_remaining_time

    @estimated_remaining_time.setter
    def estimated_remaining_time(self, estimated_remaining_time):
        r"""Sets the estimated_remaining_time of this TxnItem.

        **参数解释**： 预计剩余完成时间（秒）。 **取值范围**： ＞0。 

        :param estimated_remaining_time: The estimated_remaining_time of this TxnItem.
        :type estimated_remaining_time: int
        """
        self._estimated_remaining_time = estimated_remaining_time

    @property
    def trx_mysql_thread_id(self):
        r"""Gets the trx_mysql_thread_id of this TxnItem.

        **参数解释**： 用户会话线程ID。 **取值范围**： 不涉及。

        :return: The trx_mysql_thread_id of this TxnItem.
        :rtype: int
        """
        return self._trx_mysql_thread_id

    @trx_mysql_thread_id.setter
    def trx_mysql_thread_id(self, trx_mysql_thread_id):
        r"""Sets the trx_mysql_thread_id of this TxnItem.

        **参数解释**： 用户会话线程ID。 **取值范围**： 不涉及。

        :param trx_mysql_thread_id: The trx_mysql_thread_id of this TxnItem.
        :type trx_mysql_thread_id: int
        """
        self._trx_mysql_thread_id = trx_mysql_thread_id

    @property
    def trx_query(self):
        r"""Gets the trx_query of this TxnItem.

        **参数解释**： 额外信息，通常是正在执行的语句。 **取值范围**： 不涉及。 

        :return: The trx_query of this TxnItem.
        :rtype: str
        """
        return self._trx_query

    @trx_query.setter
    def trx_query(self, trx_query):
        r"""Sets the trx_query of this TxnItem.

        **参数解释**： 额外信息，通常是正在执行的语句。 **取值范围**： 不涉及。 

        :param trx_query: The trx_query of this TxnItem.
        :type trx_query: str
        """
        self._trx_query = trx_query

    @property
    def trx_started(self):
        r"""Gets the trx_started of this TxnItem.

        **参数解释**： 事务开始时间。 **取值范围**： 不涉及。 

        :return: The trx_started of this TxnItem.
        :rtype: str
        """
        return self._trx_started

    @trx_started.setter
    def trx_started(self, trx_started):
        r"""Sets the trx_started of this TxnItem.

        **参数解释**： 事务开始时间。 **取值范围**： 不涉及。 

        :param trx_started: The trx_started of this TxnItem.
        :type trx_started: str
        """
        self._trx_started = trx_started

    @property
    def trx_rows_modified(self):
        r"""Gets the trx_rows_modified of this TxnItem.

        **参数解释**： 事务修改的行数。 **取值范围**： ≥0。 

        :return: The trx_rows_modified of this TxnItem.
        :rtype: int
        """
        return self._trx_rows_modified

    @trx_rows_modified.setter
    def trx_rows_modified(self, trx_rows_modified):
        r"""Sets the trx_rows_modified of this TxnItem.

        **参数解释**： 事务修改的行数。 **取值范围**： ≥0。 

        :param trx_rows_modified: The trx_rows_modified of this TxnItem.
        :type trx_rows_modified: int
        """
        self._trx_rows_modified = trx_rows_modified

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
        if not isinstance(other, TxnItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
