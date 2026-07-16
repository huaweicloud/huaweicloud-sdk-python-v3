# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetModel:

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
        'code': 'str',
        'version': 'str',
        'desc': 'str',
        'series': 'str',
        'type': 'str',
        'model_desc': 'str',
        'parent_asset_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'version': 'version',
        'desc': 'desc',
        'series': 'series',
        'type': 'type',
        'model_desc': 'model_desc',
        'parent_asset_id': 'parent_asset_id'
    }

    def __init__(self, name=None, code=None, version=None, desc=None, series=None, type=None, model_desc=None, parent_asset_id=None):
        r"""AssetModel

        The model defined in huaweicloud sdk

        :param name: **参数解释**：模型名称。 **取值范围**：不涉及。
        :type name: str
        :param code: **参数解释**：模型名称。 **取值范围**：不涉及。
        :type code: str
        :param version: **参数解释**：模型发布版本。 **取值范围**：不涉及。
        :type version: str
        :param desc: **参数解释**：模型描述。 **取值范围**：不涉及。
        :type desc: str
        :param series: **参数解释**：模型品牌。 **取值范围**：不涉及。
        :type series: str
        :param type: **参数解释**：模型类型。 **取值范围**：不涉及。
        :type type: str
        :param model_desc: **参数解释**：模型资产描述。\\n**取值范围**：不涉及。
        :type model_desc: str
        :param parent_asset_id: **参数解释**：父资产ID（可选），选择已有模型时传递。\\n**取值范围**：不涉及。
        :type parent_asset_id: str
        """
        
        

        self._name = None
        self._code = None
        self._version = None
        self._desc = None
        self._series = None
        self._type = None
        self._model_desc = None
        self._parent_asset_id = None
        self.discriminator = None

        self.name = name
        if code is not None:
            self.code = code
        self.version = version
        if desc is not None:
            self.desc = desc
        if series is not None:
            self.series = series
        self.type = type
        if model_desc is not None:
            self.model_desc = model_desc
        if parent_asset_id is not None:
            self.parent_asset_id = parent_asset_id

    @property
    def name(self):
        r"""Gets the name of this AssetModel.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :return: The name of this AssetModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetModel.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :param name: The name of this AssetModel.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this AssetModel.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :return: The code of this AssetModel.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AssetModel.

        **参数解释**：模型名称。 **取值范围**：不涉及。

        :param code: The code of this AssetModel.
        :type code: str
        """
        self._code = code

    @property
    def version(self):
        r"""Gets the version of this AssetModel.

        **参数解释**：模型发布版本。 **取值范围**：不涉及。

        :return: The version of this AssetModel.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AssetModel.

        **参数解释**：模型发布版本。 **取值范围**：不涉及。

        :param version: The version of this AssetModel.
        :type version: str
        """
        self._version = version

    @property
    def desc(self):
        r"""Gets the desc of this AssetModel.

        **参数解释**：模型描述。 **取值范围**：不涉及。

        :return: The desc of this AssetModel.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this AssetModel.

        **参数解释**：模型描述。 **取值范围**：不涉及。

        :param desc: The desc of this AssetModel.
        :type desc: str
        """
        self._desc = desc

    @property
    def series(self):
        r"""Gets the series of this AssetModel.

        **参数解释**：模型品牌。 **取值范围**：不涉及。

        :return: The series of this AssetModel.
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this AssetModel.

        **参数解释**：模型品牌。 **取值范围**：不涉及。

        :param series: The series of this AssetModel.
        :type series: str
        """
        self._series = series

    @property
    def type(self):
        r"""Gets the type of this AssetModel.

        **参数解释**：模型类型。 **取值范围**：不涉及。

        :return: The type of this AssetModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssetModel.

        **参数解释**：模型类型。 **取值范围**：不涉及。

        :param type: The type of this AssetModel.
        :type type: str
        """
        self._type = type

    @property
    def model_desc(self):
        r"""Gets the model_desc of this AssetModel.

        **参数解释**：模型资产描述。\\n**取值范围**：不涉及。

        :return: The model_desc of this AssetModel.
        :rtype: str
        """
        return self._model_desc

    @model_desc.setter
    def model_desc(self, model_desc):
        r"""Sets the model_desc of this AssetModel.

        **参数解释**：模型资产描述。\\n**取值范围**：不涉及。

        :param model_desc: The model_desc of this AssetModel.
        :type model_desc: str
        """
        self._model_desc = model_desc

    @property
    def parent_asset_id(self):
        r"""Gets the parent_asset_id of this AssetModel.

        **参数解释**：父资产ID（可选），选择已有模型时传递。\\n**取值范围**：不涉及。

        :return: The parent_asset_id of this AssetModel.
        :rtype: str
        """
        return self._parent_asset_id

    @parent_asset_id.setter
    def parent_asset_id(self, parent_asset_id):
        r"""Sets the parent_asset_id of this AssetModel.

        **参数解释**：父资产ID（可选），选择已有模型时传递。\\n**取值范围**：不涉及。

        :param parent_asset_id: The parent_asset_id of this AssetModel.
        :type parent_asset_id: str
        """
        self._parent_asset_id = parent_asset_id

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
        if not isinstance(other, AssetModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
