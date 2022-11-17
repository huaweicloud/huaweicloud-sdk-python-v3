# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subtitle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'inputs': 'list[MulInputFileInfo]',
        'subtitle_type': 'int'
    }

    attribute_map = {
        'input': 'input',
        'inputs': 'inputs',
        'subtitle_type': 'subtitle_type'
    }

    def __init__(self, input=None, inputs=None, subtitle_type=None):
        """Subtitle

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param inputs: 多字幕文件地址。 
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.MulInputFileInfo`]
        :param subtitle_type: 字幕类型。取值如下：  - 0，表示不输出字幕 - 1，表示外部字幕文件嵌入视频流 - 2，表示输出WebVTT格式字幕 
        :type subtitle_type: int
        """
        
        

        self._input = None
        self._inputs = None
        self._subtitle_type = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if inputs is not None:
            self.inputs = inputs
        if subtitle_type is not None:
            self.subtitle_type = subtitle_type

    @property
    def input(self):
        """Gets the input of this Subtitle.

        :return: The input of this Subtitle.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Subtitle.

        :param input: The input of this Subtitle.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def inputs(self):
        """Gets the inputs of this Subtitle.

        多字幕文件地址。 

        :return: The inputs of this Subtitle.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.MulInputFileInfo`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Subtitle.

        多字幕文件地址。 

        :param inputs: The inputs of this Subtitle.
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.MulInputFileInfo`]
        """
        self._inputs = inputs

    @property
    def subtitle_type(self):
        """Gets the subtitle_type of this Subtitle.

        字幕类型。取值如下：  - 0，表示不输出字幕 - 1，表示外部字幕文件嵌入视频流 - 2，表示输出WebVTT格式字幕 

        :return: The subtitle_type of this Subtitle.
        :rtype: int
        """
        return self._subtitle_type

    @subtitle_type.setter
    def subtitle_type(self, subtitle_type):
        """Sets the subtitle_type of this Subtitle.

        字幕类型。取值如下：  - 0，表示不输出字幕 - 1，表示外部字幕文件嵌入视频流 - 2，表示输出WebVTT格式字幕 

        :param subtitle_type: The subtitle_type of this Subtitle.
        :type subtitle_type: int
        """
        self._subtitle_type = subtitle_type

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
        if not isinstance(other, Subtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
