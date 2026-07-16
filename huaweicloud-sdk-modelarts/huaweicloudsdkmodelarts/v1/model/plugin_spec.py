# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'Template'
    }

    attribute_map = {
        'template': 'template'
    }

    def __init__(self, template=None):
        r"""PluginSpec

        The model defined in huaweicloud sdk

        :param template: 
        :type template: :class:`huaweicloudsdkmodelarts.v1.Template`
        """
        
        

        self._template = None
        self.discriminator = None

        self.template = template

    @property
    def template(self):
        r"""Gets the template of this PluginSpec.

        :return: The template of this PluginSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Template`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this PluginSpec.

        :param template: The template of this PluginSpec.
        :type template: :class:`huaweicloudsdkmodelarts.v1.Template`
        """
        self._template = template

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
        if not isinstance(other, PluginSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
