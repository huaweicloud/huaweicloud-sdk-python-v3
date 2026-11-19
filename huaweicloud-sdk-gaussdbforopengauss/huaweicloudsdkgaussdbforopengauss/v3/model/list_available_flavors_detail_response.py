# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableFlavorsDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_category': 'FlavorCategoryDetail'
    }

    attribute_map = {
        'flavor_category': 'flavor_category'
    }

    def __init__(self, flavor_category=None):
        r"""ListAvailableFlavorsDetailResponse

        The model defined in huaweicloud sdk

        :param flavor_category: 
        :type flavor_category: :class:`huaweicloudsdkgaussdbforopengauss.v3.FlavorCategoryDetail`
        """
        
        super().__init__()

        self._flavor_category = None
        self.discriminator = None

        if flavor_category is not None:
            self.flavor_category = flavor_category

    @property
    def flavor_category(self):
        r"""Gets the flavor_category of this ListAvailableFlavorsDetailResponse.

        :return: The flavor_category of this ListAvailableFlavorsDetailResponse.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.FlavorCategoryDetail`
        """
        return self._flavor_category

    @flavor_category.setter
    def flavor_category(self, flavor_category):
        r"""Sets the flavor_category of this ListAvailableFlavorsDetailResponse.

        :param flavor_category: The flavor_category of this ListAvailableFlavorsDetailResponse.
        :type flavor_category: :class:`huaweicloudsdkgaussdbforopengauss.v3.FlavorCategoryDetail`
        """
        self._flavor_category = flavor_category

    def to_dict(self):
        import warnings
        warnings.warn("ListAvailableFlavorsDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAvailableFlavorsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
