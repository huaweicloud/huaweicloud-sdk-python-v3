# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Lineage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_type_name': 'str',
        'direction': 'str',
        'ep1_id': 'str',
        'ep1_type_name': 'str',
        'ep2_id': 'str',
        'ep2_type_name': 'str',
        'end1': 'Entity',
        'end2': 'Entity',
        'propagate_tag': 'str',
        'guid': 'str',
        'type_name': 'str',
        'type_display_name': 'str',
        'display_text': 'str',
        'attributes': 'object',
        'updated_attributes': 'list[str]',
        'project_id': 'str',
        'domain_id': 'str',
        'instance_id': 'list[str]',
        'workspace_id': 'list[str]',
        'status': 'str',
        'created_by': 'str',
        'updated_by': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'relation_type_name': 'relation_type_name',
        'direction': 'direction',
        'ep1_id': 'ep1_id',
        'ep1_type_name': 'ep1_type_name',
        'ep2_id': 'ep2_id',
        'ep2_type_name': 'ep2_type_name',
        'end1': 'end1',
        'end2': 'end2',
        'propagate_tag': 'propagate_tag',
        'guid': 'guid',
        'type_name': 'type_name',
        'type_display_name': 'type_display_name',
        'display_text': 'display_text',
        'attributes': 'attributes',
        'updated_attributes': 'updated_attributes',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'status': 'status',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, relation_type_name=None, direction=None, ep1_id=None, ep1_type_name=None, ep2_id=None, ep2_type_name=None, end1=None, end2=None, propagate_tag=None, guid=None, type_name=None, type_display_name=None, display_text=None, attributes=None, updated_attributes=None, project_id=None, domain_id=None, instance_id=None, workspace_id=None, status=None, created_by=None, updated_by=None, create_time=None, update_time=None):
        r"""Lineage

        The model defined in huaweicloud sdk

        :param relation_type_name: 关系类型。PARENT_CHILD,LOGICAL_PHYSICAL,PK_FK,DATA_FLOW,INSTANCE_OF,JOIN,IS_A,UP_DOWN,ASSOCIATION,WORK_FLOW
        :type relation_type_name: str
        :param direction: 血缘流向，IN,OUT,BOTH
        :type direction: str
        :param ep1_id: 节点一资产guid
        :type ep1_id: str
        :param ep1_type_name: 节点一资产类型
        :type ep1_type_name: str
        :param ep2_id: 节点二资产guid
        :type ep2_id: str
        :param ep2_type_name: 节点二资产类型
        :type ep2_type_name: str
        :param end1: 
        :type end1: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        :param end2: 
        :type end2: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        :param propagate_tag: 关系类型。NONE,ONE_TO_TWO,TWO_TO_ONE,BOTH
        :type propagate_tag: str
        :param guid: 资产guid
        :type guid: str
        :param type_name: 资产类型名称
        :type type_name: str
        :param type_display_name: 类型展示名称
        :type type_display_name: str
        :param display_text: 展示名称
        :type display_text: str
        :param attributes: 资产属性，Map&lt;String, Object&gt;
        :type attributes: object
        :param updated_attributes: 修改属性列表
        :type updated_attributes: list[str]
        :param project_id: 项目id
        :type project_id: str
        :param domain_id: 主账号id
        :type domain_id: str
        :param instance_id: 实例id
        :type instance_id: list[str]
        :param workspace_id: 空间id列表
        :type workspace_id: list[str]
        :param status: 状态
        :type status: str
        :param created_by: 创建人
        :type created_by: str
        :param updated_by: 修改人
        :type updated_by: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        """
        
        

        self._relation_type_name = None
        self._direction = None
        self._ep1_id = None
        self._ep1_type_name = None
        self._ep2_id = None
        self._ep2_type_name = None
        self._end1 = None
        self._end2 = None
        self._propagate_tag = None
        self._guid = None
        self._type_name = None
        self._type_display_name = None
        self._display_text = None
        self._attributes = None
        self._updated_attributes = None
        self._project_id = None
        self._domain_id = None
        self._instance_id = None
        self._workspace_id = None
        self._status = None
        self._created_by = None
        self._updated_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if relation_type_name is not None:
            self.relation_type_name = relation_type_name
        if direction is not None:
            self.direction = direction
        if ep1_id is not None:
            self.ep1_id = ep1_id
        if ep1_type_name is not None:
            self.ep1_type_name = ep1_type_name
        if ep2_id is not None:
            self.ep2_id = ep2_id
        if ep2_type_name is not None:
            self.ep2_type_name = ep2_type_name
        if end1 is not None:
            self.end1 = end1
        if end2 is not None:
            self.end2 = end2
        if propagate_tag is not None:
            self.propagate_tag = propagate_tag
        if guid is not None:
            self.guid = guid
        if type_name is not None:
            self.type_name = type_name
        if type_display_name is not None:
            self.type_display_name = type_display_name
        if display_text is not None:
            self.display_text = display_text
        if attributes is not None:
            self.attributes = attributes
        if updated_attributes is not None:
            self.updated_attributes = updated_attributes
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if status is not None:
            self.status = status
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def relation_type_name(self):
        r"""Gets the relation_type_name of this Lineage.

        关系类型。PARENT_CHILD,LOGICAL_PHYSICAL,PK_FK,DATA_FLOW,INSTANCE_OF,JOIN,IS_A,UP_DOWN,ASSOCIATION,WORK_FLOW

        :return: The relation_type_name of this Lineage.
        :rtype: str
        """
        return self._relation_type_name

    @relation_type_name.setter
    def relation_type_name(self, relation_type_name):
        r"""Sets the relation_type_name of this Lineage.

        关系类型。PARENT_CHILD,LOGICAL_PHYSICAL,PK_FK,DATA_FLOW,INSTANCE_OF,JOIN,IS_A,UP_DOWN,ASSOCIATION,WORK_FLOW

        :param relation_type_name: The relation_type_name of this Lineage.
        :type relation_type_name: str
        """
        self._relation_type_name = relation_type_name

    @property
    def direction(self):
        r"""Gets the direction of this Lineage.

        血缘流向，IN,OUT,BOTH

        :return: The direction of this Lineage.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this Lineage.

        血缘流向，IN,OUT,BOTH

        :param direction: The direction of this Lineage.
        :type direction: str
        """
        self._direction = direction

    @property
    def ep1_id(self):
        r"""Gets the ep1_id of this Lineage.

        节点一资产guid

        :return: The ep1_id of this Lineage.
        :rtype: str
        """
        return self._ep1_id

    @ep1_id.setter
    def ep1_id(self, ep1_id):
        r"""Sets the ep1_id of this Lineage.

        节点一资产guid

        :param ep1_id: The ep1_id of this Lineage.
        :type ep1_id: str
        """
        self._ep1_id = ep1_id

    @property
    def ep1_type_name(self):
        r"""Gets the ep1_type_name of this Lineage.

        节点一资产类型

        :return: The ep1_type_name of this Lineage.
        :rtype: str
        """
        return self._ep1_type_name

    @ep1_type_name.setter
    def ep1_type_name(self, ep1_type_name):
        r"""Sets the ep1_type_name of this Lineage.

        节点一资产类型

        :param ep1_type_name: The ep1_type_name of this Lineage.
        :type ep1_type_name: str
        """
        self._ep1_type_name = ep1_type_name

    @property
    def ep2_id(self):
        r"""Gets the ep2_id of this Lineage.

        节点二资产guid

        :return: The ep2_id of this Lineage.
        :rtype: str
        """
        return self._ep2_id

    @ep2_id.setter
    def ep2_id(self, ep2_id):
        r"""Sets the ep2_id of this Lineage.

        节点二资产guid

        :param ep2_id: The ep2_id of this Lineage.
        :type ep2_id: str
        """
        self._ep2_id = ep2_id

    @property
    def ep2_type_name(self):
        r"""Gets the ep2_type_name of this Lineage.

        节点二资产类型

        :return: The ep2_type_name of this Lineage.
        :rtype: str
        """
        return self._ep2_type_name

    @ep2_type_name.setter
    def ep2_type_name(self, ep2_type_name):
        r"""Sets the ep2_type_name of this Lineage.

        节点二资产类型

        :param ep2_type_name: The ep2_type_name of this Lineage.
        :type ep2_type_name: str
        """
        self._ep2_type_name = ep2_type_name

    @property
    def end1(self):
        r"""Gets the end1 of this Lineage.

        :return: The end1 of this Lineage.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        """
        return self._end1

    @end1.setter
    def end1(self, end1):
        r"""Sets the end1 of this Lineage.

        :param end1: The end1 of this Lineage.
        :type end1: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        """
        self._end1 = end1

    @property
    def end2(self):
        r"""Gets the end2 of this Lineage.

        :return: The end2 of this Lineage.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        """
        return self._end2

    @end2.setter
    def end2(self, end2):
        r"""Sets the end2 of this Lineage.

        :param end2: The end2 of this Lineage.
        :type end2: :class:`huaweicloudsdkdataartsstudio.v1.Entity`
        """
        self._end2 = end2

    @property
    def propagate_tag(self):
        r"""Gets the propagate_tag of this Lineage.

        关系类型。NONE,ONE_TO_TWO,TWO_TO_ONE,BOTH

        :return: The propagate_tag of this Lineage.
        :rtype: str
        """
        return self._propagate_tag

    @propagate_tag.setter
    def propagate_tag(self, propagate_tag):
        r"""Sets the propagate_tag of this Lineage.

        关系类型。NONE,ONE_TO_TWO,TWO_TO_ONE,BOTH

        :param propagate_tag: The propagate_tag of this Lineage.
        :type propagate_tag: str
        """
        self._propagate_tag = propagate_tag

    @property
    def guid(self):
        r"""Gets the guid of this Lineage.

        资产guid

        :return: The guid of this Lineage.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this Lineage.

        资产guid

        :param guid: The guid of this Lineage.
        :type guid: str
        """
        self._guid = guid

    @property
    def type_name(self):
        r"""Gets the type_name of this Lineage.

        资产类型名称

        :return: The type_name of this Lineage.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this Lineage.

        资产类型名称

        :param type_name: The type_name of this Lineage.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def type_display_name(self):
        r"""Gets the type_display_name of this Lineage.

        类型展示名称

        :return: The type_display_name of this Lineage.
        :rtype: str
        """
        return self._type_display_name

    @type_display_name.setter
    def type_display_name(self, type_display_name):
        r"""Sets the type_display_name of this Lineage.

        类型展示名称

        :param type_display_name: The type_display_name of this Lineage.
        :type type_display_name: str
        """
        self._type_display_name = type_display_name

    @property
    def display_text(self):
        r"""Gets the display_text of this Lineage.

        展示名称

        :return: The display_text of this Lineage.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        r"""Sets the display_text of this Lineage.

        展示名称

        :param display_text: The display_text of this Lineage.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def attributes(self):
        r"""Gets the attributes of this Lineage.

        资产属性，Map<String, Object>

        :return: The attributes of this Lineage.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this Lineage.

        资产属性，Map<String, Object>

        :param attributes: The attributes of this Lineage.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def updated_attributes(self):
        r"""Gets the updated_attributes of this Lineage.

        修改属性列表

        :return: The updated_attributes of this Lineage.
        :rtype: list[str]
        """
        return self._updated_attributes

    @updated_attributes.setter
    def updated_attributes(self, updated_attributes):
        r"""Sets the updated_attributes of this Lineage.

        修改属性列表

        :param updated_attributes: The updated_attributes of this Lineage.
        :type updated_attributes: list[str]
        """
        self._updated_attributes = updated_attributes

    @property
    def project_id(self):
        r"""Gets the project_id of this Lineage.

        项目id

        :return: The project_id of this Lineage.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Lineage.

        项目id

        :param project_id: The project_id of this Lineage.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Lineage.

        主账号id

        :return: The domain_id of this Lineage.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Lineage.

        主账号id

        :param domain_id: The domain_id of this Lineage.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Lineage.

        实例id

        :return: The instance_id of this Lineage.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Lineage.

        实例id

        :param instance_id: The instance_id of this Lineage.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this Lineage.

        空间id列表

        :return: The workspace_id of this Lineage.
        :rtype: list[str]
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this Lineage.

        空间id列表

        :param workspace_id: The workspace_id of this Lineage.
        :type workspace_id: list[str]
        """
        self._workspace_id = workspace_id

    @property
    def status(self):
        r"""Gets the status of this Lineage.

        状态

        :return: The status of this Lineage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Lineage.

        状态

        :param status: The status of this Lineage.
        :type status: str
        """
        self._status = status

    @property
    def created_by(self):
        r"""Gets the created_by of this Lineage.

        创建人

        :return: The created_by of this Lineage.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this Lineage.

        创建人

        :param created_by: The created_by of this Lineage.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        r"""Gets the updated_by of this Lineage.

        修改人

        :return: The updated_by of this Lineage.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this Lineage.

        修改人

        :param updated_by: The updated_by of this Lineage.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def create_time(self):
        r"""Gets the create_time of this Lineage.

        创建时间

        :return: The create_time of this Lineage.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Lineage.

        创建时间

        :param create_time: The create_time of this Lineage.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Lineage.

        修改时间

        :return: The update_time of this Lineage.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Lineage.

        修改时间

        :param update_time: The update_time of this Lineage.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Lineage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
