# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsBucketInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'response_headers': 'object',
        'original_headers': 'object',
        'status_code': 'int',
        'bucket_name': 'str',
        'owner': 'ObsBucketInfoOwner',
        'creation_date': 'str',
        'location': 'str',
        'storage_class': 'object',
        'metadata': 'object',
        'acl': 'object',
        'bucket_storage_class': 'object',
        'bucket_type': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'response_headers': 'responseHeaders',
        'original_headers': 'originalHeaders',
        'status_code': 'statusCode',
        'bucket_name': 'bucketName',
        'owner': 'owner',
        'creation_date': 'creationDate',
        'location': 'location',
        'storage_class': 'storageClass',
        'metadata': 'metadata',
        'acl': 'acl',
        'bucket_storage_class': 'bucketStorageClass',
        'bucket_type': 'bucketType',
        'request_id': 'requestId'
    }

    def __init__(self, response_headers=None, original_headers=None, status_code=None, bucket_name=None, owner=None, creation_date=None, location=None, storage_class=None, metadata=None, acl=None, bucket_storage_class=None, bucket_type=None, request_id=None):
        """ObsBucketInfo

        The model defined in huaweicloud sdk

        :param response_headers: 响应头
        :type response_headers: object
        :param original_headers: 请求头
        :type original_headers: object
        :param status_code: 状态
        :type status_code: int
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkeg.v1.ObsBucketInfoOwner`
        :param creation_date: 桶的创建时间
        :type creation_date: str
        :param location: 桶的位置信息
        :type location: str
        :param storage_class: 对象的存储类型
        :type storage_class: object
        :param metadata: 桶元数据
        :type metadata: object
        :param acl: 桶ACL
        :type acl: object
        :param bucket_storage_class: 桶的存储类型
        :type bucket_storage_class: object
        :param bucket_type: 桶类型
        :type bucket_type: str
        :param request_id: 请求id
        :type request_id: str
        """
        
        

        self._response_headers = None
        self._original_headers = None
        self._status_code = None
        self._bucket_name = None
        self._owner = None
        self._creation_date = None
        self._location = None
        self._storage_class = None
        self._metadata = None
        self._acl = None
        self._bucket_storage_class = None
        self._bucket_type = None
        self._request_id = None
        self.discriminator = None

        if response_headers is not None:
            self.response_headers = response_headers
        if original_headers is not None:
            self.original_headers = original_headers
        if status_code is not None:
            self.status_code = status_code
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if owner is not None:
            self.owner = owner
        if creation_date is not None:
            self.creation_date = creation_date
        if location is not None:
            self.location = location
        if storage_class is not None:
            self.storage_class = storage_class
        if metadata is not None:
            self.metadata = metadata
        if acl is not None:
            self.acl = acl
        if bucket_storage_class is not None:
            self.bucket_storage_class = bucket_storage_class
        if bucket_type is not None:
            self.bucket_type = bucket_type
        if request_id is not None:
            self.request_id = request_id

    @property
    def response_headers(self):
        """Gets the response_headers of this ObsBucketInfo.

        响应头

        :return: The response_headers of this ObsBucketInfo.
        :rtype: object
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this ObsBucketInfo.

        响应头

        :param response_headers: The response_headers of this ObsBucketInfo.
        :type response_headers: object
        """
        self._response_headers = response_headers

    @property
    def original_headers(self):
        """Gets the original_headers of this ObsBucketInfo.

        请求头

        :return: The original_headers of this ObsBucketInfo.
        :rtype: object
        """
        return self._original_headers

    @original_headers.setter
    def original_headers(self, original_headers):
        """Sets the original_headers of this ObsBucketInfo.

        请求头

        :param original_headers: The original_headers of this ObsBucketInfo.
        :type original_headers: object
        """
        self._original_headers = original_headers

    @property
    def status_code(self):
        """Gets the status_code of this ObsBucketInfo.

        状态

        :return: The status_code of this ObsBucketInfo.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ObsBucketInfo.

        状态

        :param status_code: The status_code of this ObsBucketInfo.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsBucketInfo.

        桶名称

        :return: The bucket_name of this ObsBucketInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsBucketInfo.

        桶名称

        :param bucket_name: The bucket_name of this ObsBucketInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def owner(self):
        """Gets the owner of this ObsBucketInfo.

        :return: The owner of this ObsBucketInfo.
        :rtype: :class:`huaweicloudsdkeg.v1.ObsBucketInfoOwner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ObsBucketInfo.

        :param owner: The owner of this ObsBucketInfo.
        :type owner: :class:`huaweicloudsdkeg.v1.ObsBucketInfoOwner`
        """
        self._owner = owner

    @property
    def creation_date(self):
        """Gets the creation_date of this ObsBucketInfo.

        桶的创建时间

        :return: The creation_date of this ObsBucketInfo.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ObsBucketInfo.

        桶的创建时间

        :param creation_date: The creation_date of this ObsBucketInfo.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def location(self):
        """Gets the location of this ObsBucketInfo.

        桶的位置信息

        :return: The location of this ObsBucketInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ObsBucketInfo.

        桶的位置信息

        :param location: The location of this ObsBucketInfo.
        :type location: str
        """
        self._location = location

    @property
    def storage_class(self):
        """Gets the storage_class of this ObsBucketInfo.

        对象的存储类型

        :return: The storage_class of this ObsBucketInfo.
        :rtype: object
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this ObsBucketInfo.

        对象的存储类型

        :param storage_class: The storage_class of this ObsBucketInfo.
        :type storage_class: object
        """
        self._storage_class = storage_class

    @property
    def metadata(self):
        """Gets the metadata of this ObsBucketInfo.

        桶元数据

        :return: The metadata of this ObsBucketInfo.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ObsBucketInfo.

        桶元数据

        :param metadata: The metadata of this ObsBucketInfo.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def acl(self):
        """Gets the acl of this ObsBucketInfo.

        桶ACL

        :return: The acl of this ObsBucketInfo.
        :rtype: object
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this ObsBucketInfo.

        桶ACL

        :param acl: The acl of this ObsBucketInfo.
        :type acl: object
        """
        self._acl = acl

    @property
    def bucket_storage_class(self):
        """Gets the bucket_storage_class of this ObsBucketInfo.

        桶的存储类型

        :return: The bucket_storage_class of this ObsBucketInfo.
        :rtype: object
        """
        return self._bucket_storage_class

    @bucket_storage_class.setter
    def bucket_storage_class(self, bucket_storage_class):
        """Sets the bucket_storage_class of this ObsBucketInfo.

        桶的存储类型

        :param bucket_storage_class: The bucket_storage_class of this ObsBucketInfo.
        :type bucket_storage_class: object
        """
        self._bucket_storage_class = bucket_storage_class

    @property
    def bucket_type(self):
        """Gets the bucket_type of this ObsBucketInfo.

        桶类型

        :return: The bucket_type of this ObsBucketInfo.
        :rtype: str
        """
        return self._bucket_type

    @bucket_type.setter
    def bucket_type(self, bucket_type):
        """Sets the bucket_type of this ObsBucketInfo.

        桶类型

        :param bucket_type: The bucket_type of this ObsBucketInfo.
        :type bucket_type: str
        """
        self._bucket_type = bucket_type

    @property
    def request_id(self):
        """Gets the request_id of this ObsBucketInfo.

        请求id

        :return: The request_id of this ObsBucketInfo.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ObsBucketInfo.

        请求id

        :param request_id: The request_id of this ObsBucketInfo.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ObsBucketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
