# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckBackendConnectivityResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'check_result': 'str',
        'failures': 'list[str]'
    }

    attribute_map = {
        'check_result': 'check_result',
        'failures': 'failures'
    }

    def __init__(self, check_result=None, failures=None):
        """CheckBackendConnectivityResponse - a model defined in huaweicloud sdk"""
        
        super(CheckBackendConnectivityResponse, self).__init__()

        self._check_result = None
        self._failures = None
        self.discriminator = None

        if check_result is not None:
            self.check_result = check_result
        if failures is not None:
            self.failures = failures

    @property
    def check_result(self):
        """Gets the check_result of this CheckBackendConnectivityResponse.

        后端服务连通性检测结果  SUCCESS - 连通  FAILED - 不连通

        :return: The check_result of this CheckBackendConnectivityResponse.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this CheckBackendConnectivityResponse.

        后端服务连通性检测结果  SUCCESS - 连通  FAILED - 不连通

        :param check_result: The check_result of this CheckBackendConnectivityResponse.
        :type: str
        """
        self._check_result = check_result

    @property
    def failures(self):
        """Gets the failures of this CheckBackendConnectivityResponse.

        后端服务连通检测失败的列表

        :return: The failures of this CheckBackendConnectivityResponse.
        :rtype: list[str]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this CheckBackendConnectivityResponse.

        后端服务连通检测失败的列表

        :param failures: The failures of this CheckBackendConnectivityResponse.
        :type: list[str]
        """
        self._failures = failures

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
        if not isinstance(other, CheckBackendConnectivityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
