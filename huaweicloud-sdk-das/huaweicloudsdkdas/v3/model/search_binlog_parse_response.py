# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchBinlogParseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'event_list': 'list[EventRowsVo]'
    }

    attribute_map = {
        'total': 'total',
        'event_list': 'event_list'
    }

    def __init__(self, total=None, event_list=None):
        r"""SearchBinlogParseResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param event_list: binlog详情信息列表
        :type event_list: list[:class:`huaweicloudsdkdas.v3.EventRowsVo`]
        """
        
        super().__init__()

        self._total = None
        self._event_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if event_list is not None:
            self.event_list = event_list

    @property
    def total(self):
        r"""Gets the total of this SearchBinlogParseResponse.

        总数

        :return: The total of this SearchBinlogParseResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchBinlogParseResponse.

        总数

        :param total: The total of this SearchBinlogParseResponse.
        :type total: int
        """
        self._total = total

    @property
    def event_list(self):
        r"""Gets the event_list of this SearchBinlogParseResponse.

        binlog详情信息列表

        :return: The event_list of this SearchBinlogParseResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.EventRowsVo`]
        """
        return self._event_list

    @event_list.setter
    def event_list(self, event_list):
        r"""Sets the event_list of this SearchBinlogParseResponse.

        binlog详情信息列表

        :param event_list: The event_list of this SearchBinlogParseResponse.
        :type event_list: list[:class:`huaweicloudsdkdas.v3.EventRowsVo`]
        """
        self._event_list = event_list

    def to_dict(self):
        import warnings
        warnings.warn("SearchBinlogParseResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchBinlogParseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
