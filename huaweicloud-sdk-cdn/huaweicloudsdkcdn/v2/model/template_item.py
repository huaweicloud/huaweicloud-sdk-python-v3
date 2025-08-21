# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'tml_name': 'str',
        'remark': 'str',
        'tml_id': 'str',
        'type': 'int',
        'create_time': 'int',
        'modify_time': 'int',
        'configs': 'TemplateConfigs'
    }

    attribute_map = {
        'account_id': 'account_id',
        'tml_name': 'tml_name',
        'remark': 'remark',
        'tml_id': 'tml_id',
        'type': 'type',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'configs': 'configs'
    }

    def __init__(self, account_id=None, tml_name=None, remark=None, tml_id=None, type=None, create_time=None, modify_time=None, configs=None):
        r"""TemplateItem

        The model defined in huaweicloud sdk

        :param account_id: **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type account_id: str
        :param tml_name: **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及
        :type tml_name: str
        :param remark: **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type remark: str
        :param tml_id: **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tml_id: str
        :param type: **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及
        :type type: int
        :param create_time: **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type create_time: int
        :param modify_time: **参数解释：** 修改时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type modify_time: int
        :param configs: 
        :type configs: TemplateConfigs
        """
        
        

        self._account_id = None
        self._tml_name = None
        self._remark = None
        self._tml_id = None
        self._type = None
        self._create_time = None
        self._modify_time = None
        self._configs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if tml_name is not None:
            self.tml_name = tml_name
        if remark is not None:
            self.remark = remark
        if tml_id is not None:
            self.tml_id = tml_id
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if configs is not None:
            self.configs = configs

    @property
    def account_id(self):
        r"""Gets the account_id of this TemplateItem.

        **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The account_id of this TemplateItem.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this TemplateItem.

        **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param account_id: The account_id of this TemplateItem.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def tml_name(self):
        r"""Gets the tml_name of this TemplateItem.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :return: The tml_name of this TemplateItem.
        :rtype: str
        """
        return self._tml_name

    @tml_name.setter
    def tml_name(self, tml_name):
        r"""Sets the tml_name of this TemplateItem.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :param tml_name: The tml_name of this TemplateItem.
        :type tml_name: str
        """
        self._tml_name = tml_name

    @property
    def remark(self):
        r"""Gets the remark of this TemplateItem.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The remark of this TemplateItem.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this TemplateItem.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param remark: The remark of this TemplateItem.
        :type remark: str
        """
        self._remark = remark

    @property
    def tml_id(self):
        r"""Gets the tml_id of this TemplateItem.

        **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tml_id of this TemplateItem.
        :rtype: str
        """
        return self._tml_id

    @tml_id.setter
    def tml_id(self, tml_id):
        r"""Sets the tml_id of this TemplateItem.

        **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tml_id: The tml_id of this TemplateItem.
        :type tml_id: str
        """
        self._tml_id = tml_id

    @property
    def type(self):
        r"""Gets the type of this TemplateItem.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :return: The type of this TemplateItem.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateItem.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :param type: The type of this TemplateItem.
        :type type: int
        """
        self._type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this TemplateItem.

        **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The create_time of this TemplateItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TemplateItem.

        **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param create_time: The create_time of this TemplateItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this TemplateItem.

        **参数解释：** 修改时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The modify_time of this TemplateItem.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this TemplateItem.

        **参数解释：** 修改时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param modify_time: The modify_time of this TemplateItem.
        :type modify_time: int
        """
        self._modify_time = modify_time

    @property
    def configs(self):
        r"""Gets the configs of this TemplateItem.

        :return: The configs of this TemplateItem.
        :rtype: TemplateConfigs
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this TemplateItem.

        :param configs: The configs of this TemplateItem.
        :type configs: TemplateConfigs
        """
        self._configs = configs

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
        if not isinstance(other, TemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
