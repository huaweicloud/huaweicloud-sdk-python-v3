# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "ListObjectsResponse"

    sensitive_list = []

    openapi_types = {
        'contents': 'list[Contents]',
        'common_prefixes': 'list[CommonPrefixes]',
        'delimiter': 'str',
        'encoding_type': 'str',
        'is_truncated': 'bool',
        'marker': 'str',
        'next_marker': 'str',
        'max_keys': 'str',
        'name': 'str',
        'prefix': 'str',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'x_obs_bucket_type': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'contents': 'Contents',
        'common_prefixes': 'CommonPrefixes',
        'delimiter': 'Delimiter',
        'encoding_type': 'EncodingType',
        'is_truncated': 'IsTruncated',
        'marker': 'Marker',
        'next_marker': 'NextMarker',
        'max_keys': 'MaxKeys',
        'name': 'Name',
        'prefix': 'Prefix',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'x_obs_bucket_type': 'x-obs-bucket-type',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, contents=None, common_prefixes=None, delimiter=None, encoding_type=None, is_truncated=None, marker=None, next_marker=None, max_keys=None, name=None, prefix=None, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, x_obs_bucket_type=None, connection=None, content_length=None, date=None):
        r"""ListObjectsResponse

        The model defined in huaweicloud sdk

        :param contents: 
        :type contents: list[:class:`huaweicloudsdkobs.v1.Contents`]
        :param common_prefixes: 
        :type common_prefixes: list[:class:`huaweicloudsdkobs.v1.CommonPrefixes`]
        :param delimiter: The **delimiter** parameter specified in the request
        :type delimiter: str
        :param encoding_type: Encodes some elements in the response based on the specified type. If **encoding-type** is specified in the request, **Delimiter**, **Marker**, **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker**, and **Key** in the response will be encoded.
        :type encoding_type: str
        :param is_truncated: Determines whether the returned list of objects is truncated. **true**: Not all results are returned. **false**: All results have been returned.
        :type is_truncated: bool
        :param marker: Marker for the position from which objects in a bucket will be listed
        :type marker: str
        :param next_marker: A marker for the last returned object in the list. **NextMarker** is returned when not all the objects are listed. In subsequent requests, you can set **Marker** to the value of this parameter to list the remaining objects.
        :type next_marker: str
        :param max_keys: Maximum number of objects that can be listed
        :type max_keys: str
        :param name: Name of the requested bucket
        :type name: str
        :param prefix: Prefix of an object name. Only objects whose names have this prefix are listed.
        :type prefix: str
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_bucket_type: 
        :type x_obs_bucket_type: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ListObjectsResponse, self).__init__()

        self._contents = None
        self._common_prefixes = None
        self._delimiter = None
        self._encoding_type = None
        self._is_truncated = None
        self._marker = None
        self._next_marker = None
        self._max_keys = None
        self._name = None
        self._prefix = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._x_obs_bucket_type = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if contents is not None:
            self.contents = contents
        if common_prefixes is not None:
            self.common_prefixes = common_prefixes
        if delimiter is not None:
            self.delimiter = delimiter
        if encoding_type is not None:
            self.encoding_type = encoding_type
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if marker is not None:
            self.marker = marker
        if next_marker is not None:
            self.next_marker = next_marker
        if max_keys is not None:
            self.max_keys = max_keys
        if name is not None:
            self.name = name
        if prefix is not None:
            self.prefix = prefix
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_bucket_type is not None:
            self.x_obs_bucket_type = x_obs_bucket_type
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def contents(self):
        r"""Gets the contents of this ListObjectsResponse.

        :return: The contents of this ListObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkobs.v1.Contents`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this ListObjectsResponse.

        :param contents: The contents of this ListObjectsResponse.
        :type contents: list[:class:`huaweicloudsdkobs.v1.Contents`]
        """
        self._contents = contents

    @property
    def common_prefixes(self):
        r"""Gets the common_prefixes of this ListObjectsResponse.

        :return: The common_prefixes of this ListObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkobs.v1.CommonPrefixes`]
        """
        return self._common_prefixes

    @common_prefixes.setter
    def common_prefixes(self, common_prefixes):
        r"""Sets the common_prefixes of this ListObjectsResponse.

        :param common_prefixes: The common_prefixes of this ListObjectsResponse.
        :type common_prefixes: list[:class:`huaweicloudsdkobs.v1.CommonPrefixes`]
        """
        self._common_prefixes = common_prefixes

    @property
    def delimiter(self):
        r"""Gets the delimiter of this ListObjectsResponse.

        The **delimiter** parameter specified in the request

        :return: The delimiter of this ListObjectsResponse.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        r"""Sets the delimiter of this ListObjectsResponse.

        The **delimiter** parameter specified in the request

        :param delimiter: The delimiter of this ListObjectsResponse.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def encoding_type(self):
        r"""Gets the encoding_type of this ListObjectsResponse.

        Encodes some elements in the response based on the specified type. If **encoding-type** is specified in the request, **Delimiter**, **Marker**, **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker**, and **Key** in the response will be encoded.

        :return: The encoding_type of this ListObjectsResponse.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        r"""Sets the encoding_type of this ListObjectsResponse.

        Encodes some elements in the response based on the specified type. If **encoding-type** is specified in the request, **Delimiter**, **Marker**, **Prefix** (including the **Prefix** in **CommonPrefixes**), **NextMarker**, and **Key** in the response will be encoded.

        :param encoding_type: The encoding_type of this ListObjectsResponse.
        :type encoding_type: str
        """
        self._encoding_type = encoding_type

    @property
    def is_truncated(self):
        r"""Gets the is_truncated of this ListObjectsResponse.

        Determines whether the returned list of objects is truncated. **true**: Not all results are returned. **false**: All results have been returned.

        :return: The is_truncated of this ListObjectsResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        r"""Sets the is_truncated of this ListObjectsResponse.

        Determines whether the returned list of objects is truncated. **true**: Not all results are returned. **false**: All results have been returned.

        :param is_truncated: The is_truncated of this ListObjectsResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def marker(self):
        r"""Gets the marker of this ListObjectsResponse.

        Marker for the position from which objects in a bucket will be listed

        :return: The marker of this ListObjectsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListObjectsResponse.

        Marker for the position from which objects in a bucket will be listed

        :param marker: The marker of this ListObjectsResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListObjectsResponse.

        A marker for the last returned object in the list. **NextMarker** is returned when not all the objects are listed. In subsequent requests, you can set **Marker** to the value of this parameter to list the remaining objects.

        :return: The next_marker of this ListObjectsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListObjectsResponse.

        A marker for the last returned object in the list. **NextMarker** is returned when not all the objects are listed. In subsequent requests, you can set **Marker** to the value of this parameter to list the remaining objects.

        :param next_marker: The next_marker of this ListObjectsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListObjectsResponse.

        Maximum number of objects that can be listed

        :return: The max_keys of this ListObjectsResponse.
        :rtype: str
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListObjectsResponse.

        Maximum number of objects that can be listed

        :param max_keys: The max_keys of this ListObjectsResponse.
        :type max_keys: str
        """
        self._max_keys = max_keys

    @property
    def name(self):
        r"""Gets the name of this ListObjectsResponse.

        Name of the requested bucket

        :return: The name of this ListObjectsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListObjectsResponse.

        Name of the requested bucket

        :param name: The name of this ListObjectsResponse.
        :type name: str
        """
        self._name = name

    @property
    def prefix(self):
        r"""Gets the prefix of this ListObjectsResponse.

        Prefix of an object name. Only objects whose names have this prefix are listed.

        :return: The prefix of this ListObjectsResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListObjectsResponse.

        Prefix of an object name. Only objects whose names have this prefix are listed.

        :param prefix: The prefix of this ListObjectsResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this ListObjectsResponse.

        :return: The x_obs_id_2 of this ListObjectsResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this ListObjectsResponse.

        :param x_obs_id_2: The x_obs_id_2 of this ListObjectsResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this ListObjectsResponse.

        :return: The x_obs_request_id of this ListObjectsResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this ListObjectsResponse.

        :param x_obs_request_id: The x_obs_request_id of this ListObjectsResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this ListObjectsResponse.

        :return: The e_tag of this ListObjectsResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this ListObjectsResponse.

        :param e_tag: The e_tag of this ListObjectsResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_bucket_type(self):
        r"""Gets the x_obs_bucket_type of this ListObjectsResponse.

        :return: The x_obs_bucket_type of this ListObjectsResponse.
        :rtype: str
        """
        return self._x_obs_bucket_type

    @x_obs_bucket_type.setter
    def x_obs_bucket_type(self, x_obs_bucket_type):
        r"""Sets the x_obs_bucket_type of this ListObjectsResponse.

        :param x_obs_bucket_type: The x_obs_bucket_type of this ListObjectsResponse.
        :type x_obs_bucket_type: str
        """
        self._x_obs_bucket_type = x_obs_bucket_type

    @property
    def connection(self):
        r"""Gets the connection of this ListObjectsResponse.

        :return: The connection of this ListObjectsResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ListObjectsResponse.

        :param connection: The connection of this ListObjectsResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this ListObjectsResponse.

        :return: The content_length of this ListObjectsResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ListObjectsResponse.

        :param content_length: The content_length of this ListObjectsResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this ListObjectsResponse.

        :return: The date of this ListObjectsResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ListObjectsResponse.

        :param date: The date of this ListObjectsResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ListObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
