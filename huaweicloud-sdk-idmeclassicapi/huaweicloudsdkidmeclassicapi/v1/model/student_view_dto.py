# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StudentViewDTO:

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
        'description': 'str',
        'grade': 'float',
        'id': 'str',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'name': 'str',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'rdm_version': 'int',
        'security_level': 'str',
        'tenant': 'TenantViewDTO'
    }

    attribute_map = {
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'grade': 'grade',
        'id': 'id',
        'kiaguid': 'kiaguid',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'name': 'name',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_version': 'rdmVersion',
        'security_level': 'securityLevel',
        'tenant': 'tenant'
    }

    def __init__(self, class_name=None, create_time=None, creator=None, description=None, grade=None, id=None, kiaguid=None, last_update_time=None, modifier=None, name=None, rdm_delete_flag=None, rdm_extension_type=None, rdm_version=None, security_level=None, tenant=None):
        r"""StudentViewDTO

        The model defined in huaweicloud sdk

        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type class_name: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param description: **参数解释：**  描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type description: str
        :param grade: **参数解释：**  成绩。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type grade: float
        :param id: **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param kiaguid: **参数解释：**  关键信息资产ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type kiaguid: str
        :param last_update_time: **参数解释：**  最新更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param name: **参数解释：**  名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type name: str
        :param rdm_delete_flag: **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。  - 1：表示已删除。  **默认取值：**  不涉及。 
        :type rdm_delete_flag: int
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param rdm_version: **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_version: int
        :param security_level: **参数解释：**  安全密级。  **取值范围：**  - INTERNAL：内部公开。  - SECRET：秘密。  - CONFIDENTIAL：机密。  - TOP_SECRET：绝密。  **默认取值：**  不涉及。 
        :type security_level: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        
        

        self._class_name = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._grade = None
        self._id = None
        self._kiaguid = None
        self._last_update_time = None
        self._modifier = None
        self._name = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._rdm_version = None
        self._security_level = None
        self._tenant = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if grade is not None:
            self.grade = grade
        if id is not None:
            self.id = id
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if security_level is not None:
            self.security_level = security_level
        if tenant is not None:
            self.tenant = tenant

    @property
    def class_name(self):
        r"""Gets the class_name of this StudentViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The class_name of this StudentViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this StudentViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param class_name: The class_name of this StudentViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        r"""Gets the create_time of this StudentViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this StudentViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StudentViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this StudentViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this StudentViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this StudentViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this StudentViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this StudentViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        r"""Gets the description of this StudentViewDTO.

        **参数解释：**  描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The description of this StudentViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StudentViewDTO.

        **参数解释：**  描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param description: The description of this StudentViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def grade(self):
        r"""Gets the grade of this StudentViewDTO.

        **参数解释：**  成绩。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The grade of this StudentViewDTO.
        :rtype: float
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        r"""Sets the grade of this StudentViewDTO.

        **参数解释：**  成绩。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param grade: The grade of this StudentViewDTO.
        :type grade: float
        """
        self._grade = grade

    @property
    def id(self):
        r"""Gets the id of this StudentViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this StudentViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StudentViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this StudentViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def kiaguid(self):
        r"""Gets the kiaguid of this StudentViewDTO.

        **参数解释：**  关键信息资产ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The kiaguid of this StudentViewDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        r"""Sets the kiaguid of this StudentViewDTO.

        **参数解释：**  关键信息资产ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param kiaguid: The kiaguid of this StudentViewDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this StudentViewDTO.

        **参数解释：**  最新更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this StudentViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this StudentViewDTO.

        **参数解释：**  最新更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this StudentViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        r"""Gets the modifier of this StudentViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this StudentViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this StudentViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this StudentViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        r"""Gets the name of this StudentViewDTO.

        **参数解释：**  名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The name of this StudentViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StudentViewDTO.

        **参数解释：**  名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param name: The name of this StudentViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this StudentViewDTO.

        **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。  - 1：表示已删除。  **默认取值：**  不涉及。 

        :return: The rdm_delete_flag of this StudentViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this StudentViewDTO.

        **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。  - 1：表示已删除。  **默认取值：**  不涉及。 

        :param rdm_delete_flag: The rdm_delete_flag of this StudentViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this StudentViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this StudentViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this StudentViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this StudentViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this StudentViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_version of this StudentViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this StudentViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_version: The rdm_version of this StudentViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def security_level(self):
        r"""Gets the security_level of this StudentViewDTO.

        **参数解释：**  安全密级。  **取值范围：**  - INTERNAL：内部公开。  - SECRET：秘密。  - CONFIDENTIAL：机密。  - TOP_SECRET：绝密。  **默认取值：**  不涉及。 

        :return: The security_level of this StudentViewDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this StudentViewDTO.

        **参数解释：**  安全密级。  **取值范围：**  - INTERNAL：内部公开。  - SECRET：秘密。  - CONFIDENTIAL：机密。  - TOP_SECRET：绝密。  **默认取值：**  不涉及。 

        :param security_level: The security_level of this StudentViewDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def tenant(self):
        r"""Gets the tenant of this StudentViewDTO.

        :return: The tenant of this StudentViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this StudentViewDTO.

        :param tenant: The tenant of this StudentViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

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
        if not isinstance(other, StudentViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
