# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'spec_type': 'dict(str, object)',
        'spec_size': 'float',
        'measure': 'int',
        'processed_time': 'datetime',
        'is_main_resource': 'int',
        'main_resources': 'list[RelativeResource]',
        'extend_params': 'str',
        'old_resource_id': 'str',
        'old_cloud_service_type': 'str',
        'old_resource_type': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'spec_type': 'spec_type',
        'spec_size': 'spec_size',
        'measure': 'measure',
        'processed_time': 'processed_time',
        'is_main_resource': 'is_main_resource',
        'main_resources': 'main_resources',
        'extend_params': 'extend_params',
        'old_resource_id': 'old_resource_id',
        'old_cloud_service_type': 'old_cloud_service_type',
        'old_resource_type': 'old_resource_type'
    }

    def __init__(self, resource_id=None, resource_name=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, spec_type=None, spec_size=None, measure=None, processed_time=None, is_main_resource=None, main_resources=None, extend_params=None, old_resource_id=None, old_cloud_service_type=None, old_resource_type=None):
        """JobResourceInfo

        The model defined in huaweicloud sdk

        :param resource_id: 客户在云服务Console上可见的资源实例Id，全局唯一，且不可更改，最大64个字符。  注：“规格变更”场景下（包括升降配），是对某个资源实例的规格进行调整，  该资源实例其他信息（比如资源Id、资源名称）和运行的业务数据不变化。
        :type resource_id: str
        :param resource_name: 资源名称；创建、有最新资源名称场景，必填。
        :type resource_name: str
        :param cloud_service_type: 云服务类型编码；新购、规格变更场景，必填。
        :type cloud_service_type: str
        :param resource_type: 资源类型编码；新购、规格变更场景，必填。
        :type resource_type: str
        :param resource_spec_code: 资源规格编码；新购、规格变更场景，必填。
        :type resource_spec_code: str
        :param spec_type: 规格类型，运营上需要呈现和使用的一些规格属性，多个使用K:V格式； 比如带宽的共享/独享(shareable:true/false)，数据盘的系统盘/数据盘类型(root:true/false) 当前针对共享带宽、共享盘使用，必填。
        :type spec_type: dict(str, object)
        :param spec_size: 某些规格属性大小：比如带宽大小、数据盘大小
        :type spec_size: float
        :param measure: specSize的单位编码，比如GB、M，有specSize时，此字段必填。
        :type measure: int
        :param processed_time: 处理时间
        :type processed_time: datetime
        :param is_main_resource: 该resourceId是否是主资源（仅开通场景使用，其他场景为空） * &#x60;1&#x60; - 是 * &#x60;0&#x60; - 否
        :type is_main_resource: int
        :param main_resources: resourceId的主资源。  是挂载到/绑定到/依附到/包含于/关联到资源，比如IP的主资源‘云主机’、数据盘的主资源‘云主机’。  如果resourceId是依附在多个资源上，则有多个主资源，比如共享盘挂载到多个云主机上。  无关联主资源，则空，比如独立未挂载的数据盘。
        :type main_resources: list[:class:`huaweicloudsdkworkspaceapp.v1.RelativeResource`]
        :param extend_params: expireTime：到期时间，域名注册服务使用。  UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ（2016-06-28T00:00:00Z）
        :type extend_params: str
        :param old_resource_id: 仅针对ECS/BMS云服务的“切换操作系统”场景使用： 云主机切换操作系统的资源id会变化场景 填写变更前老的资源Id。资源Id未变化，无此字段
        :type old_resource_id: str
        :param old_cloud_service_type: 仅针对ECS/BMS云服务的“切换操作系统”场景使用：云主机切换操作系统的云服务类型编码会变化场景， 填写变更前老的云服务类型编码。云服务类型未变化，无此字段。
        :type old_cloud_service_type: str
        :param old_resource_type: 仅针对ECS/BMS云服务“切换操作系统”场景使用： 云主机切换操作系统的资源类型编码会变化场景， 填写变更前老的资源类型编码。资源类型未变化，无此字段
        :type old_resource_type: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._spec_type = None
        self._spec_size = None
        self._measure = None
        self._processed_time = None
        self._is_main_resource = None
        self._main_resources = None
        self._extend_params = None
        self._old_resource_id = None
        self._old_cloud_service_type = None
        self._old_resource_type = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if spec_type is not None:
            self.spec_type = spec_type
        if spec_size is not None:
            self.spec_size = spec_size
        if measure is not None:
            self.measure = measure
        if processed_time is not None:
            self.processed_time = processed_time
        if is_main_resource is not None:
            self.is_main_resource = is_main_resource
        if main_resources is not None:
            self.main_resources = main_resources
        if extend_params is not None:
            self.extend_params = extend_params
        if old_resource_id is not None:
            self.old_resource_id = old_resource_id
        if old_cloud_service_type is not None:
            self.old_cloud_service_type = old_cloud_service_type
        if old_resource_type is not None:
            self.old_resource_type = old_resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this JobResourceInfo.

        客户在云服务Console上可见的资源实例Id，全局唯一，且不可更改，最大64个字符。  注：“规格变更”场景下（包括升降配），是对某个资源实例的规格进行调整，  该资源实例其他信息（比如资源Id、资源名称）和运行的业务数据不变化。

        :return: The resource_id of this JobResourceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this JobResourceInfo.

        客户在云服务Console上可见的资源实例Id，全局唯一，且不可更改，最大64个字符。  注：“规格变更”场景下（包括升降配），是对某个资源实例的规格进行调整，  该资源实例其他信息（比如资源Id、资源名称）和运行的业务数据不变化。

        :param resource_id: The resource_id of this JobResourceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this JobResourceInfo.

        资源名称；创建、有最新资源名称场景，必填。

        :return: The resource_name of this JobResourceInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this JobResourceInfo.

        资源名称；创建、有最新资源名称场景，必填。

        :param resource_name: The resource_name of this JobResourceInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this JobResourceInfo.

        云服务类型编码；新购、规格变更场景，必填。

        :return: The cloud_service_type of this JobResourceInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this JobResourceInfo.

        云服务类型编码；新购、规格变更场景，必填。

        :param cloud_service_type: The cloud_service_type of this JobResourceInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this JobResourceInfo.

        资源类型编码；新购、规格变更场景，必填。

        :return: The resource_type of this JobResourceInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JobResourceInfo.

        资源类型编码；新购、规格变更场景，必填。

        :param resource_type: The resource_type of this JobResourceInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this JobResourceInfo.

        资源规格编码；新购、规格变更场景，必填。

        :return: The resource_spec_code of this JobResourceInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this JobResourceInfo.

        资源规格编码；新购、规格变更场景，必填。

        :param resource_spec_code: The resource_spec_code of this JobResourceInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def spec_type(self):
        """Gets the spec_type of this JobResourceInfo.

        规格类型，运营上需要呈现和使用的一些规格属性，多个使用K:V格式； 比如带宽的共享/独享(shareable:true/false)，数据盘的系统盘/数据盘类型(root:true/false) 当前针对共享带宽、共享盘使用，必填。

        :return: The spec_type of this JobResourceInfo.
        :rtype: dict(str, object)
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this JobResourceInfo.

        规格类型，运营上需要呈现和使用的一些规格属性，多个使用K:V格式； 比如带宽的共享/独享(shareable:true/false)，数据盘的系统盘/数据盘类型(root:true/false) 当前针对共享带宽、共享盘使用，必填。

        :param spec_type: The spec_type of this JobResourceInfo.
        :type spec_type: dict(str, object)
        """
        self._spec_type = spec_type

    @property
    def spec_size(self):
        """Gets the spec_size of this JobResourceInfo.

        某些规格属性大小：比如带宽大小、数据盘大小

        :return: The spec_size of this JobResourceInfo.
        :rtype: float
        """
        return self._spec_size

    @spec_size.setter
    def spec_size(self, spec_size):
        """Sets the spec_size of this JobResourceInfo.

        某些规格属性大小：比如带宽大小、数据盘大小

        :param spec_size: The spec_size of this JobResourceInfo.
        :type spec_size: float
        """
        self._spec_size = spec_size

    @property
    def measure(self):
        """Gets the measure of this JobResourceInfo.

        specSize的单位编码，比如GB、M，有specSize时，此字段必填。

        :return: The measure of this JobResourceInfo.
        :rtype: int
        """
        return self._measure

    @measure.setter
    def measure(self, measure):
        """Sets the measure of this JobResourceInfo.

        specSize的单位编码，比如GB、M，有specSize时，此字段必填。

        :param measure: The measure of this JobResourceInfo.
        :type measure: int
        """
        self._measure = measure

    @property
    def processed_time(self):
        """Gets the processed_time of this JobResourceInfo.

        处理时间

        :return: The processed_time of this JobResourceInfo.
        :rtype: datetime
        """
        return self._processed_time

    @processed_time.setter
    def processed_time(self, processed_time):
        """Sets the processed_time of this JobResourceInfo.

        处理时间

        :param processed_time: The processed_time of this JobResourceInfo.
        :type processed_time: datetime
        """
        self._processed_time = processed_time

    @property
    def is_main_resource(self):
        """Gets the is_main_resource of this JobResourceInfo.

        该resourceId是否是主资源（仅开通场景使用，其他场景为空） * `1` - 是 * `0` - 否

        :return: The is_main_resource of this JobResourceInfo.
        :rtype: int
        """
        return self._is_main_resource

    @is_main_resource.setter
    def is_main_resource(self, is_main_resource):
        """Sets the is_main_resource of this JobResourceInfo.

        该resourceId是否是主资源（仅开通场景使用，其他场景为空） * `1` - 是 * `0` - 否

        :param is_main_resource: The is_main_resource of this JobResourceInfo.
        :type is_main_resource: int
        """
        self._is_main_resource = is_main_resource

    @property
    def main_resources(self):
        """Gets the main_resources of this JobResourceInfo.

        resourceId的主资源。  是挂载到/绑定到/依附到/包含于/关联到资源，比如IP的主资源‘云主机’、数据盘的主资源‘云主机’。  如果resourceId是依附在多个资源上，则有多个主资源，比如共享盘挂载到多个云主机上。  无关联主资源，则空，比如独立未挂载的数据盘。

        :return: The main_resources of this JobResourceInfo.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.RelativeResource`]
        """
        return self._main_resources

    @main_resources.setter
    def main_resources(self, main_resources):
        """Sets the main_resources of this JobResourceInfo.

        resourceId的主资源。  是挂载到/绑定到/依附到/包含于/关联到资源，比如IP的主资源‘云主机’、数据盘的主资源‘云主机’。  如果resourceId是依附在多个资源上，则有多个主资源，比如共享盘挂载到多个云主机上。  无关联主资源，则空，比如独立未挂载的数据盘。

        :param main_resources: The main_resources of this JobResourceInfo.
        :type main_resources: list[:class:`huaweicloudsdkworkspaceapp.v1.RelativeResource`]
        """
        self._main_resources = main_resources

    @property
    def extend_params(self):
        """Gets the extend_params of this JobResourceInfo.

        expireTime：到期时间，域名注册服务使用。  UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ（2016-06-28T00:00:00Z）

        :return: The extend_params of this JobResourceInfo.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        """Sets the extend_params of this JobResourceInfo.

        expireTime：到期时间，域名注册服务使用。  UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ（2016-06-28T00:00:00Z）

        :param extend_params: The extend_params of this JobResourceInfo.
        :type extend_params: str
        """
        self._extend_params = extend_params

    @property
    def old_resource_id(self):
        """Gets the old_resource_id of this JobResourceInfo.

        仅针对ECS/BMS云服务的“切换操作系统”场景使用： 云主机切换操作系统的资源id会变化场景 填写变更前老的资源Id。资源Id未变化，无此字段

        :return: The old_resource_id of this JobResourceInfo.
        :rtype: str
        """
        return self._old_resource_id

    @old_resource_id.setter
    def old_resource_id(self, old_resource_id):
        """Sets the old_resource_id of this JobResourceInfo.

        仅针对ECS/BMS云服务的“切换操作系统”场景使用： 云主机切换操作系统的资源id会变化场景 填写变更前老的资源Id。资源Id未变化，无此字段

        :param old_resource_id: The old_resource_id of this JobResourceInfo.
        :type old_resource_id: str
        """
        self._old_resource_id = old_resource_id

    @property
    def old_cloud_service_type(self):
        """Gets the old_cloud_service_type of this JobResourceInfo.

        仅针对ECS/BMS云服务的“切换操作系统”场景使用：云主机切换操作系统的云服务类型编码会变化场景， 填写变更前老的云服务类型编码。云服务类型未变化，无此字段。

        :return: The old_cloud_service_type of this JobResourceInfo.
        :rtype: str
        """
        return self._old_cloud_service_type

    @old_cloud_service_type.setter
    def old_cloud_service_type(self, old_cloud_service_type):
        """Sets the old_cloud_service_type of this JobResourceInfo.

        仅针对ECS/BMS云服务的“切换操作系统”场景使用：云主机切换操作系统的云服务类型编码会变化场景， 填写变更前老的云服务类型编码。云服务类型未变化，无此字段。

        :param old_cloud_service_type: The old_cloud_service_type of this JobResourceInfo.
        :type old_cloud_service_type: str
        """
        self._old_cloud_service_type = old_cloud_service_type

    @property
    def old_resource_type(self):
        """Gets the old_resource_type of this JobResourceInfo.

        仅针对ECS/BMS云服务“切换操作系统”场景使用： 云主机切换操作系统的资源类型编码会变化场景， 填写变更前老的资源类型编码。资源类型未变化，无此字段

        :return: The old_resource_type of this JobResourceInfo.
        :rtype: str
        """
        return self._old_resource_type

    @old_resource_type.setter
    def old_resource_type(self, old_resource_type):
        """Sets the old_resource_type of this JobResourceInfo.

        仅针对ECS/BMS云服务“切换操作系统”场景使用： 云主机切换操作系统的资源类型编码会变化场景， 填写变更前老的资源类型编码。资源类型未变化，无此字段

        :param old_resource_type: The old_resource_type of this JobResourceInfo.
        :type old_resource_type: str
        """
        self._old_resource_type = old_resource_type

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
        if not isinstance(other, JobResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
