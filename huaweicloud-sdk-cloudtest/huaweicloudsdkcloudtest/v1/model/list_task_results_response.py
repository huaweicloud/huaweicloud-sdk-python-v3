# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'result': 'ResultValueListTaskResultVo',
        'error': 'ApiError'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, status=None, result=None, error=None):
        r"""ListTaskResultsResponse

        The model defined in huaweicloud sdk

        :param status: success|error
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueListTaskResultVo`
        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        
        super(ListTaskResultsResponse, self).__init__()

        self._status = None
        self._result = None
        self._error = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error

    @property
    def status(self):
        r"""Gets the status of this ListTaskResultsResponse.

        success|error

        :return: The status of this ListTaskResultsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTaskResultsResponse.

        success|error

        :param status: The status of this ListTaskResultsResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        r"""Gets the result of this ListTaskResultsResponse.

        :return: The result of this ListTaskResultsResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ResultValueListTaskResultVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListTaskResultsResponse.

        :param result: The result of this ListTaskResultsResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueListTaskResultVo`
        """
        self._result = result

    @property
    def error(self):
        r"""Gets the error of this ListTaskResultsResponse.

        :return: The error of this ListTaskResultsResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListTaskResultsResponse.

        :param error: The error of this ListTaskResultsResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        self._error = error

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
        if not isinstance(other, ListTaskResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
