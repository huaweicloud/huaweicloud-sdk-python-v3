# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePartitionCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_timestamp': 'int',
        'src_partition_count': 'int',
        'target_partition_count': 'int',
        'result_code': 'int',
        'result_msg': 'int',
        'auto_scale': 'bool'
    }

    attribute_map = {
        'create_timestamp': 'create_timestamp',
        'src_partition_count': 'src_partition_count',
        'target_partition_count': 'target_partition_count',
        'result_code': 'result_code',
        'result_msg': 'result_msg',
        'auto_scale': 'auto_scale'
    }

    def __init__(self, create_timestamp=None, src_partition_count=None, target_partition_count=None, result_code=None, result_msg=None, auto_scale=None):
        r"""UpdatePartitionCount

        The model defined in huaweicloud sdk

        :param create_timestamp: 扩缩容操作执行时间戳，13位时间戳。
        :type create_timestamp: int
        :param src_partition_count: 扩缩容操作前分区数量。
        :type src_partition_count: int
        :param target_partition_count: 扩缩容操作后分区数量。
        :type target_partition_count: int
        :param result_code: 扩缩容操作响应码。
        :type result_code: int
        :param result_msg: 扩缩容操作响应信息。
        :type result_msg: int
        :param auto_scale: 本次扩缩容操作是否为自动扩缩容。  - true：自动扩缩容。 - false：手动扩缩容。
        :type auto_scale: bool
        """
        
        

        self._create_timestamp = None
        self._src_partition_count = None
        self._target_partition_count = None
        self._result_code = None
        self._result_msg = None
        self._auto_scale = None
        self.discriminator = None

        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if src_partition_count is not None:
            self.src_partition_count = src_partition_count
        if target_partition_count is not None:
            self.target_partition_count = target_partition_count
        if result_code is not None:
            self.result_code = result_code
        if result_msg is not None:
            self.result_msg = result_msg
        if auto_scale is not None:
            self.auto_scale = auto_scale

    @property
    def create_timestamp(self):
        r"""Gets the create_timestamp of this UpdatePartitionCount.

        扩缩容操作执行时间戳，13位时间戳。

        :return: The create_timestamp of this UpdatePartitionCount.
        :rtype: int
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        r"""Sets the create_timestamp of this UpdatePartitionCount.

        扩缩容操作执行时间戳，13位时间戳。

        :param create_timestamp: The create_timestamp of this UpdatePartitionCount.
        :type create_timestamp: int
        """
        self._create_timestamp = create_timestamp

    @property
    def src_partition_count(self):
        r"""Gets the src_partition_count of this UpdatePartitionCount.

        扩缩容操作前分区数量。

        :return: The src_partition_count of this UpdatePartitionCount.
        :rtype: int
        """
        return self._src_partition_count

    @src_partition_count.setter
    def src_partition_count(self, src_partition_count):
        r"""Sets the src_partition_count of this UpdatePartitionCount.

        扩缩容操作前分区数量。

        :param src_partition_count: The src_partition_count of this UpdatePartitionCount.
        :type src_partition_count: int
        """
        self._src_partition_count = src_partition_count

    @property
    def target_partition_count(self):
        r"""Gets the target_partition_count of this UpdatePartitionCount.

        扩缩容操作后分区数量。

        :return: The target_partition_count of this UpdatePartitionCount.
        :rtype: int
        """
        return self._target_partition_count

    @target_partition_count.setter
    def target_partition_count(self, target_partition_count):
        r"""Sets the target_partition_count of this UpdatePartitionCount.

        扩缩容操作后分区数量。

        :param target_partition_count: The target_partition_count of this UpdatePartitionCount.
        :type target_partition_count: int
        """
        self._target_partition_count = target_partition_count

    @property
    def result_code(self):
        r"""Gets the result_code of this UpdatePartitionCount.

        扩缩容操作响应码。

        :return: The result_code of this UpdatePartitionCount.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this UpdatePartitionCount.

        扩缩容操作响应码。

        :param result_code: The result_code of this UpdatePartitionCount.
        :type result_code: int
        """
        self._result_code = result_code

    @property
    def result_msg(self):
        r"""Gets the result_msg of this UpdatePartitionCount.

        扩缩容操作响应信息。

        :return: The result_msg of this UpdatePartitionCount.
        :rtype: int
        """
        return self._result_msg

    @result_msg.setter
    def result_msg(self, result_msg):
        r"""Sets the result_msg of this UpdatePartitionCount.

        扩缩容操作响应信息。

        :param result_msg: The result_msg of this UpdatePartitionCount.
        :type result_msg: int
        """
        self._result_msg = result_msg

    @property
    def auto_scale(self):
        r"""Gets the auto_scale of this UpdatePartitionCount.

        本次扩缩容操作是否为自动扩缩容。  - true：自动扩缩容。 - false：手动扩缩容。

        :return: The auto_scale of this UpdatePartitionCount.
        :rtype: bool
        """
        return self._auto_scale

    @auto_scale.setter
    def auto_scale(self, auto_scale):
        r"""Sets the auto_scale of this UpdatePartitionCount.

        本次扩缩容操作是否为自动扩缩容。  - true：自动扩缩容。 - false：手动扩缩容。

        :param auto_scale: The auto_scale of this UpdatePartitionCount.
        :type auto_scale: bool
        """
        self._auto_scale = auto_scale

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
        if not isinstance(other, UpdatePartitionCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
