# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisResultResultReactions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'reactants': 'list[str]',
        'product': 'str'
    }

    attribute_map = {
        'id': 'id',
        'reactants': 'reactants',
        'product': 'product'
    }

    def __init__(self, id=None, reactants=None, product=None):
        r"""SynthesisResultResultReactions

        The model defined in huaweicloud sdk

        :param id: 反应的序号
        :type id: str
        :param reactants: 反应物分子序号的列表
        :type reactants: list[str]
        :param product: 产物分子序号
        :type product: str
        """
        
        

        self._id = None
        self._reactants = None
        self._product = None
        self.discriminator = None

        self.id = id
        self.reactants = reactants
        self.product = product

    @property
    def id(self):
        r"""Gets the id of this SynthesisResultResultReactions.

        反应的序号

        :return: The id of this SynthesisResultResultReactions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SynthesisResultResultReactions.

        反应的序号

        :param id: The id of this SynthesisResultResultReactions.
        :type id: str
        """
        self._id = id

    @property
    def reactants(self):
        r"""Gets the reactants of this SynthesisResultResultReactions.

        反应物分子序号的列表

        :return: The reactants of this SynthesisResultResultReactions.
        :rtype: list[str]
        """
        return self._reactants

    @reactants.setter
    def reactants(self, reactants):
        r"""Sets the reactants of this SynthesisResultResultReactions.

        反应物分子序号的列表

        :param reactants: The reactants of this SynthesisResultResultReactions.
        :type reactants: list[str]
        """
        self._reactants = reactants

    @property
    def product(self):
        r"""Gets the product of this SynthesisResultResultReactions.

        产物分子序号

        :return: The product of this SynthesisResultResultReactions.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        r"""Sets the product of this SynthesisResultResultReactions.

        产物分子序号

        :param product: The product of this SynthesisResultResultReactions.
        :type product: str
        """
        self._product = product

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
        if not isinstance(other, SynthesisResultResultReactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
