# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportExportObsObjectsResponse(SdkResponse):

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
        'marker': 'str',
        'next_marker': 'str',
        'truncated': 'bool',
        'max_keys': 'int',
        'prefix': 'str',
        'common_prefixes': 'list[str]',
        'contents': 'list[ObsObjectInfo]'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'marker': 'marker',
        'next_marker': 'next_marker',
        'truncated': 'truncated',
        'max_keys': 'max_keys',
        'prefix': 'prefix',
        'common_prefixes': 'common_prefixes',
        'contents': 'contents'
    }

    def __init__(self, bucket_name=None, marker=None, next_marker=None, truncated=None, max_keys=None, prefix=None, common_prefixes=None, contents=None):
        r"""ImportExportObsObjectsResponse

        The model defined in huaweicloud sdk

        :param bucket_name: OBS桶名
        :type bucket_name: str
        :param marker: 列举桶内对象列表时，指定一个标识符，作为列举时的起始位置
        :type marker: str
        :param next_marker: 如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象
        :type next_marker: str
        :param truncated: 表明本次请求是否返回了全部结果
        :type truncated: bool
        :param max_keys: 列举对象的最大数目
        :type max_keys: int
        :param prefix: 列举桶内对象列表时，指定一个前缀
        :type prefix: str
        :param common_prefixes: 分组信息
        :type common_prefixes: list[str]
        :param contents: 对象的元数据信息
        :type contents: list[:class:`huaweicloudsdkdas.v3.ObsObjectInfo`]
        """
        
        super().__init__()

        self._bucket_name = None
        self._marker = None
        self._next_marker = None
        self._truncated = None
        self._max_keys = None
        self._prefix = None
        self._common_prefixes = None
        self._contents = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if marker is not None:
            self.marker = marker
        if next_marker is not None:
            self.next_marker = next_marker
        if truncated is not None:
            self.truncated = truncated
        if max_keys is not None:
            self.max_keys = max_keys
        if prefix is not None:
            self.prefix = prefix
        if common_prefixes is not None:
            self.common_prefixes = common_prefixes
        if contents is not None:
            self.contents = contents

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ImportExportObsObjectsResponse.

        OBS桶名

        :return: The bucket_name of this ImportExportObsObjectsResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ImportExportObsObjectsResponse.

        OBS桶名

        :param bucket_name: The bucket_name of this ImportExportObsObjectsResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def marker(self):
        r"""Gets the marker of this ImportExportObsObjectsResponse.

        列举桶内对象列表时，指定一个标识符，作为列举时的起始位置

        :return: The marker of this ImportExportObsObjectsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ImportExportObsObjectsResponse.

        列举桶内对象列表时，指定一个标识符，作为列举时的起始位置

        :param marker: The marker of this ImportExportObsObjectsResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ImportExportObsObjectsResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象

        :return: The next_marker of this ImportExportObsObjectsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ImportExportObsObjectsResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象

        :param next_marker: The next_marker of this ImportExportObsObjectsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def truncated(self):
        r"""Gets the truncated of this ImportExportObsObjectsResponse.

        表明本次请求是否返回了全部结果

        :return: The truncated of this ImportExportObsObjectsResponse.
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        r"""Sets the truncated of this ImportExportObsObjectsResponse.

        表明本次请求是否返回了全部结果

        :param truncated: The truncated of this ImportExportObsObjectsResponse.
        :type truncated: bool
        """
        self._truncated = truncated

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ImportExportObsObjectsResponse.

        列举对象的最大数目

        :return: The max_keys of this ImportExportObsObjectsResponse.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ImportExportObsObjectsResponse.

        列举对象的最大数目

        :param max_keys: The max_keys of this ImportExportObsObjectsResponse.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def prefix(self):
        r"""Gets the prefix of this ImportExportObsObjectsResponse.

        列举桶内对象列表时，指定一个前缀

        :return: The prefix of this ImportExportObsObjectsResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ImportExportObsObjectsResponse.

        列举桶内对象列表时，指定一个前缀

        :param prefix: The prefix of this ImportExportObsObjectsResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def common_prefixes(self):
        r"""Gets the common_prefixes of this ImportExportObsObjectsResponse.

        分组信息

        :return: The common_prefixes of this ImportExportObsObjectsResponse.
        :rtype: list[str]
        """
        return self._common_prefixes

    @common_prefixes.setter
    def common_prefixes(self, common_prefixes):
        r"""Sets the common_prefixes of this ImportExportObsObjectsResponse.

        分组信息

        :param common_prefixes: The common_prefixes of this ImportExportObsObjectsResponse.
        :type common_prefixes: list[str]
        """
        self._common_prefixes = common_prefixes

    @property
    def contents(self):
        r"""Gets the contents of this ImportExportObsObjectsResponse.

        对象的元数据信息

        :return: The contents of this ImportExportObsObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ObsObjectInfo`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this ImportExportObsObjectsResponse.

        对象的元数据信息

        :param contents: The contents of this ImportExportObsObjectsResponse.
        :type contents: list[:class:`huaweicloudsdkdas.v3.ObsObjectInfo`]
        """
        self._contents = contents

    def to_dict(self):
        import warnings
        warnings.warn("ImportExportObsObjectsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ImportExportObsObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
