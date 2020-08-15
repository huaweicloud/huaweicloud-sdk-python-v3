# coding: utf-8

import pprint
import re

import six





class NotifyTemplate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'template_content': 'str',
        'protocol': 'str',
        'event': 'int'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_content': 'template_content',
        'protocol': 'protocol',
        'event': 'event'
    }

    def __init__(self, template_name=None, template_content=None, protocol=None, event=None):
        """NotifyTemplate - a model defined in huaweicloud sdk"""
        
        

        self._template_name = None
        self._template_content = None
        self._protocol = None
        self._event = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if template_content is not None:
            self.template_content = template_content
        if protocol is not None:
            self.protocol = protocol
        if event is not None:
            self.event = event

    @property
    def template_name(self):
        """Gets the template_name of this NotifyTemplate.

        模板名称

        :return: The template_name of this NotifyTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this NotifyTemplate.

        模板名称

        :param template_name: The template_name of this NotifyTemplate.
        :type: str
        """
        self._template_name = template_name

    @property
    def template_content(self):
        """Gets the template_content of this NotifyTemplate.

        模板内容

        :return: The template_content of this NotifyTemplate.
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        """Sets the template_content of this NotifyTemplate.

        模板内容

        :param template_content: The template_content of this NotifyTemplate.
        :type: str
        """
        self._template_content = template_content

    @property
    def protocol(self):
        """Gets the protocol of this NotifyTemplate.

        协议名称

        :return: The protocol of this NotifyTemplate.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NotifyTemplate.

        协议名称

        :param protocol: The protocol of this NotifyTemplate.
        :type: str
        """
        self._protocol = protocol

    @property
    def event(self):
        """Gets the event of this NotifyTemplate.

        通知消息的事件类型。当前固定为0, 0表示转码完成事件。 

        :return: The event of this NotifyTemplate.
        :rtype: int
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this NotifyTemplate.

        通知消息的事件类型。当前固定为0, 0表示转码完成事件。 

        :param event: The event of this NotifyTemplate.
        :type: int
        """
        self._event = event

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
        if not isinstance(other, NotifyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
