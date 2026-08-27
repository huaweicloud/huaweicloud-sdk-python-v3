# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUserGroupsNewReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'group_ids': 'list[str]',
        'language': 'str'
    }

    attribute_map = {
        'name': 'name',
        'group_ids': 'group_ids',
        'language': 'language'
    }

    def __init__(self, name=None, group_ids=None, language=None):
        r"""ExportUserGroupsNewReq

        The model defined in huaweicloud sdk

        :param name: 用户组名模糊查询关键字。
        :type name: str
        :param group_ids: 用户组ID列表。有传则与name过滤结果取交集。
        :type group_ids: list[str]
        :param language: 语言，用于Excel标题国际化。 * zh_CN： 中文 * en_US： 英文
        :type language: str
        """
        
        

        self._name = None
        self._group_ids = None
        self._language = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if group_ids is not None:
            self.group_ids = group_ids
        if language is not None:
            self.language = language

    @property
    def name(self):
        r"""Gets the name of this ExportUserGroupsNewReq.

        用户组名模糊查询关键字。

        :return: The name of this ExportUserGroupsNewReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExportUserGroupsNewReq.

        用户组名模糊查询关键字。

        :param name: The name of this ExportUserGroupsNewReq.
        :type name: str
        """
        self._name = name

    @property
    def group_ids(self):
        r"""Gets the group_ids of this ExportUserGroupsNewReq.

        用户组ID列表。有传则与name过滤结果取交集。

        :return: The group_ids of this ExportUserGroupsNewReq.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this ExportUserGroupsNewReq.

        用户组ID列表。有传则与name过滤结果取交集。

        :param group_ids: The group_ids of this ExportUserGroupsNewReq.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def language(self):
        r"""Gets the language of this ExportUserGroupsNewReq.

        语言，用于Excel标题国际化。 * zh_CN： 中文 * en_US： 英文

        :return: The language of this ExportUserGroupsNewReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportUserGroupsNewReq.

        语言，用于Excel标题国际化。 * zh_CN： 中文 * en_US： 英文

        :param language: The language of this ExportUserGroupsNewReq.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportUserGroupsNewReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
