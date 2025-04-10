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
    xml_name = "Bucket"

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'creation_date': 'str',
        'location': 'str',
        'cluster_type': 'str',
        'ies_location': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'creation_date': 'CreationDate',
        'location': 'Location',
        'cluster_type': 'ClusterType',
        'ies_location': 'IESLocation'
    }

    def __init__(self, name=None, creation_date=None, location=None, cluster_type=None, ies_location=None):
        r"""Bucket

        The model defined in huaweicloud sdk

        :param name: Name of the bucket
        :type name: str
        :param creation_date: Time when the bucket was created
        :type creation_date: str
        :param location: Location of the bucket
        :type location: str
        :param cluster_type: Type of the cluster where the bucket is created. This field is returned when the bucket is created in a dedicated cluster. This field is not returned in other cases.
        :type cluster_type: str
        :param ies_location: If a bucket is created in a cluster at the IES site, the ID of the IES site is returned.  This header is not returned in other cases.
        :type ies_location: str
        """
        
        

        self._name = None
        self._creation_date = None
        self._location = None
        self._cluster_type = None
        self._ies_location = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creation_date is not None:
            self.creation_date = creation_date
        if location is not None:
            self.location = location
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if ies_location is not None:
            self.ies_location = ies_location

    @property
    def name(self):
        r"""Gets the name of this Bucket.

        Name of the bucket

        :return: The name of this Bucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Bucket.

        Name of the bucket

        :param name: The name of this Bucket.
        :type name: str
        """
        self._name = name

    @property
    def creation_date(self):
        r"""Gets the creation_date of this Bucket.

        Time when the bucket was created

        :return: The creation_date of this Bucket.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this Bucket.

        Time when the bucket was created

        :param creation_date: The creation_date of this Bucket.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def location(self):
        r"""Gets the location of this Bucket.

        Location of the bucket

        :return: The location of this Bucket.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this Bucket.

        Location of the bucket

        :param location: The location of this Bucket.
        :type location: str
        """
        self._location = location

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this Bucket.

        Type of the cluster where the bucket is created. This field is returned when the bucket is created in a dedicated cluster. This field is not returned in other cases.

        :return: The cluster_type of this Bucket.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this Bucket.

        Type of the cluster where the bucket is created. This field is returned when the bucket is created in a dedicated cluster. This field is not returned in other cases.

        :param cluster_type: The cluster_type of this Bucket.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def ies_location(self):
        r"""Gets the ies_location of this Bucket.

        If a bucket is created in a cluster at the IES site, the ID of the IES site is returned.  This header is not returned in other cases.

        :return: The ies_location of this Bucket.
        :rtype: str
        """
        return self._ies_location

    @ies_location.setter
    def ies_location(self, ies_location):
        r"""Sets the ies_location of this Bucket.

        If a bucket is created in a cluster at the IES site, the ID of the IES site is returned.  This header is not returned in other cases.

        :param ies_location: The ies_location of this Bucket.
        :type ies_location: str
        """
        self._ies_location = ies_location

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
