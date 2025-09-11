# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchedulerConfigBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_ids': 'str',
        'format': 'str',
        'frequency': 'str',
        'id': 'str',
        'mode': 'str',
        'notice': 'str',
        'start_time': 'str',
        'status': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'format': 'format',
        'frequency': 'frequency',
        'id': 'id',
        'mode': 'mode',
        'notice': 'notice',
        'start_time': 'start_time',
        'status': 'status',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, db_ids=None, format=None, frequency=None, id=None, mode=None, notice=None, start_time=None, status=None, topic_urn=None):
        r"""SchedulerConfigBase

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID
        :type db_ids: str
        :param format: 文件类型
        :type format: str
        :param frequency: 周期 - AUDIT_REPORT_DAY: 天 - AUDIT_REPORT_WEEK：周 - AUDIT_REPORT_MONTH：月 - AUDIT_REPORT_YEAR：年 - AUDIT_REPORT_REAL_TIME：实时
        :type frequency: str
        :param id: 报表模板ID
        :type id: str
        :param mode: 调度方式
        :type mode: str
        :param notice: 是否通知  - OFF：不通知  - ON：通知
        :type notice: str
        :param start_time: 开始时间
        :type start_time: str
        :param status: 模板状态
        :type status: str
        :param topic_urn: 主题URN
        :type topic_urn: str
        """
        
        

        self._db_ids = None
        self._format = None
        self._frequency = None
        self._id = None
        self._mode = None
        self._notice = None
        self._start_time = None
        self._status = None
        self._topic_urn = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if format is not None:
            self.format = format
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if mode is not None:
            self.mode = mode
        if notice is not None:
            self.notice = notice
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def db_ids(self):
        r"""Gets the db_ids of this SchedulerConfigBase.

        数据库ID

        :return: The db_ids of this SchedulerConfigBase.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this SchedulerConfigBase.

        数据库ID

        :param db_ids: The db_ids of this SchedulerConfigBase.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def format(self):
        r"""Gets the format of this SchedulerConfigBase.

        文件类型

        :return: The format of this SchedulerConfigBase.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this SchedulerConfigBase.

        文件类型

        :param format: The format of this SchedulerConfigBase.
        :type format: str
        """
        self._format = format

    @property
    def frequency(self):
        r"""Gets the frequency of this SchedulerConfigBase.

        周期 - AUDIT_REPORT_DAY: 天 - AUDIT_REPORT_WEEK：周 - AUDIT_REPORT_MONTH：月 - AUDIT_REPORT_YEAR：年 - AUDIT_REPORT_REAL_TIME：实时

        :return: The frequency of this SchedulerConfigBase.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this SchedulerConfigBase.

        周期 - AUDIT_REPORT_DAY: 天 - AUDIT_REPORT_WEEK：周 - AUDIT_REPORT_MONTH：月 - AUDIT_REPORT_YEAR：年 - AUDIT_REPORT_REAL_TIME：实时

        :param frequency: The frequency of this SchedulerConfigBase.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def id(self):
        r"""Gets the id of this SchedulerConfigBase.

        报表模板ID

        :return: The id of this SchedulerConfigBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SchedulerConfigBase.

        报表模板ID

        :param id: The id of this SchedulerConfigBase.
        :type id: str
        """
        self._id = id

    @property
    def mode(self):
        r"""Gets the mode of this SchedulerConfigBase.

        调度方式

        :return: The mode of this SchedulerConfigBase.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this SchedulerConfigBase.

        调度方式

        :param mode: The mode of this SchedulerConfigBase.
        :type mode: str
        """
        self._mode = mode

    @property
    def notice(self):
        r"""Gets the notice of this SchedulerConfigBase.

        是否通知  - OFF：不通知  - ON：通知

        :return: The notice of this SchedulerConfigBase.
        :rtype: str
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        r"""Sets the notice of this SchedulerConfigBase.

        是否通知  - OFF：不通知  - ON：通知

        :param notice: The notice of this SchedulerConfigBase.
        :type notice: str
        """
        self._notice = notice

    @property
    def start_time(self):
        r"""Gets the start_time of this SchedulerConfigBase.

        开始时间

        :return: The start_time of this SchedulerConfigBase.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SchedulerConfigBase.

        开始时间

        :param start_time: The start_time of this SchedulerConfigBase.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this SchedulerConfigBase.

        模板状态

        :return: The status of this SchedulerConfigBase.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SchedulerConfigBase.

        模板状态

        :param status: The status of this SchedulerConfigBase.
        :type status: str
        """
        self._status = status

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SchedulerConfigBase.

        主题URN

        :return: The topic_urn of this SchedulerConfigBase.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SchedulerConfigBase.

        主题URN

        :param topic_urn: The topic_urn of this SchedulerConfigBase.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, SchedulerConfigBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
