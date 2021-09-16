# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryRunInfoResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'log_list': 'list[object]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'log_list': 'log_list'
    }

    def __init__(self, code=None, message=None, log_list=None):
        """ShowHistoryRunInfoResponse - a model defined in huaweicloud sdk"""
        
        super(ShowHistoryRunInfoResponse, self).__init__()

        self._code = None
        self._message = None
        self._log_list = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if log_list is not None:
            self.log_list = log_list

    @property
    def code(self):
        """Gets the code of this ShowHistoryRunInfoResponse.

        code

        :return: The code of this ShowHistoryRunInfoResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowHistoryRunInfoResponse.

        code

        :param code: The code of this ShowHistoryRunInfoResponse.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowHistoryRunInfoResponse.

        message

        :return: The message of this ShowHistoryRunInfoResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowHistoryRunInfoResponse.

        message

        :param message: The message of this ShowHistoryRunInfoResponse.
        :type: str
        """
        self._message = message

    @property
    def log_list(self):
        """Gets the log_list of this ShowHistoryRunInfoResponse.

        log_list

        :return: The log_list of this ShowHistoryRunInfoResponse.
        :rtype: list[object]
        """
        return self._log_list

    @log_list.setter
    def log_list(self, log_list):
        """Sets the log_list of this ShowHistoryRunInfoResponse.

        log_list

        :param log_list: The log_list of this ShowHistoryRunInfoResponse.
        :type: list[object]
        """
        self._log_list = log_list

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
        if not isinstance(other, ShowHistoryRunInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other