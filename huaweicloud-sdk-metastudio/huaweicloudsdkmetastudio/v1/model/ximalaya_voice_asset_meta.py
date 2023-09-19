# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class XimalayaVoiceAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'speaker_name': 'str',
        'speaker_variant': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'speaker_name': 'speaker_name',
        'speaker_variant': 'speaker_variant'
    }

    def __init__(self, domain=None, speaker_name=None, speaker_variant=None):
        """XimalayaVoiceAssetMeta

        The model defined in huaweicloud sdk

        :param domain: 音色适用领域。
        :type domain: str
        :param speaker_name: 音色名称。
        :type speaker_name: str
        :param speaker_variant: 音色变声。
        :type speaker_variant: str
        """
        
        

        self._domain = None
        self._speaker_name = None
        self._speaker_variant = None
        self.discriminator = None

        self.domain = domain
        self.speaker_name = speaker_name
        self.speaker_variant = speaker_variant

    @property
    def domain(self):
        """Gets the domain of this XimalayaVoiceAssetMeta.

        音色适用领域。

        :return: The domain of this XimalayaVoiceAssetMeta.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this XimalayaVoiceAssetMeta.

        音色适用领域。

        :param domain: The domain of this XimalayaVoiceAssetMeta.
        :type domain: str
        """
        self._domain = domain

    @property
    def speaker_name(self):
        """Gets the speaker_name of this XimalayaVoiceAssetMeta.

        音色名称。

        :return: The speaker_name of this XimalayaVoiceAssetMeta.
        :rtype: str
        """
        return self._speaker_name

    @speaker_name.setter
    def speaker_name(self, speaker_name):
        """Sets the speaker_name of this XimalayaVoiceAssetMeta.

        音色名称。

        :param speaker_name: The speaker_name of this XimalayaVoiceAssetMeta.
        :type speaker_name: str
        """
        self._speaker_name = speaker_name

    @property
    def speaker_variant(self):
        """Gets the speaker_variant of this XimalayaVoiceAssetMeta.

        音色变声。

        :return: The speaker_variant of this XimalayaVoiceAssetMeta.
        :rtype: str
        """
        return self._speaker_variant

    @speaker_variant.setter
    def speaker_variant(self, speaker_variant):
        """Sets the speaker_variant of this XimalayaVoiceAssetMeta.

        音色变声。

        :param speaker_variant: The speaker_variant of this XimalayaVoiceAssetMeta.
        :type speaker_variant: str
        """
        self._speaker_variant = speaker_variant

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
        if not isinstance(other, XimalayaVoiceAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
