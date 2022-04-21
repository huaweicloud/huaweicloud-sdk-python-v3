# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MixInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'inputs': 'list[InputSetting]',
        'layout': 'MixInfoLayout'
    }

    attribute_map = {
        'inputs': 'inputs',
        'layout': 'layout'
    }

    def __init__(self, inputs=None, layout=None):
        """MixInfo

        The model defined in huaweicloud sdk

        :param inputs: 合成任务原始视频配置
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.InputSetting`]
        :param layout: 
        :type layout: :class:`huaweicloudsdkmpc.v1.MixInfoLayout`
        """
        
        

        self._inputs = None
        self._layout = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if layout is not None:
            self.layout = layout

    @property
    def inputs(self):
        """Gets the inputs of this MixInfo.

        合成任务原始视频配置

        :return: The inputs of this MixInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.InputSetting`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this MixInfo.

        合成任务原始视频配置

        :param inputs: The inputs of this MixInfo.
        :type inputs: list[:class:`huaweicloudsdkmpc.v1.InputSetting`]
        """
        self._inputs = inputs

    @property
    def layout(self):
        """Gets the layout of this MixInfo.


        :return: The layout of this MixInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.MixInfoLayout`
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this MixInfo.


        :param layout: The layout of this MixInfo.
        :type layout: :class:`huaweicloudsdkmpc.v1.MixInfoLayout`
        """
        self._layout = layout

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
        if not isinstance(other, MixInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
