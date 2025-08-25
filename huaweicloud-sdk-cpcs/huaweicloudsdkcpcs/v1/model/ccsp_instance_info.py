# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CcspInstanceInfo:

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
        'resource_id': 'str',
        'instance_name': 'str',
        'service_type': 'str',
        'cluster_id': 'str',
        'is_normal': 'bool',
        'status': 'str',
        'image_name': 'str',
        'specification': 'str',
        'az': 'str',
        'expired_time': 'int',
        'create_time': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'resource_id': 'resource_id',
        'instance_name': 'instance_name',
        'service_type': 'service_type',
        'cluster_id': 'cluster_id',
        'is_normal': 'is_normal',
        'status': 'status',
        'image_name': 'image_name',
        'specification': 'specification',
        'az': 'az',
        'expired_time': 'expired_time',
        'create_time': 'create_time'
    }

    def __init__(self, instance_id=None, resource_id=None, instance_name=None, service_type=None, cluster_id=None, is_normal=None, status=None, image_name=None, specification=None, az=None, expired_time=None, create_time=None):
        r"""CcspInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param resource_id: cbc资源id
        :type resource_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param service_type: 实例所属的服务
        :type service_type: str
        :param cluster_id: 实例所属的集群的ID
        :type cluster_id: str
        :param is_normal: 实例的健康状态
        :type is_normal: bool
        :param status: 实例的服务状态
        :type status: str
        :param image_name: 实例的镜像名称
        :type image_name: str
        :param specification: 实例的虚机规格
        :type specification: str
        :param az: az
        :type az: str
        :param expired_time: 超期时间
        :type expired_time: int
        :param create_time: 实例的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        """
        
        

        self._instance_id = None
        self._resource_id = None
        self._instance_name = None
        self._service_type = None
        self._cluster_id = None
        self._is_normal = None
        self._status = None
        self._image_name = None
        self._specification = None
        self._az = None
        self._expired_time = None
        self._create_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if resource_id is not None:
            self.resource_id = resource_id
        self.instance_name = instance_name
        self.service_type = service_type
        self.cluster_id = cluster_id
        self.is_normal = is_normal
        self.status = status
        self.image_name = image_name
        self.specification = specification
        self.az = az
        if expired_time is not None:
            self.expired_time = expired_time
        self.create_time = create_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CcspInstanceInfo.

        实例ID

        :return: The instance_id of this CcspInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CcspInstanceInfo.

        实例ID

        :param instance_id: The instance_id of this CcspInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CcspInstanceInfo.

        cbc资源id

        :return: The resource_id of this CcspInstanceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CcspInstanceInfo.

        cbc资源id

        :param resource_id: The resource_id of this CcspInstanceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this CcspInstanceInfo.

        实例名称

        :return: The instance_name of this CcspInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this CcspInstanceInfo.

        实例名称

        :param instance_name: The instance_name of this CcspInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def service_type(self):
        r"""Gets the service_type of this CcspInstanceInfo.

        实例所属的服务

        :return: The service_type of this CcspInstanceInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CcspInstanceInfo.

        实例所属的服务

        :param service_type: The service_type of this CcspInstanceInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CcspInstanceInfo.

        实例所属的集群的ID

        :return: The cluster_id of this CcspInstanceInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CcspInstanceInfo.

        实例所属的集群的ID

        :param cluster_id: The cluster_id of this CcspInstanceInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def is_normal(self):
        r"""Gets the is_normal of this CcspInstanceInfo.

        实例的健康状态

        :return: The is_normal of this CcspInstanceInfo.
        :rtype: bool
        """
        return self._is_normal

    @is_normal.setter
    def is_normal(self, is_normal):
        r"""Sets the is_normal of this CcspInstanceInfo.

        实例的健康状态

        :param is_normal: The is_normal of this CcspInstanceInfo.
        :type is_normal: bool
        """
        self._is_normal = is_normal

    @property
    def status(self):
        r"""Gets the status of this CcspInstanceInfo.

        实例的服务状态

        :return: The status of this CcspInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CcspInstanceInfo.

        实例的服务状态

        :param status: The status of this CcspInstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def image_name(self):
        r"""Gets the image_name of this CcspInstanceInfo.

        实例的镜像名称

        :return: The image_name of this CcspInstanceInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CcspInstanceInfo.

        实例的镜像名称

        :param image_name: The image_name of this CcspInstanceInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def specification(self):
        r"""Gets the specification of this CcspInstanceInfo.

        实例的虚机规格

        :return: The specification of this CcspInstanceInfo.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this CcspInstanceInfo.

        实例的虚机规格

        :param specification: The specification of this CcspInstanceInfo.
        :type specification: str
        """
        self._specification = specification

    @property
    def az(self):
        r"""Gets the az of this CcspInstanceInfo.

        az

        :return: The az of this CcspInstanceInfo.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this CcspInstanceInfo.

        az

        :param az: The az of this CcspInstanceInfo.
        :type az: str
        """
        self._az = az

    @property
    def expired_time(self):
        r"""Gets the expired_time of this CcspInstanceInfo.

        超期时间

        :return: The expired_time of this CcspInstanceInfo.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this CcspInstanceInfo.

        超期时间

        :param expired_time: The expired_time of this CcspInstanceInfo.
        :type expired_time: int
        """
        self._expired_time = expired_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CcspInstanceInfo.

        实例的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this CcspInstanceInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CcspInstanceInfo.

        实例的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this CcspInstanceInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, CcspInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
