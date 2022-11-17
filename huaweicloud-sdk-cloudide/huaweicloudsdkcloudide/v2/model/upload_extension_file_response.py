# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadExtensionFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error': 'Error',
        'result': 'object',
        'status': 'str'
    }

    attribute_map = {
        'error': 'error',
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, error=None, result=None, status=None):
        """UploadExtensionFileResponse

        The model defined in huaweicloud sdk

        :param error: 
        :type error: :class:`huaweicloudsdkcloudide.v2.Error`
        :param result: 结果
        :type result: object
        :param status: 状态
        :type status: str
        """
        
        super(UploadExtensionFileResponse, self).__init__()

        self._error = None
        self._result = None
        self._status = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def error(self):
        """Gets the error of this UploadExtensionFileResponse.

        :return: The error of this UploadExtensionFileResponse.
        :rtype: :class:`huaweicloudsdkcloudide.v2.Error`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this UploadExtensionFileResponse.

        :param error: The error of this UploadExtensionFileResponse.
        :type error: :class:`huaweicloudsdkcloudide.v2.Error`
        """
        self._error = error

    @property
    def result(self):
        """Gets the result of this UploadExtensionFileResponse.

        结果

        :return: The result of this UploadExtensionFileResponse.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UploadExtensionFileResponse.

        结果

        :param result: The result of this UploadExtensionFileResponse.
        :type result: object
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this UploadExtensionFileResponse.

        状态

        :return: The status of this UploadExtensionFileResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UploadExtensionFileResponse.

        状态

        :param status: The status of this UploadExtensionFileResponse.
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
        if not isinstance(other, UploadExtensionFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
