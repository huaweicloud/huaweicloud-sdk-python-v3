# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'operator_id': 'str',
        'tml_name': 'str',
        'remark': 'str',
        'tml_id': 'str',
        'apply_time': 'int',
        'type': 'int',
        'account_id': 'str',
        'resources': 'list[Resource]',
        'configs': 'TemplateConfigs'
    }

    attribute_map = {
        'status': 'status',
        'operator_id': 'operator_id',
        'tml_name': 'tml_name',
        'remark': 'remark',
        'tml_id': 'tml_id',
        'apply_time': 'apply_time',
        'type': 'type',
        'account_id': 'account_id',
        'resources': 'resources',
        'configs': 'configs'
    }

    def __init__(self, status=None, operator_id=None, tml_name=None, remark=None, tml_id=None, apply_time=None, type=None, account_id=None, resources=None, configs=None):
        r"""ApplyRecord

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 应用模板结果 **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及
        :type status: str
        :param operator_id: **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type operator_id: str
        :param tml_name: **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及
        :type tml_name: str
        :param remark: **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type remark: str
        :param tml_id: **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tml_id: str
        :param apply_time: **参数解释：** 域名模板应用时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type apply_time: int
        :param type: **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及
        :type type: int
        :param account_id: **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type account_id: str
        :param resources: 
        :type resources: list[:class:`huaweicloudsdkcdn.v2.Resource`]
        :param configs: 
        :type configs: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
        """
        
        

        self._status = None
        self._operator_id = None
        self._tml_name = None
        self._remark = None
        self._tml_id = None
        self._apply_time = None
        self._type = None
        self._account_id = None
        self._resources = None
        self._configs = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if operator_id is not None:
            self.operator_id = operator_id
        if tml_name is not None:
            self.tml_name = tml_name
        if remark is not None:
            self.remark = remark
        if tml_id is not None:
            self.tml_id = tml_id
        if apply_time is not None:
            self.apply_time = apply_time
        if type is not None:
            self.type = type
        if account_id is not None:
            self.account_id = account_id
        if resources is not None:
            self.resources = resources
        if configs is not None:
            self.configs = configs

    @property
    def status(self):
        r"""Gets the status of this ApplyRecord.

        **参数解释：** 应用模板结果 **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :return: The status of this ApplyRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApplyRecord.

        **参数解释：** 应用模板结果 **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :param status: The status of this ApplyRecord.
        :type status: str
        """
        self._status = status

    @property
    def operator_id(self):
        r"""Gets the operator_id of this ApplyRecord.

        **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The operator_id of this ApplyRecord.
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        r"""Sets the operator_id of this ApplyRecord.

        **参数解释：** 操作ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param operator_id: The operator_id of this ApplyRecord.
        :type operator_id: str
        """
        self._operator_id = operator_id

    @property
    def tml_name(self):
        r"""Gets the tml_name of this ApplyRecord.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :return: The tml_name of this ApplyRecord.
        :rtype: str
        """
        return self._tml_name

    @tml_name.setter
    def tml_name(self, tml_name):
        r"""Sets the tml_name of this ApplyRecord.

        **参数解释：** 域名模板名称 **约束限制：** 不涉及 **取值范围：** - 1-100个字符 - 仅支持字母、数字、中文、下划线（_）、中横线（-） **默认取值：** 不涉及

        :param tml_name: The tml_name of this ApplyRecord.
        :type tml_name: str
        """
        self._tml_name = tml_name

    @property
    def remark(self):
        r"""Gets the remark of this ApplyRecord.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The remark of this ApplyRecord.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ApplyRecord.

        **参数解释：** 域名模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param remark: The remark of this ApplyRecord.
        :type remark: str
        """
        self._remark = remark

    @property
    def tml_id(self):
        r"""Gets the tml_id of this ApplyRecord.

        **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tml_id of this ApplyRecord.
        :rtype: str
        """
        return self._tml_id

    @tml_id.setter
    def tml_id(self, tml_id):
        r"""Sets the tml_id of this ApplyRecord.

        **参数解释：** 域名模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tml_id: The tml_id of this ApplyRecord.
        :type tml_id: str
        """
        self._tml_id = tml_id

    @property
    def apply_time(self):
        r"""Gets the apply_time of this ApplyRecord.

        **参数解释：** 域名模板应用时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The apply_time of this ApplyRecord.
        :rtype: int
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        r"""Sets the apply_time of this ApplyRecord.

        **参数解释：** 域名模板应用时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param apply_time: The apply_time of this ApplyRecord.
        :type apply_time: int
        """
        self._apply_time = apply_time

    @property
    def type(self):
        r"""Gets the type of this ApplyRecord.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :return: The type of this ApplyRecord.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ApplyRecord.

        **参数解释：** 域名模板类型 **约束限制：** 不涉及 **取值范围：** - 1: 系统预置模板 - 2: 租户自定义模板 **默认取值：** 不涉及

        :param type: The type of this ApplyRecord.
        :type type: int
        """
        self._type = type

    @property
    def account_id(self):
        r"""Gets the account_id of this ApplyRecord.

        **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The account_id of this ApplyRecord.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ApplyRecord.

        **参数解释：** 账户ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param account_id: The account_id of this ApplyRecord.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def resources(self):
        r"""Gets the resources of this ApplyRecord.

        :return: The resources of this ApplyRecord.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ApplyRecord.

        :param resources: The resources of this ApplyRecord.
        :type resources: list[:class:`huaweicloudsdkcdn.v2.Resource`]
        """
        self._resources = resources

    @property
    def configs(self):
        r"""Gets the configs of this ApplyRecord.

        :return: The configs of this ApplyRecord.
        :rtype: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this ApplyRecord.

        :param configs: The configs of this ApplyRecord.
        :type configs: :class:`huaweicloudsdkcdn.v2.TemplateConfigs`
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
        if not isinstance(other, ApplyRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
