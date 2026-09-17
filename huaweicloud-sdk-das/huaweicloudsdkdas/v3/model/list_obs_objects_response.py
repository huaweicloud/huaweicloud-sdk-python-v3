# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsObjectsResponse(SdkResponse):

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
        'common_prefixes': 'list[str]'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'marker': 'marker',
        'next_marker': 'next_marker',
        'common_prefixes': 'common_prefixes'
    }

    def __init__(self, bucket_name=None, marker=None, next_marker=None, common_prefixes=None):
        r"""ListObsObjectsResponse

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称
        :type bucket_name: str
        :param marker: 当前页marker
        :type marker: str
        :param next_marker: 下一页marker
        :type next_marker: str
        :param common_prefixes: 文件夹列表
        :type common_prefixes: list[str]
        """
        
        super().__init__()

        self._bucket_name = None
        self._marker = None
        self._next_marker = None
        self._common_prefixes = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if marker is not None:
            self.marker = marker
        if next_marker is not None:
            self.next_marker = next_marker
        if common_prefixes is not None:
            self.common_prefixes = common_prefixes

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ListObsObjectsResponse.

        桶名称

        :return: The bucket_name of this ListObsObjectsResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ListObsObjectsResponse.

        桶名称

        :param bucket_name: The bucket_name of this ListObsObjectsResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def marker(self):
        r"""Gets the marker of this ListObsObjectsResponse.

        当前页marker

        :return: The marker of this ListObsObjectsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListObsObjectsResponse.

        当前页marker

        :param marker: The marker of this ListObsObjectsResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListObsObjectsResponse.

        下一页marker

        :return: The next_marker of this ListObsObjectsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListObsObjectsResponse.

        下一页marker

        :param next_marker: The next_marker of this ListObsObjectsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def common_prefixes(self):
        r"""Gets the common_prefixes of this ListObsObjectsResponse.

        文件夹列表

        :return: The common_prefixes of this ListObsObjectsResponse.
        :rtype: list[str]
        """
        return self._common_prefixes

    @common_prefixes.setter
    def common_prefixes(self, common_prefixes):
        r"""Sets the common_prefixes of this ListObsObjectsResponse.

        文件夹列表

        :param common_prefixes: The common_prefixes of this ListObsObjectsResponse.
        :type common_prefixes: list[str]
        """
        self._common_prefixes = common_prefixes

    def to_dict(self):
        import warnings
        warnings.warn("ListObsObjectsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListObsObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
