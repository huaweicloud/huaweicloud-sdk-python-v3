# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thread_num': 'int',
        'batch_window': 'BatchWindow'
    }

    attribute_map = {
        'thread_num': 'thread_num',
        'batch_window': 'batch_window'
    }

    def __init__(self, thread_num=None, batch_window=None):
        r"""RunOption

        The model defined in huaweicloud sdk

        :param thread_num: 并发数
        :type thread_num: int
        :param batch_window: 
        :type batch_window: :class:`huaweicloudsdkeg.v1.BatchWindow`
        """
        
        

        self._thread_num = None
        self._batch_window = None
        self.discriminator = None

        if thread_num is not None:
            self.thread_num = thread_num
        if batch_window is not None:
            self.batch_window = batch_window

    @property
    def thread_num(self):
        r"""Gets the thread_num of this RunOption.

        并发数

        :return: The thread_num of this RunOption.
        :rtype: int
        """
        return self._thread_num

    @thread_num.setter
    def thread_num(self, thread_num):
        r"""Sets the thread_num of this RunOption.

        并发数

        :param thread_num: The thread_num of this RunOption.
        :type thread_num: int
        """
        self._thread_num = thread_num

    @property
    def batch_window(self):
        r"""Gets the batch_window of this RunOption.

        :return: The batch_window of this RunOption.
        :rtype: :class:`huaweicloudsdkeg.v1.BatchWindow`
        """
        return self._batch_window

    @batch_window.setter
    def batch_window(self, batch_window):
        r"""Sets the batch_window of this RunOption.

        :param batch_window: The batch_window of this RunOption.
        :type batch_window: :class:`huaweicloudsdkeg.v1.BatchWindow`
        """
        self._batch_window = batch_window

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
        if not isinstance(other, RunOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
