# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceParamGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_version': 'str',
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str',
        'configuration_parameters': 'list[ConfigurationParameter]'
    }

    attribute_map = {
        'datastore_version': 'datastore_version',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'configuration_parameters': 'configuration_parameters'
    }

    def __init__(self, datastore_version=None, datastore_name=None, created=None, updated=None, configuration_parameters=None):
        """ShowInstanceParamGroupResponse

        The model defined in huaweicloud sdk

        :param datastore_version: 引擎版本。
        :type datastore_version: str
        :param datastore_name: 引擎名称。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-dd HH:mm:ss\&quot;。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddHH:mm:ss\&quot;。
        :type updated: str
        :param configuration_parameters: 参数对象，用户基于默认参数模板自定义的参数配置。
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ConfigurationParameter`]
        """
        
        super(ShowInstanceParamGroupResponse, self).__init__()

        self._datastore_version = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._configuration_parameters = None
        self.discriminator = None

        if datastore_version is not None:
            self.datastore_version = datastore_version
        if datastore_name is not None:
            self.datastore_name = datastore_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if configuration_parameters is not None:
            self.configuration_parameters = configuration_parameters

    @property
    def datastore_version(self):
        """Gets the datastore_version of this ShowInstanceParamGroupResponse.

        引擎版本。

        :return: The datastore_version of this ShowInstanceParamGroupResponse.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        """Sets the datastore_version of this ShowInstanceParamGroupResponse.

        引擎版本。

        :param datastore_version: The datastore_version of this ShowInstanceParamGroupResponse.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ShowInstanceParamGroupResponse.

        引擎名称。

        :return: The datastore_name of this ShowInstanceParamGroupResponse.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ShowInstanceParamGroupResponse.

        引擎名称。

        :param datastore_name: The datastore_name of this ShowInstanceParamGroupResponse.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ShowInstanceParamGroupResponse.

        创建时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :return: The created of this ShowInstanceParamGroupResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowInstanceParamGroupResponse.

        创建时间，格式为\"yyyy-MM-dd HH:mm:ss\"。

        :param created: The created of this ShowInstanceParamGroupResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowInstanceParamGroupResponse.

        更新时间，格式为\"yyyy-MM-ddHH:mm:ss\"。

        :return: The updated of this ShowInstanceParamGroupResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowInstanceParamGroupResponse.

        更新时间，格式为\"yyyy-MM-ddHH:mm:ss\"。

        :param updated: The updated of this ShowInstanceParamGroupResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def configuration_parameters(self):
        """Gets the configuration_parameters of this ShowInstanceParamGroupResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :return: The configuration_parameters of this ShowInstanceParamGroupResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ConfigurationParameter`]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        """Sets the configuration_parameters of this ShowInstanceParamGroupResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :param configuration_parameters: The configuration_parameters of this ShowInstanceParamGroupResponse.
        :type configuration_parameters: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ConfigurationParameter`]
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
        if not isinstance(other, ShowInstanceParamGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
