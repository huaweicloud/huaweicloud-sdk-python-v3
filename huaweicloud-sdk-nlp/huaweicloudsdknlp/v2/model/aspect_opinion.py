# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AspectOpinion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aspect_category': 'str',
        'aspect_term': 'str',
        'opinion_term': 'str',
        'span': 'list[int]',
        'label': 'int',
        'confidence': 'float',
        'tag': 'str'
    }

    attribute_map = {
        'aspect_category': 'aspect_category',
        'aspect_term': 'aspect_term',
        'opinion_term': 'opinion_term',
        'span': 'span',
        'label': 'label',
        'confidence': 'confidence',
        'tag': 'tag'
    }

    def __init__(self, aspect_category=None, aspect_term=None, opinion_term=None, span=None, label=None, confidence=None, tag=None):
        """AspectOpinion

        The model defined in huaweicloud sdk

        :param aspect_category: 属性类别 手机领域：[&#39;整体&#39;,&#39;性价比&#39;, &#39;赠品&#39;,&#39;分期&#39;, &#39;配件&#39;, &#39;活动&#39;, &#39;品牌&#39;, &#39;物流派送&#39;, &#39;包装&#39;, &#39;游戏性能&#39;, &#39;系统性能&#39;, &#39;芯片&#39;, &#39;屏幕&#39;, &#39;电池&#39;, &#39;自拍&#39;, &#39;拍照&#39;, &#39;音质&#39;, &#39;散热&#39;, &#39;防水&#39;, &#39;信号&#39;, &#39;解锁&#39;, &#39;外形设计&#39;, &#39;握持手感&#39;, &#39;质感&#39;, &#39;颜色&#39;, &#39;内存/容量&#39;, &#39;客服/售后&#39;, &#39;其他&#39;]
        :type aspect_category: str
        :param aspect_term: 属性词，与对应的描述词至少出现其中之一，可能为null。
        :type aspect_term: str
        :param opinion_term: 描述词，与对应的属性词至少出现其中之一，可能为null。
        :type opinion_term: str
        :param span: 共4个数字，分别表示属性词和描述词在文本中的起始位置和结束位置。若属性词为null，则1, 2两位不展示；若描述词为null，则3, 4位不展示。
        :type span: list[int]
        :param label: 情感标签，0：负向，1：正向
        :type label: int
        :param confidence: 情感标签置信度
        :type confidence: float
        :param tag: 属性-描述词片段所对应的标签。若分类为&#39;其他&#39;，则不给出标签，返回null。
        :type tag: str
        """
        
        

        self._aspect_category = None
        self._aspect_term = None
        self._opinion_term = None
        self._span = None
        self._label = None
        self._confidence = None
        self._tag = None
        self.discriminator = None

        self.aspect_category = aspect_category
        self.aspect_term = aspect_term
        self.opinion_term = opinion_term
        self.span = span
        self.label = label
        if confidence is not None:
            self.confidence = confidence
        if tag is not None:
            self.tag = tag

    @property
    def aspect_category(self):
        """Gets the aspect_category of this AspectOpinion.

        属性类别 手机领域：['整体','性价比', '赠品','分期', '配件', '活动', '品牌', '物流派送', '包装', '游戏性能', '系统性能', '芯片', '屏幕', '电池', '自拍', '拍照', '音质', '散热', '防水', '信号', '解锁', '外形设计', '握持手感', '质感', '颜色', '内存/容量', '客服/售后', '其他']

        :return: The aspect_category of this AspectOpinion.
        :rtype: str
        """
        return self._aspect_category

    @aspect_category.setter
    def aspect_category(self, aspect_category):
        """Sets the aspect_category of this AspectOpinion.

        属性类别 手机领域：['整体','性价比', '赠品','分期', '配件', '活动', '品牌', '物流派送', '包装', '游戏性能', '系统性能', '芯片', '屏幕', '电池', '自拍', '拍照', '音质', '散热', '防水', '信号', '解锁', '外形设计', '握持手感', '质感', '颜色', '内存/容量', '客服/售后', '其他']

        :param aspect_category: The aspect_category of this AspectOpinion.
        :type aspect_category: str
        """
        self._aspect_category = aspect_category

    @property
    def aspect_term(self):
        """Gets the aspect_term of this AspectOpinion.

        属性词，与对应的描述词至少出现其中之一，可能为null。

        :return: The aspect_term of this AspectOpinion.
        :rtype: str
        """
        return self._aspect_term

    @aspect_term.setter
    def aspect_term(self, aspect_term):
        """Sets the aspect_term of this AspectOpinion.

        属性词，与对应的描述词至少出现其中之一，可能为null。

        :param aspect_term: The aspect_term of this AspectOpinion.
        :type aspect_term: str
        """
        self._aspect_term = aspect_term

    @property
    def opinion_term(self):
        """Gets the opinion_term of this AspectOpinion.

        描述词，与对应的属性词至少出现其中之一，可能为null。

        :return: The opinion_term of this AspectOpinion.
        :rtype: str
        """
        return self._opinion_term

    @opinion_term.setter
    def opinion_term(self, opinion_term):
        """Sets the opinion_term of this AspectOpinion.

        描述词，与对应的属性词至少出现其中之一，可能为null。

        :param opinion_term: The opinion_term of this AspectOpinion.
        :type opinion_term: str
        """
        self._opinion_term = opinion_term

    @property
    def span(self):
        """Gets the span of this AspectOpinion.

        共4个数字，分别表示属性词和描述词在文本中的起始位置和结束位置。若属性词为null，则1, 2两位不展示；若描述词为null，则3, 4位不展示。

        :return: The span of this AspectOpinion.
        :rtype: list[int]
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this AspectOpinion.

        共4个数字，分别表示属性词和描述词在文本中的起始位置和结束位置。若属性词为null，则1, 2两位不展示；若描述词为null，则3, 4位不展示。

        :param span: The span of this AspectOpinion.
        :type span: list[int]
        """
        self._span = span

    @property
    def label(self):
        """Gets the label of this AspectOpinion.

        情感标签，0：负向，1：正向

        :return: The label of this AspectOpinion.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AspectOpinion.

        情感标签，0：负向，1：正向

        :param label: The label of this AspectOpinion.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this AspectOpinion.

        情感标签置信度

        :return: The confidence of this AspectOpinion.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AspectOpinion.

        情感标签置信度

        :param confidence: The confidence of this AspectOpinion.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def tag(self):
        """Gets the tag of this AspectOpinion.

        属性-描述词片段所对应的标签。若分类为'其他'，则不给出标签，返回null。

        :return: The tag of this AspectOpinion.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AspectOpinion.

        属性-描述词片段所对应的标签。若分类为'其他'，则不给出标签，返回null。

        :param tag: The tag of this AspectOpinion.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, AspectOpinion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
