# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOtaPackageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_id': 'str',
        'app_id': 'str',
        'package_type': 'str',
        'product_id': 'str',
        'version': 'str',
        'support_source_versions': 'list[str]',
        'description': 'str',
        'custom_info': 'str',
        'create_time': 'str',
        'file_location': 'FileLocation'
    }

    attribute_map = {
        'package_id': 'package_id',
        'app_id': 'app_id',
        'package_type': 'package_type',
        'product_id': 'product_id',
        'version': 'version',
        'support_source_versions': 'support_source_versions',
        'description': 'description',
        'custom_info': 'custom_info',
        'create_time': 'create_time',
        'file_location': 'file_location'
    }

    def __init__(self, package_id=None, app_id=None, package_type=None, product_id=None, version=None, support_source_versions=None, description=None, custom_info=None, create_time=None, file_location=None):
        """ShowOtaPackageResponse

        The model defined in huaweicloud sdk

        :param package_id: **参数说明**：升级包ID，用于唯一标识一个升级包。由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。
        :type package_id: str
        :param app_id: **参数说明**：资源空间ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param package_type: **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。
        :type package_type: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type product_id: str
        :param version: **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。
        :type version: str
        :param support_source_versions: **参数说明**：支持用于升级此版本包的设备源版本号列表。最多支持20个源版本号。 **取值范围**：源版本号列表，源版本号只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。
        :type support_source_versions: list[str]
        :param description: **参数说明**：用于描述升级包的功能等信息。 **取值范围**：长度不超过1024。
        :type description: str
        :param custom_info: **参数说明**：推送给设备的自定义信息。添加该升级包完成，并创建升级任务后，物联网平台向设备下发升级通知时，会下发该自定义信息给设备。 **取值范围**：长度不超过4096。
        :type custom_info: str
        :param create_time: 软固件包上传到物联网平台的时间，格式：\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;。
        :type create_time: str
        :param file_location: 
        :type file_location: :class:`huaweicloudsdkiotda.v5.FileLocation`
        """
        
        super(ShowOtaPackageResponse, self).__init__()

        self._package_id = None
        self._app_id = None
        self._package_type = None
        self._product_id = None
        self._version = None
        self._support_source_versions = None
        self._description = None
        self._custom_info = None
        self._create_time = None
        self._file_location = None
        self.discriminator = None

        if package_id is not None:
            self.package_id = package_id
        if app_id is not None:
            self.app_id = app_id
        if package_type is not None:
            self.package_type = package_type
        if product_id is not None:
            self.product_id = product_id
        if version is not None:
            self.version = version
        if support_source_versions is not None:
            self.support_source_versions = support_source_versions
        if description is not None:
            self.description = description
        if custom_info is not None:
            self.custom_info = custom_info
        if create_time is not None:
            self.create_time = create_time
        if file_location is not None:
            self.file_location = file_location

    @property
    def package_id(self):
        """Gets the package_id of this ShowOtaPackageResponse.

        **参数说明**：升级包ID，用于唯一标识一个升级包。由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。

        :return: The package_id of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ShowOtaPackageResponse.

        **参数说明**：升级包ID，用于唯一标识一个升级包。由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、连接符（-）的组合。

        :param package_id: The package_id of this ShowOtaPackageResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowOtaPackageResponse.

        **参数说明**：资源空间ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowOtaPackageResponse.

        **参数说明**：资源空间ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this ShowOtaPackageResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def package_type(self):
        """Gets the package_type of this ShowOtaPackageResponse.

        **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。

        :return: The package_type of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ShowOtaPackageResponse.

        **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。

        :param package_type: The package_type of this ShowOtaPackageResponse.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def product_id(self):
        """Gets the product_id of this ShowOtaPackageResponse.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The product_id of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowOtaPackageResponse.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param product_id: The product_id of this ShowOtaPackageResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def version(self):
        """Gets the version of this ShowOtaPackageResponse.

        **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :return: The version of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowOtaPackageResponse.

        **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :param version: The version of this ShowOtaPackageResponse.
        :type version: str
        """
        self._version = version

    @property
    def support_source_versions(self):
        """Gets the support_source_versions of this ShowOtaPackageResponse.

        **参数说明**：支持用于升级此版本包的设备源版本号列表。最多支持20个源版本号。 **取值范围**：源版本号列表，源版本号只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :return: The support_source_versions of this ShowOtaPackageResponse.
        :rtype: list[str]
        """
        return self._support_source_versions

    @support_source_versions.setter
    def support_source_versions(self, support_source_versions):
        """Sets the support_source_versions of this ShowOtaPackageResponse.

        **参数说明**：支持用于升级此版本包的设备源版本号列表。最多支持20个源版本号。 **取值范围**：源版本号列表，源版本号只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :param support_source_versions: The support_source_versions of this ShowOtaPackageResponse.
        :type support_source_versions: list[str]
        """
        self._support_source_versions = support_source_versions

    @property
    def description(self):
        """Gets the description of this ShowOtaPackageResponse.

        **参数说明**：用于描述升级包的功能等信息。 **取值范围**：长度不超过1024。

        :return: The description of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowOtaPackageResponse.

        **参数说明**：用于描述升级包的功能等信息。 **取值范围**：长度不超过1024。

        :param description: The description of this ShowOtaPackageResponse.
        :type description: str
        """
        self._description = description

    @property
    def custom_info(self):
        """Gets the custom_info of this ShowOtaPackageResponse.

        **参数说明**：推送给设备的自定义信息。添加该升级包完成，并创建升级任务后，物联网平台向设备下发升级通知时，会下发该自定义信息给设备。 **取值范围**：长度不超过4096。

        :return: The custom_info of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """Sets the custom_info of this ShowOtaPackageResponse.

        **参数说明**：推送给设备的自定义信息。添加该升级包完成，并创建升级任务后，物联网平台向设备下发升级通知时，会下发该自定义信息给设备。 **取值范围**：长度不超过4096。

        :param custom_info: The custom_info of this ShowOtaPackageResponse.
        :type custom_info: str
        """
        self._custom_info = custom_info

    @property
    def create_time(self):
        """Gets the create_time of this ShowOtaPackageResponse.

        软固件包上传到物联网平台的时间，格式：\"yyyyMMdd'T'HHmmss'Z'\"。

        :return: The create_time of this ShowOtaPackageResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowOtaPackageResponse.

        软固件包上传到物联网平台的时间，格式：\"yyyyMMdd'T'HHmmss'Z'\"。

        :param create_time: The create_time of this ShowOtaPackageResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def file_location(self):
        """Gets the file_location of this ShowOtaPackageResponse.

        :return: The file_location of this ShowOtaPackageResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.FileLocation`
        """
        return self._file_location

    @file_location.setter
    def file_location(self, file_location):
        """Sets the file_location of this ShowOtaPackageResponse.

        :param file_location: The file_location of this ShowOtaPackageResponse.
        :type file_location: :class:`huaweicloudsdkiotda.v5.FileLocation`
        """
        self._file_location = file_location

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
        if not isinstance(other, ShowOtaPackageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
