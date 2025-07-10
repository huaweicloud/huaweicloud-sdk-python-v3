# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BestPracticeOverviewItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'detection_count': 'int',
        'high_risk_count': 'int',
        'medium_risk_count': 'int',
        'low_risk_count': 'int',
        'risk_item_description': 'list[str]'
    }

    attribute_map = {
        'score': 'score',
        'detection_count': 'detection_count',
        'high_risk_count': 'high_risk_count',
        'medium_risk_count': 'medium_risk_count',
        'low_risk_count': 'low_risk_count',
        'risk_item_description': 'risk_item_description'
    }

    def __init__(self, score=None, detection_count=None, high_risk_count=None, medium_risk_count=None, low_risk_count=None, risk_item_description=None):
        r"""BestPracticeOverviewItem

        The model defined in huaweicloud sdk

        :param score: 分数
        :type score: float
        :param detection_count: 检测项个数
        :type detection_count: int
        :param high_risk_count: 高风险项个数
        :type high_risk_count: int
        :param medium_risk_count: 中风险项个数
        :type medium_risk_count: int
        :param low_risk_count: 低风险项个数
        :type low_risk_count: int
        :param risk_item_description: 风险描述
        :type risk_item_description: list[str]
        """
        
        

        self._score = None
        self._detection_count = None
        self._high_risk_count = None
        self._medium_risk_count = None
        self._low_risk_count = None
        self._risk_item_description = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if detection_count is not None:
            self.detection_count = detection_count
        if high_risk_count is not None:
            self.high_risk_count = high_risk_count
        if medium_risk_count is not None:
            self.medium_risk_count = medium_risk_count
        if low_risk_count is not None:
            self.low_risk_count = low_risk_count
        if risk_item_description is not None:
            self.risk_item_description = risk_item_description

    @property
    def score(self):
        r"""Gets the score of this BestPracticeOverviewItem.

        分数

        :return: The score of this BestPracticeOverviewItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this BestPracticeOverviewItem.

        分数

        :param score: The score of this BestPracticeOverviewItem.
        :type score: float
        """
        self._score = score

    @property
    def detection_count(self):
        r"""Gets the detection_count of this BestPracticeOverviewItem.

        检测项个数

        :return: The detection_count of this BestPracticeOverviewItem.
        :rtype: int
        """
        return self._detection_count

    @detection_count.setter
    def detection_count(self, detection_count):
        r"""Sets the detection_count of this BestPracticeOverviewItem.

        检测项个数

        :param detection_count: The detection_count of this BestPracticeOverviewItem.
        :type detection_count: int
        """
        self._detection_count = detection_count

    @property
    def high_risk_count(self):
        r"""Gets the high_risk_count of this BestPracticeOverviewItem.

        高风险项个数

        :return: The high_risk_count of this BestPracticeOverviewItem.
        :rtype: int
        """
        return self._high_risk_count

    @high_risk_count.setter
    def high_risk_count(self, high_risk_count):
        r"""Sets the high_risk_count of this BestPracticeOverviewItem.

        高风险项个数

        :param high_risk_count: The high_risk_count of this BestPracticeOverviewItem.
        :type high_risk_count: int
        """
        self._high_risk_count = high_risk_count

    @property
    def medium_risk_count(self):
        r"""Gets the medium_risk_count of this BestPracticeOverviewItem.

        中风险项个数

        :return: The medium_risk_count of this BestPracticeOverviewItem.
        :rtype: int
        """
        return self._medium_risk_count

    @medium_risk_count.setter
    def medium_risk_count(self, medium_risk_count):
        r"""Sets the medium_risk_count of this BestPracticeOverviewItem.

        中风险项个数

        :param medium_risk_count: The medium_risk_count of this BestPracticeOverviewItem.
        :type medium_risk_count: int
        """
        self._medium_risk_count = medium_risk_count

    @property
    def low_risk_count(self):
        r"""Gets the low_risk_count of this BestPracticeOverviewItem.

        低风险项个数

        :return: The low_risk_count of this BestPracticeOverviewItem.
        :rtype: int
        """
        return self._low_risk_count

    @low_risk_count.setter
    def low_risk_count(self, low_risk_count):
        r"""Sets the low_risk_count of this BestPracticeOverviewItem.

        低风险项个数

        :param low_risk_count: The low_risk_count of this BestPracticeOverviewItem.
        :type low_risk_count: int
        """
        self._low_risk_count = low_risk_count

    @property
    def risk_item_description(self):
        r"""Gets the risk_item_description of this BestPracticeOverviewItem.

        风险描述

        :return: The risk_item_description of this BestPracticeOverviewItem.
        :rtype: list[str]
        """
        return self._risk_item_description

    @risk_item_description.setter
    def risk_item_description(self, risk_item_description):
        r"""Sets the risk_item_description of this BestPracticeOverviewItem.

        风险描述

        :param risk_item_description: The risk_item_description of this BestPracticeOverviewItem.
        :type risk_item_description: list[str]
        """
        self._risk_item_description = risk_item_description

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
        if not isinstance(other, BestPracticeOverviewItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
