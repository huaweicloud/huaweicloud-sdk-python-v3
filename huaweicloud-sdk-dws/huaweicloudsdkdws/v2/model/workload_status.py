# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_switch': 'str',
        'max_concurrency_num': 'str'
    }

    attribute_map = {
        'workload_switch': 'workload_switch',
        'max_concurrency_num': 'max_concurrency_num'
    }

    def __init__(self, workload_switch=None, max_concurrency_num=None):
        """WorkloadStatus

        The model defined in huaweicloud sdk

        :param workload_switch: 开关。
        :type workload_switch: str
        :param max_concurrency_num: 最大并发数。
        :type max_concurrency_num: str
        """
        
        

        self._workload_switch = None
        self._max_concurrency_num = None
        self.discriminator = None

        self.workload_switch = workload_switch
        if max_concurrency_num is not None:
            self.max_concurrency_num = max_concurrency_num

    @property
    def workload_switch(self):
        """Gets the workload_switch of this WorkloadStatus.

        开关。

        :return: The workload_switch of this WorkloadStatus.
        :rtype: str
        """
        return self._workload_switch

    @workload_switch.setter
    def workload_switch(self, workload_switch):
        """Sets the workload_switch of this WorkloadStatus.

        开关。

        :param workload_switch: The workload_switch of this WorkloadStatus.
        :type workload_switch: str
        """
        self._workload_switch = workload_switch

    @property
    def max_concurrency_num(self):
        """Gets the max_concurrency_num of this WorkloadStatus.

        最大并发数。

        :return: The max_concurrency_num of this WorkloadStatus.
        :rtype: str
        """
        return self._max_concurrency_num

    @max_concurrency_num.setter
    def max_concurrency_num(self, max_concurrency_num):
        """Sets the max_concurrency_num of this WorkloadStatus.

        最大并发数。

        :param max_concurrency_num: The max_concurrency_num of this WorkloadStatus.
        :type max_concurrency_num: str
        """
        self._max_concurrency_num = max_concurrency_num

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
        if not isinstance(other, WorkloadStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
