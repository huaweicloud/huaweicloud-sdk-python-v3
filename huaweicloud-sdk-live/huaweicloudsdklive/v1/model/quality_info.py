# coding: utf-8

import pprint
import re

import six





class QualityInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'quality': 'str',
        'pvc': 'str',
        'hdlb': 'str',
        'codec': 'str',
        'width': 'int',
        'height': 'int',
        'bitrate': 'int',
        'video_frame_rate': 'int',
        'protocol': 'str',
        'i_frame_interval': 'int',
        'gop': 'int'
    }

    attribute_map = {
        'template_name': 'templateName',
        'quality': 'quality',
        'pvc': 'PVC',
        'hdlb': 'hdlb',
        'codec': 'codec',
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate',
        'video_frame_rate': 'video_frame_rate',
        'protocol': 'protocol',
        'i_frame_interval': 'iFrameInterval',
        'gop': 'gop'
    }

    def __init__(self, template_name=None, quality=None, pvc='on', hdlb='off', codec='H264', width=None, height=None, bitrate=None, video_frame_rate=None, protocol='RTMP', i_frame_interval=None, gop=None):
        """QualityInfo - a model defined in huaweicloud sdk"""
        
        

        self._template_name = None
        self._quality = None
        self._pvc = None
        self._hdlb = None
        self._codec = None
        self._width = None
        self._height = None
        self._bitrate = None
        self._video_frame_rate = None
        self._protocol = None
        self._i_frame_interval = None
        self._gop = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        self.quality = quality
        if pvc is not None:
            self.pvc = pvc
        if hdlb is not None:
            self.hdlb = hdlb
        if codec is not None:
            self.codec = codec
        self.width = width
        self.height = height
        self.bitrate = bitrate
        if video_frame_rate is not None:
            self.video_frame_rate = video_frame_rate
        if protocol is not None:
            self.protocol = protocol
        if i_frame_interval is not None:
            self.i_frame_interval = i_frame_interval
        if gop is not None:
            self.gop = gop

    @property
    def template_name(self):
        """Gets the template_name of this QualityInfo.

        模板名称。

        :return: The template_name of this QualityInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this QualityInfo.

        模板名称。

        :param template_name: The template_name of this QualityInfo.
        :type: str
        """
        self._template_name = template_name

    @property
    def quality(self):
        """Gets the quality of this QualityInfo.

        包含如下取值： - FHD： 超高清，系统缺省名称 - HD： 高清，系统缺省名称 - SD： 标清，系统缺省名称 - LD： 流畅，系统缺省名称 - XXX： 租户自定义名称。用户自定义名称不能与系统缺省名称冲突；多个自定义名称不能重复 

        :return: The quality of this QualityInfo.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this QualityInfo.

        包含如下取值： - FHD： 超高清，系统缺省名称 - HD： 高清，系统缺省名称 - SD： 标清，系统缺省名称 - LD： 流畅，系统缺省名称 - XXX： 租户自定义名称。用户自定义名称不能与系统缺省名称冲突；多个自定义名称不能重复 

        :param quality: The quality of this QualityInfo.
        :type: str
        """
        self._quality = quality

    @property
    def pvc(self):
        """Gets the pvc of this QualityInfo.

        是否使用窄带高清转码，模板组里不同模板的PVC选项必须相同。 - on：启用。 - off：不启用。 默认为off 

        :return: The pvc of this QualityInfo.
        :rtype: str
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this QualityInfo.

        是否使用窄带高清转码，模板组里不同模板的PVC选项必须相同。 - on：启用。 - off：不启用。 默认为off 

        :param pvc: The pvc of this QualityInfo.
        :type: str
        """
        self._pvc = pvc

    @property
    def hdlb(self):
        """Gets the hdlb of this QualityInfo.

        是否启用高清低码，较PVC相比画质增强。 - on：启用。 - off：不启用。 默认为off。 

        :return: The hdlb of this QualityInfo.
        :rtype: str
        """
        return self._hdlb

    @hdlb.setter
    def hdlb(self, hdlb):
        """Sets the hdlb of this QualityInfo.

        是否启用高清低码，较PVC相比画质增强。 - on：启用。 - off：不启用。 默认为off。 

        :param hdlb: The hdlb of this QualityInfo.
        :type: str
        """
        self._hdlb = hdlb

    @property
    def codec(self):
        """Gets the codec of this QualityInfo.

        视频编码格式，模板组里不同模板的编码格式必须相同。 - H264：使用H.264。 - H265：使用H.265。 默认为H264。 

        :return: The codec of this QualityInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this QualityInfo.

        视频编码格式，模板组里不同模板的编码格式必须相同。 - H264：使用H.264。 - H265：使用H.265。 默认为H264。 

        :param codec: The codec of this QualityInfo.
        :type: str
        """
        self._codec = codec

    @property
    def width(self):
        """Gets the width of this QualityInfo.

        视频宽度（单位：像素） - H264   取值范围：32-3840，必须为2的倍数 。 - H265   取值范围：320-3840 ，必须为4的倍数。 

        :return: The width of this QualityInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this QualityInfo.

        视频宽度（单位：像素） - H264   取值范围：32-3840，必须为2的倍数 。 - H265   取值范围：320-3840 ，必须为4的倍数。 

        :param width: The width of this QualityInfo.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this QualityInfo.

        视频高度（单位：像素） - H264   取值范围：32-2160，必须为2的倍数。 - H265   取值范围：240-2160，必须为4的倍数。 

        :return: The height of this QualityInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this QualityInfo.

        视频高度（单位：像素） - H264   取值范围：32-2160，必须为2的倍数。 - H265   取值范围：240-2160，必须为4的倍数。 

        :param height: The height of this QualityInfo.
        :type: int
        """
        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this QualityInfo.

        转码视频的码率（单位：Kbps）。 取值范围：40-30000。 

        :return: The bitrate of this QualityInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this QualityInfo.

        转码视频的码率（单位：Kbps）。 取值范围：40-30000。 

        :param bitrate: The bitrate of this QualityInfo.
        :type: int
        """
        self._bitrate = bitrate

    @property
    def video_frame_rate(self):
        """Gets the video_frame_rate of this QualityInfo.

        转码视频帧率（单位：fps）。 取值范围：0-30，0表示保持帧率不变。 

        :return: The video_frame_rate of this QualityInfo.
        :rtype: int
        """
        return self._video_frame_rate

    @video_frame_rate.setter
    def video_frame_rate(self, video_frame_rate):
        """Sets the video_frame_rate of this QualityInfo.

        转码视频帧率（单位：fps）。 取值范围：0-30，0表示保持帧率不变。 

        :param video_frame_rate: The video_frame_rate of this QualityInfo.
        :type: int
        """
        self._video_frame_rate = video_frame_rate

    @property
    def protocol(self):
        """Gets the protocol of this QualityInfo.

        转码输出支持的协议类型。当前只支持RTMP和HLS，且模板组里不同模板的输出协议类型必须相同。 - RTMP - HLS - DASH  默认为RTMP。 

        :return: The protocol of this QualityInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this QualityInfo.

        转码输出支持的协议类型。当前只支持RTMP和HLS，且模板组里不同模板的输出协议类型必须相同。 - RTMP - HLS - DASH  默认为RTMP。 

        :param protocol: The protocol of this QualityInfo.
        :type: str
        """
        self._protocol = protocol

    @property
    def i_frame_interval(self):
        """Gets the i_frame_interval of this QualityInfo.

        I帧间隔（单位：帧）。  取值范围：0-500。  默认为25。 

        :return: The i_frame_interval of this QualityInfo.
        :rtype: int
        """
        return self._i_frame_interval

    @i_frame_interval.setter
    def i_frame_interval(self, i_frame_interval):
        """Sets the i_frame_interval of this QualityInfo.

        I帧间隔（单位：帧）。  取值范围：0-500。  默认为25。 

        :param i_frame_interval: The i_frame_interval of this QualityInfo.
        :type: int
        """
        self._i_frame_interval = i_frame_interval

    @property
    def gop(self):
        """Gets the gop of this QualityInfo.

        按时间设置I帧间隔，与“iFrameInterval”选择一个设置即可。  取值范围：[0,10]  默认值：4 

        :return: The gop of this QualityInfo.
        :rtype: int
        """
        return self._gop

    @gop.setter
    def gop(self, gop):
        """Sets the gop of this QualityInfo.

        按时间设置I帧间隔，与“iFrameInterval”选择一个设置即可。  取值范围：[0,10]  默认值：4 

        :param gop: The gop of this QualityInfo.
        :type: int
        """
        self._gop = gop

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
        if not isinstance(other, QualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
