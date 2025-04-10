# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObsBucketObjectResponse(SdkResponse):

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
        'objects': 'list[BucketObjectDto]'
    }

    attribute_map = {
        'count': 'count',
        'objects': 'objects'
    }

    def __init__(self, count=None, objects=None):
        r"""ListObsBucketObjectResponse

        The model defined in huaweicloud sdk

        :param count: 数据（文件夹、文件）总数量
        :type count: int
        :param objects: 数据列表
        :type objects: list[:class:`huaweicloudsdkeihealth.v1.BucketObjectDto`]
        """
        
        super(ListObsBucketObjectResponse, self).__init__()

        self._count = None
        self._objects = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if objects is not None:
            self.objects = objects

    @property
    def count(self):
        r"""Gets the count of this ListObsBucketObjectResponse.

        数据（文件夹、文件）总数量

        :return: The count of this ListObsBucketObjectResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListObsBucketObjectResponse.

        数据（文件夹、文件）总数量

        :param count: The count of this ListObsBucketObjectResponse.
        :type count: int
        """
        self._count = count

    @property
    def objects(self):
        r"""Gets the objects of this ListObsBucketObjectResponse.

        数据列表

        :return: The objects of this ListObsBucketObjectResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BucketObjectDto`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this ListObsBucketObjectResponse.

        数据列表

        :param objects: The objects of this ListObsBucketObjectResponse.
        :type objects: list[:class:`huaweicloudsdkeihealth.v1.BucketObjectDto`]
        """
        self._objects = objects

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
        if not isinstance(other, ListObsBucketObjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
