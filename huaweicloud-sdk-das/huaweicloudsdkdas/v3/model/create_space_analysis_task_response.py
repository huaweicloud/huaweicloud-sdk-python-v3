# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSpaceAnalysisTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_time': 'int'
    }

    attribute_map = {
        'execution_time': 'execution_time'
    }

    def __init__(self, execution_time=None):
        """CreateSpaceAnalysisTaskResponse

        The model defined in huaweicloud sdk

        :param execution_time: 执行时间，毫秒为单位的时间戳
        :type execution_time: int
        """
        
        super(CreateSpaceAnalysisTaskResponse, self).__init__()

        self._execution_time = None
        self.discriminator = None

        if execution_time is not None:
            self.execution_time = execution_time

    @property
    def execution_time(self):
        """Gets the execution_time of this CreateSpaceAnalysisTaskResponse.

        执行时间，毫秒为单位的时间戳

        :return: The execution_time of this CreateSpaceAnalysisTaskResponse.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this CreateSpaceAnalysisTaskResponse.

        执行时间，毫秒为单位的时间戳

        :param execution_time: The execution_time of this CreateSpaceAnalysisTaskResponse.
        :type execution_time: int
        """
        self._execution_time = execution_time

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
        if not isinstance(other, CreateSpaceAnalysisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
