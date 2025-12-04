# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketsResponseBody:

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
        'owner': 'object',
        'creation_date': 'int',
        'location': 'str',
        'clustertype': 'str',
        'storage_class': 'str',
        'metadata': 'object',
        'acl': 'str',
        'bucket_storage_class': 'str',
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
        'clustertype': 'clustertype',
        'storage_class': 'storageClass',
        'metadata': 'metadata',
        'acl': 'acl',
        'bucket_storage_class': 'bucketStorageClass',
        'bucket_type': 'bucketType',
        'request_id': 'requestId'
    }

    def __init__(self, response_headers=None, original_headers=None, status_code=None, bucket_name=None, owner=None, creation_date=None, location=None, clustertype=None, storage_class=None, metadata=None, acl=None, bucket_storage_class=None, bucket_type=None, request_id=None):
        r"""ListObsBucketsResponseBody

        The model defined in huaweicloud sdk

        :param response_headers: **参数解释**： 响应头。
        :type response_headers: object
        :param original_headers: **参数解释**： 原始响应头。
        :type original_headers: object
        :param status_code: **参数解释**： 状态码。 **取值范围**： 不涉及。
        :type status_code: int
        :param bucket_name: **参数解释**： 桶名。 **取值范围**： 不涉及。
        :type bucket_name: str
        :param owner: **参数解释**： 桶拥有者信息。
        :type owner: object
        :param creation_date: **参数解释**： 桶的创建时间。 **取值范围**： 长度为24的字符串。
        :type creation_date: int
        :param location: **参数解释**： 桶所在的区域。 **取值范围**： 不涉及。
        :type location: str
        :param clustertype: **参数解释**： 集群类型。 **取值范围**： 不涉及。
        :type clustertype: str
        :param storage_class: **参数解释**： 存储类型。 **取值范围**： 不涉及。
        :type storage_class: str
        :param metadata: **参数解释**： 元数据。
        :type metadata: object
        :param acl: **参数解释**： 桶ACL策略。 **取值范围**： 不涉及。
        :type acl: str
        :param bucket_storage_class: **参数解释**： 桶的存储类型。 **取值范围**： - STANDARD：标准存储。 - WARM：低频访问存储。 - COLD：归档存储。 - DEEP_ARCHIVE：深度归档存储（受限公测）。
        :type bucket_storage_class: str
        :param bucket_type: **参数解释**： 桶类型。 **取值范围**： 不涉及。
        :type bucket_type: str
        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        """
        
        

        self._response_headers = None
        self._original_headers = None
        self._status_code = None
        self._bucket_name = None
        self._owner = None
        self._creation_date = None
        self._location = None
        self._clustertype = None
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
        if clustertype is not None:
            self.clustertype = clustertype
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
        r"""Gets the response_headers of this ListObsBucketsResponseBody.

        **参数解释**： 响应头。

        :return: The response_headers of this ListObsBucketsResponseBody.
        :rtype: object
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        r"""Sets the response_headers of this ListObsBucketsResponseBody.

        **参数解释**： 响应头。

        :param response_headers: The response_headers of this ListObsBucketsResponseBody.
        :type response_headers: object
        """
        self._response_headers = response_headers

    @property
    def original_headers(self):
        r"""Gets the original_headers of this ListObsBucketsResponseBody.

        **参数解释**： 原始响应头。

        :return: The original_headers of this ListObsBucketsResponseBody.
        :rtype: object
        """
        return self._original_headers

    @original_headers.setter
    def original_headers(self, original_headers):
        r"""Sets the original_headers of this ListObsBucketsResponseBody.

        **参数解释**： 原始响应头。

        :param original_headers: The original_headers of this ListObsBucketsResponseBody.
        :type original_headers: object
        """
        self._original_headers = original_headers

    @property
    def status_code(self):
        r"""Gets the status_code of this ListObsBucketsResponseBody.

        **参数解释**： 状态码。 **取值范围**： 不涉及。

        :return: The status_code of this ListObsBucketsResponseBody.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this ListObsBucketsResponseBody.

        **参数解释**： 状态码。 **取值范围**： 不涉及。

        :param status_code: The status_code of this ListObsBucketsResponseBody.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ListObsBucketsResponseBody.

        **参数解释**： 桶名。 **取值范围**： 不涉及。

        :return: The bucket_name of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ListObsBucketsResponseBody.

        **参数解释**： 桶名。 **取值范围**： 不涉及。

        :param bucket_name: The bucket_name of this ListObsBucketsResponseBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def owner(self):
        r"""Gets the owner of this ListObsBucketsResponseBody.

        **参数解释**： 桶拥有者信息。

        :return: The owner of this ListObsBucketsResponseBody.
        :rtype: object
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListObsBucketsResponseBody.

        **参数解释**： 桶拥有者信息。

        :param owner: The owner of this ListObsBucketsResponseBody.
        :type owner: object
        """
        self._owner = owner

    @property
    def creation_date(self):
        r"""Gets the creation_date of this ListObsBucketsResponseBody.

        **参数解释**： 桶的创建时间。 **取值范围**： 长度为24的字符串。

        :return: The creation_date of this ListObsBucketsResponseBody.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this ListObsBucketsResponseBody.

        **参数解释**： 桶的创建时间。 **取值范围**： 长度为24的字符串。

        :param creation_date: The creation_date of this ListObsBucketsResponseBody.
        :type creation_date: int
        """
        self._creation_date = creation_date

    @property
    def location(self):
        r"""Gets the location of this ListObsBucketsResponseBody.

        **参数解释**： 桶所在的区域。 **取值范围**： 不涉及。

        :return: The location of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ListObsBucketsResponseBody.

        **参数解释**： 桶所在的区域。 **取值范围**： 不涉及。

        :param location: The location of this ListObsBucketsResponseBody.
        :type location: str
        """
        self._location = location

    @property
    def clustertype(self):
        r"""Gets the clustertype of this ListObsBucketsResponseBody.

        **参数解释**： 集群类型。 **取值范围**： 不涉及。

        :return: The clustertype of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._clustertype

    @clustertype.setter
    def clustertype(self, clustertype):
        r"""Sets the clustertype of this ListObsBucketsResponseBody.

        **参数解释**： 集群类型。 **取值范围**： 不涉及。

        :param clustertype: The clustertype of this ListObsBucketsResponseBody.
        :type clustertype: str
        """
        self._clustertype = clustertype

    @property
    def storage_class(self):
        r"""Gets the storage_class of this ListObsBucketsResponseBody.

        **参数解释**： 存储类型。 **取值范围**： 不涉及。

        :return: The storage_class of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        r"""Sets the storage_class of this ListObsBucketsResponseBody.

        **参数解释**： 存储类型。 **取值范围**： 不涉及。

        :param storage_class: The storage_class of this ListObsBucketsResponseBody.
        :type storage_class: str
        """
        self._storage_class = storage_class

    @property
    def metadata(self):
        r"""Gets the metadata of this ListObsBucketsResponseBody.

        **参数解释**： 元数据。

        :return: The metadata of this ListObsBucketsResponseBody.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListObsBucketsResponseBody.

        **参数解释**： 元数据。

        :param metadata: The metadata of this ListObsBucketsResponseBody.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def acl(self):
        r"""Gets the acl of this ListObsBucketsResponseBody.

        **参数解释**： 桶ACL策略。 **取值范围**： 不涉及。

        :return: The acl of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        r"""Sets the acl of this ListObsBucketsResponseBody.

        **参数解释**： 桶ACL策略。 **取值范围**： 不涉及。

        :param acl: The acl of this ListObsBucketsResponseBody.
        :type acl: str
        """
        self._acl = acl

    @property
    def bucket_storage_class(self):
        r"""Gets the bucket_storage_class of this ListObsBucketsResponseBody.

        **参数解释**： 桶的存储类型。 **取值范围**： - STANDARD：标准存储。 - WARM：低频访问存储。 - COLD：归档存储。 - DEEP_ARCHIVE：深度归档存储（受限公测）。

        :return: The bucket_storage_class of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._bucket_storage_class

    @bucket_storage_class.setter
    def bucket_storage_class(self, bucket_storage_class):
        r"""Sets the bucket_storage_class of this ListObsBucketsResponseBody.

        **参数解释**： 桶的存储类型。 **取值范围**： - STANDARD：标准存储。 - WARM：低频访问存储。 - COLD：归档存储。 - DEEP_ARCHIVE：深度归档存储（受限公测）。

        :param bucket_storage_class: The bucket_storage_class of this ListObsBucketsResponseBody.
        :type bucket_storage_class: str
        """
        self._bucket_storage_class = bucket_storage_class

    @property
    def bucket_type(self):
        r"""Gets the bucket_type of this ListObsBucketsResponseBody.

        **参数解释**： 桶类型。 **取值范围**： 不涉及。

        :return: The bucket_type of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._bucket_type

    @bucket_type.setter
    def bucket_type(self, bucket_type):
        r"""Sets the bucket_type of this ListObsBucketsResponseBody.

        **参数解释**： 桶类型。 **取值范围**： 不涉及。

        :param bucket_type: The bucket_type of this ListObsBucketsResponseBody.
        :type bucket_type: str
        """
        self._bucket_type = bucket_type

    @property
    def request_id(self):
        r"""Gets the request_id of this ListObsBucketsResponseBody.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this ListObsBucketsResponseBody.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListObsBucketsResponseBody.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this ListObsBucketsResponseBody.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListObsBucketsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
