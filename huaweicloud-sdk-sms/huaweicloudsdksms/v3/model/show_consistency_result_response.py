# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsistencyResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consistency_result': 'list[ConsistencyResult]',
        'finished_time': 'int'
    }

    attribute_map = {
        'consistency_result': 'consistency_result',
        'finished_time': 'finished_time'
    }

    def __init__(self, consistency_result=None, finished_time=None):
        """ShowConsistencyResultResponse

        The model defined in huaweicloud sdk

        :param consistency_result: 校验结果
        :type consistency_result: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        :param finished_time: 检验完成时间
        :type finished_time: int
        """
        
        super(ShowConsistencyResultResponse, self).__init__()

        self._consistency_result = None
        self._finished_time = None
        self.discriminator = None

        if consistency_result is not None:
            self.consistency_result = consistency_result
        if finished_time is not None:
            self.finished_time = finished_time

    @property
    def consistency_result(self):
        """Gets the consistency_result of this ShowConsistencyResultResponse.

        校验结果

        :return: The consistency_result of this ShowConsistencyResultResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        return self._consistency_result

    @consistency_result.setter
    def consistency_result(self, consistency_result):
        """Sets the consistency_result of this ShowConsistencyResultResponse.

        校验结果

        :param consistency_result: The consistency_result of this ShowConsistencyResultResponse.
        :type consistency_result: list[:class:`huaweicloudsdksms.v3.ConsistencyResult`]
        """
        self._consistency_result = consistency_result

    @property
    def finished_time(self):
        """Gets the finished_time of this ShowConsistencyResultResponse.

        检验完成时间

        :return: The finished_time of this ShowConsistencyResultResponse.
        :rtype: int
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        """Sets the finished_time of this ShowConsistencyResultResponse.

        检验完成时间

        :param finished_time: The finished_time of this ShowConsistencyResultResponse.
        :type finished_time: int
        """
        self._finished_time = finished_time

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
        if not isinstance(other, ShowConsistencyResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
