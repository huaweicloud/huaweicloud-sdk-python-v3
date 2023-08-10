# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLigandSimilarityGraphLigandDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'smiles': 'str',
        'main': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'smiles': 'smiles',
        'main': 'main'
    }

    def __init__(self, name=None, smiles=None, main=None):
        """CreateLigandSimilarityGraphLigandDto

        The model defined in huaweicloud sdk

        :param name: 配体分子唯一名字，受体中的建议使用\&quot;{氨基酸}:{链}:{编号}\&quot;
        :type name: str
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param main: 配体是否为主要配体，在中心模式下，必须指定1个主要配体
        :type main: bool
        """
        
        

        self._name = None
        self._smiles = None
        self._main = None
        self.discriminator = None

        self.name = name
        self.smiles = smiles
        if main is not None:
            self.main = main

    @property
    def name(self):
        """Gets the name of this CreateLigandSimilarityGraphLigandDto.

        配体分子唯一名字，受体中的建议使用\"{氨基酸}:{链}:{编号}\"

        :return: The name of this CreateLigandSimilarityGraphLigandDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLigandSimilarityGraphLigandDto.

        配体分子唯一名字，受体中的建议使用\"{氨基酸}:{链}:{编号}\"

        :param name: The name of this CreateLigandSimilarityGraphLigandDto.
        :type name: str
        """
        self._name = name

    @property
    def smiles(self):
        """Gets the smiles of this CreateLigandSimilarityGraphLigandDto.

        分子SMILES表达式

        :return: The smiles of this CreateLigandSimilarityGraphLigandDto.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CreateLigandSimilarityGraphLigandDto.

        分子SMILES表达式

        :param smiles: The smiles of this CreateLigandSimilarityGraphLigandDto.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def main(self):
        """Gets the main of this CreateLigandSimilarityGraphLigandDto.

        配体是否为主要配体，在中心模式下，必须指定1个主要配体

        :return: The main of this CreateLigandSimilarityGraphLigandDto.
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this CreateLigandSimilarityGraphLigandDto.

        配体是否为主要配体，在中心模式下，必须指定1个主要配体

        :param main: The main of this CreateLigandSimilarityGraphLigandDto.
        :type main: bool
        """
        self._main = main

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
        if not isinstance(other, CreateLigandSimilarityGraphLigandDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
