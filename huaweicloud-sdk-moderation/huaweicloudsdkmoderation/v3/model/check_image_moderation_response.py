# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckImageModerationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'result': 'ImageDetectionResult'
    }

    attribute_map = {
        'request_id': 'request_id',
        'result': 'result'
    }

    def __init__(self, request_id=None, result=None):
        """CheckImageModerationResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的唯⼀标识，⽤于问题排查，建议保存。
        :type request_id: str
        :param result: 
        :type result: :class:`huaweicloudsdkmoderation.v3.ImageDetectionResult`
        """
        
        super(CheckImageModerationResponse, self).__init__()

        self._request_id = None
        self._result = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if result is not None:
            self.result = result

    @property
    def request_id(self):
        """Gets the request_id of this CheckImageModerationResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :return: The request_id of this CheckImageModerationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CheckImageModerationResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :param request_id: The request_id of this CheckImageModerationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def result(self):
        """Gets the result of this CheckImageModerationResponse.

        :return: The result of this CheckImageModerationResponse.
        :rtype: :class:`huaweicloudsdkmoderation.v3.ImageDetectionResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CheckImageModerationResponse.

        :param result: The result of this CheckImageModerationResponse.
        :type result: :class:`huaweicloudsdkmoderation.v3.ImageDetectionResult`
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
        if not isinstance(other, CheckImageModerationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
