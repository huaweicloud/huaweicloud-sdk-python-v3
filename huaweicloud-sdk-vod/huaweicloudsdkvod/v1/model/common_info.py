# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pvc': 'bool',
        'video_codec': 'str',
        'audio_codec': 'str',
        'is_black_cut': 'bool',
        'format': 'str',
        'hls_interval': 'int',
        'upsample': 'bool',
        'adaptation': 'str'
    }

    attribute_map = {
        'pvc': 'pvc',
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'is_black_cut': 'is_black_cut',
        'format': 'format',
        'hls_interval': 'hls_interval',
        'upsample': 'upsample',
        'adaptation': 'adaptation'
    }

    def __init__(self, pvc=None, video_codec=None, audio_codec=None, is_black_cut=None, format=None, hls_interval=None, upsample=None, adaptation=None):
        """CommonInfo

        The model defined in huaweicloud sdk

        :param pvc: pvc开关&lt;br/&gt; 
        :type pvc: bool
        :param video_codec: 视频编码格式&lt;br/&gt; 
        :type video_codec: str
        :param audio_codec: 音频编码格式&lt;br/&gt; AAC：AAC格式 (default)&lt;br/&gt; HEAAC1：HEAAC1格式&lt;br/&gt; HEAAC2：HEAAC2格式&lt;br/&gt; MP3：MP3格式&lt;br/&gt; 
        :type audio_codec: str
        :param is_black_cut: 黑边剪裁类型&lt;br/&gt; 
        :type is_black_cut: bool
        :param format: 格式&lt;br/&gt; 
        :type format: str
        :param hls_interval: 分片时长(默认为5秒)&lt;br/&gt; 
        :type hls_interval: int
        :param upsample: 上采样&lt;br/&gt; 
        :type upsample: bool
        :param adaptation: SHORT：短边自适应&lt;br/&gt; LONG：长边自适应&lt;br/&gt; NONE：宽高自适应&lt;br/&gt; 
        :type adaptation: str
        """
        
        

        self._pvc = None
        self._video_codec = None
        self._audio_codec = None
        self._is_black_cut = None
        self._format = None
        self._hls_interval = None
        self._upsample = None
        self._adaptation = None
        self.discriminator = None

        self.pvc = pvc
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if is_black_cut is not None:
            self.is_black_cut = is_black_cut
        if format is not None:
            self.format = format
        if hls_interval is not None:
            self.hls_interval = hls_interval
        if upsample is not None:
            self.upsample = upsample
        if adaptation is not None:
            self.adaptation = adaptation

    @property
    def pvc(self):
        """Gets the pvc of this CommonInfo.

        pvc开关<br/> 

        :return: The pvc of this CommonInfo.
        :rtype: bool
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this CommonInfo.

        pvc开关<br/> 

        :param pvc: The pvc of this CommonInfo.
        :type pvc: bool
        """
        self._pvc = pvc

    @property
    def video_codec(self):
        """Gets the video_codec of this CommonInfo.

        视频编码格式<br/> 

        :return: The video_codec of this CommonInfo.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this CommonInfo.

        视频编码格式<br/> 

        :param video_codec: The video_codec of this CommonInfo.
        :type video_codec: str
        """
        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this CommonInfo.

        音频编码格式<br/> AAC：AAC格式 (default)<br/> HEAAC1：HEAAC1格式<br/> HEAAC2：HEAAC2格式<br/> MP3：MP3格式<br/> 

        :return: The audio_codec of this CommonInfo.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this CommonInfo.

        音频编码格式<br/> AAC：AAC格式 (default)<br/> HEAAC1：HEAAC1格式<br/> HEAAC2：HEAAC2格式<br/> MP3：MP3格式<br/> 

        :param audio_codec: The audio_codec of this CommonInfo.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def is_black_cut(self):
        """Gets the is_black_cut of this CommonInfo.

        黑边剪裁类型<br/> 

        :return: The is_black_cut of this CommonInfo.
        :rtype: bool
        """
        return self._is_black_cut

    @is_black_cut.setter
    def is_black_cut(self, is_black_cut):
        """Sets the is_black_cut of this CommonInfo.

        黑边剪裁类型<br/> 

        :param is_black_cut: The is_black_cut of this CommonInfo.
        :type is_black_cut: bool
        """
        self._is_black_cut = is_black_cut

    @property
    def format(self):
        """Gets the format of this CommonInfo.

        格式<br/> 

        :return: The format of this CommonInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CommonInfo.

        格式<br/> 

        :param format: The format of this CommonInfo.
        :type format: str
        """
        self._format = format

    @property
    def hls_interval(self):
        """Gets the hls_interval of this CommonInfo.

        分片时长(默认为5秒)<br/> 

        :return: The hls_interval of this CommonInfo.
        :rtype: int
        """
        return self._hls_interval

    @hls_interval.setter
    def hls_interval(self, hls_interval):
        """Sets the hls_interval of this CommonInfo.

        分片时长(默认为5秒)<br/> 

        :param hls_interval: The hls_interval of this CommonInfo.
        :type hls_interval: int
        """
        self._hls_interval = hls_interval

    @property
    def upsample(self):
        """Gets the upsample of this CommonInfo.

        上采样<br/> 

        :return: The upsample of this CommonInfo.
        :rtype: bool
        """
        return self._upsample

    @upsample.setter
    def upsample(self, upsample):
        """Sets the upsample of this CommonInfo.

        上采样<br/> 

        :param upsample: The upsample of this CommonInfo.
        :type upsample: bool
        """
        self._upsample = upsample

    @property
    def adaptation(self):
        """Gets the adaptation of this CommonInfo.

        SHORT：短边自适应<br/> LONG：长边自适应<br/> NONE：宽高自适应<br/> 

        :return: The adaptation of this CommonInfo.
        :rtype: str
        """
        return self._adaptation

    @adaptation.setter
    def adaptation(self, adaptation):
        """Sets the adaptation of this CommonInfo.

        SHORT：短边自适应<br/> LONG：长边自适应<br/> NONE：宽高自适应<br/> 

        :param adaptation: The adaptation of this CommonInfo.
        :type adaptation: str
        """
        self._adaptation = adaptation

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
        if not isinstance(other, CommonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
