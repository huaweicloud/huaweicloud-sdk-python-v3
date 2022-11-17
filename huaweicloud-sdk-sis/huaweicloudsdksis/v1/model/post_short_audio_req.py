# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostShortAudioReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'Config',
        'data': 'str'
    }

    attribute_map = {
        'config': 'config',
        'data': 'data'
    }

    def __init__(self, config=None, data=None):
        """PostShortAudioReq

        The model defined in huaweicloud sdk

        :param config: 
        :type config: :class:`huaweicloudsdksis.v1.Config`
        :param data: 语音数据，base64编码，要求base64编码后大小不超过4M，音频时长不超过1分钟。
        :type data: str
        """
        
        

        self._config = None
        self._data = None
        self.discriminator = None

        self.config = config
        self.data = data

    @property
    def config(self):
        """Gets the config of this PostShortAudioReq.

        :return: The config of this PostShortAudioReq.
        :rtype: :class:`huaweicloudsdksis.v1.Config`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PostShortAudioReq.

        :param config: The config of this PostShortAudioReq.
        :type config: :class:`huaweicloudsdksis.v1.Config`
        """
        self._config = config

    @property
    def data(self):
        """Gets the data of this PostShortAudioReq.

        语音数据，base64编码，要求base64编码后大小不超过4M，音频时长不超过1分钟。

        :return: The data of this PostShortAudioReq.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PostShortAudioReq.

        语音数据，base64编码，要求base64编码后大小不超过4M，音频时长不超过1分钟。

        :param data: The data of this PostShortAudioReq.
        :type data: str
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
        if not isinstance(other, PostShortAudioReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
