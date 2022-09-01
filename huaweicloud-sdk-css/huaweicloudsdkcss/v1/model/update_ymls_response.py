# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'acknowledged': 'bool',
        'external_message': 'str',
        'http_error_response': 'str'
    }

    attribute_map = {
        'acknowledged': 'acknowledged',
        'external_message': 'externalMessage',
        'http_error_response': 'httpErrorResponse'
    }

    def __init__(self, acknowledged=None, external_message=None, http_error_response=None):
        """UpdateYmlsResponse

        The model defined in huaweicloud sdk

        :param acknowledged: 修改是否成功。 - true: 修改成功。 - false: 修改失败。
        :type acknowledged: bool
        :param external_message: 错误信息描述。当acknowledged为true时，该字段返回null。
        :type external_message: str
        :param http_error_response: HTTP错误信息。默认为null。
        :type http_error_response: str
        """
        
        super(UpdateYmlsResponse, self).__init__()

        self._acknowledged = None
        self._external_message = None
        self._http_error_response = None
        self.discriminator = None

        if acknowledged is not None:
            self.acknowledged = acknowledged
        if external_message is not None:
            self.external_message = external_message
        if http_error_response is not None:
            self.http_error_response = http_error_response

    @property
    def acknowledged(self):
        """Gets the acknowledged of this UpdateYmlsResponse.

        修改是否成功。 - true: 修改成功。 - false: 修改失败。

        :return: The acknowledged of this UpdateYmlsResponse.
        :rtype: bool
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """Sets the acknowledged of this UpdateYmlsResponse.

        修改是否成功。 - true: 修改成功。 - false: 修改失败。

        :param acknowledged: The acknowledged of this UpdateYmlsResponse.
        :type acknowledged: bool
        """
        self._acknowledged = acknowledged

    @property
    def external_message(self):
        """Gets the external_message of this UpdateYmlsResponse.

        错误信息描述。当acknowledged为true时，该字段返回null。

        :return: The external_message of this UpdateYmlsResponse.
        :rtype: str
        """
        return self._external_message

    @external_message.setter
    def external_message(self, external_message):
        """Sets the external_message of this UpdateYmlsResponse.

        错误信息描述。当acknowledged为true时，该字段返回null。

        :param external_message: The external_message of this UpdateYmlsResponse.
        :type external_message: str
        """
        self._external_message = external_message

    @property
    def http_error_response(self):
        """Gets the http_error_response of this UpdateYmlsResponse.

        HTTP错误信息。默认为null。

        :return: The http_error_response of this UpdateYmlsResponse.
        :rtype: str
        """
        return self._http_error_response

    @http_error_response.setter
    def http_error_response(self, http_error_response):
        """Sets the http_error_response of this UpdateYmlsResponse.

        HTTP错误信息。默认为null。

        :param http_error_response: The http_error_response of this UpdateYmlsResponse.
        :type http_error_response: str
        """
        self._http_error_response = http_error_response

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
        if not isinstance(other, UpdateYmlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
