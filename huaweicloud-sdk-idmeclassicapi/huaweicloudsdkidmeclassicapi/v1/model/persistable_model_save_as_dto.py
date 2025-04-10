# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistableModelSaveAsDTO:

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
        'modifier': 'str',
        'last_update_time': 'str',
        'creator': 'str',
        'create_time': 'str',
        'rdm_extension_type': 'str',
        'tenant': 'ObjectReferenceParamDTO',
        'source_entity_number': 'str',
        'source_instance_id': 'str',
        'need_set_null_attrs': 'list[str]',
        'entity_to_save': 'object',
        'entity_to_return': 'object',
        'unique_key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'modifier': 'modifier',
        'last_update_time': 'lastUpdateTime',
        'creator': 'creator',
        'create_time': 'createTime',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'source_entity_number': 'sourceEntityNumber',
        'source_instance_id': 'sourceInstanceId',
        'need_set_null_attrs': 'needSetNullAttrs',
        'entity_to_save': 'entityToSave',
        'entity_to_return': 'entityToReturn',
        'unique_key': 'uniqueKey'
    }

    def __init__(self, id=None, modifier=None, last_update_time=None, creator=None, create_time=None, rdm_extension_type=None, tenant=None, source_entity_number=None, source_instance_id=None, need_set_null_attrs=None, entity_to_save=None, entity_to_return=None, unique_key=None):
        r"""PersistableModelSaveAsDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param modifier: **参数解释：**  修改者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param last_update_time: **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param creator: **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param create_time: **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param rdm_extension_type: **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param source_entity_number: **参数解释：**  源模型编号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type source_entity_number: str
        :param source_instance_id: **参数解释：**  源实例的唯一标识（单实例为ID，版本实例为versionId）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type source_instance_id: str
        :param need_set_null_attrs: **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type need_set_null_attrs: list[str]
        :param entity_to_save: **参数解释：**  要保存的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type entity_to_save: object
        :param entity_to_return: **参数解释：**  要保存的结果。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type entity_to_return: object
        :param unique_key: **参数解释：**  唯一键约束属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type unique_key: str
        """
        
        

        self._id = None
        self._modifier = None
        self._last_update_time = None
        self._creator = None
        self._create_time = None
        self._rdm_extension_type = None
        self._tenant = None
        self._source_entity_number = None
        self._source_instance_id = None
        self._need_set_null_attrs = None
        self._entity_to_save = None
        self._entity_to_return = None
        self._unique_key = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if modifier is not None:
            self.modifier = modifier
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if source_entity_number is not None:
            self.source_entity_number = source_entity_number
        self.source_instance_id = source_instance_id
        if need_set_null_attrs is not None:
            self.need_set_null_attrs = need_set_null_attrs
        if entity_to_save is not None:
            self.entity_to_save = entity_to_save
        if entity_to_return is not None:
            self.entity_to_return = entity_to_return
        if unique_key is not None:
            self.unique_key = unique_key

    @property
    def id(self):
        r"""Gets the id of this PersistableModelSaveAsDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PersistableModelSaveAsDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this PersistableModelSaveAsDTO.
        :type id: str
        """
        self._id = id

    @property
    def modifier(self):
        r"""Gets the modifier of this PersistableModelSaveAsDTO.

        **参数解释：**  修改者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this PersistableModelSaveAsDTO.

        **参数解释：**  修改者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this PersistableModelSaveAsDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this PersistableModelSaveAsDTO.

        **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this PersistableModelSaveAsDTO.

        **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this PersistableModelSaveAsDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def creator(self):
        r"""Gets the creator of this PersistableModelSaveAsDTO.

        **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this PersistableModelSaveAsDTO.

        **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this PersistableModelSaveAsDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this PersistableModelSaveAsDTO.

        **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PersistableModelSaveAsDTO.

        **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this PersistableModelSaveAsDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this PersistableModelSaveAsDTO.

        **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this PersistableModelSaveAsDTO.

        **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this PersistableModelSaveAsDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        r"""Gets the tenant of this PersistableModelSaveAsDTO.

        :return: The tenant of this PersistableModelSaveAsDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this PersistableModelSaveAsDTO.

        :param tenant: The tenant of this PersistableModelSaveAsDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._tenant = tenant

    @property
    def source_entity_number(self):
        r"""Gets the source_entity_number of this PersistableModelSaveAsDTO.

        **参数解释：**  源模型编号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The source_entity_number of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._source_entity_number

    @source_entity_number.setter
    def source_entity_number(self, source_entity_number):
        r"""Sets the source_entity_number of this PersistableModelSaveAsDTO.

        **参数解释：**  源模型编号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param source_entity_number: The source_entity_number of this PersistableModelSaveAsDTO.
        :type source_entity_number: str
        """
        self._source_entity_number = source_entity_number

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this PersistableModelSaveAsDTO.

        **参数解释：**  源实例的唯一标识（单实例为ID，版本实例为versionId）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The source_instance_id of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this PersistableModelSaveAsDTO.

        **参数解释：**  源实例的唯一标识（单实例为ID，版本实例为versionId）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param source_instance_id: The source_instance_id of this PersistableModelSaveAsDTO.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def need_set_null_attrs(self):
        r"""Gets the need_set_null_attrs of this PersistableModelSaveAsDTO.

        **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The need_set_null_attrs of this PersistableModelSaveAsDTO.
        :rtype: list[str]
        """
        return self._need_set_null_attrs

    @need_set_null_attrs.setter
    def need_set_null_attrs(self, need_set_null_attrs):
        r"""Sets the need_set_null_attrs of this PersistableModelSaveAsDTO.

        **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param need_set_null_attrs: The need_set_null_attrs of this PersistableModelSaveAsDTO.
        :type need_set_null_attrs: list[str]
        """
        self._need_set_null_attrs = need_set_null_attrs

    @property
    def entity_to_save(self):
        r"""Gets the entity_to_save of this PersistableModelSaveAsDTO.

        **参数解释：**  要保存的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The entity_to_save of this PersistableModelSaveAsDTO.
        :rtype: object
        """
        return self._entity_to_save

    @entity_to_save.setter
    def entity_to_save(self, entity_to_save):
        r"""Sets the entity_to_save of this PersistableModelSaveAsDTO.

        **参数解释：**  要保存的属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param entity_to_save: The entity_to_save of this PersistableModelSaveAsDTO.
        :type entity_to_save: object
        """
        self._entity_to_save = entity_to_save

    @property
    def entity_to_return(self):
        r"""Gets the entity_to_return of this PersistableModelSaveAsDTO.

        **参数解释：**  要保存的结果。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The entity_to_return of this PersistableModelSaveAsDTO.
        :rtype: object
        """
        return self._entity_to_return

    @entity_to_return.setter
    def entity_to_return(self, entity_to_return):
        r"""Sets the entity_to_return of this PersistableModelSaveAsDTO.

        **参数解释：**  要保存的结果。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param entity_to_return: The entity_to_return of this PersistableModelSaveAsDTO.
        :type entity_to_return: object
        """
        self._entity_to_return = entity_to_return

    @property
    def unique_key(self):
        r"""Gets the unique_key of this PersistableModelSaveAsDTO.

        **参数解释：**  唯一键约束属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The unique_key of this PersistableModelSaveAsDTO.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        r"""Sets the unique_key of this PersistableModelSaveAsDTO.

        **参数解释：**  唯一键约束属性。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param unique_key: The unique_key of this PersistableModelSaveAsDTO.
        :type unique_key: str
        """
        self._unique_key = unique_key

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
        if not isinstance(other, PersistableModelSaveAsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
