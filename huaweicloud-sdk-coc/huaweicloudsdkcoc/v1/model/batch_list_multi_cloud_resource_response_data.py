# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListMultiCloudResourceResponseData:

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
        'resource_id': 'str',
        'name': 'str',
        'vendor': 'str',
        'type': 'str',
        'datasource': 'str',
        'region_id': 'str',
        'properties': 'dict(str, object)',
        'create_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'name': 'name',
        'vendor': 'vendor',
        'type': 'type',
        'datasource': 'datasource',
        'region_id': 'region_id',
        'properties': 'properties',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, resource_id=None, name=None, vendor=None, type=None, datasource=None, region_id=None, properties=None, create_time=None):
        """BatchListMultiCloudResourceResponseData

        The model defined in huaweicloud sdk

        :param id: CMDB生成uuid
        :type id: str
        :param resource_id: 在云厂商上存的资源id
        :type resource_id: str
        :param name: 资源名称
        :type name: str
        :param vendor: 云厂商
        :type vendor: str
        :param type: 资源类型
        :type type: str
        :param datasource: 云厂商账户id
        :type datasource: str
        :param region_id: regionId
        :type region_id: str
        :param properties: 资源详细属性
        :type properties: dict(str, object)
        :param create_time: 资源创建时间
        :type create_time: str
        """
        
        

        self._id = None
        self._resource_id = None
        self._name = None
        self._vendor = None
        self._type = None
        self._datasource = None
        self._region_id = None
        self._properties = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor
        if type is not None:
            self.type = type
        if datasource is not None:
            self.datasource = datasource
        if region_id is not None:
            self.region_id = region_id
        if properties is not None:
            self.properties = properties
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this BatchListMultiCloudResourceResponseData.

        CMDB生成uuid

        :return: The id of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchListMultiCloudResourceResponseData.

        CMDB生成uuid

        :param id: The id of this BatchListMultiCloudResourceResponseData.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this BatchListMultiCloudResourceResponseData.

        在云厂商上存的资源id

        :return: The resource_id of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BatchListMultiCloudResourceResponseData.

        在云厂商上存的资源id

        :param resource_id: The resource_id of this BatchListMultiCloudResourceResponseData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this BatchListMultiCloudResourceResponseData.

        资源名称

        :return: The name of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchListMultiCloudResourceResponseData.

        资源名称

        :param name: The name of this BatchListMultiCloudResourceResponseData.
        :type name: str
        """
        self._name = name

    @property
    def vendor(self):
        """Gets the vendor of this BatchListMultiCloudResourceResponseData.

        云厂商

        :return: The vendor of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this BatchListMultiCloudResourceResponseData.

        云厂商

        :param vendor: The vendor of this BatchListMultiCloudResourceResponseData.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def type(self):
        """Gets the type of this BatchListMultiCloudResourceResponseData.

        资源类型

        :return: The type of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchListMultiCloudResourceResponseData.

        资源类型

        :param type: The type of this BatchListMultiCloudResourceResponseData.
        :type type: str
        """
        self._type = type

    @property
    def datasource(self):
        """Gets the datasource of this BatchListMultiCloudResourceResponseData.

        云厂商账户id

        :return: The datasource of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this BatchListMultiCloudResourceResponseData.

        云厂商账户id

        :param datasource: The datasource of this BatchListMultiCloudResourceResponseData.
        :type datasource: str
        """
        self._datasource = datasource

    @property
    def region_id(self):
        """Gets the region_id of this BatchListMultiCloudResourceResponseData.

        regionId

        :return: The region_id of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this BatchListMultiCloudResourceResponseData.

        regionId

        :param region_id: The region_id of this BatchListMultiCloudResourceResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def properties(self):
        """Gets the properties of this BatchListMultiCloudResourceResponseData.

        资源详细属性

        :return: The properties of this BatchListMultiCloudResourceResponseData.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BatchListMultiCloudResourceResponseData.

        资源详细属性

        :param properties: The properties of this BatchListMultiCloudResourceResponseData.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def create_time(self):
        """Gets the create_time of this BatchListMultiCloudResourceResponseData.

        资源创建时间

        :return: The create_time of this BatchListMultiCloudResourceResponseData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BatchListMultiCloudResourceResponseData.

        资源创建时间

        :param create_time: The create_time of this BatchListMultiCloudResourceResponseData.
        :type create_time: str
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
        if not isinstance(other, BatchListMultiCloudResourceResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
