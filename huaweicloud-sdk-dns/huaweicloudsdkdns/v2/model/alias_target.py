# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AliasTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_domain_name': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_domain_name': 'resource_domain_name'
    }

    def __init__(self, resource_type=None, resource_domain_name=None):
        r"""AliasTarget

        The model defined in huaweicloud sdk

        :param resource_type: **参数解释：** 资源服务类型，支持别名记录的服务。 **约束限制：** 不涉及。 **取值范围：** - cloudsite：企业门户 - waf：Web应用防火墙  **默认取值：** 不涉及。
        :type resource_type: str
        :param resource_domain_name: **参数解释：** 对应服务下的域名，由各服务提供。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type resource_domain_name: str
        """
        
        

        self._resource_type = None
        self._resource_domain_name = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_domain_name is not None:
            self.resource_domain_name = resource_domain_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AliasTarget.

        **参数解释：** 资源服务类型，支持别名记录的服务。 **约束限制：** 不涉及。 **取值范围：** - cloudsite：企业门户 - waf：Web应用防火墙  **默认取值：** 不涉及。

        :return: The resource_type of this AliasTarget.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AliasTarget.

        **参数解释：** 资源服务类型，支持别名记录的服务。 **约束限制：** 不涉及。 **取值范围：** - cloudsite：企业门户 - waf：Web应用防火墙  **默认取值：** 不涉及。

        :param resource_type: The resource_type of this AliasTarget.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_domain_name(self):
        r"""Gets the resource_domain_name of this AliasTarget.

        **参数解释：** 对应服务下的域名，由各服务提供。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The resource_domain_name of this AliasTarget.
        :rtype: str
        """
        return self._resource_domain_name

    @resource_domain_name.setter
    def resource_domain_name(self, resource_domain_name):
        r"""Sets the resource_domain_name of this AliasTarget.

        **参数解释：** 对应服务下的域名，由各服务提供。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param resource_domain_name: The resource_domain_name of this AliasTarget.
        :type resource_domain_name: str
        """
        self._resource_domain_name = resource_domain_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AliasTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
