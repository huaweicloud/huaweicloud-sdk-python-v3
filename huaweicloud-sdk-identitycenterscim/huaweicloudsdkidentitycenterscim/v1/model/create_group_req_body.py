# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_id': 'str',
        'display_name': 'str',
        'members': 'list[MemberItemDto]',
        'schemas': 'list[str]'
    }

    attribute_map = {
        'external_id': 'externalId',
        'display_name': 'displayName',
        'members': 'members',
        'schemas': 'schemas'
    }

    def __init__(self, external_id=None, display_name=None, members=None, schemas=None):
        r"""CreateGroupReqBody

        The model defined in huaweicloud sdk

        :param external_id: 外部标识符
        :type external_id: str
        :param display_name: 包含用户组显示名称的字符串
        :type display_name: str
        :param members: 用户组中的成员对象列表
        :type members: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        :param schemas: 概要
        :type schemas: list[str]
        """
        
        

        self._external_id = None
        self._display_name = None
        self._members = None
        self._schemas = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        self.display_name = display_name
        if members is not None:
            self.members = members
        self.schemas = schemas

    @property
    def external_id(self):
        r"""Gets the external_id of this CreateGroupReqBody.

        外部标识符

        :return: The external_id of this CreateGroupReqBody.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this CreateGroupReqBody.

        外部标识符

        :param external_id: The external_id of this CreateGroupReqBody.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateGroupReqBody.

        包含用户组显示名称的字符串

        :return: The display_name of this CreateGroupReqBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateGroupReqBody.

        包含用户组显示名称的字符串

        :param display_name: The display_name of this CreateGroupReqBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def members(self):
        r"""Gets the members of this CreateGroupReqBody.

        用户组中的成员对象列表

        :return: The members of this CreateGroupReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this CreateGroupReqBody.

        用户组中的成员对象列表

        :param members: The members of this CreateGroupReqBody.
        :type members: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        """
        self._members = members

    @property
    def schemas(self):
        r"""Gets the schemas of this CreateGroupReqBody.

        概要

        :return: The schemas of this CreateGroupReqBody.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this CreateGroupReqBody.

        概要

        :param schemas: The schemas of this CreateGroupReqBody.
        :type schemas: list[str]
        """
        self._schemas = schemas

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
        if not isinstance(other, CreateGroupReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
