# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructuredDocShareViewDTO:

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
        'creator': 'str',
        'modifier': 'str',
        'create_time': 'str',
        'last_update_time': 'str',
        'rdm_version': 'int',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'tenant': 'TenantViewDTO',
        'class_name': 'str',
        'structured_doc': 'StructuredDocView',
        'share_user_name': 'str',
        'shared_user_name': 'str',
        'shared_user_id': 'str',
        'auth_type': 'str',
        'share_user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'modifier': 'modifier',
        'create_time': 'createTime',
        'last_update_time': 'lastUpdateTime',
        'rdm_version': 'rdmVersion',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'class_name': 'className',
        'structured_doc': 'structuredDoc',
        'share_user_name': 'shareUserName',
        'shared_user_name': 'sharedUserName',
        'shared_user_id': 'sharedUserId',
        'auth_type': 'authType',
        'share_user_id': 'shareUserId'
    }

    def __init__(self, id=None, creator=None, modifier=None, create_time=None, last_update_time=None, rdm_version=None, rdm_delete_flag=None, rdm_extension_type=None, tenant=None, class_name=None, structured_doc=None, share_user_name=None, shared_user_name=None, shared_user_id=None, auth_type=None, share_user_id=None):
        r"""StructuredDocShareViewDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  唯一标识。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type id: str
        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type creator: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type create_time: str
        :param last_update_time: **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type last_update_time: str
        :param rdm_version: **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type rdm_version: int
        :param rdm_delete_flag: **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。
        :type rdm_delete_flag: int
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type class_name: str
        :param structured_doc: 
        :type structured_doc: :class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`
        :param share_user_name: **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type share_user_name: str
        :param shared_user_name: **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。
        :type shared_user_name: str
        :param shared_user_id: **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。
        :type shared_user_id: str
        :param auth_type: **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。
        :type auth_type: str
        :param share_user_id: **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。
        :type share_user_id: str
        """
        
        

        self._id = None
        self._creator = None
        self._modifier = None
        self._create_time = None
        self._last_update_time = None
        self._rdm_version = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._tenant = None
        self._class_name = None
        self._structured_doc = None
        self._share_user_name = None
        self._shared_user_name = None
        self._shared_user_id = None
        self._auth_type = None
        self._share_user_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        if modifier is not None:
            self.modifier = modifier
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if class_name is not None:
            self.class_name = class_name
        if structured_doc is not None:
            self.structured_doc = structured_doc
        if share_user_name is not None:
            self.share_user_name = share_user_name
        if shared_user_name is not None:
            self.shared_user_name = shared_user_name
        if shared_user_id is not None:
            self.shared_user_id = shared_user_id
        if auth_type is not None:
            self.auth_type = auth_type
        if share_user_id is not None:
            self.share_user_id = share_user_id

    @property
    def id(self):
        r"""Gets the id of this StructuredDocShareViewDTO.

        **参数解释**：  唯一标识。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The id of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StructuredDocShareViewDTO.

        **参数解释**：  唯一标识。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param id: The id of this StructuredDocShareViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def creator(self):
        r"""Gets the creator of this StructuredDocShareViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The creator of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this StructuredDocShareViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param creator: The creator of this StructuredDocShareViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def modifier(self):
        r"""Gets the modifier of this StructuredDocShareViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this StructuredDocShareViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this StructuredDocShareViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def create_time(self):
        r"""Gets the create_time of this StructuredDocShareViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The create_time of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StructuredDocShareViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param create_time: The create_time of this StructuredDocShareViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this StructuredDocShareViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The last_update_time of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this StructuredDocShareViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param last_update_time: The last_update_time of this StructuredDocShareViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this StructuredDocShareViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The rdm_version of this StructuredDocShareViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this StructuredDocShareViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param rdm_version: The rdm_version of this StructuredDocShareViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this StructuredDocShareViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。

        :return: The rdm_delete_flag of this StructuredDocShareViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this StructuredDocShareViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。

        :param rdm_delete_flag: The rdm_delete_flag of this StructuredDocShareViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this StructuredDocShareViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The rdm_extension_type of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this StructuredDocShareViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param rdm_extension_type: The rdm_extension_type of this StructuredDocShareViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        r"""Gets the tenant of this StructuredDocShareViewDTO.

        :return: The tenant of this StructuredDocShareViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this StructuredDocShareViewDTO.

        :param tenant: The tenant of this StructuredDocShareViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def class_name(self):
        r"""Gets the class_name of this StructuredDocShareViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The class_name of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this StructuredDocShareViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param class_name: The class_name of this StructuredDocShareViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def structured_doc(self):
        r"""Gets the structured_doc of this StructuredDocShareViewDTO.

        :return: The structured_doc of this StructuredDocShareViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`
        """
        return self._structured_doc

    @structured_doc.setter
    def structured_doc(self, structured_doc):
        r"""Sets the structured_doc of this StructuredDocShareViewDTO.

        :param structured_doc: The structured_doc of this StructuredDocShareViewDTO.
        :type structured_doc: :class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`
        """
        self._structured_doc = structured_doc

    @property
    def share_user_name(self):
        r"""Gets the share_user_name of this StructuredDocShareViewDTO.

        **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The share_user_name of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._share_user_name

    @share_user_name.setter
    def share_user_name(self, share_user_name):
        r"""Sets the share_user_name of this StructuredDocShareViewDTO.

        **参数解释**：  分享用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param share_user_name: The share_user_name of this StructuredDocShareViewDTO.
        :type share_user_name: str
        """
        self._share_user_name = share_user_name

    @property
    def shared_user_name(self):
        r"""Gets the shared_user_name of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :return: The shared_user_name of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._shared_user_name

    @shared_user_name.setter
    def shared_user_name(self, shared_user_name):
        r"""Sets the shared_user_name of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户名。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :param shared_user_name: The shared_user_name of this StructuredDocShareViewDTO.
        :type shared_user_name: str
        """
        self._shared_user_name = shared_user_name

    @property
    def shared_user_id(self):
        r"""Gets the shared_user_id of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :return: The shared_user_id of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._shared_user_id

    @shared_user_id.setter
    def shared_user_id(self, shared_user_id):
        r"""Sets the shared_user_id of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :param shared_user_id: The shared_user_id of this StructuredDocShareViewDTO.
        :type shared_user_id: str
        """
        self._shared_user_id = shared_user_id

    @property
    def auth_type(self):
        r"""Gets the auth_type of this StructuredDocShareViewDTO.

        **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。

        :return: The auth_type of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this StructuredDocShareViewDTO.

        **参数解释**：  认证类型。  **约束限制**：  不涉及。  **取值范围**：  - read：只读。 - write：读写。  **默认取值**：  不涉及。

        :param auth_type: The auth_type of this StructuredDocShareViewDTO.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def share_user_id(self):
        r"""Gets the share_user_id of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :return: The share_user_id of this StructuredDocShareViewDTO.
        :rtype: str
        """
        return self._share_user_id

    @share_user_id.setter
    def share_user_id(self, share_user_id):
        r"""Sets the share_user_id of this StructuredDocShareViewDTO.

        **参数解释**：  被分享用户UserId。  **约束限制**：  不涉及。  **取值范围**：  all：表示所有人。  **默认取值**：  不涉及。

        :param share_user_id: The share_user_id of this StructuredDocShareViewDTO.
        :type share_user_id: str
        """
        self._share_user_id = share_user_id

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
        if not isinstance(other, StructuredDocShareViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
