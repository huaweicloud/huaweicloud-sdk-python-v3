# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueConfigFieldsResponseBodyResultConfigFields:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'show': 'bool',
        'show_editable': 'bool',
        'optional': 'bool',
        'controlled': 'bool',
        'issue_roles': 'list[str]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'show': 'show',
        'show_editable': 'show_editable',
        'optional': 'optional',
        'controlled': 'controlled',
        'issue_roles': 'issue_roles'
    }

    def __init__(self, display_name=None, show=None, show_editable=None, optional=None, controlled=None, issue_roles=None):
        r"""IssueConfigFieldsResponseBodyResultConfigFields

        The model defined in huaweicloud sdk

        :param display_name: 查询结果
        :type display_name: str
        :param show: 是否显示
        :type show: bool
        :param show_editable: 是否可编辑
        :type show_editable: bool
        :param optional: 是否必填
        :type optional: bool
        :param controlled: 是否受控
        :type controlled: bool
        :param issue_roles: 可编辑的角色
        :type issue_roles: list[str]
        """
        
        

        self._display_name = None
        self._show = None
        self._show_editable = None
        self._optional = None
        self._controlled = None
        self._issue_roles = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if show is not None:
            self.show = show
        if show_editable is not None:
            self.show_editable = show_editable
        if optional is not None:
            self.optional = optional
        if controlled is not None:
            self.controlled = controlled
        if issue_roles is not None:
            self.issue_roles = issue_roles

    @property
    def display_name(self):
        r"""Gets the display_name of this IssueConfigFieldsResponseBodyResultConfigFields.

        查询结果

        :return: The display_name of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this IssueConfigFieldsResponseBodyResultConfigFields.

        查询结果

        :param display_name: The display_name of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def show(self):
        r"""Gets the show of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否显示

        :return: The show of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: bool
        """
        return self._show

    @show.setter
    def show(self, show):
        r"""Sets the show of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否显示

        :param show: The show of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type show: bool
        """
        self._show = show

    @property
    def show_editable(self):
        r"""Gets the show_editable of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否可编辑

        :return: The show_editable of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: bool
        """
        return self._show_editable

    @show_editable.setter
    def show_editable(self, show_editable):
        r"""Sets the show_editable of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否可编辑

        :param show_editable: The show_editable of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type show_editable: bool
        """
        self._show_editable = show_editable

    @property
    def optional(self):
        r"""Gets the optional of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否必填

        :return: The optional of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否必填

        :param optional: The optional of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type optional: bool
        """
        self._optional = optional

    @property
    def controlled(self):
        r"""Gets the controlled of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否受控

        :return: The controlled of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: bool
        """
        return self._controlled

    @controlled.setter
    def controlled(self, controlled):
        r"""Sets the controlled of this IssueConfigFieldsResponseBodyResultConfigFields.

        是否受控

        :param controlled: The controlled of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type controlled: bool
        """
        self._controlled = controlled

    @property
    def issue_roles(self):
        r"""Gets the issue_roles of this IssueConfigFieldsResponseBodyResultConfigFields.

        可编辑的角色

        :return: The issue_roles of this IssueConfigFieldsResponseBodyResultConfigFields.
        :rtype: list[str]
        """
        return self._issue_roles

    @issue_roles.setter
    def issue_roles(self, issue_roles):
        r"""Sets the issue_roles of this IssueConfigFieldsResponseBodyResultConfigFields.

        可编辑的角色

        :param issue_roles: The issue_roles of this IssueConfigFieldsResponseBodyResultConfigFields.
        :type issue_roles: list[str]
        """
        self._issue_roles = issue_roles

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
        if not isinstance(other, IssueConfigFieldsResponseBodyResultConfigFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
