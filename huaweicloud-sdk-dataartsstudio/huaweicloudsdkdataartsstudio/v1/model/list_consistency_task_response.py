# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConsistencyTaskResponse(SdkResponse):

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
        'resources': 'list[QualityTaskOverviewVO2]'
    }

    attribute_map = {
        'count': 'count',
        'resources': 'resources'
    }

    def __init__(self, count=None, resources=None):
        r"""ListConsistencyTaskResponse

        The model defined in huaweicloud sdk

        :param count: 总条数
        :type count: int
        :param resources: 分页数据
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskOverviewVO2`]
        """
        
        super(ListConsistencyTaskResponse, self).__init__()

        self._count = None
        self._resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if resources is not None:
            self.resources = resources

    @property
    def count(self):
        r"""Gets the count of this ListConsistencyTaskResponse.

        总条数

        :return: The count of this ListConsistencyTaskResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListConsistencyTaskResponse.

        总条数

        :param count: The count of this ListConsistencyTaskResponse.
        :type count: int
        """
        self._count = count

    @property
    def resources(self):
        r"""Gets the resources of this ListConsistencyTaskResponse.

        分页数据

        :return: The resources of this ListConsistencyTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskOverviewVO2`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListConsistencyTaskResponse.

        分页数据

        :param resources: The resources of this ListConsistencyTaskResponse.
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.QualityTaskOverviewVO2`]
        """
        self._resources = resources

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
        if not isinstance(other, ListConsistencyTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
