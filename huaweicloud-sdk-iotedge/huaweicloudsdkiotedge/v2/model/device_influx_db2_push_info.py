# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceInfluxDB2PushInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization': 'str',
        'bucket': 'str',
        'format': 'str'
    }

    attribute_map = {
        'organization': 'organization',
        'bucket': 'bucket',
        'format': 'format'
    }

    def __init__(self, organization=None, bucket=None, format=None):
        r"""DeviceInfluxDB2PushInfo

        The model defined in huaweicloud sdk

        :param organization: 一组用户的工作空间，一组用户下可以创建多个bucket
        :type organization: str
        :param bucket: 数据存储的地方，结合了数据库和存储周期的概念
        :type bucket: str
        :param format: 数据格式转换类型
        :type format: str
        """
        
        

        self._organization = None
        self._bucket = None
        self._format = None
        self.discriminator = None

        self.organization = organization
        self.bucket = bucket
        self.format = format

    @property
    def organization(self):
        r"""Gets the organization of this DeviceInfluxDB2PushInfo.

        一组用户的工作空间，一组用户下可以创建多个bucket

        :return: The organization of this DeviceInfluxDB2PushInfo.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this DeviceInfluxDB2PushInfo.

        一组用户的工作空间，一组用户下可以创建多个bucket

        :param organization: The organization of this DeviceInfluxDB2PushInfo.
        :type organization: str
        """
        self._organization = organization

    @property
    def bucket(self):
        r"""Gets the bucket of this DeviceInfluxDB2PushInfo.

        数据存储的地方，结合了数据库和存储周期的概念

        :return: The bucket of this DeviceInfluxDB2PushInfo.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this DeviceInfluxDB2PushInfo.

        数据存储的地方，结合了数据库和存储周期的概念

        :param bucket: The bucket of this DeviceInfluxDB2PushInfo.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def format(self):
        r"""Gets the format of this DeviceInfluxDB2PushInfo.

        数据格式转换类型

        :return: The format of this DeviceInfluxDB2PushInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this DeviceInfluxDB2PushInfo.

        数据格式转换类型

        :param format: The format of this DeviceInfluxDB2PushInfo.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, DeviceInfluxDB2PushInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
