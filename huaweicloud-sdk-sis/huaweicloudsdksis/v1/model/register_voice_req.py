# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterVoiceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'RegisterVoiceReqConfig',
        'data': 'str'
    }

    attribute_map = {
        'config': 'config',
        'data': 'data'
    }

    def __init__(self, config=None, data=None):
        r"""RegisterVoiceReq

        The model defined in huaweicloud sdk

        :param config: 
        :type config: :class:`huaweicloudsdksis.v1.RegisterVoiceReqConfig`
        :param data: 录音数据，使用base64编码，大小不超过6MB。支持wav、mp3、m4a格式，采样率不小于16kHz，时长在5-25秒，支持单、双通道。
        :type data: str
        """
        
        

        self._config = None
        self._data = None
        self.discriminator = None

        self.config = config
        self.data = data

    @property
    def config(self):
        r"""Gets the config of this RegisterVoiceReq.

        :return: The config of this RegisterVoiceReq.
        :rtype: :class:`huaweicloudsdksis.v1.RegisterVoiceReqConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this RegisterVoiceReq.

        :param config: The config of this RegisterVoiceReq.
        :type config: :class:`huaweicloudsdksis.v1.RegisterVoiceReqConfig`
        """
        self._config = config

    @property
    def data(self):
        r"""Gets the data of this RegisterVoiceReq.

        录音数据，使用base64编码，大小不超过6MB。支持wav、mp3、m4a格式，采样率不小于16kHz，时长在5-25秒，支持单、双通道。

        :return: The data of this RegisterVoiceReq.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this RegisterVoiceReq.

        录音数据，使用base64编码，大小不超过6MB。支持wav、mp3、m4a格式，采样率不小于16kHz，时长在5-25秒，支持单、双通道。

        :param data: The data of this RegisterVoiceReq.
        :type data: str
        """
        self._data = data

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegisterVoiceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
