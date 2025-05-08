# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition': 'int',
        'result': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'partition': 'partition',
        'result': 'result',
        'error_code': 'error_code'
    }

    def __init__(self, partition=None, result=None, error_code=None):
        r"""PartitionResp

        The model defined in huaweicloud sdk

        :param partition: 分区
        :type partition: int
        :param result: 返回结果
        :type result: str
        :param error_code: 返回错误码
        :type error_code: str
        """
        
        

        self._partition = None
        self._result = None
        self._error_code = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if result is not None:
            self.result = result
        if error_code is not None:
            self.error_code = error_code

    @property
    def partition(self):
        r"""Gets the partition of this PartitionResp.

        分区

        :return: The partition of this PartitionResp.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this PartitionResp.

        分区

        :param partition: The partition of this PartitionResp.
        :type partition: int
        """
        self._partition = partition

    @property
    def result(self):
        r"""Gets the result of this PartitionResp.

        返回结果

        :return: The result of this PartitionResp.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this PartitionResp.

        返回结果

        :param result: The result of this PartitionResp.
        :type result: str
        """
        self._result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this PartitionResp.

        返回错误码

        :return: The error_code of this PartitionResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this PartitionResp.

        返回错误码

        :param error_code: The error_code of this PartitionResp.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, PartitionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
