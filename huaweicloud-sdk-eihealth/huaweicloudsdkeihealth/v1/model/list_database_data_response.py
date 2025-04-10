# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseDataResponse(SdkResponse):

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
        'objects': 'list[dict(str, str)]'
    }

    attribute_map = {
        'count': 'count',
        'objects': 'objects'
    }

    def __init__(self, count=None, objects=None):
        r"""ListDatabaseDataResponse

        The model defined in huaweicloud sdk

        :param count: 总条数
        :type count: int
        :param objects: 查询记录列表
        :type objects: list[dict(str, str)]
        """
        
        super(ListDatabaseDataResponse, self).__init__()

        self._count = None
        self._objects = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if objects is not None:
            self.objects = objects

    @property
    def count(self):
        r"""Gets the count of this ListDatabaseDataResponse.

        总条数

        :return: The count of this ListDatabaseDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDatabaseDataResponse.

        总条数

        :param count: The count of this ListDatabaseDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def objects(self):
        r"""Gets the objects of this ListDatabaseDataResponse.

        查询记录列表

        :return: The objects of this ListDatabaseDataResponse.
        :rtype: list[dict(str, str)]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this ListDatabaseDataResponse.

        查询记录列表

        :param objects: The objects of this ListDatabaseDataResponse.
        :type objects: list[dict(str, str)]
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
        if not isinstance(other, ListDatabaseDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
