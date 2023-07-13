# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationSummary:

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
        'datastore_version': 'str',
        'datastore_name': 'str',
        'ha_mode': 'str',
        'created': 'str',
        'updated': 'str',
        'user_defined': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_version': 'datastore_version',
        'datastore_name': 'datastore_name',
        'ha_mode': 'ha_mode',
        'created': 'created',
        'updated': 'updated',
        'user_defined': 'user_defined'
    }

    def __init__(self, id=None, name=None, description=None, datastore_version=None, datastore_name=None, ha_mode=None, created=None, updated=None, user_defined=None):
        """ConfigurationSummary

        The model defined in huaweicloud sdk

        :param id: 参数组ID。
        :type id: str
        :param name: 参数组名称。
        :type name: str
        :param description: 参数组描述。
        :type description: str
        :param datastore_version: 引擎版本。
        :type datastore_version: str
        :param datastore_name: 引擎名称。
        :type datastore_name: str
        :param ha_mode: 数据库部署模式。
        :type ha_mode: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-dd HH:mm:ss\&quot;。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-dd HH:mm:ss\&quot;。
        :type updated: str
        :param user_defined: 是否是用户自定义参数模板：  - false，表示为系统默认参数模板。 - true，表示为用户自定义参数模板。
        :type user_defined: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore_version = None
        self._datastore_name = None
        self._ha_mode = None
        self._created = None
        self._updated = None
        self._user_defined = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.datastore_version = datastore_version
        self.datastore_name = datastore_name
        self.ha_mode = ha_mode
        self.created = created
        self.updated = updated
        self.user_defined = user_defined

    @property
    def id(self):
        """Gets the id of this ConfigurationSummary.

        参数组ID。

        :return: The id of this ConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigurationSummary.

        参数组ID。

        :param id: The id of this ConfigurationSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigurationSummary.

        参数组名称。

        :return: The name of this ConfigurationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationSummary.

        参数组名称。

        :param name: The name of this ConfigurationSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConfigurationSummary.

        参数组描述。

        :return: The description of this ConfigurationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationSummary.

        参数组描述。

        :param description: The description of this ConfigurationSummary.
        :type description: str
        """
        self._description = description

    @property
    def datastore_version(self):
        """Gets the datastore_version of this ConfigurationSummary.

        引擎版本。

        :return: The datastore_version of this ConfigurationSummary.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        """Sets the datastore_version of this ConfigurationSummary.

        引擎版本。

        :param datastore_version: The datastore_version of this ConfigurationSummary.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ConfigurationSummary.

        引擎名称。

        :return: The datastore_name of this ConfigurationSummary.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ConfigurationSummary.

        引擎名称。

        :param datastore_name: The datastore_name of this ConfigurationSummary.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def ha_mode(self):
        """Gets the ha_mode of this ConfigurationSummary.

        数据库部署模式。

        :return: The ha_mode of this ConfigurationSummary.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this ConfigurationSummary.

        数据库部署模式。

        :param ha_mode: The ha_mode of this ConfigurationSummary.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def created(self):
        """Gets the created of this ConfigurationSummary.

        创建时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :return: The created of this ConfigurationSummary.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConfigurationSummary.

        创建时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :param created: The created of this ConfigurationSummary.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ConfigurationSummary.

        更新时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :return: The updated of this ConfigurationSummary.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ConfigurationSummary.

        更新时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :param updated: The updated of this ConfigurationSummary.
        :type updated: str
        """
        self._updated = updated

    @property
    def user_defined(self):
        """Gets the user_defined of this ConfigurationSummary.

        是否是用户自定义参数模板：  - false，表示为系统默认参数模板。 - true，表示为用户自定义参数模板。

        :return: The user_defined of this ConfigurationSummary.
        :rtype: bool
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this ConfigurationSummary.

        是否是用户自定义参数模板：  - false，表示为系统默认参数模板。 - true，表示为用户自定义参数模板。

        :param user_defined: The user_defined of this ConfigurationSummary.
        :type user_defined: bool
        """
        self._user_defined = user_defined

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
        if not isinstance(other, ConfigurationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
