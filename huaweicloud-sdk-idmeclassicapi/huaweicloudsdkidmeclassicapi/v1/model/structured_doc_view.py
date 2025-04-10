# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructuredDocView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator': 'str',
        'create_time': 'str',
        'last_update_time': 'str',
        'rdm_version': 'int',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'tenant': 'TenantViewDTO',
        'class_name': 'str',
        'clazz': 'str',
        'id': 'str',
        'document_id': 'str',
        'title': 'str',
        'type': 'str',
        'template_id': 'str',
        'organization_id': 'str',
        'wiki_id': 'str',
        'parent_document_id': 'str',
        'instance_id': 'str',
        'model_name': 'str',
        'create_user_id': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'create_time': 'createTime',
        'last_update_time': 'lastUpdateTime',
        'rdm_version': 'rdmVersion',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'class_name': 'className',
        'clazz': 'clazz',
        'id': 'id',
        'document_id': 'document_id',
        'title': 'title',
        'type': 'type',
        'template_id': 'template_id',
        'organization_id': 'organization_id',
        'wiki_id': 'wiki_id',
        'parent_document_id': 'parent_document_id',
        'instance_id': 'instance_id',
        'model_name': 'model_name',
        'create_user_id': 'create_user_id',
        'modifier': 'modifier'
    }

    def __init__(self, creator=None, create_time=None, last_update_time=None, rdm_version=None, rdm_delete_flag=None, rdm_extension_type=None, tenant=None, class_name=None, clazz=None, id=None, document_id=None, title=None, type=None, template_id=None, organization_id=None, wiki_id=None, parent_document_id=None, instance_id=None, model_name=None, create_user_id=None, modifier=None):
        r"""StructuredDocView

        The model defined in huaweicloud sdk

        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type creator: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type create_time: str
        :param last_update_time: **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type last_update_time: str
        :param rdm_version: **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type rdm_version: int
        :param rdm_delete_flag: **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  不涉及。
        :type rdm_delete_flag: int
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type class_name: str
        :param clazz: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type clazz: str
        :param id: **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。
        :type id: str
        :param document_id: **参数解释：**  kooPage文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type document_id: str
        :param title: **参数解释：**  文档标题。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type title: str
        :param type: **参数解释：**  文档类型。  **取值范围：**  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值：**  不涉及。
        :type type: str
        :param template_id: **参数解释：**  模板ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type template_id: str
        :param organization_id: **参数解释：**  团队ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type organization_id: str
        :param wiki_id: **参数解释：**  知识库ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type wiki_id: str
        :param parent_document_id: **参数解释：**  父文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type parent_document_id: str
        :param instance_id: **参数解释：**  实例ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type instance_id: str
        :param model_name: **参数解释：**  模型名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type model_name: str
        :param create_user_id: **参数解释：**  创建者ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type create_user_id: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._creator = None
        self._create_time = None
        self._last_update_time = None
        self._rdm_version = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._tenant = None
        self._class_name = None
        self._clazz = None
        self._id = None
        self._document_id = None
        self._title = None
        self._type = None
        self._template_id = None
        self._organization_id = None
        self._wiki_id = None
        self._parent_document_id = None
        self._instance_id = None
        self._model_name = None
        self._create_user_id = None
        self._modifier = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
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
        if clazz is not None:
            self.clazz = clazz
        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id
        if title is not None:
            self.title = title
        self.type = type
        if template_id is not None:
            self.template_id = template_id
        if organization_id is not None:
            self.organization_id = organization_id
        if wiki_id is not None:
            self.wiki_id = wiki_id
        if parent_document_id is not None:
            self.parent_document_id = parent_document_id
        if instance_id is not None:
            self.instance_id = instance_id
        if model_name is not None:
            self.model_name = model_name
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if modifier is not None:
            self.modifier = modifier

    @property
    def creator(self):
        r"""Gets the creator of this StructuredDocView.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The creator of this StructuredDocView.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this StructuredDocView.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param creator: The creator of this StructuredDocView.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this StructuredDocView.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The create_time of this StructuredDocView.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StructuredDocView.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param create_time: The create_time of this StructuredDocView.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this StructuredDocView.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The last_update_time of this StructuredDocView.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this StructuredDocView.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param last_update_time: The last_update_time of this StructuredDocView.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this StructuredDocView.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The rdm_version of this StructuredDocView.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this StructuredDocView.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param rdm_version: The rdm_version of this StructuredDocView.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this StructuredDocView.

        **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  不涉及。

        :return: The rdm_delete_flag of this StructuredDocView.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this StructuredDocView.

        **参数解释：**  软删除标识，参数值为0或1。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  不涉及。

        :param rdm_delete_flag: The rdm_delete_flag of this StructuredDocView.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this StructuredDocView.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The rdm_extension_type of this StructuredDocView.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this StructuredDocView.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param rdm_extension_type: The rdm_extension_type of this StructuredDocView.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        r"""Gets the tenant of this StructuredDocView.

        :return: The tenant of this StructuredDocView.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this StructuredDocView.

        :param tenant: The tenant of this StructuredDocView.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def class_name(self):
        r"""Gets the class_name of this StructuredDocView.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The class_name of this StructuredDocView.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this StructuredDocView.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param class_name: The class_name of this StructuredDocView.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def clazz(self):
        r"""Gets the clazz of this StructuredDocView.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The clazz of this StructuredDocView.
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        r"""Sets the clazz of this StructuredDocView.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param clazz: The clazz of this StructuredDocView.
        :type clazz: str
        """
        self._clazz = clazz

    @property
    def id(self):
        r"""Gets the id of this StructuredDocView.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :return: The id of this StructuredDocView.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StructuredDocView.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :param id: The id of this StructuredDocView.
        :type id: str
        """
        self._id = id

    @property
    def document_id(self):
        r"""Gets the document_id of this StructuredDocView.

        **参数解释：**  kooPage文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The document_id of this StructuredDocView.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this StructuredDocView.

        **参数解释：**  kooPage文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param document_id: The document_id of this StructuredDocView.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def title(self):
        r"""Gets the title of this StructuredDocView.

        **参数解释：**  文档标题。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The title of this StructuredDocView.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this StructuredDocView.

        **参数解释：**  文档标题。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param title: The title of this StructuredDocView.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this StructuredDocView.

        **参数解释：**  文档类型。  **取值范围：**  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值：**  不涉及。

        :return: The type of this StructuredDocView.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StructuredDocView.

        **参数解释：**  文档类型。  **取值范围：**  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值：**  不涉及。

        :param type: The type of this StructuredDocView.
        :type type: str
        """
        self._type = type

    @property
    def template_id(self):
        r"""Gets the template_id of this StructuredDocView.

        **参数解释：**  模板ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The template_id of this StructuredDocView.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this StructuredDocView.

        **参数解释：**  模板ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param template_id: The template_id of this StructuredDocView.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this StructuredDocView.

        **参数解释：**  团队ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The organization_id of this StructuredDocView.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this StructuredDocView.

        **参数解释：**  团队ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param organization_id: The organization_id of this StructuredDocView.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def wiki_id(self):
        r"""Gets the wiki_id of this StructuredDocView.

        **参数解释：**  知识库ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The wiki_id of this StructuredDocView.
        :rtype: str
        """
        return self._wiki_id

    @wiki_id.setter
    def wiki_id(self, wiki_id):
        r"""Sets the wiki_id of this StructuredDocView.

        **参数解释：**  知识库ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param wiki_id: The wiki_id of this StructuredDocView.
        :type wiki_id: str
        """
        self._wiki_id = wiki_id

    @property
    def parent_document_id(self):
        r"""Gets the parent_document_id of this StructuredDocView.

        **参数解释：**  父文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The parent_document_id of this StructuredDocView.
        :rtype: str
        """
        return self._parent_document_id

    @parent_document_id.setter
    def parent_document_id(self, parent_document_id):
        r"""Sets the parent_document_id of this StructuredDocView.

        **参数解释：**  父文档ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param parent_document_id: The parent_document_id of this StructuredDocView.
        :type parent_document_id: str
        """
        self._parent_document_id = parent_document_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this StructuredDocView.

        **参数解释：**  实例ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The instance_id of this StructuredDocView.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this StructuredDocView.

        **参数解释：**  实例ID。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param instance_id: The instance_id of this StructuredDocView.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def model_name(self):
        r"""Gets the model_name of this StructuredDocView.

        **参数解释：**  模型名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The model_name of this StructuredDocView.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this StructuredDocView.

        **参数解释：**  模型名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param model_name: The model_name of this StructuredDocView.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this StructuredDocView.

        **参数解释：**  创建者ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The create_user_id of this StructuredDocView.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this StructuredDocView.

        **参数解释：**  创建者ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param create_user_id: The create_user_id of this StructuredDocView.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def modifier(self):
        r"""Gets the modifier of this StructuredDocView.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this StructuredDocView.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this StructuredDocView.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this StructuredDocView.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, StructuredDocView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
