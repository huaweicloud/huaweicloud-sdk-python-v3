# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoMotionCaptureJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'motion_capture_mode': 'str',
        'input_info': 'InputInfo',
        'output_info': 'OutputInfo'
    }

    attribute_map = {
        'motion_capture_mode': 'motion_capture_mode',
        'input_info': 'input_info',
        'output_info': 'output_info'
    }

    def __init__(self, motion_capture_mode=None, input_info=None, output_info=None):
        r"""VideoMotionCaptureJobReq

        The model defined in huaweicloud sdk

        :param motion_capture_mode: 视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动
        :type motion_capture_mode: str
        :param input_info: 
        :type input_info: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        :param output_info: 
        :type output_info: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        """
        
        

        self._motion_capture_mode = None
        self._input_info = None
        self._output_info = None
        self.discriminator = None

        if motion_capture_mode is not None:
            self.motion_capture_mode = motion_capture_mode
        if input_info is not None:
            self.input_info = input_info
        if output_info is not None:
            self.output_info = output_info

    @property
    def motion_capture_mode(self):
        r"""Gets the motion_capture_mode of this VideoMotionCaptureJobReq.

        视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动

        :return: The motion_capture_mode of this VideoMotionCaptureJobReq.
        :rtype: str
        """
        return self._motion_capture_mode

    @motion_capture_mode.setter
    def motion_capture_mode(self, motion_capture_mode):
        r"""Sets the motion_capture_mode of this VideoMotionCaptureJobReq.

        视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动

        :param motion_capture_mode: The motion_capture_mode of this VideoMotionCaptureJobReq.
        :type motion_capture_mode: str
        """
        self._motion_capture_mode = motion_capture_mode

    @property
    def input_info(self):
        r"""Gets the input_info of this VideoMotionCaptureJobReq.

        :return: The input_info of this VideoMotionCaptureJobReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        """
        return self._input_info

    @input_info.setter
    def input_info(self, input_info):
        r"""Sets the input_info of this VideoMotionCaptureJobReq.

        :param input_info: The input_info of this VideoMotionCaptureJobReq.
        :type input_info: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        """
        self._input_info = input_info

    @property
    def output_info(self):
        r"""Gets the output_info of this VideoMotionCaptureJobReq.

        :return: The output_info of this VideoMotionCaptureJobReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        """
        return self._output_info

    @output_info.setter
    def output_info(self, output_info):
        r"""Sets the output_info of this VideoMotionCaptureJobReq.

        :param output_info: The output_info of this VideoMotionCaptureJobReq.
        :type output_info: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        """
        self._output_info = output_info

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
        if not isinstance(other, VideoMotionCaptureJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
