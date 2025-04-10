# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDefaultRuleResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_status': 'str',
        'import_error_message': 'str',
        'uuid': 'str',
        'import_data_classification_rule': 'ImportDataClassificationRuleDto',
        'rule_name': 'str',
        'rule_type': 'str',
        'rule_desc': 'str',
        'rule_name_en': 'str',
        'rule_desc_en': 'str',
        'country': 'str'
    }

    attribute_map = {
        'import_status': 'import_status',
        'import_error_message': 'import_error_message',
        'uuid': 'uuid',
        'import_data_classification_rule': 'import_data_classification_rule',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type',
        'rule_desc': 'rule_desc',
        'rule_name_en': 'rule_name_en',
        'rule_desc_en': 'rule_desc_en',
        'country': 'country'
    }

    def __init__(self, import_status=None, import_error_message=None, uuid=None, import_data_classification_rule=None, rule_name=None, rule_type=None, rule_desc=None, rule_name_en=None, rule_desc_en=None, country=None):
        r"""ImportDefaultRuleResultDto

        The model defined in huaweicloud sdk

        :param import_status: 导入状态 * success 导入成功 * failed 导入失败
        :type import_status: str
        :param import_error_message: 导入错误原因。
        :type import_error_message: str
        :param uuid: 内置规则模板id。
        :type uuid: str
        :param import_data_classification_rule: 
        :type import_data_classification_rule: :class:`huaweicloudsdkdataartsstudio.v1.ImportDataClassificationRuleDto`
        :param rule_name: 数据识别规则名称。
        :type rule_name: str
        :param rule_type: 数据识别规则类型 * REGEX 正则表达式 * KEYWORD 关键字
        :type rule_type: str
        :param rule_desc: 规则描述。
        :type rule_desc: str
        :param rule_name_en: 英文名称。
        :type rule_name_en: str
        :param rule_desc_en: 英文描述。
        :type rule_desc_en: str
        :param country: 规则所属地区。
        :type country: str
        """
        
        

        self._import_status = None
        self._import_error_message = None
        self._uuid = None
        self._import_data_classification_rule = None
        self._rule_name = None
        self._rule_type = None
        self._rule_desc = None
        self._rule_name_en = None
        self._rule_desc_en = None
        self._country = None
        self.discriminator = None

        if import_status is not None:
            self.import_status = import_status
        if import_error_message is not None:
            self.import_error_message = import_error_message
        if uuid is not None:
            self.uuid = uuid
        if import_data_classification_rule is not None:
            self.import_data_classification_rule = import_data_classification_rule
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_type is not None:
            self.rule_type = rule_type
        if rule_desc is not None:
            self.rule_desc = rule_desc
        if rule_name_en is not None:
            self.rule_name_en = rule_name_en
        if rule_desc_en is not None:
            self.rule_desc_en = rule_desc_en
        if country is not None:
            self.country = country

    @property
    def import_status(self):
        r"""Gets the import_status of this ImportDefaultRuleResultDto.

        导入状态 * success 导入成功 * failed 导入失败

        :return: The import_status of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        r"""Sets the import_status of this ImportDefaultRuleResultDto.

        导入状态 * success 导入成功 * failed 导入失败

        :param import_status: The import_status of this ImportDefaultRuleResultDto.
        :type import_status: str
        """
        self._import_status = import_status

    @property
    def import_error_message(self):
        r"""Gets the import_error_message of this ImportDefaultRuleResultDto.

        导入错误原因。

        :return: The import_error_message of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._import_error_message

    @import_error_message.setter
    def import_error_message(self, import_error_message):
        r"""Sets the import_error_message of this ImportDefaultRuleResultDto.

        导入错误原因。

        :param import_error_message: The import_error_message of this ImportDefaultRuleResultDto.
        :type import_error_message: str
        """
        self._import_error_message = import_error_message

    @property
    def uuid(self):
        r"""Gets the uuid of this ImportDefaultRuleResultDto.

        内置规则模板id。

        :return: The uuid of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ImportDefaultRuleResultDto.

        内置规则模板id。

        :param uuid: The uuid of this ImportDefaultRuleResultDto.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def import_data_classification_rule(self):
        r"""Gets the import_data_classification_rule of this ImportDefaultRuleResultDto.

        :return: The import_data_classification_rule of this ImportDefaultRuleResultDto.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ImportDataClassificationRuleDto`
        """
        return self._import_data_classification_rule

    @import_data_classification_rule.setter
    def import_data_classification_rule(self, import_data_classification_rule):
        r"""Sets the import_data_classification_rule of this ImportDefaultRuleResultDto.

        :param import_data_classification_rule: The import_data_classification_rule of this ImportDefaultRuleResultDto.
        :type import_data_classification_rule: :class:`huaweicloudsdkdataartsstudio.v1.ImportDataClassificationRuleDto`
        """
        self._import_data_classification_rule = import_data_classification_rule

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ImportDefaultRuleResultDto.

        数据识别规则名称。

        :return: The rule_name of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ImportDefaultRuleResultDto.

        数据识别规则名称。

        :param rule_name: The rule_name of this ImportDefaultRuleResultDto.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ImportDefaultRuleResultDto.

        数据识别规则类型 * REGEX 正则表达式 * KEYWORD 关键字

        :return: The rule_type of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ImportDefaultRuleResultDto.

        数据识别规则类型 * REGEX 正则表达式 * KEYWORD 关键字

        :param rule_type: The rule_type of this ImportDefaultRuleResultDto.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def rule_desc(self):
        r"""Gets the rule_desc of this ImportDefaultRuleResultDto.

        规则描述。

        :return: The rule_desc of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        r"""Sets the rule_desc of this ImportDefaultRuleResultDto.

        规则描述。

        :param rule_desc: The rule_desc of this ImportDefaultRuleResultDto.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

    @property
    def rule_name_en(self):
        r"""Gets the rule_name_en of this ImportDefaultRuleResultDto.

        英文名称。

        :return: The rule_name_en of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._rule_name_en

    @rule_name_en.setter
    def rule_name_en(self, rule_name_en):
        r"""Sets the rule_name_en of this ImportDefaultRuleResultDto.

        英文名称。

        :param rule_name_en: The rule_name_en of this ImportDefaultRuleResultDto.
        :type rule_name_en: str
        """
        self._rule_name_en = rule_name_en

    @property
    def rule_desc_en(self):
        r"""Gets the rule_desc_en of this ImportDefaultRuleResultDto.

        英文描述。

        :return: The rule_desc_en of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._rule_desc_en

    @rule_desc_en.setter
    def rule_desc_en(self, rule_desc_en):
        r"""Sets the rule_desc_en of this ImportDefaultRuleResultDto.

        英文描述。

        :param rule_desc_en: The rule_desc_en of this ImportDefaultRuleResultDto.
        :type rule_desc_en: str
        """
        self._rule_desc_en = rule_desc_en

    @property
    def country(self):
        r"""Gets the country of this ImportDefaultRuleResultDto.

        规则所属地区。

        :return: The country of this ImportDefaultRuleResultDto.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ImportDefaultRuleResultDto.

        规则所属地区。

        :param country: The country of this ImportDefaultRuleResultDto.
        :type country: str
        """
        self._country = country

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
        if not isinstance(other, ImportDefaultRuleResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
