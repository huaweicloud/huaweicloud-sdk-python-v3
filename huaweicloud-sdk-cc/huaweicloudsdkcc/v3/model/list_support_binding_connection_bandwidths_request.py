# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportBindingConnectionBandwidthsRequest:

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
        'enterprise_project_id': 'list[str]',
        'local_area': 'str',
        'remote_area': 'str',
        'binding_service': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'enterprise_project_id': 'enterprise_project_id',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'binding_service': 'binding_service'
    }

    def __init__(self, limit=None, marker=None, enterprise_project_id=None, local_area=None, remote_area=None, binding_service=None):
        """ListSupportBindingConnectionBandwidthsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param enterprise_project_id: 根据企业项目ID过滤列表。
        :type enterprise_project_id: list[str]
        :param local_area: 功能说明：本端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的local_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致
        :type local_area: str
        :param remote_area: 功能说明：远端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的remote_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致
        :type remote_area: str
        :param binding_service: 根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络
        :type binding_service: str
        """
        
        

        self._limit = None
        self._marker = None
        self._enterprise_project_id = None
        self._local_area = None
        self._remote_area = None
        self._binding_service = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        self.binding_service = binding_service

    @property
    def limit(self):
        """Gets the limit of this ListSupportBindingConnectionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSupportBindingConnectionBandwidthsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListSupportBindingConnectionBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSupportBindingConnectionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSupportBindingConnectionBandwidthsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListSupportBindingConnectionBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSupportBindingConnectionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :return: The enterprise_project_id of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSupportBindingConnectionBandwidthsRequest.

        根据企业项目ID过滤列表。

        :param enterprise_project_id: The enterprise_project_id of this ListSupportBindingConnectionBandwidthsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def local_area(self):
        """Gets the local_area of this ListSupportBindingConnectionBandwidthsRequest.

        功能说明：本端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的local_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致

        :return: The local_area of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        """Sets the local_area of this ListSupportBindingConnectionBandwidthsRequest.

        功能说明：本端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的local_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致

        :param local_area: The local_area of this ListSupportBindingConnectionBandwidthsRequest.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        """Gets the remote_area of this ListSupportBindingConnectionBandwidthsRequest.

        功能说明：远端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的remote_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致

        :return: The remote_area of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        """Sets the remote_area of this ListSupportBindingConnectionBandwidthsRequest.

        功能说明：远端接入点。   如果是region类型，则返回所有满足条件的城域带宽，不进行该字段的匹配过滤   如果是其他类型，则会用该字段跟全域互联带宽的remote_area进行匹配过滤   附带过滤条件：会通过local_area和remote_area推算最佳全域互联带宽类型进行过滤查询   限制：local_area和remote_area同为空或者同不为空，且站点类型需一致

        :param remote_area: The remote_area of this ListSupportBindingConnectionBandwidthsRequest.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def binding_service(self):
        """Gets the binding_service of this ListSupportBindingConnectionBandwidthsRequest.

        根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络

        :return: The binding_service of this ListSupportBindingConnectionBandwidthsRequest.
        :rtype: str
        """
        return self._binding_service

    @binding_service.setter
    def binding_service(self, binding_service):
        """Sets the binding_service of this ListSupportBindingConnectionBandwidthsRequest.

        根据支持绑定实例类型过滤全域互联带宽列表。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络

        :param binding_service: The binding_service of this ListSupportBindingConnectionBandwidthsRequest.
        :type binding_service: str
        """
        self._binding_service = binding_service

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
        if not isinstance(other, ListSupportBindingConnectionBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
