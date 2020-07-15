# coding: utf-8

import pprint
import re

import six





class NovaCreateServersRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server': 'NovaCreateServersOption',
        'osscheduler_hints': 'NovaCreateServersSchedulerHint'
    }

    attribute_map = {
        'server': 'server',
        'osscheduler_hints': 'os:scheduler_hints'
    }

    def __init__(self, server=None, osscheduler_hints=None):
        """NovaCreateServersRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._server = None
        self._osscheduler_hints = None
        self.discriminator = None

        self.server = server
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints

    @property
    def server(self):
        """Gets the server of this NovaCreateServersRequestBody.


        :return: The server of this NovaCreateServersRequestBody.
        :rtype: NovaCreateServersOption
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this NovaCreateServersRequestBody.


        :param server: The server of this NovaCreateServersRequestBody.
        :type: NovaCreateServersOption
        """
        self._server = server

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this NovaCreateServersRequestBody.


        :return: The osscheduler_hints of this NovaCreateServersRequestBody.
        :rtype: NovaCreateServersSchedulerHint
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this NovaCreateServersRequestBody.


        :param osscheduler_hints: The osscheduler_hints of this NovaCreateServersRequestBody.
        :type: NovaCreateServersSchedulerHint
        """
        self._osscheduler_hints = osscheduler_hints

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
        if not isinstance(other, NovaCreateServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
