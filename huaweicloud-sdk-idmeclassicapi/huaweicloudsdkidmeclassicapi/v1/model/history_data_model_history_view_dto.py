# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryDataModelHistoryViewDTO:

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
        'create_time': 'str',
        'modifier': 'str',
        'last_update_time': 'str',
        'rdm_version': 'int',
        'rdm_operation_type': 'str',
        'rdm_extension_type': 'str',
        'rdm_delete_flag': 'int',
        'tenant': 'TenantHistoryViewDTO',
        'class_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'create_time': 'createTime',
        'modifier': 'modifier',
        'last_update_time': 'lastUpdateTime',
        'rdm_version': 'rdmVersion',
        'rdm_operation_type': 'rdmOperationType',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'tenant': 'tenant',
        'class_name': 'className'
    }

    def __init__(self, id=None, creator=None, create_time=None, modifier=None, last_update_time=None, rdm_version=None, rdm_operation_type=None, rdm_extension_type=None, rdm_delete_flag=None, tenant=None, class_name=None):
        r"""HistoryDataModelHistoryViewDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param creator: **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param last_update_time: **参数解释：**  修改时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param rdm_version: **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_version: int
        :param rdm_operation_type: **参数解释：**  操作类型。  **取值范围：**  - CREATE：创建操作。 - UPDATE：更新操作。 - LOGICALDELETE：软删除操作。 - DELETE：删除操作。 - CASCADE：级联操作。  **默认取值：**  不涉及。 
        :type rdm_operation_type: str
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param rdm_delete_flag: **参数解释：**  删除标志。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_delete_flag: int
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantHistoryViewDTO`
        :param class_name: **参数解释：**  类名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type class_name: str
        """
        
        

        self._id = None
        self._creator = None
        self._create_time = None
        self._modifier = None
        self._last_update_time = None
        self._rdm_version = None
        self._rdm_operation_type = None
        self._rdm_extension_type = None
        self._rdm_delete_flag = None
        self._tenant = None
        self._class_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if modifier is not None:
            self.modifier = modifier
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if rdm_operation_type is not None:
            self.rdm_operation_type = rdm_operation_type
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if tenant is not None:
            self.tenant = tenant
        if class_name is not None:
            self.class_name = class_name

    @property
    def id(self):
        r"""Gets the id of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this HistoryDataModelHistoryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def creator(self):
        r"""Gets the creator of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this HistoryDataModelHistoryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this HistoryDataModelHistoryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modifier(self):
        r"""Gets the modifier of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this HistoryDataModelHistoryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  修改时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  修改时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this HistoryDataModelHistoryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_version of this HistoryDataModelHistoryViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_version: The rdm_version of this HistoryDataModelHistoryViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def rdm_operation_type(self):
        r"""Gets the rdm_operation_type of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  操作类型。  **取值范围：**  - CREATE：创建操作。 - UPDATE：更新操作。 - LOGICALDELETE：软删除操作。 - DELETE：删除操作。 - CASCADE：级联操作。  **默认取值：**  不涉及。 

        :return: The rdm_operation_type of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._rdm_operation_type

    @rdm_operation_type.setter
    def rdm_operation_type(self, rdm_operation_type):
        r"""Sets the rdm_operation_type of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  操作类型。  **取值范围：**  - CREATE：创建操作。 - UPDATE：更新操作。 - LOGICALDELETE：软删除操作。 - DELETE：删除操作。 - CASCADE：级联操作。  **默认取值：**  不涉及。 

        :param rdm_operation_type: The rdm_operation_type of this HistoryDataModelHistoryViewDTO.
        :type rdm_operation_type: str
        """
        self._rdm_operation_type = rdm_operation_type

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this HistoryDataModelHistoryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  删除标志。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_delete_flag of this HistoryDataModelHistoryViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  删除标志。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_delete_flag: The rdm_delete_flag of this HistoryDataModelHistoryViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def tenant(self):
        r"""Gets the tenant of this HistoryDataModelHistoryViewDTO.

        :return: The tenant of this HistoryDataModelHistoryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantHistoryViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this HistoryDataModelHistoryViewDTO.

        :param tenant: The tenant of this HistoryDataModelHistoryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantHistoryViewDTO`
        """
        self._tenant = tenant

    @property
    def class_name(self):
        r"""Gets the class_name of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  类名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The class_name of this HistoryDataModelHistoryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this HistoryDataModelHistoryViewDTO.

        **参数解释：**  类名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param class_name: The class_name of this HistoryDataModelHistoryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

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
        if not isinstance(other, HistoryDataModelHistoryViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
