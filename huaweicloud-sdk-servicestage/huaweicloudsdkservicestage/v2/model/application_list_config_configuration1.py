# coding: utf-8

import pprint
import re

import six





class ApplicationListConfigConfiguration1:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'environment_id': 'str',
        'configuration': 'ApplicationListConfigConfiguration'
    }

    attribute_map = {
        'application_id': 'application_id',
        'environment_id': 'environment_id',
        'configuration': 'configuration'
    }

    def __init__(self, application_id=None, environment_id=None, configuration=None):
        """ApplicationListConfigConfiguration1 - a model defined in huaweicloud sdk"""
        
        

        self._application_id = None
        self._environment_id = None
        self._configuration = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if environment_id is not None:
            self.environment_id = environment_id
        if configuration is not None:
            self.configuration = configuration

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationListConfigConfiguration1.

        应用ID。

        :return: The application_id of this ApplicationListConfigConfiguration1.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationListConfigConfiguration1.

        应用ID。

        :param application_id: The application_id of this ApplicationListConfigConfiguration1.
        :type: str
        """
        self._application_id = application_id

    @property
    def environment_id(self):
        """Gets the environment_id of this ApplicationListConfigConfiguration1.

        环境ID。

        :return: The environment_id of this ApplicationListConfigConfiguration1.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ApplicationListConfigConfiguration1.

        环境ID。

        :param environment_id: The environment_id of this ApplicationListConfigConfiguration1.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def configuration(self):
        """Gets the configuration of this ApplicationListConfigConfiguration1.


        :return: The configuration of this ApplicationListConfigConfiguration1.
        :rtype: ApplicationListConfigConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ApplicationListConfigConfiguration1.


        :param configuration: The configuration of this ApplicationListConfigConfiguration1.
        :type: ApplicationListConfigConfiguration
        """
        self._configuration = configuration

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
        if not isinstance(other, ApplicationListConfigConfiguration1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
