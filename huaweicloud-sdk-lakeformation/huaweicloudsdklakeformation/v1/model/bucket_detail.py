# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketDetail:

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
        'creation_date': 'datetime',
        'location': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creation_date': 'creation_date',
        'location': 'location'
    }

    def __init__(self, id=None, name=None, creation_date=None, location=None):
        """BucketDetail

        The model defined in huaweicloud sdk

        :param id: obs桶id
        :type id: str
        :param name: obs桶名
        :type name: str
        :param creation_date: obs桶创建时间
        :type creation_date: datetime
        :param location: 所属region
        :type location: str
        """
        
        

        self._id = None
        self._name = None
        self._creation_date = None
        self._location = None
        self.discriminator = None

        self.id = id
        self.name = name
        if creation_date is not None:
            self.creation_date = creation_date
        self.location = location

    @property
    def id(self):
        """Gets the id of this BucketDetail.

        obs桶id

        :return: The id of this BucketDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BucketDetail.

        obs桶id

        :param id: The id of this BucketDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BucketDetail.

        obs桶名

        :return: The name of this BucketDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BucketDetail.

        obs桶名

        :param name: The name of this BucketDetail.
        :type name: str
        """
        self._name = name

    @property
    def creation_date(self):
        """Gets the creation_date of this BucketDetail.

        obs桶创建时间

        :return: The creation_date of this BucketDetail.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this BucketDetail.

        obs桶创建时间

        :param creation_date: The creation_date of this BucketDetail.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def location(self):
        """Gets the location of this BucketDetail.

        所属region

        :return: The location of this BucketDetail.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BucketDetail.

        所属region

        :param location: The location of this BucketDetail.
        :type location: str
        """
        self._location = location

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
        if not isinstance(other, BucketDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
