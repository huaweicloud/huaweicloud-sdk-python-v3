# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'name': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'binding_service': 'list[str]',
        'type': 'list[str]',
        'charge_mode': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'binding_service': 'binding_service',
        'type': 'type',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, enterprise_project_id=None, binding_service=None, type=None, charge_mode=None):
        """ListGlobalConnectionBandwidthsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param id: 根据id查询，可查询多个id。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤列表。
        :type enterprise_project_id: list[str]
        :param binding_service: 根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络
        :type binding_service: list[str]
        :param type: 根据带宽类型过滤全域互联带宽列表。带宽类型： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽
        :type type: list[str]
        :param charge_mode: 根据计费方式过滤全域互联带宽列表： - bwd: 按带宽计费 - 95: 按传统型95计费
        :type charge_mode: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._enterprise_project_id = None
        self._binding_service = None
        self._type = None
        self._charge_mode = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if binding_service is not None:
            self.binding_service = binding_service
        if type is not None:
            self.type = type
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def limit(self):
        """Gets the limit of this ListGlobalConnectionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListGlobalConnectionBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGlobalConnectionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListGlobalConnectionBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListGlobalConnectionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListGlobalConnectionBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListGlobalConnectionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListGlobalConnectionBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListGlobalConnectionBandwidthsRequest.

        根据id查询，可查询多个id。

        :return: The id of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGlobalConnectionBandwidthsRequest.

        根据id查询，可查询多个id。

        :param id: The id of this ListGlobalConnectionBandwidthsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListGlobalConnectionBandwidthsRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGlobalConnectionBandwidthsRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListGlobalConnectionBandwidthsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListGlobalConnectionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :return: The enterprise_project_id of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListGlobalConnectionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :param enterprise_project_id: The enterprise_project_id of this ListGlobalConnectionBandwidthsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def binding_service(self):
        """Gets the binding_service of this ListGlobalConnectionBandwidthsRequest.

        根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络

        :return: The binding_service of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._binding_service

    @binding_service.setter
    def binding_service(self, binding_service):
        """Sets the binding_service of this ListGlobalConnectionBandwidthsRequest.

        根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络

        :param binding_service: The binding_service of this ListGlobalConnectionBandwidthsRequest.
        :type binding_service: list[str]
        """
        self._binding_service = binding_service

    @property
    def type(self):
        """Gets the type of this ListGlobalConnectionBandwidthsRequest.

        根据带宽类型过滤全域互联带宽列表。带宽类型： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :return: The type of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListGlobalConnectionBandwidthsRequest.

        根据带宽类型过滤全域互联带宽列表。带宽类型： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :param type: The type of this ListGlobalConnectionBandwidthsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListGlobalConnectionBandwidthsRequest.

        根据计费方式过滤全域互联带宽列表： - bwd: 按带宽计费 - 95: 按传统型95计费

        :return: The charge_mode of this ListGlobalConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListGlobalConnectionBandwidthsRequest.

        根据计费方式过滤全域互联带宽列表： - bwd: 按带宽计费 - 95: 按传统型95计费

        :param charge_mode: The charge_mode of this ListGlobalConnectionBandwidthsRequest.
        :type charge_mode: list[str]
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, ListGlobalConnectionBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
