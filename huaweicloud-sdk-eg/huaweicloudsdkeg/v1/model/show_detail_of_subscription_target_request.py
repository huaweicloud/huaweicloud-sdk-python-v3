# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfSubscriptionTargetRequest:

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
        'target_id': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'target_id': 'target_id'
    }

    def __init__(self, subscription_id=None, target_id=None):
        """ShowDetailOfSubscriptionTargetRequest

        The model defined in huaweicloud sdk

        :param subscription_id: 事件订阅ID
        :type subscription_id: str
        :param target_id: 事件订阅目标ID
        :type target_id: str
        """
        
        

        self._subscription_id = None
        self._target_id = None
        self.discriminator = None

        self.subscription_id = subscription_id
        self.target_id = target_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ShowDetailOfSubscriptionTargetRequest.

        事件订阅ID

        :return: The subscription_id of this ShowDetailOfSubscriptionTargetRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ShowDetailOfSubscriptionTargetRequest.

        事件订阅ID

        :param subscription_id: The subscription_id of this ShowDetailOfSubscriptionTargetRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def target_id(self):
        """Gets the target_id of this ShowDetailOfSubscriptionTargetRequest.

        事件订阅目标ID

        :return: The target_id of this ShowDetailOfSubscriptionTargetRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ShowDetailOfSubscriptionTargetRequest.

        事件订阅目标ID

        :param target_id: The target_id of this ShowDetailOfSubscriptionTargetRequest.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, ShowDetailOfSubscriptionTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other