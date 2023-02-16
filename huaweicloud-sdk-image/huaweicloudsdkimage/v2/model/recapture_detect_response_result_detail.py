# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecaptureDetectResponseResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'confidence': 'str'
    }

    attribute_map = {
        'label': 'label',
        'confidence': 'confidence'
    }

    def __init__(self, label=None, confidence=None):
        """RecaptureDetectResponseResultDetail

        The model defined in huaweicloud sdk

        :param label: 标签值。| original：原始图 recapture：翻拍图
        :type label: str
        :param confidence: 置信度，取值范围（0~1）。
        :type confidence: str
        """
        
        

        self._label = None
        self._confidence = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence

    @property
    def label(self):
        """Gets the label of this RecaptureDetectResponseResultDetail.

        标签值。| original：原始图 recapture：翻拍图

        :return: The label of this RecaptureDetectResponseResultDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RecaptureDetectResponseResultDetail.

        标签值。| original：原始图 recapture：翻拍图

        :param label: The label of this RecaptureDetectResponseResultDetail.
        :type label: str
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this RecaptureDetectResponseResultDetail.

        置信度，取值范围（0~1）。

        :return: The confidence of this RecaptureDetectResponseResultDetail.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecaptureDetectResponseResultDetail.

        置信度，取值范围（0~1）。

        :param confidence: The confidence of this RecaptureDetectResponseResultDetail.
        :type confidence: str
        """
        self._confidence = confidence

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
        if not isinstance(other, RecaptureDetectResponseResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
