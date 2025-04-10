# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetGroupResp:

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
        'external_id': 'str',
        'meta': 'MetaDto',
        'schemas': 'list[str]',
        'display_name': 'str',
        'members': 'list[MemberItemDto]'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId',
        'meta': 'meta',
        'schemas': 'schemas',
        'display_name': 'displayName',
        'members': 'members'
    }

    def __init__(self, id=None, external_id=None, meta=None, schemas=None, display_name=None, members=None):
        r"""GetGroupResp

        The model defined in huaweicloud sdk

        :param id: 用户组的全局唯一标识符（ID）
        :type id: str
        :param external_id: 外部标识符
        :type external_id: str
        :param meta: 
        :type meta: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        :param schemas: 概要
        :type schemas: list[str]
        :param display_name: 包含用户显示名称的字符串
        :type display_name: str
        :param members: 用户组中的成员对象列表
        :type members: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        """
        
        

        self._id = None
        self._external_id = None
        self._meta = None
        self._schemas = None
        self._display_name = None
        self._members = None
        self.discriminator = None

        self.id = id
        if external_id is not None:
            self.external_id = external_id
        if meta is not None:
            self.meta = meta
        if schemas is not None:
            self.schemas = schemas
        if display_name is not None:
            self.display_name = display_name
        if members is not None:
            self.members = members

    @property
    def id(self):
        r"""Gets the id of this GetGroupResp.

        用户组的全局唯一标识符（ID）

        :return: The id of this GetGroupResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetGroupResp.

        用户组的全局唯一标识符（ID）

        :param id: The id of this GetGroupResp.
        :type id: str
        """
        self._id = id

    @property
    def external_id(self):
        r"""Gets the external_id of this GetGroupResp.

        外部标识符

        :return: The external_id of this GetGroupResp.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this GetGroupResp.

        外部标识符

        :param external_id: The external_id of this GetGroupResp.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def meta(self):
        r"""Gets the meta of this GetGroupResp.

        :return: The meta of this GetGroupResp.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        r"""Sets the meta of this GetGroupResp.

        :param meta: The meta of this GetGroupResp.
        :type meta: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        self._meta = meta

    @property
    def schemas(self):
        r"""Gets the schemas of this GetGroupResp.

        概要

        :return: The schemas of this GetGroupResp.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this GetGroupResp.

        概要

        :param schemas: The schemas of this GetGroupResp.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def display_name(self):
        r"""Gets the display_name of this GetGroupResp.

        包含用户显示名称的字符串

        :return: The display_name of this GetGroupResp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this GetGroupResp.

        包含用户显示名称的字符串

        :param display_name: The display_name of this GetGroupResp.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def members(self):
        r"""Gets the members of this GetGroupResp.

        用户组中的成员对象列表

        :return: The members of this GetGroupResp.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this GetGroupResp.

        用户组中的成员对象列表

        :param members: The members of this GetGroupResp.
        :type members: list[:class:`huaweicloudsdkidentitycenterscim.v1.MemberItemDto`]
        """
        self._members = members

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
        if not isinstance(other, GetGroupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
