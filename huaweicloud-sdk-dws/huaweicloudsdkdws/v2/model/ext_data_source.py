# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtDataSource:

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
        'type': 'str',
        'connect_info': 'str',
        'user_name': 'str',
        'version': 'str',
        'configure_status': 'str',
        'status': 'str',
        'data_source_id': 'str',
        'created': 'str',
        'updated': 'str',
        'data_source_updated': 'str',
        'extend_properties': 'object',
        'description': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'connect_info': 'connect_info',
        'user_name': 'user_name',
        'version': 'version',
        'configure_status': 'configure_status',
        'status': 'status',
        'data_source_id': 'data_source_id',
        'created': 'created',
        'updated': 'updated',
        'data_source_updated': 'data_source_updated',
        'extend_properties': 'extend_properties',
        'description': 'description',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, type=None, connect_info=None, user_name=None, version=None, configure_status=None, status=None, data_source_id=None, created=None, updated=None, data_source_updated=None, extend_properties=None, description=None, fail_reason=None):
        r"""ExtDataSource

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 数据源ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 数据源名称。 **取值范围**： 不涉及。
        :type name: str
        :param type: **参数解释**： 类型。 **取值范围**： 不涉及。
        :type type: str
        :param connect_info: **参数解释**： 数据库。 **取值范围**： 不涉及。
        :type connect_info: str
        :param user_name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param version: **参数解释**： 版本。 **取值范围**： 不涉及。
        :type version: str
        :param configure_status: **参数解释**： 配置状态。 **取值范围**： 不涉及。
        :type configure_status: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param data_source_id: **参数解释**： 外部数据源ID。 **取值范围**： 不涉及。
        :type data_source_id: str
        :param created: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created: str
        :param updated: **参数解释**： 更新时间。 **取值范围**： 不涉及。
        :type updated: str
        :param data_source_updated: **参数解释**： 数据源更新时间。 **取值范围**： 不涉及。
        :type data_source_updated: str
        :param extend_properties: **参数解释**： 扩展信息。 **取值范围**： 不涉及。
        :type extend_properties: object
        :param description: **参数解释**： 描述。 **取值范围**： 不涉及。
        :type description: str
        :param fail_reason: **参数解释**： 失败原因。 **取值范围**： 不涉及。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._connect_info = None
        self._user_name = None
        self._version = None
        self._configure_status = None
        self._status = None
        self._data_source_id = None
        self._created = None
        self._updated = None
        self._data_source_updated = None
        self._extend_properties = None
        self._description = None
        self._fail_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if connect_info is not None:
            self.connect_info = connect_info
        if user_name is not None:
            self.user_name = user_name
        if version is not None:
            self.version = version
        if configure_status is not None:
            self.configure_status = configure_status
        if status is not None:
            self.status = status
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if data_source_updated is not None:
            self.data_source_updated = data_source_updated
        if extend_properties is not None:
            self.extend_properties = extend_properties
        if description is not None:
            self.description = description
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        r"""Gets the id of this ExtDataSource.

        **参数解释**： 数据源ID。 **取值范围**： 不涉及。

        :return: The id of this ExtDataSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExtDataSource.

        **参数解释**： 数据源ID。 **取值范围**： 不涉及。

        :param id: The id of this ExtDataSource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ExtDataSource.

        **参数解释**： 数据源名称。 **取值范围**： 不涉及。

        :return: The name of this ExtDataSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtDataSource.

        **参数解释**： 数据源名称。 **取值范围**： 不涉及。

        :param name: The name of this ExtDataSource.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ExtDataSource.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :return: The type of this ExtDataSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExtDataSource.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :param type: The type of this ExtDataSource.
        :type type: str
        """
        self._type = type

    @property
    def connect_info(self):
        r"""Gets the connect_info of this ExtDataSource.

        **参数解释**： 数据库。 **取值范围**： 不涉及。

        :return: The connect_info of this ExtDataSource.
        :rtype: str
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        r"""Sets the connect_info of this ExtDataSource.

        **参数解释**： 数据库。 **取值范围**： 不涉及。

        :param connect_info: The connect_info of this ExtDataSource.
        :type connect_info: str
        """
        self._connect_info = connect_info

    @property
    def user_name(self):
        r"""Gets the user_name of this ExtDataSource.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The user_name of this ExtDataSource.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExtDataSource.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this ExtDataSource.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def version(self):
        r"""Gets the version of this ExtDataSource.

        **参数解释**： 版本。 **取值范围**： 不涉及。

        :return: The version of this ExtDataSource.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ExtDataSource.

        **参数解释**： 版本。 **取值范围**： 不涉及。

        :param version: The version of this ExtDataSource.
        :type version: str
        """
        self._version = version

    @property
    def configure_status(self):
        r"""Gets the configure_status of this ExtDataSource.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :return: The configure_status of this ExtDataSource.
        :rtype: str
        """
        return self._configure_status

    @configure_status.setter
    def configure_status(self, configure_status):
        r"""Sets the configure_status of this ExtDataSource.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :param configure_status: The configure_status of this ExtDataSource.
        :type configure_status: str
        """
        self._configure_status = configure_status

    @property
    def status(self):
        r"""Gets the status of this ExtDataSource.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this ExtDataSource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExtDataSource.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this ExtDataSource.
        :type status: str
        """
        self._status = status

    @property
    def data_source_id(self):
        r"""Gets the data_source_id of this ExtDataSource.

        **参数解释**： 外部数据源ID。 **取值范围**： 不涉及。

        :return: The data_source_id of this ExtDataSource.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        r"""Sets the data_source_id of this ExtDataSource.

        **参数解释**： 外部数据源ID。 **取值范围**： 不涉及。

        :param data_source_id: The data_source_id of this ExtDataSource.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

    @property
    def created(self):
        r"""Gets the created of this ExtDataSource.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created of this ExtDataSource.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ExtDataSource.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created: The created of this ExtDataSource.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ExtDataSource.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :return: The updated of this ExtDataSource.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ExtDataSource.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :param updated: The updated of this ExtDataSource.
        :type updated: str
        """
        self._updated = updated

    @property
    def data_source_updated(self):
        r"""Gets the data_source_updated of this ExtDataSource.

        **参数解释**： 数据源更新时间。 **取值范围**： 不涉及。

        :return: The data_source_updated of this ExtDataSource.
        :rtype: str
        """
        return self._data_source_updated

    @data_source_updated.setter
    def data_source_updated(self, data_source_updated):
        r"""Sets the data_source_updated of this ExtDataSource.

        **参数解释**： 数据源更新时间。 **取值范围**： 不涉及。

        :param data_source_updated: The data_source_updated of this ExtDataSource.
        :type data_source_updated: str
        """
        self._data_source_updated = data_source_updated

    @property
    def extend_properties(self):
        r"""Gets the extend_properties of this ExtDataSource.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :return: The extend_properties of this ExtDataSource.
        :rtype: object
        """
        return self._extend_properties

    @extend_properties.setter
    def extend_properties(self, extend_properties):
        r"""Sets the extend_properties of this ExtDataSource.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :param extend_properties: The extend_properties of this ExtDataSource.
        :type extend_properties: object
        """
        self._extend_properties = extend_properties

    @property
    def description(self):
        r"""Gets the description of this ExtDataSource.

        **参数解释**： 描述。 **取值范围**： 不涉及。

        :return: The description of this ExtDataSource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtDataSource.

        **参数解释**： 描述。 **取值范围**： 不涉及。

        :param description: The description of this ExtDataSource.
        :type description: str
        """
        self._description = description

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ExtDataSource.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :return: The fail_reason of this ExtDataSource.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ExtDataSource.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :param fail_reason: The fail_reason of this ExtDataSource.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ExtDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
