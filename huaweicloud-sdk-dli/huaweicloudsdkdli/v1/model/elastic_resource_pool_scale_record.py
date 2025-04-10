# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElasticResourcePoolScaleRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_cu': 'int',
        'min_cu': 'int',
        'current_cu': 'int',
        'origin_cu': 'int',
        'target_cu': 'int',
        'record_time': 'int',
        'status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'max_cu': 'max_cu',
        'min_cu': 'min_cu',
        'current_cu': 'current_cu',
        'origin_cu': 'origin_cu',
        'target_cu': 'target_cu',
        'record_time': 'record_time',
        'status': 'status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, max_cu=None, min_cu=None, current_cu=None, origin_cu=None, target_cu=None, record_time=None, status=None, fail_reason=None):
        r"""ElasticResourcePoolScaleRecord

        The model defined in huaweicloud sdk

        :param max_cu: 最大Cu
        :type max_cu: int
        :param min_cu: 最小CU
        :type min_cu: int
        :param current_cu: 扩缩容后CU
        :type current_cu: int
        :param origin_cu: 扩缩容前CU
        :type origin_cu: int
        :param target_cu: 扩缩容预期CU
        :type target_cu: int
        :param record_time: 操作完成时间
        :type record_time: int
        :param status: 扩缩容成功或者失败的状态
        :type status: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        """
        
        

        self._max_cu = None
        self._min_cu = None
        self._current_cu = None
        self._origin_cu = None
        self._target_cu = None
        self._record_time = None
        self._status = None
        self._fail_reason = None
        self.discriminator = None

        self.max_cu = max_cu
        self.min_cu = min_cu
        self.current_cu = current_cu
        self.origin_cu = origin_cu
        self.target_cu = target_cu
        self.record_time = record_time
        self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def max_cu(self):
        r"""Gets the max_cu of this ElasticResourcePoolScaleRecord.

        最大Cu

        :return: The max_cu of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        r"""Sets the max_cu of this ElasticResourcePoolScaleRecord.

        最大Cu

        :param max_cu: The max_cu of this ElasticResourcePoolScaleRecord.
        :type max_cu: int
        """
        self._max_cu = max_cu

    @property
    def min_cu(self):
        r"""Gets the min_cu of this ElasticResourcePoolScaleRecord.

        最小CU

        :return: The min_cu of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        r"""Sets the min_cu of this ElasticResourcePoolScaleRecord.

        最小CU

        :param min_cu: The min_cu of this ElasticResourcePoolScaleRecord.
        :type min_cu: int
        """
        self._min_cu = min_cu

    @property
    def current_cu(self):
        r"""Gets the current_cu of this ElasticResourcePoolScaleRecord.

        扩缩容后CU

        :return: The current_cu of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._current_cu

    @current_cu.setter
    def current_cu(self, current_cu):
        r"""Sets the current_cu of this ElasticResourcePoolScaleRecord.

        扩缩容后CU

        :param current_cu: The current_cu of this ElasticResourcePoolScaleRecord.
        :type current_cu: int
        """
        self._current_cu = current_cu

    @property
    def origin_cu(self):
        r"""Gets the origin_cu of this ElasticResourcePoolScaleRecord.

        扩缩容前CU

        :return: The origin_cu of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._origin_cu

    @origin_cu.setter
    def origin_cu(self, origin_cu):
        r"""Sets the origin_cu of this ElasticResourcePoolScaleRecord.

        扩缩容前CU

        :param origin_cu: The origin_cu of this ElasticResourcePoolScaleRecord.
        :type origin_cu: int
        """
        self._origin_cu = origin_cu

    @property
    def target_cu(self):
        r"""Gets the target_cu of this ElasticResourcePoolScaleRecord.

        扩缩容预期CU

        :return: The target_cu of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._target_cu

    @target_cu.setter
    def target_cu(self, target_cu):
        r"""Sets the target_cu of this ElasticResourcePoolScaleRecord.

        扩缩容预期CU

        :param target_cu: The target_cu of this ElasticResourcePoolScaleRecord.
        :type target_cu: int
        """
        self._target_cu = target_cu

    @property
    def record_time(self):
        r"""Gets the record_time of this ElasticResourcePoolScaleRecord.

        操作完成时间

        :return: The record_time of this ElasticResourcePoolScaleRecord.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this ElasticResourcePoolScaleRecord.

        操作完成时间

        :param record_time: The record_time of this ElasticResourcePoolScaleRecord.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def status(self):
        r"""Gets the status of this ElasticResourcePoolScaleRecord.

        扩缩容成功或者失败的状态

        :return: The status of this ElasticResourcePoolScaleRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ElasticResourcePoolScaleRecord.

        扩缩容成功或者失败的状态

        :param status: The status of this ElasticResourcePoolScaleRecord.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ElasticResourcePoolScaleRecord.

        失败原因

        :return: The fail_reason of this ElasticResourcePoolScaleRecord.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ElasticResourcePoolScaleRecord.

        失败原因

        :param fail_reason: The fail_reason of this ElasticResourcePoolScaleRecord.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ElasticResourcePoolScaleRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
