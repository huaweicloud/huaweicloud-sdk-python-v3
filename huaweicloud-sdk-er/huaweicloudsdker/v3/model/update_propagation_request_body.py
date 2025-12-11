# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePropagationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_policy': 'ImportRoutePolicy'
    }

    attribute_map = {
        'route_policy': 'route_policy'
    }

    def __init__(self, route_policy=None):
        r"""UpdatePropagationRequestBody

        The model defined in huaweicloud sdk

        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        """
        
        

        self._route_policy = None
        self.discriminator = None

        self.route_policy = route_policy

    @property
    def route_policy(self):
        r"""Gets the route_policy of this UpdatePropagationRequestBody.

        :return: The route_policy of this UpdatePropagationRequestBody.
        :rtype: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        r"""Sets the route_policy of this UpdatePropagationRequestBody.

        :param route_policy: The route_policy of this UpdatePropagationRequestBody.
        :type route_policy: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        """
        self._route_policy = route_policy

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
        if not isinstance(other, UpdatePropagationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
