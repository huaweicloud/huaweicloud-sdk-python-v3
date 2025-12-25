# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCollectorParserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parser_ids': 'list[ExportParserResponseDto]'
    }

    attribute_map = {
        'parser_ids': 'parser_ids'
    }

    def __init__(self, parser_ids=None):
        r"""ExportCollectorParserResponse

        The model defined in huaweicloud sdk

        :param parser_ids: 相关描述信息
        :type parser_ids: list[:class:`huaweicloudsdksecmaster.v1.ExportParserResponseDto`]
        """
        
        super().__init__()

        self._parser_ids = None
        self.discriminator = None

        if parser_ids is not None:
            self.parser_ids = parser_ids

    @property
    def parser_ids(self):
        r"""Gets the parser_ids of this ExportCollectorParserResponse.

        相关描述信息

        :return: The parser_ids of this ExportCollectorParserResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ExportParserResponseDto`]
        """
        return self._parser_ids

    @parser_ids.setter
    def parser_ids(self, parser_ids):
        r"""Sets the parser_ids of this ExportCollectorParserResponse.

        相关描述信息

        :param parser_ids: The parser_ids of this ExportCollectorParserResponse.
        :type parser_ids: list[:class:`huaweicloudsdksecmaster.v1.ExportParserResponseDto`]
        """
        self._parser_ids = parser_ids

    def to_dict(self):
        import warnings
        warnings.warn("ExportCollectorParserResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExportCollectorParserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
