# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResultAdDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'label': 'str',
        'hit_contexts': 'list[str]'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label',
        'hit_contexts': 'hit_contexts'
    }

    def __init__(self, confidence=None, label=None, hit_contexts=None):
        """ImageDetectionResultAdDetail

        The model defined in huaweicloud sdk

        :param confidence: 置信度，取值范围 0-1。
        :type confidence: float
        :param label: ad：label为对应的广告识别结果信息 - 广告场景当前支持label列表如下：   - normal：正常   - ad：广告 - 图文审核场景当前支持label列表如下：   - normal：正常   - qr_code：二维   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品   - 其他自定义黑库名称 
        :type label: str
        :param hit_contexts: 图文审核场景命中的文本列表。
        :type hit_contexts: list[str]
        """
        
        

        self._confidence = None
        self._label = None
        self._hit_contexts = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label
        if hit_contexts is not None:
            self.hit_contexts = hit_contexts

    @property
    def confidence(self):
        """Gets the confidence of this ImageDetectionResultAdDetail.

        置信度，取值范围 0-1。

        :return: The confidence of this ImageDetectionResultAdDetail.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageDetectionResultAdDetail.

        置信度，取值范围 0-1。

        :param confidence: The confidence of this ImageDetectionResultAdDetail.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def label(self):
        """Gets the label of this ImageDetectionResultAdDetail.

        ad：label为对应的广告识别结果信息 - 广告场景当前支持label列表如下：   - normal：正常   - ad：广告 - 图文审核场景当前支持label列表如下：   - normal：正常   - qr_code：二维   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品   - 其他自定义黑库名称 

        :return: The label of this ImageDetectionResultAdDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetectionResultAdDetail.

        ad：label为对应的广告识别结果信息 - 广告场景当前支持label列表如下：   - normal：正常   - ad：广告 - 图文审核场景当前支持label列表如下：   - normal：正常   - qr_code：二维   - politics：涉政   - porn：涉黄   - ad：广告   - abuse：辱骂   - contraband：违禁品   - 其他自定义黑库名称 

        :param label: The label of this ImageDetectionResultAdDetail.
        :type label: str
        """
        self._label = label

    @property
    def hit_contexts(self):
        """Gets the hit_contexts of this ImageDetectionResultAdDetail.

        图文审核场景命中的文本列表。

        :return: The hit_contexts of this ImageDetectionResultAdDetail.
        :rtype: list[str]
        """
        return self._hit_contexts

    @hit_contexts.setter
    def hit_contexts(self, hit_contexts):
        """Sets the hit_contexts of this ImageDetectionResultAdDetail.

        图文审核场景命中的文本列表。

        :param hit_contexts: The hit_contexts of this ImageDetectionResultAdDetail.
        :type hit_contexts: list[str]
        """
        self._hit_contexts = hit_contexts

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
        if not isinstance(other, ImageDetectionResultAdDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
