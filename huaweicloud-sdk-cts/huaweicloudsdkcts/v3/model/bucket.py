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
        'bucket_name': 'str',
        'bucket_location': 'str',
        'kms_id': 'str',
        'is_support_trace_files_encryption': 'bool',
        'check_bucket_response': 'CheckBucketResponse'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'bucket_location': 'bucket_location',
        'kms_id': 'kms_id',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'check_bucket_response': 'check_bucket_response'
    }

    def __init__(self, bucket_name=None, bucket_location=None, kms_id=None, is_support_trace_files_encryption=None, check_bucket_response=None):
        """Bucket

        The model defined in huaweicloud sdk

        :param bucket_name: 标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。
        :type bucket_name: str
        :param bucket_location: 标识桶位置。
        :type bucket_location: str
        :param kms_id: 事件文件转储加密所采用的秘钥id。 如果is_support_trace_files_encryption\&quot;参数值为“是”时，此参数为必选项。
        :type kms_id: str
        :param is_support_trace_files_encryption: 事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。
        :type is_support_trace_files_encryption: bool
        :param check_bucket_response: 
        :type check_bucket_response: :class:`huaweicloudsdkcts.v3.CheckBucketResponse`
        """
        
        

        self._bucket_name = None
        self._bucket_location = None
        self._kms_id = None
        self._is_support_trace_files_encryption = None
        self._check_bucket_response = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if bucket_location is not None:
            self.bucket_location = bucket_location
        if kms_id is not None:
            self.kms_id = kms_id
        self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if check_bucket_response is not None:
            self.check_bucket_response = check_bucket_response

    @property
    def bucket_name(self):
        """Gets the bucket_name of this Bucket.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :return: The bucket_name of this Bucket.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this Bucket.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :param bucket_name: The bucket_name of this Bucket.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_location(self):
        """Gets the bucket_location of this Bucket.

        标识桶位置。

        :return: The bucket_location of this Bucket.
        :rtype: str
        """
        return self._bucket_location

    @bucket_location.setter
    def bucket_location(self, bucket_location):
        """Sets the bucket_location of this Bucket.

        标识桶位置。

        :param bucket_location: The bucket_location of this Bucket.
        :type bucket_location: str
        """
        self._bucket_location = bucket_location

    @property
    def kms_id(self):
        """Gets the kms_id of this Bucket.

        事件文件转储加密所采用的秘钥id。 如果is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this Bucket.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this Bucket.

        事件文件转储加密所采用的秘钥id。 如果is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this Bucket.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this Bucket.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :return: The is_support_trace_files_encryption of this Bucket.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this Bucket.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this Bucket.
        :type is_support_trace_files_encryption: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def check_bucket_response(self):
        """Gets the check_bucket_response of this Bucket.

        :return: The check_bucket_response of this Bucket.
        :rtype: :class:`huaweicloudsdkcts.v3.CheckBucketResponse`
        """
        return self._check_bucket_response

    @check_bucket_response.setter
    def check_bucket_response(self, check_bucket_response):
        """Sets the check_bucket_response of this Bucket.

        :param check_bucket_response: The check_bucket_response of this Bucket.
        :type check_bucket_response: :class:`huaweicloudsdkcts.v3.CheckBucketResponse`
        """
        self._check_bucket_response = check_bucket_response

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
