# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpdIssueCommentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'issue_id': 'str',
        'date_desc': 'bool',
        'page_no': 'int',
        'page_size': 'int',
        'category': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id',
        'date_desc': 'date_desc',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'category': 'category'
    }

    def __init__(self, project_id=None, issue_id=None, date_desc=None, page_no=None, page_size=None, category=None):
        r"""ListIpdIssueCommentsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param issue_id: 工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type issue_id: str
        :param date_desc: **参数解释**： 是否按创建日期倒序排列。 **取值范围**： - true：按创建时间倒序排列。 - false：按创建时间正序排列。 **默认取值**： 不涉及。
        :type date_desc: bool
        :param page_no: **参数解释**： 分页索引。 **约束限制**： 不涉及 **取值范围**： 最小值1，最大值10000 **默认取值**： 1
        :type page_no: int
        :param page_size: **参数解释**： 分页大小。 **约束限制**： 不涉及 **取值范围**： 最小值5，最大值200 **默认取值**： 200
        :type page_size: int
        :param category: **参数解释**： 评论类型，支持多值，使用英文逗号分隔。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。
        :type category: str
        """
        
        

        self._project_id = None
        self._issue_id = None
        self._date_desc = None
        self._page_no = None
        self._page_size = None
        self._category = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id
        if date_desc is not None:
            self.date_desc = date_desc
        self.page_no = page_no
        self.page_size = page_size
        if category is not None:
            self.category = category

    @property
    def project_id(self):
        r"""Gets the project_id of this ListIpdIssueCommentsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ListIpdIssueCommentsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListIpdIssueCommentsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ListIpdIssueCommentsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this ListIpdIssueCommentsRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The issue_id of this ListIpdIssueCommentsRequest.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this ListIpdIssueCommentsRequest.

        工作项唯一ID。可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param issue_id: The issue_id of this ListIpdIssueCommentsRequest.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def date_desc(self):
        r"""Gets the date_desc of this ListIpdIssueCommentsRequest.

        **参数解释**： 是否按创建日期倒序排列。 **取值范围**： - true：按创建时间倒序排列。 - false：按创建时间正序排列。 **默认取值**： 不涉及。

        :return: The date_desc of this ListIpdIssueCommentsRequest.
        :rtype: bool
        """
        return self._date_desc

    @date_desc.setter
    def date_desc(self, date_desc):
        r"""Sets the date_desc of this ListIpdIssueCommentsRequest.

        **参数解释**： 是否按创建日期倒序排列。 **取值范围**： - true：按创建时间倒序排列。 - false：按创建时间正序排列。 **默认取值**： 不涉及。

        :param date_desc: The date_desc of this ListIpdIssueCommentsRequest.
        :type date_desc: bool
        """
        self._date_desc = date_desc

    @property
    def page_no(self):
        r"""Gets the page_no of this ListIpdIssueCommentsRequest.

        **参数解释**： 分页索引。 **约束限制**： 不涉及 **取值范围**： 最小值1，最大值10000 **默认取值**： 1

        :return: The page_no of this ListIpdIssueCommentsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListIpdIssueCommentsRequest.

        **参数解释**： 分页索引。 **约束限制**： 不涉及 **取值范围**： 最小值1，最大值10000 **默认取值**： 1

        :param page_no: The page_no of this ListIpdIssueCommentsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListIpdIssueCommentsRequest.

        **参数解释**： 分页大小。 **约束限制**： 不涉及 **取值范围**： 最小值5，最大值200 **默认取值**： 200

        :return: The page_size of this ListIpdIssueCommentsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListIpdIssueCommentsRequest.

        **参数解释**： 分页大小。 **约束限制**： 不涉及 **取值范围**： 最小值5，最大值200 **默认取值**： 200

        :param page_size: The page_size of this ListIpdIssueCommentsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def category(self):
        r"""Gets the category of this ListIpdIssueCommentsRequest.

        **参数解释**： 评论类型，支持多值，使用英文逗号分隔。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。

        :return: The category of this ListIpdIssueCommentsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListIpdIssueCommentsRequest.

        **参数解释**： 评论类型，支持多值，使用英文逗号分隔。 **取值范围**： - comment：评论 - reply：回复 - operation：系统操作。 **默认取值**： 不涉及。

        :param category: The category of this ListIpdIssueCommentsRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListIpdIssueCommentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
