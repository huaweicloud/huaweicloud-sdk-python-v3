# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogStreamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_streams': 'list[LogStreamResBody]'
    }

    attribute_map = {
        'log_streams': 'log_streams'
    }

    def __init__(self, log_streams=None):
        r"""ListLogStreamResponse

        The model defined in huaweicloud sdk

        :param log_streams: 
        :type log_streams: list[:class:`huaweicloudsdklts.v2.LogStreamResBody`]
        """
        
        super().__init__()

        self._log_streams = None
        self.discriminator = None

        if log_streams is not None:
            self.log_streams = log_streams

    @property
    def log_streams(self):
        r"""Gets the log_streams of this ListLogStreamResponse.

        :return: The log_streams of this ListLogStreamResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.LogStreamResBody`]
        """
        return self._log_streams

    @log_streams.setter
    def log_streams(self, log_streams):
        r"""Sets the log_streams of this ListLogStreamResponse.

        :param log_streams: The log_streams of this ListLogStreamResponse.
        :type log_streams: list[:class:`huaweicloudsdklts.v2.LogStreamResBody`]
        """
        self._log_streams = log_streams

    def to_dict(self):
        import warnings
        warnings.warn("ListLogStreamResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListLogStreamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
