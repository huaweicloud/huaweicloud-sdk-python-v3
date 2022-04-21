# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidationLinkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, message=None, status=None):
        """ValidationLinkConfig

        The model defined in huaweicloud sdk

        :param message: 错误描述
        :type message: str
        :param status: ERROR,WARNING
        :type status: str
        """
        
        

        self._message = None
        self._status = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def message(self):
        """Gets the message of this ValidationLinkConfig.

        错误描述

        :return: The message of this ValidationLinkConfig.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationLinkConfig.

        错误描述

        :param message: The message of this ValidationLinkConfig.
        :type message: str
        """
        self._message = message

    @property
    def status(self):
        """Gets the status of this ValidationLinkConfig.

        ERROR,WARNING

        :return: The status of this ValidationLinkConfig.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ValidationLinkConfig.

        ERROR,WARNING

        :param status: The status of this ValidationLinkConfig.
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
        if not isinstance(other, ValidationLinkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
