# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'InstanceActionType',
        'parameters': 'InstanceActionParameters'
    }

    attribute_map = {
        'action': 'action',
        'parameters': 'parameters'
    }

    def __init__(self, action=None, parameters=None):
        """InstanceAction

        The model defined in huaweicloud sdk

        :param action: 
        :type action: :class:`huaweicloudsdkservicestage.v2.InstanceActionType`
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkservicestage.v2.InstanceActionParameters`
        """
        
        

        self._action = None
        self._parameters = None
        self.discriminator = None

        self.action = action
        if parameters is not None:
            self.parameters = parameters

    @property
    def action(self):
        """Gets the action of this InstanceAction.

        :return: The action of this InstanceAction.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceActionType`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InstanceAction.

        :param action: The action of this InstanceAction.
        :type action: :class:`huaweicloudsdkservicestage.v2.InstanceActionType`
        """
        self._action = action

    @property
    def parameters(self):
        """Gets the parameters of this InstanceAction.

        :return: The parameters of this InstanceAction.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceActionParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InstanceAction.

        :param parameters: The parameters of this InstanceAction.
        :type parameters: :class:`huaweicloudsdkservicestage.v2.InstanceActionParameters`
        """
        self._parameters = parameters

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
        if not isinstance(other, InstanceAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
