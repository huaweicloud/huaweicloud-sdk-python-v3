# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreRecyclingJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error': 'str',
        'status': 'str'
    }

    attribute_map = {
        'error': 'error',
        'status': 'status'
    }

    def __init__(self, error=None, status=None):
        r"""RestoreRecyclingJobsResponse

        The model defined in huaweicloud sdk

        :param error: 返回错误信息
        :type error: str
        :param status: 返回状态信息
        :type status: str
        """
        
        super(RestoreRecyclingJobsResponse, self).__init__()

        self._error = None
        self._status = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if status is not None:
            self.status = status

    @property
    def error(self):
        r"""Gets the error of this RestoreRecyclingJobsResponse.

        返回错误信息

        :return: The error of this RestoreRecyclingJobsResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this RestoreRecyclingJobsResponse.

        返回错误信息

        :param error: The error of this RestoreRecyclingJobsResponse.
        :type error: str
        """
        self._error = error

    @property
    def status(self):
        r"""Gets the status of this RestoreRecyclingJobsResponse.

        返回状态信息

        :return: The status of this RestoreRecyclingJobsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RestoreRecyclingJobsResponse.

        返回状态信息

        :param status: The status of this RestoreRecyclingJobsResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RestoreRecyclingJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
