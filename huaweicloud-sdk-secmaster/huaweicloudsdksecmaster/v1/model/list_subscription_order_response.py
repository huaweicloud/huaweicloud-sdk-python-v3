# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csb_version': 'str',
        'ecs_count': 'int',
        'resources': 'list[SubscriptionResource]',
        'subscription_count': 'int',
        'subscriptions': 'list[SmnSubscription]'
    }

    attribute_map = {
        'csb_version': 'csb_version',
        'ecs_count': 'ecs_count',
        'resources': 'resources',
        'subscription_count': 'subscription_count',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, csb_version=None, ecs_count=None, resources=None, subscription_count=None, subscriptions=None):
        r"""ListSubscriptionOrderResponse

        The model defined in huaweicloud sdk

        :param csb_version: 租户当前的版本信息 BASIC(基础版)，STANDARD（标准版），PROFESSIONAL（专业版），NA（无版本），大小写不敏感
        :type csb_version: str
        :param ecs_count: ecs个数，当请求参数purchase&#x3D;true时才会返回该值，否则为0
        :type ecs_count: int
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResource`]
        :param subscription_count: topic订阅条数，当请求参数为smn&#x3D;true，返回该字段
        :type subscription_count: int
        :param subscriptions: 租户订阅信息，当请求参数为smn&#x3D;true，会返回租户名下可订阅的smn topic列表
        :type subscriptions: list[:class:`huaweicloudsdksecmaster.v1.SmnSubscription`]
        """
        
        super().__init__()

        self._csb_version = None
        self._ecs_count = None
        self._resources = None
        self._subscription_count = None
        self._subscriptions = None
        self.discriminator = None

        if csb_version is not None:
            self.csb_version = csb_version
        if ecs_count is not None:
            self.ecs_count = ecs_count
        if resources is not None:
            self.resources = resources
        if subscription_count is not None:
            self.subscription_count = subscription_count
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def csb_version(self):
        r"""Gets the csb_version of this ListSubscriptionOrderResponse.

        租户当前的版本信息 BASIC(基础版)，STANDARD（标准版），PROFESSIONAL（专业版），NA（无版本），大小写不敏感

        :return: The csb_version of this ListSubscriptionOrderResponse.
        :rtype: str
        """
        return self._csb_version

    @csb_version.setter
    def csb_version(self, csb_version):
        r"""Sets the csb_version of this ListSubscriptionOrderResponse.

        租户当前的版本信息 BASIC(基础版)，STANDARD（标准版），PROFESSIONAL（专业版），NA（无版本），大小写不敏感

        :param csb_version: The csb_version of this ListSubscriptionOrderResponse.
        :type csb_version: str
        """
        self._csb_version = csb_version

    @property
    def ecs_count(self):
        r"""Gets the ecs_count of this ListSubscriptionOrderResponse.

        ecs个数，当请求参数purchase=true时才会返回该值，否则为0

        :return: The ecs_count of this ListSubscriptionOrderResponse.
        :rtype: int
        """
        return self._ecs_count

    @ecs_count.setter
    def ecs_count(self, ecs_count):
        r"""Sets the ecs_count of this ListSubscriptionOrderResponse.

        ecs个数，当请求参数purchase=true时才会返回该值，否则为0

        :param ecs_count: The ecs_count of this ListSubscriptionOrderResponse.
        :type ecs_count: int
        """
        self._ecs_count = ecs_count

    @property
    def resources(self):
        r"""Gets the resources of this ListSubscriptionOrderResponse.

        资源列表

        :return: The resources of this ListSubscriptionOrderResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListSubscriptionOrderResponse.

        资源列表

        :param resources: The resources of this ListSubscriptionOrderResponse.
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionResource`]
        """
        self._resources = resources

    @property
    def subscription_count(self):
        r"""Gets the subscription_count of this ListSubscriptionOrderResponse.

        topic订阅条数，当请求参数为smn=true，返回该字段

        :return: The subscription_count of this ListSubscriptionOrderResponse.
        :rtype: int
        """
        return self._subscription_count

    @subscription_count.setter
    def subscription_count(self, subscription_count):
        r"""Sets the subscription_count of this ListSubscriptionOrderResponse.

        topic订阅条数，当请求参数为smn=true，返回该字段

        :param subscription_count: The subscription_count of this ListSubscriptionOrderResponse.
        :type subscription_count: int
        """
        self._subscription_count = subscription_count

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this ListSubscriptionOrderResponse.

        租户订阅信息，当请求参数为smn=true，会返回租户名下可订阅的smn topic列表

        :return: The subscriptions of this ListSubscriptionOrderResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SmnSubscription`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this ListSubscriptionOrderResponse.

        租户订阅信息，当请求参数为smn=true，会返回租户名下可订阅的smn topic列表

        :param subscriptions: The subscriptions of this ListSubscriptionOrderResponse.
        :type subscriptions: list[:class:`huaweicloudsdksecmaster.v1.SmnSubscription`]
        """
        self._subscriptions = subscriptions

    def to_dict(self):
        import warnings
        warnings.warn("ListSubscriptionOrderResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListSubscriptionOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
