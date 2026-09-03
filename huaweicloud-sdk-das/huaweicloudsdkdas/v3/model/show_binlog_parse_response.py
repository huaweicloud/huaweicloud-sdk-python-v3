# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBinlogParseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_list': 'list[EventEventsDto]'
    }

    attribute_map = {
        'event_list': 'event_list'
    }

    def __init__(self, event_list=None):
        r"""ShowBinlogParseResponse

        The model defined in huaweicloud sdk

        :param event_list: binlog事件概览信息
        :type event_list: list[:class:`huaweicloudsdkdas.v3.EventEventsDto`]
        """
        
        super().__init__()

        self._event_list = None
        self.discriminator = None

        if event_list is not None:
            self.event_list = event_list

    @property
    def event_list(self):
        r"""Gets the event_list of this ShowBinlogParseResponse.

        binlog事件概览信息

        :return: The event_list of this ShowBinlogParseResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.EventEventsDto`]
        """
        return self._event_list

    @event_list.setter
    def event_list(self, event_list):
        r"""Sets the event_list of this ShowBinlogParseResponse.

        binlog事件概览信息

        :param event_list: The event_list of this ShowBinlogParseResponse.
        :type event_list: list[:class:`huaweicloudsdkdas.v3.EventEventsDto`]
        """
        self._event_list = event_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowBinlogParseResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBinlogParseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
