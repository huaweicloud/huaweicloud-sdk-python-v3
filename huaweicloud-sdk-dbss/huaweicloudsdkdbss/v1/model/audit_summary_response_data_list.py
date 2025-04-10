# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditSummaryResponseDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'str',
        'project_id': 'str',
        'instance_id': 'int',
        'instance_name': 'str',
        'audit_duration': 'int',
        'total_sql': 'int',
        'total_risk': 'int',
        'today_sql': 'int',
        'today_risk': 'int',
        'today_session': 'int',
        'update_time': 'int',
        'reserve1': 'str',
        'reserve2': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'audit_duration': 'audit_duration',
        'total_sql': 'total_sql',
        'total_risk': 'total_risk',
        'today_sql': 'today_sql',
        'today_risk': 'today_risk',
        'today_session': 'today_session',
        'update_time': 'update_time',
        'reserve1': 'reserve1',
        'reserve2': 'reserve2'
    }

    def __init__(self, id=None, status=None, project_id=None, instance_id=None, instance_name=None, audit_duration=None, total_sql=None, total_risk=None, today_sql=None, today_risk=None, today_session=None, update_time=None, reserve1=None, reserve2=None):
        r"""AuditSummaryResponseDataList

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: int
        :param status: 状态 - 1: success - 2: failure
        :type status: str
        :param project_id: 项目ID
        :type project_id: str
        :param instance_id: 实例ID
        :type instance_id: int
        :param instance_name: 实例名称
        :type instance_name: str
        :param audit_duration: 审计时长
        :type audit_duration: int
        :param total_sql: 语句总量
        :type total_sql: int
        :param total_risk: 风险总量
        :type total_risk: int
        :param today_sql: 今日语句
        :type today_sql: int
        :param today_risk: 今日风险
        :type today_risk: int
        :param today_session: 今日会话
        :type today_session: int
        :param update_time: 更新时间
        :type update_time: int
        :param reserve1: 保留字1
        :type reserve1: str
        :param reserve2: 保留字2
        :type reserve2: str
        """
        
        

        self._id = None
        self._status = None
        self._project_id = None
        self._instance_id = None
        self._instance_name = None
        self._audit_duration = None
        self._total_sql = None
        self._total_risk = None
        self._today_sql = None
        self._today_risk = None
        self._today_session = None
        self._update_time = None
        self._reserve1 = None
        self._reserve2 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if audit_duration is not None:
            self.audit_duration = audit_duration
        if total_sql is not None:
            self.total_sql = total_sql
        if total_risk is not None:
            self.total_risk = total_risk
        if today_sql is not None:
            self.today_sql = today_sql
        if today_risk is not None:
            self.today_risk = today_risk
        if today_session is not None:
            self.today_session = today_session
        if update_time is not None:
            self.update_time = update_time
        if reserve1 is not None:
            self.reserve1 = reserve1
        if reserve2 is not None:
            self.reserve2 = reserve2

    @property
    def id(self):
        r"""Gets the id of this AuditSummaryResponseDataList.

        ID

        :return: The id of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuditSummaryResponseDataList.

        ID

        :param id: The id of this AuditSummaryResponseDataList.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this AuditSummaryResponseDataList.

        状态 - 1: success - 2: failure

        :return: The status of this AuditSummaryResponseDataList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuditSummaryResponseDataList.

        状态 - 1: success - 2: failure

        :param status: The status of this AuditSummaryResponseDataList.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this AuditSummaryResponseDataList.

        项目ID

        :return: The project_id of this AuditSummaryResponseDataList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AuditSummaryResponseDataList.

        项目ID

        :param project_id: The project_id of this AuditSummaryResponseDataList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuditSummaryResponseDataList.

        实例ID

        :return: The instance_id of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuditSummaryResponseDataList.

        实例ID

        :param instance_id: The instance_id of this AuditSummaryResponseDataList.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this AuditSummaryResponseDataList.

        实例名称

        :return: The instance_name of this AuditSummaryResponseDataList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this AuditSummaryResponseDataList.

        实例名称

        :param instance_name: The instance_name of this AuditSummaryResponseDataList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def audit_duration(self):
        r"""Gets the audit_duration of this AuditSummaryResponseDataList.

        审计时长

        :return: The audit_duration of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._audit_duration

    @audit_duration.setter
    def audit_duration(self, audit_duration):
        r"""Sets the audit_duration of this AuditSummaryResponseDataList.

        审计时长

        :param audit_duration: The audit_duration of this AuditSummaryResponseDataList.
        :type audit_duration: int
        """
        self._audit_duration = audit_duration

    @property
    def total_sql(self):
        r"""Gets the total_sql of this AuditSummaryResponseDataList.

        语句总量

        :return: The total_sql of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._total_sql

    @total_sql.setter
    def total_sql(self, total_sql):
        r"""Sets the total_sql of this AuditSummaryResponseDataList.

        语句总量

        :param total_sql: The total_sql of this AuditSummaryResponseDataList.
        :type total_sql: int
        """
        self._total_sql = total_sql

    @property
    def total_risk(self):
        r"""Gets the total_risk of this AuditSummaryResponseDataList.

        风险总量

        :return: The total_risk of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._total_risk

    @total_risk.setter
    def total_risk(self, total_risk):
        r"""Sets the total_risk of this AuditSummaryResponseDataList.

        风险总量

        :param total_risk: The total_risk of this AuditSummaryResponseDataList.
        :type total_risk: int
        """
        self._total_risk = total_risk

    @property
    def today_sql(self):
        r"""Gets the today_sql of this AuditSummaryResponseDataList.

        今日语句

        :return: The today_sql of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._today_sql

    @today_sql.setter
    def today_sql(self, today_sql):
        r"""Sets the today_sql of this AuditSummaryResponseDataList.

        今日语句

        :param today_sql: The today_sql of this AuditSummaryResponseDataList.
        :type today_sql: int
        """
        self._today_sql = today_sql

    @property
    def today_risk(self):
        r"""Gets the today_risk of this AuditSummaryResponseDataList.

        今日风险

        :return: The today_risk of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._today_risk

    @today_risk.setter
    def today_risk(self, today_risk):
        r"""Sets the today_risk of this AuditSummaryResponseDataList.

        今日风险

        :param today_risk: The today_risk of this AuditSummaryResponseDataList.
        :type today_risk: int
        """
        self._today_risk = today_risk

    @property
    def today_session(self):
        r"""Gets the today_session of this AuditSummaryResponseDataList.

        今日会话

        :return: The today_session of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._today_session

    @today_session.setter
    def today_session(self, today_session):
        r"""Sets the today_session of this AuditSummaryResponseDataList.

        今日会话

        :param today_session: The today_session of this AuditSummaryResponseDataList.
        :type today_session: int
        """
        self._today_session = today_session

    @property
    def update_time(self):
        r"""Gets the update_time of this AuditSummaryResponseDataList.

        更新时间

        :return: The update_time of this AuditSummaryResponseDataList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AuditSummaryResponseDataList.

        更新时间

        :param update_time: The update_time of this AuditSummaryResponseDataList.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def reserve1(self):
        r"""Gets the reserve1 of this AuditSummaryResponseDataList.

        保留字1

        :return: The reserve1 of this AuditSummaryResponseDataList.
        :rtype: str
        """
        return self._reserve1

    @reserve1.setter
    def reserve1(self, reserve1):
        r"""Sets the reserve1 of this AuditSummaryResponseDataList.

        保留字1

        :param reserve1: The reserve1 of this AuditSummaryResponseDataList.
        :type reserve1: str
        """
        self._reserve1 = reserve1

    @property
    def reserve2(self):
        r"""Gets the reserve2 of this AuditSummaryResponseDataList.

        保留字2

        :return: The reserve2 of this AuditSummaryResponseDataList.
        :rtype: str
        """
        return self._reserve2

    @reserve2.setter
    def reserve2(self, reserve2):
        r"""Sets the reserve2 of this AuditSummaryResponseDataList.

        保留字2

        :param reserve2: The reserve2 of this AuditSummaryResponseDataList.
        :type reserve2: str
        """
        self._reserve2 = reserve2

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
        if not isinstance(other, AuditSummaryResponseDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
