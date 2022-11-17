# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AspectAdvanceOpinion:

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
        'label': 'int',
        'confidence': 'float',
        'aspect_term': 'str',
        'opinion_term': 'str',
        'span': 'list[int]',
        'tag': 'str'
    }

    attribute_map = {
        'aspect_category': 'aspect_category',
        'label': 'label',
        'confidence': 'confidence',
        'aspect_term': 'aspect_term',
        'opinion_term': 'opinion_term',
        'span': 'span',
        'tag': 'tag'
    }

    def __init__(self, aspect_category=None, label=None, confidence=None, aspect_term=None, opinion_term=None, span=None, tag=None):
        """AspectAdvanceOpinion

        The model defined in huaweicloud sdk

        :param aspect_category: 属性类别 手机领域：[&#39;整体&#39;,&#39;内存&#39;,&#39;外形设计&#39;,&#39;屏幕&#39;,&#39;性价比&#39;,&#39;拍照&#39;,&#39;散热&#39;,&#39;电池&#39;,&#39;人脸识别&#39;,&#39;信号&#39;,&#39;指纹识别&#39;,&#39;音质&#39;,&#39;握持手感&#39;,&#39;活动配件赠品&#39;,&#39;防水&#39;,&#39;客服&#39;,&#39;物流派送&#39;,&#39;包装&#39;] 汽车领域：[&#39;动力&#39;,&#39;外观&#39;,&#39;内饰&#39;,&#39;空间&#39;,&#39;操控&#39;, &#39;舒适性&#39;, &#39;性价比&#39;,&#39;能耗&#39;]
        :type aspect_category: str
        :param label: 情感标签，0：负向，1：正向
        :type label: int
        :param confidence: 情感标签置信度
        :type confidence: float
        :param aspect_term: 属性描述词，预留参数，暂不支持。
        :type aspect_term: str
        :param opinion_term: 观点描述词，预留参数，暂不支持。
        :type opinion_term: str
        :param span: 属性评价起始位置，预留参数，暂不支持。
        :type span: list[int]
        :param tag: 观点标签，预留参数，暂不支持。
        :type tag: str
        """
        
        

        self._aspect_category = None
        self._label = None
        self._confidence = None
        self._aspect_term = None
        self._opinion_term = None
        self._span = None
        self._tag = None
        self.discriminator = None

        self.aspect_category = aspect_category
        self.label = label
        if confidence is not None:
            self.confidence = confidence
        self.aspect_term = aspect_term
        self.opinion_term = opinion_term
        self.span = span
        if tag is not None:
            self.tag = tag

    @property
    def aspect_category(self):
        """Gets the aspect_category of this AspectAdvanceOpinion.

        属性类别 手机领域：['整体','内存','外形设计','屏幕','性价比','拍照','散热','电池','人脸识别','信号','指纹识别','音质','握持手感','活动配件赠品','防水','客服','物流派送','包装'] 汽车领域：['动力','外观','内饰','空间','操控', '舒适性', '性价比','能耗']

        :return: The aspect_category of this AspectAdvanceOpinion.
        :rtype: str
        """
        return self._aspect_category

    @aspect_category.setter
    def aspect_category(self, aspect_category):
        """Sets the aspect_category of this AspectAdvanceOpinion.

        属性类别 手机领域：['整体','内存','外形设计','屏幕','性价比','拍照','散热','电池','人脸识别','信号','指纹识别','音质','握持手感','活动配件赠品','防水','客服','物流派送','包装'] 汽车领域：['动力','外观','内饰','空间','操控', '舒适性', '性价比','能耗']

        :param aspect_category: The aspect_category of this AspectAdvanceOpinion.
        :type aspect_category: str
        """
        self._aspect_category = aspect_category

    @property
    def label(self):
        """Gets the label of this AspectAdvanceOpinion.

        情感标签，0：负向，1：正向

        :return: The label of this AspectAdvanceOpinion.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AspectAdvanceOpinion.

        情感标签，0：负向，1：正向

        :param label: The label of this AspectAdvanceOpinion.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this AspectAdvanceOpinion.

        情感标签置信度

        :return: The confidence of this AspectAdvanceOpinion.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AspectAdvanceOpinion.

        情感标签置信度

        :param confidence: The confidence of this AspectAdvanceOpinion.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def aspect_term(self):
        """Gets the aspect_term of this AspectAdvanceOpinion.

        属性描述词，预留参数，暂不支持。

        :return: The aspect_term of this AspectAdvanceOpinion.
        :rtype: str
        """
        return self._aspect_term

    @aspect_term.setter
    def aspect_term(self, aspect_term):
        """Sets the aspect_term of this AspectAdvanceOpinion.

        属性描述词，预留参数，暂不支持。

        :param aspect_term: The aspect_term of this AspectAdvanceOpinion.
        :type aspect_term: str
        """
        self._aspect_term = aspect_term

    @property
    def opinion_term(self):
        """Gets the opinion_term of this AspectAdvanceOpinion.

        观点描述词，预留参数，暂不支持。

        :return: The opinion_term of this AspectAdvanceOpinion.
        :rtype: str
        """
        return self._opinion_term

    @opinion_term.setter
    def opinion_term(self, opinion_term):
        """Sets the opinion_term of this AspectAdvanceOpinion.

        观点描述词，预留参数，暂不支持。

        :param opinion_term: The opinion_term of this AspectAdvanceOpinion.
        :type opinion_term: str
        """
        self._opinion_term = opinion_term

    @property
    def span(self):
        """Gets the span of this AspectAdvanceOpinion.

        属性评价起始位置，预留参数，暂不支持。

        :return: The span of this AspectAdvanceOpinion.
        :rtype: list[int]
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this AspectAdvanceOpinion.

        属性评价起始位置，预留参数，暂不支持。

        :param span: The span of this AspectAdvanceOpinion.
        :type span: list[int]
        """
        self._span = span

    @property
    def tag(self):
        """Gets the tag of this AspectAdvanceOpinion.

        观点标签，预留参数，暂不支持。

        :return: The tag of this AspectAdvanceOpinion.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AspectAdvanceOpinion.

        观点标签，预留参数，暂不支持。

        :param tag: The tag of this AspectAdvanceOpinion.
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
        if not isinstance(other, AspectAdvanceOpinion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
