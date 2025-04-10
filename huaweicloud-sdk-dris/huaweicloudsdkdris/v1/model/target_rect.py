# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetRect:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'camera_code': 'str',
        'camera_ip': 'str',
        'target_pos': 'TargetPos',
        'time_stamp_diff': 'int'
    }

    attribute_map = {
        'camera_code': 'camera_code',
        'camera_ip': 'camera_ip',
        'target_pos': 'target_pos',
        'time_stamp_diff': 'time_stamp_diff'
    }

    def __init__(self, camera_code=None, camera_ip=None, target_pos=None, time_stamp_diff=None):
        r"""TargetRect

        The model defined in huaweicloud sdk

        :param camera_code: **参数说明**：摄像头编码。
        :type camera_code: str
        :param camera_ip: **参数说明**：摄像头IP地址。
        :type camera_ip: str
        :param target_pos: 
        :type target_pos: :class:`huaweicloudsdkdris.v1.TargetPos`
        :param time_stamp_diff: **参数说明**：与SnapTime的时间差值：当前检测框所在相机的时间戳减去雷视拟合轨迹中的SnapTime的差值。
        :type time_stamp_diff: int
        """
        
        

        self._camera_code = None
        self._camera_ip = None
        self._target_pos = None
        self._time_stamp_diff = None
        self.discriminator = None

        if camera_code is not None:
            self.camera_code = camera_code
        if camera_ip is not None:
            self.camera_ip = camera_ip
        if target_pos is not None:
            self.target_pos = target_pos
        if time_stamp_diff is not None:
            self.time_stamp_diff = time_stamp_diff

    @property
    def camera_code(self):
        r"""Gets the camera_code of this TargetRect.

        **参数说明**：摄像头编码。

        :return: The camera_code of this TargetRect.
        :rtype: str
        """
        return self._camera_code

    @camera_code.setter
    def camera_code(self, camera_code):
        r"""Sets the camera_code of this TargetRect.

        **参数说明**：摄像头编码。

        :param camera_code: The camera_code of this TargetRect.
        :type camera_code: str
        """
        self._camera_code = camera_code

    @property
    def camera_ip(self):
        r"""Gets the camera_ip of this TargetRect.

        **参数说明**：摄像头IP地址。

        :return: The camera_ip of this TargetRect.
        :rtype: str
        """
        return self._camera_ip

    @camera_ip.setter
    def camera_ip(self, camera_ip):
        r"""Sets the camera_ip of this TargetRect.

        **参数说明**：摄像头IP地址。

        :param camera_ip: The camera_ip of this TargetRect.
        :type camera_ip: str
        """
        self._camera_ip = camera_ip

    @property
    def target_pos(self):
        r"""Gets the target_pos of this TargetRect.

        :return: The target_pos of this TargetRect.
        :rtype: :class:`huaweicloudsdkdris.v1.TargetPos`
        """
        return self._target_pos

    @target_pos.setter
    def target_pos(self, target_pos):
        r"""Sets the target_pos of this TargetRect.

        :param target_pos: The target_pos of this TargetRect.
        :type target_pos: :class:`huaweicloudsdkdris.v1.TargetPos`
        """
        self._target_pos = target_pos

    @property
    def time_stamp_diff(self):
        r"""Gets the time_stamp_diff of this TargetRect.

        **参数说明**：与SnapTime的时间差值：当前检测框所在相机的时间戳减去雷视拟合轨迹中的SnapTime的差值。

        :return: The time_stamp_diff of this TargetRect.
        :rtype: int
        """
        return self._time_stamp_diff

    @time_stamp_diff.setter
    def time_stamp_diff(self, time_stamp_diff):
        r"""Sets the time_stamp_diff of this TargetRect.

        **参数说明**：与SnapTime的时间差值：当前检测框所在相机的时间戳减去雷视拟合轨迹中的SnapTime的差值。

        :param time_stamp_diff: The time_stamp_diff of this TargetRect.
        :type time_stamp_diff: int
        """
        self._time_stamp_diff = time_stamp_diff

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
        if not isinstance(other, TargetRect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
