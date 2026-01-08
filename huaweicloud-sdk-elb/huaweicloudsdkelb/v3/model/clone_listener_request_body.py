# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneListenerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_listener_params': 'list[CloneListenerOption]'
    }

    attribute_map = {
        'target_listener_params': 'target_listener_params'
    }

    def __init__(self, target_listener_params=None):
        r"""CloneListenerRequestBody

        The model defined in huaweicloud sdk

        :param target_listener_params: **参数解释**：复制后的新监听器相关配置。 **约束限制**：不涉及
        :type target_listener_params: list[:class:`huaweicloudsdkelb.v3.CloneListenerOption`]
        """
        
        

        self._target_listener_params = None
        self.discriminator = None

        self.target_listener_params = target_listener_params

    @property
    def target_listener_params(self):
        r"""Gets the target_listener_params of this CloneListenerRequestBody.

        **参数解释**：复制后的新监听器相关配置。 **约束限制**：不涉及

        :return: The target_listener_params of this CloneListenerRequestBody.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CloneListenerOption`]
        """
        return self._target_listener_params

    @target_listener_params.setter
    def target_listener_params(self, target_listener_params):
        r"""Sets the target_listener_params of this CloneListenerRequestBody.

        **参数解释**：复制后的新监听器相关配置。 **约束限制**：不涉及

        :param target_listener_params: The target_listener_params of this CloneListenerRequestBody.
        :type target_listener_params: list[:class:`huaweicloudsdkelb.v3.CloneListenerOption`]
        """
        self._target_listener_params = target_listener_params

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
        if not isinstance(other, CloneListenerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
