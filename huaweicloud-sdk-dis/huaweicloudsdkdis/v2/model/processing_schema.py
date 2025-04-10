# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessingSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp_name': 'str',
        'timestamp_type': 'str',
        'timestamp_format': 'str'
    }

    attribute_map = {
        'timestamp_name': 'timestamp_name',
        'timestamp_type': 'timestamp_type',
        'timestamp_format': 'timestamp_format'
    }

    def __init__(self, timestamp_name=None, timestamp_type=None, timestamp_format=None):
        r"""ProcessingSchema

        The model defined in huaweicloud sdk

        :param timestamp_name: 源数据时间戳的属性名称。
        :type timestamp_name: str
        :param timestamp_type: 源数据时间戳的类型。  - String - Timestamp：Long类型的13位时间戳
        :type timestamp_type: str
        :param timestamp_format: 源数据时间戳的类型为String时必选，用于根据时间戳格式生成OBS的时间目录。
        :type timestamp_format: str
        """
        
        

        self._timestamp_name = None
        self._timestamp_type = None
        self._timestamp_format = None
        self.discriminator = None

        self.timestamp_name = timestamp_name
        self.timestamp_type = timestamp_type
        if timestamp_format is not None:
            self.timestamp_format = timestamp_format

    @property
    def timestamp_name(self):
        r"""Gets the timestamp_name of this ProcessingSchema.

        源数据时间戳的属性名称。

        :return: The timestamp_name of this ProcessingSchema.
        :rtype: str
        """
        return self._timestamp_name

    @timestamp_name.setter
    def timestamp_name(self, timestamp_name):
        r"""Sets the timestamp_name of this ProcessingSchema.

        源数据时间戳的属性名称。

        :param timestamp_name: The timestamp_name of this ProcessingSchema.
        :type timestamp_name: str
        """
        self._timestamp_name = timestamp_name

    @property
    def timestamp_type(self):
        r"""Gets the timestamp_type of this ProcessingSchema.

        源数据时间戳的类型。  - String - Timestamp：Long类型的13位时间戳

        :return: The timestamp_type of this ProcessingSchema.
        :rtype: str
        """
        return self._timestamp_type

    @timestamp_type.setter
    def timestamp_type(self, timestamp_type):
        r"""Sets the timestamp_type of this ProcessingSchema.

        源数据时间戳的类型。  - String - Timestamp：Long类型的13位时间戳

        :param timestamp_type: The timestamp_type of this ProcessingSchema.
        :type timestamp_type: str
        """
        self._timestamp_type = timestamp_type

    @property
    def timestamp_format(self):
        r"""Gets the timestamp_format of this ProcessingSchema.

        源数据时间戳的类型为String时必选，用于根据时间戳格式生成OBS的时间目录。

        :return: The timestamp_format of this ProcessingSchema.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        r"""Sets the timestamp_format of this ProcessingSchema.

        源数据时间戳的类型为String时必选，用于根据时间戳格式生成OBS的时间目录。

        :param timestamp_format: The timestamp_format of this ProcessingSchema.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

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
        if not isinstance(other, ProcessingSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
