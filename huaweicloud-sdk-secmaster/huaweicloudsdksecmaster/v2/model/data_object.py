# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'id': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'workspace_id': 'str',
        'environment': 'AlertEnvironment',
        'datasource': 'AlertDataSource',
        'first_observed_time': 'str',
        'last_observed_time': 'str',
        'create_time': 'str',
        'arrive_time': 'str',
        'title': 'str',
        'description': 'str',
        'source_url': 'str',
        'count': 'int',
        'confidence': 'int',
        'severity': 'str',
        'criticality': 'int',
        'alert_type': 'AlertAlertType',
        'network_list': 'list[AlertNetworkList]',
        'resource_list': 'list[AlertResourceList]',
        'remediation': 'AlertRemediation',
        'verification_state': 'str',
        'handle_status': 'str',
        'sla': 'int',
        'update_time': 'str',
        'close_time': 'str',
        'ipdrr_phase': 'str',
        'simulation': 'str',
        'actor': 'str',
        'owner': 'str',
        'creator': 'str',
        'close_reason': 'str',
        'close_comment': 'str',
        'malware': 'ShowAlertRspMalware',
        'system_info': 'object',
        'process': 'list[AlertProcess]',
        'user_info': 'list[AlertUserInfo]',
        'file_info': 'list[AlertFileInfo]'
    }

    attribute_map = {
        'version': 'version',
        'id': 'id',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'workspace_id': 'workspace_id',
        'environment': 'environment',
        'datasource': 'datasource',
        'first_observed_time': 'first_observed_time',
        'last_observed_time': 'last_observed_time',
        'create_time': 'create_time',
        'arrive_time': 'arrive_time',
        'title': 'title',
        'description': 'description',
        'source_url': 'source_url',
        'count': 'count',
        'confidence': 'confidence',
        'severity': 'severity',
        'criticality': 'criticality',
        'alert_type': 'alert_type',
        'network_list': 'network_list',
        'resource_list': 'resource_list',
        'remediation': 'remediation',
        'verification_state': 'verification_state',
        'handle_status': 'handle_status',
        'sla': 'sla',
        'update_time': 'update_time',
        'close_time': 'close_time',
        'ipdrr_phase': 'ipdrr_phase',
        'simulation': 'simulation',
        'actor': 'actor',
        'owner': 'owner',
        'creator': 'creator',
        'close_reason': 'close_reason',
        'close_comment': 'close_comment',
        'malware': 'malware',
        'system_info': 'system_info',
        'process': 'process',
        'user_info': 'user_info',
        'file_info': 'file_info'
    }

    def __init__(self, version=None, id=None, domain_id=None, region_id=None, workspace_id=None, environment=None, datasource=None, first_observed_time=None, last_observed_time=None, create_time=None, arrive_time=None, title=None, description=None, source_url=None, count=None, confidence=None, severity=None, criticality=None, alert_type=None, network_list=None, resource_list=None, remediation=None, verification_state=None, handle_status=None, sla=None, update_time=None, close_time=None, ipdrr_phase=None, simulation=None, actor=None, owner=None, creator=None, close_reason=None, close_comment=None, malware=None, system_info=None, process=None, user_info=None, file_info=None):
        """DataObject

        The model defined in huaweicloud sdk

        :param version: 告警对象的版本，该字段的值必须为华为云SSA服务确定的官方发布版本之一
        :type version: str
        :param id: 事件唯一标识，UUID格式，最大36个字符
        :type id: str
        :param domain_id: 数据投递后，被委托用户的domain_id
        :type domain_id: str
        :param region_id: 数据投递后，被委托用户的region_id
        :type region_id: str
        :param workspace_id: 当前的工作空间id
        :type workspace_id: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v2.AlertEnvironment`
        :param datasource: 
        :type datasource: :class:`huaweicloudsdksecmaster.v2.AlertDataSource`
        :param first_observed_time: 首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type first_observed_time: str
        :param last_observed_time: 最近发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type last_observed_time: str
        :param create_time: 记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type create_time: str
        :param arrive_time: 接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type arrive_time: str
        :param title: 告警标题
        :type title: str
        :param description: 告警描述信息
        :type description: str
        :param source_url: 告警URL链接，指向数据源产品中有关当前事件说明的页面
        :type source_url: str
        :param count: 事件发生次数
        :type count: int
        :param confidence: 事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%
        :type confidence: int
        :param severity: 严重性等级，取值范围：Tips | Low | Medium | High | Fatal 说明： 0: Tips – 未发现任何问题。 1: Low – 无需针对问题执行任何操作。 2: Medium – 问题需要处理，但不紧急。 3: High – 问题必须优先处理。 4: Fatal – 问题必须立即处理，以防止产生进一步的损害
        :type severity: str
        :param criticality: 关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源
        :type criticality: int
        :param alert_type: 
        :type alert_type: :class:`huaweicloudsdksecmaster.v2.AlertAlertType`
        :param network_list: 网络信息
        :type network_list: list[:class:`huaweicloudsdksecmaster.v2.AlertNetworkList`]
        :param resource_list: 受影响资源
        :type resource_list: list[:class:`huaweicloudsdksecmaster.v2.AlertResourceList`]
        :param remediation: 
        :type remediation: :class:`huaweicloudsdksecmaster.v2.AlertRemediation`
        :param verification_state: 验证状态，标识事件的准确性。可选类型如下： Unknown – 未知 True_Positive – 确认 False_Positive – 误报 默认填写Unknown
        :type verification_state: str
        :param handle_status: 事件处理状态，可选类型如下： Open – 打开，默认 Block – 阻塞 Closed – 关闭 默认填写Open
        :type handle_status: str
        :param sla: 约束闭环时间：设置风险接受持续时间。单位：小时
        :type sla: int
        :param update_time: 更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type update_time: str
        :param close_time: 关闭时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type close_time: str
        :param ipdrr_phase: 周期/处置阶段编号 Prepartion|Detection and Analysis|Containm，Eradication&amp; Recovery|Post-Incident-Activity
        :type ipdrr_phase: str
        :param simulation: 调试字段
        :type simulation: str
        :param actor: 告警调查员
        :type actor: str
        :param owner: 责任人、服务责任人
        :type owner: str
        :param creator: 创建人
        :type creator: str
        :param close_reason: 关闭原因: 误检 - False detection 已解决 - Resolved 重复 - Repeated 其他 - Other
        :type close_reason: str
        :param close_comment: 关闭评论
        :type close_comment: str
        :param malware: 
        :type malware: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspMalware`
        :param system_info: 系统信息
        :type system_info: object
        :param process: 进程信息
        :type process: list[:class:`huaweicloudsdksecmaster.v2.AlertProcess`]
        :param user_info: 用户信息
        :type user_info: list[:class:`huaweicloudsdksecmaster.v2.AlertUserInfo`]
        :param file_info: 文件信息
        :type file_info: list[:class:`huaweicloudsdksecmaster.v2.AlertFileInfo`]
        """
        
        

        self._version = None
        self._id = None
        self._domain_id = None
        self._region_id = None
        self._workspace_id = None
        self._environment = None
        self._datasource = None
        self._first_observed_time = None
        self._last_observed_time = None
        self._create_time = None
        self._arrive_time = None
        self._title = None
        self._description = None
        self._source_url = None
        self._count = None
        self._confidence = None
        self._severity = None
        self._criticality = None
        self._alert_type = None
        self._network_list = None
        self._resource_list = None
        self._remediation = None
        self._verification_state = None
        self._handle_status = None
        self._sla = None
        self._update_time = None
        self._close_time = None
        self._ipdrr_phase = None
        self._simulation = None
        self._actor = None
        self._owner = None
        self._creator = None
        self._close_reason = None
        self._close_comment = None
        self._malware = None
        self._system_info = None
        self._process = None
        self._user_info = None
        self._file_info = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if environment is not None:
            self.environment = environment
        if datasource is not None:
            self.datasource = datasource
        if first_observed_time is not None:
            self.first_observed_time = first_observed_time
        if last_observed_time is not None:
            self.last_observed_time = last_observed_time
        if create_time is not None:
            self.create_time = create_time
        if arrive_time is not None:
            self.arrive_time = arrive_time
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if source_url is not None:
            self.source_url = source_url
        if count is not None:
            self.count = count
        if confidence is not None:
            self.confidence = confidence
        if severity is not None:
            self.severity = severity
        if criticality is not None:
            self.criticality = criticality
        if alert_type is not None:
            self.alert_type = alert_type
        if network_list is not None:
            self.network_list = network_list
        if resource_list is not None:
            self.resource_list = resource_list
        if remediation is not None:
            self.remediation = remediation
        if verification_state is not None:
            self.verification_state = verification_state
        if handle_status is not None:
            self.handle_status = handle_status
        if sla is not None:
            self.sla = sla
        if update_time is not None:
            self.update_time = update_time
        if close_time is not None:
            self.close_time = close_time
        if ipdrr_phase is not None:
            self.ipdrr_phase = ipdrr_phase
        if simulation is not None:
            self.simulation = simulation
        if actor is not None:
            self.actor = actor
        if owner is not None:
            self.owner = owner
        if creator is not None:
            self.creator = creator
        if close_reason is not None:
            self.close_reason = close_reason
        if close_comment is not None:
            self.close_comment = close_comment
        if malware is not None:
            self.malware = malware
        if system_info is not None:
            self.system_info = system_info
        if process is not None:
            self.process = process
        if user_info is not None:
            self.user_info = user_info
        if file_info is not None:
            self.file_info = file_info

    @property
    def version(self):
        """Gets the version of this DataObject.

        告警对象的版本，该字段的值必须为华为云SSA服务确定的官方发布版本之一

        :return: The version of this DataObject.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DataObject.

        告警对象的版本，该字段的值必须为华为云SSA服务确定的官方发布版本之一

        :param version: The version of this DataObject.
        :type version: str
        """
        self._version = version

    @property
    def id(self):
        """Gets the id of this DataObject.

        事件唯一标识，UUID格式，最大36个字符

        :return: The id of this DataObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataObject.

        事件唯一标识，UUID格式，最大36个字符

        :param id: The id of this DataObject.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this DataObject.

        数据投递后，被委托用户的domain_id

        :return: The domain_id of this DataObject.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DataObject.

        数据投递后，被委托用户的domain_id

        :param domain_id: The domain_id of this DataObject.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        """Gets the region_id of this DataObject.

        数据投递后，被委托用户的region_id

        :return: The region_id of this DataObject.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DataObject.

        数据投递后，被委托用户的region_id

        :param region_id: The region_id of this DataObject.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this DataObject.

        当前的工作空间id

        :return: The workspace_id of this DataObject.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this DataObject.

        当前的工作空间id

        :param workspace_id: The workspace_id of this DataObject.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def environment(self):
        """Gets the environment of this DataObject.

        :return: The environment of this DataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this DataObject.

        :param environment: The environment of this DataObject.
        :type environment: :class:`huaweicloudsdksecmaster.v2.AlertEnvironment`
        """
        self._environment = environment

    @property
    def datasource(self):
        """Gets the datasource of this DataObject.

        :return: The datasource of this DataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertDataSource`
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this DataObject.

        :param datasource: The datasource of this DataObject.
        :type datasource: :class:`huaweicloudsdksecmaster.v2.AlertDataSource`
        """
        self._datasource = datasource

    @property
    def first_observed_time(self):
        """Gets the first_observed_time of this DataObject.

        首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The first_observed_time of this DataObject.
        :rtype: str
        """
        return self._first_observed_time

    @first_observed_time.setter
    def first_observed_time(self, first_observed_time):
        """Sets the first_observed_time of this DataObject.

        首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param first_observed_time: The first_observed_time of this DataObject.
        :type first_observed_time: str
        """
        self._first_observed_time = first_observed_time

    @property
    def last_observed_time(self):
        """Gets the last_observed_time of this DataObject.

        最近发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The last_observed_time of this DataObject.
        :rtype: str
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time):
        """Sets the last_observed_time of this DataObject.

        最近发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param last_observed_time: The last_observed_time of this DataObject.
        :type last_observed_time: str
        """
        self._last_observed_time = last_observed_time

    @property
    def create_time(self):
        """Gets the create_time of this DataObject.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The create_time of this DataObject.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataObject.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param create_time: The create_time of this DataObject.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def arrive_time(self):
        """Gets the arrive_time of this DataObject.

        接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The arrive_time of this DataObject.
        :rtype: str
        """
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, arrive_time):
        """Sets the arrive_time of this DataObject.

        接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param arrive_time: The arrive_time of this DataObject.
        :type arrive_time: str
        """
        self._arrive_time = arrive_time

    @property
    def title(self):
        """Gets the title of this DataObject.

        告警标题

        :return: The title of this DataObject.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DataObject.

        告警标题

        :param title: The title of this DataObject.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this DataObject.

        告警描述信息

        :return: The description of this DataObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataObject.

        告警描述信息

        :param description: The description of this DataObject.
        :type description: str
        """
        self._description = description

    @property
    def source_url(self):
        """Gets the source_url of this DataObject.

        告警URL链接，指向数据源产品中有关当前事件说明的页面

        :return: The source_url of this DataObject.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this DataObject.

        告警URL链接，指向数据源产品中有关当前事件说明的页面

        :param source_url: The source_url of this DataObject.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def count(self):
        """Gets the count of this DataObject.

        事件发生次数

        :return: The count of this DataObject.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DataObject.

        事件发生次数

        :param count: The count of this DataObject.
        :type count: int
        """
        self._count = count

    @property
    def confidence(self):
        """Gets the confidence of this DataObject.

        事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%

        :return: The confidence of this DataObject.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this DataObject.

        事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%

        :param confidence: The confidence of this DataObject.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def severity(self):
        """Gets the severity of this DataObject.

        严重性等级，取值范围：Tips | Low | Medium | High | Fatal 说明： 0: Tips – 未发现任何问题。 1: Low – 无需针对问题执行任何操作。 2: Medium – 问题需要处理，但不紧急。 3: High – 问题必须优先处理。 4: Fatal – 问题必须立即处理，以防止产生进一步的损害

        :return: The severity of this DataObject.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this DataObject.

        严重性等级，取值范围：Tips | Low | Medium | High | Fatal 说明： 0: Tips – 未发现任何问题。 1: Low – 无需针对问题执行任何操作。 2: Medium – 问题需要处理，但不紧急。 3: High – 问题必须优先处理。 4: Fatal – 问题必须立即处理，以防止产生进一步的损害

        :param severity: The severity of this DataObject.
        :type severity: str
        """
        self._severity = severity

    @property
    def criticality(self):
        """Gets the criticality of this DataObject.

        关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源

        :return: The criticality of this DataObject.
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this DataObject.

        关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源

        :param criticality: The criticality of this DataObject.
        :type criticality: int
        """
        self._criticality = criticality

    @property
    def alert_type(self):
        """Gets the alert_type of this DataObject.

        :return: The alert_type of this DataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertAlertType`
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this DataObject.

        :param alert_type: The alert_type of this DataObject.
        :type alert_type: :class:`huaweicloudsdksecmaster.v2.AlertAlertType`
        """
        self._alert_type = alert_type

    @property
    def network_list(self):
        """Gets the network_list of this DataObject.

        网络信息

        :return: The network_list of this DataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertNetworkList`]
        """
        return self._network_list

    @network_list.setter
    def network_list(self, network_list):
        """Sets the network_list of this DataObject.

        网络信息

        :param network_list: The network_list of this DataObject.
        :type network_list: list[:class:`huaweicloudsdksecmaster.v2.AlertNetworkList`]
        """
        self._network_list = network_list

    @property
    def resource_list(self):
        """Gets the resource_list of this DataObject.

        受影响资源

        :return: The resource_list of this DataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertResourceList`]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """Sets the resource_list of this DataObject.

        受影响资源

        :param resource_list: The resource_list of this DataObject.
        :type resource_list: list[:class:`huaweicloudsdksecmaster.v2.AlertResourceList`]
        """
        self._resource_list = resource_list

    @property
    def remediation(self):
        """Gets the remediation of this DataObject.

        :return: The remediation of this DataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertRemediation`
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this DataObject.

        :param remediation: The remediation of this DataObject.
        :type remediation: :class:`huaweicloudsdksecmaster.v2.AlertRemediation`
        """
        self._remediation = remediation

    @property
    def verification_state(self):
        """Gets the verification_state of this DataObject.

        验证状态，标识事件的准确性。可选类型如下： Unknown – 未知 True_Positive – 确认 False_Positive – 误报 默认填写Unknown

        :return: The verification_state of this DataObject.
        :rtype: str
        """
        return self._verification_state

    @verification_state.setter
    def verification_state(self, verification_state):
        """Sets the verification_state of this DataObject.

        验证状态，标识事件的准确性。可选类型如下： Unknown – 未知 True_Positive – 确认 False_Positive – 误报 默认填写Unknown

        :param verification_state: The verification_state of this DataObject.
        :type verification_state: str
        """
        self._verification_state = verification_state

    @property
    def handle_status(self):
        """Gets the handle_status of this DataObject.

        事件处理状态，可选类型如下： Open – 打开，默认 Block – 阻塞 Closed – 关闭 默认填写Open

        :return: The handle_status of this DataObject.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this DataObject.

        事件处理状态，可选类型如下： Open – 打开，默认 Block – 阻塞 Closed – 关闭 默认填写Open

        :param handle_status: The handle_status of this DataObject.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def sla(self):
        """Gets the sla of this DataObject.

        约束闭环时间：设置风险接受持续时间。单位：小时

        :return: The sla of this DataObject.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this DataObject.

        约束闭环时间：设置风险接受持续时间。单位：小时

        :param sla: The sla of this DataObject.
        :type sla: int
        """
        self._sla = sla

    @property
    def update_time(self):
        """Gets the update_time of this DataObject.

        更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The update_time of this DataObject.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataObject.

        更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param update_time: The update_time of this DataObject.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def close_time(self):
        """Gets the close_time of this DataObject.

        关闭时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The close_time of this DataObject.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this DataObject.

        关闭时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param close_time: The close_time of this DataObject.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def ipdrr_phase(self):
        """Gets the ipdrr_phase of this DataObject.

        周期/处置阶段编号 Prepartion|Detection and Analysis|Containm，Eradication& Recovery|Post-Incident-Activity

        :return: The ipdrr_phase of this DataObject.
        :rtype: str
        """
        return self._ipdrr_phase

    @ipdrr_phase.setter
    def ipdrr_phase(self, ipdrr_phase):
        """Sets the ipdrr_phase of this DataObject.

        周期/处置阶段编号 Prepartion|Detection and Analysis|Containm，Eradication& Recovery|Post-Incident-Activity

        :param ipdrr_phase: The ipdrr_phase of this DataObject.
        :type ipdrr_phase: str
        """
        self._ipdrr_phase = ipdrr_phase

    @property
    def simulation(self):
        """Gets the simulation of this DataObject.

        调试字段

        :return: The simulation of this DataObject.
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this DataObject.

        调试字段

        :param simulation: The simulation of this DataObject.
        :type simulation: str
        """
        self._simulation = simulation

    @property
    def actor(self):
        """Gets the actor of this DataObject.

        告警调查员

        :return: The actor of this DataObject.
        :rtype: str
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this DataObject.

        告警调查员

        :param actor: The actor of this DataObject.
        :type actor: str
        """
        self._actor = actor

    @property
    def owner(self):
        """Gets the owner of this DataObject.

        责任人、服务责任人

        :return: The owner of this DataObject.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DataObject.

        责任人、服务责任人

        :param owner: The owner of this DataObject.
        :type owner: str
        """
        self._owner = owner

    @property
    def creator(self):
        """Gets the creator of this DataObject.

        创建人

        :return: The creator of this DataObject.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DataObject.

        创建人

        :param creator: The creator of this DataObject.
        :type creator: str
        """
        self._creator = creator

    @property
    def close_reason(self):
        """Gets the close_reason of this DataObject.

        关闭原因: 误检 - False detection 已解决 - Resolved 重复 - Repeated 其他 - Other

        :return: The close_reason of this DataObject.
        :rtype: str
        """
        return self._close_reason

    @close_reason.setter
    def close_reason(self, close_reason):
        """Sets the close_reason of this DataObject.

        关闭原因: 误检 - False detection 已解决 - Resolved 重复 - Repeated 其他 - Other

        :param close_reason: The close_reason of this DataObject.
        :type close_reason: str
        """
        self._close_reason = close_reason

    @property
    def close_comment(self):
        """Gets the close_comment of this DataObject.

        关闭评论

        :return: The close_comment of this DataObject.
        :rtype: str
        """
        return self._close_comment

    @close_comment.setter
    def close_comment(self, close_comment):
        """Sets the close_comment of this DataObject.

        关闭评论

        :param close_comment: The close_comment of this DataObject.
        :type close_comment: str
        """
        self._close_comment = close_comment

    @property
    def malware(self):
        """Gets the malware of this DataObject.

        :return: The malware of this DataObject.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspMalware`
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        """Sets the malware of this DataObject.

        :param malware: The malware of this DataObject.
        :type malware: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspMalware`
        """
        self._malware = malware

    @property
    def system_info(self):
        """Gets the system_info of this DataObject.

        系统信息

        :return: The system_info of this DataObject.
        :rtype: object
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this DataObject.

        系统信息

        :param system_info: The system_info of this DataObject.
        :type system_info: object
        """
        self._system_info = system_info

    @property
    def process(self):
        """Gets the process of this DataObject.

        进程信息

        :return: The process of this DataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertProcess`]
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this DataObject.

        进程信息

        :param process: The process of this DataObject.
        :type process: list[:class:`huaweicloudsdksecmaster.v2.AlertProcess`]
        """
        self._process = process

    @property
    def user_info(self):
        """Gets the user_info of this DataObject.

        用户信息

        :return: The user_info of this DataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertUserInfo`]
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this DataObject.

        用户信息

        :param user_info: The user_info of this DataObject.
        :type user_info: list[:class:`huaweicloudsdksecmaster.v2.AlertUserInfo`]
        """
        self._user_info = user_info

    @property
    def file_info(self):
        """Gets the file_info of this DataObject.

        文件信息

        :return: The file_info of this DataObject.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertFileInfo`]
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        """Sets the file_info of this DataObject.

        文件信息

        :param file_info: The file_info of this DataObject.
        :type file_info: list[:class:`huaweicloudsdksecmaster.v2.AlertFileInfo`]
        """
        self._file_info = file_info

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
        if not isinstance(other, DataObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
