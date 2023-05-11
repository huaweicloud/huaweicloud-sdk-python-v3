# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisResultResultMolecules:

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
        'smiles': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'smiles': 'smiles',
        'source': 'source'
    }

    def __init__(self, id=None, smiles=None, source=None):
        """SynthesisResultResultMolecules

        The model defined in huaweicloud sdk

        :param id: molecule的序号
        :type id: str
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param source: molecule的smiles来源
        :type source: str
        """
        
        

        self._id = None
        self._smiles = None
        self._source = None
        self.discriminator = None

        self.id = id
        self.smiles = smiles
        self.source = source

    @property
    def id(self):
        """Gets the id of this SynthesisResultResultMolecules.

        molecule的序号

        :return: The id of this SynthesisResultResultMolecules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SynthesisResultResultMolecules.

        molecule的序号

        :param id: The id of this SynthesisResultResultMolecules.
        :type id: str
        """
        self._id = id

    @property
    def smiles(self):
        """Gets the smiles of this SynthesisResultResultMolecules.

        分子SMILES表达式

        :return: The smiles of this SynthesisResultResultMolecules.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this SynthesisResultResultMolecules.

        分子SMILES表达式

        :param smiles: The smiles of this SynthesisResultResultMolecules.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def source(self):
        """Gets the source of this SynthesisResultResultMolecules.

        molecule的smiles来源

        :return: The source of this SynthesisResultResultMolecules.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SynthesisResultResultMolecules.

        molecule的smiles来源

        :param source: The source of this SynthesisResultResultMolecules.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, SynthesisResultResultMolecules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
