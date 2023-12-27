# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObjectRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_key': 'str',
        'date': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'date': 'Date',
        'version_id': 'versionId'
    }

    def __init__(self, bucket_name=None, object_key=None, date=None, version_id=None):
        """DeleteObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称 
        :type bucket_name: str
        :param object_key: 通过此请求删除的对象名称。 
        :type object_key: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param version_id: 待删除对象的版本号。 
        :type version_id: str
        """
        
        

        self._bucket_name = None
        self._object_key = None
        self._date = None
        self._version_id = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.object_key = object_key
        if date is not None:
            self.date = date
        if version_id is not None:
            self.version_id = version_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this DeleteObjectRequest.

        桶名称 

        :return: The bucket_name of this DeleteObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this DeleteObjectRequest.

        桶名称 

        :param bucket_name: The bucket_name of this DeleteObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this DeleteObjectRequest.

        通过此请求删除的对象名称。 

        :return: The object_key of this DeleteObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this DeleteObjectRequest.

        通过此请求删除的对象名称。 

        :param object_key: The object_key of this DeleteObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        """Gets the date of this DeleteObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this DeleteObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DeleteObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this DeleteObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def version_id(self):
        """Gets the version_id of this DeleteObjectRequest.

        待删除对象的版本号。 

        :return: The version_id of this DeleteObjectRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DeleteObjectRequest.

        待删除对象的版本号。 

        :param version_id: The version_id of this DeleteObjectRequest.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, DeleteObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
