# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpdateJobHistoryResponse(SdkResponse):

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
        'error': 'object',
        'result': 'JobUpdateRecordListVoResult'
    }

    attribute_map = {
        'status': 'status',
        'error': 'error',
        'result': 'result'
    }

    def __init__(self, status=None, error=None, result=None):
        r"""ListUpdateJobHistoryResponse

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: str
        :param error: 错误
        :type error: object
        :param result: 
        :type result: :class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResult`
        """
        
        super(ListUpdateJobHistoryResponse, self).__init__()

        self._status = None
        self._error = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this ListUpdateJobHistoryResponse.

        状态

        :return: The status of this ListUpdateJobHistoryResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListUpdateJobHistoryResponse.

        状态

        :param status: The status of this ListUpdateJobHistoryResponse.
        :type status: str
        """
        self._status = status

    @property
    def error(self):
        r"""Gets the error of this ListUpdateJobHistoryResponse.

        错误

        :return: The error of this ListUpdateJobHistoryResponse.
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListUpdateJobHistoryResponse.

        错误

        :param error: The error of this ListUpdateJobHistoryResponse.
        :type error: object
        """
        self._error = error

    @property
    def result(self):
        r"""Gets the result of this ListUpdateJobHistoryResponse.

        :return: The result of this ListUpdateJobHistoryResponse.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListUpdateJobHistoryResponse.

        :param result: The result of this ListUpdateJobHistoryResponse.
        :type result: :class:`huaweicloudsdkcodeartsbuild.v3.JobUpdateRecordListVoResult`
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
        if not isinstance(other, ListUpdateJobHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
