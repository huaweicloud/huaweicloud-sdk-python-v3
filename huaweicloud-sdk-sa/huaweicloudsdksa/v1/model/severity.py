# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Severity:

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
        'normalize_score': 'int',
        'original_score': 'int'
    }

    attribute_map = {
        'label': 'label',
        'normalize_score': 'normalize_score',
        'original_score': 'original_score'
    }

    def __init__(self, label=None, normalize_score=None, original_score=None):
        r"""Severity

        The model defined in huaweicloud sdk

        :param label: 严重性等级取值范围：TIPS、LOW、MEDIUM、HIGH、FATAL。 TIPS：未发现任何问题。 LOW：无需针对问题执行任何操作。 MEDIUM：问题需要处理，但不紧急。 HIGH：问题必须优先处理。 FATAL：问题必须立即处理，以防止产生进一步的损害。
        :type label: str
        :param normalize_score: 严重性评分取值范围：0-100； 与严重性等级的对应关系： TIPS 0； LOW 1-39； MEDIUM 40-69； HIGH 70-89； FATAL 90-100。
        :type normalize_score: int
        :param original_score: 严重性原始评分，指在数据源产品中的评分。
        :type original_score: int
        """
        
        

        self._label = None
        self._normalize_score = None
        self._original_score = None
        self.discriminator = None

        self.label = label
        if normalize_score is not None:
            self.normalize_score = normalize_score
        if original_score is not None:
            self.original_score = original_score

    @property
    def label(self):
        r"""Gets the label of this Severity.

        严重性等级取值范围：TIPS、LOW、MEDIUM、HIGH、FATAL。 TIPS：未发现任何问题。 LOW：无需针对问题执行任何操作。 MEDIUM：问题需要处理，但不紧急。 HIGH：问题必须优先处理。 FATAL：问题必须立即处理，以防止产生进一步的损害。

        :return: The label of this Severity.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this Severity.

        严重性等级取值范围：TIPS、LOW、MEDIUM、HIGH、FATAL。 TIPS：未发现任何问题。 LOW：无需针对问题执行任何操作。 MEDIUM：问题需要处理，但不紧急。 HIGH：问题必须优先处理。 FATAL：问题必须立即处理，以防止产生进一步的损害。

        :param label: The label of this Severity.
        :type label: str
        """
        self._label = label

    @property
    def normalize_score(self):
        r"""Gets the normalize_score of this Severity.

        严重性评分取值范围：0-100； 与严重性等级的对应关系： TIPS 0； LOW 1-39； MEDIUM 40-69； HIGH 70-89； FATAL 90-100。

        :return: The normalize_score of this Severity.
        :rtype: int
        """
        return self._normalize_score

    @normalize_score.setter
    def normalize_score(self, normalize_score):
        r"""Sets the normalize_score of this Severity.

        严重性评分取值范围：0-100； 与严重性等级的对应关系： TIPS 0； LOW 1-39； MEDIUM 40-69； HIGH 70-89； FATAL 90-100。

        :param normalize_score: The normalize_score of this Severity.
        :type normalize_score: int
        """
        self._normalize_score = normalize_score

    @property
    def original_score(self):
        r"""Gets the original_score of this Severity.

        严重性原始评分，指在数据源产品中的评分。

        :return: The original_score of this Severity.
        :rtype: int
        """
        return self._original_score

    @original_score.setter
    def original_score(self, original_score):
        r"""Sets the original_score of this Severity.

        严重性原始评分，指在数据源产品中的评分。

        :param original_score: The original_score of this Severity.
        :type original_score: int
        """
        self._original_score = original_score

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
        if not isinstance(other, Severity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
