# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemandProductInfo:

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
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec': 'str',
        'region': 'str',
        'available_zone': 'str',
        'resource_size': 'int',
        'size_measure_id': 'int',
        'usage_factor': 'str',
        'usage_value': 'decimal.Decimal',
        'usage_measure_id': 'int',
        'subscription_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec': 'resource_spec',
        'region': 'region',
        'available_zone': 'available_zone',
        'resource_size': 'resource_size',
        'size_measure_id': 'size_measure_id',
        'usage_factor': 'usage_factor',
        'usage_value': 'usage_value',
        'usage_measure_id': 'usage_measure_id',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, id=None, cloud_service_type=None, resource_type=None, resource_spec=None, region=None, available_zone=None, resource_size=None, size_measure_id=None, usage_factor=None, usage_value=None, usage_measure_id=None, subscription_num=None):
        r"""DemandProductInfo

        The model defined in huaweicloud sdk

        :param id: ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。
        :type id: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。
        :type cloud_service_type: str
        :param resource_type: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。
        :type resource_type: str
        :param resource_spec: 云服务类型的资源规格，部分云服务类型和资源规格举例如下： 弹性云服务器：根据操作系统类型在云服务器规格的ID后添加“.win”或“.linux”，例如“s2.small.1.linux”。云服务器规格的ID字段，您可以调用查询规格详情和规格扩展信息列表接口获取。 带宽：12_bgp：动态BGP按流量计费带宽12_sbgp：静态BGP按流量计费带宽19_bgp：动态BGP按带宽计费带宽19_sbgp：静态BGP按带宽计费带宽19_share：按带宽计费共享带宽 IP：5_bgp：动态BGP公网IP5_sbgp：静态BGP公网IP 云硬盘：SATA：普通IO云硬盘SAS：高IO云硬盘GPSSD：通用型SSD云硬盘SSD：超高IO云硬盘
        :type resource_spec: str
        :param region: 云服务区编码，例如：“cn-north-1”。
        :type region: str
        :param available_zone: 可用区标识。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type available_zone: str
        :param resource_size: 资源容量大小，例如购买的卷大小或带宽大小。 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。
        :type resource_size: int
        :param size_measure_id: 资源容量度量标识，枚举值如下： 15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个（次） 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。
        :type size_measure_id: int
        :param usage_factor: 使用量因子编码，大小写不敏感，取值和话单中的使用量因子一致，云服务和使用量因子对应关系举例如下： 云服务器：Duration云硬盘：Duration弹性IP：Duration带宽：Duration或upflow市场镜像：Duration 您可以调用查询使用量类型列表接口获取响应参数表3中参数code的取值，即每种云服务对应的计费因子。
        :type usage_factor: str
        :param usage_value: 使用量值。 例如按小时询价，使用量值为1，使用量单位为小时。
        :type usage_value: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param usage_measure_id: 使用量度量单位， 例如按小时询价，使用量值为1，使用量单位为小时。
        :type usage_measure_id: int
        :param subscription_num: 订购数量。
        :type subscription_num: int
        """
        
        

        self._id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec = None
        self._region = None
        self._available_zone = None
        self._resource_size = None
        self._size_measure_id = None
        self._usage_factor = None
        self._usage_value = None
        self._usage_measure_id = None
        self._subscription_num = None
        self.discriminator = None

        self.id = id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec = resource_spec
        self.region = region
        if available_zone is not None:
            self.available_zone = available_zone
        if resource_size is not None:
            self.resource_size = resource_size
        if size_measure_id is not None:
            self.size_measure_id = size_measure_id
        self.usage_factor = usage_factor
        self.usage_value = usage_value
        self.usage_measure_id = usage_measure_id
        self.subscription_num = subscription_num

    @property
    def id(self):
        r"""Gets the id of this DemandProductInfo.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。

        :return: The id of this DemandProductInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DemandProductInfo.

        ID标识，同一次询价中不能重复，用于标识返回询价结果和请求的映射关系。

        :param id: The id of this DemandProductInfo.
        :type id: str
        """
        self._id = id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this DemandProductInfo.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。

        :return: The cloud_service_type of this DemandProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this DemandProductInfo.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。

        :param cloud_service_type: The cloud_service_type of this DemandProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this DemandProductInfo.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。

        :return: The resource_type of this DemandProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this DemandProductInfo.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。

        :param resource_type: The resource_type of this DemandProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec(self):
        r"""Gets the resource_spec of this DemandProductInfo.

        云服务类型的资源规格，部分云服务类型和资源规格举例如下： 弹性云服务器：根据操作系统类型在云服务器规格的ID后添加“.win”或“.linux”，例如“s2.small.1.linux”。云服务器规格的ID字段，您可以调用查询规格详情和规格扩展信息列表接口获取。 带宽：12_bgp：动态BGP按流量计费带宽12_sbgp：静态BGP按流量计费带宽19_bgp：动态BGP按带宽计费带宽19_sbgp：静态BGP按带宽计费带宽19_share：按带宽计费共享带宽 IP：5_bgp：动态BGP公网IP5_sbgp：静态BGP公网IP 云硬盘：SATA：普通IO云硬盘SAS：高IO云硬盘GPSSD：通用型SSD云硬盘SSD：超高IO云硬盘

        :return: The resource_spec of this DemandProductInfo.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        r"""Sets the resource_spec of this DemandProductInfo.

        云服务类型的资源规格，部分云服务类型和资源规格举例如下： 弹性云服务器：根据操作系统类型在云服务器规格的ID后添加“.win”或“.linux”，例如“s2.small.1.linux”。云服务器规格的ID字段，您可以调用查询规格详情和规格扩展信息列表接口获取。 带宽：12_bgp：动态BGP按流量计费带宽12_sbgp：静态BGP按流量计费带宽19_bgp：动态BGP按带宽计费带宽19_sbgp：静态BGP按带宽计费带宽19_share：按带宽计费共享带宽 IP：5_bgp：动态BGP公网IP5_sbgp：静态BGP公网IP 云硬盘：SATA：普通IO云硬盘SAS：高IO云硬盘GPSSD：通用型SSD云硬盘SSD：超高IO云硬盘

        :param resource_spec: The resource_spec of this DemandProductInfo.
        :type resource_spec: str
        """
        self._resource_spec = resource_spec

    @property
    def region(self):
        r"""Gets the region of this DemandProductInfo.

        云服务区编码，例如：“cn-north-1”。

        :return: The region of this DemandProductInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DemandProductInfo.

        云服务区编码，例如：“cn-north-1”。

        :param region: The region of this DemandProductInfo.
        :type region: str
        """
        self._region = region

    @property
    def available_zone(self):
        r"""Gets the available_zone of this DemandProductInfo.

        可用区标识。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The available_zone of this DemandProductInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this DemandProductInfo.

        可用区标识。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param available_zone: The available_zone of this DemandProductInfo.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def resource_size(self):
        r"""Gets the resource_size of this DemandProductInfo.

        资源容量大小，例如购买的卷大小或带宽大小。 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。

        :return: The resource_size of this DemandProductInfo.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this DemandProductInfo.

        资源容量大小，例如购买的卷大小或带宽大小。 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。

        :param resource_size: The resource_size of this DemandProductInfo.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def size_measure_id(self):
        r"""Gets the size_measure_id of this DemandProductInfo.

        资源容量度量标识，枚举值如下： 15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个（次） 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。

        :return: The size_measure_id of this DemandProductInfo.
        :rtype: int
        """
        return self._size_measure_id

    @size_measure_id.setter
    def size_measure_id(self, size_measure_id):
        r"""Sets the size_measure_id of this DemandProductInfo.

        资源容量度量标识，枚举值如下： 15：Mbps（购买带宽时使用）17：GB（购买云硬盘时使用）14：个（次） 线性产品时该参数不能为空。线性产品为包括硬盘，带宽等在订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小。非线性产品时此参数不携带或者携带值为null时，不作为筛选条件。

        :param size_measure_id: The size_measure_id of this DemandProductInfo.
        :type size_measure_id: int
        """
        self._size_measure_id = size_measure_id

    @property
    def usage_factor(self):
        r"""Gets the usage_factor of this DemandProductInfo.

        使用量因子编码，大小写不敏感，取值和话单中的使用量因子一致，云服务和使用量因子对应关系举例如下： 云服务器：Duration云硬盘：Duration弹性IP：Duration带宽：Duration或upflow市场镜像：Duration 您可以调用查询使用量类型列表接口获取响应参数表3中参数code的取值，即每种云服务对应的计费因子。

        :return: The usage_factor of this DemandProductInfo.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        r"""Sets the usage_factor of this DemandProductInfo.

        使用量因子编码，大小写不敏感，取值和话单中的使用量因子一致，云服务和使用量因子对应关系举例如下： 云服务器：Duration云硬盘：Duration弹性IP：Duration带宽：Duration或upflow市场镜像：Duration 您可以调用查询使用量类型列表接口获取响应参数表3中参数code的取值，即每种云服务对应的计费因子。

        :param usage_factor: The usage_factor of this DemandProductInfo.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def usage_value(self):
        r"""Gets the usage_value of this DemandProductInfo.

        使用量值。 例如按小时询价，使用量值为1，使用量单位为小时。

        :return: The usage_value of this DemandProductInfo.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._usage_value

    @usage_value.setter
    def usage_value(self, usage_value):
        r"""Sets the usage_value of this DemandProductInfo.

        使用量值。 例如按小时询价，使用量值为1，使用量单位为小时。

        :param usage_value: The usage_value of this DemandProductInfo.
        :type usage_value: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._usage_value = usage_value

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this DemandProductInfo.

        使用量度量单位， 例如按小时询价，使用量值为1，使用量单位为小时。

        :return: The usage_measure_id of this DemandProductInfo.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this DemandProductInfo.

        使用量度量单位， 例如按小时询价，使用量值为1，使用量单位为小时。

        :param usage_measure_id: The usage_measure_id of this DemandProductInfo.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this DemandProductInfo.

        订购数量。

        :return: The subscription_num of this DemandProductInfo.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this DemandProductInfo.

        订购数量。

        :param subscription_num: The subscription_num of this DemandProductInfo.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

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
        if not isinstance(other, DemandProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
