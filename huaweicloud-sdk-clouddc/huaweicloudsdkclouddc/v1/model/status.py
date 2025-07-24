# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Status:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'State',
        'health': 'Health'
    }

    attribute_map = {
        'state': 'state',
        'health': 'health'
    }

    def __init__(self, state=None, health=None):
        r"""Status

        The model defined in huaweicloud sdk

        :param state: 
        :type state: :class:`huaweicloudsdkclouddc.v1.State`
        :param health: 
        :type health: :class:`huaweicloudsdkclouddc.v1.Health`
        """
        
        

        self._state = None
        self._health = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if health is not None:
            self.health = health

    @property
    def state(self):
        r"""Gets the state of this Status.

        :return: The state of this Status.
        :rtype: :class:`huaweicloudsdkclouddc.v1.State`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Status.

        :param state: The state of this Status.
        :type state: :class:`huaweicloudsdkclouddc.v1.State`
        """
        self._state = state

    @property
    def health(self):
        r"""Gets the health of this Status.

        :return: The health of this Status.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Health`
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this Status.

        :param health: The health of this Status.
        :type health: :class:`huaweicloudsdkclouddc.v1.Health`
        """
        self._health = health

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
