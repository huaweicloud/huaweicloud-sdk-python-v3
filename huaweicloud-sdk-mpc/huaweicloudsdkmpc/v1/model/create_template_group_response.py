# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateTemplateGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_group': 'TemplateGroup'
    }

    attribute_map = {
        'template_group': 'template_group'
    }

    def __init__(self, template_group=None):
        """CreateTemplateGroupResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._template_group = None
        self.discriminator = None

        if template_group is not None:
            self.template_group = template_group

    @property
    def template_group(self):
        """Gets the template_group of this CreateTemplateGroupResponse.


        :return: The template_group of this CreateTemplateGroupResponse.
        :rtype: TemplateGroup
        """
        return self._template_group

    @template_group.setter
    def template_group(self, template_group):
        """Sets the template_group of this CreateTemplateGroupResponse.


        :param template_group: The template_group of this CreateTemplateGroupResponse.
        :type: TemplateGroup
        """
        self._template_group = template_group

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateTemplateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
