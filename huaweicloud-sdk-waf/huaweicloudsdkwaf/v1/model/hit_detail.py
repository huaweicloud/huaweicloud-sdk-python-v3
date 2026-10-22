# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HitDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_type': 'str',
        'sub_risk_type': 'list[str]',
        'prob': 'float',
        'segments': 'list[SegmentInfo]',
        'extra_info': 'object'
    }

    attribute_map = {
        'risk_type': 'risk_type',
        'sub_risk_type': 'sub_risk_type',
        'prob': 'prob',
        'segments': 'segments',
        'extra_info': 'extra_info'
    }

    def __init__(self, risk_type=None, sub_risk_type=None, prob=None, segments=None, extra_info=None):
        r"""HitDetail

        The model defined in huaweicloud sdk

        :param risk_type: 威胁类型
        :type risk_type: str
        :param sub_risk_type: 子威胁类型
        :type sub_risk_type: list[str]
        :param prob: 置信度分数
        :type prob: float
        :param segments: 命中规则的片段
        :type segments: list[:class:`huaweicloudsdkwaf.v1.SegmentInfo`]
        :param extra_info: 额外检测信息，不同风险类型下字段不固定
        :type extra_info: object
        """
        
        

        self._risk_type = None
        self._sub_risk_type = None
        self._prob = None
        self._segments = None
        self._extra_info = None
        self.discriminator = None

        if risk_type is not None:
            self.risk_type = risk_type
        if sub_risk_type is not None:
            self.sub_risk_type = sub_risk_type
        if prob is not None:
            self.prob = prob
        if segments is not None:
            self.segments = segments
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def risk_type(self):
        r"""Gets the risk_type of this HitDetail.

        威胁类型

        :return: The risk_type of this HitDetail.
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        r"""Sets the risk_type of this HitDetail.

        威胁类型

        :param risk_type: The risk_type of this HitDetail.
        :type risk_type: str
        """
        self._risk_type = risk_type

    @property
    def sub_risk_type(self):
        r"""Gets the sub_risk_type of this HitDetail.

        子威胁类型

        :return: The sub_risk_type of this HitDetail.
        :rtype: list[str]
        """
        return self._sub_risk_type

    @sub_risk_type.setter
    def sub_risk_type(self, sub_risk_type):
        r"""Sets the sub_risk_type of this HitDetail.

        子威胁类型

        :param sub_risk_type: The sub_risk_type of this HitDetail.
        :type sub_risk_type: list[str]
        """
        self._sub_risk_type = sub_risk_type

    @property
    def prob(self):
        r"""Gets the prob of this HitDetail.

        置信度分数

        :return: The prob of this HitDetail.
        :rtype: float
        """
        return self._prob

    @prob.setter
    def prob(self, prob):
        r"""Sets the prob of this HitDetail.

        置信度分数

        :param prob: The prob of this HitDetail.
        :type prob: float
        """
        self._prob = prob

    @property
    def segments(self):
        r"""Gets the segments of this HitDetail.

        命中规则的片段

        :return: The segments of this HitDetail.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SegmentInfo`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        r"""Sets the segments of this HitDetail.

        命中规则的片段

        :param segments: The segments of this HitDetail.
        :type segments: list[:class:`huaweicloudsdkwaf.v1.SegmentInfo`]
        """
        self._segments = segments

    @property
    def extra_info(self):
        r"""Gets the extra_info of this HitDetail.

        额外检测信息，不同风险类型下字段不固定

        :return: The extra_info of this HitDetail.
        :rtype: object
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this HitDetail.

        额外检测信息，不同风险类型下字段不固定

        :param extra_info: The extra_info of this HitDetail.
        :type extra_info: object
        """
        self._extra_info = extra_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HitDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
