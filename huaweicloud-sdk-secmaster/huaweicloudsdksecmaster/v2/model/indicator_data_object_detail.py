# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorDataObjectDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indicator_type': 'IndicatorDataObjectDetailIndicatorType',
        'value': 'str',
        'update_time': 'str',
        'create_time': 'str',
        'environment': 'IndicatorDataObjectDetailEnvironment',
        'data_source': 'IndicatorDataObjectDetailDataSource',
        'first_report_time': 'str',
        'is_deleted': 'bool',
        'last_report_time': 'str',
        'granular_marking': 'int',
        'name': 'str',
        'id': 'str',
        'project_id': 'str',
        'revoked': 'bool',
        'status': 'str',
        'verdict': 'str',
        'workspace_id': 'str',
        'confidence': 'int'
    }

    attribute_map = {
        'indicator_type': 'indicator_type',
        'value': 'value',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'environment': 'environment',
        'data_source': 'data_source',
        'first_report_time': 'first_report_time',
        'is_deleted': 'is_deleted',
        'last_report_time': 'last_report_time',
        'granular_marking': 'granular_marking',
        'name': 'name',
        'id': 'id',
        'project_id': 'project_id',
        'revoked': 'revoked',
        'status': 'status',
        'verdict': 'verdict',
        'workspace_id': 'workspace_id',
        'confidence': 'confidence'
    }

    def __init__(self, indicator_type=None, value=None, update_time=None, create_time=None, environment=None, data_source=None, first_report_time=None, is_deleted=None, last_report_time=None, granular_marking=None, name=None, id=None, project_id=None, revoked=None, status=None, verdict=None, workspace_id=None, confidence=None):
        """IndicatorDataObjectDetail

        The model defined in huaweicloud sdk

        :param indicator_type: 
        :type indicator_type: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailIndicatorType`
        :param value: 值，如：ip url domain等
        :type value: str
        :param update_time: 更新时间
        :type update_time: str
        :param create_time: 创建时间
        :type create_time: str
        :param environment: 
        :type environment: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailEnvironment`
        :param data_source: 
        :type data_source: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailDataSource`
        :param first_report_time: 首次发生时间
        :type first_report_time: str
        :param is_deleted: 是否删除
        :type is_deleted: bool
        :param last_report_time: 最近发生时间
        :type last_report_time: str
        :param granular_marking: 粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）
        :type granular_marking: int
        :param name: 名称
        :type name: str
        :param id: 情报ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param revoked: 是否作废
        :type revoked: bool
        :param status: 状态， Open--打开，Closed--关闭, Revoked--作废
        :type status: str
        :param verdict: 威胁度， Black--黑,White--白，Gray--灰
        :type verdict: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param confidence: 置信度，取值范围是80-100
        :type confidence: int
        """
        
        

        self._indicator_type = None
        self._value = None
        self._update_time = None
        self._create_time = None
        self._environment = None
        self._data_source = None
        self._first_report_time = None
        self._is_deleted = None
        self._last_report_time = None
        self._granular_marking = None
        self._name = None
        self._id = None
        self._project_id = None
        self._revoked = None
        self._status = None
        self._verdict = None
        self._workspace_id = None
        self._confidence = None
        self.discriminator = None

        if indicator_type is not None:
            self.indicator_type = indicator_type
        if value is not None:
            self.value = value
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if environment is not None:
            self.environment = environment
        if data_source is not None:
            self.data_source = data_source
        if first_report_time is not None:
            self.first_report_time = first_report_time
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if last_report_time is not None:
            self.last_report_time = last_report_time
        if granular_marking is not None:
            self.granular_marking = granular_marking
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if revoked is not None:
            self.revoked = revoked
        if status is not None:
            self.status = status
        if verdict is not None:
            self.verdict = verdict
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if confidence is not None:
            self.confidence = confidence

    @property
    def indicator_type(self):
        """Gets the indicator_type of this IndicatorDataObjectDetail.

        :return: The indicator_type of this IndicatorDataObjectDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailIndicatorType`
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this IndicatorDataObjectDetail.

        :param indicator_type: The indicator_type of this IndicatorDataObjectDetail.
        :type indicator_type: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailIndicatorType`
        """
        self._indicator_type = indicator_type

    @property
    def value(self):
        """Gets the value of this IndicatorDataObjectDetail.

        值，如：ip url domain等

        :return: The value of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IndicatorDataObjectDetail.

        值，如：ip url domain等

        :param value: The value of this IndicatorDataObjectDetail.
        :type value: str
        """
        self._value = value

    @property
    def update_time(self):
        """Gets the update_time of this IndicatorDataObjectDetail.

        更新时间

        :return: The update_time of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this IndicatorDataObjectDetail.

        更新时间

        :param update_time: The update_time of this IndicatorDataObjectDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this IndicatorDataObjectDetail.

        创建时间

        :return: The create_time of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IndicatorDataObjectDetail.

        创建时间

        :param create_time: The create_time of this IndicatorDataObjectDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def environment(self):
        """Gets the environment of this IndicatorDataObjectDetail.

        :return: The environment of this IndicatorDataObjectDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailEnvironment`
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this IndicatorDataObjectDetail.

        :param environment: The environment of this IndicatorDataObjectDetail.
        :type environment: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailEnvironment`
        """
        self._environment = environment

    @property
    def data_source(self):
        """Gets the data_source of this IndicatorDataObjectDetail.

        :return: The data_source of this IndicatorDataObjectDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailDataSource`
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this IndicatorDataObjectDetail.

        :param data_source: The data_source of this IndicatorDataObjectDetail.
        :type data_source: :class:`huaweicloudsdksecmaster.v2.IndicatorDataObjectDetailDataSource`
        """
        self._data_source = data_source

    @property
    def first_report_time(self):
        """Gets the first_report_time of this IndicatorDataObjectDetail.

        首次发生时间

        :return: The first_report_time of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._first_report_time

    @first_report_time.setter
    def first_report_time(self, first_report_time):
        """Sets the first_report_time of this IndicatorDataObjectDetail.

        首次发生时间

        :param first_report_time: The first_report_time of this IndicatorDataObjectDetail.
        :type first_report_time: str
        """
        self._first_report_time = first_report_time

    @property
    def is_deleted(self):
        """Gets the is_deleted of this IndicatorDataObjectDetail.

        是否删除

        :return: The is_deleted of this IndicatorDataObjectDetail.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this IndicatorDataObjectDetail.

        是否删除

        :param is_deleted: The is_deleted of this IndicatorDataObjectDetail.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def last_report_time(self):
        """Gets the last_report_time of this IndicatorDataObjectDetail.

        最近发生时间

        :return: The last_report_time of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._last_report_time

    @last_report_time.setter
    def last_report_time(self, last_report_time):
        """Sets the last_report_time of this IndicatorDataObjectDetail.

        最近发生时间

        :param last_report_time: The last_report_time of this IndicatorDataObjectDetail.
        :type last_report_time: str
        """
        self._last_report_time = last_report_time

    @property
    def granular_marking(self):
        """Gets the granular_marking of this IndicatorDataObjectDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :return: The granular_marking of this IndicatorDataObjectDetail.
        :rtype: int
        """
        return self._granular_marking

    @granular_marking.setter
    def granular_marking(self, granular_marking):
        """Sets the granular_marking of this IndicatorDataObjectDetail.

        粒度（保密等级），由高到低：1（首次发现）、2（自产数据）、3（需购买）、4（外网直接查询）

        :param granular_marking: The granular_marking of this IndicatorDataObjectDetail.
        :type granular_marking: int
        """
        self._granular_marking = granular_marking

    @property
    def name(self):
        """Gets the name of this IndicatorDataObjectDetail.

        名称

        :return: The name of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndicatorDataObjectDetail.

        名称

        :param name: The name of this IndicatorDataObjectDetail.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this IndicatorDataObjectDetail.

        情报ID

        :return: The id of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndicatorDataObjectDetail.

        情报ID

        :param id: The id of this IndicatorDataObjectDetail.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this IndicatorDataObjectDetail.

        项目ID

        :return: The project_id of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IndicatorDataObjectDetail.

        项目ID

        :param project_id: The project_id of this IndicatorDataObjectDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def revoked(self):
        """Gets the revoked of this IndicatorDataObjectDetail.

        是否作废

        :return: The revoked of this IndicatorDataObjectDetail.
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this IndicatorDataObjectDetail.

        是否作废

        :param revoked: The revoked of this IndicatorDataObjectDetail.
        :type revoked: bool
        """
        self._revoked = revoked

    @property
    def status(self):
        """Gets the status of this IndicatorDataObjectDetail.

        状态， Open--打开，Closed--关闭, Revoked--作废

        :return: The status of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IndicatorDataObjectDetail.

        状态， Open--打开，Closed--关闭, Revoked--作废

        :param status: The status of this IndicatorDataObjectDetail.
        :type status: str
        """
        self._status = status

    @property
    def verdict(self):
        """Gets the verdict of this IndicatorDataObjectDetail.

        威胁度， Black--黑,White--白，Gray--灰

        :return: The verdict of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        """Sets the verdict of this IndicatorDataObjectDetail.

        威胁度， Black--黑,White--白，Gray--灰

        :param verdict: The verdict of this IndicatorDataObjectDetail.
        :type verdict: str
        """
        self._verdict = verdict

    @property
    def workspace_id(self):
        """Gets the workspace_id of this IndicatorDataObjectDetail.

        工作空间ID

        :return: The workspace_id of this IndicatorDataObjectDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this IndicatorDataObjectDetail.

        工作空间ID

        :param workspace_id: The workspace_id of this IndicatorDataObjectDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def confidence(self):
        """Gets the confidence of this IndicatorDataObjectDetail.

        置信度，取值范围是80-100

        :return: The confidence of this IndicatorDataObjectDetail.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this IndicatorDataObjectDetail.

        置信度，取值范围是80-100

        :param confidence: The confidence of this IndicatorDataObjectDetail.
        :type confidence: int
        """
        self._confidence = confidence

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
        if not isinstance(other, IndicatorDataObjectDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
