# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionInfo:

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
        'publication_id': 'str',
        'publication_name': 'str',
        'is_cloud': 'bool',
        'subscription_database': 'str',
        'subscription_type': 'str',
        'publication_subscription': 'Subscription4PublicationInfo',
        'local_subscription': 'Subscription4InstanceInfo',
        'job_schedule': 'UsedJobSchedule'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'publication_id': 'publication_id',
        'publication_name': 'publication_name',
        'is_cloud': 'is_cloud',
        'subscription_database': 'subscription_database',
        'subscription_type': 'subscription_type',
        'publication_subscription': 'publication_subscription',
        'local_subscription': 'local_subscription',
        'job_schedule': 'job_schedule'
    }

    def __init__(self, id=None, status=None, publication_id=None, publication_name=None, is_cloud=None, subscription_database=None, subscription_type=None, publication_subscription=None, local_subscription=None, job_schedule=None):
        r"""ListSubscriptionInfo

        The model defined in huaweicloud sdk

        :param id: 订阅id。
        :type id: str
        :param status: 订阅状态。normal，abnormal，creating，createfail
        :type status: str
        :param publication_id: 发布id。
        :type publication_id: str
        :param publication_name: 发布名称。
        :type publication_name: str
        :param is_cloud: 订阅服务器来源。true：订阅服务器为云上实例, false：订阅服务器非云上实例。
        :type is_cloud: bool
        :param subscription_database: 目标数据库名。
        :type subscription_database: str
        :param subscription_type: 订阅方式，push:推送。
        :type subscription_type: str
        :param publication_subscription: 
        :type publication_subscription: :class:`huaweicloudsdkrds.v3.Subscription4PublicationInfo`
        :param local_subscription: 
        :type local_subscription: :class:`huaweicloudsdkrds.v3.Subscription4InstanceInfo`
        :param job_schedule: 
        :type job_schedule: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        """
        
        

        self._id = None
        self._status = None
        self._publication_id = None
        self._publication_name = None
        self._is_cloud = None
        self._subscription_database = None
        self._subscription_type = None
        self._publication_subscription = None
        self._local_subscription = None
        self._job_schedule = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if publication_id is not None:
            self.publication_id = publication_id
        if publication_name is not None:
            self.publication_name = publication_name
        if is_cloud is not None:
            self.is_cloud = is_cloud
        if subscription_database is not None:
            self.subscription_database = subscription_database
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if publication_subscription is not None:
            self.publication_subscription = publication_subscription
        if local_subscription is not None:
            self.local_subscription = local_subscription
        if job_schedule is not None:
            self.job_schedule = job_schedule

    @property
    def id(self):
        r"""Gets the id of this ListSubscriptionInfo.

        订阅id。

        :return: The id of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSubscriptionInfo.

        订阅id。

        :param id: The id of this ListSubscriptionInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ListSubscriptionInfo.

        订阅状态。normal，abnormal，creating，createfail

        :return: The status of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSubscriptionInfo.

        订阅状态。normal，abnormal，creating，createfail

        :param status: The status of this ListSubscriptionInfo.
        :type status: str
        """
        self._status = status

    @property
    def publication_id(self):
        r"""Gets the publication_id of this ListSubscriptionInfo.

        发布id。

        :return: The publication_id of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._publication_id

    @publication_id.setter
    def publication_id(self, publication_id):
        r"""Sets the publication_id of this ListSubscriptionInfo.

        发布id。

        :param publication_id: The publication_id of this ListSubscriptionInfo.
        :type publication_id: str
        """
        self._publication_id = publication_id

    @property
    def publication_name(self):
        r"""Gets the publication_name of this ListSubscriptionInfo.

        发布名称。

        :return: The publication_name of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._publication_name

    @publication_name.setter
    def publication_name(self, publication_name):
        r"""Sets the publication_name of this ListSubscriptionInfo.

        发布名称。

        :param publication_name: The publication_name of this ListSubscriptionInfo.
        :type publication_name: str
        """
        self._publication_name = publication_name

    @property
    def is_cloud(self):
        r"""Gets the is_cloud of this ListSubscriptionInfo.

        订阅服务器来源。true：订阅服务器为云上实例, false：订阅服务器非云上实例。

        :return: The is_cloud of this ListSubscriptionInfo.
        :rtype: bool
        """
        return self._is_cloud

    @is_cloud.setter
    def is_cloud(self, is_cloud):
        r"""Sets the is_cloud of this ListSubscriptionInfo.

        订阅服务器来源。true：订阅服务器为云上实例, false：订阅服务器非云上实例。

        :param is_cloud: The is_cloud of this ListSubscriptionInfo.
        :type is_cloud: bool
        """
        self._is_cloud = is_cloud

    @property
    def subscription_database(self):
        r"""Gets the subscription_database of this ListSubscriptionInfo.

        目标数据库名。

        :return: The subscription_database of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._subscription_database

    @subscription_database.setter
    def subscription_database(self, subscription_database):
        r"""Sets the subscription_database of this ListSubscriptionInfo.

        目标数据库名。

        :param subscription_database: The subscription_database of this ListSubscriptionInfo.
        :type subscription_database: str
        """
        self._subscription_database = subscription_database

    @property
    def subscription_type(self):
        r"""Gets the subscription_type of this ListSubscriptionInfo.

        订阅方式，push:推送。

        :return: The subscription_type of this ListSubscriptionInfo.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        r"""Sets the subscription_type of this ListSubscriptionInfo.

        订阅方式，push:推送。

        :param subscription_type: The subscription_type of this ListSubscriptionInfo.
        :type subscription_type: str
        """
        self._subscription_type = subscription_type

    @property
    def publication_subscription(self):
        r"""Gets the publication_subscription of this ListSubscriptionInfo.

        :return: The publication_subscription of this ListSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.Subscription4PublicationInfo`
        """
        return self._publication_subscription

    @publication_subscription.setter
    def publication_subscription(self, publication_subscription):
        r"""Sets the publication_subscription of this ListSubscriptionInfo.

        :param publication_subscription: The publication_subscription of this ListSubscriptionInfo.
        :type publication_subscription: :class:`huaweicloudsdkrds.v3.Subscription4PublicationInfo`
        """
        self._publication_subscription = publication_subscription

    @property
    def local_subscription(self):
        r"""Gets the local_subscription of this ListSubscriptionInfo.

        :return: The local_subscription of this ListSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.Subscription4InstanceInfo`
        """
        return self._local_subscription

    @local_subscription.setter
    def local_subscription(self, local_subscription):
        r"""Sets the local_subscription of this ListSubscriptionInfo.

        :param local_subscription: The local_subscription of this ListSubscriptionInfo.
        :type local_subscription: :class:`huaweicloudsdkrds.v3.Subscription4InstanceInfo`
        """
        self._local_subscription = local_subscription

    @property
    def job_schedule(self):
        r"""Gets the job_schedule of this ListSubscriptionInfo.

        :return: The job_schedule of this ListSubscriptionInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        """
        return self._job_schedule

    @job_schedule.setter
    def job_schedule(self, job_schedule):
        r"""Sets the job_schedule of this ListSubscriptionInfo.

        :param job_schedule: The job_schedule of this ListSubscriptionInfo.
        :type job_schedule: :class:`huaweicloudsdkrds.v3.UsedJobSchedule`
        """
        self._job_schedule = job_schedule

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
        if not isinstance(other, ListSubscriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
