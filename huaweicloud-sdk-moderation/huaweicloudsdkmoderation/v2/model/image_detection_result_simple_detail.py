# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResultSimpleDetail:

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
        'label': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label'
    }

    def __init__(self, confidence=None, label=None):
        """ImageDetectionResultSimpleDetail

        The model defined in huaweicloud sdk

        :param confidence: 置信度，取值范围 0-1。
        :type confidence: float
        :param label: 每个检测结果的标签化说明： - terrorism：label为对应的涉政暴恐元素信息。 - 涉政暴恐场景当前支持label列表如下：   - normal：正常   - knife：刀   - gun：枪   - fire：火灾   - bloody ：血腥   - terrorist：暴恐组织及标志   - fascist：法西斯组织及标志   - cult：邪教组织及标志   - negative_politics ：涉政负面组织及标志   - negative_political_events：涉政负面事件及标志   - special_characters ：特殊文字   - kidnap：绑架   - corpse：尸体   - riot：暴乱事件   - parade ：游行示威   - sensitive_landmarks：敏感地标   - military_weapon：军事武器   - army：警察部队   - positive_politics：涉政正面组织及标志   - crowd：人群聚集 - porn：label为对应的涉黄分类（涉黄、性感等）信息。 - 鉴黄场景当前支持label列表如下：   - normal：正常   - porn：色情   - sexy：性感 
        :type label: str
        """
        
        

        self._confidence = None
        self._label = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label

    @property
    def confidence(self):
        """Gets the confidence of this ImageDetectionResultSimpleDetail.

        置信度，取值范围 0-1。

        :return: The confidence of this ImageDetectionResultSimpleDetail.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageDetectionResultSimpleDetail.

        置信度，取值范围 0-1。

        :param confidence: The confidence of this ImageDetectionResultSimpleDetail.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def label(self):
        """Gets the label of this ImageDetectionResultSimpleDetail.

        每个检测结果的标签化说明： - terrorism：label为对应的涉政暴恐元素信息。 - 涉政暴恐场景当前支持label列表如下：   - normal：正常   - knife：刀   - gun：枪   - fire：火灾   - bloody ：血腥   - terrorist：暴恐组织及标志   - fascist：法西斯组织及标志   - cult：邪教组织及标志   - negative_politics ：涉政负面组织及标志   - negative_political_events：涉政负面事件及标志   - special_characters ：特殊文字   - kidnap：绑架   - corpse：尸体   - riot：暴乱事件   - parade ：游行示威   - sensitive_landmarks：敏感地标   - military_weapon：军事武器   - army：警察部队   - positive_politics：涉政正面组织及标志   - crowd：人群聚集 - porn：label为对应的涉黄分类（涉黄、性感等）信息。 - 鉴黄场景当前支持label列表如下：   - normal：正常   - porn：色情   - sexy：性感 

        :return: The label of this ImageDetectionResultSimpleDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetectionResultSimpleDetail.

        每个检测结果的标签化说明： - terrorism：label为对应的涉政暴恐元素信息。 - 涉政暴恐场景当前支持label列表如下：   - normal：正常   - knife：刀   - gun：枪   - fire：火灾   - bloody ：血腥   - terrorist：暴恐组织及标志   - fascist：法西斯组织及标志   - cult：邪教组织及标志   - negative_politics ：涉政负面组织及标志   - negative_political_events：涉政负面事件及标志   - special_characters ：特殊文字   - kidnap：绑架   - corpse：尸体   - riot：暴乱事件   - parade ：游行示威   - sensitive_landmarks：敏感地标   - military_weapon：军事武器   - army：警察部队   - positive_politics：涉政正面组织及标志   - crowd：人群聚集 - porn：label为对应的涉黄分类（涉黄、性感等）信息。 - 鉴黄场景当前支持label列表如下：   - normal：正常   - porn：色情   - sexy：性感 

        :param label: The label of this ImageDetectionResultSimpleDetail.
        :type label: str
        """
        self._label = label

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
        if not isinstance(other, ImageDetectionResultSimpleDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
