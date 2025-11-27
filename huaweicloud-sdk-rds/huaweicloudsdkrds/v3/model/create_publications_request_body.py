# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicationsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publication_name': 'str',
        'publication_database': 'str',
        'is_create_snapshot_immediately': 'str',
        'subscription_options': 'SubscriptionOption',
        'job_schedule': 'OperateUsedJobSchedule',
        'is_select_all_table': 'bool',
        'extend_tables': 'list[str]',
        'tables': 'list[PublicationTableInfoRequest]'
    }

    attribute_map = {
        'publication_name': 'publication_name',
        'publication_database': 'publication_database',
        'is_create_snapshot_immediately': 'is_create_snapshot_immediately',
        'subscription_options': 'subscription_options',
        'job_schedule': 'job_schedule',
        'is_select_all_table': 'is_select_all_table',
        'extend_tables': 'extend_tables',
        'tables': 'tables'
    }

    def __init__(self, publication_name=None, publication_database=None, is_create_snapshot_immediately=None, subscription_options=None, job_schedule=None, is_select_all_table=None, extend_tables=None, tables=None):
        r"""CreatePublicationsRequestBody

        The model defined in huaweicloud sdk

        :param publication_name: 发布名称。  发布名称长度可在5～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符。
        :type publication_name: str
        :param publication_database: 发布数据库名。
        :type publication_database: str
        :param is_create_snapshot_immediately: 是否立即创建快照。
        :type is_create_snapshot_immediately: str
        :param subscription_options: 
        :type subscription_options: :class:`huaweicloudsdkrds.v3.SubscriptionOption`
        :param job_schedule: 
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        :param is_select_all_table: 是否选择所有数据表。
        :type is_select_all_table: bool
        :param extend_tables: 全选所有表后需要去除的表。
        :type extend_tables: list[str]
        :param tables: 发布数据表。
        :type tables: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoRequest`]
        """
        
        

        self._publication_name = None
        self._publication_database = None
        self._is_create_snapshot_immediately = None
        self._subscription_options = None
        self._job_schedule = None
        self._is_select_all_table = None
        self._extend_tables = None
        self._tables = None
        self.discriminator = None

        self.publication_name = publication_name
        self.publication_database = publication_database
        self.is_create_snapshot_immediately = is_create_snapshot_immediately
        if subscription_options is not None:
            self.subscription_options = subscription_options
        self.job_schedule = job_schedule
        if is_select_all_table is not None:
            self.is_select_all_table = is_select_all_table
        if extend_tables is not None:
            self.extend_tables = extend_tables
        self.tables = tables

    @property
    def publication_name(self):
        r"""Gets the publication_name of this CreatePublicationsRequestBody.

        发布名称。  发布名称长度可在5～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符。

        :return: The publication_name of this CreatePublicationsRequestBody.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this CreatePublicationsRequestBody.

        发布名称。  发布名称长度可在5～64个字符之间，由字母、数字或下划线组成，不能包含其他特殊字符。

        :param publication_name: The publication_name of this CreatePublicationsRequestBody.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def publication_database(self):
        r"""Gets the publication_database of this CreatePublicationsRequestBody.

        发布数据库名。

        :return: The publication_database of this CreatePublicationsRequestBody.
        :rtype: str
        """
        return self._publication_database

    @publication_database.setter
    def publication_database(self, publication_database):
        r"""Sets the publication_database of this CreatePublicationsRequestBody.

        发布数据库名。

        :param publication_database: The publication_database of this CreatePublicationsRequestBody.
        :type publication_database: str
        """
        self._publication_database = publication_database

    @property
    def is_create_snapshot_immediately(self):
        r"""Gets the is_create_snapshot_immediately of this CreatePublicationsRequestBody.

        是否立即创建快照。

        :return: The is_create_snapshot_immediately of this CreatePublicationsRequestBody.
        :rtype: str
        """
        return self._is_create_snapshot_immediately

    @is_create_snapshot_immediately.setter
    def is_create_snapshot_immediately(self, is_create_snapshot_immediately):
        r"""Sets the is_create_snapshot_immediately of this CreatePublicationsRequestBody.

        是否立即创建快照。

        :param is_create_snapshot_immediately: The is_create_snapshot_immediately of this CreatePublicationsRequestBody.
        :type is_create_snapshot_immediately: str
        """
        self._is_create_snapshot_immediately = is_create_snapshot_immediately

    @property
    def subscription_options(self):
        r"""Gets the subscription_options of this CreatePublicationsRequestBody.

        :return: The subscription_options of this CreatePublicationsRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SubscriptionOption`
        """
        return self._subscription_options

    @subscription_options.setter
    def subscription_options(self, subscription_options):
        r"""Sets the subscription_options of this CreatePublicationsRequestBody.

        :param subscription_options: The subscription_options of this CreatePublicationsRequestBody.
        :type subscription_options: :class:`huaweicloudsdkrds.v3.SubscriptionOption`
        """
        self._subscription_options = subscription_options

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this CreatePublicationsRequestBody.

        :return: The job_schedule of this CreatePublicationsRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this CreatePublicationsRequestBody.

        :param job_schedule: The job_schedule of this CreatePublicationsRequestBody.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        self._job_schedule = job_schedule

    @property
    def is_select_all_table(self):
        r"""Gets the is_select_all_table of this CreatePublicationsRequestBody.

        是否选择所有数据表。

        :return: The is_select_all_table of this CreatePublicationsRequestBody.
        :rtype: bool
        """
        return self._is_select_all_table

    @is_select_all_table.setter
    def is_select_all_table(self, is_select_all_table):
        r"""Sets the is_select_all_table of this CreatePublicationsRequestBody.

        是否选择所有数据表。

        :param is_select_all_table: The is_select_all_table of this CreatePublicationsRequestBody.
        :type is_select_all_table: bool
        """
        self._is_select_all_table = is_select_all_table

    @property
    def extend_tables(self):
        r"""Gets the extend_tables of this CreatePublicationsRequestBody.

        全选所有表后需要去除的表。

        :return: The extend_tables of this CreatePublicationsRequestBody.
        :rtype: list[str]
        """
        return self._extend_tables

    @extend_tables.setter
    def extend_tables(self, extend_tables):
        r"""Sets the extend_tables of this CreatePublicationsRequestBody.

        全选所有表后需要去除的表。

        :param extend_tables: The extend_tables of this CreatePublicationsRequestBody.
        :type extend_tables: list[str]
        """
        self._extend_tables = extend_tables

    @property
    def tables(self):
        r"""Gets the tables of this CreatePublicationsRequestBody.

        发布数据表。

        :return: The tables of this CreatePublicationsRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoRequest`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this CreatePublicationsRequestBody.

        发布数据表。

        :param tables: The tables of this CreatePublicationsRequestBody.
        :type tables: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoRequest`]
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
        if not isinstance(other, CreatePublicationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
