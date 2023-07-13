# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAudioJobRequestBodyInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'data': 'list[AudioInputData]'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, type=None, data=None):
        """CreateAudioJobRequestBodyInput

        The model defined in huaweicloud sdk

        :param type: 视频数据的输入类型： - obs：表示从华为云 OBS 中读取视频数据。 - url：表示从指定的 URL 地址中读取视频数据。 
        :type type: str
        :param data: 数据输入内容
        :type data: list[:class:`huaweicloudsdkvcm.v2.AudioInputData`]
        """
        
        

        self._type = None
        self._data = None
        self.discriminator = None

        self.type = type
        self.data = data

    @property
    def type(self):
        """Gets the type of this CreateAudioJobRequestBodyInput.

        视频数据的输入类型： - obs：表示从华为云 OBS 中读取视频数据。 - url：表示从指定的 URL 地址中读取视频数据。 

        :return: The type of this CreateAudioJobRequestBodyInput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAudioJobRequestBodyInput.

        视频数据的输入类型： - obs：表示从华为云 OBS 中读取视频数据。 - url：表示从指定的 URL 地址中读取视频数据。 

        :param type: The type of this CreateAudioJobRequestBodyInput.
        :type type: str
        """
        self._type = type

    @property
    def data(self):
        """Gets the data of this CreateAudioJobRequestBodyInput.

        数据输入内容

        :return: The data of this CreateAudioJobRequestBodyInput.
        :rtype: list[:class:`huaweicloudsdkvcm.v2.AudioInputData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateAudioJobRequestBodyInput.

        数据输入内容

        :param data: The data of this CreateAudioJobRequestBodyInput.
        :type data: list[:class:`huaweicloudsdkvcm.v2.AudioInputData`]
        """
        self._data = data

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
        if not isinstance(other, CreateAudioJobRequestBodyInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
