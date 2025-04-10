# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TermAssignmentHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'int',
        'steward': 'str',
        'source': 'str',
        'status': 'str',
        'create_user': 'str',
        'expression': 'str',
        'display_text': 'str',
        'term_guid': 'str',
        'relation_guid': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'steward': 'steward',
        'source': 'source',
        'status': 'status',
        'create_user': 'create_user',
        'expression': 'expression',
        'display_text': 'display_text',
        'term_guid': 'term_guid',
        'relation_guid': 'relation_guid'
    }

    def __init__(self, confidence=None, steward=None, source=None, status=None, create_user=None, expression=None, display_text=None, term_guid=None, relation_guid=None):
        r"""TermAssignmentHeader

        The model defined in huaweicloud sdk

        :param confidence: 信任id
        :type confidence: int
        :param steward: 管理员
        :type steward: str
        :param source: 来源
        :type source: str
        :param status: 状态 枚举值：DISCOVERED、PROPOSED、IMPORTED、VALIDATED、DEPRECATED、OBSOLETE、OTHER
        :type status: str
        :param create_user: 创建人
        :type create_user: str
        :param expression: 表达式
        :type expression: str
        :param display_text: 展示信息
        :type display_text: str
        :param term_guid: 标签guid
        :type term_guid: str
        :param relation_guid: 关联guid
        :type relation_guid: str
        """
        
        

        self._confidence = None
        self._steward = None
        self._source = None
        self._status = None
        self._create_user = None
        self._expression = None
        self._display_text = None
        self._term_guid = None
        self._relation_guid = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if steward is not None:
            self.steward = steward
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if create_user is not None:
            self.create_user = create_user
        if expression is not None:
            self.expression = expression
        if display_text is not None:
            self.display_text = display_text
        if term_guid is not None:
            self.term_guid = term_guid
        if relation_guid is not None:
            self.relation_guid = relation_guid

    @property
    def confidence(self):
        r"""Gets the confidence of this TermAssignmentHeader.

        信任id

        :return: The confidence of this TermAssignmentHeader.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this TermAssignmentHeader.

        信任id

        :param confidence: The confidence of this TermAssignmentHeader.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def steward(self):
        r"""Gets the steward of this TermAssignmentHeader.

        管理员

        :return: The steward of this TermAssignmentHeader.
        :rtype: str
        """
        return self._steward

    @steward.setter
    def steward(self, steward):
        r"""Sets the steward of this TermAssignmentHeader.

        管理员

        :param steward: The steward of this TermAssignmentHeader.
        :type steward: str
        """
        self._steward = steward

    @property
    def source(self):
        r"""Gets the source of this TermAssignmentHeader.

        来源

        :return: The source of this TermAssignmentHeader.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this TermAssignmentHeader.

        来源

        :param source: The source of this TermAssignmentHeader.
        :type source: str
        """
        self._source = source

    @property
    def status(self):
        r"""Gets the status of this TermAssignmentHeader.

        状态 枚举值：DISCOVERED、PROPOSED、IMPORTED、VALIDATED、DEPRECATED、OBSOLETE、OTHER

        :return: The status of this TermAssignmentHeader.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TermAssignmentHeader.

        状态 枚举值：DISCOVERED、PROPOSED、IMPORTED、VALIDATED、DEPRECATED、OBSOLETE、OTHER

        :param status: The status of this TermAssignmentHeader.
        :type status: str
        """
        self._status = status

    @property
    def create_user(self):
        r"""Gets the create_user of this TermAssignmentHeader.

        创建人

        :return: The create_user of this TermAssignmentHeader.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this TermAssignmentHeader.

        创建人

        :param create_user: The create_user of this TermAssignmentHeader.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def expression(self):
        r"""Gets the expression of this TermAssignmentHeader.

        表达式

        :return: The expression of this TermAssignmentHeader.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this TermAssignmentHeader.

        表达式

        :param expression: The expression of this TermAssignmentHeader.
        :type expression: str
        """
        self._expression = expression

    @property
    def display_text(self):
        r"""Gets the display_text of this TermAssignmentHeader.

        展示信息

        :return: The display_text of this TermAssignmentHeader.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        r"""Sets the display_text of this TermAssignmentHeader.

        展示信息

        :param display_text: The display_text of this TermAssignmentHeader.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def term_guid(self):
        r"""Gets the term_guid of this TermAssignmentHeader.

        标签guid

        :return: The term_guid of this TermAssignmentHeader.
        :rtype: str
        """
        return self._term_guid

    @term_guid.setter
    def term_guid(self, term_guid):
        r"""Sets the term_guid of this TermAssignmentHeader.

        标签guid

        :param term_guid: The term_guid of this TermAssignmentHeader.
        :type term_guid: str
        """
        self._term_guid = term_guid

    @property
    def relation_guid(self):
        r"""Gets the relation_guid of this TermAssignmentHeader.

        关联guid

        :return: The relation_guid of this TermAssignmentHeader.
        :rtype: str
        """
        return self._relation_guid

    @relation_guid.setter
    def relation_guid(self, relation_guid):
        r"""Sets the relation_guid of this TermAssignmentHeader.

        关联guid

        :param relation_guid: The relation_guid of this TermAssignmentHeader.
        :type relation_guid: str
        """
        self._relation_guid = relation_guid

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
        if not isinstance(other, TermAssignmentHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
