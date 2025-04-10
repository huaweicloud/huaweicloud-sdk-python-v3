# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEntityConfigurationResponse(SdkResponse):

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
        'parameters': 'list[EntityConfigurationParametersResult]'
    }

    attribute_map = {
        'datastore_version': 'datastore_version',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'parameters': 'parameters'
    }

    def __init__(self, datastore_version=None, datastore_name=None, created=None, updated=None, parameters=None):
        r"""ShowEntityConfigurationResponse

        The model defined in huaweicloud sdk

        :param datastore_version: 数据库版本。
        :type datastore_version: str
        :param datastore_name: 数据库类型。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated: str
        :param parameters: 参数对象，用户基于默认参数模板自定义的参数配置。
        :type parameters: list[:class:`huaweicloudsdkdds.v3.EntityConfigurationParametersResult`]
        """
        
        super(ShowEntityConfigurationResponse, self).__init__()

        self._datastore_version = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._parameters = None
        self.discriminator = None

        if datastore_version is not None:
            self.datastore_version = datastore_version
        if datastore_name is not None:
            self.datastore_name = datastore_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if parameters is not None:
            self.parameters = parameters

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ShowEntityConfigurationResponse.

        数据库版本。

        :return: The datastore_version of this ShowEntityConfigurationResponse.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ShowEntityConfigurationResponse.

        数据库版本。

        :param datastore_version: The datastore_version of this ShowEntityConfigurationResponse.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_name(self):
        r"""Gets the datastore_name of this ShowEntityConfigurationResponse.

        数据库类型。

        :return: The datastore_name of this ShowEntityConfigurationResponse.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        r"""Sets the datastore_name of this ShowEntityConfigurationResponse.

        数据库类型。

        :param datastore_name: The datastore_name of this ShowEntityConfigurationResponse.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        r"""Gets the created of this ShowEntityConfigurationResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this ShowEntityConfigurationResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowEntityConfigurationResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this ShowEntityConfigurationResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowEntityConfigurationResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated of this ShowEntityConfigurationResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowEntityConfigurationResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated: The updated of this ShowEntityConfigurationResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def parameters(self):
        r"""Gets the parameters of this ShowEntityConfigurationResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :return: The parameters of this ShowEntityConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.EntityConfigurationParametersResult`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ShowEntityConfigurationResponse.

        参数对象，用户基于默认参数模板自定义的参数配置。

        :param parameters: The parameters of this ShowEntityConfigurationResponse.
        :type parameters: list[:class:`huaweicloudsdkdds.v3.EntityConfigurationParametersResult`]
        """
        self._parameters = parameters

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
        if not isinstance(other, ShowEntityConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
