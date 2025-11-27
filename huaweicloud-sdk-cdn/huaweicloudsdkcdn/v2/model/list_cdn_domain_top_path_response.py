# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainTopPathResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_path_summary': 'list[TopPathSummary]'
    }

    attribute_map = {
        'top_path_summary': 'top_path_summary'
    }

    def __init__(self, top_path_summary=None):
        r"""ListCdnDomainTopPathResponse

        The model defined in huaweicloud sdk

        :param top_path_summary: 详情数据对象。
        :type top_path_summary: list[:class:`huaweicloudsdkcdn.v2.TopPathSummary`]
        """
        
        super().__init__()

        self._top_path_summary = None
        self.discriminator = None

        if top_path_summary is not None:
            self.top_path_summary = top_path_summary

    @property
    def top_path_summary(self):
        r"""Gets the top_path_summary of this ListCdnDomainTopPathResponse.

        详情数据对象。

        :return: The top_path_summary of this ListCdnDomainTopPathResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.TopPathSummary`]
        """
        return self._top_path_summary

    @top_path_summary.setter
    def top_path_summary(self, top_path_summary):
        r"""Sets the top_path_summary of this ListCdnDomainTopPathResponse.

        详情数据对象。

        :param top_path_summary: The top_path_summary of this ListCdnDomainTopPathResponse.
        :type top_path_summary: list[:class:`huaweicloudsdkcdn.v2.TopPathSummary`]
        """
        self._top_path_summary = top_path_summary

    def to_dict(self):
        import warnings
        warnings.warn("ListCdnDomainTopPathResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCdnDomainTopPathResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
