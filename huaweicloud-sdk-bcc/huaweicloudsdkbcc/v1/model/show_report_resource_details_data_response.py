# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportResourceDetailsDataResponse(SdkResponse):

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
        'next_marker': 'str',
        'resources': 'list[ResourceEntity]'
    }

    attribute_map = {
        'count': 'count',
        'next_marker': 'next_marker',
        'resources': 'resources'
    }

    def __init__(self, count=None, next_marker=None, resources=None):
        r"""ShowReportResourceDetailsDataResponse

        The model defined in huaweicloud sdk

        :param count: 本次分页查询响应的数据条数
        :type count: int
        :param next_marker: 下一次分页查询的游标
        :type next_marker: str
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdkbcc.v1.ResourceEntity`]
        """
        
        super().__init__()

        self._count = None
        self._next_marker = None
        self._resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if next_marker is not None:
            self.next_marker = next_marker
        if resources is not None:
            self.resources = resources

    @property
    def count(self):
        r"""Gets the count of this ShowReportResourceDetailsDataResponse.

        本次分页查询响应的数据条数

        :return: The count of this ShowReportResourceDetailsDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowReportResourceDetailsDataResponse.

        本次分页查询响应的数据条数

        :param count: The count of this ShowReportResourceDetailsDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ShowReportResourceDetailsDataResponse.

        下一次分页查询的游标

        :return: The next_marker of this ShowReportResourceDetailsDataResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ShowReportResourceDetailsDataResponse.

        下一次分页查询的游标

        :param next_marker: The next_marker of this ShowReportResourceDetailsDataResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def resources(self):
        r"""Gets the resources of this ShowReportResourceDetailsDataResponse.

        资源列表

        :return: The resources of this ShowReportResourceDetailsDataResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceEntity`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ShowReportResourceDetailsDataResponse.

        资源列表

        :param resources: The resources of this ShowReportResourceDetailsDataResponse.
        :type resources: list[:class:`huaweicloudsdkbcc.v1.ResourceEntity`]
        """
        self._resources = resources

    def to_dict(self):
        import warnings
        warnings.warn("ShowReportResourceDetailsDataResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReportResourceDetailsDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
