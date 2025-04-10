# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InferenceEyeCorrectionMarkInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eye_correction_start_time': 'str',
        'eye_correction_end_time': 'str'
    }

    attribute_map = {
        'eye_correction_start_time': 'eye_correction_start_time',
        'eye_correction_end_time': 'eye_correction_end_time'
    }

    def __init__(self, eye_correction_start_time=None, eye_correction_end_time=None):
        r"""InferenceEyeCorrectionMarkInfo

        The model defined in huaweicloud sdk

        :param eye_correction_start_time: 选取推理数据预处理眼神矫正起始时间。格式：“HH:MM:SS.mmm”。
        :type eye_correction_start_time: str
        :param eye_correction_end_time: 选取推理数据预处理眼神矫正结束时间。格式：“HH:MM:SS.mmm”。
        :type eye_correction_end_time: str
        """
        
        

        self._eye_correction_start_time = None
        self._eye_correction_end_time = None
        self.discriminator = None

        if eye_correction_start_time is not None:
            self.eye_correction_start_time = eye_correction_start_time
        if eye_correction_end_time is not None:
            self.eye_correction_end_time = eye_correction_end_time

    @property
    def eye_correction_start_time(self):
        r"""Gets the eye_correction_start_time of this InferenceEyeCorrectionMarkInfo.

        选取推理数据预处理眼神矫正起始时间。格式：“HH:MM:SS.mmm”。

        :return: The eye_correction_start_time of this InferenceEyeCorrectionMarkInfo.
        :rtype: str
        """
        return self._eye_correction_start_time

    @eye_correction_start_time.setter
    def eye_correction_start_time(self, eye_correction_start_time):
        r"""Sets the eye_correction_start_time of this InferenceEyeCorrectionMarkInfo.

        选取推理数据预处理眼神矫正起始时间。格式：“HH:MM:SS.mmm”。

        :param eye_correction_start_time: The eye_correction_start_time of this InferenceEyeCorrectionMarkInfo.
        :type eye_correction_start_time: str
        """
        self._eye_correction_start_time = eye_correction_start_time

    @property
    def eye_correction_end_time(self):
        r"""Gets the eye_correction_end_time of this InferenceEyeCorrectionMarkInfo.

        选取推理数据预处理眼神矫正结束时间。格式：“HH:MM:SS.mmm”。

        :return: The eye_correction_end_time of this InferenceEyeCorrectionMarkInfo.
        :rtype: str
        """
        return self._eye_correction_end_time

    @eye_correction_end_time.setter
    def eye_correction_end_time(self, eye_correction_end_time):
        r"""Sets the eye_correction_end_time of this InferenceEyeCorrectionMarkInfo.

        选取推理数据预处理眼神矫正结束时间。格式：“HH:MM:SS.mmm”。

        :param eye_correction_end_time: The eye_correction_end_time of this InferenceEyeCorrectionMarkInfo.
        :type eye_correction_end_time: str
        """
        self._eye_correction_end_time = eye_correction_end_time

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
        if not isinstance(other, InferenceEyeCorrectionMarkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
