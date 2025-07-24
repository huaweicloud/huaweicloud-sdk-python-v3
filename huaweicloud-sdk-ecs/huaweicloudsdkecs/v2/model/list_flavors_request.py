# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'flavor_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'flavor_id': 'flavor_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, availability_zone=None, flavor_id=None, limit=None, marker=None):
        r"""ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param availability_zone: 可用区，需要指定可用区（AZ）的名称或者ID或者code。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;ECS&amp;api&#x3D;NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type availability_zone: str
        :param flavor_id: 规格id
        :type flavor_id: str
        :param limit: 查询返回云服务器规格列表当前页面的数量。默认为1000
        :type limit: int
        :param marker: 从marker指定的flavor_id的下一条数据开始查询
        :type marker: str
        """
        
        

        self._availability_zone = None
        self._flavor_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListFlavorsRequest.

        可用区，需要指定可用区（AZ）的名称或者ID或者code。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The availability_zone of this ListFlavorsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListFlavorsRequest.

        可用区，需要指定可用区（AZ）的名称或者ID或者code。  可通过接口 [查询可用区列表接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=ECS&api=NovaListAvailabilityZones) 获取，也可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param availability_zone: The availability_zone of this ListFlavorsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListFlavorsRequest.

        规格id

        :return: The flavor_id of this ListFlavorsRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListFlavorsRequest.

        规格id

        :param flavor_id: The flavor_id of this ListFlavorsRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def limit(self):
        r"""Gets the limit of this ListFlavorsRequest.

        查询返回云服务器规格列表当前页面的数量。默认为1000

        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlavorsRequest.

        查询返回云服务器规格列表当前页面的数量。默认为1000

        :param limit: The limit of this ListFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListFlavorsRequest.

        从marker指定的flavor_id的下一条数据开始查询

        :return: The marker of this ListFlavorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFlavorsRequest.

        从marker指定的flavor_id的下一条数据开始查询

        :param marker: The marker of this ListFlavorsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
