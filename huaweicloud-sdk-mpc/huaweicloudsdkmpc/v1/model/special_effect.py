# coding: utf-8

import pprint
import re

import six





class SpecialEffect:


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
        'auto_detect': 'str',
        'effect_infos': 'list[EffectInfo]'
    }

    attribute_map = {
        'type': 'type',
        'auto_detect': 'auto_detect',
        'effect_infos': 'effect_infos'
    }

    def __init__(self, type=None, auto_detect=None, effect_infos=None):
        """SpecialEffect - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._auto_detect = None
        self._effect_infos = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if auto_detect is not None:
            self.auto_detect = auto_detect
        if effect_infos is not None:
            self.effect_infos = effect_infos

    @property
    def type(self):
        """Gets the type of this SpecialEffect.

        特效处理类型。取值： Blur（水印模糊化） Mosaic（水印打马赛克，暂不支持） Replace（替换，暂不支持） 

        :return: The type of this SpecialEffect.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpecialEffect.

        特效处理类型。取值： Blur（水印模糊化） Mosaic（水印打马赛克，暂不支持） Replace（替换，暂不支持） 

        :param type: The type of this SpecialEffect.
        :type: str
        """
        self._type = type

    @property
    def auto_detect(self):
        """Gets the auto_detect of this SpecialEffect.

        On：表示自动检测特效处理的参数信息，如水印的时间、位置信息等，无需输入参数信息effectinfos OFF：表示需输入特效处理的相关参数信息effectinfos 

        :return: The auto_detect of this SpecialEffect.
        :rtype: str
        """
        return self._auto_detect

    @auto_detect.setter
    def auto_detect(self, auto_detect):
        """Sets the auto_detect of this SpecialEffect.

        On：表示自动检测特效处理的参数信息，如水印的时间、位置信息等，无需输入参数信息effectinfos OFF：表示需输入特效处理的相关参数信息effectinfos 

        :param auto_detect: The auto_detect of this SpecialEffect.
        :type: str
        """
        self._auto_detect = auto_detect

    @property
    def effect_infos(self):
        """Gets the effect_infos of this SpecialEffect.

        特效处理相关参数，数组 约束：1）每帧视频最多处理2个指定区域；2）每个视频最多处理20个指定区域。 

        :return: The effect_infos of this SpecialEffect.
        :rtype: list[EffectInfo]
        """
        return self._effect_infos

    @effect_infos.setter
    def effect_infos(self, effect_infos):
        """Sets the effect_infos of this SpecialEffect.

        特效处理相关参数，数组 约束：1）每帧视频最多处理2个指定区域；2）每个视频最多处理20个指定区域。 

        :param effect_infos: The effect_infos of this SpecialEffect.
        :type: list[EffectInfo]
        """
        self._effect_infos = effect_infos

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpecialEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
