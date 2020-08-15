# coding: utf-8

import pprint
import re

import six





class MediaDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'features': 'list[str]',
        'origin_para': 'OriginPara',
        'output_video_paras': 'list[OutputVideoPara]',
        'output_thumbnail_para': 'OutputThumbnailPara',
        'output_watermark_paras': 'OutputWatermarkPara'
    }

    attribute_map = {
        'features': 'features',
        'origin_para': 'origin_para',
        'output_video_paras': 'output_video_paras',
        'output_thumbnail_para': 'output_thumbnail_para',
        'output_watermark_paras': 'output_watermark_paras'
    }

    def __init__(self, features=None, origin_para=None, output_video_paras=None, output_thumbnail_para=None, output_watermark_paras=None):
        """MediaDetail - a model defined in huaweicloud sdk"""
        
        

        self._features = None
        self._origin_para = None
        self._output_video_paras = None
        self._output_thumbnail_para = None
        self._output_watermark_paras = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if origin_para is not None:
            self.origin_para = origin_para
        if output_video_paras is not None:
            self.output_video_paras = output_video_paras
        if output_thumbnail_para is not None:
            self.output_thumbnail_para = output_thumbnail_para
        if output_watermark_paras is not None:
            self.output_watermark_paras = output_watermark_paras

    @property
    def features(self):
        """Gets the features of this MediaDetail.

        任务名称

        :return: The features of this MediaDetail.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this MediaDetail.

        任务名称

        :param features: The features of this MediaDetail.
        :type: list[str]
        """
        self._features = features

    @property
    def origin_para(self):
        """Gets the origin_para of this MediaDetail.


        :return: The origin_para of this MediaDetail.
        :rtype: OriginPara
        """
        return self._origin_para

    @origin_para.setter
    def origin_para(self, origin_para):
        """Sets the origin_para of this MediaDetail.


        :param origin_para: The origin_para of this MediaDetail.
        :type: OriginPara
        """
        self._origin_para = origin_para

    @property
    def output_video_paras(self):
        """Gets the output_video_paras of this MediaDetail.

        多路输出片源信息

        :return: The output_video_paras of this MediaDetail.
        :rtype: list[OutputVideoPara]
        """
        return self._output_video_paras

    @output_video_paras.setter
    def output_video_paras(self, output_video_paras):
        """Sets the output_video_paras of this MediaDetail.

        多路输出片源信息

        :param output_video_paras: The output_video_paras of this MediaDetail.
        :type: list[OutputVideoPara]
        """
        self._output_video_paras = output_video_paras

    @property
    def output_thumbnail_para(self):
        """Gets the output_thumbnail_para of this MediaDetail.


        :return: The output_thumbnail_para of this MediaDetail.
        :rtype: OutputThumbnailPara
        """
        return self._output_thumbnail_para

    @output_thumbnail_para.setter
    def output_thumbnail_para(self, output_thumbnail_para):
        """Sets the output_thumbnail_para of this MediaDetail.


        :param output_thumbnail_para: The output_thumbnail_para of this MediaDetail.
        :type: OutputThumbnailPara
        """
        self._output_thumbnail_para = output_thumbnail_para

    @property
    def output_watermark_paras(self):
        """Gets the output_watermark_paras of this MediaDetail.


        :return: The output_watermark_paras of this MediaDetail.
        :rtype: OutputWatermarkPara
        """
        return self._output_watermark_paras

    @output_watermark_paras.setter
    def output_watermark_paras(self, output_watermark_paras):
        """Sets the output_watermark_paras of this MediaDetail.


        :param output_watermark_paras: The output_watermark_paras of this MediaDetail.
        :type: OutputWatermarkPara
        """
        self._output_watermark_paras = output_watermark_paras

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
        if not isinstance(other, MediaDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
