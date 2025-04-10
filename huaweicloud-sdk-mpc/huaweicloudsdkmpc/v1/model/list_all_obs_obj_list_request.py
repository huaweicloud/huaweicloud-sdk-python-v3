# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllObsObjListRequest:

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
        'prefix': 'str',
        'type': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'prefix': 'prefix',
        'type': 'type'
    }

    def __init__(self, bucket=None, prefix=None, type=None):
        r"""ListAllObsObjListRequest

        The model defined in huaweicloud sdk

        :param bucket: 桶名
        :type bucket: str
        :param prefix: 查询对象前缀
        :type prefix: str
        :param type: 查询对象文件类型
        :type type: str
        """
        
        

        self._bucket = None
        self._prefix = None
        self._type = None
        self.discriminator = None

        self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        if type is not None:
            self.type = type

    @property
    def bucket(self):
        r"""Gets the bucket of this ListAllObsObjListRequest.

        桶名

        :return: The bucket of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ListAllObsObjListRequest.

        桶名

        :param bucket: The bucket of this ListAllObsObjListRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        r"""Gets the prefix of this ListAllObsObjListRequest.

        查询对象前缀

        :return: The prefix of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListAllObsObjListRequest.

        查询对象前缀

        :param prefix: The prefix of this ListAllObsObjListRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def type(self):
        r"""Gets the type of this ListAllObsObjListRequest.

        查询对象文件类型

        :return: The type of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAllObsObjListRequest.

        查询对象文件类型

        :param type: The type of this ListAllObsObjListRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAllObsObjListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
