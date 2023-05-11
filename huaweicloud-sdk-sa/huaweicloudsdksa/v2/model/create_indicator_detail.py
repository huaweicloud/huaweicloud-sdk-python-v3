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
        'data_source': 'CreateAlertDataSource',
        'verdict': 'str',
        'confidence': 'int',
        'status': 'str',
        'labels': 'str',
        'value': 'str',
        'granular_marking': 'str',
        'environment': 'ShowAlertRspEnvironment',
        'defanged': 'bool',
        'first_report_time': 'str',
        'last_report_time': 'str',
        'id': 'str',
        'indicator_type': 'CreateIndicatorDetailIndicatorType',
        'name': 'str',
        'dataclass_id': 'str',
        'type': 'str',
        'data_object': 'IndicatorDataObjectDetail',
        'workspace_id': 'str',
        'project_id': 'str',
        'layout_id': 'str',
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
        'type': 'type',
        'data_object': 'data_object',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'layout_id': 'layout_id',
        'dataclass': 'dataclass',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, data_source=None, verdict=None, confidence=None, status=None, labels=None, value=None, granular_marking=None, environment=None, defanged=None, first_report_time=None, last_report_time=None, id=None, indicator_type=None, name=None, dataclass_id=None, type=None, data_object=None, workspace_id=None, project_id=None, layout_id=None, dataclass=None, create_time=None, update_time=None):
        """CreateIndicatorDetail

        The model defined in huaweicloud sdk

        :param data_source: 
        :type data_source: :class:`huaweicloudsdksa.v2.CreateAlertDataSource`
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
        :type environment: :class:`huaweicloudsdksa.v2.ShowAlertRspEnvironment`
        :param defanged: 是否失效
        :type defanged: bool
        :param first_report_time: Create time
        :type first_report_time: str
        :param last_report_time: Update time
        :type last_report_time: str
        :param id: 指标ID
        :type id: str
        :param indicator_type: 
        :type indicator_type: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        :param name: 指标名称
        :type name: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param type: 类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）
        :type type: str
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        :param workspace_id: workspace id
        :type workspace_id: str
        :param project_id: Project id value
        :type project_id: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksa.v2.DataClassRefPojo`
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
        self._type = None
        self._data_object = None
        self._workspace_id = None
        self._project_id = None
        self._layout_id = None
        self._dataclass = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if data_source is not None:
            self.data_source = data_source
        if verdict is not None:
            self.verdict = verdict
        if confidence is not None:
            self.confidence = confidence
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        if value is not None:
            self.value = value
        if granular_marking is not None:
            self.granular_marking = granular_marking
        if environment is not None:
            self.environment = environment
        if defanged is not None:
            self.defanged = defanged
        if first_report_time is not None:
            self.first_report_time = first_report_time
        if last_report_time is not None:
            self.last_report_time = last_report_time
        if id is not None:
            self.id = id
        if indicator_type is not None:
            self.indicator_type = indicator_type
        self.name = name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if type is not None:
            self.type = type
        if data_object is not None:
            self.data_object = data_object
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if layout_id is not None:
            self.layout_id = layout_id
        if dataclass is not None:
            self.dataclass = dataclass
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def data_source(self):
        """Gets the data_source of this CreateIndicatorDetail.

        :return: The data_source of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertDataSource`
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this CreateIndicatorDetail.

        :param data_source: The data_source of this CreateIndicatorDetail.
        :type data_source: :class:`huaweicloudsdksa.v2.CreateAlertDataSource`
        """
        self._data_source = data_source

    @property
    def verdict(self):
        """Gets the verdict of this CreateIndicatorDetail.

        威胁度

        :return: The verdict of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        """Sets the verdict of this CreateIndicatorDetail.

        威胁度

        :param verdict: The verdict of this CreateIndicatorDetail.
        :type verdict: str
        """
        self._verdict = verdict

    @property
    def confidence(self):
        """Gets the confidence of this CreateIndicatorDetail.

        置信度

        :return: The confidence of this CreateIndicatorDetail.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this CreateIndicatorDetail.

        置信度

        :param confidence: The confidence of this CreateIndicatorDetail.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def status(self):
        """Gets the status of this CreateIndicatorDetail.

        状态

        :return: The status of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateIndicatorDetail.

        状态

        :param status: The status of this CreateIndicatorDetail.
        :type status: str
        """
        self._status = status

    @property
    def labels(self):
        """Gets the labels of this CreateIndicatorDetail.

        标签

        :return: The labels of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateIndicatorDetail.

        标签

        :param labels: The labels of this CreateIndicatorDetail.
        :type labels: str
        """
        self._labels = labels

    @property
    def value(self):
        """Gets the value of this CreateIndicatorDetail.

        值

        :return: The value of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateIndicatorDetail.

        值

        :param value: The value of this CreateIndicatorDetail.
        :type value: str
        """
        self._value = value

    @property
    def granular_marking(self):
        """Gets the granular_marking of this CreateIndicatorDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :return: The granular_marking of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._granular_marking

    @granular_marking.setter
    def granular_marking(self, granular_marking):
        """Sets the granular_marking of this CreateIndicatorDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :param granular_marking: The granular_marking of this CreateIndicatorDetail.
        :type granular_marking: str
        """
        self._granular_marking = granular_marking

    @property
    def environment(self):
        """Gets the environment of this CreateIndicatorDetail.

        :return: The environment of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertRspEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this CreateIndicatorDetail.

        :param environment: The environment of this CreateIndicatorDetail.
        :type environment: :class:`huaweicloudsdksa.v2.ShowAlertRspEnvironment`
        """
        self._environment = environment

    @property
    def defanged(self):
        """Gets the defanged of this CreateIndicatorDetail.

        是否失效

        :return: The defanged of this CreateIndicatorDetail.
        :rtype: bool
        """
        return self._defanged

    @defanged.setter
    def defanged(self, defanged):
        """Sets the defanged of this CreateIndicatorDetail.

        是否失效

        :param defanged: The defanged of this CreateIndicatorDetail.
        :type defanged: bool
        """
        self._defanged = defanged

    @property
    def first_report_time(self):
        """Gets the first_report_time of this CreateIndicatorDetail.

        Create time

        :return: The first_report_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._first_report_time

    @first_report_time.setter
    def first_report_time(self, first_report_time):
        """Sets the first_report_time of this CreateIndicatorDetail.

        Create time

        :param first_report_time: The first_report_time of this CreateIndicatorDetail.
        :type first_report_time: str
        """
        self._first_report_time = first_report_time

    @property
    def last_report_time(self):
        """Gets the last_report_time of this CreateIndicatorDetail.

        Update time

        :return: The last_report_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._last_report_time

    @last_report_time.setter
    def last_report_time(self, last_report_time):
        """Sets the last_report_time of this CreateIndicatorDetail.

        Update time

        :param last_report_time: The last_report_time of this CreateIndicatorDetail.
        :type last_report_time: str
        """
        self._last_report_time = last_report_time

    @property
    def id(self):
        """Gets the id of this CreateIndicatorDetail.

        指标ID

        :return: The id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateIndicatorDetail.

        指标ID

        :param id: The id of this CreateIndicatorDetail.
        :type id: str
        """
        self._id = id

    @property
    def indicator_type(self):
        """Gets the indicator_type of this CreateIndicatorDetail.

        :return: The indicator_type of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this CreateIndicatorDetail.

        :param indicator_type: The indicator_type of this CreateIndicatorDetail.
        :type indicator_type: :class:`huaweicloudsdksa.v2.CreateIndicatorDetailIndicatorType`
        """
        self._indicator_type = indicator_type

    @property
    def name(self):
        """Gets the name of this CreateIndicatorDetail.

        指标名称

        :return: The name of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIndicatorDetail.

        指标名称

        :param name: The name of this CreateIndicatorDetail.
        :type name: str
        """
        self._name = name

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this CreateIndicatorDetail.

        数据类ID

        :return: The dataclass_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this CreateIndicatorDetail.

        数据类ID

        :param dataclass_id: The dataclass_id of this CreateIndicatorDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def type(self):
        """Gets the type of this CreateIndicatorDetail.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :return: The type of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateIndicatorDetail.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :param type: The type of this CreateIndicatorDetail.
        :type type: str
        """
        self._type = type

    @property
    def data_object(self):
        """Gets the data_object of this CreateIndicatorDetail.

        :return: The data_object of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this CreateIndicatorDetail.

        :param data_object: The data_object of this CreateIndicatorDetail.
        :type data_object: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        """
        self._data_object = data_object

    @property
    def workspace_id(self):
        """Gets the workspace_id of this CreateIndicatorDetail.

        workspace id

        :return: The workspace_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this CreateIndicatorDetail.

        workspace id

        :param workspace_id: The workspace_id of this CreateIndicatorDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateIndicatorDetail.

        Project id value

        :return: The project_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateIndicatorDetail.

        Project id value

        :param project_id: The project_id of this CreateIndicatorDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def layout_id(self):
        """Gets the layout_id of this CreateIndicatorDetail.

        布局ID

        :return: The layout_id of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this CreateIndicatorDetail.

        布局ID

        :param layout_id: The layout_id of this CreateIndicatorDetail.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def dataclass(self):
        """Gets the dataclass of this CreateIndicatorDetail.

        :return: The dataclass of this CreateIndicatorDetail.
        :rtype: :class:`huaweicloudsdksa.v2.DataClassRefPojo`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        """Sets the dataclass of this CreateIndicatorDetail.

        :param dataclass: The dataclass of this CreateIndicatorDetail.
        :type dataclass: :class:`huaweicloudsdksa.v2.DataClassRefPojo`
        """
        self._dataclass = dataclass

    @property
    def create_time(self):
        """Gets the create_time of this CreateIndicatorDetail.

        Create time

        :return: The create_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateIndicatorDetail.

        Create time

        :param create_time: The create_time of this CreateIndicatorDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateIndicatorDetail.

        Update time

        :return: The update_time of this CreateIndicatorDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateIndicatorDetail.

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
