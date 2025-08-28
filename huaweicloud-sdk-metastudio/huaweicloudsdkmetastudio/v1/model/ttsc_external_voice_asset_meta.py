# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtscExternalVoiceAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'mobvoi_voice_meta': 'TtscMobvoiVoiceAssetMeta',
        'audiox_voice_meta': 'TtscAudioxVoiceAssetMeta'
    }

    attribute_map = {
        'provider': 'provider',
        'mobvoi_voice_meta': 'mobvoi_voice_meta',
        'audiox_voice_meta': 'audiox_voice_meta'
    }

    def __init__(self, provider=None, mobvoi_voice_meta=None, audiox_voice_meta=None):
        r"""TtscExternalVoiceAssetMeta

        The model defined in huaweicloud sdk

        :param provider: 第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS
        :type provider: str
        :param mobvoi_voice_meta: 
        :type mobvoi_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscMobvoiVoiceAssetMeta`
        :param audiox_voice_meta: 
        :type audiox_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscAudioxVoiceAssetMeta`
        """
        
        

        self._provider = None
        self._mobvoi_voice_meta = None
        self._audiox_voice_meta = None
        self.discriminator = None

        self.provider = provider
        if mobvoi_voice_meta is not None:
            self.mobvoi_voice_meta = mobvoi_voice_meta
        if audiox_voice_meta is not None:
            self.audiox_voice_meta = audiox_voice_meta

    @property
    def provider(self):
        r"""Gets the provider of this TtscExternalVoiceAssetMeta.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS

        :return: The provider of this TtscExternalVoiceAssetMeta.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this TtscExternalVoiceAssetMeta.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS

        :param provider: The provider of this TtscExternalVoiceAssetMeta.
        :type provider: str
        """
        self._provider = provider

    @property
    def mobvoi_voice_meta(self):
        r"""Gets the mobvoi_voice_meta of this TtscExternalVoiceAssetMeta.

        :return: The mobvoi_voice_meta of this TtscExternalVoiceAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TtscMobvoiVoiceAssetMeta`
        """
        return self._mobvoi_voice_meta

    @mobvoi_voice_meta.setter
    def mobvoi_voice_meta(self, mobvoi_voice_meta):
        r"""Sets the mobvoi_voice_meta of this TtscExternalVoiceAssetMeta.

        :param mobvoi_voice_meta: The mobvoi_voice_meta of this TtscExternalVoiceAssetMeta.
        :type mobvoi_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscMobvoiVoiceAssetMeta`
        """
        self._mobvoi_voice_meta = mobvoi_voice_meta

    @property
    def audiox_voice_meta(self):
        r"""Gets the audiox_voice_meta of this TtscExternalVoiceAssetMeta.

        :return: The audiox_voice_meta of this TtscExternalVoiceAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TtscAudioxVoiceAssetMeta`
        """
        return self._audiox_voice_meta

    @audiox_voice_meta.setter
    def audiox_voice_meta(self, audiox_voice_meta):
        r"""Sets the audiox_voice_meta of this TtscExternalVoiceAssetMeta.

        :param audiox_voice_meta: The audiox_voice_meta of this TtscExternalVoiceAssetMeta.
        :type audiox_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscAudioxVoiceAssetMeta`
        """
        self._audiox_voice_meta = audiox_voice_meta

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
        if not isinstance(other, TtscExternalVoiceAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
