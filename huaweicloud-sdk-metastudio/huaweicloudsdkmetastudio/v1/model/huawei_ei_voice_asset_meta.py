# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HuaweiEIVoiceAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_property': 'str',
        'is_cloned_voice': 'bool',
        'training_job_id': 'str'
    }

    attribute_map = {
        '_property': 'property',
        'is_cloned_voice': 'is_cloned_voice',
        'training_job_id': 'training_job_id'
    }

    def __init__(self, _property=None, is_cloned_voice=None, training_job_id=None):
        """HuaweiEIVoiceAssetMeta

        The model defined in huaweicloud sdk

        :param _property: 音色属性。
        :type _property: str
        :param is_cloned_voice: 是否是克隆音色，默认是false。
        :type is_cloned_voice: bool
        :param training_job_id: 音色克隆时的训练任务ID。当is_cloned_voice&#x3D;true时需要填写。
        :type training_job_id: str
        """
        
        

        self.__property = None
        self._is_cloned_voice = None
        self._training_job_id = None
        self.discriminator = None

        self._property = _property
        if is_cloned_voice is not None:
            self.is_cloned_voice = is_cloned_voice
        if training_job_id is not None:
            self.training_job_id = training_job_id

    @property
    def _property(self):
        """Gets the _property of this HuaweiEIVoiceAssetMeta.

        音色属性。

        :return: The _property of this HuaweiEIVoiceAssetMeta.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this HuaweiEIVoiceAssetMeta.

        音色属性。

        :param _property: The _property of this HuaweiEIVoiceAssetMeta.
        :type _property: str
        """
        self.__property = _property

    @property
    def is_cloned_voice(self):
        """Gets the is_cloned_voice of this HuaweiEIVoiceAssetMeta.

        是否是克隆音色，默认是false。

        :return: The is_cloned_voice of this HuaweiEIVoiceAssetMeta.
        :rtype: bool
        """
        return self._is_cloned_voice

    @is_cloned_voice.setter
    def is_cloned_voice(self, is_cloned_voice):
        """Sets the is_cloned_voice of this HuaweiEIVoiceAssetMeta.

        是否是克隆音色，默认是false。

        :param is_cloned_voice: The is_cloned_voice of this HuaweiEIVoiceAssetMeta.
        :type is_cloned_voice: bool
        """
        self._is_cloned_voice = is_cloned_voice

    @property
    def training_job_id(self):
        """Gets the training_job_id of this HuaweiEIVoiceAssetMeta.

        音色克隆时的训练任务ID。当is_cloned_voice=true时需要填写。

        :return: The training_job_id of this HuaweiEIVoiceAssetMeta.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        """Sets the training_job_id of this HuaweiEIVoiceAssetMeta.

        音色克隆时的训练任务ID。当is_cloned_voice=true时需要填写。

        :param training_job_id: The training_job_id of this HuaweiEIVoiceAssetMeta.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

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
        if not isinstance(other, HuaweiEIVoiceAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
