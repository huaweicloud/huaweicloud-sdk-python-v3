# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'gop': 'int',
        'bitrate_adaptive': 'str',
        'i_frame_policy': 'str'
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
        'gop': 'gop',
        'bitrate_adaptive': 'bitrate_adaptive',
        'i_frame_policy': 'i_frame_policy'
    }

    def __init__(self, template_name=None, quality=None, pvc=None, hdlb=None, codec=None, width=None, height=None, bitrate=None, video_frame_rate=None, protocol=None, i_frame_interval=None, gop=None, bitrate_adaptive=None, i_frame_policy=None):
        """QualityInfo

        The model defined in huaweicloud sdk

        :param template_name: 自定义模板名称。 - 若需要自定义模板名称，请将quality参数设置为userdefine； - 多个自定义模板名称之间不能重复； - 自定义模板名称不能与其他模板的quality参数重复； - 若quality不为userdefine，请勿填写此字段。 
        :type template_name: str
        :param quality: 包含如下取值： - lud： 超高清，系统缺省名称； - lhd： 高清，系统缺省名称； - lsd： 标清，系统缺省名称； - lld： 流畅，系统缺省名称； - userdefine： 视频质量自定义。填写userdefine时，templateName字段不能为空。 
        :type quality: str
        :param pvc: 是否使用窄带高清转码。默认值：off。  注意：该字段已不再维护，建议使用hdlb。  包含如下取值： - off：不启用。 - on：启用。 
        :type pvc: str
        :param hdlb: 是否启用高清低码，较PVC相比画质增强。默认值：off。  提示：使用hdlb字段开启高清低码时，PVC字段不生效。  包含如下取值： - off：不开启高清低码； - on：开启高清低码。 
        :type hdlb: str
        :param codec: 视频编码格式。默认为H264。 - H264：使用H.264。 - H265：使用H.265。 
        :type codec: str
        :param width: 视频长边（横屏的宽，竖屏的高）  单位：像素；默认值：0 - H264 建议取值范围：32-3840，必须为2的倍数 。 - H265 建议取值范围：320-3840 ，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 
        :type width: int
        :param height: 视频短边（横屏的高，竖屏的宽）  单位：像素；默认值：0 - H264 建议取值范围：32-2160，必须为2的倍数。 - H265 建议取值范围：240-2160，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 
        :type height: int
        :param bitrate: 转码视频的码率  单位：Kbps  取值范围：40-30000 
        :type bitrate: int
        :param video_frame_rate: 转码视频帧率  单位：fps  默认值：0  取值范围：0-60，0表示保持帧率不变。 
        :type video_frame_rate: int
        :param protocol: 转码输出支持的协议类型。默认为RTMP。当前只支持RTMP。  包含如下取值： - RTMP 
        :type protocol: str
        :param i_frame_interval: 最大I帧间隔  单位：帧数  取值范围：[0, 500]，默认值：50  注意：若希望通过iFrameInterval设置i帧间隔，请将gop设为0，或不传gop参数。 
        :type i_frame_interval: int
        :param gop: 按时间设置I帧间隔  单位：秒  取值范围：[0,10]，默认值：2  注意：gop不为0时，则以gop设置i帧间隔，iFrameInterval字段不生效。 
        :type gop: int
        :param bitrate_adaptive: 自适应码率参数，默认值：off。  包含如下取值： - off：关闭码率自适应，目标码率按设定的码率输出； - minimum：目标码率按设定码率和源文件码率最小值输出（即码率不上扬）； - adaptive：目标码率按源文件码率自适应输出。 
        :type bitrate_adaptive: str
        :param i_frame_policy: 编码输出I帧策略，默认值：auto。  包含如下取值： - auto：I帧按设置的gop时长输出； - strictSync：编码输出I帧完全和源保持一致（源是I帧则编码输出I帧，源不是I帧则编码非I帧），设置该参数后gop时长设置无效。 
        :type i_frame_policy: str
        """
        
        

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
        self._bitrate_adaptive = None
        self._i_frame_policy = None
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
        if width is not None:
            self.width = width
        if height is not None:
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
        if bitrate_adaptive is not None:
            self.bitrate_adaptive = bitrate_adaptive
        if i_frame_policy is not None:
            self.i_frame_policy = i_frame_policy

    @property
    def template_name(self):
        """Gets the template_name of this QualityInfo.

        自定义模板名称。 - 若需要自定义模板名称，请将quality参数设置为userdefine； - 多个自定义模板名称之间不能重复； - 自定义模板名称不能与其他模板的quality参数重复； - 若quality不为userdefine，请勿填写此字段。 

        :return: The template_name of this QualityInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this QualityInfo.

        自定义模板名称。 - 若需要自定义模板名称，请将quality参数设置为userdefine； - 多个自定义模板名称之间不能重复； - 自定义模板名称不能与其他模板的quality参数重复； - 若quality不为userdefine，请勿填写此字段。 

        :param template_name: The template_name of this QualityInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def quality(self):
        """Gets the quality of this QualityInfo.

        包含如下取值： - lud： 超高清，系统缺省名称； - lhd： 高清，系统缺省名称； - lsd： 标清，系统缺省名称； - lld： 流畅，系统缺省名称； - userdefine： 视频质量自定义。填写userdefine时，templateName字段不能为空。 

        :return: The quality of this QualityInfo.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this QualityInfo.

        包含如下取值： - lud： 超高清，系统缺省名称； - lhd： 高清，系统缺省名称； - lsd： 标清，系统缺省名称； - lld： 流畅，系统缺省名称； - userdefine： 视频质量自定义。填写userdefine时，templateName字段不能为空。 

        :param quality: The quality of this QualityInfo.
        :type quality: str
        """
        self._quality = quality

    @property
    def pvc(self):
        """Gets the pvc of this QualityInfo.

        是否使用窄带高清转码。默认值：off。  注意：该字段已不再维护，建议使用hdlb。  包含如下取值： - off：不启用。 - on：启用。 

        :return: The pvc of this QualityInfo.
        :rtype: str
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this QualityInfo.

        是否使用窄带高清转码。默认值：off。  注意：该字段已不再维护，建议使用hdlb。  包含如下取值： - off：不启用。 - on：启用。 

        :param pvc: The pvc of this QualityInfo.
        :type pvc: str
        """
        self._pvc = pvc

    @property
    def hdlb(self):
        """Gets the hdlb of this QualityInfo.

        是否启用高清低码，较PVC相比画质增强。默认值：off。  提示：使用hdlb字段开启高清低码时，PVC字段不生效。  包含如下取值： - off：不开启高清低码； - on：开启高清低码。 

        :return: The hdlb of this QualityInfo.
        :rtype: str
        """
        return self._hdlb

    @hdlb.setter
    def hdlb(self, hdlb):
        """Sets the hdlb of this QualityInfo.

        是否启用高清低码，较PVC相比画质增强。默认值：off。  提示：使用hdlb字段开启高清低码时，PVC字段不生效。  包含如下取值： - off：不开启高清低码； - on：开启高清低码。 

        :param hdlb: The hdlb of this QualityInfo.
        :type hdlb: str
        """
        self._hdlb = hdlb

    @property
    def codec(self):
        """Gets the codec of this QualityInfo.

        视频编码格式。默认为H264。 - H264：使用H.264。 - H265：使用H.265。 

        :return: The codec of this QualityInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this QualityInfo.

        视频编码格式。默认为H264。 - H264：使用H.264。 - H265：使用H.265。 

        :param codec: The codec of this QualityInfo.
        :type codec: str
        """
        self._codec = codec

    @property
    def width(self):
        """Gets the width of this QualityInfo.

        视频长边（横屏的宽，竖屏的高）  单位：像素；默认值：0 - H264 建议取值范围：32-3840，必须为2的倍数 。 - H265 建议取值范围：320-3840 ，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 

        :return: The width of this QualityInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this QualityInfo.

        视频长边（横屏的宽，竖屏的高）  单位：像素；默认值：0 - H264 建议取值范围：32-3840，必须为2的倍数 。 - H265 建议取值范围：320-3840 ，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 

        :param width: The width of this QualityInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this QualityInfo.

        视频短边（横屏的高，竖屏的宽）  单位：像素；默认值：0 - H264 建议取值范围：32-2160，必须为2的倍数。 - H265 建议取值范围：240-2160，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 

        :return: The height of this QualityInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this QualityInfo.

        视频短边（横屏的高，竖屏的宽）  单位：像素；默认值：0 - H264 建议取值范围：32-2160，必须为2的倍数。 - H265 建议取值范围：240-2160，必须为2的倍数。  注意：width和height全为0，则输出分辨率和源一致；width和height只有一个为0， 则分辨率按非0项的比例缩放。 

        :param height: The height of this QualityInfo.
        :type height: int
        """
        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this QualityInfo.

        转码视频的码率  单位：Kbps  取值范围：40-30000 

        :return: The bitrate of this QualityInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this QualityInfo.

        转码视频的码率  单位：Kbps  取值范围：40-30000 

        :param bitrate: The bitrate of this QualityInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def video_frame_rate(self):
        """Gets the video_frame_rate of this QualityInfo.

        转码视频帧率  单位：fps  默认值：0  取值范围：0-60，0表示保持帧率不变。 

        :return: The video_frame_rate of this QualityInfo.
        :rtype: int
        """
        return self._video_frame_rate

    @video_frame_rate.setter
    def video_frame_rate(self, video_frame_rate):
        """Sets the video_frame_rate of this QualityInfo.

        转码视频帧率  单位：fps  默认值：0  取值范围：0-60，0表示保持帧率不变。 

        :param video_frame_rate: The video_frame_rate of this QualityInfo.
        :type video_frame_rate: int
        """
        self._video_frame_rate = video_frame_rate

    @property
    def protocol(self):
        """Gets the protocol of this QualityInfo.

        转码输出支持的协议类型。默认为RTMP。当前只支持RTMP。  包含如下取值： - RTMP 

        :return: The protocol of this QualityInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this QualityInfo.

        转码输出支持的协议类型。默认为RTMP。当前只支持RTMP。  包含如下取值： - RTMP 

        :param protocol: The protocol of this QualityInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def i_frame_interval(self):
        """Gets the i_frame_interval of this QualityInfo.

        最大I帧间隔  单位：帧数  取值范围：[0, 500]，默认值：50  注意：若希望通过iFrameInterval设置i帧间隔，请将gop设为0，或不传gop参数。 

        :return: The i_frame_interval of this QualityInfo.
        :rtype: int
        """
        return self._i_frame_interval

    @i_frame_interval.setter
    def i_frame_interval(self, i_frame_interval):
        """Sets the i_frame_interval of this QualityInfo.

        最大I帧间隔  单位：帧数  取值范围：[0, 500]，默认值：50  注意：若希望通过iFrameInterval设置i帧间隔，请将gop设为0，或不传gop参数。 

        :param i_frame_interval: The i_frame_interval of this QualityInfo.
        :type i_frame_interval: int
        """
        self._i_frame_interval = i_frame_interval

    @property
    def gop(self):
        """Gets the gop of this QualityInfo.

        按时间设置I帧间隔  单位：秒  取值范围：[0,10]，默认值：2  注意：gop不为0时，则以gop设置i帧间隔，iFrameInterval字段不生效。 

        :return: The gop of this QualityInfo.
        :rtype: int
        """
        return self._gop

    @gop.setter
    def gop(self, gop):
        """Sets the gop of this QualityInfo.

        按时间设置I帧间隔  单位：秒  取值范围：[0,10]，默认值：2  注意：gop不为0时，则以gop设置i帧间隔，iFrameInterval字段不生效。 

        :param gop: The gop of this QualityInfo.
        :type gop: int
        """
        self._gop = gop

    @property
    def bitrate_adaptive(self):
        """Gets the bitrate_adaptive of this QualityInfo.

        自适应码率参数，默认值：off。  包含如下取值： - off：关闭码率自适应，目标码率按设定的码率输出； - minimum：目标码率按设定码率和源文件码率最小值输出（即码率不上扬）； - adaptive：目标码率按源文件码率自适应输出。 

        :return: The bitrate_adaptive of this QualityInfo.
        :rtype: str
        """
        return self._bitrate_adaptive

    @bitrate_adaptive.setter
    def bitrate_adaptive(self, bitrate_adaptive):
        """Sets the bitrate_adaptive of this QualityInfo.

        自适应码率参数，默认值：off。  包含如下取值： - off：关闭码率自适应，目标码率按设定的码率输出； - minimum：目标码率按设定码率和源文件码率最小值输出（即码率不上扬）； - adaptive：目标码率按源文件码率自适应输出。 

        :param bitrate_adaptive: The bitrate_adaptive of this QualityInfo.
        :type bitrate_adaptive: str
        """
        self._bitrate_adaptive = bitrate_adaptive

    @property
    def i_frame_policy(self):
        """Gets the i_frame_policy of this QualityInfo.

        编码输出I帧策略，默认值：auto。  包含如下取值： - auto：I帧按设置的gop时长输出； - strictSync：编码输出I帧完全和源保持一致（源是I帧则编码输出I帧，源不是I帧则编码非I帧），设置该参数后gop时长设置无效。 

        :return: The i_frame_policy of this QualityInfo.
        :rtype: str
        """
        return self._i_frame_policy

    @i_frame_policy.setter
    def i_frame_policy(self, i_frame_policy):
        """Sets the i_frame_policy of this QualityInfo.

        编码输出I帧策略，默认值：auto。  包含如下取值： - auto：I帧按设置的gop时长输出； - strictSync：编码输出I帧完全和源保持一致（源是I帧则编码输出I帧，源不是I帧则编码非I帧），设置该参数后gop时长设置无效。 

        :param i_frame_policy: The i_frame_policy of this QualityInfo.
        :type i_frame_policy: str
        """
        self._i_frame_policy = i_frame_policy

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
        if not isinstance(other, QualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
