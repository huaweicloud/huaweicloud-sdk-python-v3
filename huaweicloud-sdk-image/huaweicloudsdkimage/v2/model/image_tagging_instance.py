# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageTaggingInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bounding_box': 'ImageTaggingBoundingBox',
        'confidence': 'str'
    }

    attribute_map = {
        'bounding_box': 'bounding_box',
        'confidence': 'confidence'
    }

    def __init__(self, bounding_box=None, confidence=None):
        r"""ImageTaggingInstance

        The model defined in huaweicloud sdk

        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkimage.v2.ImageTaggingBoundingBox`
        :param confidence: 检测标签置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。
        :type confidence: str
        """
        
        

        self._bounding_box = None
        self._confidence = None
        self.discriminator = None

        if bounding_box is not None:
            self.bounding_box = bounding_box
        if confidence is not None:
            self.confidence = confidence

    @property
    def bounding_box(self):
        r"""Gets the bounding_box of this ImageTaggingInstance.

        :return: The bounding_box of this ImageTaggingInstance.
        :rtype: :class:`huaweicloudsdkimage.v2.ImageTaggingBoundingBox`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        r"""Sets the bounding_box of this ImageTaggingInstance.

        :param bounding_box: The bounding_box of this ImageTaggingInstance.
        :type bounding_box: :class:`huaweicloudsdkimage.v2.ImageTaggingBoundingBox`
        """
        self._bounding_box = bounding_box

    @property
    def confidence(self):
        r"""Gets the confidence of this ImageTaggingInstance.

        检测标签置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。

        :return: The confidence of this ImageTaggingInstance.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this ImageTaggingInstance.

        检测标签置信度,将Float型置信度转为String类型返回,Float取值范围（0~100）。

        :param confidence: The confidence of this ImageTaggingInstance.
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
        if not isinstance(other, ImageTaggingInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
