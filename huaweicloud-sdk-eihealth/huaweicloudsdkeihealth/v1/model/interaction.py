# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Interaction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binding_site': 'str',
        'type': 'InteractionType',
        'amino_acid': 'str'
    }

    attribute_map = {
        'binding_site': 'binding_site',
        'type': 'type',
        'amino_acid': 'amino_acid'
    }

    def __init__(self, binding_site=None, type=None, amino_acid=None):
        r"""Interaction

        The model defined in huaweicloud sdk

        :param binding_site: 靶点，只支持target1或target2。
        :type binding_site: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.InteractionType`
        :param amino_acid: 氨基酸
        :type amino_acid: str
        """
        
        

        self._binding_site = None
        self._type = None
        self._amino_acid = None
        self.discriminator = None

        self.binding_site = binding_site
        self.type = type
        self.amino_acid = amino_acid

    @property
    def binding_site(self):
        r"""Gets the binding_site of this Interaction.

        靶点，只支持target1或target2。

        :return: The binding_site of this Interaction.
        :rtype: str
        """
        return self._binding_site

    @binding_site.setter
    def binding_site(self, binding_site):
        r"""Sets the binding_site of this Interaction.

        靶点，只支持target1或target2。

        :param binding_site: The binding_site of this Interaction.
        :type binding_site: str
        """
        self._binding_site = binding_site

    @property
    def type(self):
        r"""Gets the type of this Interaction.

        :return: The type of this Interaction.
        :rtype: :class:`huaweicloudsdkeihealth.v1.InteractionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Interaction.

        :param type: The type of this Interaction.
        :type type: :class:`huaweicloudsdkeihealth.v1.InteractionType`
        """
        self._type = type

    @property
    def amino_acid(self):
        r"""Gets the amino_acid of this Interaction.

        氨基酸

        :return: The amino_acid of this Interaction.
        :rtype: str
        """
        return self._amino_acid

    @amino_acid.setter
    def amino_acid(self, amino_acid):
        r"""Sets the amino_acid of this Interaction.

        氨基酸

        :param amino_acid: The amino_acid of this Interaction.
        :type amino_acid: str
        """
        self._amino_acid = amino_acid

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
        if not isinstance(other, Interaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
