# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDiagnosisResultDiagnosisResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item': 'QueryDiagnosisResultItem',
        'state': 'str',
        'result_list': 'list[QueryDiagnosisResultResultList]',
        'suggestion_list': 'list[QueryDiagnosisResultSuggestionList]',
        'score': 'int',
        'time': 'str'
    }

    attribute_map = {
        'item': 'item',
        'state': 'state',
        'result_list': 'result_list',
        'suggestion_list': 'suggestion_list',
        'score': 'score',
        'time': 'time'
    }

    def __init__(self, item=None, state=None, result_list=None, suggestion_list=None, score=None, time=None):
        r"""QueryDiagnosisResultDiagnosisResults

        The model defined in huaweicloud sdk

        :param item: 
        :type item: :class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultItem`
        :param state: 诊断项状态。
        :type state: str
        :param result_list: 诊断结果。
        :type result_list: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultResultList`]
        :param suggestion_list: 诊断建议。
        :type suggestion_list: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultSuggestionList`]
        :param score: 诊断项得分。
        :type score: int
        :param time: 完成时间。
        :type time: str
        """
        
        

        self._item = None
        self._state = None
        self._result_list = None
        self._suggestion_list = None
        self._score = None
        self._time = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if state is not None:
            self.state = state
        if result_list is not None:
            self.result_list = result_list
        if suggestion_list is not None:
            self.suggestion_list = suggestion_list
        if score is not None:
            self.score = score
        if time is not None:
            self.time = time

    @property
    def item(self):
        r"""Gets the item of this QueryDiagnosisResultDiagnosisResults.

        :return: The item of this QueryDiagnosisResultDiagnosisResults.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultItem`
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this QueryDiagnosisResultDiagnosisResults.

        :param item: The item of this QueryDiagnosisResultDiagnosisResults.
        :type item: :class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultItem`
        """
        self._item = item

    @property
    def state(self):
        r"""Gets the state of this QueryDiagnosisResultDiagnosisResults.

        诊断项状态。

        :return: The state of this QueryDiagnosisResultDiagnosisResults.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this QueryDiagnosisResultDiagnosisResults.

        诊断项状态。

        :param state: The state of this QueryDiagnosisResultDiagnosisResults.
        :type state: str
        """
        self._state = state

    @property
    def result_list(self):
        r"""Gets the result_list of this QueryDiagnosisResultDiagnosisResults.

        诊断结果。

        :return: The result_list of this QueryDiagnosisResultDiagnosisResults.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultResultList`]
        """
        return self._result_list

    @result_list.setter
    def result_list(self, result_list):
        r"""Sets the result_list of this QueryDiagnosisResultDiagnosisResults.

        诊断结果。

        :param result_list: The result_list of this QueryDiagnosisResultDiagnosisResults.
        :type result_list: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultResultList`]
        """
        self._result_list = result_list

    @property
    def suggestion_list(self):
        r"""Gets the suggestion_list of this QueryDiagnosisResultDiagnosisResults.

        诊断建议。

        :return: The suggestion_list of this QueryDiagnosisResultDiagnosisResults.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultSuggestionList`]
        """
        return self._suggestion_list

    @suggestion_list.setter
    def suggestion_list(self, suggestion_list):
        r"""Sets the suggestion_list of this QueryDiagnosisResultDiagnosisResults.

        诊断建议。

        :param suggestion_list: The suggestion_list of this QueryDiagnosisResultDiagnosisResults.
        :type suggestion_list: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultSuggestionList`]
        """
        self._suggestion_list = suggestion_list

    @property
    def score(self):
        r"""Gets the score of this QueryDiagnosisResultDiagnosisResults.

        诊断项得分。

        :return: The score of this QueryDiagnosisResultDiagnosisResults.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this QueryDiagnosisResultDiagnosisResults.

        诊断项得分。

        :param score: The score of this QueryDiagnosisResultDiagnosisResults.
        :type score: int
        """
        self._score = score

    @property
    def time(self):
        r"""Gets the time of this QueryDiagnosisResultDiagnosisResults.

        完成时间。

        :return: The time of this QueryDiagnosisResultDiagnosisResults.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this QueryDiagnosisResultDiagnosisResults.

        完成时间。

        :param time: The time of this QueryDiagnosisResultDiagnosisResults.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, QueryDiagnosisResultDiagnosisResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
