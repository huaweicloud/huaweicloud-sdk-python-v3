# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPublicationsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_options': 'SubscriptionOption',
        'job_schedule': 'OperateUsedJobSchedule',
        'is_select_all_table': 'bool',
        'extend_tables': 'list[str]',
        'tables': 'list[PublicationTableInfoRequest]'
    }

    attribute_map = {
        'subscription_options': 'subscription_options',
        'job_schedule': 'job_schedule',
        'is_select_all_table': 'is_select_all_table',
        'extend_tables': 'extend_tables',
        'tables': 'tables'
    }

    def __init__(self, subscription_options=None, job_schedule=None, is_select_all_table=None, extend_tables=None, tables=None):
        r"""ModifyPublicationsRequestBody

        The model defined in huaweicloud sdk

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
        
        

        self._subscription_options = None
        self._job_schedule = None
        self._is_select_all_table = None
        self._extend_tables = None
        self._tables = None
        self.discriminator = None

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
    def subscription_options(self):
        r"""Gets the subscription_options of this ModifyPublicationsRequestBody.

        :return: The subscription_options of this ModifyPublicationsRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SubscriptionOption`
        """
        return self._subscription_options

    @subscription_options.setter
    def subscription_options(self, subscription_options):
        r"""Sets the subscription_options of this ModifyPublicationsRequestBody.

        :param subscription_options: The subscription_options of this ModifyPublicationsRequestBody.
        :type subscription_options: :class:`huaweicloudsdkrds.v3.SubscriptionOption`
        """
        self._subscription_options = subscription_options

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this ModifyPublicationsRequestBody.

        :return: The job_schedule of this ModifyPublicationsRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this ModifyPublicationsRequestBody.

        :param job_schedule: The job_schedule of this ModifyPublicationsRequestBody.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        self._job_schedule = job_schedule

    @property
    def is_select_all_table(self):
        r"""Gets the is_select_all_table of this ModifyPublicationsRequestBody.

        是否选择所有数据表。

        :return: The is_select_all_table of this ModifyPublicationsRequestBody.
        :rtype: bool
        """
        return self._is_select_all_table

    @is_select_all_table.setter
    def is_select_all_table(self, is_select_all_table):
        r"""Sets the is_select_all_table of this ModifyPublicationsRequestBody.

        是否选择所有数据表。

        :param is_select_all_table: The is_select_all_table of this ModifyPublicationsRequestBody.
        :type is_select_all_table: bool
        """
        self._is_select_all_table = is_select_all_table

    @property
    def extend_tables(self):
        r"""Gets the extend_tables of this ModifyPublicationsRequestBody.

        全选所有表后需要去除的表。

        :return: The extend_tables of this ModifyPublicationsRequestBody.
        :rtype: list[str]
        """
        return self._extend_tables

    @extend_tables.setter
    def extend_tables(self, extend_tables):
        r"""Sets the extend_tables of this ModifyPublicationsRequestBody.

        全选所有表后需要去除的表。

        :param extend_tables: The extend_tables of this ModifyPublicationsRequestBody.
        :type extend_tables: list[str]
        """
        self._extend_tables = extend_tables

    @property
    def tables(self):
        r"""Gets the tables of this ModifyPublicationsRequestBody.

        发布数据表。

        :return: The tables of this ModifyPublicationsRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PublicationTableInfoRequest`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this ModifyPublicationsRequestBody.

        发布数据表。

        :param tables: The tables of this ModifyPublicationsRequestBody.
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
        if not isinstance(other, ModifyPublicationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
