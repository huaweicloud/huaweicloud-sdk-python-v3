# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectMemberSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'sync_enabled': 'bool',
        'sync_all_role_enabled': 'bool',
        'role_sync': 'list[RoleSyncDto]'
    }

    attribute_map = {
        'product_id': 'product_id',
        'sync_enabled': 'sync_enabled',
        'sync_all_role_enabled': 'sync_all_role_enabled',
        'role_sync': 'role_sync'
    }

    def __init__(self, product_id=None, sync_enabled=None, sync_all_role_enabled=None, role_sync=None):
        r"""ShowProjectMemberSettingResponse

        The model defined in huaweicloud sdk

        :param product_id: **参数解释：** 项目id **取值范围：** 字符串长度不少于1，不超过1000。
        :type product_id: str
        :param sync_enabled: **参数解释：** 同步开关
        :type sync_enabled: bool
        :param sync_all_role_enabled: **参数解释：** 同步所有角色开关
        :type sync_all_role_enabled: bool
        :param role_sync: **参数解释：** 角色同步
        :type role_sync: list[:class:`huaweicloudsdkcodehub.v4.RoleSyncDto`]
        """
        
        super(ShowProjectMemberSettingResponse, self).__init__()

        self._product_id = None
        self._sync_enabled = None
        self._sync_all_role_enabled = None
        self._role_sync = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if sync_enabled is not None:
            self.sync_enabled = sync_enabled
        if sync_all_role_enabled is not None:
            self.sync_all_role_enabled = sync_all_role_enabled
        if role_sync is not None:
            self.role_sync = role_sync

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowProjectMemberSettingResponse.

        **参数解释：** 项目id **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The product_id of this ShowProjectMemberSettingResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowProjectMemberSettingResponse.

        **参数解释：** 项目id **取值范围：** 字符串长度不少于1，不超过1000。

        :param product_id: The product_id of this ShowProjectMemberSettingResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def sync_enabled(self):
        r"""Gets the sync_enabled of this ShowProjectMemberSettingResponse.

        **参数解释：** 同步开关

        :return: The sync_enabled of this ShowProjectMemberSettingResponse.
        :rtype: bool
        """
        return self._sync_enabled

    @sync_enabled.setter
    def sync_enabled(self, sync_enabled):
        r"""Sets the sync_enabled of this ShowProjectMemberSettingResponse.

        **参数解释：** 同步开关

        :param sync_enabled: The sync_enabled of this ShowProjectMemberSettingResponse.
        :type sync_enabled: bool
        """
        self._sync_enabled = sync_enabled

    @property
    def sync_all_role_enabled(self):
        r"""Gets the sync_all_role_enabled of this ShowProjectMemberSettingResponse.

        **参数解释：** 同步所有角色开关

        :return: The sync_all_role_enabled of this ShowProjectMemberSettingResponse.
        :rtype: bool
        """
        return self._sync_all_role_enabled

    @sync_all_role_enabled.setter
    def sync_all_role_enabled(self, sync_all_role_enabled):
        r"""Sets the sync_all_role_enabled of this ShowProjectMemberSettingResponse.

        **参数解释：** 同步所有角色开关

        :param sync_all_role_enabled: The sync_all_role_enabled of this ShowProjectMemberSettingResponse.
        :type sync_all_role_enabled: bool
        """
        self._sync_all_role_enabled = sync_all_role_enabled

    @property
    def role_sync(self):
        r"""Gets the role_sync of this ShowProjectMemberSettingResponse.

        **参数解释：** 角色同步

        :return: The role_sync of this ShowProjectMemberSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RoleSyncDto`]
        """
        return self._role_sync

    @role_sync.setter
    def role_sync(self, role_sync):
        r"""Sets the role_sync of this ShowProjectMemberSettingResponse.

        **参数解释：** 角色同步

        :param role_sync: The role_sync of this ShowProjectMemberSettingResponse.
        :type role_sync: list[:class:`huaweicloudsdkcodehub.v4.RoleSyncDto`]
        """
        self._role_sync = role_sync

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
        if not isinstance(other, ShowProjectMemberSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
