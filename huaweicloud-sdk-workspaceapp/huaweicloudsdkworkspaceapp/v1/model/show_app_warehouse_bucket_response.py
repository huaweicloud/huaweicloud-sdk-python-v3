# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppWarehouseBucketResponse(SdkResponse):

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
        'bucket_name': 'str',
        'is_user_create_bucket': 'bool',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'bucket_name': 'bucket_name',
        'is_user_create_bucket': 'is_user_create_bucket',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, bucket_name=None, is_user_create_bucket=None, update_time=None):
        r"""ShowAppWarehouseBucketResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识。
        :type id: str
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param is_user_create_bucket: 是否是用户自建桶
        :type is_user_create_bucket: bool
        :param update_time: 桶记录更新时间。
        :type update_time: datetime
        """
        
        super(ShowAppWarehouseBucketResponse, self).__init__()

        self._id = None
        self._bucket_name = None
        self._is_user_create_bucket = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if is_user_create_bucket is not None:
            self.is_user_create_bucket = is_user_create_bucket
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowAppWarehouseBucketResponse.

        唯一标识。

        :return: The id of this ShowAppWarehouseBucketResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAppWarehouseBucketResponse.

        唯一标识。

        :param id: The id of this ShowAppWarehouseBucketResponse.
        :type id: str
        """
        self._id = id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ShowAppWarehouseBucketResponse.

        桶名称

        :return: The bucket_name of this ShowAppWarehouseBucketResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ShowAppWarehouseBucketResponse.

        桶名称

        :param bucket_name: The bucket_name of this ShowAppWarehouseBucketResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def is_user_create_bucket(self):
        r"""Gets the is_user_create_bucket of this ShowAppWarehouseBucketResponse.

        是否是用户自建桶

        :return: The is_user_create_bucket of this ShowAppWarehouseBucketResponse.
        :rtype: bool
        """
        return self._is_user_create_bucket

    @is_user_create_bucket.setter
    def is_user_create_bucket(self, is_user_create_bucket):
        r"""Sets the is_user_create_bucket of this ShowAppWarehouseBucketResponse.

        是否是用户自建桶

        :param is_user_create_bucket: The is_user_create_bucket of this ShowAppWarehouseBucketResponse.
        :type is_user_create_bucket: bool
        """
        self._is_user_create_bucket = is_user_create_bucket

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAppWarehouseBucketResponse.

        桶记录更新时间。

        :return: The update_time of this ShowAppWarehouseBucketResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAppWarehouseBucketResponse.

        桶记录更新时间。

        :param update_time: The update_time of this ShowAppWarehouseBucketResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowAppWarehouseBucketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
