# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueWithReasonVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'category': 'str',
        'title': 'str',
        'number': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'title': 'title',
        'number': 'number',
        'reason': 'reason'
    }

    def __init__(self, id=None, category=None, title=None, number=None, reason=None):
        r"""IssueWithReasonVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **取值范围**： 不涉及。
        :type id: str
        :param category: **参数解释**： 工作项类型。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug
        :type category: str
        :param title: **参数解释**： 工作项标题。  **取值范围**： 不涉及。
        :type title: str
        :param number: **参数解释**： 工作项唯一编码number。  **取值范围**： 不涉及。
        :type number: str
        :param reason: **参数解释**： 操作失败原因。  **取值范围**： 不涉及。
        :type reason: str
        """
        
        

        self._id = None
        self._category = None
        self._title = None
        self._number = None
        self._reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if title is not None:
            self.title = title
        if number is not None:
            self.number = number
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        r"""Gets the id of this IssueWithReasonVO.

        **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **取值范围**： 不涉及。

        :return: The id of this IssueWithReasonVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueWithReasonVO.

        **参数解释**： 工作项唯一ID。可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **取值范围**： 不涉及。

        :param id: The id of this IssueWithReasonVO.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this IssueWithReasonVO.

        **参数解释**： 工作项类型。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug

        :return: The category of this IssueWithReasonVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueWithReasonVO.

        **参数解释**： 工作项类型。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug

        :param category: The category of this IssueWithReasonVO.
        :type category: str
        """
        self._category = category

    @property
    def title(self):
        r"""Gets the title of this IssueWithReasonVO.

        **参数解释**： 工作项标题。  **取值范围**： 不涉及。

        :return: The title of this IssueWithReasonVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueWithReasonVO.

        **参数解释**： 工作项标题。  **取值范围**： 不涉及。

        :param title: The title of this IssueWithReasonVO.
        :type title: str
        """
        self._title = title

    @property
    def number(self):
        r"""Gets the number of this IssueWithReasonVO.

        **参数解释**： 工作项唯一编码number。  **取值范围**： 不涉及。

        :return: The number of this IssueWithReasonVO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueWithReasonVO.

        **参数解释**： 工作项唯一编码number。  **取值范围**： 不涉及。

        :param number: The number of this IssueWithReasonVO.
        :type number: str
        """
        self._number = number

    @property
    def reason(self):
        r"""Gets the reason of this IssueWithReasonVO.

        **参数解释**： 操作失败原因。  **取值范围**： 不涉及。

        :return: The reason of this IssueWithReasonVO.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this IssueWithReasonVO.

        **参数解释**： 操作失败原因。  **取值范围**： 不涉及。

        :param reason: The reason of this IssueWithReasonVO.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, IssueWithReasonVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
