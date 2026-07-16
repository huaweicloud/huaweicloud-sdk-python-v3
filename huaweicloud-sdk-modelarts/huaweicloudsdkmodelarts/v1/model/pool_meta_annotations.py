# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMetaAnnotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_description': 'str',
        'os_modelarts_billing_mode': 'str',
        'os_modelarts_period_num': 'str',
        'os_modelarts_period_type': 'str',
        'os_modelarts_auto_renew': 'str',
        'os_modelarts_promotion_info': 'str',
        'os_modelarts_service_console_url': 'str',
        'os_modelarts_order_id': 'str',
        'os_modelarts_flavor_resource_ids': 'str',
        'os_modelarts_tms_tags': 'str',
        'os_modelarts_pool_scheduler_queue_strategy': 'str',
        'os_modelarts_pool_subpools_count': 'str',
        'os_modelarts_tenant_domain_name': 'str',
        'os_modelarts_pool_scope_external_dependency_train': 'str'
    }

    attribute_map = {
        'os_modelarts_description': 'os.modelarts/description',
        'os_modelarts_billing_mode': 'os.modelarts/billing.mode',
        'os_modelarts_period_num': 'os.modelarts/period.num',
        'os_modelarts_period_type': 'os.modelarts/period.type',
        'os_modelarts_auto_renew': 'os.modelarts/auto.renew',
        'os_modelarts_promotion_info': 'os.modelarts/promotion.info',
        'os_modelarts_service_console_url': 'os.modelarts/service.console.url',
        'os_modelarts_order_id': 'os.modelarts/order.id',
        'os_modelarts_flavor_resource_ids': 'os.modelarts/flavor.resource.ids',
        'os_modelarts_tms_tags': 'os.modelarts/tms.tags',
        'os_modelarts_pool_scheduler_queue_strategy': 'os.modelarts.pool/scheduler.queue.strategy',
        'os_modelarts_pool_subpools_count': 'os.modelarts.pool/subpools.count',
        'os_modelarts_tenant_domain_name': 'os.modelarts/tenant.domain.name',
        'os_modelarts_pool_scope_external_dependency_train': 'os.modelarts.pool/scope.external.dependency.train'
    }

    def __init__(self, os_modelarts_description=None, os_modelarts_billing_mode=None, os_modelarts_period_num=None, os_modelarts_period_type=None, os_modelarts_auto_renew=None, os_modelarts_promotion_info=None, os_modelarts_service_console_url=None, os_modelarts_order_id=None, os_modelarts_flavor_resource_ids=None, os_modelarts_tms_tags=None, os_modelarts_pool_scheduler_queue_strategy=None, os_modelarts_pool_subpools_count=None, os_modelarts_tenant_domain_name=None, os_modelarts_pool_scope_external_dependency_train=None):
        r"""PoolMetaAnnotations

        The model defined in huaweicloud sdk

        :param os_modelarts_description: **参数解释**：资源池的描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_description: str
        :param os_modelarts_billing_mode: **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。
        :type os_modelarts_billing_mode: str
        :param os_modelarts_period_num: **参数解释**：包周期资源池的订购周期。 **约束限制**：和os.modelarts/period.type字段配合使用。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_period_num: str
        :param os_modelarts_period_type: **参数解释**：包周期资源池的订购类型。 **约束限制**：和os.modelarts/period.num字段配合使用。 **取值范围**：可选值如下： - 2：包月。 - 3：包年。 **默认取值**：不涉及。
        :type os_modelarts_period_type: str
        :param os_modelarts_auto_renew: **参数解释**：包周期资源池的自动续费类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费。 - 1：自动续费。 **默认取值**：0。
        :type os_modelarts_auto_renew: str
        :param os_modelarts_promotion_info: **参数解释**：包周期资源池购买时选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_promotion_info: str
        :param os_modelarts_service_console_url: **参数解释**：购买包周期资源在订单支付完成后跳转地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_service_console_url: str
        :param os_modelarts_order_id: **参数解释**：包周期资源池购买时传递的订单ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_order_id: str
        :param os_modelarts_flavor_resource_ids: **参数解释**：包周期资源池中资源规格对应的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_flavor_resource_ids: str
        :param os_modelarts_tms_tags: **参数解释**：资源池上的资源标签。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_tms_tags: str
        :param os_modelarts_pool_scheduler_queue_strategy: **参数解释**：资源池调度队列的策略，用于定义任务调度的规则。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_pool_scheduler_queue_strategy: str
        :param os_modelarts_pool_subpools_count: **参数解释**：资源池包含的逻辑子池的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_pool_subpools_count: str
        :param os_modelarts_tenant_domain_name: **参数解释**：资源池的租户账号 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_tenant_domain_name: str
        :param os_modelarts_pool_scope_external_dependency_train: **参数解释**：训练外部依赖标识 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_pool_scope_external_dependency_train: str
        """
        
        

        self._os_modelarts_description = None
        self._os_modelarts_billing_mode = None
        self._os_modelarts_period_num = None
        self._os_modelarts_period_type = None
        self._os_modelarts_auto_renew = None
        self._os_modelarts_promotion_info = None
        self._os_modelarts_service_console_url = None
        self._os_modelarts_order_id = None
        self._os_modelarts_flavor_resource_ids = None
        self._os_modelarts_tms_tags = None
        self._os_modelarts_pool_scheduler_queue_strategy = None
        self._os_modelarts_pool_subpools_count = None
        self._os_modelarts_tenant_domain_name = None
        self._os_modelarts_pool_scope_external_dependency_train = None
        self.discriminator = None

        if os_modelarts_description is not None:
            self.os_modelarts_description = os_modelarts_description
        if os_modelarts_billing_mode is not None:
            self.os_modelarts_billing_mode = os_modelarts_billing_mode
        if os_modelarts_period_num is not None:
            self.os_modelarts_period_num = os_modelarts_period_num
        if os_modelarts_period_type is not None:
            self.os_modelarts_period_type = os_modelarts_period_type
        if os_modelarts_auto_renew is not None:
            self.os_modelarts_auto_renew = os_modelarts_auto_renew
        if os_modelarts_promotion_info is not None:
            self.os_modelarts_promotion_info = os_modelarts_promotion_info
        if os_modelarts_service_console_url is not None:
            self.os_modelarts_service_console_url = os_modelarts_service_console_url
        if os_modelarts_order_id is not None:
            self.os_modelarts_order_id = os_modelarts_order_id
        if os_modelarts_flavor_resource_ids is not None:
            self.os_modelarts_flavor_resource_ids = os_modelarts_flavor_resource_ids
        if os_modelarts_tms_tags is not None:
            self.os_modelarts_tms_tags = os_modelarts_tms_tags
        if os_modelarts_pool_scheduler_queue_strategy is not None:
            self.os_modelarts_pool_scheduler_queue_strategy = os_modelarts_pool_scheduler_queue_strategy
        if os_modelarts_pool_subpools_count is not None:
            self.os_modelarts_pool_subpools_count = os_modelarts_pool_subpools_count
        if os_modelarts_tenant_domain_name is not None:
            self.os_modelarts_tenant_domain_name = os_modelarts_tenant_domain_name
        if os_modelarts_pool_scope_external_dependency_train is not None:
            self.os_modelarts_pool_scope_external_dependency_train = os_modelarts_pool_scope_external_dependency_train

    @property
    def os_modelarts_description(self):
        r"""Gets the os_modelarts_description of this PoolMetaAnnotations.

        **参数解释**：资源池的描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_description of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_description

    @os_modelarts_description.setter
    def os_modelarts_description(self, os_modelarts_description):
        r"""Sets the os_modelarts_description of this PoolMetaAnnotations.

        **参数解释**：资源池的描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_description: The os_modelarts_description of this PoolMetaAnnotations.
        :type os_modelarts_description: str
        """
        self._os_modelarts_description = os_modelarts_description

    @property
    def os_modelarts_billing_mode(self):
        r"""Gets the os_modelarts_billing_mode of this PoolMetaAnnotations.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。

        :return: The os_modelarts_billing_mode of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_billing_mode

    @os_modelarts_billing_mode.setter
    def os_modelarts_billing_mode(self, os_modelarts_billing_mode):
        r"""Sets the os_modelarts_billing_mode of this PoolMetaAnnotations.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：按需计费 - 1：包周期计费 **默认取值**：不涉及。

        :param os_modelarts_billing_mode: The os_modelarts_billing_mode of this PoolMetaAnnotations.
        :type os_modelarts_billing_mode: str
        """
        self._os_modelarts_billing_mode = os_modelarts_billing_mode

    @property
    def os_modelarts_period_num(self):
        r"""Gets the os_modelarts_period_num of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的订购周期。 **约束限制**：和os.modelarts/period.type字段配合使用。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_period_num of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_period_num

    @os_modelarts_period_num.setter
    def os_modelarts_period_num(self, os_modelarts_period_num):
        r"""Sets the os_modelarts_period_num of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的订购周期。 **约束限制**：和os.modelarts/period.type字段配合使用。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_period_num: The os_modelarts_period_num of this PoolMetaAnnotations.
        :type os_modelarts_period_num: str
        """
        self._os_modelarts_period_num = os_modelarts_period_num

    @property
    def os_modelarts_period_type(self):
        r"""Gets the os_modelarts_period_type of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的订购类型。 **约束限制**：和os.modelarts/period.num字段配合使用。 **取值范围**：可选值如下： - 2：包月。 - 3：包年。 **默认取值**：不涉及。

        :return: The os_modelarts_period_type of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_period_type

    @os_modelarts_period_type.setter
    def os_modelarts_period_type(self, os_modelarts_period_type):
        r"""Sets the os_modelarts_period_type of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的订购类型。 **约束限制**：和os.modelarts/period.num字段配合使用。 **取值范围**：可选值如下： - 2：包月。 - 3：包年。 **默认取值**：不涉及。

        :param os_modelarts_period_type: The os_modelarts_period_type of this PoolMetaAnnotations.
        :type os_modelarts_period_type: str
        """
        self._os_modelarts_period_type = os_modelarts_period_type

    @property
    def os_modelarts_auto_renew(self):
        r"""Gets the os_modelarts_auto_renew of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的自动续费类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费。 - 1：自动续费。 **默认取值**：0。

        :return: The os_modelarts_auto_renew of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_auto_renew

    @os_modelarts_auto_renew.setter
    def os_modelarts_auto_renew(self, os_modelarts_auto_renew):
        r"""Sets the os_modelarts_auto_renew of this PoolMetaAnnotations.

        **参数解释**：包周期资源池的自动续费类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - 0：不自动续费。 - 1：自动续费。 **默认取值**：0。

        :param os_modelarts_auto_renew: The os_modelarts_auto_renew of this PoolMetaAnnotations.
        :type os_modelarts_auto_renew: str
        """
        self._os_modelarts_auto_renew = os_modelarts_auto_renew

    @property
    def os_modelarts_promotion_info(self):
        r"""Gets the os_modelarts_promotion_info of this PoolMetaAnnotations.

        **参数解释**：包周期资源池购买时选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_promotion_info of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_promotion_info

    @os_modelarts_promotion_info.setter
    def os_modelarts_promotion_info(self, os_modelarts_promotion_info):
        r"""Sets the os_modelarts_promotion_info of this PoolMetaAnnotations.

        **参数解释**：包周期资源池购买时选择的折扣信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_promotion_info: The os_modelarts_promotion_info of this PoolMetaAnnotations.
        :type os_modelarts_promotion_info: str
        """
        self._os_modelarts_promotion_info = os_modelarts_promotion_info

    @property
    def os_modelarts_service_console_url(self):
        r"""Gets the os_modelarts_service_console_url of this PoolMetaAnnotations.

        **参数解释**：购买包周期资源在订单支付完成后跳转地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_service_console_url of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_service_console_url

    @os_modelarts_service_console_url.setter
    def os_modelarts_service_console_url(self, os_modelarts_service_console_url):
        r"""Sets the os_modelarts_service_console_url of this PoolMetaAnnotations.

        **参数解释**：购买包周期资源在订单支付完成后跳转地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_service_console_url: The os_modelarts_service_console_url of this PoolMetaAnnotations.
        :type os_modelarts_service_console_url: str
        """
        self._os_modelarts_service_console_url = os_modelarts_service_console_url

    @property
    def os_modelarts_order_id(self):
        r"""Gets the os_modelarts_order_id of this PoolMetaAnnotations.

        **参数解释**：包周期资源池购买时传递的订单ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_order_id of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_order_id

    @os_modelarts_order_id.setter
    def os_modelarts_order_id(self, os_modelarts_order_id):
        r"""Sets the os_modelarts_order_id of this PoolMetaAnnotations.

        **参数解释**：包周期资源池购买时传递的订单ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_order_id: The os_modelarts_order_id of this PoolMetaAnnotations.
        :type os_modelarts_order_id: str
        """
        self._os_modelarts_order_id = os_modelarts_order_id

    @property
    def os_modelarts_flavor_resource_ids(self):
        r"""Gets the os_modelarts_flavor_resource_ids of this PoolMetaAnnotations.

        **参数解释**：包周期资源池中资源规格对应的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_flavor_resource_ids of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_flavor_resource_ids

    @os_modelarts_flavor_resource_ids.setter
    def os_modelarts_flavor_resource_ids(self, os_modelarts_flavor_resource_ids):
        r"""Sets the os_modelarts_flavor_resource_ids of this PoolMetaAnnotations.

        **参数解释**：包周期资源池中资源规格对应的资源ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_flavor_resource_ids: The os_modelarts_flavor_resource_ids of this PoolMetaAnnotations.
        :type os_modelarts_flavor_resource_ids: str
        """
        self._os_modelarts_flavor_resource_ids = os_modelarts_flavor_resource_ids

    @property
    def os_modelarts_tms_tags(self):
        r"""Gets the os_modelarts_tms_tags of this PoolMetaAnnotations.

        **参数解释**：资源池上的资源标签。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_tms_tags of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_tms_tags

    @os_modelarts_tms_tags.setter
    def os_modelarts_tms_tags(self, os_modelarts_tms_tags):
        r"""Sets the os_modelarts_tms_tags of this PoolMetaAnnotations.

        **参数解释**：资源池上的资源标签。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_tms_tags: The os_modelarts_tms_tags of this PoolMetaAnnotations.
        :type os_modelarts_tms_tags: str
        """
        self._os_modelarts_tms_tags = os_modelarts_tms_tags

    @property
    def os_modelarts_pool_scheduler_queue_strategy(self):
        r"""Gets the os_modelarts_pool_scheduler_queue_strategy of this PoolMetaAnnotations.

        **参数解释**：资源池调度队列的策略，用于定义任务调度的规则。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_pool_scheduler_queue_strategy of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_pool_scheduler_queue_strategy

    @os_modelarts_pool_scheduler_queue_strategy.setter
    def os_modelarts_pool_scheduler_queue_strategy(self, os_modelarts_pool_scheduler_queue_strategy):
        r"""Sets the os_modelarts_pool_scheduler_queue_strategy of this PoolMetaAnnotations.

        **参数解释**：资源池调度队列的策略，用于定义任务调度的规则。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_pool_scheduler_queue_strategy: The os_modelarts_pool_scheduler_queue_strategy of this PoolMetaAnnotations.
        :type os_modelarts_pool_scheduler_queue_strategy: str
        """
        self._os_modelarts_pool_scheduler_queue_strategy = os_modelarts_pool_scheduler_queue_strategy

    @property
    def os_modelarts_pool_subpools_count(self):
        r"""Gets the os_modelarts_pool_subpools_count of this PoolMetaAnnotations.

        **参数解释**：资源池包含的逻辑子池的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_pool_subpools_count of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_pool_subpools_count

    @os_modelarts_pool_subpools_count.setter
    def os_modelarts_pool_subpools_count(self, os_modelarts_pool_subpools_count):
        r"""Sets the os_modelarts_pool_subpools_count of this PoolMetaAnnotations.

        **参数解释**：资源池包含的逻辑子池的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_pool_subpools_count: The os_modelarts_pool_subpools_count of this PoolMetaAnnotations.
        :type os_modelarts_pool_subpools_count: str
        """
        self._os_modelarts_pool_subpools_count = os_modelarts_pool_subpools_count

    @property
    def os_modelarts_tenant_domain_name(self):
        r"""Gets the os_modelarts_tenant_domain_name of this PoolMetaAnnotations.

        **参数解释**：资源池的租户账号 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_tenant_domain_name of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_tenant_domain_name

    @os_modelarts_tenant_domain_name.setter
    def os_modelarts_tenant_domain_name(self, os_modelarts_tenant_domain_name):
        r"""Sets the os_modelarts_tenant_domain_name of this PoolMetaAnnotations.

        **参数解释**：资源池的租户账号 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_tenant_domain_name: The os_modelarts_tenant_domain_name of this PoolMetaAnnotations.
        :type os_modelarts_tenant_domain_name: str
        """
        self._os_modelarts_tenant_domain_name = os_modelarts_tenant_domain_name

    @property
    def os_modelarts_pool_scope_external_dependency_train(self):
        r"""Gets the os_modelarts_pool_scope_external_dependency_train of this PoolMetaAnnotations.

        **参数解释**：训练外部依赖标识 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_pool_scope_external_dependency_train of this PoolMetaAnnotations.
        :rtype: str
        """
        return self._os_modelarts_pool_scope_external_dependency_train

    @os_modelarts_pool_scope_external_dependency_train.setter
    def os_modelarts_pool_scope_external_dependency_train(self, os_modelarts_pool_scope_external_dependency_train):
        r"""Sets the os_modelarts_pool_scope_external_dependency_train of this PoolMetaAnnotations.

        **参数解释**：训练外部依赖标识 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_pool_scope_external_dependency_train: The os_modelarts_pool_scope_external_dependency_train of this PoolMetaAnnotations.
        :type os_modelarts_pool_scope_external_dependency_train: str
        """
        self._os_modelarts_pool_scope_external_dependency_train = os_modelarts_pool_scope_external_dependency_train

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
        if not isinstance(other, PoolMetaAnnotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
