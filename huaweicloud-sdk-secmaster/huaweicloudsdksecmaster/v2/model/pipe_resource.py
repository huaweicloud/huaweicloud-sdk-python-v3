# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipeResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipe_resource_type': 'object'
    }

    attribute_map = {
        'pipe_resource_type': 'pipe_resource_type'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, pipe_resource_type=None):
        r"""PipeResource

        The model defined in huaweicloud sdk

        :param pipe_resource_type: 管道资源
        :type pipe_resource_type: object
        """
        
        

        self._pipe_resource_type = None
        self.discriminator = 'pipe_resource_type'

        self.pipe_resource_type = pipe_resource_type

    @property
    def pipe_resource_type(self):
        r"""Gets the pipe_resource_type of this PipeResource.

        管道资源

        :return: The pipe_resource_type of this PipeResource.
        :rtype: object
        """
        return self._pipe_resource_type

    @pipe_resource_type.setter
    def pipe_resource_type(self, pipe_resource_type):
        r"""Sets the pipe_resource_type of this PipeResource.

        管道资源

        :param pipe_resource_type: The pipe_resource_type of this PipeResource.
        :type pipe_resource_type: object
        """
        self._pipe_resource_type = pipe_resource_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)
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
        if not isinstance(other, PipeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
