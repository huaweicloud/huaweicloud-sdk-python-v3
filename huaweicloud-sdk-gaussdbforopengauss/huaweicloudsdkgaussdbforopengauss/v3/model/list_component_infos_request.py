# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComponentInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'component_type': 'str',
        'availability_zone_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'component_type': 'component_type',
        'availability_zone_id': 'availability_zone_id'
    }

    def __init__(self, x_language=None, instance_id=None, offset=None, limit=None, component_type=None, availability_zone_id=None):
        """ListComponentInfosRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100
        :type limit: int
        :param component_type: 组件类型，过滤拿到需要的组件类型的组件信息，默认为ALL，传参数会查询对应组件信息。 枚举值：   \&quot;ALL\&quot;: 查询所有组件类型。   \&quot;CN\&quot;: 查询CN组件类型。   \&quot;DN\&quot;: 查询DN组件类型。   \&quot;CM\&quot;: 查询CMS组件类型。   \&quot;GTM\&quot;: 查询GTM组件类型。   \&quot;ETCD\&quot;: 查询ETCD组件类型。
        :type component_type: str
        :param availability_zone_id: 主组件所在可用区编号，筛选符合条件的组件，默认为ALL，查询实例所有可用区上的节点的组件信息。 当调用接口传入可用区编号时：   相对于DN组件，会查询出的DN分片中的主组件在该可用区上的这个分片的所有副本的组件信息。   相对于CN组件，CN组件没有主备关系，会查询出该可用区上的CN组件信息。   相对于其他组件，会查询该可用区上有没有某个组件类型的主组件，有则会返回该组件类型的所有组件信息，没有则不返回该组件类型的信息。
        :type availability_zone_id: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._offset = None
        self._limit = None
        self._component_type = None
        self._availability_zone_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if component_type is not None:
            self.component_type = component_type
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id

    @property
    def x_language(self):
        """Gets the x_language of this ListComponentInfosRequest.

        语言

        :return: The x_language of this ListComponentInfosRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListComponentInfosRequest.

        语言

        :param x_language: The x_language of this ListComponentInfosRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListComponentInfosRequest.

        实例ID。

        :return: The instance_id of this ListComponentInfosRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListComponentInfosRequest.

        实例ID。

        :param instance_id: The instance_id of this ListComponentInfosRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListComponentInfosRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListComponentInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListComponentInfosRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListComponentInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListComponentInfosRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100

        :return: The limit of this ListComponentInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListComponentInfosRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100

        :param limit: The limit of this ListComponentInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def component_type(self):
        """Gets the component_type of this ListComponentInfosRequest.

        组件类型，过滤拿到需要的组件类型的组件信息，默认为ALL，传参数会查询对应组件信息。 枚举值：   \"ALL\": 查询所有组件类型。   \"CN\": 查询CN组件类型。   \"DN\": 查询DN组件类型。   \"CM\": 查询CMS组件类型。   \"GTM\": 查询GTM组件类型。   \"ETCD\": 查询ETCD组件类型。

        :return: The component_type of this ListComponentInfosRequest.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this ListComponentInfosRequest.

        组件类型，过滤拿到需要的组件类型的组件信息，默认为ALL，传参数会查询对应组件信息。 枚举值：   \"ALL\": 查询所有组件类型。   \"CN\": 查询CN组件类型。   \"DN\": 查询DN组件类型。   \"CM\": 查询CMS组件类型。   \"GTM\": 查询GTM组件类型。   \"ETCD\": 查询ETCD组件类型。

        :param component_type: The component_type of this ListComponentInfosRequest.
        :type component_type: str
        """
        self._component_type = component_type

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this ListComponentInfosRequest.

        主组件所在可用区编号，筛选符合条件的组件，默认为ALL，查询实例所有可用区上的节点的组件信息。 当调用接口传入可用区编号时：   相对于DN组件，会查询出的DN分片中的主组件在该可用区上的这个分片的所有副本的组件信息。   相对于CN组件，CN组件没有主备关系，会查询出该可用区上的CN组件信息。   相对于其他组件，会查询该可用区上有没有某个组件类型的主组件，有则会返回该组件类型的所有组件信息，没有则不返回该组件类型的信息。

        :return: The availability_zone_id of this ListComponentInfosRequest.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this ListComponentInfosRequest.

        主组件所在可用区编号，筛选符合条件的组件，默认为ALL，查询实例所有可用区上的节点的组件信息。 当调用接口传入可用区编号时：   相对于DN组件，会查询出的DN分片中的主组件在该可用区上的这个分片的所有副本的组件信息。   相对于CN组件，CN组件没有主备关系，会查询出该可用区上的CN组件信息。   相对于其他组件，会查询该可用区上有没有某个组件类型的主组件，有则会返回该组件类型的所有组件信息，没有则不返回该组件类型的信息。

        :param availability_zone_id: The availability_zone_id of this ListComponentInfosRequest.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

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
        if not isinstance(other, ListComponentInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
