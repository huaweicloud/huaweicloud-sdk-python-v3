# coding: utf-8

import re
import six





class CloudWafSubscriptioResponseResources:


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
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'status': 'int',
        'expire_time': 'str',
        'resource_size': 'int'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'cloud_service_type': 'cloudServiceType',
        'resource_type': 'resourceType',
        'resource_spec_code': 'resourceSpecCode',
        'status': 'status',
        'expire_time': 'expireTime',
        'resource_size': 'resourceSize'
    }

    def __init__(self, resource_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, status=None, expire_time=None, resource_size=None):
        """CloudWafSubscriptioResponseResources - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._status = None
        self._expire_time = None
        self._resource_size = None
        self.discriminator = None

        self.resource_id = resource_id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code
        if status is not None:
            self.status = status
        if expire_time is not None:
            self.expire_time = expire_time
        if resource_size is not None:
            self.resource_size = resource_size

    @property
    def resource_id(self):
        """Gets the resource_id of this CloudWafSubscriptioResponseResources.

        资源id

        :return: The resource_id of this CloudWafSubscriptioResponseResources.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CloudWafSubscriptioResponseResources.

        资源id

        :param resource_id: The resource_id of this CloudWafSubscriptioResponseResources.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this CloudWafSubscriptioResponseResources.

        云服务产品对应的云服务类型

        :return: The cloud_service_type of this CloudWafSubscriptioResponseResources.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this CloudWafSubscriptioResponseResources.

        云服务产品对应的云服务类型

        :param cloud_service_type: The cloud_service_type of this CloudWafSubscriptioResponseResources.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this CloudWafSubscriptioResponseResources.

        云服务产品的资源类型

        :return: The resource_type of this CloudWafSubscriptioResponseResources.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CloudWafSubscriptioResponseResources.

        云服务产品的资源类型

        :param resource_type: The resource_type of this CloudWafSubscriptioResponseResources.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CloudWafSubscriptioResponseResources.

        云服务产品的资源规格

        :return: The resource_spec_code of this CloudWafSubscriptioResponseResources.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CloudWafSubscriptioResponseResources.

        云服务产品的资源规格

        :param resource_spec_code: The resource_spec_code of this CloudWafSubscriptioResponseResources.
        :type: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def status(self):
        """Gets the status of this CloudWafSubscriptioResponseResources.

        资源状态，0：解冻/正常，1：冻结，2：删除

        :return: The status of this CloudWafSubscriptioResponseResources.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudWafSubscriptioResponseResources.

        资源状态，0：解冻/正常，1：冻结，2：删除

        :param status: The status of this CloudWafSubscriptioResponseResources.
        :type: int
        """
        self._status = status

    @property
    def expire_time(self):
        """Gets the expire_time of this CloudWafSubscriptioResponseResources.

        资源到期时间

        :return: The expire_time of this CloudWafSubscriptioResponseResources.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CloudWafSubscriptioResponseResources.

        资源到期时间

        :param expire_time: The expire_time of this CloudWafSubscriptioResponseResources.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def resource_size(self):
        """Gets the resource_size of this CloudWafSubscriptioResponseResources.

        资源数量

        :return: The resource_size of this CloudWafSubscriptioResponseResources.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this CloudWafSubscriptioResponseResources.

        资源数量

        :param resource_size: The resource_size of this CloudWafSubscriptioResponseResources.
        :type: int
        """
        self._resource_size = resource_size

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudWafSubscriptioResponseResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
