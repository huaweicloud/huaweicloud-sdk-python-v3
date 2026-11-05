# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_list': 'list[ServiceStatusItem]'
    }

    attribute_map = {
        'service_list': 'service_list'
    }

    def __init__(self, service_list=None):
        r"""ListServiceStatusesResponse

        The model defined in huaweicloud sdk

        :param service_list: **参数解释**：服务开通状态。 **取值范围**：数组元素个数限制为16个
        :type service_list: list[:class:`huaweicloudsdkmodelarts.v1.ServiceStatusItem`]
        """
        
        super().__init__()

        self._service_list = None
        self.discriminator = None

        if service_list is not None:
            self.service_list = service_list

    @property
    def service_list(self):
        r"""Gets the service_list of this ListServiceStatusesResponse.

        **参数解释**：服务开通状态。 **取值范围**：数组元素个数限制为16个

        :return: The service_list of this ListServiceStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServiceStatusItem`]
        """
        return self._service_list

    @service_list.setter
    def service_list(self, service_list):
        r"""Sets the service_list of this ListServiceStatusesResponse.

        **参数解释**：服务开通状态。 **取值范围**：数组元素个数限制为16个

        :param service_list: The service_list of this ListServiceStatusesResponse.
        :type service_list: list[:class:`huaweicloudsdkmodelarts.v1.ServiceStatusItem`]
        """
        self._service_list = service_list

    def to_dict(self):
        import warnings
        warnings.warn("ListServiceStatusesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListServiceStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
