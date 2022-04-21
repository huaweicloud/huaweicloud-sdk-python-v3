# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityEnhanceVideo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'video_denoise': 'VideoDenoise',
        'video_sharp': 'VideoSharp',
        'video_contrast': 'VideoContrast',
        'video_superresolution': 'VideoSuperresolution',
        'video_deblock': 'VideoDeblock',
        'video_saturation': 'VideoSaturation'
    }

    attribute_map = {
        'video_denoise': 'video_denoise',
        'video_sharp': 'video_sharp',
        'video_contrast': 'video_contrast',
        'video_superresolution': 'video_superresolution',
        'video_deblock': 'video_deblock',
        'video_saturation': 'video_saturation'
    }

    def __init__(self, video_denoise=None, video_sharp=None, video_contrast=None, video_superresolution=None, video_deblock=None, video_saturation=None):
        """QualityEnhanceVideo

        The model defined in huaweicloud sdk

        :param video_denoise: 
        :type video_denoise: :class:`huaweicloudsdkmpc.v1.VideoDenoise`
        :param video_sharp: 
        :type video_sharp: :class:`huaweicloudsdkmpc.v1.VideoSharp`
        :param video_contrast: 
        :type video_contrast: :class:`huaweicloudsdkmpc.v1.VideoContrast`
        :param video_superresolution: 
        :type video_superresolution: :class:`huaweicloudsdkmpc.v1.VideoSuperresolution`
        :param video_deblock: 
        :type video_deblock: :class:`huaweicloudsdkmpc.v1.VideoDeblock`
        :param video_saturation: 
        :type video_saturation: :class:`huaweicloudsdkmpc.v1.VideoSaturation`
        """
        
        

        self._video_denoise = None
        self._video_sharp = None
        self._video_contrast = None
        self._video_superresolution = None
        self._video_deblock = None
        self._video_saturation = None
        self.discriminator = None

        if video_denoise is not None:
            self.video_denoise = video_denoise
        if video_sharp is not None:
            self.video_sharp = video_sharp
        if video_contrast is not None:
            self.video_contrast = video_contrast
        if video_superresolution is not None:
            self.video_superresolution = video_superresolution
        if video_deblock is not None:
            self.video_deblock = video_deblock
        if video_saturation is not None:
            self.video_saturation = video_saturation

    @property
    def video_denoise(self):
        """Gets the video_denoise of this QualityEnhanceVideo.


        :return: The video_denoise of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoDenoise`
        """
        return self._video_denoise

    @video_denoise.setter
    def video_denoise(self, video_denoise):
        """Sets the video_denoise of this QualityEnhanceVideo.


        :param video_denoise: The video_denoise of this QualityEnhanceVideo.
        :type video_denoise: :class:`huaweicloudsdkmpc.v1.VideoDenoise`
        """
        self._video_denoise = video_denoise

    @property
    def video_sharp(self):
        """Gets the video_sharp of this QualityEnhanceVideo.


        :return: The video_sharp of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoSharp`
        """
        return self._video_sharp

    @video_sharp.setter
    def video_sharp(self, video_sharp):
        """Sets the video_sharp of this QualityEnhanceVideo.


        :param video_sharp: The video_sharp of this QualityEnhanceVideo.
        :type video_sharp: :class:`huaweicloudsdkmpc.v1.VideoSharp`
        """
        self._video_sharp = video_sharp

    @property
    def video_contrast(self):
        """Gets the video_contrast of this QualityEnhanceVideo.


        :return: The video_contrast of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoContrast`
        """
        return self._video_contrast

    @video_contrast.setter
    def video_contrast(self, video_contrast):
        """Sets the video_contrast of this QualityEnhanceVideo.


        :param video_contrast: The video_contrast of this QualityEnhanceVideo.
        :type video_contrast: :class:`huaweicloudsdkmpc.v1.VideoContrast`
        """
        self._video_contrast = video_contrast

    @property
    def video_superresolution(self):
        """Gets the video_superresolution of this QualityEnhanceVideo.


        :return: The video_superresolution of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoSuperresolution`
        """
        return self._video_superresolution

    @video_superresolution.setter
    def video_superresolution(self, video_superresolution):
        """Sets the video_superresolution of this QualityEnhanceVideo.


        :param video_superresolution: The video_superresolution of this QualityEnhanceVideo.
        :type video_superresolution: :class:`huaweicloudsdkmpc.v1.VideoSuperresolution`
        """
        self._video_superresolution = video_superresolution

    @property
    def video_deblock(self):
        """Gets the video_deblock of this QualityEnhanceVideo.


        :return: The video_deblock of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoDeblock`
        """
        return self._video_deblock

    @video_deblock.setter
    def video_deblock(self, video_deblock):
        """Sets the video_deblock of this QualityEnhanceVideo.


        :param video_deblock: The video_deblock of this QualityEnhanceVideo.
        :type video_deblock: :class:`huaweicloudsdkmpc.v1.VideoDeblock`
        """
        self._video_deblock = video_deblock

    @property
    def video_saturation(self):
        """Gets the video_saturation of this QualityEnhanceVideo.


        :return: The video_saturation of this QualityEnhanceVideo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoSaturation`
        """
        return self._video_saturation

    @video_saturation.setter
    def video_saturation(self, video_saturation):
        """Sets the video_saturation of this QualityEnhanceVideo.


        :param video_saturation: The video_saturation of this QualityEnhanceVideo.
        :type video_saturation: :class:`huaweicloudsdkmpc.v1.VideoSaturation`
        """
        self._video_saturation = video_saturation

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
        if not isinstance(other, QualityEnhanceVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
