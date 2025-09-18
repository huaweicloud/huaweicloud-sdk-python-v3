# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStrategyResponse(SdkResponse):

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
        'type': 'str',
        'version': 'str',
        'creator': 'str',
        'create_time': 'str',
        'updater': 'str',
        'update_time': 'str',
        'is_valid': 'bool',
        'rule_instances': 'list[RuleInstance]',
        'level': 'str',
        'is_public': 'bool',
        'is_legacy': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'creator': 'creator',
        'create_time': 'create_time',
        'updater': 'updater',
        'update_time': 'update_time',
        'is_valid': 'is_valid',
        'rule_instances': 'rule_instances',
        'level': 'level',
        'is_public': 'is_public',
        'is_legacy': 'is_legacy'
    }

    def __init__(self, id=None, name=None, type=None, version=None, creator=None, create_time=None, updater=None, update_time=None, is_valid=None, rule_instances=None, level=None, is_public=None, is_legacy=None):
        r"""ShowStrategyResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 规则模板实例ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type id: str
        :param name: **参数解释**： 规则模板实例名称。 **取值范围**： 不涉及。 
        :type name: str
        :param type: **参数解释**： 规则模板类型。 **取值范围**： 不涉及。 
        :type type: str
        :param version: **参数解释**： 规则模板策略。 **取值范围**： 不涉及。 
        :type version: str
        :param creator: **参数解释**： 策略创建人。 **取值范围**： 不涉及。 
        :type creator: str
        :param create_time: **参数解释**： 策略创建时间。 **取值范围**： 不涉及。 
        :type create_time: str
        :param updater: **参数解释**： 策略最近更新人。 **取值范围**： 不涉及。 
        :type updater: str
        :param update_time: **参数解释**： 策略最近更新时间。 **取值范围**： 不涉及。 
        :type update_time: str
        :param is_valid: **参数解释**： 策略是否生效。 **取值范围**： - true：策略生效。 - false：策略不生效。 
        :type is_valid: bool
        :param rule_instances: **参数解释**： 规则实例集合。 **取值范围**： 不涉及。 
        :type rule_instances: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstance`]
        :param level: **参数解释**： 规则实例生效级别。 **取值范围**： 不涉及。 
        :type level: str
        :param is_public: **参数解释**： 规则实例是否系统级。 **取值范围**： - true：规则实例是系统级。 - false：规则实例不是系统级。 
        :type is_public: bool
        :param is_legacy: **参数解释**： 规则实例是1.0的数据。 **取值范围**： - true：规则实例是1.0的数据。 - false：规则实例是1.0的数据。 
        :type is_legacy: bool
        """
        
        super(ShowStrategyResponse, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._version = None
        self._creator = None
        self._create_time = None
        self._updater = None
        self._update_time = None
        self._is_valid = None
        self._rule_instances = None
        self._level = None
        self._is_public = None
        self._is_legacy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if updater is not None:
            self.updater = updater
        if update_time is not None:
            self.update_time = update_time
        if is_valid is not None:
            self.is_valid = is_valid
        if rule_instances is not None:
            self.rule_instances = rule_instances
        if level is not None:
            self.level = level
        if is_public is not None:
            self.is_public = is_public
        if is_legacy is not None:
            self.is_legacy = is_legacy

    @property
    def id(self):
        r"""Gets the id of this ShowStrategyResponse.

        **参数解释**： 规则模板实例ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The id of this ShowStrategyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowStrategyResponse.

        **参数解释**： 规则模板实例ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param id: The id of this ShowStrategyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowStrategyResponse.

        **参数解释**： 规则模板实例名称。 **取值范围**： 不涉及。 

        :return: The name of this ShowStrategyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowStrategyResponse.

        **参数解释**： 规则模板实例名称。 **取值范围**： 不涉及。 

        :param name: The name of this ShowStrategyResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowStrategyResponse.

        **参数解释**： 规则模板类型。 **取值范围**： 不涉及。 

        :return: The type of this ShowStrategyResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowStrategyResponse.

        **参数解释**： 规则模板类型。 **取值范围**： 不涉及。 

        :param type: The type of this ShowStrategyResponse.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ShowStrategyResponse.

        **参数解释**： 规则模板策略。 **取值范围**： 不涉及。 

        :return: The version of this ShowStrategyResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowStrategyResponse.

        **参数解释**： 规则模板策略。 **取值范围**： 不涉及。 

        :param version: The version of this ShowStrategyResponse.
        :type version: str
        """
        self._version = version

    @property
    def creator(self):
        r"""Gets the creator of this ShowStrategyResponse.

        **参数解释**： 策略创建人。 **取值范围**： 不涉及。 

        :return: The creator of this ShowStrategyResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowStrategyResponse.

        **参数解释**： 策略创建人。 **取值范围**： 不涉及。 

        :param creator: The creator of this ShowStrategyResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowStrategyResponse.

        **参数解释**： 策略创建时间。 **取值范围**： 不涉及。 

        :return: The create_time of this ShowStrategyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowStrategyResponse.

        **参数解释**： 策略创建时间。 **取值范围**： 不涉及。 

        :param create_time: The create_time of this ShowStrategyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def updater(self):
        r"""Gets the updater of this ShowStrategyResponse.

        **参数解释**： 策略最近更新人。 **取值范围**： 不涉及。 

        :return: The updater of this ShowStrategyResponse.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this ShowStrategyResponse.

        **参数解释**： 策略最近更新人。 **取值范围**： 不涉及。 

        :param updater: The updater of this ShowStrategyResponse.
        :type updater: str
        """
        self._updater = updater

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowStrategyResponse.

        **参数解释**： 策略最近更新时间。 **取值范围**： 不涉及。 

        :return: The update_time of this ShowStrategyResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowStrategyResponse.

        **参数解释**： 策略最近更新时间。 **取值范围**： 不涉及。 

        :param update_time: The update_time of this ShowStrategyResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def is_valid(self):
        r"""Gets the is_valid of this ShowStrategyResponse.

        **参数解释**： 策略是否生效。 **取值范围**： - true：策略生效。 - false：策略不生效。 

        :return: The is_valid of this ShowStrategyResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this ShowStrategyResponse.

        **参数解释**： 策略是否生效。 **取值范围**： - true：策略生效。 - false：策略不生效。 

        :param is_valid: The is_valid of this ShowStrategyResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def rule_instances(self):
        r"""Gets the rule_instances of this ShowStrategyResponse.

        **参数解释**： 规则实例集合。 **取值范围**： 不涉及。 

        :return: The rule_instances of this ShowStrategyResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstance`]
        """
        return self._rule_instances

    @rule_instances.setter
    def rule_instances(self, rule_instances):
        r"""Sets the rule_instances of this ShowStrategyResponse.

        **参数解释**： 规则实例集合。 **取值范围**： 不涉及。 

        :param rule_instances: The rule_instances of this ShowStrategyResponse.
        :type rule_instances: list[:class:`huaweicloudsdkcodeartspipeline.v2.RuleInstance`]
        """
        self._rule_instances = rule_instances

    @property
    def level(self):
        r"""Gets the level of this ShowStrategyResponse.

        **参数解释**： 规则实例生效级别。 **取值范围**： 不涉及。 

        :return: The level of this ShowStrategyResponse.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowStrategyResponse.

        **参数解释**： 规则实例生效级别。 **取值范围**： 不涉及。 

        :param level: The level of this ShowStrategyResponse.
        :type level: str
        """
        self._level = level

    @property
    def is_public(self):
        r"""Gets the is_public of this ShowStrategyResponse.

        **参数解释**： 规则实例是否系统级。 **取值范围**： - true：规则实例是系统级。 - false：规则实例不是系统级。 

        :return: The is_public of this ShowStrategyResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this ShowStrategyResponse.

        **参数解释**： 规则实例是否系统级。 **取值范围**： - true：规则实例是系统级。 - false：规则实例不是系统级。 

        :param is_public: The is_public of this ShowStrategyResponse.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def is_legacy(self):
        r"""Gets the is_legacy of this ShowStrategyResponse.

        **参数解释**： 规则实例是1.0的数据。 **取值范围**： - true：规则实例是1.0的数据。 - false：规则实例是1.0的数据。 

        :return: The is_legacy of this ShowStrategyResponse.
        :rtype: bool
        """
        return self._is_legacy

    @is_legacy.setter
    def is_legacy(self, is_legacy):
        r"""Sets the is_legacy of this ShowStrategyResponse.

        **参数解释**： 规则实例是1.0的数据。 **取值范围**： - true：规则实例是1.0的数据。 - false：规则实例是1.0的数据。 

        :param is_legacy: The is_legacy of this ShowStrategyResponse.
        :type is_legacy: bool
        """
        self._is_legacy = is_legacy

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
        if not isinstance(other, ShowStrategyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
