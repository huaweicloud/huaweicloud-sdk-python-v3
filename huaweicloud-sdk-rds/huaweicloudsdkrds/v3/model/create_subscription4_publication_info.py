# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscription4PublicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_instance_id': 'str',
        'user_info': 'ReplicationUserInfo'
    }

    attribute_map = {
        'subscription_instance_id': 'subscription_instance_id',
        'user_info': 'user_info'
    }

    def __init__(self, subscription_instance_id=None, user_info=None):
        r"""CreateSubscription4PublicationInfo

        The model defined in huaweicloud sdk

        :param subscription_instance_id: 订阅服务器来源为云上实例时的订阅实例id。
        :type subscription_instance_id: str
        :param user_info: 
        :type user_info: :class:`huaweicloudsdkrds.v3.ReplicationUserInfo`
        """
        
        

        self._subscription_instance_id = None
        self._user_info = None
        self.discriminator = None

        self.subscription_instance_id = subscription_instance_id
        if user_info is not None:
            self.user_info = user_info

    @property
    def subscription_instance_id(self):
        r"""Gets the subscription_instance_id of this CreateSubscription4PublicationInfo.

        订阅服务器来源为云上实例时的订阅实例id。

        :return: The subscription_instance_id of this CreateSubscription4PublicationInfo.
        :rtype: str
        """
        return self._subscription_instance_id

    @subscription_instance_id.setter
    def subscription_instance_id(self, subscription_instance_id):
        r"""Sets the subscription_instance_id of this CreateSubscription4PublicationInfo.

        订阅服务器来源为云上实例时的订阅实例id。

        :param subscription_instance_id: The subscription_instance_id of this CreateSubscription4PublicationInfo.
        :type subscription_instance_id: str
        """
        self._subscription_instance_id = subscription_instance_id

    @property
    def user_info(self):
        r"""Gets the user_info of this CreateSubscription4PublicationInfo.

        :return: The user_info of this CreateSubscription4PublicationInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.ReplicationUserInfo`
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        r"""Sets the user_info of this CreateSubscription4PublicationInfo.

        :param user_info: The user_info of this CreateSubscription4PublicationInfo.
        :type user_info: :class:`huaweicloudsdkrds.v3.ReplicationUserInfo`
        """
        self._user_info = user_info

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
        if not isinstance(other, CreateSubscription4PublicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
