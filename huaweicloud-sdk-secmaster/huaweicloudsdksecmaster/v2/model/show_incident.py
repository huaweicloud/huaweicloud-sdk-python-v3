# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIncident:

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
        'environment': 'IncidentEnvironment',
        'datasource': 'IncidentDatasource',
        'first_observed_time': 'str',
        'last_observed_time': 'str',
        'create_time': 'str',
        'arrive_time': 'str',
        'title': 'str',
        'description': 'str',
        'source_url': 'str',
        'count': 'str',
        'confidence': 'int',
        'serverity': 'str',
        'criticality': 'int',
        'incident_type': 'object',
        'network_list': 'list[CreateIncidentNetworkList]',
        'resource_list': 'list[CreateIncidentResourceList]',
        'remediation': 'ShowAlertRspRemediation',
        'verification_state': 'str',
        'handle_status': 'str',
        'sla': 'int',
        'update_time': 'str',
        'close_time': 'str',
        'chop_phase': 'str',
        'ipdrr_phase': 'str',
        'ppdr_phase': 'str',
        'simulation': 'str',
        'actor': 'str',
        'owner': 'str',
        'cteator': 'str',
        'close_reason': 'str',
        'close_comment': 'str',
        'malware': 'CreateIncidentMalware',
        'system_info': 'object',
        'process': 'list[CreateIncidentProcess]',
        'user_info': 'list[CreateIncidentUserInfo]',
        'file_info': 'list[ShowAlertRspFileInfo]',
        'system_incident_table': 'object',
        'id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'version': 'version',
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
        'serverity': 'serverity',
        'criticality': 'criticality',
        'incident_type': 'incident_type',
        'network_list': 'network_list',
        'resource_list': 'resource_list',
        'remediation': 'remediation',
        'verification_state': 'verification_state',
        'handle_status': 'handle_status',
        'sla': 'sla',
        'update_time': 'update_time',
        'close_time': 'close_time',
        'chop_phase': 'chop_phase',
        'ipdrr_phase': 'ipdrr_phase',
        'ppdr_phase': 'ppdr_phase',
        'simulation': 'simulation',
        'actor': 'actor',
        'owner': 'owner',
        'cteator': 'cteator',
        'close_reason': 'close_reason',
        'close_comment': 'close_comment',
        'malware': 'malware',
        'system_info': 'system_info',
        'process': 'process',
        'user_info': 'user_info',
        'file_info': 'file_info',
        'system_incident_table': 'system_incident_table',
        'id': 'id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, version=None, environment=None, datasource=None, first_observed_time=None, last_observed_time=None, create_time=None, arrive_time=None, title=None, description=None, source_url=None, count=None, confidence=None, serverity=None, criticality=None, incident_type=None, network_list=None, resource_list=None, remediation=None, verification_state=None, handle_status=None, sla=None, update_time=None, close_time=None, chop_phase=None, ipdrr_phase=None, ppdr_phase=None, simulation=None, actor=None, owner=None, cteator=None, close_reason=None, close_comment=None, malware=None, system_info=None, process=None, user_info=None, file_info=None, system_incident_table=None, id=None, workspace_id=None):
        """ShowIncident

        The model defined in huaweicloud sdk

        :param version: 版本
        :type version: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v2.IncidentEnvironment`
        :param datasource: 
        :type datasource: :class:`huaweicloudsdksecmaster.v2.IncidentDatasource`
        :param first_observed_time: Update time
        :type first_observed_time: str
        :param last_observed_time: Update time
        :type last_observed_time: str
        :param create_time: Create time
        :type create_time: str
        :param arrive_time: Update time
        :type arrive_time: str
        :param title: The name, display only
        :type title: str
        :param description: The description, display only
        :type description: str
        :param source_url: 事件URL链接
        :type source_url: str
        :param count: 事件发生次数
        :type count: str
        :param confidence: 置信度
        :type confidence: int
        :param serverity: 严重性等级
        :type serverity: str
        :param criticality: 关键性，是指事件涉及的资源的重要性级别。
        :type criticality: int
        :param incident_type: 事件分类
        :type incident_type: object
        :param network_list: network_list
        :type network_list: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentNetworkList`]
        :param resource_list: network_list
        :type resource_list: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentResourceList`]
        :param remediation: 
        :type remediation: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspRemediation`
        :param verification_state: 验证状态
        :type verification_state: str
        :param handle_status: 事件处理状态
        :type handle_status: str
        :param sla: sla
        :type sla: int
        :param update_time: Create time
        :type update_time: str
        :param close_time: Create time
        :type close_time: str
        :param chop_phase: 周期/处置阶段编号
        :type chop_phase: str
        :param ipdrr_phase: 周期/处置阶段编号
        :type ipdrr_phase: str
        :param ppdr_phase: 周期/处置阶段编号
        :type ppdr_phase: str
        :param simulation: 是否为调试事件.
        :type simulation: str
        :param actor: 委托人
        :type actor: str
        :param owner: The name, display only
        :type owner: str
        :param cteator: The name, display only
        :type cteator: str
        :param close_reason: 关闭原因
        :type close_reason: str
        :param close_comment: 关闭原因
        :type close_comment: str
        :param malware: 
        :type malware: :class:`huaweicloudsdksecmaster.v2.CreateIncidentMalware`
        :param system_info: 系统信息
        :type system_info: object
        :param process: 进程信息
        :type process: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentProcess`]
        :param user_info: 用户信息
        :type user_info: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentUserInfo`]
        :param file_info: 文件信息
        :type file_info: list[:class:`huaweicloudsdksecmaster.v2.ShowAlertRspFileInfo`]
        :param system_incident_table: 系统信息
        :type system_incident_table: object
        :param id: Id value
        :type id: str
        :param workspace_id: workspace id
        :type workspace_id: str
        """
        
        

        self._version = None
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
        self._serverity = None
        self._criticality = None
        self._incident_type = None
        self._network_list = None
        self._resource_list = None
        self._remediation = None
        self._verification_state = None
        self._handle_status = None
        self._sla = None
        self._update_time = None
        self._close_time = None
        self._chop_phase = None
        self._ipdrr_phase = None
        self._ppdr_phase = None
        self._simulation = None
        self._actor = None
        self._owner = None
        self._cteator = None
        self._close_reason = None
        self._close_comment = None
        self._malware = None
        self._system_info = None
        self._process = None
        self._user_info = None
        self._file_info = None
        self._system_incident_table = None
        self._id = None
        self._workspace_id = None
        self.discriminator = None

        if version is not None:
            self.version = version
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
        if serverity is not None:
            self.serverity = serverity
        if criticality is not None:
            self.criticality = criticality
        if incident_type is not None:
            self.incident_type = incident_type
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
        if chop_phase is not None:
            self.chop_phase = chop_phase
        if ipdrr_phase is not None:
            self.ipdrr_phase = ipdrr_phase
        if ppdr_phase is not None:
            self.ppdr_phase = ppdr_phase
        if simulation is not None:
            self.simulation = simulation
        if actor is not None:
            self.actor = actor
        if owner is not None:
            self.owner = owner
        if cteator is not None:
            self.cteator = cteator
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
        if system_incident_table is not None:
            self.system_incident_table = system_incident_table
        if id is not None:
            self.id = id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def version(self):
        """Gets the version of this ShowIncident.

        版本

        :return: The version of this ShowIncident.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowIncident.

        版本

        :param version: The version of this ShowIncident.
        :type version: str
        """
        self._version = version

    @property
    def environment(self):
        """Gets the environment of this ShowIncident.

        :return: The environment of this ShowIncident.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IncidentEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ShowIncident.

        :param environment: The environment of this ShowIncident.
        :type environment: :class:`huaweicloudsdksecmaster.v2.IncidentEnvironment`
        """
        self._environment = environment

    @property
    def datasource(self):
        """Gets the datasource of this ShowIncident.

        :return: The datasource of this ShowIncident.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IncidentDatasource`
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this ShowIncident.

        :param datasource: The datasource of this ShowIncident.
        :type datasource: :class:`huaweicloudsdksecmaster.v2.IncidentDatasource`
        """
        self._datasource = datasource

    @property
    def first_observed_time(self):
        """Gets the first_observed_time of this ShowIncident.

        Update time

        :return: The first_observed_time of this ShowIncident.
        :rtype: str
        """
        return self._first_observed_time

    @first_observed_time.setter
    def first_observed_time(self, first_observed_time):
        """Sets the first_observed_time of this ShowIncident.

        Update time

        :param first_observed_time: The first_observed_time of this ShowIncident.
        :type first_observed_time: str
        """
        self._first_observed_time = first_observed_time

    @property
    def last_observed_time(self):
        """Gets the last_observed_time of this ShowIncident.

        Update time

        :return: The last_observed_time of this ShowIncident.
        :rtype: str
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time):
        """Sets the last_observed_time of this ShowIncident.

        Update time

        :param last_observed_time: The last_observed_time of this ShowIncident.
        :type last_observed_time: str
        """
        self._last_observed_time = last_observed_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowIncident.

        Create time

        :return: The create_time of this ShowIncident.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowIncident.

        Create time

        :param create_time: The create_time of this ShowIncident.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def arrive_time(self):
        """Gets the arrive_time of this ShowIncident.

        Update time

        :return: The arrive_time of this ShowIncident.
        :rtype: str
        """
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, arrive_time):
        """Sets the arrive_time of this ShowIncident.

        Update time

        :param arrive_time: The arrive_time of this ShowIncident.
        :type arrive_time: str
        """
        self._arrive_time = arrive_time

    @property
    def title(self):
        """Gets the title of this ShowIncident.

        The name, display only

        :return: The title of this ShowIncident.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowIncident.

        The name, display only

        :param title: The title of this ShowIncident.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this ShowIncident.

        The description, display only

        :return: The description of this ShowIncident.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowIncident.

        The description, display only

        :param description: The description of this ShowIncident.
        :type description: str
        """
        self._description = description

    @property
    def source_url(self):
        """Gets the source_url of this ShowIncident.

        事件URL链接

        :return: The source_url of this ShowIncident.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this ShowIncident.

        事件URL链接

        :param source_url: The source_url of this ShowIncident.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def count(self):
        """Gets the count of this ShowIncident.

        事件发生次数

        :return: The count of this ShowIncident.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowIncident.

        事件发生次数

        :param count: The count of this ShowIncident.
        :type count: str
        """
        self._count = count

    @property
    def confidence(self):
        """Gets the confidence of this ShowIncident.

        置信度

        :return: The confidence of this ShowIncident.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ShowIncident.

        置信度

        :param confidence: The confidence of this ShowIncident.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def serverity(self):
        """Gets the serverity of this ShowIncident.

        严重性等级

        :return: The serverity of this ShowIncident.
        :rtype: str
        """
        return self._serverity

    @serverity.setter
    def serverity(self, serverity):
        """Sets the serverity of this ShowIncident.

        严重性等级

        :param serverity: The serverity of this ShowIncident.
        :type serverity: str
        """
        self._serverity = serverity

    @property
    def criticality(self):
        """Gets the criticality of this ShowIncident.

        关键性，是指事件涉及的资源的重要性级别。

        :return: The criticality of this ShowIncident.
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this ShowIncident.

        关键性，是指事件涉及的资源的重要性级别。

        :param criticality: The criticality of this ShowIncident.
        :type criticality: int
        """
        self._criticality = criticality

    @property
    def incident_type(self):
        """Gets the incident_type of this ShowIncident.

        事件分类

        :return: The incident_type of this ShowIncident.
        :rtype: object
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        """Sets the incident_type of this ShowIncident.

        事件分类

        :param incident_type: The incident_type of this ShowIncident.
        :type incident_type: object
        """
        self._incident_type = incident_type

    @property
    def network_list(self):
        """Gets the network_list of this ShowIncident.

        network_list

        :return: The network_list of this ShowIncident.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentNetworkList`]
        """
        return self._network_list

    @network_list.setter
    def network_list(self, network_list):
        """Sets the network_list of this ShowIncident.

        network_list

        :param network_list: The network_list of this ShowIncident.
        :type network_list: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentNetworkList`]
        """
        self._network_list = network_list

    @property
    def resource_list(self):
        """Gets the resource_list of this ShowIncident.

        network_list

        :return: The resource_list of this ShowIncident.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentResourceList`]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """Sets the resource_list of this ShowIncident.

        network_list

        :param resource_list: The resource_list of this ShowIncident.
        :type resource_list: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentResourceList`]
        """
        self._resource_list = resource_list

    @property
    def remediation(self):
        """Gets the remediation of this ShowIncident.

        :return: The remediation of this ShowIncident.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspRemediation`
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this ShowIncident.

        :param remediation: The remediation of this ShowIncident.
        :type remediation: :class:`huaweicloudsdksecmaster.v2.ShowAlertRspRemediation`
        """
        self._remediation = remediation

    @property
    def verification_state(self):
        """Gets the verification_state of this ShowIncident.

        验证状态

        :return: The verification_state of this ShowIncident.
        :rtype: str
        """
        return self._verification_state

    @verification_state.setter
    def verification_state(self, verification_state):
        """Sets the verification_state of this ShowIncident.

        验证状态

        :param verification_state: The verification_state of this ShowIncident.
        :type verification_state: str
        """
        self._verification_state = verification_state

    @property
    def handle_status(self):
        """Gets the handle_status of this ShowIncident.

        事件处理状态

        :return: The handle_status of this ShowIncident.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this ShowIncident.

        事件处理状态

        :param handle_status: The handle_status of this ShowIncident.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def sla(self):
        """Gets the sla of this ShowIncident.

        sla

        :return: The sla of this ShowIncident.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this ShowIncident.

        sla

        :param sla: The sla of this ShowIncident.
        :type sla: int
        """
        self._sla = sla

    @property
    def update_time(self):
        """Gets the update_time of this ShowIncident.

        Create time

        :return: The update_time of this ShowIncident.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowIncident.

        Create time

        :param update_time: The update_time of this ShowIncident.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def close_time(self):
        """Gets the close_time of this ShowIncident.

        Create time

        :return: The close_time of this ShowIncident.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this ShowIncident.

        Create time

        :param close_time: The close_time of this ShowIncident.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def chop_phase(self):
        """Gets the chop_phase of this ShowIncident.

        周期/处置阶段编号

        :return: The chop_phase of this ShowIncident.
        :rtype: str
        """
        return self._chop_phase

    @chop_phase.setter
    def chop_phase(self, chop_phase):
        """Sets the chop_phase of this ShowIncident.

        周期/处置阶段编号

        :param chop_phase: The chop_phase of this ShowIncident.
        :type chop_phase: str
        """
        self._chop_phase = chop_phase

    @property
    def ipdrr_phase(self):
        """Gets the ipdrr_phase of this ShowIncident.

        周期/处置阶段编号

        :return: The ipdrr_phase of this ShowIncident.
        :rtype: str
        """
        return self._ipdrr_phase

    @ipdrr_phase.setter
    def ipdrr_phase(self, ipdrr_phase):
        """Sets the ipdrr_phase of this ShowIncident.

        周期/处置阶段编号

        :param ipdrr_phase: The ipdrr_phase of this ShowIncident.
        :type ipdrr_phase: str
        """
        self._ipdrr_phase = ipdrr_phase

    @property
    def ppdr_phase(self):
        """Gets the ppdr_phase of this ShowIncident.

        周期/处置阶段编号

        :return: The ppdr_phase of this ShowIncident.
        :rtype: str
        """
        return self._ppdr_phase

    @ppdr_phase.setter
    def ppdr_phase(self, ppdr_phase):
        """Sets the ppdr_phase of this ShowIncident.

        周期/处置阶段编号

        :param ppdr_phase: The ppdr_phase of this ShowIncident.
        :type ppdr_phase: str
        """
        self._ppdr_phase = ppdr_phase

    @property
    def simulation(self):
        """Gets the simulation of this ShowIncident.

        是否为调试事件.

        :return: The simulation of this ShowIncident.
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ShowIncident.

        是否为调试事件.

        :param simulation: The simulation of this ShowIncident.
        :type simulation: str
        """
        self._simulation = simulation

    @property
    def actor(self):
        """Gets the actor of this ShowIncident.

        委托人

        :return: The actor of this ShowIncident.
        :rtype: str
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this ShowIncident.

        委托人

        :param actor: The actor of this ShowIncident.
        :type actor: str
        """
        self._actor = actor

    @property
    def owner(self):
        """Gets the owner of this ShowIncident.

        The name, display only

        :return: The owner of this ShowIncident.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowIncident.

        The name, display only

        :param owner: The owner of this ShowIncident.
        :type owner: str
        """
        self._owner = owner

    @property
    def cteator(self):
        """Gets the cteator of this ShowIncident.

        The name, display only

        :return: The cteator of this ShowIncident.
        :rtype: str
        """
        return self._cteator

    @cteator.setter
    def cteator(self, cteator):
        """Sets the cteator of this ShowIncident.

        The name, display only

        :param cteator: The cteator of this ShowIncident.
        :type cteator: str
        """
        self._cteator = cteator

    @property
    def close_reason(self):
        """Gets the close_reason of this ShowIncident.

        关闭原因

        :return: The close_reason of this ShowIncident.
        :rtype: str
        """
        return self._close_reason

    @close_reason.setter
    def close_reason(self, close_reason):
        """Sets the close_reason of this ShowIncident.

        关闭原因

        :param close_reason: The close_reason of this ShowIncident.
        :type close_reason: str
        """
        self._close_reason = close_reason

    @property
    def close_comment(self):
        """Gets the close_comment of this ShowIncident.

        关闭原因

        :return: The close_comment of this ShowIncident.
        :rtype: str
        """
        return self._close_comment

    @close_comment.setter
    def close_comment(self, close_comment):
        """Sets the close_comment of this ShowIncident.

        关闭原因

        :param close_comment: The close_comment of this ShowIncident.
        :type close_comment: str
        """
        self._close_comment = close_comment

    @property
    def malware(self):
        """Gets the malware of this ShowIncident.

        :return: The malware of this ShowIncident.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIncidentMalware`
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        """Sets the malware of this ShowIncident.

        :param malware: The malware of this ShowIncident.
        :type malware: :class:`huaweicloudsdksecmaster.v2.CreateIncidentMalware`
        """
        self._malware = malware

    @property
    def system_info(self):
        """Gets the system_info of this ShowIncident.

        系统信息

        :return: The system_info of this ShowIncident.
        :rtype: object
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this ShowIncident.

        系统信息

        :param system_info: The system_info of this ShowIncident.
        :type system_info: object
        """
        self._system_info = system_info

    @property
    def process(self):
        """Gets the process of this ShowIncident.

        进程信息

        :return: The process of this ShowIncident.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentProcess`]
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this ShowIncident.

        进程信息

        :param process: The process of this ShowIncident.
        :type process: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentProcess`]
        """
        self._process = process

    @property
    def user_info(self):
        """Gets the user_info of this ShowIncident.

        用户信息

        :return: The user_info of this ShowIncident.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentUserInfo`]
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this ShowIncident.

        用户信息

        :param user_info: The user_info of this ShowIncident.
        :type user_info: list[:class:`huaweicloudsdksecmaster.v2.CreateIncidentUserInfo`]
        """
        self._user_info = user_info

    @property
    def file_info(self):
        """Gets the file_info of this ShowIncident.

        文件信息

        :return: The file_info of this ShowIncident.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ShowAlertRspFileInfo`]
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        """Sets the file_info of this ShowIncident.

        文件信息

        :param file_info: The file_info of this ShowIncident.
        :type file_info: list[:class:`huaweicloudsdksecmaster.v2.ShowAlertRspFileInfo`]
        """
        self._file_info = file_info

    @property
    def system_incident_table(self):
        """Gets the system_incident_table of this ShowIncident.

        系统信息

        :return: The system_incident_table of this ShowIncident.
        :rtype: object
        """
        return self._system_incident_table

    @system_incident_table.setter
    def system_incident_table(self, system_incident_table):
        """Sets the system_incident_table of this ShowIncident.

        系统信息

        :param system_incident_table: The system_incident_table of this ShowIncident.
        :type system_incident_table: object
        """
        self._system_incident_table = system_incident_table

    @property
    def id(self):
        """Gets the id of this ShowIncident.

        Id value

        :return: The id of this ShowIncident.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowIncident.

        Id value

        :param id: The id of this ShowIncident.
        :type id: str
        """
        self._id = id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ShowIncident.

        workspace id

        :return: The workspace_id of this ShowIncident.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ShowIncident.

        workspace id

        :param workspace_id: The workspace_id of this ShowIncident.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ShowIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
