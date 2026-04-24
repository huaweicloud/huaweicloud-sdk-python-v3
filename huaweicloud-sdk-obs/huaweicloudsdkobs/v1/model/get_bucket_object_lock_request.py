# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketObjectLockRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketObjectLockRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'object_lock': 'str',
        'host': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'object_lock': 'object-lock',
        'host': 'Host'
    }

    def __init__(self, date=None, bucket_name=None, object_lock=None, host=None):
        r"""GetBucketObjectLockRequest

        The model defined in huaweicloud sdk

        :param date: The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.
        :type date: str
        :param bucket_name: The name of the requested bucket.
        :type bucket_name: str
        :param object_lock: object-lock indicates a request to the default WORM policy for a Bucket API.
        :type object_lock: str
        :param host: Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.
        :type host: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._object_lock = None
        self._host = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.object_lock = object_lock
        if host is not None:
            self.host = host

    @property
    def date(self):
        r"""Gets the date of this GetBucketObjectLockRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.

        :return: The date of this GetBucketObjectLockRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketObjectLockRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.

        :param date: The date of this GetBucketObjectLockRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetBucketObjectLockRequest.

        The name of the requested bucket.

        :return: The bucket_name of this GetBucketObjectLockRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetBucketObjectLockRequest.

        The name of the requested bucket.

        :param bucket_name: The bucket_name of this GetBucketObjectLockRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_lock(self):
        r"""Gets the object_lock of this GetBucketObjectLockRequest.

        object-lock indicates a request to the default WORM policy for a Bucket API.

        :return: The object_lock of this GetBucketObjectLockRequest.
        :rtype: str
        """
        return self._object_lock

    @object_lock.setter
    def object_lock(self, object_lock):
        r"""Sets the object_lock of this GetBucketObjectLockRequest.

        object-lock indicates a request to the default WORM policy for a Bucket API.

        :param object_lock: The object_lock of this GetBucketObjectLockRequest.
        :type object_lock: str
        """
        self._object_lock = object_lock

    @property
    def host(self):
        r"""Gets the host of this GetBucketObjectLockRequest.

        Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :return: The host of this GetBucketObjectLockRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this GetBucketObjectLockRequest.

        Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :param host: The host of this GetBucketObjectLockRequest.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, GetBucketObjectLockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
