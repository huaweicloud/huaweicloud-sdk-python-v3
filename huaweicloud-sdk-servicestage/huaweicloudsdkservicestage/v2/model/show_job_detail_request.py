# coding: utf-8

import pprint
import re

import six





class ShowJobDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'desc': 'desc'
    }

    def __init__(self, job_id=None, instance_id=None, limit=20, offset=0, desc='false'):
        """ShowJobDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._job_id = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._desc = None
        self.discriminator = None

        self.job_id = job_id
        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if desc is not None:
            self.desc = desc

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobDetailRequest.


        :return: The job_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobDetailRequest.


        :param job_id: The job_id of this ShowJobDetailRequest.
        :type: str
        """
        self._job_id = job_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowJobDetailRequest.


        :return: The instance_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowJobDetailRequest.


        :param instance_id: The instance_id of this ShowJobDetailRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ShowJobDetailRequest.


        :return: The limit of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowJobDetailRequest.


        :param limit: The limit of this ShowJobDetailRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowJobDetailRequest.


        :return: The offset of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowJobDetailRequest.


        :param offset: The offset of this ShowJobDetailRequest.
        :type: int
        """
        self._offset = offset

    @property
    def desc(self):
        """Gets the desc of this ShowJobDetailRequest.


        :return: The desc of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ShowJobDetailRequest.


        :param desc: The desc of this ShowJobDetailRequest.
        :type: str
        """
        self._desc = desc

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
        if not isinstance(other, ShowJobDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
