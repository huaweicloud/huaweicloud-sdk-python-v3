# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComputeResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_package_infos': 'list[ResourcePackageInfo]',
        'total': 'int'
    }

    attribute_map = {
        'resource_package_infos': 'resource_package_infos',
        'total': 'total'
    }

    def __init__(self, resource_package_infos=None, total=None):
        r"""ListComputeResourceResponse

        The model defined in huaweicloud sdk

        :param resource_package_infos: 资源包信息列表。
        :type resource_package_infos: list[:class:`huaweicloudsdkrds.v3.ResourcePackageInfo`]
        :param total: 总记录数。
        :type total: int
        """
        
        super().__init__()

        self._resource_package_infos = None
        self._total = None
        self.discriminator = None

        if resource_package_infos is not None:
            self.resource_package_infos = resource_package_infos
        if total is not None:
            self.total = total

    @property
    def resource_package_infos(self):
        r"""Gets the resource_package_infos of this ListComputeResourceResponse.

        资源包信息列表。

        :return: The resource_package_infos of this ListComputeResourceResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ResourcePackageInfo`]
        """
        return self._resource_package_infos

    @resource_package_infos.setter
    def resource_package_infos(self, resource_package_infos):
        r"""Sets the resource_package_infos of this ListComputeResourceResponse.

        资源包信息列表。

        :param resource_package_infos: The resource_package_infos of this ListComputeResourceResponse.
        :type resource_package_infos: list[:class:`huaweicloudsdkrds.v3.ResourcePackageInfo`]
        """
        self._resource_package_infos = resource_package_infos

    @property
    def total(self):
        r"""Gets the total of this ListComputeResourceResponse.

        总记录数。

        :return: The total of this ListComputeResourceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListComputeResourceResponse.

        总记录数。

        :param total: The total of this ListComputeResourceResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListComputeResourceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListComputeResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
