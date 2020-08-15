# coding: utf-8

import pprint
import re

import six





class Entity:


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
        'spec_type': 'str',
        'spec_size': 'float',
        'measure': 'int',
        'processed_time': 'str',
        'is_main_resource': 'int',
        'main_resources': 'list[RelativeResource]',
        'sub_resources': 'list[RelativeResource]',
        'extend_params': 'str'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'resource_name': 'resourceName',
        'cloud_service_type': 'cloudServiceType',
        'resource_type': 'resourceType',
        'resource_spec_code': 'resourceSpecCode',
        'spec_type': 'specType',
        'spec_size': 'specSize',
        'measure': 'measure',
        'processed_time': 'processedTime',
        'is_main_resource': 'isMainResource',
        'main_resources': 'mainResources',
        'sub_resources': 'subResources',
        'extend_params': 'extendParams'
    }

    def __init__(self, resource_id=None, resource_name=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, spec_type=None, spec_size=None, measure=None, processed_time=None, is_main_resource=None, main_resources=None, sub_resources=None, extend_params=None):
        """Entity - a model defined in huaweicloud sdk"""
        
        

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
        self._sub_resources = None
        self._extend_params = None
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
        if sub_resources is not None:
            self.sub_resources = sub_resources
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def resource_id(self):
        """Gets the resource_id of this Entity.

        资源Id

        :return: The resource_id of this Entity.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Entity.

        资源Id

        :param resource_id: The resource_id of this Entity.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this Entity.

        资源名称

        :return: The resource_name of this Entity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Entity.

        资源名称

        :param resource_name: The resource_name of this Entity.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this Entity.

        云服务类型编码

        :return: The cloud_service_type of this Entity.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this Entity.

        云服务类型编码

        :param cloud_service_type: The cloud_service_type of this Entity.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this Entity.

        资源类型

        :return: The resource_type of this Entity.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Entity.

        资源类型

        :param resource_type: The resource_type of this Entity.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this Entity.

        资源规格编码

        :return: The resource_spec_code of this Entity.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this Entity.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this Entity.
        :type: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def spec_type(self):
        """Gets the spec_type of this Entity.

        规格类型

        :return: The spec_type of this Entity.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this Entity.

        规格类型

        :param spec_type: The spec_type of this Entity.
        :type: str
        """
        self._spec_type = spec_type

    @property
    def spec_size(self):
        """Gets the spec_size of this Entity.

        规格属性大小

        :return: The spec_size of this Entity.
        :rtype: float
        """
        return self._spec_size

    @spec_size.setter
    def spec_size(self, spec_size):
        """Sets the spec_size of this Entity.

        规格属性大小

        :param spec_size: The spec_size of this Entity.
        :type: float
        """
        self._spec_size = spec_size

    @property
    def measure(self):
        """Gets the measure of this Entity.

        规格属性的单位

        :return: The measure of this Entity.
        :rtype: int
        """
        return self._measure

    @measure.setter
    def measure(self, measure):
        """Sets the measure of this Entity.

        规格属性的单位

        :param measure: The measure of this Entity.
        :type: int
        """
        self._measure = measure

    @property
    def processed_time(self):
        """Gets the processed_time of this Entity.

        处理时间

        :return: The processed_time of this Entity.
        :rtype: str
        """
        return self._processed_time

    @processed_time.setter
    def processed_time(self, processed_time):
        """Sets the processed_time of this Entity.

        处理时间

        :param processed_time: The processed_time of this Entity.
        :type: str
        """
        self._processed_time = processed_time

    @property
    def is_main_resource(self):
        """Gets the is_main_resource of this Entity.

        是否主要资源

        :return: The is_main_resource of this Entity.
        :rtype: int
        """
        return self._is_main_resource

    @is_main_resource.setter
    def is_main_resource(self, is_main_resource):
        """Sets the is_main_resource of this Entity.

        是否主要资源

        :param is_main_resource: The is_main_resource of this Entity.
        :type: int
        """
        self._is_main_resource = is_main_resource

    @property
    def main_resources(self):
        """Gets the main_resources of this Entity.

        主要资源列表

        :return: The main_resources of this Entity.
        :rtype: list[RelativeResource]
        """
        return self._main_resources

    @main_resources.setter
    def main_resources(self, main_resources):
        """Sets the main_resources of this Entity.

        主要资源列表

        :param main_resources: The main_resources of this Entity.
        :type: list[RelativeResource]
        """
        self._main_resources = main_resources

    @property
    def sub_resources(self):
        """Gets the sub_resources of this Entity.

        子资源列表

        :return: The sub_resources of this Entity.
        :rtype: list[RelativeResource]
        """
        return self._sub_resources

    @sub_resources.setter
    def sub_resources(self, sub_resources):
        """Sets the sub_resources of this Entity.

        子资源列表

        :param sub_resources: The sub_resources of this Entity.
        :type: list[RelativeResource]
        """
        self._sub_resources = sub_resources

    @property
    def extend_params(self):
        """Gets the extend_params of this Entity.

        扩展参数

        :return: The extend_params of this Entity.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        """Sets the extend_params of this Entity.

        扩展参数

        :param extend_params: The extend_params of this Entity.
        :type: str
        """
        self._extend_params = extend_params

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Entity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
