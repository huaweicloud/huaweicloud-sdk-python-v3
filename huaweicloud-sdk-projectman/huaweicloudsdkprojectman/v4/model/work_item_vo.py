# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemVO:

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
        'title': 'str',
        'number': 'str',
        'category': 'str',
        'status': 'StatusVoIpd',
        'assignee': 'UserVO',
        'baseline': 'str',
        'change_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'number': 'number',
        'category': 'category',
        'status': 'status',
        'assignee': 'assignee',
        'baseline': 'baseline',
        'change_status': 'change_status'
    }

    def __init__(self, id=None, title=None, number=None, category=None, status=None, assignee=None, baseline=None, change_status=None):
        r"""WorkItemVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 工作项唯一ID。 **取值范围**： 不涉及。
        :type id: str
        :param title: **参数解释**： 工作项标题。 **取值范围**： 不涉及。
        :type title: str
        :param number: **参数解释**： 工作项编号。 **取值范围**： 不涉及。
        :type number: str
        :param category: **参数解释**： 工作项分类。 **取值范围**： 不涉及。
        :type category: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVoIpd`
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param baseline: **参数解释**： 工作项基线状态。 **取值范围**： - baselined：已基线 - unbaseline：未基线 - \&quot;\&quot;：未基线
        :type baseline: str
        :param change_status: **参数解释**： 工作项变更状态。 **取值范围**： - cannot_finish：不可完成
        :type change_status: str
        """
        
        

        self._id = None
        self._title = None
        self._number = None
        self._category = None
        self._status = None
        self._assignee = None
        self._baseline = None
        self._change_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if number is not None:
            self.number = number
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if assignee is not None:
            self.assignee = assignee
        if baseline is not None:
            self.baseline = baseline
        if change_status is not None:
            self.change_status = change_status

    @property
    def id(self):
        r"""Gets the id of this WorkItemVO.

        **参数解释**： 工作项唯一ID。 **取值范围**： 不涉及。

        :return: The id of this WorkItemVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemVO.

        **参数解释**： 工作项唯一ID。 **取值范围**： 不涉及。

        :param id: The id of this WorkItemVO.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this WorkItemVO.

        **参数解释**： 工作项标题。 **取值范围**： 不涉及。

        :return: The title of this WorkItemVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WorkItemVO.

        **参数解释**： 工作项标题。 **取值范围**： 不涉及。

        :param title: The title of this WorkItemVO.
        :type title: str
        """
        self._title = title

    @property
    def number(self):
        r"""Gets the number of this WorkItemVO.

        **参数解释**： 工作项编号。 **取值范围**： 不涉及。

        :return: The number of this WorkItemVO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this WorkItemVO.

        **参数解释**： 工作项编号。 **取值范围**： 不涉及。

        :param number: The number of this WorkItemVO.
        :type number: str
        """
        self._number = number

    @property
    def category(self):
        r"""Gets the category of this WorkItemVO.

        **参数解释**： 工作项分类。 **取值范围**： 不涉及。

        :return: The category of this WorkItemVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this WorkItemVO.

        **参数解释**： 工作项分类。 **取值范围**： 不涉及。

        :param category: The category of this WorkItemVO.
        :type category: str
        """
        self._category = category

    @property
    def status(self):
        r"""Gets the status of this WorkItemVO.

        :return: The status of this WorkItemVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusVoIpd`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkItemVO.

        :param status: The status of this WorkItemVO.
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVoIpd`
        """
        self._status = status

    @property
    def assignee(self):
        r"""Gets the assignee of this WorkItemVO.

        :return: The assignee of this WorkItemVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this WorkItemVO.

        :param assignee: The assignee of this WorkItemVO.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._assignee = assignee

    @property
    def baseline(self):
        r"""Gets the baseline of this WorkItemVO.

        **参数解释**： 工作项基线状态。 **取值范围**： - baselined：已基线 - unbaseline：未基线 - \"\"：未基线

        :return: The baseline of this WorkItemVO.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this WorkItemVO.

        **参数解释**： 工作项基线状态。 **取值范围**： - baselined：已基线 - unbaseline：未基线 - \"\"：未基线

        :param baseline: The baseline of this WorkItemVO.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def change_status(self):
        r"""Gets the change_status of this WorkItemVO.

        **参数解释**： 工作项变更状态。 **取值范围**： - cannot_finish：不可完成

        :return: The change_status of this WorkItemVO.
        :rtype: str
        """
        return self._change_status

    @change_status.setter
    def change_status(self, change_status):
        r"""Sets the change_status of this WorkItemVO.

        **参数解释**： 工作项变更状态。 **取值范围**： - cannot_finish：不可完成

        :param change_status: The change_status of this WorkItemVO.
        :type change_status: str
        """
        self._change_status = change_status

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
        if not isinstance(other, WorkItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
