# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpGroup:

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
        'name': 'str',
        'description': 'str',
        'ip_list': 'list[IpInfo]',
        'listeners': 'list[ListenerRef]',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ip_list': 'ip_list',
        'listeners': 'listeners',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, ip_list=None, listeners=None, project_id=None, enterprise_project_id=None, created_at=None, updated_at=None):
        r"""IpGroup

        The model defined in huaweicloud sdk

        :param id: **参数解释**：IP地址组的ID。  **取值范围**：不涉及
        :type id: str
        :param name: **参数解释**：IP地址组的名称。  **取值范围**：不涉及
        :type name: str
        :param description: **参数解释**：IP地址组的描述信息。  **取值范围**：不涉及
        :type description: str
        :param ip_list: **参数解释**：IP地址组中包含的IP地址列表。[]表示任意IP。
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.IpInfo`]
        :param listeners: **参数解释**：与IP地址组关联的监听器的ID列表。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        :param project_id: **参数解释**：IP地址组的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。  **取值范围**： - \&quot;0\&quot;：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param created_at: **参数解释**：IP地址组的创建时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type created_at: str
        :param updated_at: **参数解释**：IP地址组的更新时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._ip_list = None
        self._listeners = None
        self._project_id = None
        self._enterprise_project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.ip_list = ip_list
        self.listeners = listeners
        self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this IpGroup.

        **参数解释**：IP地址组的ID。  **取值范围**：不涉及

        :return: The id of this IpGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpGroup.

        **参数解释**：IP地址组的ID。  **取值范围**：不涉及

        :param id: The id of this IpGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this IpGroup.

        **参数解释**：IP地址组的名称。  **取值范围**：不涉及

        :return: The name of this IpGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpGroup.

        **参数解释**：IP地址组的名称。  **取值范围**：不涉及

        :param name: The name of this IpGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this IpGroup.

        **参数解释**：IP地址组的描述信息。  **取值范围**：不涉及

        :return: The description of this IpGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IpGroup.

        **参数解释**：IP地址组的描述信息。  **取值范围**：不涉及

        :param description: The description of this IpGroup.
        :type description: str
        """
        self._description = description

    @property
    def ip_list(self):
        r"""Gets the ip_list of this IpGroup.

        **参数解释**：IP地址组中包含的IP地址列表。[]表示任意IP。

        :return: The ip_list of this IpGroup.
        :rtype: list[:class:`huaweicloudsdkelb.v3.IpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this IpGroup.

        **参数解释**：IP地址组中包含的IP地址列表。[]表示任意IP。

        :param ip_list: The ip_list of this IpGroup.
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.IpInfo`]
        """
        self._ip_list = ip_list

    @property
    def listeners(self):
        r"""Gets the listeners of this IpGroup.

        **参数解释**：与IP地址组关联的监听器的ID列表。

        :return: The listeners of this IpGroup.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this IpGroup.

        **参数解释**：与IP地址组关联的监听器的ID列表。

        :param listeners: The listeners of this IpGroup.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def project_id(self):
        r"""Gets the project_id of this IpGroup.

        **参数解释**：IP地址组的项目ID。  **取值范围**：不涉及

        :return: The project_id of this IpGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IpGroup.

        **参数解释**：IP地址组的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this IpGroup.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this IpGroup.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this IpGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this IpGroup.

        **参数解释**：资源所属的企业项目ID。  **取值范围**： - \"0\"：表示资源属于default企业项目。 - UUID格式的字符串，表示非默认企业项目。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this IpGroup.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this IpGroup.

        **参数解释**：IP地址组的创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The created_at of this IpGroup.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this IpGroup.

        **参数解释**：IP地址组的创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param created_at: The created_at of this IpGroup.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this IpGroup.

        **参数解释**：IP地址组的更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The updated_at of this IpGroup.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this IpGroup.

        **参数解释**：IP地址组的更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param updated_at: The updated_at of this IpGroup.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, IpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
