# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequestV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'git_url': 'str',
        'git_branch': 'str',
        'language': 'list[str]',
        'rule_sets': 'list[RuleSetV2]',
        'task_type': 'str',
        'username': 'str',
        'access_token': 'str',
        'endpoint_id': 'str',
        'inc_config': 'IncConfigV2',
        'resource_pool_id': 'str',
        'sm_level': 'str',
        'check_type': 'list[str]',
        'enable_fossbot': 'bool'
    }

    attribute_map = {
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'language': 'language',
        'rule_sets': 'rule_sets',
        'task_type': 'task_type',
        'username': 'username',
        'access_token': 'access_token',
        'endpoint_id': 'endpoint_id',
        'inc_config': 'inc_config',
        'resource_pool_id': 'resource_pool_id',
        'sm_level': 'sm_level',
        'check_type': 'check_type',
        'enable_fossbot': 'enable_fossbot'
    }

    def __init__(self, git_url=None, git_branch=None, language=None, rule_sets=None, task_type=None, username=None, access_token=None, endpoint_id=None, inc_config=None, resource_pool_id=None, sm_level=None, check_type=None, enable_fossbot=None):
        r"""CreateTaskRequestV2

        The model defined in huaweicloud sdk

        :param git_url: **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** repo仓传以git开头的地址；非repo仓传以http开头的地址。 **默认取值：** 不涉及。
        :type git_url: str
        :param git_branch: **参数解释：** 计划创建任务的对应代码仓的分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type git_branch: str
        :param language: **参数解释：** 启用的检查语言，数组格式，支持的语言请关注服务更新特性文档。 **约束限制：** 与rule_sets 2选1使用。
        :type language: list[str]
        :param rule_sets: **参数解释：** 启用的规则集，数组格式，当只传语言，不传规则集ID时，与language参数等效，启用这些语言在项目下的默认规则集，支持的语言请关注服务更新特性文档。 **约束限制：** 与language 2选1使用。
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleSetV2`]
        :param task_type: **参数解释：** 任务类型。 **约束限制：** 不涉及。 **取值范围：** - full：代码仓分支对应的全量任务。 - inc：MR增量任务。 **默认取值：** full
        :type task_type: str
        :param username: **参数解释：** 用户名，与access_token联合使用，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type username: str
        :param access_token: **参数解释：** 密码或访问密钥/令牌，username，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type access_token: str
        :param endpoint_id: **参数解释：** 用户预先创建的项目下的代码源扩展点ID，保存了代码仓信息。创建第三方代码源任务，若未填写endpoint，会自动创建扩展点，需要账号有创建扩展点权限，且项目下扩展点未达到上限。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type endpoint_id: str
        :param inc_config: 
        :type inc_config: :class:`huaweicloudsdkcodeartscheck.v2.IncConfigV2`
        :param resource_pool_id: **参数解释：** 用户购买的资源池ID，创建任务时如传此参数，任务将使用对应资源池进行检查。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type resource_pool_id: str
        :param sm_level: **参数解释：** [密级ID,可见信息密级的ID，从页面接口GET https://{endpoint}/projects/v1/options的响应参数中获取，其中的code值即为密级ID。](tag:hcs_sm,hcs_sitesm)[该参数暂无业务意义，传0即可。](tag:fcs) **约束限制：** [租户开启密级功能后必传。](tag:hcs_sm,hcs_sitesm)[不涉及。](tag:fcs) **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type sm_level: str
        :param check_type: **参数解释：** 废弃参数
        :type check_type: list[str]
        :param enable_fossbot: **参数解释：** 废弃参数
        :type enable_fossbot: bool
        """
        
        

        self._git_url = None
        self._git_branch = None
        self._language = None
        self._rule_sets = None
        self._task_type = None
        self._username = None
        self._access_token = None
        self._endpoint_id = None
        self._inc_config = None
        self._resource_pool_id = None
        self._sm_level = None
        self._check_type = None
        self._enable_fossbot = None
        self.discriminator = None

        self.git_url = git_url
        self.git_branch = git_branch
        if language is not None:
            self.language = language
        if rule_sets is not None:
            self.rule_sets = rule_sets
        if task_type is not None:
            self.task_type = task_type
        if username is not None:
            self.username = username
        if access_token is not None:
            self.access_token = access_token
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if inc_config is not None:
            self.inc_config = inc_config
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if sm_level is not None:
            self.sm_level = sm_level
        if check_type is not None:
            self.check_type = check_type
        if enable_fossbot is not None:
            self.enable_fossbot = enable_fossbot

    @property
    def git_url(self):
        r"""Gets the git_url of this CreateTaskRequestV2.

        **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** repo仓传以git开头的地址；非repo仓传以http开头的地址。 **默认取值：** 不涉及。

        :return: The git_url of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this CreateTaskRequestV2.

        **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** repo仓传以git开头的地址；非repo仓传以http开头的地址。 **默认取值：** 不涉及。

        :param git_url: The git_url of this CreateTaskRequestV2.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        r"""Gets the git_branch of this CreateTaskRequestV2.

        **参数解释：** 计划创建任务的对应代码仓的分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The git_branch of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        r"""Sets the git_branch of this CreateTaskRequestV2.

        **参数解释：** 计划创建任务的对应代码仓的分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param git_branch: The git_branch of this CreateTaskRequestV2.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def language(self):
        r"""Gets the language of this CreateTaskRequestV2.

        **参数解释：** 启用的检查语言，数组格式，支持的语言请关注服务更新特性文档。 **约束限制：** 与rule_sets 2选1使用。

        :return: The language of this CreateTaskRequestV2.
        :rtype: list[str]
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateTaskRequestV2.

        **参数解释：** 启用的检查语言，数组格式，支持的语言请关注服务更新特性文档。 **约束限制：** 与rule_sets 2选1使用。

        :param language: The language of this CreateTaskRequestV2.
        :type language: list[str]
        """
        self._language = language

    @property
    def rule_sets(self):
        r"""Gets the rule_sets of this CreateTaskRequestV2.

        **参数解释：** 启用的规则集，数组格式，当只传语言，不传规则集ID时，与language参数等效，启用这些语言在项目下的默认规则集，支持的语言请关注服务更新特性文档。 **约束限制：** 与language 2选1使用。

        :return: The rule_sets of this CreateTaskRequestV2.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleSetV2`]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        r"""Sets the rule_sets of this CreateTaskRequestV2.

        **参数解释：** 启用的规则集，数组格式，当只传语言，不传规则集ID时，与language参数等效，启用这些语言在项目下的默认规则集，支持的语言请关注服务更新特性文档。 **约束限制：** 与language 2选1使用。

        :param rule_sets: The rule_sets of this CreateTaskRequestV2.
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleSetV2`]
        """
        self._rule_sets = rule_sets

    @property
    def task_type(self):
        r"""Gets the task_type of this CreateTaskRequestV2.

        **参数解释：** 任务类型。 **约束限制：** 不涉及。 **取值范围：** - full：代码仓分支对应的全量任务。 - inc：MR增量任务。 **默认取值：** full

        :return: The task_type of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this CreateTaskRequestV2.

        **参数解释：** 任务类型。 **约束限制：** 不涉及。 **取值范围：** - full：代码仓分支对应的全量任务。 - inc：MR增量任务。 **默认取值：** full

        :param task_type: The task_type of this CreateTaskRequestV2.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def username(self):
        r"""Gets the username of this CreateTaskRequestV2.

        **参数解释：** 用户名，与access_token联合使用，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The username of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this CreateTaskRequestV2.

        **参数解释：** 用户名，与access_token联合使用，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param username: The username of this CreateTaskRequestV2.
        :type username: str
        """
        self._username = username

    @property
    def access_token(self):
        r"""Gets the access_token of this CreateTaskRequestV2.

        **参数解释：** 密码或访问密钥/令牌，username，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The access_token of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this CreateTaskRequestV2.

        **参数解释：** 密码或访问密钥/令牌，username，用于在创建三方仓时，由Check服务创建1个通用git扩展点，从而保存代码仓信息。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param access_token: The access_token of this CreateTaskRequestV2.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this CreateTaskRequestV2.

        **参数解释：** 用户预先创建的项目下的代码源扩展点ID，保存了代码仓信息。创建第三方代码源任务，若未填写endpoint，会自动创建扩展点，需要账号有创建扩展点权限，且项目下扩展点未达到上限。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The endpoint_id of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this CreateTaskRequestV2.

        **参数解释：** 用户预先创建的项目下的代码源扩展点ID，保存了代码仓信息。创建第三方代码源任务，若未填写endpoint，会自动创建扩展点，需要账号有创建扩展点权限，且项目下扩展点未达到上限。 **约束限制：** username、access_token组合与endpoint_id 2选1使用。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param endpoint_id: The endpoint_id of this CreateTaskRequestV2.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def inc_config(self):
        r"""Gets the inc_config of this CreateTaskRequestV2.

        :return: The inc_config of this CreateTaskRequestV2.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.IncConfigV2`
        """
        return self._inc_config

    @inc_config.setter
    def inc_config(self, inc_config):
        r"""Sets the inc_config of this CreateTaskRequestV2.

        :param inc_config: The inc_config of this CreateTaskRequestV2.
        :type inc_config: :class:`huaweicloudsdkcodeartscheck.v2.IncConfigV2`
        """
        self._inc_config = inc_config

    @property
    def resource_pool_id(self):
        r"""Gets the resource_pool_id of this CreateTaskRequestV2.

        **参数解释：** 用户购买的资源池ID，创建任务时如传此参数，任务将使用对应资源池进行检查。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The resource_pool_id of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        r"""Sets the resource_pool_id of this CreateTaskRequestV2.

        **参数解释：** 用户购买的资源池ID，创建任务时如传此参数，任务将使用对应资源池进行检查。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param resource_pool_id: The resource_pool_id of this CreateTaskRequestV2.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def sm_level(self):
        r"""Gets the sm_level of this CreateTaskRequestV2.

        **参数解释：** [密级ID,可见信息密级的ID，从页面接口GET https://{endpoint}/projects/v1/options的响应参数中获取，其中的code值即为密级ID。](tag:hcs_sm,hcs_sitesm)[该参数暂无业务意义，传0即可。](tag:fcs) **约束限制：** [租户开启密级功能后必传。](tag:hcs_sm,hcs_sitesm)[不涉及。](tag:fcs) **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The sm_level of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._sm_level

    @sm_level.setter
    def sm_level(self, sm_level):
        r"""Sets the sm_level of this CreateTaskRequestV2.

        **参数解释：** [密级ID,可见信息密级的ID，从页面接口GET https://{endpoint}/projects/v1/options的响应参数中获取，其中的code值即为密级ID。](tag:hcs_sm,hcs_sitesm)[该参数暂无业务意义，传0即可。](tag:fcs) **约束限制：** [租户开启密级功能后必传。](tag:hcs_sm,hcs_sitesm)[不涉及。](tag:fcs) **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param sm_level: The sm_level of this CreateTaskRequestV2.
        :type sm_level: str
        """
        self._sm_level = sm_level

    @property
    def check_type(self):
        r"""Gets the check_type of this CreateTaskRequestV2.

        **参数解释：** 废弃参数

        :return: The check_type of this CreateTaskRequestV2.
        :rtype: list[str]
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this CreateTaskRequestV2.

        **参数解释：** 废弃参数

        :param check_type: The check_type of this CreateTaskRequestV2.
        :type check_type: list[str]
        """
        self._check_type = check_type

    @property
    def enable_fossbot(self):
        r"""Gets the enable_fossbot of this CreateTaskRequestV2.

        **参数解释：** 废弃参数

        :return: The enable_fossbot of this CreateTaskRequestV2.
        :rtype: bool
        """
        return self._enable_fossbot

    @enable_fossbot.setter
    def enable_fossbot(self, enable_fossbot):
        r"""Sets the enable_fossbot of this CreateTaskRequestV2.

        **参数解释：** 废弃参数

        :param enable_fossbot: The enable_fossbot of this CreateTaskRequestV2.
        :type enable_fossbot: bool
        """
        self._enable_fossbot = enable_fossbot

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
        if not isinstance(other, CreateTaskRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
