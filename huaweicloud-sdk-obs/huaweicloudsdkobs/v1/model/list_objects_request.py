# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "ListObjectsRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'prefix': 'str',
        'marker': 'str',
        'max_keys': 'int',
        'delimiter': 'str',
        'key_marker': 'str',
        'version_id_marker': 'str',
        'encoding_type': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'prefix': 'prefix',
        'marker': 'marker',
        'max_keys': 'max-keys',
        'delimiter': 'delimiter',
        'key_marker': 'key-marker',
        'version_id_marker': 'version-id-marker',
        'encoding_type': 'encoding-type'
    }

    def __init__(self, date=None, bucket_name=None, prefix=None, marker=None, max_keys=None, delimiter=None, key_marker=None, version_id_marker=None, encoding_type=None):
        r"""ListObjectsRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param prefix: Lists objects whose name starts with the specified prefix.
        :type prefix: str
        :param marker: Specifies a marker when listing objects in a bucket. With a marker configured, objects after this marker will be returned in alphabetical order.
        :type marker: str
        :param max_keys: Sets the maximum number of objects returned (in alphabetical order) in the response. The value ranges from 1 to 1000. If there are over 1,000 objects, only 1,000 objects are returned by default.
        :type max_keys: int
        :param delimiter: Separator used to group object names. If a prefix is specified, objects with the same string from the prefix to the first delimiter are grouped into one **CommonPrefixes**. If no prefix is specified, objects with the same string from the first character to the first delimiter are grouped into one **CommonPrefixes**.  Assume that a bucket has objects **abcd**, **abcde**, and **bbcde** in it. If **delimiter** is set to **d** and **prefix** is set to **a**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix. If only **delimiter** is set to **d**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix, and **bbcde** is grouped separately into another **CommonPrefixes** with **bbcd** as the prefix.
        :type delimiter: str
        :param key_marker: Position to start with when objects are listed. Valid value: value of **NextKeyMarker** in the response body of the last request
        :type key_marker: str
        :param version_id_marker: This parameter applies only when versioning is enabled.  Specifies the version ID to start with when objects in a bucket are listed. Objects are listed in alphabetical order and a maximum of 1,000 objects can be displayed at a time. This parameter is used together with **key-marker**. If the value of **version-id-marker** does not match **key-marker**, **version-id-marker** is invalid.  Valid value: object version ID, which is the value of **NextVersionIdMarker** in the response body of the last request
        :type version_id_marker: str
        :param encoding_type: Encodes some elements in the response based on the specified type. If **Delimiter**, **Marker** (or **KeyMarker**), **Prefix**, **NextMarker** (or **NextKeyMarker**), and **Key** contain control characters that are not supported by XML 1.0 standards, you can configure **encoding-type** to encode **Delimiter**, **Marker** (or **KeyMarker**), **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker** (or **NextKeyMarker**), and **Key** in the response.  Optional value: url
        :type encoding_type: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._prefix = None
        self._marker = None
        self._max_keys = None
        self._delimiter = None
        self._key_marker = None
        self._version_id_marker = None
        self._encoding_type = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        if prefix is not None:
            self.prefix = prefix
        if marker is not None:
            self.marker = marker
        if max_keys is not None:
            self.max_keys = max_keys
        if delimiter is not None:
            self.delimiter = delimiter
        if key_marker is not None:
            self.key_marker = key_marker
        if version_id_marker is not None:
            self.version_id_marker = version_id_marker
        if encoding_type is not None:
            self.encoding_type = encoding_type

    @property
    def date(self):
        r"""Gets the date of this ListObjectsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this ListObjectsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ListObjectsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this ListObjectsRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ListObjectsRequest.

        Name of the requested bucket

        :return: The bucket_name of this ListObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ListObjectsRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this ListObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        r"""Gets the prefix of this ListObjectsRequest.

        Lists objects whose name starts with the specified prefix.

        :return: The prefix of this ListObjectsRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListObjectsRequest.

        Lists objects whose name starts with the specified prefix.

        :param prefix: The prefix of this ListObjectsRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def marker(self):
        r"""Gets the marker of this ListObjectsRequest.

        Specifies a marker when listing objects in a bucket. With a marker configured, objects after this marker will be returned in alphabetical order.

        :return: The marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListObjectsRequest.

        Specifies a marker when listing objects in a bucket. With a marker configured, objects after this marker will be returned in alphabetical order.

        :param marker: The marker of this ListObjectsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListObjectsRequest.

        Sets the maximum number of objects returned (in alphabetical order) in the response. The value ranges from 1 to 1000. If there are over 1,000 objects, only 1,000 objects are returned by default.

        :return: The max_keys of this ListObjectsRequest.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListObjectsRequest.

        Sets the maximum number of objects returned (in alphabetical order) in the response. The value ranges from 1 to 1000. If there are over 1,000 objects, only 1,000 objects are returned by default.

        :param max_keys: The max_keys of this ListObjectsRequest.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def delimiter(self):
        r"""Gets the delimiter of this ListObjectsRequest.

        Separator used to group object names. If a prefix is specified, objects with the same string from the prefix to the first delimiter are grouped into one **CommonPrefixes**. If no prefix is specified, objects with the same string from the first character to the first delimiter are grouped into one **CommonPrefixes**.  Assume that a bucket has objects **abcd**, **abcde**, and **bbcde** in it. If **delimiter** is set to **d** and **prefix** is set to **a**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix. If only **delimiter** is set to **d**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix, and **bbcde** is grouped separately into another **CommonPrefixes** with **bbcd** as the prefix.

        :return: The delimiter of this ListObjectsRequest.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        r"""Sets the delimiter of this ListObjectsRequest.

        Separator used to group object names. If a prefix is specified, objects with the same string from the prefix to the first delimiter are grouped into one **CommonPrefixes**. If no prefix is specified, objects with the same string from the first character to the first delimiter are grouped into one **CommonPrefixes**.  Assume that a bucket has objects **abcd**, **abcde**, and **bbcde** in it. If **delimiter** is set to **d** and **prefix** is set to **a**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix. If only **delimiter** is set to **d**, objects **abcd** and **abcde** are grouped into a **CommonPrefixes** with **abcd** as the prefix, and **bbcde** is grouped separately into another **CommonPrefixes** with **bbcd** as the prefix.

        :param delimiter: The delimiter of this ListObjectsRequest.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def key_marker(self):
        r"""Gets the key_marker of this ListObjectsRequest.

        Position to start with when objects are listed. Valid value: value of **NextKeyMarker** in the response body of the last request

        :return: The key_marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._key_marker

    @key_marker.setter
    def key_marker(self, key_marker):
        r"""Sets the key_marker of this ListObjectsRequest.

        Position to start with when objects are listed. Valid value: value of **NextKeyMarker** in the response body of the last request

        :param key_marker: The key_marker of this ListObjectsRequest.
        :type key_marker: str
        """
        self._key_marker = key_marker

    @property
    def version_id_marker(self):
        r"""Gets the version_id_marker of this ListObjectsRequest.

        This parameter applies only when versioning is enabled.  Specifies the version ID to start with when objects in a bucket are listed. Objects are listed in alphabetical order and a maximum of 1,000 objects can be displayed at a time. This parameter is used together with **key-marker**. If the value of **version-id-marker** does not match **key-marker**, **version-id-marker** is invalid.  Valid value: object version ID, which is the value of **NextVersionIdMarker** in the response body of the last request

        :return: The version_id_marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._version_id_marker

    @version_id_marker.setter
    def version_id_marker(self, version_id_marker):
        r"""Sets the version_id_marker of this ListObjectsRequest.

        This parameter applies only when versioning is enabled.  Specifies the version ID to start with when objects in a bucket are listed. Objects are listed in alphabetical order and a maximum of 1,000 objects can be displayed at a time. This parameter is used together with **key-marker**. If the value of **version-id-marker** does not match **key-marker**, **version-id-marker** is invalid.  Valid value: object version ID, which is the value of **NextVersionIdMarker** in the response body of the last request

        :param version_id_marker: The version_id_marker of this ListObjectsRequest.
        :type version_id_marker: str
        """
        self._version_id_marker = version_id_marker

    @property
    def encoding_type(self):
        r"""Gets the encoding_type of this ListObjectsRequest.

        Encodes some elements in the response based on the specified type. If **Delimiter**, **Marker** (or **KeyMarker**), **Prefix**, **NextMarker** (or **NextKeyMarker**), and **Key** contain control characters that are not supported by XML 1.0 standards, you can configure **encoding-type** to encode **Delimiter**, **Marker** (or **KeyMarker**), **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker** (or **NextKeyMarker**), and **Key** in the response.  Optional value: url

        :return: The encoding_type of this ListObjectsRequest.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        r"""Sets the encoding_type of this ListObjectsRequest.

        Encodes some elements in the response based on the specified type. If **Delimiter**, **Marker** (or **KeyMarker**), **Prefix**, **NextMarker** (or **NextKeyMarker**), and **Key** contain control characters that are not supported by XML 1.0 standards, you can configure **encoding-type** to encode **Delimiter**, **Marker** (or **KeyMarker**), **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker** (or **NextKeyMarker**), and **Key** in the response.  Optional value: url

        :param encoding_type: The encoding_type of this ListObjectsRequest.
        :type encoding_type: str
        """
        self._encoding_type = encoding_type

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
        if not isinstance(other, ListObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
