# coding: utf-8

import pprint
import re

import six





class QualityEnhance:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'normal_enhance': 'str',
        'revive': 'str',
        'sdr_to_hdr': 'str'
    }

    attribute_map = {
        'normal_enhance': 'normal_enhance',
        'revive': 'revive',
        'sdr_to_hdr': 'sdr_to_hdr'
    }

    def __init__(self, normal_enhance=None, revive=None, sdr_to_hdr=None):
        """QualityEnhance - a model defined in huaweicloud sdk"""
        
        

        self._normal_enhance = None
        self._revive = None
        self._sdr_to_hdr = None
        self.discriminator = None

        if normal_enhance is not None:
            self.normal_enhance = normal_enhance
        if revive is not None:
            self.revive = revive
        if sdr_to_hdr is not None:
            self.sdr_to_hdr = sdr_to_hdr

    @property
    def normal_enhance(self):
        """Gets the normal_enhance of this QualityEnhance.

        针对一般质量、无明显问题的普通片源，通过增强、锐化等技术明显提升主观效果。单纯该处理操作前后，分辨率、帧率等参数不发生变化。 可和old_repair、super_resolution、super_framerate、SDRToHDR组合使用。 

        :return: The normal_enhance of this QualityEnhance.
        :rtype: str
        """
        return self._normal_enhance

    @normal_enhance.setter
    def normal_enhance(self, normal_enhance):
        """Sets the normal_enhance of this QualityEnhance.

        针对一般质量、无明显问题的普通片源，通过增强、锐化等技术明显提升主观效果。单纯该处理操作前后，分辨率、帧率等参数不发生变化。 可和old_repair、super_resolution、super_framerate、SDRToHDR组合使用。 

        :param normal_enhance: The normal_enhance of this QualityEnhance.
        :type: str
        """
        self._normal_enhance = normal_enhance

    @property
    def revive(self):
        """Gets the revive of this QualityEnhance.

        针对旧片、老片，画质主观质量比较低的片源，通过降噪、去压缩失真等视频增强技术，提升画质主观效果。 

        :return: The revive of this QualityEnhance.
        :rtype: str
        """
        return self._revive

    @revive.setter
    def revive(self, revive):
        """Sets the revive of this QualityEnhance.

        针对旧片、老片，画质主观质量比较低的片源，通过降噪、去压缩失真等视频增强技术，提升画质主观效果。 

        :param revive: The revive of this QualityEnhance.
        :type: str
        """
        self._revive = revive

    @property
    def sdr_to_hdr(self):
        """Gets the sdr_to_hdr of this QualityEnhance.

        超动态范围，提升视频动态范围，明显提升片源动态范围。单纯该处理操作前后，分辨率、帧率等参数不发生变化，动态范围、色域范围、码率发生变化。 可和normal_ enhance组合使用。 取值范围： - SDRtoHDR10 ：转换模式1，为标准模式 - SDRtoHDRFLAT”：转换模式2，清新模式，基本不改变源片的饱和度，适用于饱和度高的SDR源片转换为HDR 

        :return: The sdr_to_hdr of this QualityEnhance.
        :rtype: str
        """
        return self._sdr_to_hdr

    @sdr_to_hdr.setter
    def sdr_to_hdr(self, sdr_to_hdr):
        """Sets the sdr_to_hdr of this QualityEnhance.

        超动态范围，提升视频动态范围，明显提升片源动态范围。单纯该处理操作前后，分辨率、帧率等参数不发生变化，动态范围、色域范围、码率发生变化。 可和normal_ enhance组合使用。 取值范围： - SDRtoHDR10 ：转换模式1，为标准模式 - SDRtoHDRFLAT”：转换模式2，清新模式，基本不改变源片的饱和度，适用于饱和度高的SDR源片转换为HDR 

        :param sdr_to_hdr: The sdr_to_hdr of this QualityEnhance.
        :type: str
        """
        self._sdr_to_hdr = sdr_to_hdr

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
        if not isinstance(other, QualityEnhance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
