# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObjectMetaDataRequest:

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
        'object': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, bucket=None, object=None, marker=None, limit=None):
        r"""ShowObjectMetaDataRequest

        The model defined in huaweicloud sdk

        :param bucket: obs桶名称
        :type bucket: str
        :param object: obs对象路径
        :type object: str
        :param marker: 列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表
        :type marker: str
        :param limit: 列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前limit个对象
        :type limit: int
        """
        
        

        self._bucket = None
        self._object = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.bucket = bucket
        if object is not None:
            self.object = object
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowObjectMetaDataRequest.

        obs桶名称

        :return: The bucket of this ShowObjectMetaDataRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowObjectMetaDataRequest.

        obs桶名称

        :param bucket: The bucket of this ShowObjectMetaDataRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        r"""Gets the object of this ShowObjectMetaDataRequest.

        obs对象路径

        :return: The object of this ShowObjectMetaDataRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        r"""Sets the object of this ShowObjectMetaDataRequest.

        obs对象路径

        :param object: The object of this ShowObjectMetaDataRequest.
        :type object: str
        """
        self._object = object

    @property
    def marker(self):
        r"""Gets the marker of this ShowObjectMetaDataRequest.

        列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表

        :return: The marker of this ShowObjectMetaDataRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowObjectMetaDataRequest.

        列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表

        :param marker: The marker of this ShowObjectMetaDataRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ShowObjectMetaDataRequest.

        列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前limit个对象

        :return: The limit of this ShowObjectMetaDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowObjectMetaDataRequest.

        列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前limit个对象

        :param limit: The limit of this ShowObjectMetaDataRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowObjectMetaDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
