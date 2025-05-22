# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bytes_done': 'int',
        'byte_left': 'int',
        'tables_done': 'int',
        'tables_left': 'int',
        'table_progress': 'int',
        'total_progress': 'int',
        'redis_rate': 'str',
        'estimated_time': 'str',
        'completed': 'bool',
        'initialed': 'bool',
        'fail_count': 'int',
        'redistributing': 'bool',
        'status': 'str',
        'pause_by_user': 'bool'
    }

    attribute_map = {
        'bytes_done': 'bytes_done',
        'byte_left': 'byte_left',
        'tables_done': 'tables_done',
        'tables_left': 'tables_left',
        'table_progress': 'table_progress',
        'total_progress': 'total_progress',
        'redis_rate': 'redis_rate',
        'estimated_time': 'estimated_time',
        'completed': 'completed',
        'initialed': 'initialed',
        'fail_count': 'fail_count',
        'redistributing': 'redistributing',
        'status': 'status',
        'pause_by_user': 'pause_by_user'
    }

    def __init__(self, bytes_done=None, byte_left=None, tables_done=None, tables_left=None, table_progress=None, total_progress=None, redis_rate=None, estimated_time=None, completed=None, initialed=None, fail_count=None, redistributing=None, status=None, pause_by_user=None):
        r"""RedisProgress

        The model defined in huaweicloud sdk

        :param bytes_done: **参数解释**： 已完成字节数。 **取值范围**： 不涉及。
        :type bytes_done: int
        :param byte_left: **参数解释**： 剩余字节数。 **取值范围**： 不涉及。
        :type byte_left: int
        :param tables_done: **参数解释**： 完成表数量。 **取值范围**： 不涉及。
        :type tables_done: int
        :param tables_left: **参数解释**： 剩余表数量。 **取值范围**： 不涉及。
        :type tables_left: int
        :param table_progress: **参数解释**： 表重分布进度。 **取值范围**： 1~100。
        :type table_progress: int
        :param total_progress: **参数解释**： 总进度。 **取值范围**： 1~100。
        :type total_progress: int
        :param redis_rate: **参数解释**： 重分布速度。 **取值范围**： 不涉及。
        :type redis_rate: str
        :param estimated_time: **参数解释**： 预估时间。 **取值范围**： 不涉及。
        :type estimated_time: str
        :param completed: **参数解释**： 是否已完成。 **取值范围**： 不涉及。
        :type completed: bool
        :param initialed: **参数解释**： 是否完成初始化。 **取值范围**： 不涉及。
        :type initialed: bool
        :param fail_count: **参数解释**： 失败次数。 **取值范围**： 不涉及。
        :type fail_count: int
        :param redistributing: **参数解释**： cm_ctl查询的重分布结果。 **取值范围**： 不涉及。
        :type redistributing: bool
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param pause_by_user: **参数解释**： 是否用户暂停。 **取值范围**： 不涉及。
        :type pause_by_user: bool
        """
        
        

        self._bytes_done = None
        self._byte_left = None
        self._tables_done = None
        self._tables_left = None
        self._table_progress = None
        self._total_progress = None
        self._redis_rate = None
        self._estimated_time = None
        self._completed = None
        self._initialed = None
        self._fail_count = None
        self._redistributing = None
        self._status = None
        self._pause_by_user = None
        self.discriminator = None

        if bytes_done is not None:
            self.bytes_done = bytes_done
        if byte_left is not None:
            self.byte_left = byte_left
        if tables_done is not None:
            self.tables_done = tables_done
        if tables_left is not None:
            self.tables_left = tables_left
        if table_progress is not None:
            self.table_progress = table_progress
        if total_progress is not None:
            self.total_progress = total_progress
        if redis_rate is not None:
            self.redis_rate = redis_rate
        if estimated_time is not None:
            self.estimated_time = estimated_time
        if completed is not None:
            self.completed = completed
        if initialed is not None:
            self.initialed = initialed
        if fail_count is not None:
            self.fail_count = fail_count
        if redistributing is not None:
            self.redistributing = redistributing
        if status is not None:
            self.status = status
        if pause_by_user is not None:
            self.pause_by_user = pause_by_user

    @property
    def bytes_done(self):
        r"""Gets the bytes_done of this RedisProgress.

        **参数解释**： 已完成字节数。 **取值范围**： 不涉及。

        :return: The bytes_done of this RedisProgress.
        :rtype: int
        """
        return self._bytes_done

    @bytes_done.setter
    def bytes_done(self, bytes_done):
        r"""Sets the bytes_done of this RedisProgress.

        **参数解释**： 已完成字节数。 **取值范围**： 不涉及。

        :param bytes_done: The bytes_done of this RedisProgress.
        :type bytes_done: int
        """
        self._bytes_done = bytes_done

    @property
    def byte_left(self):
        r"""Gets the byte_left of this RedisProgress.

        **参数解释**： 剩余字节数。 **取值范围**： 不涉及。

        :return: The byte_left of this RedisProgress.
        :rtype: int
        """
        return self._byte_left

    @byte_left.setter
    def byte_left(self, byte_left):
        r"""Sets the byte_left of this RedisProgress.

        **参数解释**： 剩余字节数。 **取值范围**： 不涉及。

        :param byte_left: The byte_left of this RedisProgress.
        :type byte_left: int
        """
        self._byte_left = byte_left

    @property
    def tables_done(self):
        r"""Gets the tables_done of this RedisProgress.

        **参数解释**： 完成表数量。 **取值范围**： 不涉及。

        :return: The tables_done of this RedisProgress.
        :rtype: int
        """
        return self._tables_done

    @tables_done.setter
    def tables_done(self, tables_done):
        r"""Sets the tables_done of this RedisProgress.

        **参数解释**： 完成表数量。 **取值范围**： 不涉及。

        :param tables_done: The tables_done of this RedisProgress.
        :type tables_done: int
        """
        self._tables_done = tables_done

    @property
    def tables_left(self):
        r"""Gets the tables_left of this RedisProgress.

        **参数解释**： 剩余表数量。 **取值范围**： 不涉及。

        :return: The tables_left of this RedisProgress.
        :rtype: int
        """
        return self._tables_left

    @tables_left.setter
    def tables_left(self, tables_left):
        r"""Sets the tables_left of this RedisProgress.

        **参数解释**： 剩余表数量。 **取值范围**： 不涉及。

        :param tables_left: The tables_left of this RedisProgress.
        :type tables_left: int
        """
        self._tables_left = tables_left

    @property
    def table_progress(self):
        r"""Gets the table_progress of this RedisProgress.

        **参数解释**： 表重分布进度。 **取值范围**： 1~100。

        :return: The table_progress of this RedisProgress.
        :rtype: int
        """
        return self._table_progress

    @table_progress.setter
    def table_progress(self, table_progress):
        r"""Sets the table_progress of this RedisProgress.

        **参数解释**： 表重分布进度。 **取值范围**： 1~100。

        :param table_progress: The table_progress of this RedisProgress.
        :type table_progress: int
        """
        self._table_progress = table_progress

    @property
    def total_progress(self):
        r"""Gets the total_progress of this RedisProgress.

        **参数解释**： 总进度。 **取值范围**： 1~100。

        :return: The total_progress of this RedisProgress.
        :rtype: int
        """
        return self._total_progress

    @total_progress.setter
    def total_progress(self, total_progress):
        r"""Sets the total_progress of this RedisProgress.

        **参数解释**： 总进度。 **取值范围**： 1~100。

        :param total_progress: The total_progress of this RedisProgress.
        :type total_progress: int
        """
        self._total_progress = total_progress

    @property
    def redis_rate(self):
        r"""Gets the redis_rate of this RedisProgress.

        **参数解释**： 重分布速度。 **取值范围**： 不涉及。

        :return: The redis_rate of this RedisProgress.
        :rtype: str
        """
        return self._redis_rate

    @redis_rate.setter
    def redis_rate(self, redis_rate):
        r"""Sets the redis_rate of this RedisProgress.

        **参数解释**： 重分布速度。 **取值范围**： 不涉及。

        :param redis_rate: The redis_rate of this RedisProgress.
        :type redis_rate: str
        """
        self._redis_rate = redis_rate

    @property
    def estimated_time(self):
        r"""Gets the estimated_time of this RedisProgress.

        **参数解释**： 预估时间。 **取值范围**： 不涉及。

        :return: The estimated_time of this RedisProgress.
        :rtype: str
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        r"""Sets the estimated_time of this RedisProgress.

        **参数解释**： 预估时间。 **取值范围**： 不涉及。

        :param estimated_time: The estimated_time of this RedisProgress.
        :type estimated_time: str
        """
        self._estimated_time = estimated_time

    @property
    def completed(self):
        r"""Gets the completed of this RedisProgress.

        **参数解释**： 是否已完成。 **取值范围**： 不涉及。

        :return: The completed of this RedisProgress.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        r"""Sets the completed of this RedisProgress.

        **参数解释**： 是否已完成。 **取值范围**： 不涉及。

        :param completed: The completed of this RedisProgress.
        :type completed: bool
        """
        self._completed = completed

    @property
    def initialed(self):
        r"""Gets the initialed of this RedisProgress.

        **参数解释**： 是否完成初始化。 **取值范围**： 不涉及。

        :return: The initialed of this RedisProgress.
        :rtype: bool
        """
        return self._initialed

    @initialed.setter
    def initialed(self, initialed):
        r"""Sets the initialed of this RedisProgress.

        **参数解释**： 是否完成初始化。 **取值范围**： 不涉及。

        :param initialed: The initialed of this RedisProgress.
        :type initialed: bool
        """
        self._initialed = initialed

    @property
    def fail_count(self):
        r"""Gets the fail_count of this RedisProgress.

        **参数解释**： 失败次数。 **取值范围**： 不涉及。

        :return: The fail_count of this RedisProgress.
        :rtype: int
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        r"""Sets the fail_count of this RedisProgress.

        **参数解释**： 失败次数。 **取值范围**： 不涉及。

        :param fail_count: The fail_count of this RedisProgress.
        :type fail_count: int
        """
        self._fail_count = fail_count

    @property
    def redistributing(self):
        r"""Gets the redistributing of this RedisProgress.

        **参数解释**： cm_ctl查询的重分布结果。 **取值范围**： 不涉及。

        :return: The redistributing of this RedisProgress.
        :rtype: bool
        """
        return self._redistributing

    @redistributing.setter
    def redistributing(self, redistributing):
        r"""Sets the redistributing of this RedisProgress.

        **参数解释**： cm_ctl查询的重分布结果。 **取值范围**： 不涉及。

        :param redistributing: The redistributing of this RedisProgress.
        :type redistributing: bool
        """
        self._redistributing = redistributing

    @property
    def status(self):
        r"""Gets the status of this RedisProgress.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this RedisProgress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RedisProgress.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this RedisProgress.
        :type status: str
        """
        self._status = status

    @property
    def pause_by_user(self):
        r"""Gets the pause_by_user of this RedisProgress.

        **参数解释**： 是否用户暂停。 **取值范围**： 不涉及。

        :return: The pause_by_user of this RedisProgress.
        :rtype: bool
        """
        return self._pause_by_user

    @pause_by_user.setter
    def pause_by_user(self, pause_by_user):
        r"""Sets the pause_by_user of this RedisProgress.

        **参数解释**： 是否用户暂停。 **取值范围**： 不涉及。

        :param pause_by_user: The pause_by_user of this RedisProgress.
        :type pause_by_user: bool
        """
        self._pause_by_user = pause_by_user

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
        if not isinstance(other, RedisProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
