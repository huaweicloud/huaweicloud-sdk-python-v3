# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DictionaryCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'dict_id': 'str',
        'dict_key': 'str',
        'dict_code': 'str',
        'dict_val': 'str',
        'dict_pkey': 'str',
        'dict_pcode': 'str',
        'scope': 'str',
        'description': 'str',
        'extend_field': 'object',
        'language': 'str'
    }

    attribute_map = {
        'version': 'version',
        'dict_id': 'dict_id',
        'dict_key': 'dict_key',
        'dict_code': 'dict_code',
        'dict_val': 'dict_val',
        'dict_pkey': 'dict_pkey',
        'dict_pcode': 'dict_pcode',
        'scope': 'scope',
        'description': 'description',
        'extend_field': 'extend_field',
        'language': 'language'
    }

    def __init__(self, version=None, dict_id=None, dict_key=None, dict_code=None, dict_val=None, dict_pkey=None, dict_pcode=None, scope=None, description=None, extend_field=None, language=None):
        r"""DictionaryCreate

        The model defined in huaweicloud sdk

        :param version: 版本号
        :type version: str
        :param dict_id: 字典id
        :type dict_id: str
        :param dict_key: 字典key
        :type dict_key: str
        :param dict_code: 字典code码
        :type dict_code: str
        :param dict_val: 字典值
        :type dict_val: str
        :param dict_pkey: 字典key
        :type dict_pkey: str
        :param dict_pcode: 字典关联的父code
        :type dict_pcode: str
        :param scope: 字典所属领域
        :type scope: str
        :param description: 字典描述信息
        :type description: str
        :param extend_field: 额外字段
        :type extend_field: object
        :param language: 用户当前语言环境
        :type language: str
        """
        
        

        self._version = None
        self._dict_id = None
        self._dict_key = None
        self._dict_code = None
        self._dict_val = None
        self._dict_pkey = None
        self._dict_pcode = None
        self._scope = None
        self._description = None
        self._extend_field = None
        self._language = None
        self.discriminator = None

        if version is not None:
            self.version = version
        self.dict_id = dict_id
        self.dict_key = dict_key
        self.dict_code = dict_code
        self.dict_val = dict_val
        if dict_pkey is not None:
            self.dict_pkey = dict_pkey
        if dict_pcode is not None:
            self.dict_pcode = dict_pcode
        if scope is not None:
            self.scope = scope
        if description is not None:
            self.description = description
        if extend_field is not None:
            self.extend_field = extend_field
        self.language = language

    @property
    def version(self):
        r"""Gets the version of this DictionaryCreate.

        版本号

        :return: The version of this DictionaryCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DictionaryCreate.

        版本号

        :param version: The version of this DictionaryCreate.
        :type version: str
        """
        self._version = version

    @property
    def dict_id(self):
        r"""Gets the dict_id of this DictionaryCreate.

        字典id

        :return: The dict_id of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_id

    @dict_id.setter
    def dict_id(self, dict_id):
        r"""Sets the dict_id of this DictionaryCreate.

        字典id

        :param dict_id: The dict_id of this DictionaryCreate.
        :type dict_id: str
        """
        self._dict_id = dict_id

    @property
    def dict_key(self):
        r"""Gets the dict_key of this DictionaryCreate.

        字典key

        :return: The dict_key of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_key

    @dict_key.setter
    def dict_key(self, dict_key):
        r"""Sets the dict_key of this DictionaryCreate.

        字典key

        :param dict_key: The dict_key of this DictionaryCreate.
        :type dict_key: str
        """
        self._dict_key = dict_key

    @property
    def dict_code(self):
        r"""Gets the dict_code of this DictionaryCreate.

        字典code码

        :return: The dict_code of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        r"""Sets the dict_code of this DictionaryCreate.

        字典code码

        :param dict_code: The dict_code of this DictionaryCreate.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def dict_val(self):
        r"""Gets the dict_val of this DictionaryCreate.

        字典值

        :return: The dict_val of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_val

    @dict_val.setter
    def dict_val(self, dict_val):
        r"""Sets the dict_val of this DictionaryCreate.

        字典值

        :param dict_val: The dict_val of this DictionaryCreate.
        :type dict_val: str
        """
        self._dict_val = dict_val

    @property
    def dict_pkey(self):
        r"""Gets the dict_pkey of this DictionaryCreate.

        字典key

        :return: The dict_pkey of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_pkey

    @dict_pkey.setter
    def dict_pkey(self, dict_pkey):
        r"""Sets the dict_pkey of this DictionaryCreate.

        字典key

        :param dict_pkey: The dict_pkey of this DictionaryCreate.
        :type dict_pkey: str
        """
        self._dict_pkey = dict_pkey

    @property
    def dict_pcode(self):
        r"""Gets the dict_pcode of this DictionaryCreate.

        字典关联的父code

        :return: The dict_pcode of this DictionaryCreate.
        :rtype: str
        """
        return self._dict_pcode

    @dict_pcode.setter
    def dict_pcode(self, dict_pcode):
        r"""Sets the dict_pcode of this DictionaryCreate.

        字典关联的父code

        :param dict_pcode: The dict_pcode of this DictionaryCreate.
        :type dict_pcode: str
        """
        self._dict_pcode = dict_pcode

    @property
    def scope(self):
        r"""Gets the scope of this DictionaryCreate.

        字典所属领域

        :return: The scope of this DictionaryCreate.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this DictionaryCreate.

        字典所属领域

        :param scope: The scope of this DictionaryCreate.
        :type scope: str
        """
        self._scope = scope

    @property
    def description(self):
        r"""Gets the description of this DictionaryCreate.

        字典描述信息

        :return: The description of this DictionaryCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DictionaryCreate.

        字典描述信息

        :param description: The description of this DictionaryCreate.
        :type description: str
        """
        self._description = description

    @property
    def extend_field(self):
        r"""Gets the extend_field of this DictionaryCreate.

        额外字段

        :return: The extend_field of this DictionaryCreate.
        :rtype: object
        """
        return self._extend_field

    @extend_field.setter
    def extend_field(self, extend_field):
        r"""Sets the extend_field of this DictionaryCreate.

        额外字段

        :param extend_field: The extend_field of this DictionaryCreate.
        :type extend_field: object
        """
        self._extend_field = extend_field

    @property
    def language(self):
        r"""Gets the language of this DictionaryCreate.

        用户当前语言环境

        :return: The language of this DictionaryCreate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this DictionaryCreate.

        用户当前语言环境

        :param language: The language of this DictionaryCreate.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, DictionaryCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
