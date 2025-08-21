# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupSettingsInheritCfgResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_update': 'bool',
        'id': 'int',
        'product_id': 'str',
        'namespace_id': 'int',
        'parent_id': 'int',
        'ownership': 'int',
        'pbi': 'int',
        'protected_branches': 'int',
        'protected_tags': 'int',
        'push_rules': 'int',
        'change_requests': 'int',
        'custom_ctrl_items': 'int',
        'reviews': 'int',
        'issues': 'int',
        'cr_evaluation': 'int',
        'e2e_settings': 'int',
        'committer_settings': 'int',
        'webhook_settings': 'int',
        'stream_event_settings': 'int',
        'pipeline_settings': 'int',
        'issue_templates': 'int',
        'cr_comment_emplates': 'int',
        'merge_requests': 'int',
        'mr_branch_policies': 'int',
        'repository_settings': 'int',
        'deploy_keys': 'int',
        'watermark': 'int',
        'created_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'can_update': 'can_update',
        'id': 'id',
        'product_id': 'product_id',
        'namespace_id': 'namespace_id',
        'parent_id': 'parent_id',
        'ownership': 'ownership',
        'pbi': 'pbi',
        'protected_branches': 'protected_branches',
        'protected_tags': 'protected_tags',
        'push_rules': 'push_rules',
        'change_requests': 'change_requests',
        'custom_ctrl_items': 'custom_ctrl_items',
        'reviews': 'reviews',
        'issues': 'issues',
        'cr_evaluation': 'cr_evaluation',
        'e2e_settings': 'e2e_settings',
        'committer_settings': 'committer_settings',
        'webhook_settings': 'webhook_settings',
        'stream_event_settings': 'stream_event_settings',
        'pipeline_settings': 'pipeline_settings',
        'issue_templates': 'issue_templates',
        'cr_comment_emplates': 'cr_comment_emplates',
        'merge_requests': 'merge_requests',
        'mr_branch_policies': 'mr_branch_policies',
        'repository_settings': 'repository_settings',
        'deploy_keys': 'deploy_keys',
        'watermark': 'watermark',
        'created_at': 'created_at',
        'update_at': 'update_at'
    }

    def __init__(self, can_update=None, id=None, product_id=None, namespace_id=None, parent_id=None, ownership=None, pbi=None, protected_branches=None, protected_tags=None, push_rules=None, change_requests=None, custom_ctrl_items=None, reviews=None, issues=None, cr_evaluation=None, e2e_settings=None, committer_settings=None, webhook_settings=None, stream_event_settings=None, pipeline_settings=None, issue_templates=None, cr_comment_emplates=None, merge_requests=None, mr_branch_policies=None, repository_settings=None, deploy_keys=None, watermark=None, created_at=None, update_at=None):
        r"""ShowGroupSettingsInheritCfgResponse

        The model defined in huaweicloud sdk

        :param can_update: **参数解释：** 是否可用。
        :type can_update: bool
        :param id: **参数解释：** 记录id。
        :type id: int
        :param product_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type product_id: str
        :param namespace_id: **参数解释：** 代码组id。
        :type namespace_id: int
        :param parent_id: **参数解释：** 父id。
        :type parent_id: int
        :param ownership: **参数解释：** 排序id。
        :type ownership: int
        :param pbi: **参数解释：** 排序id。
        :type pbi: int
        :param protected_branches: **参数解释：** 保护分支策略。
        :type protected_branches: int
        :param protected_tags: **参数解释：** 保护tag策略。
        :type protected_tags: int
        :param push_rules: **参数解释：** 推送规则策略。
        :type push_rules: int
        :param change_requests: **参数解释：** cr策略。
        :type change_requests: int
        :param custom_ctrl_items: **参数解释：** 排序id。
        :type custom_ctrl_items: int
        :param reviews: **参数解释：** 排序id。
        :type reviews: int
        :param issues: **参数解释：** issue继承模式。
        :type issues: int
        :param cr_evaluation: **参数解释：** 排序id。
        :type cr_evaluation: int
        :param e2e_settings: **参数解释：** e2e策略。
        :type e2e_settings: int
        :param committer_settings: **参数解释：** 提交策略。
        :type committer_settings: int
        :param webhook_settings: **参数解释：** webhook策略。
        :type webhook_settings: int
        :param stream_event_settings: **参数解释：** 排序id。
        :type stream_event_settings: int
        :param pipeline_settings: **参数解释：** 排序id。
        :type pipeline_settings: int
        :param issue_templates: **参数解释：** issue模板继承模式。
        :type issue_templates: int
        :param cr_comment_emplates: **参数解释：** 排序id。
        :type cr_comment_emplates: int
        :param merge_requests: **参数解释：** 排序id。
        :type merge_requests: int
        :param mr_branch_policies: **参数解释：** 合并请求策略。
        :type mr_branch_policies: int
        :param repository_settings: **参数解释：** 仓库策略。
        :type repository_settings: int
        :param deploy_keys: **参数解释：** 部署秘钥策略。
        :type deploy_keys: int
        :param watermark: **参数解释：** 水印策略。
        :type watermark: int
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param update_at: **参数解释：** 更新时间。
        :type update_at: str
        """
        
        super(ShowGroupSettingsInheritCfgResponse, self).__init__()

        self._can_update = None
        self._id = None
        self._product_id = None
        self._namespace_id = None
        self._parent_id = None
        self._ownership = None
        self._pbi = None
        self._protected_branches = None
        self._protected_tags = None
        self._push_rules = None
        self._change_requests = None
        self._custom_ctrl_items = None
        self._reviews = None
        self._issues = None
        self._cr_evaluation = None
        self._e2e_settings = None
        self._committer_settings = None
        self._webhook_settings = None
        self._stream_event_settings = None
        self._pipeline_settings = None
        self._issue_templates = None
        self._cr_comment_emplates = None
        self._merge_requests = None
        self._mr_branch_policies = None
        self._repository_settings = None
        self._deploy_keys = None
        self._watermark = None
        self._created_at = None
        self._update_at = None
        self.discriminator = None

        if can_update is not None:
            self.can_update = can_update
        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if parent_id is not None:
            self.parent_id = parent_id
        if ownership is not None:
            self.ownership = ownership
        if pbi is not None:
            self.pbi = pbi
        if protected_branches is not None:
            self.protected_branches = protected_branches
        if protected_tags is not None:
            self.protected_tags = protected_tags
        if push_rules is not None:
            self.push_rules = push_rules
        if change_requests is not None:
            self.change_requests = change_requests
        if custom_ctrl_items is not None:
            self.custom_ctrl_items = custom_ctrl_items
        if reviews is not None:
            self.reviews = reviews
        if issues is not None:
            self.issues = issues
        if cr_evaluation is not None:
            self.cr_evaluation = cr_evaluation
        if e2e_settings is not None:
            self.e2e_settings = e2e_settings
        if committer_settings is not None:
            self.committer_settings = committer_settings
        if webhook_settings is not None:
            self.webhook_settings = webhook_settings
        if stream_event_settings is not None:
            self.stream_event_settings = stream_event_settings
        if pipeline_settings is not None:
            self.pipeline_settings = pipeline_settings
        if issue_templates is not None:
            self.issue_templates = issue_templates
        if cr_comment_emplates is not None:
            self.cr_comment_emplates = cr_comment_emplates
        if merge_requests is not None:
            self.merge_requests = merge_requests
        if mr_branch_policies is not None:
            self.mr_branch_policies = mr_branch_policies
        if repository_settings is not None:
            self.repository_settings = repository_settings
        if deploy_keys is not None:
            self.deploy_keys = deploy_keys
        if watermark is not None:
            self.watermark = watermark
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def can_update(self):
        r"""Gets the can_update of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 是否可用。

        :return: The can_update of this ShowGroupSettingsInheritCfgResponse.
        :rtype: bool
        """
        return self._can_update

    @can_update.setter
    def can_update(self, can_update):
        r"""Sets the can_update of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 是否可用。

        :param can_update: The can_update of this ShowGroupSettingsInheritCfgResponse.
        :type can_update: bool
        """
        self._can_update = can_update

    @property
    def id(self):
        r"""Gets the id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 记录id。

        :return: The id of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 记录id。

        :param id: The id of this ShowGroupSettingsInheritCfgResponse.
        :type id: int
        """
        self._id = id

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The product_id of this ShowGroupSettingsInheritCfgResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param product_id: The product_id of this ShowGroupSettingsInheritCfgResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 代码组id。

        :return: The namespace_id of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 代码组id。

        :param namespace_id: The namespace_id of this ShowGroupSettingsInheritCfgResponse.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 父id。

        :return: The parent_id of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 父id。

        :param parent_id: The parent_id of this ShowGroupSettingsInheritCfgResponse.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def ownership(self):
        r"""Gets the ownership of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The ownership of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        r"""Sets the ownership of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param ownership: The ownership of this ShowGroupSettingsInheritCfgResponse.
        :type ownership: int
        """
        self._ownership = ownership

    @property
    def pbi(self):
        r"""Gets the pbi of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The pbi of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._pbi

    @pbi.setter
    def pbi(self, pbi):
        r"""Sets the pbi of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param pbi: The pbi of this ShowGroupSettingsInheritCfgResponse.
        :type pbi: int
        """
        self._pbi = pbi

    @property
    def protected_branches(self):
        r"""Gets the protected_branches of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 保护分支策略。

        :return: The protected_branches of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._protected_branches

    @protected_branches.setter
    def protected_branches(self, protected_branches):
        r"""Sets the protected_branches of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 保护分支策略。

        :param protected_branches: The protected_branches of this ShowGroupSettingsInheritCfgResponse.
        :type protected_branches: int
        """
        self._protected_branches = protected_branches

    @property
    def protected_tags(self):
        r"""Gets the protected_tags of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 保护tag策略。

        :return: The protected_tags of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._protected_tags

    @protected_tags.setter
    def protected_tags(self, protected_tags):
        r"""Sets the protected_tags of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 保护tag策略。

        :param protected_tags: The protected_tags of this ShowGroupSettingsInheritCfgResponse.
        :type protected_tags: int
        """
        self._protected_tags = protected_tags

    @property
    def push_rules(self):
        r"""Gets the push_rules of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 推送规则策略。

        :return: The push_rules of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._push_rules

    @push_rules.setter
    def push_rules(self, push_rules):
        r"""Sets the push_rules of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 推送规则策略。

        :param push_rules: The push_rules of this ShowGroupSettingsInheritCfgResponse.
        :type push_rules: int
        """
        self._push_rules = push_rules

    @property
    def change_requests(self):
        r"""Gets the change_requests of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** cr策略。

        :return: The change_requests of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._change_requests

    @change_requests.setter
    def change_requests(self, change_requests):
        r"""Sets the change_requests of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** cr策略。

        :param change_requests: The change_requests of this ShowGroupSettingsInheritCfgResponse.
        :type change_requests: int
        """
        self._change_requests = change_requests

    @property
    def custom_ctrl_items(self):
        r"""Gets the custom_ctrl_items of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The custom_ctrl_items of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._custom_ctrl_items

    @custom_ctrl_items.setter
    def custom_ctrl_items(self, custom_ctrl_items):
        r"""Sets the custom_ctrl_items of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param custom_ctrl_items: The custom_ctrl_items of this ShowGroupSettingsInheritCfgResponse.
        :type custom_ctrl_items: int
        """
        self._custom_ctrl_items = custom_ctrl_items

    @property
    def reviews(self):
        r"""Gets the reviews of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The reviews of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        r"""Sets the reviews of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param reviews: The reviews of this ShowGroupSettingsInheritCfgResponse.
        :type reviews: int
        """
        self._reviews = reviews

    @property
    def issues(self):
        r"""Gets the issues of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** issue继承模式。

        :return: The issues of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        r"""Sets the issues of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** issue继承模式。

        :param issues: The issues of this ShowGroupSettingsInheritCfgResponse.
        :type issues: int
        """
        self._issues = issues

    @property
    def cr_evaluation(self):
        r"""Gets the cr_evaluation of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The cr_evaluation of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._cr_evaluation

    @cr_evaluation.setter
    def cr_evaluation(self, cr_evaluation):
        r"""Sets the cr_evaluation of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param cr_evaluation: The cr_evaluation of this ShowGroupSettingsInheritCfgResponse.
        :type cr_evaluation: int
        """
        self._cr_evaluation = cr_evaluation

    @property
    def e2e_settings(self):
        r"""Gets the e2e_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** e2e策略。

        :return: The e2e_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._e2e_settings

    @e2e_settings.setter
    def e2e_settings(self, e2e_settings):
        r"""Sets the e2e_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** e2e策略。

        :param e2e_settings: The e2e_settings of this ShowGroupSettingsInheritCfgResponse.
        :type e2e_settings: int
        """
        self._e2e_settings = e2e_settings

    @property
    def committer_settings(self):
        r"""Gets the committer_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 提交策略。

        :return: The committer_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._committer_settings

    @committer_settings.setter
    def committer_settings(self, committer_settings):
        r"""Sets the committer_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 提交策略。

        :param committer_settings: The committer_settings of this ShowGroupSettingsInheritCfgResponse.
        :type committer_settings: int
        """
        self._committer_settings = committer_settings

    @property
    def webhook_settings(self):
        r"""Gets the webhook_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** webhook策略。

        :return: The webhook_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._webhook_settings

    @webhook_settings.setter
    def webhook_settings(self, webhook_settings):
        r"""Sets the webhook_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** webhook策略。

        :param webhook_settings: The webhook_settings of this ShowGroupSettingsInheritCfgResponse.
        :type webhook_settings: int
        """
        self._webhook_settings = webhook_settings

    @property
    def stream_event_settings(self):
        r"""Gets the stream_event_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The stream_event_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._stream_event_settings

    @stream_event_settings.setter
    def stream_event_settings(self, stream_event_settings):
        r"""Sets the stream_event_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param stream_event_settings: The stream_event_settings of this ShowGroupSettingsInheritCfgResponse.
        :type stream_event_settings: int
        """
        self._stream_event_settings = stream_event_settings

    @property
    def pipeline_settings(self):
        r"""Gets the pipeline_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The pipeline_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._pipeline_settings

    @pipeline_settings.setter
    def pipeline_settings(self, pipeline_settings):
        r"""Sets the pipeline_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param pipeline_settings: The pipeline_settings of this ShowGroupSettingsInheritCfgResponse.
        :type pipeline_settings: int
        """
        self._pipeline_settings = pipeline_settings

    @property
    def issue_templates(self):
        r"""Gets the issue_templates of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** issue模板继承模式。

        :return: The issue_templates of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._issue_templates

    @issue_templates.setter
    def issue_templates(self, issue_templates):
        r"""Sets the issue_templates of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** issue模板继承模式。

        :param issue_templates: The issue_templates of this ShowGroupSettingsInheritCfgResponse.
        :type issue_templates: int
        """
        self._issue_templates = issue_templates

    @property
    def cr_comment_emplates(self):
        r"""Gets the cr_comment_emplates of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The cr_comment_emplates of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._cr_comment_emplates

    @cr_comment_emplates.setter
    def cr_comment_emplates(self, cr_comment_emplates):
        r"""Sets the cr_comment_emplates of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param cr_comment_emplates: The cr_comment_emplates of this ShowGroupSettingsInheritCfgResponse.
        :type cr_comment_emplates: int
        """
        self._cr_comment_emplates = cr_comment_emplates

    @property
    def merge_requests(self):
        r"""Gets the merge_requests of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :return: The merge_requests of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._merge_requests

    @merge_requests.setter
    def merge_requests(self, merge_requests):
        r"""Sets the merge_requests of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 排序id。

        :param merge_requests: The merge_requests of this ShowGroupSettingsInheritCfgResponse.
        :type merge_requests: int
        """
        self._merge_requests = merge_requests

    @property
    def mr_branch_policies(self):
        r"""Gets the mr_branch_policies of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 合并请求策略。

        :return: The mr_branch_policies of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._mr_branch_policies

    @mr_branch_policies.setter
    def mr_branch_policies(self, mr_branch_policies):
        r"""Sets the mr_branch_policies of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 合并请求策略。

        :param mr_branch_policies: The mr_branch_policies of this ShowGroupSettingsInheritCfgResponse.
        :type mr_branch_policies: int
        """
        self._mr_branch_policies = mr_branch_policies

    @property
    def repository_settings(self):
        r"""Gets the repository_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 仓库策略。

        :return: The repository_settings of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._repository_settings

    @repository_settings.setter
    def repository_settings(self, repository_settings):
        r"""Sets the repository_settings of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 仓库策略。

        :param repository_settings: The repository_settings of this ShowGroupSettingsInheritCfgResponse.
        :type repository_settings: int
        """
        self._repository_settings = repository_settings

    @property
    def deploy_keys(self):
        r"""Gets the deploy_keys of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 部署秘钥策略。

        :return: The deploy_keys of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._deploy_keys

    @deploy_keys.setter
    def deploy_keys(self, deploy_keys):
        r"""Sets the deploy_keys of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 部署秘钥策略。

        :param deploy_keys: The deploy_keys of this ShowGroupSettingsInheritCfgResponse.
        :type deploy_keys: int
        """
        self._deploy_keys = deploy_keys

    @property
    def watermark(self):
        r"""Gets the watermark of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 水印策略。

        :return: The watermark of this ShowGroupSettingsInheritCfgResponse.
        :rtype: int
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        r"""Sets the watermark of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 水印策略。

        :param watermark: The watermark of this ShowGroupSettingsInheritCfgResponse.
        :type watermark: int
        """
        self._watermark = watermark

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 创建时间。

        :return: The created_at of this ShowGroupSettingsInheritCfgResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this ShowGroupSettingsInheritCfgResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 更新时间。

        :return: The update_at of this ShowGroupSettingsInheritCfgResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowGroupSettingsInheritCfgResponse.

        **参数解释：** 更新时间。

        :param update_at: The update_at of this ShowGroupSettingsInheritCfgResponse.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, ShowGroupSettingsInheritCfgResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
