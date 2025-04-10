# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDetectFaceRespResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alive': 'bool',
        'confidence': 'float',
        'picture': 'str'
    }

    attribute_map = {
        'alive': 'alive',
        'confidence': 'confidence',
        'picture': 'picture'
    }

    def __init__(self, alive=None, confidence=None, picture=None):
        r"""LiveDetectFaceRespResult

        The model defined in huaweicloud sdk

        :param alive: 是否是活体。
        :type alive: bool
        :param confidence: 置信度，取值范围0～1。
        :type confidence: float
        :param picture: 检测出最大人脸的图片base64字符串。
        :type picture: str
        """
        
        

        self._alive = None
        self._confidence = None
        self._picture = None
        self.discriminator = None

        if alive is not None:
            self.alive = alive
        if confidence is not None:
            self.confidence = confidence
        if picture is not None:
            self.picture = picture

    @property
    def alive(self):
        r"""Gets the alive of this LiveDetectFaceRespResult.

        是否是活体。

        :return: The alive of this LiveDetectFaceRespResult.
        :rtype: bool
        """
        return self._alive

    @alive.setter
    def alive(self, alive):
        r"""Sets the alive of this LiveDetectFaceRespResult.

        是否是活体。

        :param alive: The alive of this LiveDetectFaceRespResult.
        :type alive: bool
        """
        self._alive = alive

    @property
    def confidence(self):
        r"""Gets the confidence of this LiveDetectFaceRespResult.

        置信度，取值范围0～1。

        :return: The confidence of this LiveDetectFaceRespResult.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this LiveDetectFaceRespResult.

        置信度，取值范围0～1。

        :param confidence: The confidence of this LiveDetectFaceRespResult.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def picture(self):
        r"""Gets the picture of this LiveDetectFaceRespResult.

        检测出最大人脸的图片base64字符串。

        :return: The picture of this LiveDetectFaceRespResult.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        r"""Sets the picture of this LiveDetectFaceRespResult.

        检测出最大人脸的图片base64字符串。

        :param picture: The picture of this LiveDetectFaceRespResult.
        :type picture: str
        """
        self._picture = picture

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
        if not isinstance(other, LiveDetectFaceRespResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
