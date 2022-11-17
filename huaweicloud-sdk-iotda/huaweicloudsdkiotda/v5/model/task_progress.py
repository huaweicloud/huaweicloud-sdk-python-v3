# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'processing': 'int',
        'success': 'int',
        'fail': 'int',
        'waitting': 'int',
        'fail_wait_retry': 'int',
        'stopped': 'int'
    }

    attribute_map = {
        'total': 'total',
        'processing': 'processing',
        'success': 'success',
        'fail': 'fail',
        'waitting': 'waitting',
        'fail_wait_retry': 'fail_wait_retry',
        'stopped': 'stopped'
    }

    def __init__(self, total=None, processing=None, success=None, fail=None, waitting=None, fail_wait_retry=None, stopped=None):
        """TaskProgress

        The model defined in huaweicloud sdk

        :param total: 子任务总个数。
        :type total: int
        :param processing: 正在执行的子任务个数。
        :type processing: int
        :param success: 执行成功的子任务个数。
        :type success: int
        :param fail: 执行失败的的子任务个数。
        :type fail: int
        :param waitting: 等待执行的子任务个数。
        :type waitting: int
        :param fail_wait_retry: 失败等待重试的子任务个数。
        :type fail_wait_retry: int
        :param stopped: 停止的子任务个数。
        :type stopped: int
        """
        
        

        self._total = None
        self._processing = None
        self._success = None
        self._fail = None
        self._waitting = None
        self._fail_wait_retry = None
        self._stopped = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if processing is not None:
            self.processing = processing
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail
        if waitting is not None:
            self.waitting = waitting
        if fail_wait_retry is not None:
            self.fail_wait_retry = fail_wait_retry
        if stopped is not None:
            self.stopped = stopped

    @property
    def total(self):
        """Gets the total of this TaskProgress.

        子任务总个数。

        :return: The total of this TaskProgress.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TaskProgress.

        子任务总个数。

        :param total: The total of this TaskProgress.
        :type total: int
        """
        self._total = total

    @property
    def processing(self):
        """Gets the processing of this TaskProgress.

        正在执行的子任务个数。

        :return: The processing of this TaskProgress.
        :rtype: int
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """Sets the processing of this TaskProgress.

        正在执行的子任务个数。

        :param processing: The processing of this TaskProgress.
        :type processing: int
        """
        self._processing = processing

    @property
    def success(self):
        """Gets the success of this TaskProgress.

        执行成功的子任务个数。

        :return: The success of this TaskProgress.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TaskProgress.

        执行成功的子任务个数。

        :param success: The success of this TaskProgress.
        :type success: int
        """
        self._success = success

    @property
    def fail(self):
        """Gets the fail of this TaskProgress.

        执行失败的的子任务个数。

        :return: The fail of this TaskProgress.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this TaskProgress.

        执行失败的的子任务个数。

        :param fail: The fail of this TaskProgress.
        :type fail: int
        """
        self._fail = fail

    @property
    def waitting(self):
        """Gets the waitting of this TaskProgress.

        等待执行的子任务个数。

        :return: The waitting of this TaskProgress.
        :rtype: int
        """
        return self._waitting

    @waitting.setter
    def waitting(self, waitting):
        """Sets the waitting of this TaskProgress.

        等待执行的子任务个数。

        :param waitting: The waitting of this TaskProgress.
        :type waitting: int
        """
        self._waitting = waitting

    @property
    def fail_wait_retry(self):
        """Gets the fail_wait_retry of this TaskProgress.

        失败等待重试的子任务个数。

        :return: The fail_wait_retry of this TaskProgress.
        :rtype: int
        """
        return self._fail_wait_retry

    @fail_wait_retry.setter
    def fail_wait_retry(self, fail_wait_retry):
        """Sets the fail_wait_retry of this TaskProgress.

        失败等待重试的子任务个数。

        :param fail_wait_retry: The fail_wait_retry of this TaskProgress.
        :type fail_wait_retry: int
        """
        self._fail_wait_retry = fail_wait_retry

    @property
    def stopped(self):
        """Gets the stopped of this TaskProgress.

        停止的子任务个数。

        :return: The stopped of this TaskProgress.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        """Sets the stopped of this TaskProgress.

        停止的子任务个数。

        :param stopped: The stopped of this TaskProgress.
        :type stopped: int
        """
        self._stopped = stopped

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
        if not isinstance(other, TaskProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
