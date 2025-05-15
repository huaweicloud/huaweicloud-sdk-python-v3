# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackagesRequest:

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
        'cloud_connection_id': 'list[str]',
        'status': 'list[str]',
        'billing_mode': 'list[str]',
        'resource_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'cloud_connection_id': 'cloud_connection_id',
        'status': 'status',
        'billing_mode': 'billing_mode',
        'resource_id': 'resource_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, enterprise_project_id=None, cloud_connection_id=None, status=None, billing_mode=None, resource_id=None):
        r"""ListBandwidthPackagesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param id: 根据ID查询，可查询多个ID。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤列表。
        :type enterprise_project_id: list[str]
        :param cloud_connection_id: 根据云连接的ID过滤列表。
        :type cloud_connection_id: list[str]
        :param status: 根据状态过滤带宽包实例列表。ACTIVE：表示状态可用。
        :type status: list[str]
        :param billing_mode: 根据计费方式过滤带宽包实例列表。
        :type billing_mode: list[str]
        :param resource_id: 根据绑定的资源ID过滤带宽包实例列表。
        :type resource_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._enterprise_project_id = None
        self._cloud_connection_id = None
        self._status = None
        self._billing_mode = None
        self._resource_id = None
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
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if status is not None:
            self.status = status
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def limit(self):
        r"""Gets the limit of this ListBandwidthPackagesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListBandwidthPackagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBandwidthPackagesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListBandwidthPackagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListBandwidthPackagesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListBandwidthPackagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListBandwidthPackagesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListBandwidthPackagesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListBandwidthPackagesRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListBandwidthPackagesRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListBandwidthPackagesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListBandwidthPackagesRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListBandwidthPackagesRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListBandwidthPackagesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBandwidthPackagesRequest.

        根据企业项目ID过滤列表。

        :return: The enterprise_project_id of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBandwidthPackagesRequest.

        根据企业项目ID过滤列表。

        :param enterprise_project_id: The enterprise_project_id of this ListBandwidthPackagesRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this ListBandwidthPackagesRequest.

        根据云连接的ID过滤列表。

        :return: The cloud_connection_id of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this ListBandwidthPackagesRequest.

        根据云连接的ID过滤列表。

        :param cloud_connection_id: The cloud_connection_id of this ListBandwidthPackagesRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def status(self):
        r"""Gets the status of this ListBandwidthPackagesRequest.

        根据状态过滤带宽包实例列表。ACTIVE：表示状态可用。

        :return: The status of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListBandwidthPackagesRequest.

        根据状态过滤带宽包实例列表。ACTIVE：表示状态可用。

        :param status: The status of this ListBandwidthPackagesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ListBandwidthPackagesRequest.

        根据计费方式过滤带宽包实例列表。

        :return: The billing_mode of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ListBandwidthPackagesRequest.

        根据计费方式过滤带宽包实例列表。

        :param billing_mode: The billing_mode of this ListBandwidthPackagesRequest.
        :type billing_mode: list[str]
        """
        self._billing_mode = billing_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListBandwidthPackagesRequest.

        根据绑定的资源ID过滤带宽包实例列表。

        :return: The resource_id of this ListBandwidthPackagesRequest.
        :rtype: list[str]
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListBandwidthPackagesRequest.

        根据绑定的资源ID过滤带宽包实例列表。

        :param resource_id: The resource_id of this ListBandwidthPackagesRequest.
        :type resource_id: list[str]
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ListBandwidthPackagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
