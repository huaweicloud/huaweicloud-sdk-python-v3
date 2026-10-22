# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'applications': 'list[ServeApplication]'
    }

    attribute_map = {
        'applications': 'applications'
    }

    def __init__(self, applications=None):
        r"""ServeConfig

        The model defined in huaweicloud sdk

        :param applications: **参数解释**：Serve 应用列表。 **约束限制**：数量不超过3个，且各应用 name 与 route_prefix 均不可重复。
        :type applications: list[:class:`huaweicloudsdkaidatalake.v2.ServeApplication`]
        """
        
        

        self._applications = None
        self.discriminator = None

        self.applications = applications

    @property
    def applications(self):
        r"""Gets the applications of this ServeConfig.

        **参数解释**：Serve 应用列表。 **约束限制**：数量不超过3个，且各应用 name 与 route_prefix 均不可重复。

        :return: The applications of this ServeConfig.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ServeApplication`]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        r"""Sets the applications of this ServeConfig.

        **参数解释**：Serve 应用列表。 **约束限制**：数量不超过3个，且各应用 name 与 route_prefix 均不可重复。

        :param applications: The applications of this ServeConfig.
        :type applications: list[:class:`huaweicloudsdkaidatalake.v2.ServeApplication`]
        """
        self._applications = applications

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
        if not isinstance(other, ServeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
