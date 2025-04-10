# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAgencyPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unbind_role_names': 'list[str]',
        'bind_role_names': 'list[str]'
    }

    attribute_map = {
        'unbind_role_names': 'unbind_role_names',
        'bind_role_names': 'bind_role_names'
    }

    def __init__(self, unbind_role_names=None, bind_role_names=None):
        r"""UpdateAgencyPolicyRequestBody

        The model defined in huaweicloud sdk

        :param unbind_role_names: 委托解绑的权限策略集合。
        :type unbind_role_names: list[str]
        :param bind_role_names: 委托绑定的权限策略集合。
        :type bind_role_names: list[str]
        """
        
        

        self._unbind_role_names = None
        self._bind_role_names = None
        self.discriminator = None

        self.unbind_role_names = unbind_role_names
        self.bind_role_names = bind_role_names

    @property
    def unbind_role_names(self):
        r"""Gets the unbind_role_names of this UpdateAgencyPolicyRequestBody.

        委托解绑的权限策略集合。

        :return: The unbind_role_names of this UpdateAgencyPolicyRequestBody.
        :rtype: list[str]
        """
        return self._unbind_role_names

    @unbind_role_names.setter
    def unbind_role_names(self, unbind_role_names):
        r"""Sets the unbind_role_names of this UpdateAgencyPolicyRequestBody.

        委托解绑的权限策略集合。

        :param unbind_role_names: The unbind_role_names of this UpdateAgencyPolicyRequestBody.
        :type unbind_role_names: list[str]
        """
        self._unbind_role_names = unbind_role_names

    @property
    def bind_role_names(self):
        r"""Gets the bind_role_names of this UpdateAgencyPolicyRequestBody.

        委托绑定的权限策略集合。

        :return: The bind_role_names of this UpdateAgencyPolicyRequestBody.
        :rtype: list[str]
        """
        return self._bind_role_names

    @bind_role_names.setter
    def bind_role_names(self, bind_role_names):
        r"""Sets the bind_role_names of this UpdateAgencyPolicyRequestBody.

        委托绑定的权限策略集合。

        :param bind_role_names: The bind_role_names of this UpdateAgencyPolicyRequestBody.
        :type bind_role_names: list[str]
        """
        self._bind_role_names = bind_role_names

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
        if not isinstance(other, UpdateAgencyPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
