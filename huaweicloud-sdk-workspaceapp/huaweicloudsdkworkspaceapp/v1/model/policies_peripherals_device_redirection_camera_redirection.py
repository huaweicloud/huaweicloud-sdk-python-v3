# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirectionCameraRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_compress_enable': 'bool',
        'options': 'CameraRedirectionOptions'
    }

    attribute_map = {
        'video_compress_enable': 'video_compress_enable',
        'options': 'options'
    }

    def __init__(self, video_compress_enable=None, options=None):
        """PoliciesPeripheralsDeviceRedirectionCameraRedirection

        The model defined in huaweicloud sdk

        :param video_compress_enable: 是否开启摄像头设备重定向。取值为： false：表示关闭。 true：表示开启。
        :type video_compress_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.CameraRedirectionOptions`
        """
        
        

        self._video_compress_enable = None
        self._options = None
        self.discriminator = None

        if video_compress_enable is not None:
            self.video_compress_enable = video_compress_enable
        if options is not None:
            self.options = options

    @property
    def video_compress_enable(self):
        """Gets the video_compress_enable of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.

        是否开启摄像头设备重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The video_compress_enable of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.
        :rtype: bool
        """
        return self._video_compress_enable

    @video_compress_enable.setter
    def video_compress_enable(self, video_compress_enable):
        """Sets the video_compress_enable of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.

        是否开启摄像头设备重定向。取值为： false：表示关闭。 true：表示开启。

        :param video_compress_enable: The video_compress_enable of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.
        :type video_compress_enable: bool
        """
        self._video_compress_enable = video_compress_enable

    @property
    def options(self):
        """Gets the options of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.

        :return: The options of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CameraRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.

        :param options: The options of this PoliciesPeripheralsDeviceRedirectionCameraRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.CameraRedirectionOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirectionCameraRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
