# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTaskParameterBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_id': 'int',
        'ruleset_id': 'str',
        'language': 'str',
        'status': 'str',
        'task_check_settings': 'list[TaskCheckSettingsItem]'
    }

    attribute_map = {
        'check_id': 'check_id',
        'ruleset_id': 'ruleset_id',
        'language': 'language',
        'status': 'status',
        'task_check_settings': 'task_check_settings'
    }

    def __init__(self, check_id=None, ruleset_id=None, language=None, status=None, task_check_settings=None):
        r"""ConfigTaskParameterBody

        The model defined in huaweicloud sdk

        :param check_id: **参数解释：** 参数已废弃，默认填写0即可。 **约束限制:** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type check_id: int
        :param ruleset_id: **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集ID，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值：** 不涉及。
        :type ruleset_id: str
        :param language: **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集对应语言，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID对应的语言。 **约束限制:** 不涉及。 **取值范围:** 与ruleset_id规则集的语言对应。 **默认取值：** 不涉及。
        :type language: str
        :param status: **参数解释:** 当前规则集对应的编译配置总开关。 **约束限制:** 不涉及。 **取值范围:** - off：关闭。 - on：打开。 **默认取值：** 不涉及。
        :type status: str
        :param task_check_settings: **参数解释:** 数组类型，当前规则集对应编译配置具体详情，可基于web页面查看当前规则集所涉及的编译配置，多个参数配置多条即可。 **约束限制:** 不涉及。
        :type task_check_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        
        

        self._check_id = None
        self._ruleset_id = None
        self._language = None
        self._status = None
        self._task_check_settings = None
        self.discriminator = None

        self.check_id = check_id
        self.ruleset_id = ruleset_id
        self.language = language
        self.status = status
        if task_check_settings is not None:
            self.task_check_settings = task_check_settings

    @property
    def check_id(self):
        r"""Gets the check_id of this ConfigTaskParameterBody.

        **参数解释：** 参数已废弃，默认填写0即可。 **约束限制:** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The check_id of this ConfigTaskParameterBody.
        :rtype: int
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        r"""Sets the check_id of this ConfigTaskParameterBody.

        **参数解释：** 参数已废弃，默认填写0即可。 **约束限制:** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param check_id: The check_id of this ConfigTaskParameterBody.
        :type check_id: int
        """
        self._check_id = check_id

    @property
    def ruleset_id(self):
        r"""Gets the ruleset_id of this ConfigTaskParameterBody.

        **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集ID，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :return: The ruleset_id of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        r"""Sets the ruleset_id of this ConfigTaskParameterBody.

        **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集ID，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :param ruleset_id: The ruleset_id of this ConfigTaskParameterBody.
        :type ruleset_id: str
        """
        self._ruleset_id = ruleset_id

    @property
    def language(self):
        r"""Gets the language of this ConfigTaskParameterBody.

        **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集对应语言，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID对应的语言。 **约束限制:** 不涉及。 **取值范围:** 与ruleset_id规则集的语言对应。 **默认取值：** 不涉及。

        :return: The language of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ConfigTaskParameterBody.

        **参数解释:** 兼容历史版本的废弃参数，不校验真实性。规则集对应语言，通过[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口可获取到规则集ID对应的语言。 **约束限制:** 不涉及。 **取值范围:** 与ruleset_id规则集的语言对应。 **默认取值：** 不涉及。

        :param language: The language of this ConfigTaskParameterBody.
        :type language: str
        """
        self._language = language

    @property
    def status(self):
        r"""Gets the status of this ConfigTaskParameterBody.

        **参数解释:** 当前规则集对应的编译配置总开关。 **约束限制:** 不涉及。 **取值范围:** - off：关闭。 - on：打开。 **默认取值：** 不涉及。

        :return: The status of this ConfigTaskParameterBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConfigTaskParameterBody.

        **参数解释:** 当前规则集对应的编译配置总开关。 **约束限制:** 不涉及。 **取值范围:** - off：关闭。 - on：打开。 **默认取值：** 不涉及。

        :param status: The status of this ConfigTaskParameterBody.
        :type status: str
        """
        self._status = status

    @property
    def task_check_settings(self):
        r"""Gets the task_check_settings of this ConfigTaskParameterBody.

        **参数解释:** 数组类型，当前规则集对应编译配置具体详情，可基于web页面查看当前规则集所涉及的编译配置，多个参数配置多条即可。 **约束限制:** 不涉及。

        :return: The task_check_settings of this ConfigTaskParameterBody.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        return self._task_check_settings

    @task_check_settings.setter
    def task_check_settings(self, task_check_settings):
        r"""Sets the task_check_settings of this ConfigTaskParameterBody.

        **参数解释:** 数组类型，当前规则集对应编译配置具体详情，可基于web页面查看当前规则集所涉及的编译配置，多个参数配置多条即可。 **约束限制:** 不涉及。

        :param task_check_settings: The task_check_settings of this ConfigTaskParameterBody.
        :type task_check_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskCheckSettingsItem`]
        """
        self._task_check_settings = task_check_settings

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
        if not isinstance(other, ConfigTaskParameterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
