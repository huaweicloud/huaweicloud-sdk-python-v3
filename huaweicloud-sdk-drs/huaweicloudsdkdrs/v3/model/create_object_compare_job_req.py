# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateObjectCompareJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_task_num': 'int'
    }

    attribute_map = {
        'compare_task_num': 'compare_task_num'
    }

    def __init__(self, compare_task_num=None):
        """CreateObjectCompareJobReq

        The model defined in huaweicloud sdk

        :param compare_task_num: 对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。
        :type compare_task_num: int
        """
        
        

        self._compare_task_num = None
        self.discriminator = None

        if compare_task_num is not None:
            self.compare_task_num = compare_task_num

    @property
    def compare_task_num(self):
        """Gets the compare_task_num of this CreateObjectCompareJobReq.

        对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。

        :return: The compare_task_num of this CreateObjectCompareJobReq.
        :rtype: int
        """
        return self._compare_task_num

    @compare_task_num.setter
    def compare_task_num(self, compare_task_num):
        """Sets the compare_task_num of this CreateObjectCompareJobReq.

        对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。

        :param compare_task_num: The compare_task_num of this CreateObjectCompareJobReq.
        :type compare_task_num: int
        """
        self._compare_task_num = compare_task_num

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
        if not isinstance(other, CreateObjectCompareJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
