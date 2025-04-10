# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Bucket:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str',
        'bucket_location': 'str',
        'bucket_name': 'str',
        'bucket_policy': 'str',
        'create_time': 'int',
        'deleted': 'bool',
        'id': 'str',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'bucket_location': 'bucket_location',
        'bucket_name': 'bucket_name',
        'bucket_policy': 'bucket_policy',
        'create_time': 'create_time',
        'deleted': 'deleted',
        'id': 'id',
        'is_deleted': 'is_deleted'
    }

    def __init__(self, asset_name=None, bucket_location=None, bucket_name=None, bucket_policy=None, create_time=None, deleted=None, id=None, is_deleted=None):
        r"""Bucket

        The model defined in huaweicloud sdk

        :param asset_name: 资产名称
        :type asset_name: str
        :param bucket_location: 桶位置
        :type bucket_location: str
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param bucket_policy: 桶策略
        :type bucket_policy: str
        :param create_time: 创建时间
        :type create_time: int
        :param deleted: 是否被删除
        :type deleted: bool
        :param id: 桶ID
        :type id: str
        :param is_deleted: 是否被删除
        :type is_deleted: bool
        """
        
        

        self._asset_name = None
        self._bucket_location = None
        self._bucket_name = None
        self._bucket_policy = None
        self._create_time = None
        self._deleted = None
        self._id = None
        self._is_deleted = None
        self.discriminator = None

        if asset_name is not None:
            self.asset_name = asset_name
        if bucket_location is not None:
            self.bucket_location = bucket_location
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_policy is not None:
            self.bucket_policy = bucket_policy
        if create_time is not None:
            self.create_time = create_time
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def asset_name(self):
        r"""Gets the asset_name of this Bucket.

        资产名称

        :return: The asset_name of this Bucket.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this Bucket.

        资产名称

        :param asset_name: The asset_name of this Bucket.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def bucket_location(self):
        r"""Gets the bucket_location of this Bucket.

        桶位置

        :return: The bucket_location of this Bucket.
        :rtype: str
        """
        return self._bucket_location

    @bucket_location.setter
    def bucket_location(self, bucket_location):
        r"""Sets the bucket_location of this Bucket.

        桶位置

        :param bucket_location: The bucket_location of this Bucket.
        :type bucket_location: str
        """
        self._bucket_location = bucket_location

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this Bucket.

        桶名称

        :return: The bucket_name of this Bucket.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this Bucket.

        桶名称

        :param bucket_name: The bucket_name of this Bucket.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_policy(self):
        r"""Gets the bucket_policy of this Bucket.

        桶策略

        :return: The bucket_policy of this Bucket.
        :rtype: str
        """
        return self._bucket_policy

    @bucket_policy.setter
    def bucket_policy(self, bucket_policy):
        r"""Sets the bucket_policy of this Bucket.

        桶策略

        :param bucket_policy: The bucket_policy of this Bucket.
        :type bucket_policy: str
        """
        self._bucket_policy = bucket_policy

    @property
    def create_time(self):
        r"""Gets the create_time of this Bucket.

        创建时间

        :return: The create_time of this Bucket.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Bucket.

        创建时间

        :param create_time: The create_time of this Bucket.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def deleted(self):
        r"""Gets the deleted of this Bucket.

        是否被删除

        :return: The deleted of this Bucket.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this Bucket.

        是否被删除

        :param deleted: The deleted of this Bucket.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def id(self):
        r"""Gets the id of this Bucket.

        桶ID

        :return: The id of this Bucket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Bucket.

        桶ID

        :param id: The id of this Bucket.
        :type id: str
        """
        self._id = id

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this Bucket.

        是否被删除

        :return: The is_deleted of this Bucket.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this Bucket.

        是否被删除

        :param is_deleted: The is_deleted of this Bucket.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
