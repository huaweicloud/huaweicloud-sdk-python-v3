# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePersistentStorageResponse(SdkResponse):

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
        'name': 'str',
        'storage_metadata': 'StorageMetadata',
        'create_time': 'datetime',
        'user_claim_count': 'int',
        'share_claim_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'storage_metadata': 'storage_metadata',
        'create_time': 'create_time',
        'user_claim_count': 'user_claim_count',
        'share_claim_count': 'share_claim_count'
    }

    def __init__(self, id=None, name=None, storage_metadata=None, create_time=None, user_claim_count=None, share_claim_count=None):
        """CreatePersistentStorageResponse

        The model defined in huaweicloud sdk

        :param id: WKS存储ID
        :type id: str
        :param name: 名称
        :type name: str
        :param storage_metadata: 
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        :param create_time: 创建时间
        :type create_time: datetime
        :param user_claim_count: 个人目录声明数量
        :type user_claim_count: int
        :param share_claim_count: 共享目录声明数量
        :type share_claim_count: int
        """
        
        super(CreatePersistentStorageResponse, self).__init__()

        self._id = None
        self._name = None
        self._storage_metadata = None
        self._create_time = None
        self._user_claim_count = None
        self._share_claim_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if storage_metadata is not None:
            self.storage_metadata = storage_metadata
        if create_time is not None:
            self.create_time = create_time
        if user_claim_count is not None:
            self.user_claim_count = user_claim_count
        if share_claim_count is not None:
            self.share_claim_count = share_claim_count

    @property
    def id(self):
        """Gets the id of this CreatePersistentStorageResponse.

        WKS存储ID

        :return: The id of this CreatePersistentStorageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePersistentStorageResponse.

        WKS存储ID

        :param id: The id of this CreatePersistentStorageResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePersistentStorageResponse.

        名称

        :return: The name of this CreatePersistentStorageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePersistentStorageResponse.

        名称

        :param name: The name of this CreatePersistentStorageResponse.
        :type name: str
        """
        self._name = name

    @property
    def storage_metadata(self):
        """Gets the storage_metadata of this CreatePersistentStorageResponse.

        :return: The storage_metadata of this CreatePersistentStorageResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        """
        return self._storage_metadata

    @storage_metadata.setter
    def storage_metadata(self, storage_metadata):
        """Sets the storage_metadata of this CreatePersistentStorageResponse.

        :param storage_metadata: The storage_metadata of this CreatePersistentStorageResponse.
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        """
        self._storage_metadata = storage_metadata

    @property
    def create_time(self):
        """Gets the create_time of this CreatePersistentStorageResponse.

        创建时间

        :return: The create_time of this CreatePersistentStorageResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreatePersistentStorageResponse.

        创建时间

        :param create_time: The create_time of this CreatePersistentStorageResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def user_claim_count(self):
        """Gets the user_claim_count of this CreatePersistentStorageResponse.

        个人目录声明数量

        :return: The user_claim_count of this CreatePersistentStorageResponse.
        :rtype: int
        """
        return self._user_claim_count

    @user_claim_count.setter
    def user_claim_count(self, user_claim_count):
        """Sets the user_claim_count of this CreatePersistentStorageResponse.

        个人目录声明数量

        :param user_claim_count: The user_claim_count of this CreatePersistentStorageResponse.
        :type user_claim_count: int
        """
        self._user_claim_count = user_claim_count

    @property
    def share_claim_count(self):
        """Gets the share_claim_count of this CreatePersistentStorageResponse.

        共享目录声明数量

        :return: The share_claim_count of this CreatePersistentStorageResponse.
        :rtype: int
        """
        return self._share_claim_count

    @share_claim_count.setter
    def share_claim_count(self, share_claim_count):
        """Sets the share_claim_count of this CreatePersistentStorageResponse.

        共享目录声明数量

        :param share_claim_count: The share_claim_count of this CreatePersistentStorageResponse.
        :type share_claim_count: int
        """
        self._share_claim_count = share_claim_count

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
        if not isinstance(other, CreatePersistentStorageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
