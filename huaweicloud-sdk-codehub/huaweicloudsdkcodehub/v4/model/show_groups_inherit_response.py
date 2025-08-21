# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupsInheritResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'source_setting': 'str',
        'project_id': 'str',
        'upward_inherit_editable': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'source_setting': 'source_setting',
        'project_id': 'project_id',
        'upward_inherit_editable': 'upward_inherit_editable'
    }

    def __init__(self, group_id=None, source_setting=None, project_id=None, upward_inherit_editable=None):
        r"""ShowGroupsInheritResponse

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type group_id: str
        :param source_setting: **参数解释：** 资源类型设置。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type source_setting: str
        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param upward_inherit_editable: **参数解释：** 向上继承是否可编辑。
        :type upward_inherit_editable: bool
        """
        
        super(ShowGroupsInheritResponse, self).__init__()

        self._group_id = None
        self._source_setting = None
        self._project_id = None
        self._upward_inherit_editable = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if source_setting is not None:
            self.source_setting = source_setting
        if project_id is not None:
            self.project_id = project_id
        if upward_inherit_editable is not None:
            self.upward_inherit_editable = upward_inherit_editable

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowGroupsInheritResponse.

        **参数解释：** 代码组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The group_id of this ShowGroupsInheritResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowGroupsInheritResponse.

        **参数解释：** 代码组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param group_id: The group_id of this ShowGroupsInheritResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def source_setting(self):
        r"""Gets the source_setting of this ShowGroupsInheritResponse.

        **参数解释：** 资源类型设置。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The source_setting of this ShowGroupsInheritResponse.
        :rtype: str
        """
        return self._source_setting

    @source_setting.setter
    def source_setting(self, source_setting):
        r"""Sets the source_setting of this ShowGroupsInheritResponse.

        **参数解释：** 资源类型设置。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param source_setting: The source_setting of this ShowGroupsInheritResponse.
        :type source_setting: str
        """
        self._source_setting = source_setting

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowGroupsInheritResponse.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this ShowGroupsInheritResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowGroupsInheritResponse.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this ShowGroupsInheritResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def upward_inherit_editable(self):
        r"""Gets the upward_inherit_editable of this ShowGroupsInheritResponse.

        **参数解释：** 向上继承是否可编辑。

        :return: The upward_inherit_editable of this ShowGroupsInheritResponse.
        :rtype: bool
        """
        return self._upward_inherit_editable

    @upward_inherit_editable.setter
    def upward_inherit_editable(self, upward_inherit_editable):
        r"""Sets the upward_inherit_editable of this ShowGroupsInheritResponse.

        **参数解释：** 向上继承是否可编辑。

        :param upward_inherit_editable: The upward_inherit_editable of this ShowGroupsInheritResponse.
        :type upward_inherit_editable: bool
        """
        self._upward_inherit_editable = upward_inherit_editable

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
        if not isinstance(other, ShowGroupsInheritResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
