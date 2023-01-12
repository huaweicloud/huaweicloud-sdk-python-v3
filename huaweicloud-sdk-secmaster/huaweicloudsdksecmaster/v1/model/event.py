# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

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
        'environment': 'Environment',
        'data_source': 'DataSource',
        'first_observed_time': 'datetime',
        'last_observed_time': 'datetime',
        'create_time': 'datetime',
        'arrive_time': 'datetime',
        'event_id': 'str',
        'title': 'str',
        'description': 'str',
        'source_url': 'str',
        'count': 'int',
        'confidence': 'int',
        'severity': 'Severity',
        'criticality': 'int',
        'type': 'Type',
        'compliance': 'Compliance',
        'network': 'Network',
        'vulnerability_patch': 'VulnerabilityPatch',
        'malware': 'Malware',
        'threat_intel': 'ThreatIntel',
        'resource': 'Resource',
        'remediation': 'Remediation',
        'data_source_fields': 'object',
        'verification_state': 'str',
        'handle_status': 'str',
        'phase': 'str',
        'sla': 'int'
    }

    attribute_map = {
        'version': 'version',
        'environment': 'environment',
        'data_source': 'data_source',
        'first_observed_time': 'first_observed_time',
        'last_observed_time': 'last_observed_time',
        'create_time': 'create_time',
        'arrive_time': 'arrive_time',
        'event_id': 'event_id',
        'title': 'title',
        'description': 'description',
        'source_url': 'source_url',
        'count': 'count',
        'confidence': 'confidence',
        'severity': 'severity',
        'criticality': 'criticality',
        'type': 'type',
        'compliance': 'compliance',
        'network': 'network',
        'vulnerability_patch': 'vulnerability_patch',
        'malware': 'malware',
        'threat_intel': 'threat_intel',
        'resource': 'resource',
        'remediation': 'remediation',
        'data_source_fields': 'data_source_fields',
        'verification_state': 'verification_state',
        'handle_status': 'handle_status',
        'phase': 'phase',
        'sla': 'sla'
    }

    def __init__(self, version=None, environment=None, data_source=None, first_observed_time=None, last_observed_time=None, create_time=None, arrive_time=None, event_id=None, title=None, description=None, source_url=None, count=None, confidence=None, severity=None, criticality=None, type=None, compliance=None, network=None, vulnerability_patch=None, malware=None, threat_intel=None, resource=None, remediation=None, data_source_fields=None, verification_state=None, handle_status=None, phase=None, sla=None):
        """Event

        The model defined in huaweicloud sdk

        :param version: SA数据对象版本号，数据接入时需携带版本号。版本号由SA服务团队负责更新，数据源只可填写SA给定的版本号。目前版本为1.0.0。
        :type version: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v1.Environment`
        :param data_source: 
        :type data_source: :class:`huaweicloudsdksecmaster.v1.DataSource`
        :param first_observed_time: 首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。
        :type first_observed_time: datetime
        :param last_observed_time: 最新发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。
        :type last_observed_time: datetime
        :param create_time: 记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。
        :type create_time: datetime
        :param arrive_time: 数据接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。  是指事件数据被SA侧接收的时间，由SA接收时填写，产品上报数据时不用填写。
        :type arrive_time: datetime
        :param event_id: 事件唯一标识，UUID格式。
        :type event_id: str
        :param title: 事件标题，最大255字符。
        :type title: str
        :param description: 事件描述信息，最大1024个字符
        :type description: str
        :param source_url: 事件URL链接，指向数据源产品中有关当前事件说明的页面。
        :type source_url: str
        :param count: 事件发生次数，默认为1，必填。
        :type count: int
        :param confidence: 事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%。
        :type confidence: int
        :param severity: 
        :type severity: :class:`huaweicloudsdksecmaster.v1.Severity`
        :param criticality: 关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源。
        :type criticality: int
        :param type: 
        :type type: :class:`huaweicloudsdksecmaster.v1.Type`
        :param compliance: 
        :type compliance: :class:`huaweicloudsdksecmaster.v1.Compliance`
        :param network: 
        :type network: :class:`huaweicloudsdksecmaster.v1.Network`
        :param vulnerability_patch: 
        :type vulnerability_patch: :class:`huaweicloudsdksecmaster.v1.VulnerabilityPatch`
        :param malware: 
        :type malware: :class:`huaweicloudsdksecmaster.v1.Malware`
        :param threat_intel: 
        :type threat_intel: :class:`huaweicloudsdksecmaster.v1.ThreatIntel`
        :param resource: 
        :type resource: :class:`huaweicloudsdksecmaster.v1.Resource`
        :param remediation: 
        :type remediation: :class:`huaweicloudsdksecmaster.v1.Remediation`
        :param data_source_fields: 数据源自定义信息，最多支持50个key/value对，约束条件： 1、该对象不能包含冗余数据，并且不能与已定义的SSA事件格式字段冲突。 2、字段名称可以包含字母数字字符、空格和以下符号：_ . / &#x3D; + \\ - @。 示例： \&quot;data_source_fields\&quot;: {     \&quot;key1\&quot;: \&quot;value1\&quot;,     \&quot;key2\&quot;, \&quot;value2\&quot;,   }
        :type data_source_fields: object
        :param verification_state: 事件验证状态，标识事件的准确性。 Unknown – 未知，默认 True_positive – 确认 False_positive – 误报。
        :type verification_state: str
        :param handle_status: 事件处理状态，New/Ignored/Resolved；默认New。
        :type handle_status: str
        :param phase: 阶段：Prepartion|Detection and Analysis|Containm，Eradication&amp; Recovery| Post-Incident-Activity。
        :type phase: str
        :param sla: 约束闭环时间：单位：天。
        :type sla: int
        """
        
        

        self._version = None
        self._environment = None
        self._data_source = None
        self._first_observed_time = None
        self._last_observed_time = None
        self._create_time = None
        self._arrive_time = None
        self._event_id = None
        self._title = None
        self._description = None
        self._source_url = None
        self._count = None
        self._confidence = None
        self._severity = None
        self._criticality = None
        self._type = None
        self._compliance = None
        self._network = None
        self._vulnerability_patch = None
        self._malware = None
        self._threat_intel = None
        self._resource = None
        self._remediation = None
        self._data_source_fields = None
        self._verification_state = None
        self._handle_status = None
        self._phase = None
        self._sla = None
        self.discriminator = None

        self.version = version
        self.environment = environment
        self.data_source = data_source
        self.first_observed_time = first_observed_time
        if last_observed_time is not None:
            self.last_observed_time = last_observed_time
        self.create_time = create_time
        if arrive_time is not None:
            self.arrive_time = arrive_time
        self.event_id = event_id
        self.title = title
        self.description = description
        if source_url is not None:
            self.source_url = source_url
        self.count = count
        if confidence is not None:
            self.confidence = confidence
        self.severity = severity
        if criticality is not None:
            self.criticality = criticality
        self.type = type
        if compliance is not None:
            self.compliance = compliance
        if network is not None:
            self.network = network
        if vulnerability_patch is not None:
            self.vulnerability_patch = vulnerability_patch
        if malware is not None:
            self.malware = malware
        if threat_intel is not None:
            self.threat_intel = threat_intel
        self.resource = resource
        if remediation is not None:
            self.remediation = remediation
        if data_source_fields is not None:
            self.data_source_fields = data_source_fields
        if verification_state is not None:
            self.verification_state = verification_state
        self.handle_status = handle_status
        if phase is not None:
            self.phase = phase
        if sla is not None:
            self.sla = sla

    @property
    def version(self):
        """Gets the version of this Event.

        SA数据对象版本号，数据接入时需携带版本号。版本号由SA服务团队负责更新，数据源只可填写SA给定的版本号。目前版本为1.0.0。

        :return: The version of this Event.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Event.

        SA数据对象版本号，数据接入时需携带版本号。版本号由SA服务团队负责更新，数据源只可填写SA给定的版本号。目前版本为1.0.0。

        :param version: The version of this Event.
        :type version: str
        """
        self._version = version

    @property
    def environment(self):
        """Gets the environment of this Event.

        :return: The environment of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Environment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Event.

        :param environment: The environment of this Event.
        :type environment: :class:`huaweicloudsdksecmaster.v1.Environment`
        """
        self._environment = environment

    @property
    def data_source(self):
        """Gets the data_source of this Event.

        :return: The data_source of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DataSource`
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this Event.

        :param data_source: The data_source of this Event.
        :type data_source: :class:`huaweicloudsdksecmaster.v1.DataSource`
        """
        self._data_source = data_source

    @property
    def first_observed_time(self):
        """Gets the first_observed_time of this Event.

        首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :return: The first_observed_time of this Event.
        :rtype: datetime
        """
        return self._first_observed_time

    @first_observed_time.setter
    def first_observed_time(self, first_observed_time):
        """Sets the first_observed_time of this Event.

        首次发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :param first_observed_time: The first_observed_time of this Event.
        :type first_observed_time: datetime
        """
        self._first_observed_time = first_observed_time

    @property
    def last_observed_time(self):
        """Gets the last_observed_time of this Event.

        最新发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :return: The last_observed_time of this Event.
        :rtype: datetime
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time):
        """Sets the last_observed_time of this Event.

        最新发现时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :param last_observed_time: The last_observed_time of this Event.
        :type last_observed_time: datetime
        """
        self._last_observed_time = last_observed_time

    @property
    def create_time(self):
        """Gets the create_time of this Event.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :return: The create_time of this Event.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Event.

        记录时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :param create_time: The create_time of this Event.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def arrive_time(self):
        """Gets the arrive_time of this Event.

        数据接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。  是指事件数据被SA侧接收的时间，由SA接收时填写，产品上报数据时不用填写。

        :return: The arrive_time of this Event.
        :rtype: datetime
        """
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, arrive_time):
        """Sets the arrive_time of this Event.

        数据接收时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。  是指事件数据被SA侧接收的时间，由SA接收时填写，产品上报数据时不用填写。

        :param arrive_time: The arrive_time of this Event.
        :type arrive_time: datetime
        """
        self._arrive_time = arrive_time

    @property
    def event_id(self):
        """Gets the event_id of this Event.

        事件唯一标识，UUID格式。

        :return: The event_id of this Event.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event.

        事件唯一标识，UUID格式。

        :param event_id: The event_id of this Event.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def title(self):
        """Gets the title of this Event.

        事件标题，最大255字符。

        :return: The title of this Event.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Event.

        事件标题，最大255字符。

        :param title: The title of this Event.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this Event.

        事件描述信息，最大1024个字符

        :return: The description of this Event.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Event.

        事件描述信息，最大1024个字符

        :param description: The description of this Event.
        :type description: str
        """
        self._description = description

    @property
    def source_url(self):
        """Gets the source_url of this Event.

        事件URL链接，指向数据源产品中有关当前事件说明的页面。

        :return: The source_url of this Event.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this Event.

        事件URL链接，指向数据源产品中有关当前事件说明的页面。

        :param source_url: The source_url of this Event.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def count(self):
        """Gets the count of this Event.

        事件发生次数，默认为1，必填。

        :return: The count of this Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Event.

        事件发生次数，默认为1，必填。

        :param count: The count of this Event.
        :type count: int
        """
        self._count = count

    @property
    def confidence(self):
        """Gets the confidence of this Event.

        事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%。

        :return: The confidence of this Event.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Event.

        事件的置信度。置信度的定义旨在说明识别的行为或问题的可能性。 取值范围：0-100，0表示置信度为0%，100表示置信度为100%。

        :param confidence: The confidence of this Event.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def severity(self):
        """Gets the severity of this Event.

        :return: The severity of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Severity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Event.

        :param severity: The severity of this Event.
        :type severity: :class:`huaweicloudsdksecmaster.v1.Severity`
        """
        self._severity = severity

    @property
    def criticality(self):
        """Gets the criticality of this Event.

        关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源。

        :return: The criticality of this Event.
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this Event.

        关键性，是指事件涉及的资源的重要性级别。 取值范围：0-100，0表示资源不关键，100表示最关键资源。

        :param criticality: The criticality of this Event.
        :type criticality: int
        """
        self._criticality = criticality

    @property
    def type(self):
        """Gets the type of this Event.

        :return: The type of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Type`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Event.

        :param type: The type of this Event.
        :type type: :class:`huaweicloudsdksecmaster.v1.Type`
        """
        self._type = type

    @property
    def compliance(self):
        """Gets the compliance of this Event.

        :return: The compliance of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Compliance`
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this Event.

        :param compliance: The compliance of this Event.
        :type compliance: :class:`huaweicloudsdksecmaster.v1.Compliance`
        """
        self._compliance = compliance

    @property
    def network(self):
        """Gets the network of this Event.

        :return: The network of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Network`
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Event.

        :param network: The network of this Event.
        :type network: :class:`huaweicloudsdksecmaster.v1.Network`
        """
        self._network = network

    @property
    def vulnerability_patch(self):
        """Gets the vulnerability_patch of this Event.

        :return: The vulnerability_patch of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.VulnerabilityPatch`
        """
        return self._vulnerability_patch

    @vulnerability_patch.setter
    def vulnerability_patch(self, vulnerability_patch):
        """Sets the vulnerability_patch of this Event.

        :param vulnerability_patch: The vulnerability_patch of this Event.
        :type vulnerability_patch: :class:`huaweicloudsdksecmaster.v1.VulnerabilityPatch`
        """
        self._vulnerability_patch = vulnerability_patch

    @property
    def malware(self):
        """Gets the malware of this Event.

        :return: The malware of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Malware`
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        """Sets the malware of this Event.

        :param malware: The malware of this Event.
        :type malware: :class:`huaweicloudsdksecmaster.v1.Malware`
        """
        self._malware = malware

    @property
    def threat_intel(self):
        """Gets the threat_intel of this Event.

        :return: The threat_intel of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ThreatIntel`
        """
        return self._threat_intel

    @threat_intel.setter
    def threat_intel(self, threat_intel):
        """Sets the threat_intel of this Event.

        :param threat_intel: The threat_intel of this Event.
        :type threat_intel: :class:`huaweicloudsdksecmaster.v1.ThreatIntel`
        """
        self._threat_intel = threat_intel

    @property
    def resource(self):
        """Gets the resource of this Event.

        :return: The resource of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Resource`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Event.

        :param resource: The resource of this Event.
        :type resource: :class:`huaweicloudsdksecmaster.v1.Resource`
        """
        self._resource = resource

    @property
    def remediation(self):
        """Gets the remediation of this Event.

        :return: The remediation of this Event.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Remediation`
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this Event.

        :param remediation: The remediation of this Event.
        :type remediation: :class:`huaweicloudsdksecmaster.v1.Remediation`
        """
        self._remediation = remediation

    @property
    def data_source_fields(self):
        """Gets the data_source_fields of this Event.

        数据源自定义信息，最多支持50个key/value对，约束条件： 1、该对象不能包含冗余数据，并且不能与已定义的SSA事件格式字段冲突。 2、字段名称可以包含字母数字字符、空格和以下符号：_ . / = + \\ - @。 示例： \"data_source_fields\": {     \"key1\": \"value1\",     \"key2\", \"value2\",   }

        :return: The data_source_fields of this Event.
        :rtype: object
        """
        return self._data_source_fields

    @data_source_fields.setter
    def data_source_fields(self, data_source_fields):
        """Sets the data_source_fields of this Event.

        数据源自定义信息，最多支持50个key/value对，约束条件： 1、该对象不能包含冗余数据，并且不能与已定义的SSA事件格式字段冲突。 2、字段名称可以包含字母数字字符、空格和以下符号：_ . / = + \\ - @。 示例： \"data_source_fields\": {     \"key1\": \"value1\",     \"key2\", \"value2\",   }

        :param data_source_fields: The data_source_fields of this Event.
        :type data_source_fields: object
        """
        self._data_source_fields = data_source_fields

    @property
    def verification_state(self):
        """Gets the verification_state of this Event.

        事件验证状态，标识事件的准确性。 Unknown – 未知，默认 True_positive – 确认 False_positive – 误报。

        :return: The verification_state of this Event.
        :rtype: str
        """
        return self._verification_state

    @verification_state.setter
    def verification_state(self, verification_state):
        """Sets the verification_state of this Event.

        事件验证状态，标识事件的准确性。 Unknown – 未知，默认 True_positive – 确认 False_positive – 误报。

        :param verification_state: The verification_state of this Event.
        :type verification_state: str
        """
        self._verification_state = verification_state

    @property
    def handle_status(self):
        """Gets the handle_status of this Event.

        事件处理状态，New/Ignored/Resolved；默认New。

        :return: The handle_status of this Event.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this Event.

        事件处理状态，New/Ignored/Resolved；默认New。

        :param handle_status: The handle_status of this Event.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def phase(self):
        """Gets the phase of this Event.

        阶段：Prepartion|Detection and Analysis|Containm，Eradication& Recovery| Post-Incident-Activity。

        :return: The phase of this Event.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this Event.

        阶段：Prepartion|Detection and Analysis|Containm，Eradication& Recovery| Post-Incident-Activity。

        :param phase: The phase of this Event.
        :type phase: str
        """
        self._phase = phase

    @property
    def sla(self):
        """Gets the sla of this Event.

        约束闭环时间：单位：天。

        :return: The sla of this Event.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this Event.

        约束闭环时间：单位：天。

        :param sla: The sla of this Event.
        :type sla: int
        """
        self._sla = sla

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
