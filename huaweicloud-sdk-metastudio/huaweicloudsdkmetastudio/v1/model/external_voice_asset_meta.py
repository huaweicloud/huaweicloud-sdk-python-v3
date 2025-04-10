# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalVoiceAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str'
    }

    attribute_map = {
        'provider': 'provider'
    }

    def __init__(self, provider=None):
        r"""ExternalVoiceAssetMeta

        The model defined in huaweicloud sdk

        :param provider: 第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：华为云EI TTS * MOBVOI：出门问问 TTS * AUDIOX：逻辑智能 TTS * SINOVOICE：捷通华声 TTS * DATABAKER：标贝 TTS * AISPEECH：思必驰 TTS
        :type provider: str
        """
        
        

        self._provider = None
        self.discriminator = None

        self.provider = provider

    @property
    def provider(self):
        r"""Gets the provider of this ExternalVoiceAssetMeta.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：华为云EI TTS * MOBVOI：出门问问 TTS * AUDIOX：逻辑智能 TTS * SINOVOICE：捷通华声 TTS * DATABAKER：标贝 TTS * AISPEECH：思必驰 TTS

        :return: The provider of this ExternalVoiceAssetMeta.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ExternalVoiceAssetMeta.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：华为云EI TTS * MOBVOI：出门问问 TTS * AUDIOX：逻辑智能 TTS * SINOVOICE：捷通华声 TTS * DATABAKER：标贝 TTS * AISPEECH：思必驰 TTS

        :param provider: The provider of this ExternalVoiceAssetMeta.
        :type provider: str
        """
        self._provider = provider

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
        if not isinstance(other, ExternalVoiceAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
