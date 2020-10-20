# coding: utf-8

import pprint
import re

import six





class UpdateL7PolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'description': 'str',
        'name': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'name': 'name',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id'
    }

    def __init__(self, admin_state_up=True, description=None, name=None, redirect_listener_id=None, redirect_pool_id=None):
        """UpdateL7PolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._description = None
        self._name = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateL7PolicyOption.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this UpdateL7PolicyOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateL7PolicyOption.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this UpdateL7PolicyOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateL7PolicyOption.

        转发策略描述信息。

        :return: The description of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateL7PolicyOption.

        转发策略描述信息。

        :param description: The description of this UpdateL7PolicyOption.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateL7PolicyOption.

        转发策略名称。

        :return: The name of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateL7PolicyOption.

        转发策略名称。

        :param name: The name of this UpdateL7PolicyOption.
        :type: str
        """
        self._name = name

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this UpdateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。使用说明：只支持protocol为TERMINATED_HTTPS的listener。不能指定为其他loadbalancer下的listener。当action为REDIRECT_TO_POOL时，不可指定。

        :return: The redirect_listener_id of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this UpdateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。使用说明：只支持protocol为TERMINATED_HTTPS的listener。不能指定为其他loadbalancer下的listener。当action为REDIRECT_TO_POOL时，不可指定。

        :param redirect_listener_id: The redirect_listener_id of this UpdateL7PolicyOption.
        :type: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this UpdateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_LISTENER时，不可指定。

        :return: The redirect_pool_id of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this UpdateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_LISTENER时，不可指定。

        :param redirect_pool_id: The redirect_pool_id of this UpdateL7PolicyOption.
        :type: str
        """
        self._redirect_pool_id = redirect_pool_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateL7PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
