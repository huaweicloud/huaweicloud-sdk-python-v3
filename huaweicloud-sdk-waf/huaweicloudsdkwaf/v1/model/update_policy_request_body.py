# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'action': 'PolicyAction',
        'options': 'PolicyOption'
    }

    attribute_map = {
        'name': 'name',
        'action': 'action',
        'options': 'options'
    }

    def __init__(self, name=None, action=None, options=None):
        """UpdatePolicyRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._action = None
        self._options = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if options is not None:
            self.options = options

    @property
    def name(self):
        """Gets the name of this UpdatePolicyRequestBody.

        防护策略名

        :return: The name of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePolicyRequestBody.

        防护策略名

        :param name: The name of this UpdatePolicyRequestBody.
        :type: str
        """
        self._name = name

    @property
    def action(self):
        """Gets the action of this UpdatePolicyRequestBody.


        :return: The action of this UpdatePolicyRequestBody.
        :rtype: PolicyAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdatePolicyRequestBody.


        :param action: The action of this UpdatePolicyRequestBody.
        :type: PolicyAction
        """
        self._action = action

    @property
    def options(self):
        """Gets the options of this UpdatePolicyRequestBody.


        :return: The options of this UpdatePolicyRequestBody.
        :rtype: PolicyOption
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this UpdatePolicyRequestBody.


        :param options: The options of this UpdatePolicyRequestBody.
        :type: PolicyOption
        """
        self._options = options

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
        if not isinstance(other, UpdatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
