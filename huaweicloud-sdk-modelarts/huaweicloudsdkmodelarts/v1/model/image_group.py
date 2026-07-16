# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'create_at': 'int',
        'namespace': 'str',
        'update_at': 'int',
        'version_count': 'int',
        'description': 'str',
        'read_me': 'str',
        'icon_name': 'str',
        'id': 'str',
        'swr_instance_name': 'str',
        'swr_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'create_at': 'create_at',
        'namespace': 'namespace',
        'update_at': 'update_at',
        'version_count': 'version_count',
        'description': 'description',
        'read_me': 'read_me',
        'icon_name': 'icon_name',
        'id': 'id',
        'swr_instance_name': 'swr_instance_name',
        'swr_instance_id': 'swr_instance_id'
    }

    def __init__(self, name=None, create_at=None, namespace=None, update_at=None, version_count=None, description=None, read_me=None, icon_name=None, id=None, swr_instance_name=None, swr_instance_id=None):
        r"""ImageGroup

        The model defined in huaweicloud sdk

        :param name: **参数解释**：镜像名称。 **取值范围**：不涉及。
        :type name: str
        :param create_at: **参数解释**：镜像创建的时间，单位：UTC毫秒。 **取值范围**：不涉及。
        :type create_at: int
        :param namespace: **参数解释**：镜像所属的SWR组织。 **取值范围**：不涉及。
        :type namespace: str
        :param update_at: **参数解释**：镜像最后更新的时间，单位：UTC毫秒。 **取值范围**：不涉及。
        :type update_at: int
        :param version_count: **参数解释**：镜像版本个数。 **取值范围**：不涉及。
        :type version_count: int
        :param description: **参数解释**：镜像描述信息。 **取值范围**：不涉及。
        :type description: str
        :param read_me: **参数解释**：镜像指导。 **取值范围**：不涉及。
        :type read_me: str
        :param icon_name: **参数解释**：镜像图标名称。 **取值范围**：不涉及。
        :type icon_name: str
        :param id: **参数解释**：镜像id。 **取值范围**：不涉及。
        :type id: str
        :param swr_instance_name: **参数解释**：SWR企业版镜像仓库名称。 **取值范围**：不涉及。
        :type swr_instance_name: str
        :param swr_instance_id: **参数解释**：SWR企业版镜像仓库ID。 **取值范围**：不涉及。
        :type swr_instance_id: str
        """
        
        

        self._name = None
        self._create_at = None
        self._namespace = None
        self._update_at = None
        self._version_count = None
        self._description = None
        self._read_me = None
        self._icon_name = None
        self._id = None
        self._swr_instance_name = None
        self._swr_instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_at is not None:
            self.create_at = create_at
        if namespace is not None:
            self.namespace = namespace
        if update_at is not None:
            self.update_at = update_at
        if version_count is not None:
            self.version_count = version_count
        if description is not None:
            self.description = description
        if read_me is not None:
            self.read_me = read_me
        if icon_name is not None:
            self.icon_name = icon_name
        if id is not None:
            self.id = id
        if swr_instance_name is not None:
            self.swr_instance_name = swr_instance_name
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id

    @property
    def name(self):
        r"""Gets the name of this ImageGroup.

        **参数解释**：镜像名称。 **取值范围**：不涉及。

        :return: The name of this ImageGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageGroup.

        **参数解释**：镜像名称。 **取值范围**：不涉及。

        :param name: The name of this ImageGroup.
        :type name: str
        """
        self._name = name

    @property
    def create_at(self):
        r"""Gets the create_at of this ImageGroup.

        **参数解释**：镜像创建的时间，单位：UTC毫秒。 **取值范围**：不涉及。

        :return: The create_at of this ImageGroup.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ImageGroup.

        **参数解释**：镜像创建的时间，单位：UTC毫秒。 **取值范围**：不涉及。

        :param create_at: The create_at of this ImageGroup.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageGroup.

        **参数解释**：镜像所属的SWR组织。 **取值范围**：不涉及。

        :return: The namespace of this ImageGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageGroup.

        **参数解释**：镜像所属的SWR组织。 **取值范围**：不涉及。

        :param namespace: The namespace of this ImageGroup.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def update_at(self):
        r"""Gets the update_at of this ImageGroup.

        **参数解释**：镜像最后更新的时间，单位：UTC毫秒。 **取值范围**：不涉及。

        :return: The update_at of this ImageGroup.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ImageGroup.

        **参数解释**：镜像最后更新的时间，单位：UTC毫秒。 **取值范围**：不涉及。

        :param update_at: The update_at of this ImageGroup.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def version_count(self):
        r"""Gets the version_count of this ImageGroup.

        **参数解释**：镜像版本个数。 **取值范围**：不涉及。

        :return: The version_count of this ImageGroup.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this ImageGroup.

        **参数解释**：镜像版本个数。 **取值范围**：不涉及。

        :param version_count: The version_count of this ImageGroup.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def description(self):
        r"""Gets the description of this ImageGroup.

        **参数解释**：镜像描述信息。 **取值范围**：不涉及。

        :return: The description of this ImageGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageGroup.

        **参数解释**：镜像描述信息。 **取值范围**：不涉及。

        :param description: The description of this ImageGroup.
        :type description: str
        """
        self._description = description

    @property
    def read_me(self):
        r"""Gets the read_me of this ImageGroup.

        **参数解释**：镜像指导。 **取值范围**：不涉及。

        :return: The read_me of this ImageGroup.
        :rtype: str
        """
        return self._read_me

    @read_me.setter
    def read_me(self, read_me):
        r"""Sets the read_me of this ImageGroup.

        **参数解释**：镜像指导。 **取值范围**：不涉及。

        :param read_me: The read_me of this ImageGroup.
        :type read_me: str
        """
        self._read_me = read_me

    @property
    def icon_name(self):
        r"""Gets the icon_name of this ImageGroup.

        **参数解释**：镜像图标名称。 **取值范围**：不涉及。

        :return: The icon_name of this ImageGroup.
        :rtype: str
        """
        return self._icon_name

    @icon_name.setter
    def icon_name(self, icon_name):
        r"""Sets the icon_name of this ImageGroup.

        **参数解释**：镜像图标名称。 **取值范围**：不涉及。

        :param icon_name: The icon_name of this ImageGroup.
        :type icon_name: str
        """
        self._icon_name = icon_name

    @property
    def id(self):
        r"""Gets the id of this ImageGroup.

        **参数解释**：镜像id。 **取值范围**：不涉及。

        :return: The id of this ImageGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageGroup.

        **参数解释**：镜像id。 **取值范围**：不涉及。

        :param id: The id of this ImageGroup.
        :type id: str
        """
        self._id = id

    @property
    def swr_instance_name(self):
        r"""Gets the swr_instance_name of this ImageGroup.

        **参数解释**：SWR企业版镜像仓库名称。 **取值范围**：不涉及。

        :return: The swr_instance_name of this ImageGroup.
        :rtype: str
        """
        return self._swr_instance_name

    @swr_instance_name.setter
    def swr_instance_name(self, swr_instance_name):
        r"""Sets the swr_instance_name of this ImageGroup.

        **参数解释**：SWR企业版镜像仓库名称。 **取值范围**：不涉及。

        :param swr_instance_name: The swr_instance_name of this ImageGroup.
        :type swr_instance_name: str
        """
        self._swr_instance_name = swr_instance_name

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this ImageGroup.

        **参数解释**：SWR企业版镜像仓库ID。 **取值范围**：不涉及。

        :return: The swr_instance_id of this ImageGroup.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this ImageGroup.

        **参数解释**：SWR企业版镜像仓库ID。 **取值范围**：不涉及。

        :param swr_instance_id: The swr_instance_id of this ImageGroup.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
