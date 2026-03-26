# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Model:

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
        'name': 'str',
        'datastore_type': 'str',
        'datastore_version': 'str',
        'is_text_model': 'str',
        'model_version_id': 'str',
        'desc': 'str',
        'language': 'str',
        'arch_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'datastore_type': 'datastore_type',
        'datastore_version': 'datastore_version',
        'is_text_model': 'is_text_model',
        'model_version_id': 'model_version_id',
        'desc': 'desc',
        'language': 'language',
        'arch_type': 'arch_type'
    }

    def __init__(self, id=None, name=None, datastore_type=None, datastore_version=None, is_text_model=None, model_version_id=None, desc=None, language=None, arch_type=None):
        r"""Model

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 模型id **取值范围**： 不涉及
        :type id: str
        :param name: **参数解释**： 模型名字 **取值范围**： 不涉及
        :type name: str
        :param datastore_type: **参数解释**： 模型类型 **取值范围**： 不涉及
        :type datastore_type: str
        :param datastore_version: **参数解释**： 模型版本 **取值范围**： 不涉及
        :type datastore_version: str
        :param is_text_model: **参数解释**： 是否是文本模型 **取值范围**： 不涉及
        :type is_text_model: str
        :param model_version_id: **参数解释**： 模型版本id **取值范围**： 不涉及
        :type model_version_id: str
        :param desc: **参数解释**： 模型描述 **取值范围**： 不涉及
        :type desc: str
        :param language: **参数解释**： 模型语言 **取值范围**： 不涉及
        :type language: str
        :param arch_type: **参数解释**： 模型规格 **取值范围**： 不涉及
        :type arch_type: str
        """
        
        

        self._id = None
        self._name = None
        self._datastore_type = None
        self._datastore_version = None
        self._is_text_model = None
        self._model_version_id = None
        self._desc = None
        self._language = None
        self._arch_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if datastore_version is not None:
            self.datastore_version = datastore_version
        if is_text_model is not None:
            self.is_text_model = is_text_model
        if model_version_id is not None:
            self.model_version_id = model_version_id
        if desc is not None:
            self.desc = desc
        if language is not None:
            self.language = language
        if arch_type is not None:
            self.arch_type = arch_type

    @property
    def id(self):
        r"""Gets the id of this Model.

        **参数解释**： 模型id **取值范围**： 不涉及

        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Model.

        **参数解释**： 模型id **取值范围**： 不涉及

        :param id: The id of this Model.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Model.

        **参数解释**： 模型名字 **取值范围**： 不涉及

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Model.

        **参数解释**： 模型名字 **取值范围**： 不涉及

        :param name: The name of this Model.
        :type name: str
        """
        self._name = name

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this Model.

        **参数解释**： 模型类型 **取值范围**： 不涉及

        :return: The datastore_type of this Model.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this Model.

        **参数解释**： 模型类型 **取值范围**： 不涉及

        :param datastore_type: The datastore_type of this Model.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this Model.

        **参数解释**： 模型版本 **取值范围**： 不涉及

        :return: The datastore_version of this Model.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this Model.

        **参数解释**： 模型版本 **取值范围**： 不涉及

        :param datastore_version: The datastore_version of this Model.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def is_text_model(self):
        r"""Gets the is_text_model of this Model.

        **参数解释**： 是否是文本模型 **取值范围**： 不涉及

        :return: The is_text_model of this Model.
        :rtype: str
        """
        return self._is_text_model

    @is_text_model.setter
    def is_text_model(self, is_text_model):
        r"""Sets the is_text_model of this Model.

        **参数解释**： 是否是文本模型 **取值范围**： 不涉及

        :param is_text_model: The is_text_model of this Model.
        :type is_text_model: str
        """
        self._is_text_model = is_text_model

    @property
    def model_version_id(self):
        r"""Gets the model_version_id of this Model.

        **参数解释**： 模型版本id **取值范围**： 不涉及

        :return: The model_version_id of this Model.
        :rtype: str
        """
        return self._model_version_id

    @model_version_id.setter
    def model_version_id(self, model_version_id):
        r"""Sets the model_version_id of this Model.

        **参数解释**： 模型版本id **取值范围**： 不涉及

        :param model_version_id: The model_version_id of this Model.
        :type model_version_id: str
        """
        self._model_version_id = model_version_id

    @property
    def desc(self):
        r"""Gets the desc of this Model.

        **参数解释**： 模型描述 **取值范围**： 不涉及

        :return: The desc of this Model.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this Model.

        **参数解释**： 模型描述 **取值范围**： 不涉及

        :param desc: The desc of this Model.
        :type desc: str
        """
        self._desc = desc

    @property
    def language(self):
        r"""Gets the language of this Model.

        **参数解释**： 模型语言 **取值范围**： 不涉及

        :return: The language of this Model.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this Model.

        **参数解释**： 模型语言 **取值范围**： 不涉及

        :param language: The language of this Model.
        :type language: str
        """
        self._language = language

    @property
    def arch_type(self):
        r"""Gets the arch_type of this Model.

        **参数解释**： 模型规格 **取值范围**： 不涉及

        :return: The arch_type of this Model.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this Model.

        **参数解释**： 模型规格 **取值范围**： 不涉及

        :param arch_type: The arch_type of this Model.
        :type arch_type: str
        """
        self._arch_type = arch_type

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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
