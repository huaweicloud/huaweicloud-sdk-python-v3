# coding: utf-8

import pprint
import re

import six





class ObsBucket:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'creation_date': 'str',
        'is_authorized': 'int'
    }

    attribute_map = {
        'bucket': 'bucket',
        'creation_date': 'creation_date',
        'is_authorized': 'is_authorized'
    }

    def __init__(self, bucket=None, creation_date=None, is_authorized=None):
        """ObsBucket - a model defined in huaweicloud sdk"""
        
        

        self._bucket = None
        self._creation_date = None
        self._is_authorized = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if creation_date is not None:
            self.creation_date = creation_date
        if is_authorized is not None:
            self.is_authorized = is_authorized

    @property
    def bucket(self):
        """Gets the bucket of this ObsBucket.

        桶名称 

        :return: The bucket of this ObsBucket.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ObsBucket.

        桶名称 

        :param bucket: The bucket of this ObsBucket.
        :type: str
        """
        self._bucket = bucket

    @property
    def creation_date(self):
        """Gets the creation_date of this ObsBucket.

        桶的创建时间 

        :return: The creation_date of this ObsBucket.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ObsBucket.

        桶的创建时间 

        :param creation_date: The creation_date of this ObsBucket.
        :type: str
        """
        self._creation_date = creation_date

    @property
    def is_authorized(self):
        """Gets the is_authorized of this ObsBucket.

        授权结果，取值[0,1]，0表示未授权给转码服务，1表示已授权转码服务 

        :return: The is_authorized of this ObsBucket.
        :rtype: int
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this ObsBucket.

        授权结果，取值[0,1]，0表示未授权给转码服务，1表示已授权转码服务 

        :param is_authorized: The is_authorized of this ObsBucket.
        :type: int
        """
        self._is_authorized = is_authorized

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
        if not isinstance(other, ObsBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
