# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_version_name': 'str',
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str',
        'configuration_parameters': 'list[ConfigurationParameter]'
    }

    attribute_map = {
        'datastore_version_name': 'datastore_version_name',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'configuration_parameters': 'configuration_parameters'
    }

    def __init__(self, datastore_version_name=None, datastore_name=None, created=None, updated=None, configuration_parameters=None):
        """ShowInstanceConfigurationResponse

        The model defined in huaweicloud sdk

        :param datastore_version_name: 引擎版本。
        :type datastore_version_name: str
        :param datastore_name: 引擎名。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated: str
        :param configuration_parameters: 参数对象，用户基于默认参数模板自定义的参数配置。
        :type configuration_parameters: list[:class:`huaweicloudsdkrds.v3.ConfigurationParameter`]
        """
        
        super(ShowInstanceConfigurationResponse, self).__init__()

        self._datastore_version_name = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._configuration_parameters = None
        self.discriminator = None

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
    def datastore_version_name(self):
        """Gets the datastore_version_name of this ShowInstanceConfigurationResponse.

        引擎版本。

        :return: The datastore_version_name of this ShowInstanceConfigurationResponse.
        :rtype: str
        """
        return self._datastore_version_name

    @datastore_version_name.setter
    def datastore_version_name(self, datastore_version_name):
        """Sets the datastore_version_name of this ShowInstanceConfigurationResponse.

        引擎版本。

        :param datastore_version_name: The datastore_version_name of this ShowInstanceConfigurationResponse.
        :type datastore_version_name: str
        """
        self._datastore_version_name = datastore_version_name

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ShowInstanceConfigurationResponse.

        引擎名。

        :return: The datastore_name of this ShowInstanceConfigurationResponse.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ShowInstanceConfigurationResponse.

        引擎名。

        :param datastore_name: The datastore_name of this ShowInstanceConfigurationResponse.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ShowInstanceConfigurationResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this ShowInstanceConfigurationResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowInstanceConfigurationResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this ShowInstanceConfigurationResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowInstanceConfigurationResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated of this ShowInstanceConfigurationResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowInstanceConfigurationResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated: The updated of this ShowInstanceConfigurationResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def configuration_parameters(self):
        """Gets the configuration_parameters of this ShowInstanceConfigurationResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :return: The configuration_parameters of this ShowInstanceConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ConfigurationParameter`]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        """Sets the configuration_parameters of this ShowInstanceConfigurationResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :param configuration_parameters: The configuration_parameters of this ShowInstanceConfigurationResponse.
        :type configuration_parameters: list[:class:`huaweicloudsdkrds.v3.ConfigurationParameter`]
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
        if not isinstance(other, ShowInstanceConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
