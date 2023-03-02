# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSynthesisInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_config': 'VideoSynthesisInfo'
    }

    attribute_map = {
        'video_config': 'video_config'
    }

    def __init__(self, video_config=None):
        """VideoSynthesisInference

        The model defined in huaweicloud sdk

        :param video_config: 
        :type video_config: :class:`huaweicloudsdkimage.v2.VideoSynthesisInfo`
        """
        
        

        self._video_config = None
        self.discriminator = None

        self.video_config = video_config

    @property
    def video_config(self):
        """Gets the video_config of this VideoSynthesisInference.

        :return: The video_config of this VideoSynthesisInference.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoSynthesisInfo`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this VideoSynthesisInference.

        :param video_config: The video_config of this VideoSynthesisInference.
        :type video_config: :class:`huaweicloudsdkimage.v2.VideoSynthesisInfo`
        """
        self._video_config = video_config

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
        if not isinstance(other, VideoSynthesisInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
