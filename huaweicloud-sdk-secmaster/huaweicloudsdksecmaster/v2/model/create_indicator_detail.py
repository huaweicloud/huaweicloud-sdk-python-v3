# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIndicatorDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_source': 'CreateIndicatorDetailDataSource',
        'verdict': 'str',
        'confidence': 'int',
        'status': 'str',
        'labels': 'str',
        'value': 'str',
        'granular_marking': 'str',
        'environment': 'CreateIndicatorDetailEnvironment',
        'defanged': 'bool',
        'first_report_time': 'str',
        'last_report_time': 'str',
        'id': 'str',
        'indicator_type': 'CreateIndicatorDetailIndicatorType',
        'name': 'str',
        'dataclass_id': 'str',
        'workspace_id': 'str',
        'project_id': 'str',
        'dataclass': 'DataClassRefPojo',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'data_source': 'data_source',
        'verdict': 'verdict',
        'confidence': 'confidence',
        'status': 'status',
        'labels': 'labels',
        'value': 'value',
        'granular_marking': 'granular_marking',
        'environment': 'environment',
        'defanged': 'defanged',
        'first_report_time': 'first_report_time',
        'last_report_time': 'last_report_time',
        'id': 'id',
        'indicator_type': 'indicator_type',
        'name': 'name',
        'dataclass_id': 'dataclass_id',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'dataclass': 'dataclass',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, data_source=None, verdict=None, confidence=None, status=None, labels=None, value=None, granular_marking=None, environment=None, defanged=None, first_report_time=None, last_report_time=None, id=None, indicator_type=None, name=None, dataclass_id=None, workspace_id=None, project_id=None, dataclass=None, create_time=None, update_time=None):
        r"""CreateIndicatorDetail

        The model defined in huaweicloud sdk

        :param data_source: 
        :type data_source: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailDataSource`
        :param verdict: 威胁度
        :type verdict: str
        :param confidence: 置信度
        :type confidence: int
        :param status: 状态
        :type status: str
        :param labels: 标签
        :type labels: str
        :param value: 值
        :type value: str
        :param granular_marking: 粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）
        :type granular_marking: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailEnvironment`
        :param defanged: 是否失效
        :type defanged: bool
        :param first_report_time: 首次发生时间
        :type first_report_time: str
        :param last_report_time: 最近发生时间
        :type last_report_time: str
        :param id: 威胁情报ID
        :type id: str
        :param indicator_type: 
        :type indicator_type: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailIndicatorType`
        :param name: 威胁情报名称
        :type name: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param workspace_id: workspace id
        :type workspace_id: str
        :param project_id: Project id value
        :type project_id: str
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        :param create_time: Create time
        :type create_time: str
        :param update_time: Update time
        :type update_time: str
        """
        
        

        self._data_source = None
        self._verdict = None
        self._confidence = None
        self._status = None
        self._labels = None
        self._value = None
        self._granular_marking = None
        self._environment = None
        self._defanged = None
        self._first_report_time = None
        self._last_report_time = None
        self._id = None
        self._indicator_type = None
        self._name = None
        self._dataclass_id = None
        self._workspace_id = None
        self._project_id = None
        self._dataclass = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.data_source = data_source
        self.verdict = verdict
        if confidence is not None:
            self.confidence = confidence
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        self.value = value
        self.granular_marking = granular_marking
        self.environment = environment
        self.defanged = defanged
        self.first_report_time = first_report_time
        if last_report_time is not None:
            self.last_report_time = last_report_time
        if id is not None:
            self.id = id
        self.indicator_type = indicator_type
        self.name = name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if dataclass is not None:
            self.dataclass = dataclass
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def data_source(self):
        r"""Gets the data_source of this CreateIndicatorDetail.

        :return: The data_source of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailDataSource`
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this CreateIndicatorDetail.

        :param data_source: The data_source of this CreateIndicatorDetail.
        :type data_source: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailDataSource`
        """
        self._data_source = data_source

    @property
    def verdict(self):
        r"""Gets the verdict of this CreateIndicatorDetail.

        威胁度

        :return: The verdict of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        r"""Sets the verdict of this CreateIndicatorDetail.

        威胁度

        :param verdict: The verdict of this CreateIndicatorDetail.
        :type verdict: str
        """
        self._verdict = verdict

    @property
    def confidence(self):
        r"""Gets the confidence of this CreateIndicatorDetail.

        置信度

        :return: The confidence of this CreateIndicatorDetail.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this CreateIndicatorDetail.

        置信度

        :param confidence: The confidence of this CreateIndicatorDetail.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def status(self):
        r"""Gets the status of this CreateIndicatorDetail.

        状态

        :return: The status of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateIndicatorDetail.

        状态

        :param status: The status of this CreateIndicatorDetail.
        :type status: str
        """
        self._status = status

    @property
    def labels(self):
        r"""Gets the labels of this CreateIndicatorDetail.

        标签

        :return: The labels of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateIndicatorDetail.

        标签

        :param labels: The labels of this CreateIndicatorDetail.
        :type labels: str
        """
        self._labels = labels

    @property
    def value(self):
        r"""Gets the value of this CreateIndicatorDetail.

        值

        :return: The value of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateIndicatorDetail.

        值

        :param value: The value of this CreateIndicatorDetail.
        :type value: str
        """
        self._value = value

    @property
    def granular_marking(self):
        r"""Gets the granular_marking of this CreateIndicatorDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :return: The granular_marking of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._granular_marking

    @granular_marking.setter
    def granular_marking(self, granular_marking):
        r"""Sets the granular_marking of this CreateIndicatorDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :param granular_marking: The granular_marking of this CreateIndicatorDetail.
        :type granular_marking: str
        """
        self._granular_marking = granular_marking

    @property
    def environment(self):
        r"""Gets the environment of this CreateIndicatorDetail.

        :return: The environment of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this CreateIndicatorDetail.

        :param environment: The environment of this CreateIndicatorDetail.
        :type environment: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailEnvironment`
        """
        self._environment = environment

    @property
    def defanged(self):
        r"""Gets the defanged of this CreateIndicatorDetail.

        是否失效

        :return: The defanged of this CreateIndicatorDetail.
        :rtype: bool
        """
        return self._defanged

    @defanged.setter
    def defanged(self, defanged):
        r"""Sets the defanged of this CreateIndicatorDetail.

        是否失效

        :param defanged: The defanged of this CreateIndicatorDetail.
        :type defanged: bool
        """
        self._defanged = defanged

    @property
    def first_report_time(self):
        r"""Gets the first_report_time of this CreateIndicatorDetail.

        首次发生时间

        :return: The first_report_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._first_report_time

    @first_report_time.setter
    def first_report_time(self, first_report_time):
        r"""Sets the first_report_time of this CreateIndicatorDetail.

        首次发生时间

        :param first_report_time: The first_report_time of this CreateIndicatorDetail.
        :type first_report_time: str
        """
        self._first_report_time = first_report_time

    @property
    def last_report_time(self):
        r"""Gets the last_report_time of this CreateIndicatorDetail.

        最近发生时间

        :return: The last_report_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._last_report_time

    @last_report_time.setter
    def last_report_time(self, last_report_time):
        r"""Sets the last_report_time of this CreateIndicatorDetail.

        最近发生时间

        :param last_report_time: The last_report_time of this CreateIndicatorDetail.
        :type last_report_time: str
        """
        self._last_report_time = last_report_time

    @property
    def id(self):
        r"""Gets the id of this CreateIndicatorDetail.

        威胁情报ID

        :return: The id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateIndicatorDetail.

        威胁情报ID

        :param id: The id of this CreateIndicatorDetail.
        :type id: str
        """
        self._id = id

    @property
    def indicator_type(self):
        r"""Gets the indicator_type of this CreateIndicatorDetail.

        :return: The indicator_type of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailIndicatorType`
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        r"""Sets the indicator_type of this CreateIndicatorDetail.

        :param indicator_type: The indicator_type of this CreateIndicatorDetail.
        :type indicator_type: :class:`huaweicloudsdksecmaster.v2.CreateIndicatorDetailIndicatorType`
        """
        self._indicator_type = indicator_type

    @property
    def name(self):
        r"""Gets the name of this CreateIndicatorDetail.

        威胁情报名称

        :return: The name of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIndicatorDetail.

        威胁情报名称

        :param name: The name of this CreateIndicatorDetail.
        :type name: str
        """
        self._name = name

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this CreateIndicatorDetail.

        数据类ID

        :return: The dataclass_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this CreateIndicatorDetail.

        数据类ID

        :param dataclass_id: The dataclass_id of this CreateIndicatorDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateIndicatorDetail.

        workspace id

        :return: The workspace_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateIndicatorDetail.

        workspace id

        :param workspace_id: The workspace_id of this CreateIndicatorDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateIndicatorDetail.

        Project id value

        :return: The project_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateIndicatorDetail.

        Project id value

        :param project_id: The project_id of this CreateIndicatorDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataclass(self):
        r"""Gets the dataclass of this CreateIndicatorDetail.

        :return: The dataclass of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this CreateIndicatorDetail.

        :param dataclass: The dataclass of this CreateIndicatorDetail.
        :type dataclass: :class:`huaweicloudsdksecmaster.v2.DataClassRefPojo`
        """
        self._dataclass = dataclass

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateIndicatorDetail.

        Create time

        :return: The create_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateIndicatorDetail.

        Create time

        :param create_time: The create_time of this CreateIndicatorDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateIndicatorDetail.

        Update time

        :return: The update_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateIndicatorDetail.

        Update time

        :param update_time: The update_time of this CreateIndicatorDetail.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, CreateIndicatorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
