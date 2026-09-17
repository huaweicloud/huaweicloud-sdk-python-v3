# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'bucket_name': 'str',
        'max_keys': 'int',
        'marker': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'bucket_name': 'bucket_name',
        'max_keys': 'max_keys',
        'marker': 'marker',
        'prefix': 'prefix'
    }

    def __init__(self, instance_id=None, bucket_name=None, max_keys=None, marker=None, prefix=None):
        r"""ListObsObjectsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param bucket_name: OBS桶名
        :type bucket_name: str
        :param max_keys: 最大对象数量
        :type max_keys: int
        :param marker: 起始对象名称
        :type marker: str
        :param prefix: 对象前缀
        :type prefix: str
        """
        
        

        self._instance_id = None
        self._bucket_name = None
        self._max_keys = None
        self._marker = None
        self._prefix = None
        self.discriminator = None

        self.instance_id = instance_id
        self.bucket_name = bucket_name
        self.max_keys = max_keys
        self.marker = marker
        self.prefix = prefix

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListObsObjectsRequest.

        实例ID

        :return: The instance_id of this ListObsObjectsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListObsObjectsRequest.

        实例ID

        :param instance_id: The instance_id of this ListObsObjectsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ListObsObjectsRequest.

        OBS桶名

        :return: The bucket_name of this ListObsObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ListObsObjectsRequest.

        OBS桶名

        :param bucket_name: The bucket_name of this ListObsObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListObsObjectsRequest.

        最大对象数量

        :return: The max_keys of this ListObsObjectsRequest.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListObsObjectsRequest.

        最大对象数量

        :param max_keys: The max_keys of this ListObsObjectsRequest.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def marker(self):
        r"""Gets the marker of this ListObsObjectsRequest.

        起始对象名称

        :return: The marker of this ListObsObjectsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListObsObjectsRequest.

        起始对象名称

        :param marker: The marker of this ListObsObjectsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def prefix(self):
        r"""Gets the prefix of this ListObsObjectsRequest.

        对象前缀

        :return: The prefix of this ListObsObjectsRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListObsObjectsRequest.

        对象前缀

        :param prefix: The prefix of this ListObsObjectsRequest.
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
        if not isinstance(other, ListObsObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
