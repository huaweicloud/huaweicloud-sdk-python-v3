# coding: utf-8

import re
import six





class UpdatePoolRequestBody:


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
        'description': 'str',
        'option': 'PremiumWafPoolOption'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'option': 'option'
    }

    def __init__(self, name=None, description=None, option=None):
        """UpdatePoolRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._option = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if option is not None:
            self.option = option

    @property
    def name(self):
        """Gets the name of this UpdatePoolRequestBody.

        WAF独享引擎组名称

        :return: The name of this UpdatePoolRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePoolRequestBody.

        WAF独享引擎组名称

        :param name: The name of this UpdatePoolRequestBody.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdatePoolRequestBody.

        注释

        :return: The description of this UpdatePoolRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePoolRequestBody.

        注释

        :param description: The description of this UpdatePoolRequestBody.
        :type: str
        """
        self._description = description

    @property
    def option(self):
        """Gets the option of this UpdatePoolRequestBody.


        :return: The option of this UpdatePoolRequestBody.
        :rtype: PremiumWafPoolOption
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this UpdatePoolRequestBody.


        :param option: The option of this UpdatePoolRequestBody.
        :type: PremiumWafPoolOption
        """
        self._option = option

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
        if not isinstance(other, UpdatePoolRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
