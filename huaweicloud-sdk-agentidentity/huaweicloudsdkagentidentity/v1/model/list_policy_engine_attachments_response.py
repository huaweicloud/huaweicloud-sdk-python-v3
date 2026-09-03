# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyEngineAttachmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachments': 'list[PolicyEngineAttachmentSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'attachments': 'attachments',
        'page_info': 'page_info'
    }

    def __init__(self, attachments=None, page_info=None):
        r"""ListPolicyEngineAttachmentsResponse

        The model defined in huaweicloud sdk

        :param attachments: 
        :type attachments: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineAttachmentSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        
        super().__init__()

        self._attachments = None
        self._page_info = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if page_info is not None:
            self.page_info = page_info

    @property
    def attachments(self):
        r"""Gets the attachments of this ListPolicyEngineAttachmentsResponse.

        :return: The attachments of this ListPolicyEngineAttachmentsResponse.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineAttachmentSummary`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this ListPolicyEngineAttachmentsResponse.

        :param attachments: The attachments of this ListPolicyEngineAttachmentsResponse.
        :type attachments: list[:class:`huaweicloudsdkagentidentity.v1.PolicyEngineAttachmentSummary`]
        """
        self._attachments = attachments

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPolicyEngineAttachmentsResponse.

        :return: The page_info of this ListPolicyEngineAttachmentsResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPolicyEngineAttachmentsResponse.

        :param page_info: The page_info of this ListPolicyEngineAttachmentsResponse.
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListPolicyEngineAttachmentsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPolicyEngineAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
