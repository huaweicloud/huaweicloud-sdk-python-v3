# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'objects': 'list[ObsObject]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'objects': 'objects',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, count=None, objects=None, x_request_id=None):
        """ListObsBucketObjectsResponse

        The model defined in huaweicloud sdk

        :param count: 对象的总数
        :type count: int
        :param objects: obs文件
        :type objects: list[:class:`huaweicloudsdkcloudrtc.v2.ObsObject`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListObsBucketObjectsResponse, self).__init__()

        self._count = None
        self._objects = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if objects is not None:
            self.objects = objects
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        """Gets the count of this ListObsBucketObjectsResponse.

        对象的总数

        :return: The count of this ListObsBucketObjectsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListObsBucketObjectsResponse.

        对象的总数

        :param count: The count of this ListObsBucketObjectsResponse.
        :type count: int
        """
        self._count = count

    @property
    def objects(self):
        """Gets the objects of this ListObsBucketObjectsResponse.

        obs文件

        :return: The objects of this ListObsBucketObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v2.ObsObject`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this ListObsBucketObjectsResponse.

        obs文件

        :param objects: The objects of this ListObsBucketObjectsResponse.
        :type objects: list[:class:`huaweicloudsdkcloudrtc.v2.ObsObject`]
        """
        self._objects = objects

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListObsBucketObjectsResponse.

        :return: The x_request_id of this ListObsBucketObjectsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListObsBucketObjectsResponse.

        :param x_request_id: The x_request_id of this ListObsBucketObjectsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListObsBucketObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
