# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDisassociateModelProxiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_details': 'list[CoreModelProxyDetails]',
        'failed_details': 'list[CodeModelProxyFailedItem]'
    }

    attribute_map = {
        'success_details': 'success_details',
        'failed_details': 'failed_details'
    }

    def __init__(self, success_details=None, failed_details=None):
        r"""BatchDisassociateModelProxiesResponse

        The model defined in huaweicloud sdk

        :param success_details: **参数解释：** 成功详情。 **取值范围：** 不涉及。 
        :type success_details: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        :param failed_details: **参数解释：** 失败详情。 **取值范围：** 不涉及。 
        :type failed_details: list[:class:`huaweicloudsdkagentarts.v1.CodeModelProxyFailedItem`]
        """
        
        super().__init__()

        self._success_details = None
        self._failed_details = None
        self.discriminator = None

        if success_details is not None:
            self.success_details = success_details
        if failed_details is not None:
            self.failed_details = failed_details

    @property
    def success_details(self):
        r"""Gets the success_details of this BatchDisassociateModelProxiesResponse.

        **参数解释：** 成功详情。 **取值范围：** 不涉及。 

        :return: The success_details of this BatchDisassociateModelProxiesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        """
        return self._success_details

    @success_details.setter
    def success_details(self, success_details):
        r"""Sets the success_details of this BatchDisassociateModelProxiesResponse.

        **参数解释：** 成功详情。 **取值范围：** 不涉及。 

        :param success_details: The success_details of this BatchDisassociateModelProxiesResponse.
        :type success_details: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        """
        self._success_details = success_details

    @property
    def failed_details(self):
        r"""Gets the failed_details of this BatchDisassociateModelProxiesResponse.

        **参数解释：** 失败详情。 **取值范围：** 不涉及。 

        :return: The failed_details of this BatchDisassociateModelProxiesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CodeModelProxyFailedItem`]
        """
        return self._failed_details

    @failed_details.setter
    def failed_details(self, failed_details):
        r"""Sets the failed_details of this BatchDisassociateModelProxiesResponse.

        **参数解释：** 失败详情。 **取值范围：** 不涉及。 

        :param failed_details: The failed_details of this BatchDisassociateModelProxiesResponse.
        :type failed_details: list[:class:`huaweicloudsdkagentarts.v1.CodeModelProxyFailedItem`]
        """
        self._failed_details = failed_details

    def to_dict(self):
        import warnings
        warnings.warn("BatchDisassociateModelProxiesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDisassociateModelProxiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
