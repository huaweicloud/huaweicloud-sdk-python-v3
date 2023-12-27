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
        """ListObjectsRequest

        The model defined in huaweicloud sdk

        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param bucket_name: 请求的桶名称。 
        :type bucket_name: str
        :param prefix: 列举以指定的字符串prefix开头的对象。 
        :type prefix: str
        :param marker: 列举桶内对象列表时，指定一个标识符，从该标识符以后按字典顺序返回对象列表。 
        :type marker: str
        :param max_keys: 指定返回的最大对象数，返回的对象列表将是按照字典顺序的最多前max-keys个对象，范围是[1，1000]，超出范围时，按照默认的1000进行处理。 
        :type max_keys: int
        :param delimiter: 将对象名进行分组的分隔符。如果指定了prefix，从prefix到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes；如果没有指定prefix，从对象名的首字符到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes。  例如，桶中有3个对象，分别为abcd、abcde、bbcde。如果指定delimiter为d，prefix为a，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes；如果只指定delimiter为d，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes，而bbcde会被单独分成一组，形成一条前缀为bbcd的CommonPrefixes。 
        :type delimiter: str
        :param key_marker: 列举对象时的起始位置。 有效值：上次请求返回体的NextKeyMarker值 
        :type key_marker: str
        :param version_id_marker: 本参数只适用于多版本例举场景  与请求中的key-marker配合使用，返回的对象列表将是按照字典顺序排序后在该标识符以后的对象(单次返回最大为1000个)。如果version-id-marker不是key-marker对应的一个版本号，则该参数无效。  有效值：对象的版本号，即上次请求返回体的NextVersionIdMarker值 
        :type version_id_marker: str
        :param encoding_type: 对响应中的部分元素进行指定类型的编码。如果Delimiter、Marker（或KeyMarker）、Prefix、NextMarker（或NextKeyMarker）和Key包含xml 1.0标准不支持的控制字符，可通过设置encoding-type对响应中的Delimiter、Marker（或KeyMarker）、Prefix（包括CommonPrefixes中的Prefix）、NextMarker（或NextKeyMarker）和Key进行编码。  可选值：url 
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
        """Gets the date of this ListObjectsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this ListObjectsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListObjectsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this ListObjectsRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListObjectsRequest.

        请求的桶名称。 

        :return: The bucket_name of this ListObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListObjectsRequest.

        请求的桶名称。 

        :param bucket_name: The bucket_name of this ListObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        """Gets the prefix of this ListObjectsRequest.

        列举以指定的字符串prefix开头的对象。 

        :return: The prefix of this ListObjectsRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ListObjectsRequest.

        列举以指定的字符串prefix开头的对象。 

        :param prefix: The prefix of this ListObjectsRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def marker(self):
        """Gets the marker of this ListObjectsRequest.

        列举桶内对象列表时，指定一个标识符，从该标识符以后按字典顺序返回对象列表。 

        :return: The marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListObjectsRequest.

        列举桶内对象列表时，指定一个标识符，从该标识符以后按字典顺序返回对象列表。 

        :param marker: The marker of this ListObjectsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def max_keys(self):
        """Gets the max_keys of this ListObjectsRequest.

        指定返回的最大对象数，返回的对象列表将是按照字典顺序的最多前max-keys个对象，范围是[1，1000]，超出范围时，按照默认的1000进行处理。 

        :return: The max_keys of this ListObjectsRequest.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        """Sets the max_keys of this ListObjectsRequest.

        指定返回的最大对象数，返回的对象列表将是按照字典顺序的最多前max-keys个对象，范围是[1，1000]，超出范围时，按照默认的1000进行处理。 

        :param max_keys: The max_keys of this ListObjectsRequest.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def delimiter(self):
        """Gets the delimiter of this ListObjectsRequest.

        将对象名进行分组的分隔符。如果指定了prefix，从prefix到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes；如果没有指定prefix，从对象名的首字符到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes。  例如，桶中有3个对象，分别为abcd、abcde、bbcde。如果指定delimiter为d，prefix为a，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes；如果只指定delimiter为d，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes，而bbcde会被单独分成一组，形成一条前缀为bbcd的CommonPrefixes。 

        :return: The delimiter of this ListObjectsRequest.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ListObjectsRequest.

        将对象名进行分组的分隔符。如果指定了prefix，从prefix到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes；如果没有指定prefix，从对象名的首字符到第一次出现delimiter间具有相同字符串的对象名会被分成一组，形成一条CommonPrefixes。  例如，桶中有3个对象，分别为abcd、abcde、bbcde。如果指定delimiter为d，prefix为a，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes；如果只指定delimiter为d，abcd、abcde会被分成一组，形成一条前缀为abcd的CommonPrefixes，而bbcde会被单独分成一组，形成一条前缀为bbcd的CommonPrefixes。 

        :param delimiter: The delimiter of this ListObjectsRequest.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def key_marker(self):
        """Gets the key_marker of this ListObjectsRequest.

        列举对象时的起始位置。 有效值：上次请求返回体的NextKeyMarker值 

        :return: The key_marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._key_marker

    @key_marker.setter
    def key_marker(self, key_marker):
        """Sets the key_marker of this ListObjectsRequest.

        列举对象时的起始位置。 有效值：上次请求返回体的NextKeyMarker值 

        :param key_marker: The key_marker of this ListObjectsRequest.
        :type key_marker: str
        """
        self._key_marker = key_marker

    @property
    def version_id_marker(self):
        """Gets the version_id_marker of this ListObjectsRequest.

        本参数只适用于多版本例举场景  与请求中的key-marker配合使用，返回的对象列表将是按照字典顺序排序后在该标识符以后的对象(单次返回最大为1000个)。如果version-id-marker不是key-marker对应的一个版本号，则该参数无效。  有效值：对象的版本号，即上次请求返回体的NextVersionIdMarker值 

        :return: The version_id_marker of this ListObjectsRequest.
        :rtype: str
        """
        return self._version_id_marker

    @version_id_marker.setter
    def version_id_marker(self, version_id_marker):
        """Sets the version_id_marker of this ListObjectsRequest.

        本参数只适用于多版本例举场景  与请求中的key-marker配合使用，返回的对象列表将是按照字典顺序排序后在该标识符以后的对象(单次返回最大为1000个)。如果version-id-marker不是key-marker对应的一个版本号，则该参数无效。  有效值：对象的版本号，即上次请求返回体的NextVersionIdMarker值 

        :param version_id_marker: The version_id_marker of this ListObjectsRequest.
        :type version_id_marker: str
        """
        self._version_id_marker = version_id_marker

    @property
    def encoding_type(self):
        """Gets the encoding_type of this ListObjectsRequest.

        对响应中的部分元素进行指定类型的编码。如果Delimiter、Marker（或KeyMarker）、Prefix、NextMarker（或NextKeyMarker）和Key包含xml 1.0标准不支持的控制字符，可通过设置encoding-type对响应中的Delimiter、Marker（或KeyMarker）、Prefix（包括CommonPrefixes中的Prefix）、NextMarker（或NextKeyMarker）和Key进行编码。  可选值：url 

        :return: The encoding_type of this ListObjectsRequest.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        """Sets the encoding_type of this ListObjectsRequest.

        对响应中的部分元素进行指定类型的编码。如果Delimiter、Marker（或KeyMarker）、Prefix、NextMarker（或NextKeyMarker）和Key包含xml 1.0标准不支持的控制字符，可通过设置encoding-type对响应中的Delimiter、Marker（或KeyMarker）、Prefix（包括CommonPrefixes中的Prefix）、NextMarker（或NextKeyMarker）和Key进行编码。  可选值：url 

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
