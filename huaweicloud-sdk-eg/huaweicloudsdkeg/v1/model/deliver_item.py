# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeliverItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str',
        'subscription_name': 'str',
        'success_counts': 'int',
        'fail_counts': 'int',
        'all_deliver_times': 'int',
        'deliver_target_list': 'list[DeliverTarget]'
    }

    attribute_map = {
        'subscription_id': 'subscriptionId',
        'subscription_name': 'subscriptionName',
        'success_counts': 'successCounts',
        'fail_counts': 'failCounts',
        'all_deliver_times': 'allDeliverTimes',
        'deliver_target_list': 'deliverTargetList'
    }

    def __init__(self, subscription_id=None, subscription_name=None, success_counts=None, fail_counts=None, all_deliver_times=None, deliver_target_list=None):
        """DeliverItem

        The model defined in huaweicloud sdk

        :param subscription_id: 订阅ID，全局唯一
        :type subscription_id: str
        :param subscription_name: 订阅名称
        :type subscription_name: str
        :param success_counts: 成功目标个数
        :type success_counts: int
        :param fail_counts: 失败目标个数
        :type fail_counts: int
        :param all_deliver_times: 共投递次数
        :type all_deliver_times: int
        :param deliver_target_list: 投递详情
        :type deliver_target_list: list[:class:`huaweicloudsdkeg.v1.DeliverTarget`]
        """
        
        

        self._subscription_id = None
        self._subscription_name = None
        self._success_counts = None
        self._fail_counts = None
        self._all_deliver_times = None
        self._deliver_target_list = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_name is not None:
            self.subscription_name = subscription_name
        if success_counts is not None:
            self.success_counts = success_counts
        if fail_counts is not None:
            self.fail_counts = fail_counts
        if all_deliver_times is not None:
            self.all_deliver_times = all_deliver_times
        if deliver_target_list is not None:
            self.deliver_target_list = deliver_target_list

    @property
    def subscription_id(self):
        """Gets the subscription_id of this DeliverItem.

        订阅ID，全局唯一

        :return: The subscription_id of this DeliverItem.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this DeliverItem.

        订阅ID，全局唯一

        :param subscription_id: The subscription_id of this DeliverItem.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def subscription_name(self):
        """Gets the subscription_name of this DeliverItem.

        订阅名称

        :return: The subscription_name of this DeliverItem.
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this DeliverItem.

        订阅名称

        :param subscription_name: The subscription_name of this DeliverItem.
        :type subscription_name: str
        """
        self._subscription_name = subscription_name

    @property
    def success_counts(self):
        """Gets the success_counts of this DeliverItem.

        成功目标个数

        :return: The success_counts of this DeliverItem.
        :rtype: int
        """
        return self._success_counts

    @success_counts.setter
    def success_counts(self, success_counts):
        """Sets the success_counts of this DeliverItem.

        成功目标个数

        :param success_counts: The success_counts of this DeliverItem.
        :type success_counts: int
        """
        self._success_counts = success_counts

    @property
    def fail_counts(self):
        """Gets the fail_counts of this DeliverItem.

        失败目标个数

        :return: The fail_counts of this DeliverItem.
        :rtype: int
        """
        return self._fail_counts

    @fail_counts.setter
    def fail_counts(self, fail_counts):
        """Sets the fail_counts of this DeliverItem.

        失败目标个数

        :param fail_counts: The fail_counts of this DeliverItem.
        :type fail_counts: int
        """
        self._fail_counts = fail_counts

    @property
    def all_deliver_times(self):
        """Gets the all_deliver_times of this DeliverItem.

        共投递次数

        :return: The all_deliver_times of this DeliverItem.
        :rtype: int
        """
        return self._all_deliver_times

    @all_deliver_times.setter
    def all_deliver_times(self, all_deliver_times):
        """Sets the all_deliver_times of this DeliverItem.

        共投递次数

        :param all_deliver_times: The all_deliver_times of this DeliverItem.
        :type all_deliver_times: int
        """
        self._all_deliver_times = all_deliver_times

    @property
    def deliver_target_list(self):
        """Gets the deliver_target_list of this DeliverItem.

        投递详情

        :return: The deliver_target_list of this DeliverItem.
        :rtype: list[:class:`huaweicloudsdkeg.v1.DeliverTarget`]
        """
        return self._deliver_target_list

    @deliver_target_list.setter
    def deliver_target_list(self, deliver_target_list):
        """Sets the deliver_target_list of this DeliverItem.

        投递详情

        :param deliver_target_list: The deliver_target_list of this DeliverItem.
        :type deliver_target_list: list[:class:`huaweicloudsdkeg.v1.DeliverTarget`]
        """
        self._deliver_target_list = deliver_target_list

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
        if not isinstance(other, DeliverItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
