# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOtaPackageInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'app_id': 'str',
        'package_type': 'str',
        'product_id': 'str',
        'version': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'app_id': 'app_id',
        'package_type': 'package_type',
        'product_id': 'product_id',
        'version': 'version',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, app_id=None, package_type=None, product_id=None, version=None, limit=None, marker=None, offset=None):
        """ListOtaPackageInfoRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。
        :type instance_id: str
        :param app_id: **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定查询指定资源空间的升级包列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param package_type: **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。
        :type package_type: str
        :param product_id: **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type product_id: str
        :param version: **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。
        :type version: str
        :param limit: **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。
        :type limit: int
        :param marker: **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。**取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。
        :type marker: str
        :param offset: **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._app_id = None
        self._package_type = None
        self._product_id = None
        self._version = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        self.package_type = package_type
        if product_id is not None:
            self.product_id = product_id
        if version is not None:
            self.version = version
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListOtaPackageInfoRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :return: The instance_id of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListOtaPackageInfoRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :param instance_id: The instance_id of this ListOtaPackageInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListOtaPackageInfoRequest.

        **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定查询指定资源空间的升级包列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListOtaPackageInfoRequest.

        **参数说明**：资源空间ID。存在多资源空间的用户需要使用该接口时，建议携带该参数指定查询指定资源空间的升级包列表。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this ListOtaPackageInfoRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def package_type(self):
        """Gets the package_type of this ListOtaPackageInfoRequest.

        **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。

        :return: The package_type of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ListOtaPackageInfoRequest.

        **参数说明**：升级包类型。 **取值范围**：软件包必须设置为：softwarePackage，固件包必须设置为：firmwarePackage。

        :param package_type: The package_type of this ListOtaPackageInfoRequest.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def product_id(self):
        """Gets the product_id of this ListOtaPackageInfoRequest.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The product_id of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListOtaPackageInfoRequest.

        **参数说明**：设备关联的产品ID，用于唯一标识一个产品模型，创建产品后获得。方法请参见 [[创建产品](https://support.huaweicloud.com/api-iothub/iot_06_v5_0050.html)](tag:hws)[[创建产品](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0050.html)](tag:hws_hk)。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param product_id: The product_id of this ListOtaPackageInfoRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def version(self):
        """Gets the version of this ListOtaPackageInfoRequest.

        **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :return: The version of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListOtaPackageInfoRequest.

        **参数说明**：升级包版本号。 **取值范围**：长度不超过256，只允许字母、数字、下划线（_）、连接符（-）、英文点（.）的组合。

        :param version: The version of this ListOtaPackageInfoRequest.
        :type version: str
        """
        self._version = version

    @property
    def limit(self):
        """Gets the limit of this ListOtaPackageInfoRequest.

        **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。

        :return: The limit of this ListOtaPackageInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOtaPackageInfoRequest.

        **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。

        :param limit: The limit of this ListOtaPackageInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListOtaPackageInfoRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。**取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :return: The marker of this ListOtaPackageInfoRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListOtaPackageInfoRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。**取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :param marker: The marker of this ListOtaPackageInfoRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListOtaPackageInfoRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :return: The offset of this ListOtaPackageInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOtaPackageInfoRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。 **取值范围**：0-500的整数，默认为0。

        :param offset: The offset of this ListOtaPackageInfoRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListOtaPackageInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
