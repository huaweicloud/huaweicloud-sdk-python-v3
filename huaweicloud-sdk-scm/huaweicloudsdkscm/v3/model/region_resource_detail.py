# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'is_error': 'bool',
        'resources': 'list[ResourceDetail]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'is_error': 'is_error',
        'resources': 'resources'
    }

    def __init__(self, region_id=None, is_error=None, resources=None):
        r"""RegionResourceDetail

        The model defined in huaweicloud sdk

        :param region_id: 局点ID。当服务为全局服务时，region_id为global，其余按照IAM的标准命名。
        :type region_id: str
        :param is_error: 请求当前region资源信息过程中，响应是否存在异常的标志。 - true : 存在异常，当前region所统计数据不准确 - false: 无异常，当前region所统计数据准确 
        :type is_error: bool
        :param resources: 资源集合，每个资源的标识：资源ID + “:” + 资源名称，详情请参见ResourceDetail字段数据结构说明。
        :type resources: list[:class:`huaweicloudsdkscm.v3.ResourceDetail`]
        """
        
        

        self._region_id = None
        self._is_error = None
        self._resources = None
        self.discriminator = None

        self.region_id = region_id
        self.is_error = is_error
        self.resources = resources

    @property
    def region_id(self):
        r"""Gets the region_id of this RegionResourceDetail.

        局点ID。当服务为全局服务时，region_id为global，其余按照IAM的标准命名。

        :return: The region_id of this RegionResourceDetail.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this RegionResourceDetail.

        局点ID。当服务为全局服务时，region_id为global，其余按照IAM的标准命名。

        :param region_id: The region_id of this RegionResourceDetail.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def is_error(self):
        r"""Gets the is_error of this RegionResourceDetail.

        请求当前region资源信息过程中，响应是否存在异常的标志。 - true : 存在异常，当前region所统计数据不准确 - false: 无异常，当前region所统计数据准确 

        :return: The is_error of this RegionResourceDetail.
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        r"""Sets the is_error of this RegionResourceDetail.

        请求当前region资源信息过程中，响应是否存在异常的标志。 - true : 存在异常，当前region所统计数据不准确 - false: 无异常，当前region所统计数据准确 

        :param is_error: The is_error of this RegionResourceDetail.
        :type is_error: bool
        """
        self._is_error = is_error

    @property
    def resources(self):
        r"""Gets the resources of this RegionResourceDetail.

        资源集合，每个资源的标识：资源ID + “:” + 资源名称，详情请参见ResourceDetail字段数据结构说明。

        :return: The resources of this RegionResourceDetail.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ResourceDetail`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this RegionResourceDetail.

        资源集合，每个资源的标识：资源ID + “:” + 资源名称，详情请参见ResourceDetail字段数据结构说明。

        :param resources: The resources of this RegionResourceDetail.
        :type resources: list[:class:`huaweicloudsdkscm.v3.ResourceDetail`]
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
        if not isinstance(other, RegionResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
