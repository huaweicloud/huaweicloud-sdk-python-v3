# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportExportObsObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'bucket_name': 'str',
        'max_keys': 'int',
        'marker': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'bucket_name': 'bucket_name',
        'max_keys': 'max_keys',
        'marker': 'marker',
        'prefix': 'prefix'
    }

    def __init__(self, connection_id=None, bucket_name=None, max_keys=None, marker=None, prefix=None):
        r"""ImportExportObsObjectsRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param max_keys: 最大返回对象数
        :type max_keys: int
        :param marker: 标记
        :type marker: str
        :param prefix: 前缀
        :type prefix: str
        """
        
        

        self._connection_id = None
        self._bucket_name = None
        self._max_keys = None
        self._marker = None
        self._prefix = None
        self.discriminator = None

        self.connection_id = connection_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if max_keys is not None:
            self.max_keys = max_keys
        if marker is not None:
            self.marker = marker
        if prefix is not None:
            self.prefix = prefix

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ImportExportObsObjectsRequest.

        连接ID

        :return: The connection_id of this ImportExportObsObjectsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ImportExportObsObjectsRequest.

        连接ID

        :param connection_id: The connection_id of this ImportExportObsObjectsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ImportExportObsObjectsRequest.

        桶名称

        :return: The bucket_name of this ImportExportObsObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ImportExportObsObjectsRequest.

        桶名称

        :param bucket_name: The bucket_name of this ImportExportObsObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ImportExportObsObjectsRequest.

        最大返回对象数

        :return: The max_keys of this ImportExportObsObjectsRequest.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ImportExportObsObjectsRequest.

        最大返回对象数

        :param max_keys: The max_keys of this ImportExportObsObjectsRequest.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def marker(self):
        r"""Gets the marker of this ImportExportObsObjectsRequest.

        标记

        :return: The marker of this ImportExportObsObjectsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ImportExportObsObjectsRequest.

        标记

        :param marker: The marker of this ImportExportObsObjectsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def prefix(self):
        r"""Gets the prefix of this ImportExportObsObjectsRequest.

        前缀

        :return: The prefix of this ImportExportObsObjectsRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ImportExportObsObjectsRequest.

        前缀

        :param prefix: The prefix of this ImportExportObsObjectsRequest.
        :type prefix: str
        """
        self._prefix = prefix

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
        if not isinstance(other, ImportExportObsObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
