# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskStream:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common': 'object',
        'input': 'TaskInput',
        'outputs': 'list[TaskOutputs]'
    }

    attribute_map = {
        'common': 'common',
        'input': 'input',
        'outputs': 'outputs'
    }

    def __init__(self, common=None, input=None, outputs=None):
        """TaskStream

        The model defined in huaweicloud sdk

        :param common: 作业参数配置
        :type common: object
        :param input: 
        :type input: :class:`huaweicloudsdkhilens.v3.TaskInput`
        :param outputs: 输出详情
        :type outputs: list[:class:`huaweicloudsdkhilens.v3.TaskOutputs`]
        """
        
        

        self._common = None
        self._input = None
        self._outputs = None
        self.discriminator = None

        if common is not None:
            self.common = common
        self.input = input
        self.outputs = outputs

    @property
    def common(self):
        """Gets the common of this TaskStream.

        作业参数配置

        :return: The common of this TaskStream.
        :rtype: object
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this TaskStream.

        作业参数配置

        :param common: The common of this TaskStream.
        :type common: object
        """
        self._common = common

    @property
    def input(self):
        """Gets the input of this TaskStream.

        :return: The input of this TaskStream.
        :rtype: :class:`huaweicloudsdkhilens.v3.TaskInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TaskStream.

        :param input: The input of this TaskStream.
        :type input: :class:`huaweicloudsdkhilens.v3.TaskInput`
        """
        self._input = input

    @property
    def outputs(self):
        """Gets the outputs of this TaskStream.

        输出详情

        :return: The outputs of this TaskStream.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TaskOutputs`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TaskStream.

        输出详情

        :param outputs: The outputs of this TaskStream.
        :type outputs: list[:class:`huaweicloudsdkhilens.v3.TaskOutputs`]
        """
        self._outputs = outputs

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
        if not isinstance(other, TaskStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
