# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverrideSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_selectors': 'list[ResourceSelector]',
        'overriders': 'object'
    }

    attribute_map = {
        'resource_selectors': 'resourceSelectors',
        'overriders': 'overriders'
    }

    def __init__(self, resource_selectors=None, overriders=None):
        r"""OverrideSpec

        The model defined in huaweicloud sdk

        :param resource_selectors: 资源选择器，限制该覆盖策略适用的资源类型
        :type resource_selectors: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        :param overriders: 将应用于资源的覆盖规则
        :type overriders: object
        """
        
        

        self._resource_selectors = None
        self._overriders = None
        self.discriminator = None

        if resource_selectors is not None:
            self.resource_selectors = resource_selectors
        if overriders is not None:
            self.overriders = overriders

    @property
    def resource_selectors(self):
        r"""Gets the resource_selectors of this OverrideSpec.

        资源选择器，限制该覆盖策略适用的资源类型

        :return: The resource_selectors of this OverrideSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        """
        return self._resource_selectors

    @resource_selectors.setter
    def resource_selectors(self, resource_selectors):
        r"""Sets the resource_selectors of this OverrideSpec.

        资源选择器，限制该覆盖策略适用的资源类型

        :param resource_selectors: The resource_selectors of this OverrideSpec.
        :type resource_selectors: list[:class:`huaweicloudsdkucs.v1.ResourceSelector`]
        """
        self._resource_selectors = resource_selectors

    @property
    def overriders(self):
        r"""Gets the overriders of this OverrideSpec.

        将应用于资源的覆盖规则

        :return: The overriders of this OverrideSpec.
        :rtype: object
        """
        return self._overriders

    @overriders.setter
    def overriders(self, overriders):
        r"""Sets the overriders of this OverrideSpec.

        将应用于资源的覆盖规则

        :param overriders: The overriders of this OverrideSpec.
        :type overriders: object
        """
        self._overriders = overriders

    def to_dict(self):
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
        if not isinstance(other, OverrideSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
