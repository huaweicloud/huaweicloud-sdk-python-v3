# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'flavor': 'str',
        'ip': 'str',
        'limit': 'int',
        'name': 'str',
        'not_tags': 'str',
        'offset': 'int',
        'reservation_id': 'str',
        'status': 'str',
        'tags': 'str',
        'ip_eq': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'flavor': 'flavor',
        'ip': 'ip',
        'limit': 'limit',
        'name': 'name',
        'not_tags': 'not-tags',
        'offset': 'offset',
        'reservation_id': 'reservation_id',
        'status': 'status',
        'tags': 'tags',
        'ip_eq': 'ip_eq',
        'server_id': 'server_id'
    }

    def __init__(self, enterprise_project_id=None, flavor=None, ip=None, limit=None, name=None, not_tags=None, offset=None, reservation_id=None, status=None, tags=None, ip_eq=None, server_id=None):
        """ListServersDetailsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 查询绑定某个企业项目的弹性云服务器。  若需要查询当前用户所有企业项目绑定的弹性云服务，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param flavor: 云服务器规格ID,已上线的规格请参见《弹性云服务器用户指南》的“实例和应用场景”章节。
        :type flavor: str
        :param ip: IPv4地址过滤结果，匹配规则为模糊匹配。
        :type ip: str
        :param limit: 查询返回云服务器当前页面的大小。每页默认值是25，最多返回1000台云服务器的信息。
        :type limit: int
        :param name: 云服务器名称，匹配规则为模糊匹配。
        :type name: str
        :param not_tags: 查询tag字段中不包含该值的云服务器。
        :type not_tags: str
        :param offset: 页码。 当前页面数，默认为1，取值范围大于等于0。 当取值为0时，系统默认返回第1页，与取值为1时相同。 建议设置该参数大于等于1。
        :type offset: int
        :param reservation_id: 批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。
        :type reservation_id: str
        :param status: 云服务器状态。  取值范围：  ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  只有管理员可以使用“deleted”状态过滤查询已经删除的弹性云服务器。  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)
        :type status: str
        :param tags: 查询tag字段中包含该值的云服务器。
        :type tags: str
        :param ip_eq: IPv4地址过滤结果，匹配规则为精确匹配。
        :type ip_eq: str
        :param server_id: 云服务器ID，格式为UUID，匹配规则为精确匹配  示例: server_id&#x3D;{id1},{id2}  说明： 在使用server_id作为过滤条件时，不能同时使用其他过滤条件。如果同时指定server_id及其他过滤条件，则以server_id条件为准，其他过滤条件会被忽略 当server_id中含有不存在的云服务器ID时，返回的响应参数中该云服务器ID对应的servers结构体中除了id和fault其它字段均为null 为了避免API的URI过长，建议一次查询的server_id个数不超过100个
        :type server_id: str
        """
        
        

        self._enterprise_project_id = None
        self._flavor = None
        self._ip = None
        self._limit = None
        self._name = None
        self._not_tags = None
        self._offset = None
        self._reservation_id = None
        self._status = None
        self._tags = None
        self._ip_eq = None
        self._server_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if flavor is not None:
            self.flavor = flavor
        if ip is not None:
            self.ip = ip
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if not_tags is not None:
            self.not_tags = not_tags
        if offset is not None:
            self.offset = offset
        if reservation_id is not None:
            self.reservation_id = reservation_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if ip_eq is not None:
            self.ip_eq = ip_eq
        if server_id is not None:
            self.server_id = server_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListServersDetailsRequest.

        查询绑定某个企业项目的弹性云服务器。  若需要查询当前用户所有企业项目绑定的弹性云服务，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListServersDetailsRequest.

        查询绑定某个企业项目的弹性云服务器。  若需要查询当前用户所有企业项目绑定的弹性云服务，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListServersDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor(self):
        """Gets the flavor of this ListServersDetailsRequest.

        云服务器规格ID,已上线的规格请参见《弹性云服务器用户指南》的“实例和应用场景”章节。

        :return: The flavor of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ListServersDetailsRequest.

        云服务器规格ID,已上线的规格请参见《弹性云服务器用户指南》的“实例和应用场景”章节。

        :param flavor: The flavor of this ListServersDetailsRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def ip(self):
        """Gets the ip of this ListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为模糊匹配。

        :return: The ip of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为模糊匹配。

        :param ip: The ip of this ListServersDetailsRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def limit(self):
        """Gets the limit of this ListServersDetailsRequest.

        查询返回云服务器当前页面的大小。每页默认值是25，最多返回1000台云服务器的信息。

        :return: The limit of this ListServersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServersDetailsRequest.

        查询返回云服务器当前页面的大小。每页默认值是25，最多返回1000台云服务器的信息。

        :param limit: The limit of this ListServersDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListServersDetailsRequest.

        云服务器名称，匹配规则为模糊匹配。

        :return: The name of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListServersDetailsRequest.

        云服务器名称，匹配规则为模糊匹配。

        :param name: The name of this ListServersDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def not_tags(self):
        """Gets the not_tags of this ListServersDetailsRequest.

        查询tag字段中不包含该值的云服务器。

        :return: The not_tags of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListServersDetailsRequest.

        查询tag字段中不包含该值的云服务器。

        :param not_tags: The not_tags of this ListServersDetailsRequest.
        :type not_tags: str
        """
        self._not_tags = not_tags

    @property
    def offset(self):
        """Gets the offset of this ListServersDetailsRequest.

        页码。 当前页面数，默认为1，取值范围大于等于0。 当取值为0时，系统默认返回第1页，与取值为1时相同。 建议设置该参数大于等于1。

        :return: The offset of this ListServersDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServersDetailsRequest.

        页码。 当前页面数，默认为1，取值范围大于等于0。 当取值为0时，系统默认返回第1页，与取值为1时相同。 建议设置该参数大于等于1。

        :param offset: The offset of this ListServersDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def reservation_id(self):
        """Gets the reservation_id of this ListServersDetailsRequest.

        批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。

        :return: The reservation_id of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this ListServersDetailsRequest.

        批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。

        :param reservation_id: The reservation_id of this ListServersDetailsRequest.
        :type reservation_id: str
        """
        self._reservation_id = reservation_id

    @property
    def status(self):
        """Gets the status of this ListServersDetailsRequest.

        云服务器状态。  取值范围：  ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  只有管理员可以使用“deleted”状态过滤查询已经删除的弹性云服务器。  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :return: The status of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListServersDetailsRequest.

        云服务器状态。  取值范围：  ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  只有管理员可以使用“deleted”状态过滤查询已经删除的弹性云服务器。  弹性云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)

        :param status: The status of this ListServersDetailsRequest.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ListServersDetailsRequest.

        查询tag字段中包含该值的云服务器。

        :return: The tags of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListServersDetailsRequest.

        查询tag字段中包含该值的云服务器。

        :param tags: The tags of this ListServersDetailsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def ip_eq(self):
        """Gets the ip_eq of this ListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为精确匹配。

        :return: The ip_eq of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._ip_eq

    @ip_eq.setter
    def ip_eq(self, ip_eq):
        """Sets the ip_eq of this ListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为精确匹配。

        :param ip_eq: The ip_eq of this ListServersDetailsRequest.
        :type ip_eq: str
        """
        self._ip_eq = ip_eq

    @property
    def server_id(self):
        """Gets the server_id of this ListServersDetailsRequest.

        云服务器ID，格式为UUID，匹配规则为精确匹配  示例: server_id={id1},{id2}  说明： 在使用server_id作为过滤条件时，不能同时使用其他过滤条件。如果同时指定server_id及其他过滤条件，则以server_id条件为准，其他过滤条件会被忽略 当server_id中含有不存在的云服务器ID时，返回的响应参数中该云服务器ID对应的servers结构体中除了id和fault其它字段均为null 为了避免API的URI过长，建议一次查询的server_id个数不超过100个

        :return: The server_id of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListServersDetailsRequest.

        云服务器ID，格式为UUID，匹配规则为精确匹配  示例: server_id={id1},{id2}  说明： 在使用server_id作为过滤条件时，不能同时使用其他过滤条件。如果同时指定server_id及其他过滤条件，则以server_id条件为准，其他过滤条件会被忽略 当server_id中含有不存在的云服务器ID时，返回的响应参数中该云服务器ID对应的servers结构体中除了id和fault其它字段均为null 为了避免API的URI过长，建议一次查询的server_id个数不超过100个

        :param server_id: The server_id of this ListServersDetailsRequest.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ListServersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
