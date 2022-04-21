# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaListServersDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'changes_since': 'str',
        'flavor': 'str',
        'image': 'str',
        'ip': 'str',
        'limit': 'int',
        'marker': 'str',
        'name': 'str',
        'not_tags': 'str',
        'reservation_id': 'str',
        'sort_key': 'str',
        'status': 'str',
        'tags': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'changes_since': 'changes-since',
        'flavor': 'flavor',
        'image': 'image',
        'ip': 'ip',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'not_tags': 'not-tags',
        'reservation_id': 'reservation_id',
        'sort_key': 'sort_key',
        'status': 'status',
        'tags': 'tags',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, changes_since=None, flavor=None, image=None, ip=None, limit=None, marker=None, name=None, not_tags=None, reservation_id=None, sort_key=None, status=None, tags=None, open_stack_api_version=None):
        """NovaListServersDetailsRequest

        The model defined in huaweicloud sdk

        :param changes_since: 云服务器上次更新状态的时间戳信息。时间戳为UTC格式。
        :type changes_since: str
        :param flavor: 云服务器规格ID。
        :type flavor: str
        :param image: 镜像ID  在使用image作为条件过滤时，不能同时支持其他过滤条件和分页条件。如果同时指定image及其他条件，则以image条件为准；当条件不含image时，接口功能不受限制。
        :type image: str
        :param ip: IPv4地址过滤结果，匹配规则为模糊匹配。
        :type ip: str
        :param limit: 查询返回云服务器数量限制。
        :type limit: int
        :param marker: 从marker指定的云服务器ID的下一条数据开始查询。
        :type marker: str
        :param name: 云服务器名称。
        :type name: str
        :param not_tags: 查询tag字段中不包含该值的云服务器，值为标签的Key。  &gt; 说明： &gt;  &gt; 系统近期对标签功能进行了升级。如果之前添加的Tag为“Key.Value”的形式，则查询的时候需要使用“Key”来查询。 &gt;  &gt; 例如：之前添加的tag为“a.b”,则升级后，查询时需使用“not-tags&#x3D;a”。
        :type not_tags: str
        :param reservation_id: 批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。
        :type reservation_id: str
        :param sort_key: 查询结果按弹性云服务器属性排序，默认排序顺序为created_at逆序。
        :type sort_key: str
        :param status: 云服务器状态。  取值范围： ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  直到2.37微版本，非上面范围的status字段将返回空列表，2.38之后的微版本，将返回400错误。  云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)。
        :type status: str
        :param tags: 查询tag字段中包含该值的云服务器。
        :type tags: str
        :param open_stack_api_version: 微版本头
        :type open_stack_api_version: str
        """
        
        

        self._changes_since = None
        self._flavor = None
        self._image = None
        self._ip = None
        self._limit = None
        self._marker = None
        self._name = None
        self._not_tags = None
        self._reservation_id = None
        self._sort_key = None
        self._status = None
        self._tags = None
        self._open_stack_api_version = None
        self.discriminator = None

        if changes_since is not None:
            self.changes_since = changes_since
        if flavor is not None:
            self.flavor = flavor
        if image is not None:
            self.image = image
        if ip is not None:
            self.ip = ip
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if not_tags is not None:
            self.not_tags = not_tags
        if reservation_id is not None:
            self.reservation_id = reservation_id
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def changes_since(self):
        """Gets the changes_since of this NovaListServersDetailsRequest.

        云服务器上次更新状态的时间戳信息。时间戳为UTC格式。

        :return: The changes_since of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._changes_since

    @changes_since.setter
    def changes_since(self, changes_since):
        """Sets the changes_since of this NovaListServersDetailsRequest.

        云服务器上次更新状态的时间戳信息。时间戳为UTC格式。

        :param changes_since: The changes_since of this NovaListServersDetailsRequest.
        :type changes_since: str
        """
        self._changes_since = changes_since

    @property
    def flavor(self):
        """Gets the flavor of this NovaListServersDetailsRequest.

        云服务器规格ID。

        :return: The flavor of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this NovaListServersDetailsRequest.

        云服务器规格ID。

        :param flavor: The flavor of this NovaListServersDetailsRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def image(self):
        """Gets the image of this NovaListServersDetailsRequest.

        镜像ID  在使用image作为条件过滤时，不能同时支持其他过滤条件和分页条件。如果同时指定image及其他条件，则以image条件为准；当条件不含image时，接口功能不受限制。

        :return: The image of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NovaListServersDetailsRequest.

        镜像ID  在使用image作为条件过滤时，不能同时支持其他过滤条件和分页条件。如果同时指定image及其他条件，则以image条件为准；当条件不含image时，接口功能不受限制。

        :param image: The image of this NovaListServersDetailsRequest.
        :type image: str
        """
        self._image = image

    @property
    def ip(self):
        """Gets the ip of this NovaListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为模糊匹配。

        :return: The ip of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NovaListServersDetailsRequest.

        IPv4地址过滤结果，匹配规则为模糊匹配。

        :param ip: The ip of this NovaListServersDetailsRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def limit(self):
        """Gets the limit of this NovaListServersDetailsRequest.

        查询返回云服务器数量限制。

        :return: The limit of this NovaListServersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListServersDetailsRequest.

        查询返回云服务器数量限制。

        :param limit: The limit of this NovaListServersDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListServersDetailsRequest.

        从marker指定的云服务器ID的下一条数据开始查询。

        :return: The marker of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListServersDetailsRequest.

        从marker指定的云服务器ID的下一条数据开始查询。

        :param marker: The marker of this NovaListServersDetailsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this NovaListServersDetailsRequest.

        云服务器名称。

        :return: The name of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaListServersDetailsRequest.

        云服务器名称。

        :param name: The name of this NovaListServersDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def not_tags(self):
        """Gets the not_tags of this NovaListServersDetailsRequest.

        查询tag字段中不包含该值的云服务器，值为标签的Key。  > 说明： >  > 系统近期对标签功能进行了升级。如果之前添加的Tag为“Key.Value”的形式，则查询的时候需要使用“Key”来查询。 >  > 例如：之前添加的tag为“a.b”,则升级后，查询时需使用“not-tags=a”。

        :return: The not_tags of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this NovaListServersDetailsRequest.

        查询tag字段中不包含该值的云服务器，值为标签的Key。  > 说明： >  > 系统近期对标签功能进行了升级。如果之前添加的Tag为“Key.Value”的形式，则查询的时候需要使用“Key”来查询。 >  > 例如：之前添加的tag为“a.b”,则升级后，查询时需使用“not-tags=a”。

        :param not_tags: The not_tags of this NovaListServersDetailsRequest.
        :type not_tags: str
        """
        self._not_tags = not_tags

    @property
    def reservation_id(self):
        """Gets the reservation_id of this NovaListServersDetailsRequest.

        批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。

        :return: The reservation_id of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this NovaListServersDetailsRequest.

        批量创建弹性云服务器时，指定返回的ID，用于查询本次批量创建的弹性云服务器。

        :param reservation_id: The reservation_id of this NovaListServersDetailsRequest.
        :type reservation_id: str
        """
        self._reservation_id = reservation_id

    @property
    def sort_key(self):
        """Gets the sort_key of this NovaListServersDetailsRequest.

        查询结果按弹性云服务器属性排序，默认排序顺序为created_at逆序。

        :return: The sort_key of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this NovaListServersDetailsRequest.

        查询结果按弹性云服务器属性排序，默认排序顺序为created_at逆序。

        :param sort_key: The sort_key of this NovaListServersDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this NovaListServersDetailsRequest.

        云服务器状态。  取值范围： ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  直到2.37微版本，非上面范围的status字段将返回空列表，2.38之后的微版本，将返回400错误。  云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)。

        :return: The status of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaListServersDetailsRequest.

        云服务器状态。  取值范围： ACTIVE， BUILD，DELETED，ERROR，HARD_REBOOT，MIGRATING，REBOOT，RESIZE，REVERT_RESIZE，SHELVED，SHELVED_OFFLOADED，SHUTOFF，UNKNOWN，VERIFY_RESIZE  直到2.37微版本，非上面范围的status字段将返回空列表，2.38之后的微版本，将返回400错误。  云服务器状态说明请参考[云服务器状态](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)。

        :param status: The status of this NovaListServersDetailsRequest.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this NovaListServersDetailsRequest.

        查询tag字段中包含该值的云服务器。

        :return: The tags of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NovaListServersDetailsRequest.

        查询tag字段中包含该值的云服务器。

        :param tags: The tags of this NovaListServersDetailsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaListServersDetailsRequest.

        微版本头

        :return: The open_stack_api_version of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaListServersDetailsRequest.

        微版本头

        :param open_stack_api_version: The open_stack_api_version of this NovaListServersDetailsRequest.
        :type open_stack_api_version: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaListServersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
