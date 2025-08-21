# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestNoteDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'str',
        'severity': 'str',
        'assignee_id': 'str',
        'review_categories': 'str',
        'review_modules': 'str',
        'proposer_id': 'str',
        'resolved': 'bool'
    }

    attribute_map = {
        'body': 'body',
        'severity': 'severity',
        'assignee_id': 'assignee_id',
        'review_categories': 'review_categories',
        'review_modules': 'review_modules',
        'proposer_id': 'proposer_id',
        'resolved': 'resolved'
    }

    def __init__(self, body=None, severity=None, assignee_id=None, review_categories=None, review_modules=None, proposer_id=None, resolved=None):
        r"""UpdateMergeRequestNoteDto

        The model defined in huaweicloud sdk

        :param body: **参数解释：** 评论内容。  
        :type body: str
        :param severity: **参数解释：** 检视意见严重程度。
        :type severity: str
        :param assignee_id: **参数解释：** 检视意见指派人id。
        :type assignee_id: str
        :param review_categories: **参数解释：** 检视意见分类。
        :type review_categories: str
        :param review_modules: **参数解释：** 检视意见模块。
        :type review_modules: str
        :param proposer_id: **参数解释：** 检视意见检视人id。
        :type proposer_id: str
        :param resolved: **参数解释：** 解决或取消解决检视意见(使用时需仅传此参数)。
        :type resolved: bool
        """
        
        

        self._body = None
        self._severity = None
        self._assignee_id = None
        self._review_categories = None
        self._review_modules = None
        self._proposer_id = None
        self._resolved = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if severity is not None:
            self.severity = severity
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if review_categories is not None:
            self.review_categories = review_categories
        if review_modules is not None:
            self.review_modules = review_modules
        if proposer_id is not None:
            self.proposer_id = proposer_id
        if resolved is not None:
            self.resolved = resolved

    @property
    def body(self):
        r"""Gets the body of this UpdateMergeRequestNoteDto.

        **参数解释：** 评论内容。  

        :return: The body of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMergeRequestNoteDto.

        **参数解释：** 评论内容。  

        :param body: The body of this UpdateMergeRequestNoteDto.
        :type body: str
        """
        self._body = body

    @property
    def severity(self):
        r"""Gets the severity of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见严重程度。

        :return: The severity of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见严重程度。

        :param severity: The severity of this UpdateMergeRequestNoteDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def assignee_id(self):
        r"""Gets the assignee_id of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见指派人id。

        :return: The assignee_id of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        r"""Sets the assignee_id of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见指派人id。

        :param assignee_id: The assignee_id of this UpdateMergeRequestNoteDto.
        :type assignee_id: str
        """
        self._assignee_id = assignee_id

    @property
    def review_categories(self):
        r"""Gets the review_categories of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见分类。

        :return: The review_categories of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见分类。

        :param review_categories: The review_categories of this UpdateMergeRequestNoteDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_modules(self):
        r"""Gets the review_modules of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见模块。

        :return: The review_modules of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见模块。

        :param review_modules: The review_modules of this UpdateMergeRequestNoteDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def proposer_id(self):
        r"""Gets the proposer_id of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见检视人id。

        :return: The proposer_id of this UpdateMergeRequestNoteDto.
        :rtype: str
        """
        return self._proposer_id

    @proposer_id.setter
    def proposer_id(self, proposer_id):
        r"""Sets the proposer_id of this UpdateMergeRequestNoteDto.

        **参数解释：** 检视意见检视人id。

        :param proposer_id: The proposer_id of this UpdateMergeRequestNoteDto.
        :type proposer_id: str
        """
        self._proposer_id = proposer_id

    @property
    def resolved(self):
        r"""Gets the resolved of this UpdateMergeRequestNoteDto.

        **参数解释：** 解决或取消解决检视意见(使用时需仅传此参数)。

        :return: The resolved of this UpdateMergeRequestNoteDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        r"""Sets the resolved of this UpdateMergeRequestNoteDto.

        **参数解释：** 解决或取消解决检视意见(使用时需仅传此参数)。

        :param resolved: The resolved of this UpdateMergeRequestNoteDto.
        :type resolved: bool
        """
        self._resolved = resolved

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
        if not isinstance(other, UpdateMergeRequestNoteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
