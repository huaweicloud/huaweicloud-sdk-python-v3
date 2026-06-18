# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupResourcePermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, status=None, message=None):
        r"""UpdateGroupResourcePermissionsResponse

        The model defined in huaweicloud sdk

        :param status: 返回状态码
        :type status: int
        :param message: 返回信息
        :type message: str
        """
        
        super().__init__()

        self._status = None
        self._message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def status(self):
        r"""Gets the status of this UpdateGroupResourcePermissionsResponse.

        返回状态码

        :return: The status of this UpdateGroupResourcePermissionsResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateGroupResourcePermissionsResponse.

        返回状态码

        :param status: The status of this UpdateGroupResourcePermissionsResponse.
        :type status: int
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this UpdateGroupResourcePermissionsResponse.

        返回信息

        :return: The message of this UpdateGroupResourcePermissionsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this UpdateGroupResourcePermissionsResponse.

        返回信息

        :param message: The message of this UpdateGroupResourcePermissionsResponse.
        :type message: str
        """
        self._message = message

    def to_dict(self):
        import warnings
        warnings.warn("UpdateGroupResourcePermissionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateGroupResourcePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
