# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTemplateSimpleVOStages:

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
        'sequence': 'int'
    }

    attribute_map = {
        'name': 'name',
        'sequence': 'sequence'
    }

    def __init__(self, name=None, sequence=None):
        """PipelineTemplateSimpleVOStages

        The model defined in huaweicloud sdk

        :param name: 阶段名称
        :type name: str
        :param sequence: 序列号
        :type sequence: int
        """
        
        

        self._name = None
        self._sequence = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sequence is not None:
            self.sequence = sequence

    @property
    def name(self):
        """Gets the name of this PipelineTemplateSimpleVOStages.

        阶段名称

        :return: The name of this PipelineTemplateSimpleVOStages.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTemplateSimpleVOStages.

        阶段名称

        :param name: The name of this PipelineTemplateSimpleVOStages.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        """Gets the sequence of this PipelineTemplateSimpleVOStages.

        序列号

        :return: The sequence of this PipelineTemplateSimpleVOStages.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this PipelineTemplateSimpleVOStages.

        序列号

        :param sequence: The sequence of this PipelineTemplateSimpleVOStages.
        :type sequence: int
        """
        self._sequence = sequence

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
        if not isinstance(other, PipelineTemplateSimpleVOStages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
