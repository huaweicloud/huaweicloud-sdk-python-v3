# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandPreviewInfoDto:

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
        'name': 'str',
        'success': 'bool',
        'smiles': 'str',
        'formula': 'str',
        'is_3d': 'bool',
        'structure': 'LigandStructureDto',
        'reason': 'str'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'success': 'success',
        'smiles': 'smiles',
        'formula': 'formula',
        'is_3d': 'is_3d',
        'structure': 'structure',
        'reason': 'reason'
    }

    def __init__(self, index=None, name=None, success=None, smiles=None, formula=None, is_3d=None, structure=None, reason=None):
        r"""LigandPreviewInfoDto

        The model defined in huaweicloud sdk

        :param index: 配体索引（从0起编号）
        :type index: int
        :param name: 配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）
        :type name: str
        :param success: 解析是否成功
        :type success: bool
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param formula: 配体分子的化学式
        :type formula: str
        :param is_3d: 标识原始数据是否为3D
        :type is_3d: bool
        :param structure: 
        :type structure: :class:`huaweicloudsdkeihealth.v1.LigandStructureDto`
        :param reason: 解析失败的理由
        :type reason: str
        """
        
        

        self._index = None
        self._name = None
        self._success = None
        self._smiles = None
        self._formula = None
        self._is_3d = None
        self._structure = None
        self._reason = None
        self.discriminator = None

        self.index = index
        self.name = name
        self.success = success
        if smiles is not None:
            self.smiles = smiles
        if formula is not None:
            self.formula = formula
        if is_3d is not None:
            self.is_3d = is_3d
        if structure is not None:
            self.structure = structure
        if reason is not None:
            self.reason = reason

    @property
    def index(self):
        r"""Gets the index of this LigandPreviewInfoDto.

        配体索引（从0起编号）

        :return: The index of this LigandPreviewInfoDto.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this LigandPreviewInfoDto.

        配体索引（从0起编号）

        :param index: The index of this LigandPreviewInfoDto.
        :type index: int
        """
        self._index = index

    @property
    def name(self):
        r"""Gets the name of this LigandPreviewInfoDto.

        配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）

        :return: The name of this LigandPreviewInfoDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LigandPreviewInfoDto.

        配体名称，若无名称则自动命名，格式为UNK+索引（从1起编号）

        :param name: The name of this LigandPreviewInfoDto.
        :type name: str
        """
        self._name = name

    @property
    def success(self):
        r"""Gets the success of this LigandPreviewInfoDto.

        解析是否成功

        :return: The success of this LigandPreviewInfoDto.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this LigandPreviewInfoDto.

        解析是否成功

        :param success: The success of this LigandPreviewInfoDto.
        :type success: bool
        """
        self._success = success

    @property
    def smiles(self):
        r"""Gets the smiles of this LigandPreviewInfoDto.

        分子SMILES表达式

        :return: The smiles of this LigandPreviewInfoDto.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        r"""Sets the smiles of this LigandPreviewInfoDto.

        分子SMILES表达式

        :param smiles: The smiles of this LigandPreviewInfoDto.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def formula(self):
        r"""Gets the formula of this LigandPreviewInfoDto.

        配体分子的化学式

        :return: The formula of this LigandPreviewInfoDto.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        r"""Sets the formula of this LigandPreviewInfoDto.

        配体分子的化学式

        :param formula: The formula of this LigandPreviewInfoDto.
        :type formula: str
        """
        self._formula = formula

    @property
    def is_3d(self):
        r"""Gets the is_3d of this LigandPreviewInfoDto.

        标识原始数据是否为3D

        :return: The is_3d of this LigandPreviewInfoDto.
        :rtype: bool
        """
        return self._is_3d

    @is_3d.setter
    def is_3d(self, is_3d):
        r"""Sets the is_3d of this LigandPreviewInfoDto.

        标识原始数据是否为3D

        :param is_3d: The is_3d of this LigandPreviewInfoDto.
        :type is_3d: bool
        """
        self._is_3d = is_3d

    @property
    def structure(self):
        r"""Gets the structure of this LigandPreviewInfoDto.

        :return: The structure of this LigandPreviewInfoDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.LigandStructureDto`
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        r"""Sets the structure of this LigandPreviewInfoDto.

        :param structure: The structure of this LigandPreviewInfoDto.
        :type structure: :class:`huaweicloudsdkeihealth.v1.LigandStructureDto`
        """
        self._structure = structure

    @property
    def reason(self):
        r"""Gets the reason of this LigandPreviewInfoDto.

        解析失败的理由

        :return: The reason of this LigandPreviewInfoDto.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this LigandPreviewInfoDto.

        解析失败的理由

        :param reason: The reason of this LigandPreviewInfoDto.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, LigandPreviewInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
