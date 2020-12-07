# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateMessageTemplateResponse(SdkResponse):


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
        'message_template_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'message_template_id': 'message_template_id'
    }

    def __init__(self, request_id=None, message_template_id=None):
        """CreateMessageTemplateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._message_template_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if message_template_id is not None:
            self.message_template_id = message_template_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateMessageTemplateResponse.

        请求的唯一标识ID。

        :return: The request_id of this CreateMessageTemplateResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateMessageTemplateResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this CreateMessageTemplateResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def message_template_id(self):
        """Gets the message_template_id of this CreateMessageTemplateResponse.

        模板唯一的资源标识。

        :return: The message_template_id of this CreateMessageTemplateResponse.
        :rtype: str
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this CreateMessageTemplateResponse.

        模板唯一的资源标识。

        :param message_template_id: The message_template_id of this CreateMessageTemplateResponse.
        :type: str
        """
        self._message_template_id = message_template_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMessageTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
