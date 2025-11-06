# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscriptions': 'list[CreateSubscriptionInfo]',
        'current_publication_id': 'str'
    }

    attribute_map = {
        'subscriptions': 'subscriptions',
        'current_publication_id': 'current_publication_id'
    }

    def __init__(self, subscriptions=None, current_publication_id=None):
        r"""CreateSubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param subscriptions: 订阅详情。一次最多创建十个订阅。
        :type subscriptions: list[:class:`huaweicloudsdkrds.v3.CreateSubscriptionInfo`]
        :param current_publication_id: 给发布创建订阅时的发布id。给发布创建订阅时必传，不传时则为创建本地订阅。
        :type current_publication_id: str
        """
        
        

        self._subscriptions = None
        self._current_publication_id = None
        self.discriminator = None

        self.subscriptions = subscriptions
        if current_publication_id is not None:
            self.current_publication_id = current_publication_id

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this CreateSubscriptionRequestBody.

        订阅详情。一次最多创建十个订阅。

        :return: The subscriptions of this CreateSubscriptionRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.CreateSubscriptionInfo`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this CreateSubscriptionRequestBody.

        订阅详情。一次最多创建十个订阅。

        :param subscriptions: The subscriptions of this CreateSubscriptionRequestBody.
        :type subscriptions: list[:class:`huaweicloudsdkrds.v3.CreateSubscriptionInfo`]
        """
        self._subscriptions = subscriptions

    @property
    def current_publication_id(self):
        r"""Gets the current_publication_id of this CreateSubscriptionRequestBody.

        给发布创建订阅时的发布id。给发布创建订阅时必传，不传时则为创建本地订阅。

        :return: The current_publication_id of this CreateSubscriptionRequestBody.
        :rtype: str
        """
        return self._current_publication_id

    @current_publication_id.setter
    def current_publication_id(self, current_publication_id):
        r"""Sets the current_publication_id of this CreateSubscriptionRequestBody.

        给发布创建订阅时的发布id。给发布创建订阅时必传，不传时则为创建本地订阅。

        :param current_publication_id: The current_publication_id of this CreateSubscriptionRequestBody.
        :type current_publication_id: str
        """
        self._current_publication_id = current_publication_id

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
        if not isinstance(other, CreateSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
