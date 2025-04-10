# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScaleInPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idle_time': 'int',
        'threshold': 'int',
        'delay_after_add': 'int',
        'delay_after_delete': 'int',
        'delay_after_failure': 'int',
        'max_nodes_batch_deletion': 'int',
        'check_interval': 'int'
    }

    attribute_map = {
        'idle_time': 'idle_time',
        'threshold': 'threshold',
        'delay_after_add': 'delay_after_add',
        'delay_after_delete': 'delay_after_delete',
        'delay_after_failure': 'delay_after_failure',
        'max_nodes_batch_deletion': 'max_nodes_batch_deletion',
        'check_interval': 'check_interval'
    }

    def __init__(self, idle_time=None, threshold=None, delay_after_add=None, delay_after_delete=None, delay_after_failure=None, max_nodes_batch_deletion=None, check_interval=None):
        r"""ShowScaleInPolicyResponse

        The model defined in huaweicloud sdk

        :param idle_time: 空置时间
        :type idle_time: int
        :param threshold: 缩容阈值
        :type threshold: int
        :param delay_after_add: 扩容后多久再次判断缩容
        :type delay_after_add: int
        :param delay_after_delete: 节点删除后多久再次判断缩容
        :type delay_after_delete: int
        :param delay_after_failure: 缩容失败后多久再次判断缩容
        :type delay_after_failure: int
        :param max_nodes_batch_deletion: 缩容并发数
        :type max_nodes_batch_deletion: int
        :param check_interval: 检查间隔
        :type check_interval: int
        """
        
        super(ShowScaleInPolicyResponse, self).__init__()

        self._idle_time = None
        self._threshold = None
        self._delay_after_add = None
        self._delay_after_delete = None
        self._delay_after_failure = None
        self._max_nodes_batch_deletion = None
        self._check_interval = None
        self.discriminator = None

        if idle_time is not None:
            self.idle_time = idle_time
        if threshold is not None:
            self.threshold = threshold
        if delay_after_add is not None:
            self.delay_after_add = delay_after_add
        if delay_after_delete is not None:
            self.delay_after_delete = delay_after_delete
        if delay_after_failure is not None:
            self.delay_after_failure = delay_after_failure
        if max_nodes_batch_deletion is not None:
            self.max_nodes_batch_deletion = max_nodes_batch_deletion
        if check_interval is not None:
            self.check_interval = check_interval

    @property
    def idle_time(self):
        r"""Gets the idle_time of this ShowScaleInPolicyResponse.

        空置时间

        :return: The idle_time of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        r"""Sets the idle_time of this ShowScaleInPolicyResponse.

        空置时间

        :param idle_time: The idle_time of this ShowScaleInPolicyResponse.
        :type idle_time: int
        """
        self._idle_time = idle_time

    @property
    def threshold(self):
        r"""Gets the threshold of this ShowScaleInPolicyResponse.

        缩容阈值

        :return: The threshold of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ShowScaleInPolicyResponse.

        缩容阈值

        :param threshold: The threshold of this ShowScaleInPolicyResponse.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def delay_after_add(self):
        r"""Gets the delay_after_add of this ShowScaleInPolicyResponse.

        扩容后多久再次判断缩容

        :return: The delay_after_add of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._delay_after_add

    @delay_after_add.setter
    def delay_after_add(self, delay_after_add):
        r"""Sets the delay_after_add of this ShowScaleInPolicyResponse.

        扩容后多久再次判断缩容

        :param delay_after_add: The delay_after_add of this ShowScaleInPolicyResponse.
        :type delay_after_add: int
        """
        self._delay_after_add = delay_after_add

    @property
    def delay_after_delete(self):
        r"""Gets the delay_after_delete of this ShowScaleInPolicyResponse.

        节点删除后多久再次判断缩容

        :return: The delay_after_delete of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._delay_after_delete

    @delay_after_delete.setter
    def delay_after_delete(self, delay_after_delete):
        r"""Sets the delay_after_delete of this ShowScaleInPolicyResponse.

        节点删除后多久再次判断缩容

        :param delay_after_delete: The delay_after_delete of this ShowScaleInPolicyResponse.
        :type delay_after_delete: int
        """
        self._delay_after_delete = delay_after_delete

    @property
    def delay_after_failure(self):
        r"""Gets the delay_after_failure of this ShowScaleInPolicyResponse.

        缩容失败后多久再次判断缩容

        :return: The delay_after_failure of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._delay_after_failure

    @delay_after_failure.setter
    def delay_after_failure(self, delay_after_failure):
        r"""Sets the delay_after_failure of this ShowScaleInPolicyResponse.

        缩容失败后多久再次判断缩容

        :param delay_after_failure: The delay_after_failure of this ShowScaleInPolicyResponse.
        :type delay_after_failure: int
        """
        self._delay_after_failure = delay_after_failure

    @property
    def max_nodes_batch_deletion(self):
        r"""Gets the max_nodes_batch_deletion of this ShowScaleInPolicyResponse.

        缩容并发数

        :return: The max_nodes_batch_deletion of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._max_nodes_batch_deletion

    @max_nodes_batch_deletion.setter
    def max_nodes_batch_deletion(self, max_nodes_batch_deletion):
        r"""Sets the max_nodes_batch_deletion of this ShowScaleInPolicyResponse.

        缩容并发数

        :param max_nodes_batch_deletion: The max_nodes_batch_deletion of this ShowScaleInPolicyResponse.
        :type max_nodes_batch_deletion: int
        """
        self._max_nodes_batch_deletion = max_nodes_batch_deletion

    @property
    def check_interval(self):
        r"""Gets the check_interval of this ShowScaleInPolicyResponse.

        检查间隔

        :return: The check_interval of this ShowScaleInPolicyResponse.
        :rtype: int
        """
        return self._check_interval

    @check_interval.setter
    def check_interval(self, check_interval):
        r"""Sets the check_interval of this ShowScaleInPolicyResponse.

        检查间隔

        :param check_interval: The check_interval of this ShowScaleInPolicyResponse.
        :type check_interval: int
        """
        self._check_interval = check_interval

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
        if not isinstance(other, ShowScaleInPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
