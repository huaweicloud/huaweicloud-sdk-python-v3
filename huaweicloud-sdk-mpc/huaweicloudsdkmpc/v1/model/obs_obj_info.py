# coding: utf-8

import pprint
import re

import six





class ObsObjInfo:


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
        'location': 'str',
        'object': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'location': 'location',
        'object': 'object',
        'file_name': 'file_name'
    }

    def __init__(self, bucket=None, location=None, object=None, file_name=None):
        """ObsObjInfo - a model defined in huaweicloud sdk"""
        
        

        self._bucket = None
        self._location = None
        self._object = None
        self._file_name = None
        self.discriminator = None

        self.bucket = bucket
        self.location = location
        self.object = object
        if file_name is not None:
            self.file_name = file_name

    @property
    def bucket(self):
        """Gets the bucket of this ObsObjInfo.

        OBS的bucket名称。 

        :return: The bucket of this ObsObjInfo.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ObsObjInfo.

        OBS的bucket名称。 

        :param bucket: The bucket of this ObsObjInfo.
        :type: str
        """
        self._bucket = bucket

    @property
    def location(self):
        """Gets the location of this ObsObjInfo.

        OBS桶所在的区域，且必须与使用的MPC区域保持一致。 

        :return: The location of this ObsObjInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ObsObjInfo.

        OBS桶所在的区域，且必须与使用的MPC区域保持一致。 

        :param location: The location of this ObsObjInfo.
        :type: str
        """
        self._location = location

    @property
    def object(self):
        """Gets the object of this ObsObjInfo.

        OBS对象路径，遵守OSS Object定义。  - 当用于指示input时,需要指定到具体对象。 - 当用于指示output时, 只需指定到转码结果期望存放的路径。 

        :return: The object of this ObsObjInfo.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ObsObjInfo.

        OBS对象路径，遵守OSS Object定义。  - 当用于指示input时,需要指定到具体对象。 - 当用于指示output时, 只需指定到转码结果期望存放的路径。 

        :param object: The object of this ObsObjInfo.
        :type: str
        """
        self._object = object

    @property
    def file_name(self):
        """Gets the file_name of this ObsObjInfo.

        文件名，仅用于转封装指定输出名称。  - 当指定了此参数时，输出的对象名为object/file_name 。 - 当不指定此参数时，输出的对象名为object/xxx，其中xxx由MPC指定。 

        :return: The file_name of this ObsObjInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ObsObjInfo.

        文件名，仅用于转封装指定输出名称。  - 当指定了此参数时，输出的对象名为object/file_name 。 - 当不指定此参数时，输出的对象名为object/xxx，其中xxx由MPC指定。 

        :param file_name: The file_name of this ObsObjInfo.
        :type: str
        """
        self._file_name = file_name

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
        if not isinstance(other, ObsObjInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
