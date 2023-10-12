# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CameraRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'camera_frame_rate': 'int',
        'camera_max_width': 'int',
        'camera_max_heigth': 'int',
        'camera_compression_method': 'str'
    }

    attribute_map = {
        'camera_frame_rate': 'camera_frame_rate',
        'camera_max_width': 'camera_max_width',
        'camera_max_heigth': 'camera_max_heigth',
        'camera_compression_method': 'camera_compression_method'
    }

    def __init__(self, camera_frame_rate=None, camera_max_width=None, camera_max_heigth=None, camera_compression_method=None):
        """CameraRedirectionOptions

        The model defined in huaweicloud sdk

        :param camera_frame_rate: 摄像头帧率（fps）。取值范围为[1-30]。默认：15。
        :type camera_frame_rate: int
        :param camera_max_width: 摄像头最大宽度（pixel）。取值范围为[1-9999]。默认：3000。
        :type camera_max_width: int
        :param camera_max_heigth: 摄像头最大高度（pixel）。取值范围为[1-9999]。默认：3000。
        :type camera_max_heigth: int
        :param camera_compression_method: 摄像头数据压缩方式。取值为：H.264。
        :type camera_compression_method: str
        """
        
        

        self._camera_frame_rate = None
        self._camera_max_width = None
        self._camera_max_heigth = None
        self._camera_compression_method = None
        self.discriminator = None

        if camera_frame_rate is not None:
            self.camera_frame_rate = camera_frame_rate
        if camera_max_width is not None:
            self.camera_max_width = camera_max_width
        if camera_max_heigth is not None:
            self.camera_max_heigth = camera_max_heigth
        if camera_compression_method is not None:
            self.camera_compression_method = camera_compression_method

    @property
    def camera_frame_rate(self):
        """Gets the camera_frame_rate of this CameraRedirectionOptions.

        摄像头帧率（fps）。取值范围为[1-30]。默认：15。

        :return: The camera_frame_rate of this CameraRedirectionOptions.
        :rtype: int
        """
        return self._camera_frame_rate

    @camera_frame_rate.setter
    def camera_frame_rate(self, camera_frame_rate):
        """Sets the camera_frame_rate of this CameraRedirectionOptions.

        摄像头帧率（fps）。取值范围为[1-30]。默认：15。

        :param camera_frame_rate: The camera_frame_rate of this CameraRedirectionOptions.
        :type camera_frame_rate: int
        """
        self._camera_frame_rate = camera_frame_rate

    @property
    def camera_max_width(self):
        """Gets the camera_max_width of this CameraRedirectionOptions.

        摄像头最大宽度（pixel）。取值范围为[1-9999]。默认：3000。

        :return: The camera_max_width of this CameraRedirectionOptions.
        :rtype: int
        """
        return self._camera_max_width

    @camera_max_width.setter
    def camera_max_width(self, camera_max_width):
        """Sets the camera_max_width of this CameraRedirectionOptions.

        摄像头最大宽度（pixel）。取值范围为[1-9999]。默认：3000。

        :param camera_max_width: The camera_max_width of this CameraRedirectionOptions.
        :type camera_max_width: int
        """
        self._camera_max_width = camera_max_width

    @property
    def camera_max_heigth(self):
        """Gets the camera_max_heigth of this CameraRedirectionOptions.

        摄像头最大高度（pixel）。取值范围为[1-9999]。默认：3000。

        :return: The camera_max_heigth of this CameraRedirectionOptions.
        :rtype: int
        """
        return self._camera_max_heigth

    @camera_max_heigth.setter
    def camera_max_heigth(self, camera_max_heigth):
        """Sets the camera_max_heigth of this CameraRedirectionOptions.

        摄像头最大高度（pixel）。取值范围为[1-9999]。默认：3000。

        :param camera_max_heigth: The camera_max_heigth of this CameraRedirectionOptions.
        :type camera_max_heigth: int
        """
        self._camera_max_heigth = camera_max_heigth

    @property
    def camera_compression_method(self):
        """Gets the camera_compression_method of this CameraRedirectionOptions.

        摄像头数据压缩方式。取值为：H.264。

        :return: The camera_compression_method of this CameraRedirectionOptions.
        :rtype: str
        """
        return self._camera_compression_method

    @camera_compression_method.setter
    def camera_compression_method(self, camera_compression_method):
        """Sets the camera_compression_method of this CameraRedirectionOptions.

        摄像头数据压缩方式。取值为：H.264。

        :param camera_compression_method: The camera_compression_method of this CameraRedirectionOptions.
        :type camera_compression_method: str
        """
        self._camera_compression_method = camera_compression_method

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
        if not isinstance(other, CameraRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
