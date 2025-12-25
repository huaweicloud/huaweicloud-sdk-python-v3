# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRetrieveScriptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'delete_time': 'int'
    }

    attribute_map = {
        'script_id': 'script_id',
        'delete_time': 'delete_time'
    }

    def __init__(self, script_id=None, delete_time=None):
        r"""DeleteRetrieveScriptResponse

        The model defined in huaweicloud sdk

        :param script_id: UUID
        :type script_id: str
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        super().__init__()

        self._script_id = None
        self._delete_time = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def script_id(self):
        r"""Gets the script_id of this DeleteRetrieveScriptResponse.

        UUID

        :return: The script_id of this DeleteRetrieveScriptResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this DeleteRetrieveScriptResponse.

        UUID

        :param script_id: The script_id of this DeleteRetrieveScriptResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def delete_time(self):
        r"""Gets the delete_time of this DeleteRetrieveScriptResponse.

        毫秒时间戳

        :return: The delete_time of this DeleteRetrieveScriptResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this DeleteRetrieveScriptResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this DeleteRetrieveScriptResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("DeleteRetrieveScriptResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteRetrieveScriptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
