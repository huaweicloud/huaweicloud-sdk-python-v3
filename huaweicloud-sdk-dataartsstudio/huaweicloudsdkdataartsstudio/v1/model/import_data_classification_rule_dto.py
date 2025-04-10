# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDataClassificationRuleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'classification_type': 'str',
        'secrecy_level': 'str',
        'name': 'str',
        'enable': 'bool',
        'method': 'str',
        'description': 'str',
        'category_id': 'str',
        'builtin_rule_id': 'str',
        'updated_by': 'str',
        'update_at': 'int',
        'created_by': 'str',
        'create_at': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'classification_type': 'classification_type',
        'secrecy_level': 'secrecy_level',
        'name': 'name',
        'enable': 'enable',
        'method': 'method',
        'description': 'description',
        'category_id': 'category_id',
        'builtin_rule_id': 'builtin_rule_id',
        'updated_by': 'updated_by',
        'update_at': 'update_at',
        'created_by': 'created_by',
        'create_at': 'create_at'
    }

    def __init__(self, uuid=None, classification_type=None, secrecy_level=None, name=None, enable=None, method=None, description=None, category_id=None, builtin_rule_id=None, updated_by=None, update_at=None, created_by=None, create_at=None):
        r"""ImportDataClassificationRuleDto

        The model defined in huaweicloud sdk

        :param uuid: 数据识别规则id。
        :type uuid: str
        :param classification_type: 识别规则类型 * BUILTIN 内置 * CUSTOM 自定义
        :type classification_type: str
        :param secrecy_level: 数据密级id。
        :type secrecy_level: str
        :param name: 数据识别规则名称。
        :type name: str
        :param enable: 是否启用。
        :type enable: bool
        :param method: 识别规则类型 * NONE 无 * REGULAR 正则表达式 * DEFAULT 默认
        :type method: str
        :param description: 描述。
        :type description: str
        :param category_id: 数据分类id。
        :type category_id: str
        :param builtin_rule_id: 预置规则id。
        :type builtin_rule_id: str
        :param updated_by: 更新人。
        :type updated_by: str
        :param update_at: 更新时间。
        :type update_at: int
        :param created_by: 创建人。
        :type created_by: str
        :param create_at: 创建时间。
        :type create_at: int
        """
        
        

        self._uuid = None
        self._classification_type = None
        self._secrecy_level = None
        self._name = None
        self._enable = None
        self._method = None
        self._description = None
        self._category_id = None
        self._builtin_rule_id = None
        self._updated_by = None
        self._update_at = None
        self._created_by = None
        self._create_at = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if classification_type is not None:
            self.classification_type = classification_type
        if secrecy_level is not None:
            self.secrecy_level = secrecy_level
        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable
        if method is not None:
            self.method = method
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if builtin_rule_id is not None:
            self.builtin_rule_id = builtin_rule_id
        if updated_by is not None:
            self.updated_by = updated_by
        if update_at is not None:
            self.update_at = update_at
        if created_by is not None:
            self.created_by = created_by
        if create_at is not None:
            self.create_at = create_at

    @property
    def uuid(self):
        r"""Gets the uuid of this ImportDataClassificationRuleDto.

        数据识别规则id。

        :return: The uuid of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ImportDataClassificationRuleDto.

        数据识别规则id。

        :param uuid: The uuid of this ImportDataClassificationRuleDto.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def classification_type(self):
        r"""Gets the classification_type of this ImportDataClassificationRuleDto.

        识别规则类型 * BUILTIN 内置 * CUSTOM 自定义

        :return: The classification_type of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._classification_type

    @classification_type.setter
    def classification_type(self, classification_type):
        r"""Sets the classification_type of this ImportDataClassificationRuleDto.

        识别规则类型 * BUILTIN 内置 * CUSTOM 自定义

        :param classification_type: The classification_type of this ImportDataClassificationRuleDto.
        :type classification_type: str
        """
        self._classification_type = classification_type

    @property
    def secrecy_level(self):
        r"""Gets the secrecy_level of this ImportDataClassificationRuleDto.

        数据密级id。

        :return: The secrecy_level of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._secrecy_level

    @secrecy_level.setter
    def secrecy_level(self, secrecy_level):
        r"""Sets the secrecy_level of this ImportDataClassificationRuleDto.

        数据密级id。

        :param secrecy_level: The secrecy_level of this ImportDataClassificationRuleDto.
        :type secrecy_level: str
        """
        self._secrecy_level = secrecy_level

    @property
    def name(self):
        r"""Gets the name of this ImportDataClassificationRuleDto.

        数据识别规则名称。

        :return: The name of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImportDataClassificationRuleDto.

        数据识别规则名称。

        :param name: The name of this ImportDataClassificationRuleDto.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this ImportDataClassificationRuleDto.

        是否启用。

        :return: The enable of this ImportDataClassificationRuleDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ImportDataClassificationRuleDto.

        是否启用。

        :param enable: The enable of this ImportDataClassificationRuleDto.
        :type enable: bool
        """
        self._enable = enable

    @property
    def method(self):
        r"""Gets the method of this ImportDataClassificationRuleDto.

        识别规则类型 * NONE 无 * REGULAR 正则表达式 * DEFAULT 默认

        :return: The method of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this ImportDataClassificationRuleDto.

        识别规则类型 * NONE 无 * REGULAR 正则表达式 * DEFAULT 默认

        :param method: The method of this ImportDataClassificationRuleDto.
        :type method: str
        """
        self._method = method

    @property
    def description(self):
        r"""Gets the description of this ImportDataClassificationRuleDto.

        描述。

        :return: The description of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImportDataClassificationRuleDto.

        描述。

        :param description: The description of this ImportDataClassificationRuleDto.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        r"""Gets the category_id of this ImportDataClassificationRuleDto.

        数据分类id。

        :return: The category_id of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this ImportDataClassificationRuleDto.

        数据分类id。

        :param category_id: The category_id of this ImportDataClassificationRuleDto.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def builtin_rule_id(self):
        r"""Gets the builtin_rule_id of this ImportDataClassificationRuleDto.

        预置规则id。

        :return: The builtin_rule_id of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._builtin_rule_id

    @builtin_rule_id.setter
    def builtin_rule_id(self, builtin_rule_id):
        r"""Sets the builtin_rule_id of this ImportDataClassificationRuleDto.

        预置规则id。

        :param builtin_rule_id: The builtin_rule_id of this ImportDataClassificationRuleDto.
        :type builtin_rule_id: str
        """
        self._builtin_rule_id = builtin_rule_id

    @property
    def updated_by(self):
        r"""Gets the updated_by of this ImportDataClassificationRuleDto.

        更新人。

        :return: The updated_by of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this ImportDataClassificationRuleDto.

        更新人。

        :param updated_by: The updated_by of this ImportDataClassificationRuleDto.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def update_at(self):
        r"""Gets the update_at of this ImportDataClassificationRuleDto.

        更新时间。

        :return: The update_at of this ImportDataClassificationRuleDto.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ImportDataClassificationRuleDto.

        更新时间。

        :param update_at: The update_at of this ImportDataClassificationRuleDto.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def created_by(self):
        r"""Gets the created_by of this ImportDataClassificationRuleDto.

        创建人。

        :return: The created_by of this ImportDataClassificationRuleDto.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ImportDataClassificationRuleDto.

        创建人。

        :param created_by: The created_by of this ImportDataClassificationRuleDto.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def create_at(self):
        r"""Gets the create_at of this ImportDataClassificationRuleDto.

        创建时间。

        :return: The create_at of this ImportDataClassificationRuleDto.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ImportDataClassificationRuleDto.

        创建时间。

        :param create_at: The create_at of this ImportDataClassificationRuleDto.
        :type create_at: int
        """
        self._create_at = create_at

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
        if not isinstance(other, ImportDataClassificationRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
