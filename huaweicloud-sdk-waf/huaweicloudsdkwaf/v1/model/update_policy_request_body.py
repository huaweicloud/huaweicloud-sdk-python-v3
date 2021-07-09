# coding: utf-8

import re
import six





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
        'options': 'PolicyOption',
        'level': 'int',
        'full_detection': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'action': 'action',
        'options': 'options',
        'level': 'level',
        'full_detection': 'full_detection'
    }

    def __init__(self, name=None, action=None, options=None, level=None, full_detection=None):
        """UpdatePolicyRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._action = None
        self._options = None
        self._level = None
        self._full_detection = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if options is not None:
            self.options = options
        if level is not None:
            self.level = level
        if full_detection is not None:
            self.full_detection = full_detection

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

    @property
    def level(self):
        """Gets the level of this UpdatePolicyRequestBody.

        防护等级

        :return: The level of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdatePolicyRequestBody.

        防护等级

        :param level: The level of this UpdatePolicyRequestBody.
        :type: int
        """
        self._level = level

    @property
    def full_detection(self):
        """Gets the full_detection of this UpdatePolicyRequestBody.

        精准防护中的检测模式

        :return: The full_detection of this UpdatePolicyRequestBody.
        :rtype: bool
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        """Sets the full_detection of this UpdatePolicyRequestBody.

        精准防护中的检测模式

        :param full_detection: The full_detection of this UpdatePolicyRequestBody.
        :type: bool
        """
        self._full_detection = full_detection

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
