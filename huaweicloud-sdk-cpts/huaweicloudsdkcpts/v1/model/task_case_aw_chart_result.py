# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskCaseAwChartResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broken_list': 'BrokenList',
        'err_message': 'str',
        'resp_time_range': 'dict(str, str)'
    }

    attribute_map = {
        'broken_list': 'broken_list',
        'err_message': 'err_message',
        'resp_time_range': 'resp_time_range'
    }

    def __init__(self, broken_list=None, err_message=None, resp_time_range=None):
        """TaskCaseAwChartResult

        The model defined in huaweicloud sdk

        :param broken_list: 
        :type broken_list: :class:`huaweicloudsdkcpts.v1.BrokenList`
        :param err_message: 错误信息
        :type err_message: str
        :param resp_time_range: 响应时间区间与出现次数的汇总信息
        :type resp_time_range: dict(str, str)
        """
        
        

        self._broken_list = None
        self._err_message = None
        self._resp_time_range = None
        self.discriminator = None

        if broken_list is not None:
            self.broken_list = broken_list
        if err_message is not None:
            self.err_message = err_message
        if resp_time_range is not None:
            self.resp_time_range = resp_time_range

    @property
    def broken_list(self):
        """Gets the broken_list of this TaskCaseAwChartResult.

        :return: The broken_list of this TaskCaseAwChartResult.
        :rtype: :class:`huaweicloudsdkcpts.v1.BrokenList`
        """
        return self._broken_list

    @broken_list.setter
    def broken_list(self, broken_list):
        """Sets the broken_list of this TaskCaseAwChartResult.

        :param broken_list: The broken_list of this TaskCaseAwChartResult.
        :type broken_list: :class:`huaweicloudsdkcpts.v1.BrokenList`
        """
        self._broken_list = broken_list

    @property
    def err_message(self):
        """Gets the err_message of this TaskCaseAwChartResult.

        错误信息

        :return: The err_message of this TaskCaseAwChartResult.
        :rtype: str
        """
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        """Sets the err_message of this TaskCaseAwChartResult.

        错误信息

        :param err_message: The err_message of this TaskCaseAwChartResult.
        :type err_message: str
        """
        self._err_message = err_message

    @property
    def resp_time_range(self):
        """Gets the resp_time_range of this TaskCaseAwChartResult.

        响应时间区间与出现次数的汇总信息

        :return: The resp_time_range of this TaskCaseAwChartResult.
        :rtype: dict(str, str)
        """
        return self._resp_time_range

    @resp_time_range.setter
    def resp_time_range(self, resp_time_range):
        """Sets the resp_time_range of this TaskCaseAwChartResult.

        响应时间区间与出现次数的汇总信息

        :param resp_time_range: The resp_time_range of this TaskCaseAwChartResult.
        :type resp_time_range: dict(str, str)
        """
        self._resp_time_range = resp_time_range

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
        if not isinstance(other, TaskCaseAwChartResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
