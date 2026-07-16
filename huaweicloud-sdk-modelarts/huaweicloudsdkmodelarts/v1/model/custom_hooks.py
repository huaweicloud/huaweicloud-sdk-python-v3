# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomHooks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_hooks': 'ContainerHooks'
    }

    attribute_map = {
        'container_hooks': 'container_hooks'
    }

    def __init__(self, container_hooks=None):
        r"""CustomHooks

        The model defined in huaweicloud sdk

        :param container_hooks: 
        :type container_hooks: :class:`huaweicloudsdkmodelarts.v1.ContainerHooks`
        """
        
        

        self._container_hooks = None
        self.discriminator = None

        if container_hooks is not None:
            self.container_hooks = container_hooks

    @property
    def container_hooks(self):
        r"""Gets the container_hooks of this CustomHooks.

        :return: The container_hooks of this CustomHooks.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ContainerHooks`
        """
        return self._container_hooks

    @container_hooks.setter
    def container_hooks(self, container_hooks):
        r"""Sets the container_hooks of this CustomHooks.

        :param container_hooks: The container_hooks of this CustomHooks.
        :type container_hooks: :class:`huaweicloudsdkmodelarts.v1.ContainerHooks`
        """
        self._container_hooks = container_hooks

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
        if not isinstance(other, CustomHooks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
