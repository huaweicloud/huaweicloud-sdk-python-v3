# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandPreviewDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'file': 'DrugFile',
        'name': 'str',
        'smiles': 'str'
    }

    attribute_map = {
        'index': 'index',
        'file': 'file',
        'name': 'name',
        'smiles': 'smiles'
    }

    def __init__(self, index=None, file=None, name=None, smiles=None):
        """LigandPreviewDto

        The model defined in huaweicloud sdk

        :param index: 配体索引（从0起编号）
        :type index: int
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param name: 配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）
        :type name: str
        :param smiles: 分子SMILES表达式
        :type smiles: str
        """
        
        

        self._index = None
        self._file = None
        self._name = None
        self._smiles = None
        self.discriminator = None

        self.index = index
        self.file = file
        self.name = name
        self.smiles = smiles

    @property
    def index(self):
        """Gets the index of this LigandPreviewDto.

        配体索引（从0起编号）

        :return: The index of this LigandPreviewDto.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this LigandPreviewDto.

        配体索引（从0起编号）

        :param index: The index of this LigandPreviewDto.
        :type index: int
        """
        self._index = index

    @property
    def file(self):
        """Gets the file of this LigandPreviewDto.

        :return: The file of this LigandPreviewDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this LigandPreviewDto.

        :param file: The file of this LigandPreviewDto.
        :type file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._file = file

    @property
    def name(self):
        """Gets the name of this LigandPreviewDto.

        配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）

        :return: The name of this LigandPreviewDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LigandPreviewDto.

        配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）

        :param name: The name of this LigandPreviewDto.
        :type name: str
        """
        self._name = name

    @property
    def smiles(self):
        """Gets the smiles of this LigandPreviewDto.

        分子SMILES表达式

        :return: The smiles of this LigandPreviewDto.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this LigandPreviewDto.

        分子SMILES表达式

        :param smiles: The smiles of this LigandPreviewDto.
        :type smiles: str
        """
        self._smiles = smiles

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
        if not isinstance(other, LigandPreviewDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
