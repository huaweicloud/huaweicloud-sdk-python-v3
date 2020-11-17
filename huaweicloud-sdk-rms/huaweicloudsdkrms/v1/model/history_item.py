# coding: utf-8

import pprint
import re

import six





class HistoryItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'capture_time': 'str',
        'status': 'str',
        'relations': 'list[ResourceRelation]',
        'resource': 'ResourceEntity'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'capture_time': 'capture_time',
        'status': 'status',
        'relations': 'relations',
        'resource': 'resource'
    }

    def __init__(self, domain_id=None, resource_id=None, resource_type=None, capture_time=None, status=None, relations=None, resource=None):
        """HistoryItem - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._resource_id = None
        self._resource_type = None
        self._capture_time = None
        self._status = None
        self._relations = None
        self._resource = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if capture_time is not None:
            self.capture_time = capture_time
        if status is not None:
            self.status = status
        if relations is not None:
            self.relations = relations
        if resource is not None:
            self.resource = resource

    @property
    def domain_id(self):
        """Gets the domain_id of this HistoryItem.

        租户id

        :return: The domain_id of this HistoryItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this HistoryItem.

        租户id

        :param domain_id: The domain_id of this HistoryItem.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def resource_id(self):
        """Gets the resource_id of this HistoryItem.

        资源id

        :return: The resource_id of this HistoryItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this HistoryItem.

        资源id

        :param resource_id: The resource_id of this HistoryItem.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this HistoryItem.

        资源类型

        :return: The resource_type of this HistoryItem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this HistoryItem.

        资源类型

        :param resource_type: The resource_type of this HistoryItem.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def capture_time(self):
        """Gets the capture_time of this HistoryItem.

        该资源在RMS系统捕获时间

        :return: The capture_time of this HistoryItem.
        :rtype: str
        """
        return self._capture_time

    @capture_time.setter
    def capture_time(self, capture_time):
        """Sets the capture_time of this HistoryItem.

        该资源在RMS系统捕获时间

        :param capture_time: The capture_time of this HistoryItem.
        :type: str
        """
        self._capture_time = capture_time

    @property
    def status(self):
        """Gets the status of this HistoryItem.

        资源状态

        :return: The status of this HistoryItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HistoryItem.

        资源状态

        :param status: The status of this HistoryItem.
        :type: str
        """
        self._status = status

    @property
    def relations(self):
        """Gets the relations of this HistoryItem.

        资源关系列表

        :return: The relations of this HistoryItem.
        :rtype: list[ResourceRelation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this HistoryItem.

        资源关系列表

        :param relations: The relations of this HistoryItem.
        :type: list[ResourceRelation]
        """
        self._relations = relations

    @property
    def resource(self):
        """Gets the resource of this HistoryItem.


        :return: The resource of this HistoryItem.
        :rtype: ResourceEntity
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this HistoryItem.


        :param resource: The resource of this HistoryItem.
        :type: ResourceEntity
        """
        self._resource = resource

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
        if not isinstance(other, HistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
