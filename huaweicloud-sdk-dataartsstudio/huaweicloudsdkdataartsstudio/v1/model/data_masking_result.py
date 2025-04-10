# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataMaskingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'DiagnoseResult',
        'count': 'int'
    }

    attribute_map = {
        'result': 'result',
        'count': 'count'
    }

    def __init__(self, result=None, count=None):
        r"""DataMaskingResult

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        :param count: 没有配置脱敏任务的表数量
        :type count: int
        """
        
        

        self._result = None
        self._count = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if count is not None:
            self.count = count

    @property
    def result(self):
        r"""Gets the result of this DataMaskingResult.

        :return: The result of this DataMaskingResult.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DataMaskingResult.

        :param result: The result of this DataMaskingResult.
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        self._result = result

    @property
    def count(self):
        r"""Gets the count of this DataMaskingResult.

        没有配置脱敏任务的表数量

        :return: The count of this DataMaskingResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this DataMaskingResult.

        没有配置脱敏任务的表数量

        :param count: The count of this DataMaskingResult.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, DataMaskingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
