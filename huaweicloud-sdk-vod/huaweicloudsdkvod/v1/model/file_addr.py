# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileAddr:

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
        'object': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'location': 'location',
        'object': 'object'
    }

    def __init__(self, bucket=None, location=None, object=None):
        """FileAddr

        The model defined in huaweicloud sdk

        :param bucket: OBS的bucket名称。
        :type bucket: str
        :param location: 桶所在的区域名， 如“华北-北京四”的区域名为“cn-north-4”，创建的桶所在区域必须和点播服务所在区域保持一致。
        :type location: str
        :param object: 文件的存储路径。
        :type object: str
        """
        
        

        self._bucket = None
        self._location = None
        self._object = None
        self.discriminator = None

        self.bucket = bucket
        self.location = location
        self.object = object

    @property
    def bucket(self):
        """Gets the bucket of this FileAddr.

        OBS的bucket名称。

        :return: The bucket of this FileAddr.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this FileAddr.

        OBS的bucket名称。

        :param bucket: The bucket of this FileAddr.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def location(self):
        """Gets the location of this FileAddr.

        桶所在的区域名， 如“华北-北京四”的区域名为“cn-north-4”，创建的桶所在区域必须和点播服务所在区域保持一致。

        :return: The location of this FileAddr.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FileAddr.

        桶所在的区域名， 如“华北-北京四”的区域名为“cn-north-4”，创建的桶所在区域必须和点播服务所在区域保持一致。

        :param location: The location of this FileAddr.
        :type location: str
        """
        self._location = location

    @property
    def object(self):
        """Gets the object of this FileAddr.

        文件的存储路径。

        :return: The object of this FileAddr.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this FileAddr.

        文件的存储路径。

        :param object: The object of this FileAddr.
        :type object: str
        """
        self._object = object

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
        if not isinstance(other, FileAddr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
