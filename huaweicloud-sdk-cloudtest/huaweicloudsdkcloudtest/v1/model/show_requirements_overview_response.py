# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRequirementsOverviewResponse(SdkResponse):

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
        'result': 'ResultValueRequirementsOverviewVo',
        'error': 'ApiError'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, status=None, result=None, error=None):
        """ShowRequirementsOverviewResponse

        The model defined in huaweicloud sdk

        :param status: success|error;
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueRequirementsOverviewVo`
        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        
        super(ShowRequirementsOverviewResponse, self).__init__()

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
        """Gets the status of this ShowRequirementsOverviewResponse.

        success|error;

        :return: The status of this ShowRequirementsOverviewResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowRequirementsOverviewResponse.

        success|error;

        :param status: The status of this ShowRequirementsOverviewResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this ShowRequirementsOverviewResponse.

        :return: The result of this ShowRequirementsOverviewResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ResultValueRequirementsOverviewVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowRequirementsOverviewResponse.

        :param result: The result of this ShowRequirementsOverviewResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueRequirementsOverviewVo`
        """
        self._result = result

    @property
    def error(self):
        """Gets the error of this ShowRequirementsOverviewResponse.

        :return: The error of this ShowRequirementsOverviewResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ShowRequirementsOverviewResponse.

        :param error: The error of this ShowRequirementsOverviewResponse.
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
        if not isinstance(other, ShowRequirementsOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
