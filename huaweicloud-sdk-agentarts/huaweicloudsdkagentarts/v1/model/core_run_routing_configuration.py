# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunRoutingConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_weights': 'list[CoreRunVersionWeight]'
    }

    attribute_map = {
        'version_weights': 'version_weights'
    }

    def __init__(self, version_weights=None):
        r"""CoreRunRoutingConfiguration

        The model defined in huaweicloud sdk

        :param version_weights: **参数解释**: 运行时访问方式多版本权重配置。 
        :type version_weights: list[:class:`huaweicloudsdkagentarts.v1.CoreRunVersionWeight`]
        """
        
        

        self._version_weights = None
        self.discriminator = None

        if version_weights is not None:
            self.version_weights = version_weights

    @property
    def version_weights(self):
        r"""Gets the version_weights of this CoreRunRoutingConfiguration.

        **参数解释**: 运行时访问方式多版本权重配置。 

        :return: The version_weights of this CoreRunRoutingConfiguration.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunVersionWeight`]
        """
        return self._version_weights

    @version_weights.setter
    def version_weights(self, version_weights):
        r"""Sets the version_weights of this CoreRunRoutingConfiguration.

        **参数解释**: 运行时访问方式多版本权重配置。 

        :param version_weights: The version_weights of this CoreRunRoutingConfiguration.
        :type version_weights: list[:class:`huaweicloudsdkagentarts.v1.CoreRunVersionWeight`]
        """
        self._version_weights = version_weights

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
        if not isinstance(other, CoreRunRoutingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
