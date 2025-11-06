# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_database': 'str',
        'subscription_type': 'str',
        'initialize_at': 'str',
        'initialize_info': 'CreateSubscriptionInfoInitializeInfo',
        'independent_agent': 'bool',
        'job_schedule': 'OperateUsedJobSchedule',
        'bak_file_name': 'str',
        'bak_bucket_name': 'str',
        'publication_subscription': 'CreateSubscription4PublicationInfo',
        'local_subscription': 'CreateSubscription4InstanceInfo'
    }

    attribute_map = {
        'subscription_database': 'subscription_database',
        'subscription_type': 'subscription_type',
        'initialize_at': 'initialize_at',
        'initialize_info': 'initialize_info',
        'independent_agent': 'independent_agent',
        'job_schedule': 'job_schedule',
        'bak_file_name': 'bak_file_name',
        'bak_bucket_name': 'bak_bucket_name',
        'publication_subscription': 'publication_subscription',
        'local_subscription': 'local_subscription'
    }

    def __init__(self, subscription_database=None, subscription_type=None, initialize_at=None, initialize_info=None, independent_agent=None, job_schedule=None, bak_file_name=None, bak_bucket_name=None, publication_subscription=None, local_subscription=None):
        r"""CreateSubscriptionInfo

        The model defined in huaweicloud sdk

        :param subscription_database: 订阅数据库名。
        :type subscription_database: str
        :param subscription_type: 订阅方式，push:推送。
        :type subscription_type: str
        :param initialize_at: 初始化类型：不初始化(do_not)、立即初始化(immediate)、首次同步初始化(at_first_sync)。
        :type initialize_at: str
        :param initialize_info: 
        :type initialize_info: :class:`huaweicloudsdkrds.v3.CreateSubscriptionInfoInitializeInfo`
        :param independent_agent: 独立的分发代理。  true：使用。 false：不使用。
        :type independent_agent: bool
        :param job_schedule: 
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        :param bak_file_name: 备份文件名称。若该值不为空，则订阅初始化方式为通过备份文件初始化。
        :type bak_file_name: str
        :param bak_bucket_name: 备份文件所在的obs桶名。 若bak_file_name为空，该参数无效。 若该值为空，则备份文件来源为rds的备份文件。 若该值不为空，则备份文件来源为用户obs桶。
        :type bak_bucket_name: str
        :param publication_subscription: 
        :type publication_subscription: :class:`huaweicloudsdkrds.v3.CreateSubscription4PublicationInfo`
        :param local_subscription: 
        :type local_subscription: :class:`huaweicloudsdkrds.v3.CreateSubscription4InstanceInfo`
        """
        
        

        self._subscription_database = None
        self._subscription_type = None
        self._initialize_at = None
        self._initialize_info = None
        self._independent_agent = None
        self._job_schedule = None
        self._bak_file_name = None
        self._bak_bucket_name = None
        self._publication_subscription = None
        self._local_subscription = None
        self.discriminator = None

        self.subscription_database = subscription_database
        self.subscription_type = subscription_type
        self.initialize_at = initialize_at
        if initialize_info is not None:
            self.initialize_info = initialize_info
        if independent_agent is not None:
            self.independent_agent = independent_agent
        self.job_schedule = job_schedule
        if bak_file_name is not None:
            self.bak_file_name = bak_file_name
        if bak_bucket_name is not None:
            self.bak_bucket_name = bak_bucket_name
        if publication_subscription is not None:
            self.publication_subscription = publication_subscription
        if local_subscription is not None:
            self.local_subscription = local_subscription

    @property
    def subscription_database(self):
        r"""Gets the subscription_database of this CreateSubscriptionInfo.

        订阅数据库名。

        :return: The subscription_database of this CreateSubscriptionInfo.
        :rtype: str
        """
        return self._subscription_database

    @subscription_database.setter
    def subscription_database(self, subscription_database):
        r"""Sets the subscription_database of this CreateSubscriptionInfo.

        订阅数据库名。

        :param subscription_database: The subscription_database of this CreateSubscriptionInfo.
        :type subscription_database: str
        """
        self._subscription_database = subscription_database

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this CreateSubscriptionInfo.

        订阅方式，push:推送。

        :return: The subscription_type of this CreateSubscriptionInfo.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this CreateSubscriptionInfo.

        订阅方式，push:推送。

        :param subscription_type: The subscription_type of this CreateSubscriptionInfo.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def initialize_at(self):
        r"""Gets the initialize_at of this CreateSubscriptionInfo.

        初始化类型：不初始化(do_not)、立即初始化(immediate)、首次同步初始化(at_first_sync)。

        :return: The initialize_at of this CreateSubscriptionInfo.
        :rtype: str
        """
        return self._initialize_at

    @initialize_at.setter
    def initialize_at(self, initialize_at):
        r"""Sets the initialize_at of this CreateSubscriptionInfo.

        初始化类型：不初始化(do_not)、立即初始化(immediate)、首次同步初始化(at_first_sync)。

        :param initialize_at: The initialize_at of this CreateSubscriptionInfo.
        :type initialize_at: str
        """
        self._initialize_at = initialize_at

    @property
    def initialize_info(self):
        r"""Gets the initialize_info of this CreateSubscriptionInfo.

        :return: The initialize_info of this CreateSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSubscriptionInfoInitializeInfo`
        """
        return self._initialize_info

    @initialize_info.setter
    def initialize_info(self, initialize_info):
        r"""Sets the initialize_info of this CreateSubscriptionInfo.

        :param initialize_info: The initialize_info of this CreateSubscriptionInfo.
        :type initialize_info: :class:`huaweicloudsdkrds.v3.CreateSubscriptionInfoInitializeInfo`
        """
        self._initialize_info = initialize_info

    @property
    def independent_agent(self):
        r"""Gets the independent_agent of this CreateSubscriptionInfo.

        独立的分发代理。  true：使用。 false：不使用。

        :return: The independent_agent of this CreateSubscriptionInfo.
        :rtype: bool
        """
        return self._independent_agent

    @independent_agent.setter
    def independent_agent(self, independent_agent):
        r"""Sets the independent_agent of this CreateSubscriptionInfo.

        独立的分发代理。  true：使用。 false：不使用。

        :param independent_agent: The independent_agent of this CreateSubscriptionInfo.
        :type independent_agent: bool
        """
        self._independent_agent = independent_agent

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this CreateSubscriptionInfo.

        :return: The job_schedule of this CreateSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this CreateSubscriptionInfo.

        :param job_schedule: The job_schedule of this CreateSubscriptionInfo.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.OperateUsedJobSchedule`
        """
        self._job_schedule = job_schedule

    @property
    def bak_file_name(self):
        r"""Gets the bak_file_name of this CreateSubscriptionInfo.

        备份文件名称。若该值不为空，则订阅初始化方式为通过备份文件初始化。

        :return: The bak_file_name of this CreateSubscriptionInfo.
        :rtype: str
        """
        return self._bak_file_name

    @bak_file_name.setter
    def bak_file_name(self, bak_file_name):
        r"""Sets the bak_file_name of this CreateSubscriptionInfo.

        备份文件名称。若该值不为空，则订阅初始化方式为通过备份文件初始化。

        :param bak_file_name: The bak_file_name of this CreateSubscriptionInfo.
        :type bak_file_name: str
        """
        self._bak_file_name = bak_file_name

    @property
    def bak_bucket_name(self):
        r"""Gets the bak_bucket_name of this CreateSubscriptionInfo.

        备份文件所在的obs桶名。 若bak_file_name为空，该参数无效。 若该值为空，则备份文件来源为rds的备份文件。 若该值不为空，则备份文件来源为用户obs桶。

        :return: The bak_bucket_name of this CreateSubscriptionInfo.
        :rtype: str
        """
        return self._bak_bucket_name

    @bak_bucket_name.setter
    def bak_bucket_name(self, bak_bucket_name):
        r"""Sets the bak_bucket_name of this CreateSubscriptionInfo.

        备份文件所在的obs桶名。 若bak_file_name为空，该参数无效。 若该值为空，则备份文件来源为rds的备份文件。 若该值不为空，则备份文件来源为用户obs桶。

        :param bak_bucket_name: The bak_bucket_name of this CreateSubscriptionInfo.
        :type bak_bucket_name: str
        """
        self._bak_bucket_name = bak_bucket_name

    @property
    def publication_subscription(self):
        r"""Gets the publication_subscription of this CreateSubscriptionInfo.

        :return: The publication_subscription of this CreateSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSubscription4PublicationInfo`
        """
        return self._publication_subscription

    @publication_subscription.setter
    def publication_subscription(self, publication_subscription):
        r"""Sets the publication_subscription of this CreateSubscriptionInfo.

        :param publication_subscription: The publication_subscription of this CreateSubscriptionInfo.
        :type publication_subscription: :class:`huaweicloudsdkrds.v3.CreateSubscription4PublicationInfo`
        """
        self._publication_subscription = publication_subscription

    @property
    def local_subscription(self):
        r"""Gets the local_subscription of this CreateSubscriptionInfo.

        :return: The local_subscription of this CreateSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSubscription4InstanceInfo`
        """
        return self._local_subscription

    @local_subscription.setter
    def local_subscription(self, local_subscription):
        r"""Sets the local_subscription of this CreateSubscriptionInfo.

        :param local_subscription: The local_subscription of this CreateSubscriptionInfo.
        :type local_subscription: :class:`huaweicloudsdkrds.v3.CreateSubscription4InstanceInfo`
        """
        self._local_subscription = local_subscription

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
        if not isinstance(other, CreateSubscriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
