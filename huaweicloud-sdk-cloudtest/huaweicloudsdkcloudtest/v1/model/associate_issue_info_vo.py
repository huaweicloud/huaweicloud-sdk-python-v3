# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateIssueInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associate': 'bool',
        'issue_id': 'str',
        'tracker_id': 'str',
        'board_id': 'str',
        'tracker_name': 'str'
    }

    attribute_map = {
        'associate': 'associate',
        'issue_id': 'issue_id',
        'tracker_id': 'tracker_id',
        'board_id': 'board_id',
        'tracker_name': 'tracker_name'
    }

    def __init__(self, associate=None, issue_id=None, tracker_id=None, board_id=None, tracker_name=None):
        r"""AssociateIssueInfoVo

        The model defined in huaweicloud sdk

        :param associate: 是否已关联
        :type associate: bool
        :param issue_id: 需求ID
        :type issue_id: str
        :param tracker_id: 需求类型
        :type tracker_id: str
        :param board_id: 工作项层级ID
        :type board_id: str
        :param tracker_name: 需求类型名称
        :type tracker_name: str
        """
        
        

        self._associate = None
        self._issue_id = None
        self._tracker_id = None
        self._board_id = None
        self._tracker_name = None
        self.discriminator = None

        if associate is not None:
            self.associate = associate
        if issue_id is not None:
            self.issue_id = issue_id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if board_id is not None:
            self.board_id = board_id
        if tracker_name is not None:
            self.tracker_name = tracker_name

    @property
    def associate(self):
        r"""Gets the associate of this AssociateIssueInfoVo.

        是否已关联

        :return: The associate of this AssociateIssueInfoVo.
        :rtype: bool
        """
        return self._associate

    @associate.setter
    def associate(self, associate):
        r"""Sets the associate of this AssociateIssueInfoVo.

        是否已关联

        :param associate: The associate of this AssociateIssueInfoVo.
        :type associate: bool
        """
        self._associate = associate

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AssociateIssueInfoVo.

        需求ID

        :return: The issue_id of this AssociateIssueInfoVo.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AssociateIssueInfoVo.

        需求ID

        :param issue_id: The issue_id of this AssociateIssueInfoVo.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this AssociateIssueInfoVo.

        需求类型

        :return: The tracker_id of this AssociateIssueInfoVo.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this AssociateIssueInfoVo.

        需求类型

        :param tracker_id: The tracker_id of this AssociateIssueInfoVo.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def board_id(self):
        r"""Gets the board_id of this AssociateIssueInfoVo.

        工作项层级ID

        :return: The board_id of this AssociateIssueInfoVo.
        :rtype: str
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        r"""Sets the board_id of this AssociateIssueInfoVo.

        工作项层级ID

        :param board_id: The board_id of this AssociateIssueInfoVo.
        :type board_id: str
        """
        self._board_id = board_id

    @property
    def tracker_name(self):
        r"""Gets the tracker_name of this AssociateIssueInfoVo.

        需求类型名称

        :return: The tracker_name of this AssociateIssueInfoVo.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        r"""Sets the tracker_name of this AssociateIssueInfoVo.

        需求类型名称

        :param tracker_name: The tracker_name of this AssociateIssueInfoVo.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

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
        if not isinstance(other, AssociateIssueInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
