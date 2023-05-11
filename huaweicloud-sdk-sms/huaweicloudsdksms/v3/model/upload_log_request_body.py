# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadLogRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_bucket': 'str',
        'log_expire': 'int'
    }

    attribute_map = {
        'log_bucket': 'log_bucket',
        'log_expire': 'log_expire'
    }

    def __init__(self, log_bucket=None, log_expire=None):
        """UploadLogRequestBody

        The model defined in huaweicloud sdk

        :param log_bucket: 指定桶名称
        :type log_bucket: str
        :param log_expire: 指定有效期
        :type log_expire: int
        """
        
        

        self._log_bucket = None
        self._log_expire = None
        self.discriminator = None

        self.log_bucket = log_bucket
        self.log_expire = log_expire

    @property
    def log_bucket(self):
        """Gets the log_bucket of this UploadLogRequestBody.

        指定桶名称

        :return: The log_bucket of this UploadLogRequestBody.
        :rtype: str
        """
        return self._log_bucket

    @log_bucket.setter
    def log_bucket(self, log_bucket):
        """Sets the log_bucket of this UploadLogRequestBody.

        指定桶名称

        :param log_bucket: The log_bucket of this UploadLogRequestBody.
        :type log_bucket: str
        """
        self._log_bucket = log_bucket

    @property
    def log_expire(self):
        """Gets the log_expire of this UploadLogRequestBody.

        指定有效期

        :return: The log_expire of this UploadLogRequestBody.
        :rtype: int
        """
        return self._log_expire

    @log_expire.setter
    def log_expire(self, log_expire):
        """Sets the log_expire of this UploadLogRequestBody.

        指定有效期

        :param log_expire: The log_expire of this UploadLogRequestBody.
        :type log_expire: int
        """
        self._log_expire = log_expire

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
        if not isinstance(other, UploadLogRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
