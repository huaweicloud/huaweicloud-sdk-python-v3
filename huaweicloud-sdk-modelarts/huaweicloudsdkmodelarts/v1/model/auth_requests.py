# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthRequests:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'action': 'str',
        'resource': 'str',
        'service_attributes': 'dict(str, str)'
    }

    attribute_map = {
        'action_id': 'action_id',
        'action': 'action',
        'resource': 'resource',
        'service_attributes': 'service_attributes'
    }

    def __init__(self, action_id=None, action=None, resource=None, service_attributes=None):
        r"""AuthRequests

        The model defined in huaweicloud sdk

        :param action_id: **参数解释**：随机UUID，用来定位使用。 **取值范围**不涉及。
        :type action_id: str
        :param action: **参数解释**：细粒度action。 **取值范围**不涉及。
        :type action: str
        :param resource: **参数解释**：资源。 **取值范围**不涉及。
        :type resource: str
        :param service_attributes: **参数解释**：操作对象。 **取值范围**不涉及。
        :type service_attributes: dict(str, str)
        """
        
        

        self._action_id = None
        self._action = None
        self._resource = None
        self._service_attributes = None
        self.discriminator = None

        self.action_id = action_id
        self.action = action
        if resource is not None:
            self.resource = resource
        if service_attributes is not None:
            self.service_attributes = service_attributes

    @property
    def action_id(self):
        r"""Gets the action_id of this AuthRequests.

        **参数解释**：随机UUID，用来定位使用。 **取值范围**不涉及。

        :return: The action_id of this AuthRequests.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this AuthRequests.

        **参数解释**：随机UUID，用来定位使用。 **取值范围**不涉及。

        :param action_id: The action_id of this AuthRequests.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action(self):
        r"""Gets the action of this AuthRequests.

        **参数解释**：细粒度action。 **取值范围**不涉及。

        :return: The action of this AuthRequests.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AuthRequests.

        **参数解释**：细粒度action。 **取值范围**不涉及。

        :param action: The action of this AuthRequests.
        :type action: str
        """
        self._action = action

    @property
    def resource(self):
        r"""Gets the resource of this AuthRequests.

        **参数解释**：资源。 **取值范围**不涉及。

        :return: The resource of this AuthRequests.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this AuthRequests.

        **参数解释**：资源。 **取值范围**不涉及。

        :param resource: The resource of this AuthRequests.
        :type resource: str
        """
        self._resource = resource

    @property
    def service_attributes(self):
        r"""Gets the service_attributes of this AuthRequests.

        **参数解释**：操作对象。 **取值范围**不涉及。

        :return: The service_attributes of this AuthRequests.
        :rtype: dict(str, str)
        """
        return self._service_attributes

    @service_attributes.setter
    def service_attributes(self, service_attributes):
        r"""Sets the service_attributes of this AuthRequests.

        **参数解释**：操作对象。 **取值范围**不涉及。

        :param service_attributes: The service_attributes of this AuthRequests.
        :type service_attributes: dict(str, str)
        """
        self._service_attributes = service_attributes

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
        if not isinstance(other, AuthRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
