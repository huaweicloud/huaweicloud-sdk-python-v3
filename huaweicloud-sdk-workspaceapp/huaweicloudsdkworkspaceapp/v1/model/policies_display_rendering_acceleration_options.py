# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesDisplayRenderingAccelerationOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_acceleration_enhancement_enable': 'bool',
        'video_optimization_enable': 'bool',
        'gpu_color_optimization_enable': 'bool'
    }

    attribute_map = {
        'video_acceleration_enhancement_enable': 'video_acceleration_enhancement_enable',
        'video_optimization_enable': 'video_optimization_enable',
        'gpu_color_optimization_enable': 'gpu_color_optimization_enable'
    }

    def __init__(self, video_acceleration_enhancement_enable=None, video_optimization_enable=None, gpu_color_optimization_enable=None):
        """PoliciesDisplayRenderingAccelerationOptions

        The model defined in huaweicloud sdk

        :param video_acceleration_enhancement_enable: 视频加速增强配置。取值为： false：表示关闭。 true：表示开启。
        :type video_acceleration_enhancement_enable: bool
        :param video_optimization_enable: 是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。
        :type video_optimization_enable: bool
        :param gpu_color_optimization_enable: 是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。
        :type gpu_color_optimization_enable: bool
        """
        
        

        self._video_acceleration_enhancement_enable = None
        self._video_optimization_enable = None
        self._gpu_color_optimization_enable = None
        self.discriminator = None

        if video_acceleration_enhancement_enable is not None:
            self.video_acceleration_enhancement_enable = video_acceleration_enhancement_enable
        if video_optimization_enable is not None:
            self.video_optimization_enable = video_optimization_enable
        if gpu_color_optimization_enable is not None:
            self.gpu_color_optimization_enable = gpu_color_optimization_enable

    @property
    def video_acceleration_enhancement_enable(self):
        """Gets the video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.

        视频加速增强配置。取值为： false：表示关闭。 true：表示开启。

        :return: The video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._video_acceleration_enhancement_enable

    @video_acceleration_enhancement_enable.setter
    def video_acceleration_enhancement_enable(self, video_acceleration_enhancement_enable):
        """Sets the video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.

        视频加速增强配置。取值为： false：表示关闭。 true：表示开启。

        :param video_acceleration_enhancement_enable: The video_acceleration_enhancement_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type video_acceleration_enhancement_enable: bool
        """
        self._video_acceleration_enhancement_enable = video_acceleration_enhancement_enable

    @property
    def video_optimization_enable(self):
        """Gets the video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。

        :return: The video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._video_optimization_enable

    @video_optimization_enable.setter
    def video_optimization_enable(self, video_optimization_enable):
        """Sets the video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启视频场景优化。取值为： false：表示关闭。 true：表示开启。

        :param video_optimization_enable: The video_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type video_optimization_enable: bool
        """
        self._video_optimization_enable = video_optimization_enable

    @property
    def gpu_color_optimization_enable(self):
        """Gets the gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。

        :return: The gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :rtype: bool
        """
        return self._gpu_color_optimization_enable

    @gpu_color_optimization_enable.setter
    def gpu_color_optimization_enable(self, gpu_color_optimization_enable):
        """Sets the gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.

        是否开启GPU色彩优化。取值为： false：表示关闭。 true：表示开启。

        :param gpu_color_optimization_enable: The gpu_color_optimization_enable of this PoliciesDisplayRenderingAccelerationOptions.
        :type gpu_color_optimization_enable: bool
        """
        self._gpu_color_optimization_enable = gpu_color_optimization_enable

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
        if not isinstance(other, PoliciesDisplayRenderingAccelerationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
