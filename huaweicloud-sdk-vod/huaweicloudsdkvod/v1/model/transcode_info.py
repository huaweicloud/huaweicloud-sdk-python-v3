# coding: utf-8

import pprint
import re

import six





class TranscodeInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_group_name': 'str',
        'output': 'list[Output]',
        'exec_desc': 'str',
        'transcode_status': 'str'
    }

    attribute_map = {
        'template_group_name': 'template_group_name',
        'output': 'output',
        'exec_desc': 'exec_desc',
        'transcode_status': 'transcode_status'
    }

    def __init__(self, template_group_name=None, output=None, exec_desc=None, transcode_status=None):
        """TranscodeInfo - a model defined in huaweicloud sdk"""
        
        

        self._template_group_name = None
        self._output = None
        self._exec_desc = None
        self._transcode_status = None
        self.discriminator = None

        self.template_group_name = template_group_name
        self.output = output
        if exec_desc is not None:
            self.exec_desc = exec_desc
        if transcode_status is not None:
            self.transcode_status = transcode_status

    @property
    def template_group_name(self):
        """Gets the template_group_name of this TranscodeInfo.

        转码模板组名称

        :return: The template_group_name of this TranscodeInfo.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this TranscodeInfo.

        转码模板组名称

        :param template_group_name: The template_group_name of this TranscodeInfo.
        :type: str
        """
        self._template_group_name = template_group_name

    @property
    def output(self):
        """Gets the output of this TranscodeInfo.


        :return: The output of this TranscodeInfo.
        :rtype: list[Output]
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TranscodeInfo.


        :param output: The output of this TranscodeInfo.
        :type: list[Output]
        """
        self._output = output

    @property
    def exec_desc(self):
        """Gets the exec_desc of this TranscodeInfo.


        :return: The exec_desc of this TranscodeInfo.
        :rtype: str
        """
        return self._exec_desc

    @exec_desc.setter
    def exec_desc(self, exec_desc):
        """Sets the exec_desc of this TranscodeInfo.


        :param exec_desc: The exec_desc of this TranscodeInfo.
        :type: str
        """
        self._exec_desc = exec_desc

    @property
    def transcode_status(self):
        """Gets the transcode_status of this TranscodeInfo.


        :return: The transcode_status of this TranscodeInfo.
        :rtype: str
        """
        return self._transcode_status

    @transcode_status.setter
    def transcode_status(self, transcode_status):
        """Sets the transcode_status of this TranscodeInfo.


        :param transcode_status: The transcode_status of this TranscodeInfo.
        :type: str
        """
        self._transcode_status = transcode_status

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
        if not isinstance(other, TranscodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
