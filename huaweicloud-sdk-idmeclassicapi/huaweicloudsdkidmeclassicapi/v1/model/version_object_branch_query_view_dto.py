# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionObjectBranchQueryViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'class_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'id': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'rdm_extension_type': 'str',
        'tenant': 'TenantQueryViewDTO',
        'version': 'str'
    }

    attribute_map = {
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'version': 'version'
    }

    def __init__(self, class_name=None, create_time=None, creator=None, id=None, last_update_time=None, modifier=None, rdm_extension_type=None, tenant=None, version=None):
        r"""VersionObjectBranchQueryViewDTO

        The model defined in huaweicloud sdk

        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type class_name: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param id: **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param last_update_time: **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        :param version: **参数解释：**  版本号。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type version: str
        """
        
        

        self._class_name = None
        self._create_time = None
        self._creator = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._rdm_extension_type = None
        self._tenant = None
        self._version = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if version is not None:
            self.version = version

    @property
    def class_name(self):
        r"""Gets the class_name of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The class_name of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param class_name: The class_name of this VersionObjectBranchQueryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        r"""Gets the create_time of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this VersionObjectBranchQueryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this VersionObjectBranchQueryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def id(self):
        r"""Gets the id of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this VersionObjectBranchQueryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this VersionObjectBranchQueryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        r"""Gets the modifier of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this VersionObjectBranchQueryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this VersionObjectBranchQueryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        r"""Gets the tenant of this VersionObjectBranchQueryViewDTO.

        :return: The tenant of this VersionObjectBranchQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this VersionObjectBranchQueryViewDTO.

        :param tenant: The tenant of this VersionObjectBranchQueryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        self._tenant = tenant

    @property
    def version(self):
        r"""Gets the version of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  版本号。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The version of this VersionObjectBranchQueryViewDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VersionObjectBranchQueryViewDTO.

        **参数解释：**  版本号。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param version: The version of this VersionObjectBranchQueryViewDTO.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, VersionObjectBranchQueryViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
