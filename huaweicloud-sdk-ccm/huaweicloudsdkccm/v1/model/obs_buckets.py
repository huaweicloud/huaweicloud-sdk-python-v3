# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsBuckets:

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
        'create_time': 'int'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'create_time': 'create_time'
    }

    def __init__(self, bucket_name=None, create_time=None):
        r"""ObsBuckets

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称。
        :type bucket_name: str
        :param create_time: 创建时间,格式为时间戳（毫秒级）。
        :type create_time: int
        """
        
        

        self._bucket_name = None
        self._create_time = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.create_time = create_time

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ObsBuckets.

        桶名称。

        :return: The bucket_name of this ObsBuckets.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ObsBuckets.

        桶名称。

        :param bucket_name: The bucket_name of this ObsBuckets.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ObsBuckets.

        创建时间,格式为时间戳（毫秒级）。

        :return: The create_time of this ObsBuckets.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ObsBuckets.

        创建时间,格式为时间戳（毫秒级）。

        :param create_time: The create_time of this ObsBuckets.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ObsBuckets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
