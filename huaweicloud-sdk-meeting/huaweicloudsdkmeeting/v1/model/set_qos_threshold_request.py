# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetQosThresholdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'threshold_type': 'str',
        'body': 'SetQosThresholdReq'
    }

    attribute_map = {
        'threshold_type': 'thresholdType',
        'body': 'body'
    }

    def __init__(self, threshold_type=None, body=None):
        """SetQosThresholdRequest

        The model defined in huaweicloud sdk

        :param threshold_type: 阈值类型： * AUDIO：音频相关阈值 * VIDEO：视频相关阈值 * SCREEN：屏幕共享相关阈值 * CPU：CPU相关阈值
        :type threshold_type: str
        :param body: Body of the SetQosThresholdRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdReq`
        """
        
        

        self._threshold_type = None
        self._body = None
        self.discriminator = None

        self.threshold_type = threshold_type
        if body is not None:
            self.body = body

    @property
    def threshold_type(self):
        """Gets the threshold_type of this SetQosThresholdRequest.

        阈值类型： * AUDIO：音频相关阈值 * VIDEO：视频相关阈值 * SCREEN：屏幕共享相关阈值 * CPU：CPU相关阈值

        :return: The threshold_type of this SetQosThresholdRequest.
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this SetQosThresholdRequest.

        阈值类型： * AUDIO：音频相关阈值 * VIDEO：视频相关阈值 * SCREEN：屏幕共享相关阈值 * CPU：CPU相关阈值

        :param threshold_type: The threshold_type of this SetQosThresholdRequest.
        :type threshold_type: str
        """
        self._threshold_type = threshold_type

    @property
    def body(self):
        """Gets the body of this SetQosThresholdRequest.


        :return: The body of this SetQosThresholdRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetQosThresholdRequest.


        :param body: The body of this SetQosThresholdRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdReq`
        """
        self._body = body

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
        if not isinstance(other, SetQosThresholdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
