# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleExtraMetaModellingAlgorithm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'additional_properties': 'StyleExtraMetaAdditionalProperties1'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties'
    }

    def __init__(self, additional_properties=None):
        """StyleExtraMetaModellingAlgorithm

        The model defined in huaweicloud sdk

        :param additional_properties: 
        :type additional_properties: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMetaAdditionalProperties1`
        """
        
        

        self._additional_properties = None
        self.discriminator = None

        if additional_properties is not None:
            self.additional_properties = additional_properties

    @property
    def additional_properties(self):
        """Gets the additional_properties of this StyleExtraMetaModellingAlgorithm.

        :return: The additional_properties of this StyleExtraMetaModellingAlgorithm.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMetaAdditionalProperties1`
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """Sets the additional_properties of this StyleExtraMetaModellingAlgorithm.

        :param additional_properties: The additional_properties of this StyleExtraMetaModellingAlgorithm.
        :type additional_properties: :class:`huaweicloudsdkmetastudio.v1.StyleExtraMetaAdditionalProperties1`
        """
        self._additional_properties = additional_properties

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
        if not isinstance(other, StyleExtraMetaModellingAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
