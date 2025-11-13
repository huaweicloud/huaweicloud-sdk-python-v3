# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemLinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lines': 'list[SystemLine]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'lines': 'lines',
        'metadata': 'metadata'
    }

    def __init__(self, lines=None, metadata=None):
        r"""ListSystemLinesResponse

        The model defined in huaweicloud sdk

        :param lines: **参数解释：** 线路列表。 **取值范围：** 不涉及。
        :type lines: list[:class:`huaweicloudsdkdns.v2.SystemLine`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super().__init__()

        self._lines = None
        self._metadata = None
        self.discriminator = None

        if lines is not None:
            self.lines = lines
        if metadata is not None:
            self.metadata = metadata

    @property
    def lines(self):
        r"""Gets the lines of this ListSystemLinesResponse.

        **参数解释：** 线路列表。 **取值范围：** 不涉及。

        :return: The lines of this ListSystemLinesResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.SystemLine`]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this ListSystemLinesResponse.

        **参数解释：** 线路列表。 **取值范围：** 不涉及。

        :param lines: The lines of this ListSystemLinesResponse.
        :type lines: list[:class:`huaweicloudsdkdns.v2.SystemLine`]
        """
        self._lines = lines

    @property
    def metadata(self):
        r"""Gets the metadata of this ListSystemLinesResponse.

        :return: The metadata of this ListSystemLinesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListSystemLinesResponse.

        :param metadata: The metadata of this ListSystemLinesResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        self._metadata = metadata

    def to_dict(self):
        import warnings
        warnings.warn("ListSystemLinesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSystemLinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
