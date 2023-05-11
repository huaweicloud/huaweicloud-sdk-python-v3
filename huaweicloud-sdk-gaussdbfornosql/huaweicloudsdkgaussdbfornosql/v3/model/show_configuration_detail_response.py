# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigurationDetailResponse(SdkResponse):

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
        'datastore_version_name': 'str',
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str',
        'configuration_parameters': 'list[ConfigurationParameterResult]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_version_name': 'datastore_version_name',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'configuration_parameters': 'configuration_parameters'
    }

    def __init__(self, id=None, name=None, description=None, datastore_version_name=None, datastore_name=None, created=None, updated=None, configuration_parameters=None):
        """ShowConfigurationDetailResponse

        The model defined in huaweicloud sdk

        :param id: 参数模板ID。
        :type id: str
        :param name: 参数模板名称。
        :type name: str
        :param description: 参数模板描述。
        :type description: str
        :param datastore_version_name: 数据库版本名称。
        :type datastore_version_name: str
        :param datastore_name: 数据库名称。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated: str
        :param configuration_parameters: 参数对象，用户基于默认参数模板自定义的参数配置。
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationParameterResult`]
        """
        
        super(ShowConfigurationDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._datastore_version_name = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._configuration_parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if datastore_version_name is not None:
            self.datastore_version_name = datastore_version_name
        if datastore_name is not None:
            self.datastore_name = datastore_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if configuration_parameters is not None:
            self.configuration_parameters = configuration_parameters

    @property
    def id(self):
        """Gets the id of this ShowConfigurationDetailResponse.

        参数模板ID。

        :return: The id of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowConfigurationDetailResponse.

        参数模板ID。

        :param id: The id of this ShowConfigurationDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowConfigurationDetailResponse.

        参数模板名称。

        :return: The name of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowConfigurationDetailResponse.

        参数模板名称。

        :param name: The name of this ShowConfigurationDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowConfigurationDetailResponse.

        参数模板描述。

        :return: The description of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowConfigurationDetailResponse.

        参数模板描述。

        :param description: The description of this ShowConfigurationDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def datastore_version_name(self):
        """Gets the datastore_version_name of this ShowConfigurationDetailResponse.

        数据库版本名称。

        :return: The datastore_version_name of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._datastore_version_name

    @datastore_version_name.setter
    def datastore_version_name(self, datastore_version_name):
        """Sets the datastore_version_name of this ShowConfigurationDetailResponse.

        数据库版本名称。

        :param datastore_version_name: The datastore_version_name of this ShowConfigurationDetailResponse.
        :type datastore_version_name: str
        """
        self._datastore_version_name = datastore_version_name

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ShowConfigurationDetailResponse.

        数据库名称。

        :return: The datastore_name of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ShowConfigurationDetailResponse.

        数据库名称。

        :param datastore_name: The datastore_name of this ShowConfigurationDetailResponse.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ShowConfigurationDetailResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowConfigurationDetailResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this ShowConfigurationDetailResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowConfigurationDetailResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated of this ShowConfigurationDetailResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowConfigurationDetailResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated: The updated of this ShowConfigurationDetailResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def configuration_parameters(self):
        """Gets the configuration_parameters of this ShowConfigurationDetailResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :return: The configuration_parameters of this ShowConfigurationDetailResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationParameterResult`]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        """Sets the configuration_parameters of this ShowConfigurationDetailResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :param configuration_parameters: The configuration_parameters of this ShowConfigurationDetailResponse.
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationParameterResult`]
        """
        self._configuration_parameters = configuration_parameters

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
        if not isinstance(other, ShowConfigurationDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
