# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryPublicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'publication_name': 'str',
        'publication_database': 'str',
        'subscription_count': 'int',
        'subscription_options': 'SubscriptionOptionsResult',
        'job_schedule': 'UsedJobSchedule',
        'is_select_all_table': 'bool',
        'extend_tables': 'list[str]',
        'tables': 'list[PublicationTableInfoResponse]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'publication_name': 'publication_name',
        'publication_database': 'publication_database',
        'subscription_count': 'subscription_count',
        'subscription_options': 'subscription_options',
        'job_schedule': 'job_schedule',
        'is_select_all_table': 'is_select_all_table',
        'extend_tables': 'extend_tables',
        'tables': 'tables'
    }

    def __init__(self, id=None, status=None, publication_name=None, publication_database=None, subscription_count=None, subscription_options=None, job_schedule=None, is_select_all_table=None, extend_tables=None, tables=None):
        r"""QueryPublicationInfo

        The model defined in huaweicloud sdk

        :param id: 发布id。
        :type id: str
        :param status: 发布状态。normal，abnormal，creating，modifying，createfail
        :type status: str
        :param publication_name: 发布名。
        :type publication_name: str
        :param publication_database: 发布数据库名。
        :type publication_database: str
        :param subscription_count: 订阅数。
        :type subscription_count: int
        :param subscription_options: 
        :type subscription_options: :class:`huaweicloudsdkrds.v3.SubscriptionOptionsResult`
        :param job_schedule: 
        :type job_schedule: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        :param is_select_all_table: 是否选择所有数据表。
        :type is_select_all_table: bool
        :param extend_tables: 全选所有表后需要去除的表。
        :type extend_tables: list[str]
        :param tables: 发布数据表。
        :type tables: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoResponse`]
        """
        
        

        self._id = None
        self._status = None
        self._publication_name = None
        self._publication_database = None
        self._subscription_count = None
        self._subscription_options = None
        self._job_schedule = None
        self._is_select_all_table = None
        self._extend_tables = None
        self._tables = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if publication_name is not None:
            self.publication_name = publication_name
        if publication_database is not None:
            self.publication_database = publication_database
        if subscription_count is not None:
            self.subscription_count = subscription_count
        if subscription_options is not None:
            self.subscription_options = subscription_options
        if job_schedule is not None:
            self.job_schedule = job_schedule
        if is_select_all_table is not None:
            self.is_select_all_table = is_select_all_table
        if extend_tables is not None:
            self.extend_tables = extend_tables
        if tables is not None:
            self.tables = tables

    @property
    def id(self):
        r"""Gets the id of this QueryPublicationInfo.

        发布id。

        :return: The id of this QueryPublicationInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryPublicationInfo.

        发布id。

        :param id: The id of this QueryPublicationInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this QueryPublicationInfo.

        发布状态。normal，abnormal，creating，modifying，createfail

        :return: The status of this QueryPublicationInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryPublicationInfo.

        发布状态。normal，abnormal，creating，modifying，createfail

        :param status: The status of this QueryPublicationInfo.
        :type status: str
        """
        self._status = status

    @property
    def publication_name(self):
        r"""Gets the publication_name of this QueryPublicationInfo.

        发布名。

        :return: The publication_name of this QueryPublicationInfo.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this QueryPublicationInfo.

        发布名。

        :param publication_name: The publication_name of this QueryPublicationInfo.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def publication_database(self):
        r"""Gets the publication_database of this QueryPublicationInfo.

        发布数据库名。

        :return: The publication_database of this QueryPublicationInfo.
        :rtype: str
        """
        return self._publication_database

    @publication_database.setter
    def publication_database(self, publication_database):
        r"""Sets the publication_database of this QueryPublicationInfo.

        发布数据库名。

        :param publication_database: The publication_database of this QueryPublicationInfo.
        :type publication_database: str
        """
        self._publication_database = publication_database

    @property
    def subscription_count(self):
        r"""Gets the subscription_count of this QueryPublicationInfo.

        订阅数。

        :return: The subscription_count of this QueryPublicationInfo.
        :rtype: int
        """
        return self._subscription_count

    @subscription_count.setter
    def subscription_count(self, subscription_count):
        r"""Sets the subscription_count of this QueryPublicationInfo.

        订阅数。

        :param subscription_count: The subscription_count of this QueryPublicationInfo.
        :type subscription_count: int
        """
        self._subscription_count = subscription_count

    @property
    def subscription_options(self):
        r"""Gets the subscription_options of this QueryPublicationInfo.

        :return: The subscription_options of this QueryPublicationInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.SubscriptionOptionsResult`
        """
        return self._subscription_options

    @subscription_options.setter
    def subscription_options(self, subscription_options):
        r"""Sets the subscription_options of this QueryPublicationInfo.

        :param subscription_options: The subscription_options of this QueryPublicationInfo.
        :type subscription_options: :class:`huaweicloudsdkrds.v3.SubscriptionOptionsResult`
        """
        self._subscription_options = subscription_options

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this QueryPublicationInfo.

        :return: The job_schedule of this QueryPublicationInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this QueryPublicationInfo.

        :param job_schedule: The job_schedule of this QueryPublicationInfo.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        """
        self._job_schedule = job_schedule

    @property
    def is_select_all_table(self):
        r"""Gets the is_select_all_table of this QueryPublicationInfo.

        是否选择所有数据表。

        :return: The is_select_all_table of this QueryPublicationInfo.
        :rtype: bool
        """
        return self._is_select_all_table

    @is_select_all_table.setter
    def is_select_all_table(self, is_select_all_table):
        r"""Sets the is_select_all_table of this QueryPublicationInfo.

        是否选择所有数据表。

        :param is_select_all_table: The is_select_all_table of this QueryPublicationInfo.
        :type is_select_all_table: bool
        """
        self._is_select_all_table = is_select_all_table

    @property
    def extend_tables(self):
        r"""Gets the extend_tables of this QueryPublicationInfo.

        全选所有表后需要去除的表。

        :return: The extend_tables of this QueryPublicationInfo.
        :rtype: list[str]
        """
        return self._extend_tables

    @extend_tables.setter
    def extend_tables(self, extend_tables):
        r"""Sets the extend_tables of this QueryPublicationInfo.

        全选所有表后需要去除的表。

        :param extend_tables: The extend_tables of this QueryPublicationInfo.
        :type extend_tables: list[str]
        """
        self._extend_tables = extend_tables

    @property
    def tables(self):
        r"""Gets the tables of this QueryPublicationInfo.

        发布数据表。

        :return: The tables of this QueryPublicationInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoResponse`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this QueryPublicationInfo.

        发布数据表。

        :param tables: The tables of this QueryPublicationInfo.
        :type tables: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoResponse`]
        """
        self._tables = tables

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
        if not isinstance(other, QueryPublicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
