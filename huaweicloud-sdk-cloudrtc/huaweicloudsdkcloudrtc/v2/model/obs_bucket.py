# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsBucket:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'location': 'str',
        'creation_date': 'str',
        'is_authorized': 'bool'
    }

    attribute_map = {
        'bucket': 'bucket',
        'location': 'location',
        'creation_date': 'creation_date',
        'is_authorized': 'is_authorized'
    }

    def __init__(self, bucket=None, location=None, creation_date=None, is_authorized=None):
        r"""ObsBucket

        The model defined in huaweicloud sdk

        :param bucket: OBS的bucket名称
        :type bucket: str
        :param location: OBS的bucket所在region
        :type location: str
        :param creation_date: 创建时间，格式如：2020/07/16 15:11:55 GMT+08:00
        :type creation_date: str
        :param is_authorized: 鉴权
        :type is_authorized: bool
        """
        
        

        self._bucket = None
        self._location = None
        self._creation_date = None
        self._is_authorized = None
        self.discriminator = None

        self.bucket = bucket
        self.location = location
        self.creation_date = creation_date
        self.is_authorized = is_authorized

    @property
    def bucket(self):
        r"""Gets the bucket of this ObsBucket.

        OBS的bucket名称

        :return: The bucket of this ObsBucket.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ObsBucket.

        OBS的bucket名称

        :param bucket: The bucket of this ObsBucket.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def location(self):
        r"""Gets the location of this ObsBucket.

        OBS的bucket所在region

        :return: The location of this ObsBucket.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ObsBucket.

        OBS的bucket所在region

        :param location: The location of this ObsBucket.
        :type location: str
        """
        self._location = location

    @property
    def creation_date(self):
        r"""Gets the creation_date of this ObsBucket.

        创建时间，格式如：2020/07/16 15:11:55 GMT+08:00

        :return: The creation_date of this ObsBucket.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this ObsBucket.

        创建时间，格式如：2020/07/16 15:11:55 GMT+08:00

        :param creation_date: The creation_date of this ObsBucket.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def is_authorized(self):
        r"""Gets the is_authorized of this ObsBucket.

        鉴权

        :return: The is_authorized of this ObsBucket.
        :rtype: bool
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        r"""Sets the is_authorized of this ObsBucket.

        鉴权

        :param is_authorized: The is_authorized of this ObsBucket.
        :type is_authorized: bool
        """
        self._is_authorized = is_authorized

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
        if not isinstance(other, ObsBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
