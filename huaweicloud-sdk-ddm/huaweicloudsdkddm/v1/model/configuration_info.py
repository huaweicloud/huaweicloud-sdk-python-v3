# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationInfo:

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
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str',
        'user_defined': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'user_defined': 'user_defined'
    }

    def __init__(self, id=None, name=None, description=None, datastore_name=None, created=None, updated=None, user_defined=None):
        r"""ConfigurationInfo

        The model defined in huaweicloud sdk

        :param id: 参数模板ID。
        :type id: str
        :param name: 参数模板名称。
        :type name: str
        :param description: 参数模板描述。
        :type description: str
        :param datastore_name: 数据库类型。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated: str
        :param user_defined: 是否是用户自定义参数模板：  false，表示为系统默认参数模板。 true，表示为用户自定义参数模板。
        :type user_defined: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._user_defined = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.datastore_name = datastore_name
        self.created = created
        self.updated = updated
        self.user_defined = user_defined

    @property
    def id(self):
        r"""Gets the id of this ConfigurationInfo.

        参数模板ID。

        :return: The id of this ConfigurationInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConfigurationInfo.

        参数模板ID。

        :param id: The id of this ConfigurationInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ConfigurationInfo.

        参数模板名称。

        :return: The name of this ConfigurationInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationInfo.

        参数模板名称。

        :param name: The name of this ConfigurationInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ConfigurationInfo.

        参数模板描述。

        :return: The description of this ConfigurationInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationInfo.

        参数模板描述。

        :param description: The description of this ConfigurationInfo.
        :type description: str
        """
        self._description = description

    @property
    def datastore_name(self):
        r"""Gets the datastore_name of this ConfigurationInfo.

        数据库类型。

        :return: The datastore_name of this ConfigurationInfo.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        r"""Sets the datastore_name of this ConfigurationInfo.

        数据库类型。

        :param datastore_name: The datastore_name of this ConfigurationInfo.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        r"""Gets the created of this ConfigurationInfo.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this ConfigurationInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ConfigurationInfo.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this ConfigurationInfo.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ConfigurationInfo.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated of this ConfigurationInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ConfigurationInfo.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated: The updated of this ConfigurationInfo.
        :type updated: str
        """
        self._updated = updated

    @property
    def user_defined(self):
        r"""Gets the user_defined of this ConfigurationInfo.

        是否是用户自定义参数模板：  false，表示为系统默认参数模板。 true，表示为用户自定义参数模板。

        :return: The user_defined of this ConfigurationInfo.
        :rtype: bool
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        r"""Sets the user_defined of this ConfigurationInfo.

        是否是用户自定义参数模板：  false，表示为系统默认参数模板。 true，表示为用户自定义参数模板。

        :param user_defined: The user_defined of this ConfigurationInfo.
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
        if not isinstance(other, ConfigurationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
