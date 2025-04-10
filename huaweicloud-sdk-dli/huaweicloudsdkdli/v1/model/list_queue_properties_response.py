# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueuePropertiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'properties': 'list[QueueProperty]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'properties': 'properties'
    }

    def __init__(self, is_success=None, message=None, properties=None):
        r"""ListQueuePropertiesResponse

        The model defined in huaweicloud sdk

        :param is_success: 
        :type is_success: bool
        :param message: 
        :type message: str
        :param properties: 
        :type properties: list[:class:`huaweicloudsdkdli.v1.QueueProperty`]
        """
        
        super(ListQueuePropertiesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._properties = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if properties is not None:
            self.properties = properties

    @property
    def is_success(self):
        r"""Gets the is_success of this ListQueuePropertiesResponse.

        :return: The is_success of this ListQueuePropertiesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListQueuePropertiesResponse.

        :param is_success: The is_success of this ListQueuePropertiesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListQueuePropertiesResponse.

        :return: The message of this ListQueuePropertiesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListQueuePropertiesResponse.

        :param message: The message of this ListQueuePropertiesResponse.
        :type message: str
        """
        self._message = message

    @property
    def properties(self):
        r"""Gets the properties of this ListQueuePropertiesResponse.

        :return: The properties of this ListQueuePropertiesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.QueueProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ListQueuePropertiesResponse.

        :param properties: The properties of this ListQueuePropertiesResponse.
        :type properties: list[:class:`huaweicloudsdkdli.v1.QueueProperty`]
        """
        self._properties = properties

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
        if not isinstance(other, ListQueuePropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
