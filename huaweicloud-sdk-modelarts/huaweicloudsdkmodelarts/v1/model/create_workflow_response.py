# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkflowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'workflow_id': 'str',
        'created_at': 'str',
        'description': 'str',
        'steps': 'list[WorkflowStep]',
        'user_name': 'str',
        'workspace_id': 'str',
        'data_requirements': 'list[DataRequirement]',
        'data': 'list[Data]',
        'parameters': 'list[WorkflowParameter]',
        'source_workflow_id': 'str',
        'gallery_subscription': 'WorkflowGallerySubscription',
        'latest_execution': 'ExecutionBrief',
        'run_count': 'int',
        'param_ready': 'bool',
        'source': 'str',
        'storages': 'list[WorkflowStorage]',
        'labels': 'list[str]',
        'assets': 'list[WorkflowAsset]',
        'sub_graphs': 'list[WorkflowSubgraph]',
        'extend': 'dict(str, object)',
        'policy': 'WorkflowPolicy',
        'with_subscription': 'bool',
        'smn_switch': 'bool',
        'subscription_id': 'str',
        'exeml_template_id': 'str',
        'last_modified_at': 'str',
        'package': 'WorkflowServicePackege'
    }

    attribute_map = {
        'name': 'name',
        'workflow_id': 'workflow_id',
        'created_at': 'created_at',
        'description': 'description',
        'steps': 'steps',
        'user_name': 'user_name',
        'workspace_id': 'workspace_id',
        'data_requirements': 'data_requirements',
        'data': 'data',
        'parameters': 'parameters',
        'source_workflow_id': 'source_workflow_id',
        'gallery_subscription': 'gallery_subscription',
        'latest_execution': 'latest_execution',
        'run_count': 'run_count',
        'param_ready': 'param_ready',
        'source': 'source',
        'storages': 'storages',
        'labels': 'labels',
        'assets': 'assets',
        'sub_graphs': 'sub_graphs',
        'extend': 'extend',
        'policy': 'policy',
        'with_subscription': 'with_subscription',
        'smn_switch': 'smn_switch',
        'subscription_id': 'subscription_id',
        'exeml_template_id': 'exeml_template_id',
        'last_modified_at': 'last_modified_at',
        'package': 'package'
    }

    def __init__(self, name=None, workflow_id=None, created_at=None, description=None, steps=None, user_name=None, workspace_id=None, data_requirements=None, data=None, parameters=None, source_workflow_id=None, gallery_subscription=None, latest_execution=None, run_count=None, param_ready=None, source=None, storages=None, labels=None, assets=None, sub_graphs=None, extend=None, policy=None, with_subscription=None, smn_switch=None, subscription_id=None, exeml_template_id=None, last_modified_at=None, package=None):
        r"""CreateWorkflowResponse

        The model defined in huaweicloud sdk

        :param name: Workflow工作流名称，1到64位只包含中英文、数字、空格、下划线（_）和中划线（-），并且以中英文开头。
        :type name: str
        :param workflow_id: Workflow工作流ID。创建工作流时后台自动生成。
        :type workflow_id: str
        :param created_at: Workflow工作流的创建时间。
        :type created_at: str
        :param description: Workflow工作流的描述信息。
        :type description: str
        :param steps: Workflow工作流包含的步骤定义。
        :type steps: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        :param user_name: 创建Workflow工作流的用户名。
        :type user_name: str
        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param data_requirements: Workflow需要的数据。
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        :param data: Workflow包含的数据。
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.Data`]
        :param parameters: Workflow包含的参数。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        :param source_workflow_id: 从指定Workflow工作流进行复制。通过复制来创建Workflow时必填。
        :type source_workflow_id: str
        :param gallery_subscription: 
        :type gallery_subscription: :class:`huaweicloudsdkmodelarts.v1.WorkflowGallerySubscription`
        :param latest_execution: 
        :type latest_execution: :class:`huaweicloudsdkmodelarts.v1.ExecutionBrief`
        :param run_count: 工作流的已运行次数。
        :type run_count: int
        :param param_ready: 当前工作流的必选参数是否都已填完。
        :type param_ready: bool
        :param source: 工作流来源，可选值为ai_gallery，表示工作流是从AI Gallery导入的。
        :type source: str
        :param storages: Workflow包含的统一存储定义。
        :type storages: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        :param labels: 为Workflow工作流设置的标签。
        :type labels: list[str]
        :param assets: 工作流绑定的资产。
        :type assets: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowAsset`]
        :param sub_graphs: 工作流包含的子图。
        :type sub_graphs: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        :param extend: 计费工作流使用的拓展字段。
        :type extend: dict(str, object)
        :param policy: 
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowPolicy`
        :param with_subscription: 工作流SMN消息订阅开关，默认为false，表示关闭消息订阅开关。
        :type with_subscription: bool
        :param smn_switch: SMN开关。
        :type smn_switch: bool
        :param subscription_id: SMN消息订阅ID。
        :type subscription_id: str
        :param exeml_template_id: 自动学习模板ID。
        :type exeml_template_id: str
        :param last_modified_at: 最近一次修改的时间。
        :type last_modified_at: str
        :param package: 
        :type package: :class:`huaweicloudsdkmodelarts.v1.WorkflowServicePackege`
        """
        
        super().__init__()

        self._name = None
        self._workflow_id = None
        self._created_at = None
        self._description = None
        self._steps = None
        self._user_name = None
        self._workspace_id = None
        self._data_requirements = None
        self._data = None
        self._parameters = None
        self._source_workflow_id = None
        self._gallery_subscription = None
        self._latest_execution = None
        self._run_count = None
        self._param_ready = None
        self._source = None
        self._storages = None
        self._labels = None
        self._assets = None
        self._sub_graphs = None
        self._extend = None
        self._policy = None
        self._with_subscription = None
        self._smn_switch = None
        self._subscription_id = None
        self._exeml_template_id = None
        self._last_modified_at = None
        self._package = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if steps is not None:
            self.steps = steps
        if user_name is not None:
            self.user_name = user_name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if data_requirements is not None:
            self.data_requirements = data_requirements
        if data is not None:
            self.data = data
        if parameters is not None:
            self.parameters = parameters
        if source_workflow_id is not None:
            self.source_workflow_id = source_workflow_id
        if gallery_subscription is not None:
            self.gallery_subscription = gallery_subscription
        if latest_execution is not None:
            self.latest_execution = latest_execution
        if run_count is not None:
            self.run_count = run_count
        if param_ready is not None:
            self.param_ready = param_ready
        if source is not None:
            self.source = source
        if storages is not None:
            self.storages = storages
        if labels is not None:
            self.labels = labels
        if assets is not None:
            self.assets = assets
        if sub_graphs is not None:
            self.sub_graphs = sub_graphs
        if extend is not None:
            self.extend = extend
        if policy is not None:
            self.policy = policy
        if with_subscription is not None:
            self.with_subscription = with_subscription
        if smn_switch is not None:
            self.smn_switch = smn_switch
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if exeml_template_id is not None:
            self.exeml_template_id = exeml_template_id
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if package is not None:
            self.package = package

    @property
    def name(self):
        r"""Gets the name of this CreateWorkflowResponse.

        Workflow工作流名称，1到64位只包含中英文、数字、空格、下划线（_）和中划线（-），并且以中英文开头。

        :return: The name of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWorkflowResponse.

        Workflow工作流名称，1到64位只包含中英文、数字、空格、下划线（_）和中划线（-），并且以中英文开头。

        :param name: The name of this CreateWorkflowResponse.
        :type name: str
        """
        self._name = name

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CreateWorkflowResponse.

        Workflow工作流ID。创建工作流时后台自动生成。

        :return: The workflow_id of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CreateWorkflowResponse.

        Workflow工作流ID。创建工作流时后台自动生成。

        :param workflow_id: The workflow_id of this CreateWorkflowResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateWorkflowResponse.

        Workflow工作流的创建时间。

        :return: The created_at of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateWorkflowResponse.

        Workflow工作流的创建时间。

        :param created_at: The created_at of this CreateWorkflowResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this CreateWorkflowResponse.

        Workflow工作流的描述信息。

        :return: The description of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWorkflowResponse.

        Workflow工作流的描述信息。

        :param description: The description of this CreateWorkflowResponse.
        :type description: str
        """
        self._description = description

    @property
    def steps(self):
        r"""Gets the steps of this CreateWorkflowResponse.

        Workflow工作流包含的步骤定义。

        :return: The steps of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this CreateWorkflowResponse.

        Workflow工作流包含的步骤定义。

        :param steps: The steps of this CreateWorkflowResponse.
        :type steps: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStep`]
        """
        self._steps = steps

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateWorkflowResponse.

        创建Workflow工作流的用户名。

        :return: The user_name of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateWorkflowResponse.

        创建Workflow工作流的用户名。

        :param user_name: The user_name of this CreateWorkflowResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateWorkflowResponse.

        工作空间ID。

        :return: The workspace_id of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateWorkflowResponse.

        工作空间ID。

        :param workspace_id: The workspace_id of this CreateWorkflowResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def data_requirements(self):
        r"""Gets the data_requirements of this CreateWorkflowResponse.

        Workflow需要的数据。

        :return: The data_requirements of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        return self._data_requirements

    @data_requirements.setter
    def data_requirements(self, data_requirements):
        r"""Sets the data_requirements of this CreateWorkflowResponse.

        Workflow需要的数据。

        :param data_requirements: The data_requirements of this CreateWorkflowResponse.
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        self._data_requirements = data_requirements

    @property
    def data(self):
        r"""Gets the data of this CreateWorkflowResponse.

        Workflow包含的数据。

        :return: The data of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Data`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreateWorkflowResponse.

        Workflow包含的数据。

        :param data: The data of this CreateWorkflowResponse.
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.Data`]
        """
        self._data = data

    @property
    def parameters(self):
        r"""Gets the parameters of this CreateWorkflowResponse.

        Workflow包含的参数。

        :return: The parameters of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CreateWorkflowResponse.

        Workflow包含的参数。

        :param parameters: The parameters of this CreateWorkflowResponse.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        self._parameters = parameters

    @property
    def source_workflow_id(self):
        r"""Gets the source_workflow_id of this CreateWorkflowResponse.

        从指定Workflow工作流进行复制。通过复制来创建Workflow时必填。

        :return: The source_workflow_id of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._source_workflow_id

    @source_workflow_id.setter
    def source_workflow_id(self, source_workflow_id):
        r"""Sets the source_workflow_id of this CreateWorkflowResponse.

        从指定Workflow工作流进行复制。通过复制来创建Workflow时必填。

        :param source_workflow_id: The source_workflow_id of this CreateWorkflowResponse.
        :type source_workflow_id: str
        """
        self._source_workflow_id = source_workflow_id

    @property
    def gallery_subscription(self):
        r"""Gets the gallery_subscription of this CreateWorkflowResponse.

        :return: The gallery_subscription of this CreateWorkflowResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowGallerySubscription`
        """
        return self._gallery_subscription

    @gallery_subscription.setter
    def gallery_subscription(self, gallery_subscription):
        r"""Sets the gallery_subscription of this CreateWorkflowResponse.

        :param gallery_subscription: The gallery_subscription of this CreateWorkflowResponse.
        :type gallery_subscription: :class:`huaweicloudsdkmodelarts.v1.WorkflowGallerySubscription`
        """
        self._gallery_subscription = gallery_subscription

    @property
    def latest_execution(self):
        r"""Gets the latest_execution of this CreateWorkflowResponse.

        :return: The latest_execution of this CreateWorkflowResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ExecutionBrief`
        """
        return self._latest_execution

    @latest_execution.setter
    def latest_execution(self, latest_execution):
        r"""Sets the latest_execution of this CreateWorkflowResponse.

        :param latest_execution: The latest_execution of this CreateWorkflowResponse.
        :type latest_execution: :class:`huaweicloudsdkmodelarts.v1.ExecutionBrief`
        """
        self._latest_execution = latest_execution

    @property
    def run_count(self):
        r"""Gets the run_count of this CreateWorkflowResponse.

        工作流的已运行次数。

        :return: The run_count of this CreateWorkflowResponse.
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count):
        r"""Sets the run_count of this CreateWorkflowResponse.

        工作流的已运行次数。

        :param run_count: The run_count of this CreateWorkflowResponse.
        :type run_count: int
        """
        self._run_count = run_count

    @property
    def param_ready(self):
        r"""Gets the param_ready of this CreateWorkflowResponse.

        当前工作流的必选参数是否都已填完。

        :return: The param_ready of this CreateWorkflowResponse.
        :rtype: bool
        """
        return self._param_ready

    @param_ready.setter
    def param_ready(self, param_ready):
        r"""Sets the param_ready of this CreateWorkflowResponse.

        当前工作流的必选参数是否都已填完。

        :param param_ready: The param_ready of this CreateWorkflowResponse.
        :type param_ready: bool
        """
        self._param_ready = param_ready

    @property
    def source(self):
        r"""Gets the source of this CreateWorkflowResponse.

        工作流来源，可选值为ai_gallery，表示工作流是从AI Gallery导入的。

        :return: The source of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateWorkflowResponse.

        工作流来源，可选值为ai_gallery，表示工作流是从AI Gallery导入的。

        :param source: The source of this CreateWorkflowResponse.
        :type source: str
        """
        self._source = source

    @property
    def storages(self):
        r"""Gets the storages of this CreateWorkflowResponse.

        Workflow包含的统一存储定义。

        :return: The storages of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        r"""Sets the storages of this CreateWorkflowResponse.

        Workflow包含的统一存储定义。

        :param storages: The storages of this CreateWorkflowResponse.
        :type storages: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowStorage`]
        """
        self._storages = storages

    @property
    def labels(self):
        r"""Gets the labels of this CreateWorkflowResponse.

        为Workflow工作流设置的标签。

        :return: The labels of this CreateWorkflowResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateWorkflowResponse.

        为Workflow工作流设置的标签。

        :param labels: The labels of this CreateWorkflowResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def assets(self):
        r"""Gets the assets of this CreateWorkflowResponse.

        工作流绑定的资产。

        :return: The assets of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowAsset`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this CreateWorkflowResponse.

        工作流绑定的资产。

        :param assets: The assets of this CreateWorkflowResponse.
        :type assets: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowAsset`]
        """
        self._assets = assets

    @property
    def sub_graphs(self):
        r"""Gets the sub_graphs of this CreateWorkflowResponse.

        工作流包含的子图。

        :return: The sub_graphs of this CreateWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        """
        return self._sub_graphs

    @sub_graphs.setter
    def sub_graphs(self, sub_graphs):
        r"""Sets the sub_graphs of this CreateWorkflowResponse.

        工作流包含的子图。

        :param sub_graphs: The sub_graphs of this CreateWorkflowResponse.
        :type sub_graphs: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        """
        self._sub_graphs = sub_graphs

    @property
    def extend(self):
        r"""Gets the extend of this CreateWorkflowResponse.

        计费工作流使用的拓展字段。

        :return: The extend of this CreateWorkflowResponse.
        :rtype: dict(str, object)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this CreateWorkflowResponse.

        计费工作流使用的拓展字段。

        :param extend: The extend of this CreateWorkflowResponse.
        :type extend: dict(str, object)
        """
        self._extend = extend

    @property
    def policy(self):
        r"""Gets the policy of this CreateWorkflowResponse.

        :return: The policy of this CreateWorkflowResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this CreateWorkflowResponse.

        :param policy: The policy of this CreateWorkflowResponse.
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowPolicy`
        """
        self._policy = policy

    @property
    def with_subscription(self):
        r"""Gets the with_subscription of this CreateWorkflowResponse.

        工作流SMN消息订阅开关，默认为false，表示关闭消息订阅开关。

        :return: The with_subscription of this CreateWorkflowResponse.
        :rtype: bool
        """
        return self._with_subscription

    @with_subscription.setter
    def with_subscription(self, with_subscription):
        r"""Sets the with_subscription of this CreateWorkflowResponse.

        工作流SMN消息订阅开关，默认为false，表示关闭消息订阅开关。

        :param with_subscription: The with_subscription of this CreateWorkflowResponse.
        :type with_subscription: bool
        """
        self._with_subscription = with_subscription

    @property
    def smn_switch(self):
        r"""Gets the smn_switch of this CreateWorkflowResponse.

        SMN开关。

        :return: The smn_switch of this CreateWorkflowResponse.
        :rtype: bool
        """
        return self._smn_switch

    @smn_switch.setter
    def smn_switch(self, smn_switch):
        r"""Sets the smn_switch of this CreateWorkflowResponse.

        SMN开关。

        :param smn_switch: The smn_switch of this CreateWorkflowResponse.
        :type smn_switch: bool
        """
        self._smn_switch = smn_switch

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this CreateWorkflowResponse.

        SMN消息订阅ID。

        :return: The subscription_id of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this CreateWorkflowResponse.

        SMN消息订阅ID。

        :param subscription_id: The subscription_id of this CreateWorkflowResponse.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def exeml_template_id(self):
        r"""Gets the exeml_template_id of this CreateWorkflowResponse.

        自动学习模板ID。

        :return: The exeml_template_id of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._exeml_template_id

    @exeml_template_id.setter
    def exeml_template_id(self, exeml_template_id):
        r"""Sets the exeml_template_id of this CreateWorkflowResponse.

        自动学习模板ID。

        :param exeml_template_id: The exeml_template_id of this CreateWorkflowResponse.
        :type exeml_template_id: str
        """
        self._exeml_template_id = exeml_template_id

    @property
    def last_modified_at(self):
        r"""Gets the last_modified_at of this CreateWorkflowResponse.

        最近一次修改的时间。

        :return: The last_modified_at of this CreateWorkflowResponse.
        :rtype: str
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        r"""Sets the last_modified_at of this CreateWorkflowResponse.

        最近一次修改的时间。

        :param last_modified_at: The last_modified_at of this CreateWorkflowResponse.
        :type last_modified_at: str
        """
        self._last_modified_at = last_modified_at

    @property
    def package(self):
        r"""Gets the package of this CreateWorkflowResponse.

        :return: The package of this CreateWorkflowResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowServicePackege`
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this CreateWorkflowResponse.

        :param package: The package of this CreateWorkflowResponse.
        :type package: :class:`huaweicloudsdkmodelarts.v1.WorkflowServicePackege`
        """
        self._package = package

    def to_dict(self):
        import warnings
        warnings.warn("CreateWorkflowResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
