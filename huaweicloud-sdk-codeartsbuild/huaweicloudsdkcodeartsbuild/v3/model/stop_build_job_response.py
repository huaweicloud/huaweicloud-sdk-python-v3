# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopBuildJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'result': 'str'
    }

    attribute_map = {
        'success': 'success',
        'result': 'result'
    }

    def __init__(self, success=None, result=None):
        """StopBuildJobResponse

        The model defined in huaweicloud sdk

        :param success: 是否停止成功
        :type success: bool
        :param result: 返回结果
        :type result: str
        """
        
        super(StopBuildJobResponse, self).__init__()

        self._success = None
        self._result = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if result is not None:
            self.result = result

    @property
    def success(self):
        """Gets the success of this StopBuildJobResponse.

        是否停止成功

        :return: The success of this StopBuildJobResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this StopBuildJobResponse.

        是否停止成功

        :param success: The success of this StopBuildJobResponse.
        :type success: bool
        """
        self._success = success

    @property
    def result(self):
        """Gets the result of this StopBuildJobResponse.

        返回结果

        :return: The result of this StopBuildJobResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StopBuildJobResponse.

        返回结果

        :param result: The result of this StopBuildJobResponse.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, StopBuildJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
