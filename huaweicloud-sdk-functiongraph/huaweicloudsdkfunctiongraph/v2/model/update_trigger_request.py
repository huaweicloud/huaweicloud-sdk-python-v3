# coding: utf-8

import pprint
import re

import six





class UpdateTriggerRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'trigger_type_code': 'str',
        'trigger_id': 'str',
        'body': 'UpdateTriggerRequestBody'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'trigger_type_code': 'trigger_type_code',
        'trigger_id': 'triggerId',
        'body': 'body'
    }

    def __init__(self, function_urn=None, trigger_type_code=None, trigger_id=None, body=None):
        """UpdateTriggerRequest - a model defined in huaweicloud sdk"""
        
        

        self._function_urn = None
        self._trigger_type_code = None
        self._trigger_id = None
        self._body = None
        self.discriminator = None

        self.function_urn = function_urn
        self.trigger_type_code = trigger_type_code
        self.trigger_id = trigger_id
        if body is not None:
            self.body = body

    @property
    def function_urn(self):
        """Gets the function_urn of this UpdateTriggerRequest.


        :return: The function_urn of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this UpdateTriggerRequest.


        :param function_urn: The function_urn of this UpdateTriggerRequest.
        :type: str
        """
        self._function_urn = function_urn

    @property
    def trigger_type_code(self):
        """Gets the trigger_type_code of this UpdateTriggerRequest.


        :return: The trigger_type_code of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._trigger_type_code

    @trigger_type_code.setter
    def trigger_type_code(self, trigger_type_code):
        """Sets the trigger_type_code of this UpdateTriggerRequest.


        :param trigger_type_code: The trigger_type_code of this UpdateTriggerRequest.
        :type: str
        """
        self._trigger_type_code = trigger_type_code

    @property
    def trigger_id(self):
        """Gets the trigger_id of this UpdateTriggerRequest.


        :return: The trigger_id of this UpdateTriggerRequest.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this UpdateTriggerRequest.


        :param trigger_id: The trigger_id of this UpdateTriggerRequest.
        :type: str
        """
        self._trigger_id = trigger_id

    @property
    def body(self):
        """Gets the body of this UpdateTriggerRequest.


        :return: The body of this UpdateTriggerRequest.
        :rtype: UpdateTriggerRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTriggerRequest.


        :param body: The body of this UpdateTriggerRequest.
        :type: UpdateTriggerRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateTriggerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
