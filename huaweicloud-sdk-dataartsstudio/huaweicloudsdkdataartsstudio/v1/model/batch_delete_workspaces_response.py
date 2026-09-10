# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteWorkspacesResponse(SdkResponse):

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
        'is_success': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'is_success': 'is_success'
    }

    def __init__(self, message=None, is_success=None):
        r"""BatchDeleteWorkspacesResponse

        The model defined in huaweicloud sdk

        :param message: 返回消息
        :type message: str
        :param is_success: 是否成功
        :type is_success: bool
        """
        
        super().__init__()

        self._message = None
        self._is_success = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if is_success is not None:
            self.is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this BatchDeleteWorkspacesResponse.

        返回消息

        :return: The message of this BatchDeleteWorkspacesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchDeleteWorkspacesResponse.

        返回消息

        :param message: The message of this BatchDeleteWorkspacesResponse.
        :type message: str
        """
        self._message = message

    @property
    def is_success(self):
        r"""Gets the is_success of this BatchDeleteWorkspacesResponse.

        是否成功

        :return: The is_success of this BatchDeleteWorkspacesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this BatchDeleteWorkspacesResponse.

        是否成功

        :param is_success: The is_success of this BatchDeleteWorkspacesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteWorkspacesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeleteWorkspacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
