# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaShowFlavorExtraSpecsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_specs': 'dict(str, str)'
    }

    attribute_map = {
        'extra_specs': 'extra_specs'
    }

    def __init__(self, extra_specs=None):
        r"""NovaShowFlavorExtraSpecsResponse

        The model defined in huaweicloud sdk

        :param extra_specs: 描述弹性云服务器规格的键值对。
        :type extra_specs: dict(str, str)
        """
        
        super().__init__()

        self._extra_specs = None
        self.discriminator = None

        if extra_specs is not None:
            self.extra_specs = extra_specs

    @property
    def extra_specs(self):
        r"""Gets the extra_specs of this NovaShowFlavorExtraSpecsResponse.

        描述弹性云服务器规格的键值对。

        :return: The extra_specs of this NovaShowFlavorExtraSpecsResponse.
        :rtype: dict(str, str)
        """
        return self._extra_specs

    @extra_specs.setter
    def extra_specs(self, extra_specs):
        r"""Sets the extra_specs of this NovaShowFlavorExtraSpecsResponse.

        描述弹性云服务器规格的键值对。

        :param extra_specs: The extra_specs of this NovaShowFlavorExtraSpecsResponse.
        :type extra_specs: dict(str, str)
        """
        self._extra_specs = extra_specs

    def to_dict(self):
        import warnings
        warnings.warn("NovaShowFlavorExtraSpecsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, NovaShowFlavorExtraSpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
