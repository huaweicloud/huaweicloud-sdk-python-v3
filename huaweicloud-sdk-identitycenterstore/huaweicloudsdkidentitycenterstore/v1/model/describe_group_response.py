# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'display_name': 'str',
        'external_id': 'str',
        'external_ids': 'list[ExternalIdDto]',
        'group_id': 'str',
        'identity_store_id': 'str',
        'created_at': 'int',
        'created_by': 'str',
        'updated_at': 'int',
        'updated_by': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'external_id': 'external_id',
        'external_ids': 'external_ids',
        'group_id': 'group_id',
        'identity_store_id': 'identity_store_id',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'updated_at': 'updated_at',
        'updated_by': 'updated_by'
    }

    def __init__(self, description=None, display_name=None, external_id=None, external_ids=None, group_id=None, identity_store_id=None, created_at=None, created_by=None, updated_at=None, updated_by=None):
        r"""DescribeGroupResponse

        The model defined in huaweicloud sdk

        :param description: 包含组描述的字符串
        :type description: str
        :param display_name: 包含组显示名称的字符串
        :type display_name: str
        :param external_id: 外部身份源分配给此资源的标识符
        :type external_id: str
        :param external_ids: 包含外部身份提供商颁发给此资源的标识符的对象列表
        :type external_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        :param group_id: 身份源中IdentityCenter用户组的全局唯一标识符（ID）
        :type group_id: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param created_at: 创建时的时间戳
        :type created_at: int
        :param created_by: 创建者
        :type created_by: str
        :param updated_at: 更新时的时间戳
        :type updated_at: int
        :param updated_by: 更新者
        :type updated_by: str
        """
        
        super(DescribeGroupResponse, self).__init__()

        self._description = None
        self._display_name = None
        self._external_id = None
        self._external_ids = None
        self._group_id = None
        self._identity_store_id = None
        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._updated_by = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if external_id is not None:
            self.external_id = external_id
        if external_ids is not None:
            self.external_ids = external_ids
        if group_id is not None:
            self.group_id = group_id
        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def description(self):
        r"""Gets the description of this DescribeGroupResponse.

        包含组描述的字符串

        :return: The description of this DescribeGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DescribeGroupResponse.

        包含组描述的字符串

        :param description: The description of this DescribeGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        r"""Gets the display_name of this DescribeGroupResponse.

        包含组显示名称的字符串

        :return: The display_name of this DescribeGroupResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this DescribeGroupResponse.

        包含组显示名称的字符串

        :param display_name: The display_name of this DescribeGroupResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def external_id(self):
        r"""Gets the external_id of this DescribeGroupResponse.

        外部身份源分配给此资源的标识符

        :return: The external_id of this DescribeGroupResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this DescribeGroupResponse.

        外部身份源分配给此资源的标识符

        :param external_id: The external_id of this DescribeGroupResponse.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def external_ids(self):
        r"""Gets the external_ids of this DescribeGroupResponse.

        包含外部身份提供商颁发给此资源的标识符的对象列表

        :return: The external_ids of this DescribeGroupResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        r"""Sets the external_ids of this DescribeGroupResponse.

        包含外部身份提供商颁发给此资源的标识符的对象列表

        :param external_ids: The external_ids of this DescribeGroupResponse.
        :type external_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        self._external_ids = external_ids

    @property
    def group_id(self):
        r"""Gets the group_id of this DescribeGroupResponse.

        身份源中IdentityCenter用户组的全局唯一标识符（ID）

        :return: The group_id of this DescribeGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DescribeGroupResponse.

        身份源中IdentityCenter用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this DescribeGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this DescribeGroupResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this DescribeGroupResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this DescribeGroupResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this DescribeGroupResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def created_at(self):
        r"""Gets the created_at of this DescribeGroupResponse.

        创建时的时间戳

        :return: The created_at of this DescribeGroupResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DescribeGroupResponse.

        创建时的时间戳

        :param created_at: The created_at of this DescribeGroupResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def created_by(self):
        r"""Gets the created_by of this DescribeGroupResponse.

        创建者

        :return: The created_by of this DescribeGroupResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this DescribeGroupResponse.

        创建者

        :param created_by: The created_by of this DescribeGroupResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DescribeGroupResponse.

        更新时的时间戳

        :return: The updated_at of this DescribeGroupResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DescribeGroupResponse.

        更新时的时间戳

        :param updated_at: The updated_at of this DescribeGroupResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def updated_by(self):
        r"""Gets the updated_by of this DescribeGroupResponse.

        更新者

        :return: The updated_by of this DescribeGroupResponse.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this DescribeGroupResponse.

        更新者

        :param updated_by: The updated_by of this DescribeGroupResponse.
        :type updated_by: str
        """
        self._updated_by = updated_by

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
        if not isinstance(other, DescribeGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
