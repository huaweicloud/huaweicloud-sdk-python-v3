# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLockTrendPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'occurrence_time': 'int',
        'total_deadlock_count': 'int',
        'key_deadlock_count': 'int',
        'object_deadlock_count': 'int',
        'rid_deadlock_count': 'int',
        'page_deadlock_count': 'int',
        'compile_deadlock_count': 'int'
    }

    attribute_map = {
        'occurrence_time': 'occurrence_time',
        'total_deadlock_count': 'total_deadlock_count',
        'key_deadlock_count': 'key_deadlock_count',
        'object_deadlock_count': 'object_deadlock_count',
        'rid_deadlock_count': 'rid_deadlock_count',
        'page_deadlock_count': 'page_deadlock_count',
        'compile_deadlock_count': 'compile_deadlock_count'
    }

    def __init__(self, occurrence_time=None, total_deadlock_count=None, key_deadlock_count=None, object_deadlock_count=None, rid_deadlock_count=None, page_deadlock_count=None, compile_deadlock_count=None):
        r"""DeadLockTrendPoint

        The model defined in huaweicloud sdk

        :param occurrence_time: 发生时间
        :type occurrence_time: int
        :param total_deadlock_count: 死锁总数
        :type total_deadlock_count: int
        :param key_deadlock_count: keylock数量
        :type key_deadlock_count: int
        :param object_deadlock_count: objectlock数量
        :type object_deadlock_count: int
        :param rid_deadlock_count: ridlock数量
        :type rid_deadlock_count: int
        :param page_deadlock_count: pagelock数量
        :type page_deadlock_count: int
        :param compile_deadlock_count: compilelock数量
        :type compile_deadlock_count: int
        """
        
        

        self._occurrence_time = None
        self._total_deadlock_count = None
        self._key_deadlock_count = None
        self._object_deadlock_count = None
        self._rid_deadlock_count = None
        self._page_deadlock_count = None
        self._compile_deadlock_count = None
        self.discriminator = None

        if occurrence_time is not None:
            self.occurrence_time = occurrence_time
        if total_deadlock_count is not None:
            self.total_deadlock_count = total_deadlock_count
        if key_deadlock_count is not None:
            self.key_deadlock_count = key_deadlock_count
        if object_deadlock_count is not None:
            self.object_deadlock_count = object_deadlock_count
        if rid_deadlock_count is not None:
            self.rid_deadlock_count = rid_deadlock_count
        if page_deadlock_count is not None:
            self.page_deadlock_count = page_deadlock_count
        if compile_deadlock_count is not None:
            self.compile_deadlock_count = compile_deadlock_count

    @property
    def occurrence_time(self):
        r"""Gets the occurrence_time of this DeadLockTrendPoint.

        发生时间

        :return: The occurrence_time of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, occurrence_time):
        r"""Sets the occurrence_time of this DeadLockTrendPoint.

        发生时间

        :param occurrence_time: The occurrence_time of this DeadLockTrendPoint.
        :type occurrence_time: int
        """
        self._occurrence_time = occurrence_time

    @property
    def total_deadlock_count(self):
        r"""Gets the total_deadlock_count of this DeadLockTrendPoint.

        死锁总数

        :return: The total_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._total_deadlock_count

    @total_deadlock_count.setter
    def total_deadlock_count(self, total_deadlock_count):
        r"""Sets the total_deadlock_count of this DeadLockTrendPoint.

        死锁总数

        :param total_deadlock_count: The total_deadlock_count of this DeadLockTrendPoint.
        :type total_deadlock_count: int
        """
        self._total_deadlock_count = total_deadlock_count

    @property
    def key_deadlock_count(self):
        r"""Gets the key_deadlock_count of this DeadLockTrendPoint.

        keylock数量

        :return: The key_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._key_deadlock_count

    @key_deadlock_count.setter
    def key_deadlock_count(self, key_deadlock_count):
        r"""Sets the key_deadlock_count of this DeadLockTrendPoint.

        keylock数量

        :param key_deadlock_count: The key_deadlock_count of this DeadLockTrendPoint.
        :type key_deadlock_count: int
        """
        self._key_deadlock_count = key_deadlock_count

    @property
    def object_deadlock_count(self):
        r"""Gets the object_deadlock_count of this DeadLockTrendPoint.

        objectlock数量

        :return: The object_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._object_deadlock_count

    @object_deadlock_count.setter
    def object_deadlock_count(self, object_deadlock_count):
        r"""Sets the object_deadlock_count of this DeadLockTrendPoint.

        objectlock数量

        :param object_deadlock_count: The object_deadlock_count of this DeadLockTrendPoint.
        :type object_deadlock_count: int
        """
        self._object_deadlock_count = object_deadlock_count

    @property
    def rid_deadlock_count(self):
        r"""Gets the rid_deadlock_count of this DeadLockTrendPoint.

        ridlock数量

        :return: The rid_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._rid_deadlock_count

    @rid_deadlock_count.setter
    def rid_deadlock_count(self, rid_deadlock_count):
        r"""Sets the rid_deadlock_count of this DeadLockTrendPoint.

        ridlock数量

        :param rid_deadlock_count: The rid_deadlock_count of this DeadLockTrendPoint.
        :type rid_deadlock_count: int
        """
        self._rid_deadlock_count = rid_deadlock_count

    @property
    def page_deadlock_count(self):
        r"""Gets the page_deadlock_count of this DeadLockTrendPoint.

        pagelock数量

        :return: The page_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._page_deadlock_count

    @page_deadlock_count.setter
    def page_deadlock_count(self, page_deadlock_count):
        r"""Sets the page_deadlock_count of this DeadLockTrendPoint.

        pagelock数量

        :param page_deadlock_count: The page_deadlock_count of this DeadLockTrendPoint.
        :type page_deadlock_count: int
        """
        self._page_deadlock_count = page_deadlock_count

    @property
    def compile_deadlock_count(self):
        r"""Gets the compile_deadlock_count of this DeadLockTrendPoint.

        compilelock数量

        :return: The compile_deadlock_count of this DeadLockTrendPoint.
        :rtype: int
        """
        return self._compile_deadlock_count

    @compile_deadlock_count.setter
    def compile_deadlock_count(self, compile_deadlock_count):
        r"""Sets the compile_deadlock_count of this DeadLockTrendPoint.

        compilelock数量

        :param compile_deadlock_count: The compile_deadlock_count of this DeadLockTrendPoint.
        :type compile_deadlock_count: int
        """
        self._compile_deadlock_count = compile_deadlock_count

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
        if not isinstance(other, DeadLockTrendPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
