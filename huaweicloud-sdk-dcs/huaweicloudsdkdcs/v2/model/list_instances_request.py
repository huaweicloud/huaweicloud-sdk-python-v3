# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'include_failure': 'str',
        'include_delete': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'name_equal': 'str',
        'tags': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'include_failure': 'include_failure',
        'include_delete': 'include_delete',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'name_equal': 'name_equal',
        'tags': 'tags',
        'ip': 'ip'
    }

    def __init__(self, instance_id=None, include_failure=None, include_delete=None, name=None, offset=None, limit=None, status=None, name_equal=None, tags=None, ip=None):
        """ListInstancesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param include_failure: 是否返回创建失败的实例数。 当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。
        :type include_failure: str
        :param include_delete: 是否返回已删除的实例数。 当参数值为“true”时，返回已删除的实例数。参数值为“false”或者其他值，不返回已删除的实例数。
        :type include_delete: str
        :param name: 实例名称。
        :type name: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。
        :type limit: int
        :param status: 实例状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)
        :type status: str
        :param name_equal: 是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。
        :type name_equal: str
        :param tags: 根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。 
        :type tags: str
        :param ip: 连接缓存实例的IP地址。
        :type ip: str
        """
        
        

        self._instance_id = None
        self._include_failure = None
        self._include_delete = None
        self._name = None
        self._offset = None
        self._limit = None
        self._status = None
        self._name_equal = None
        self._tags = None
        self._ip = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if include_failure is not None:
            self.include_failure = include_failure
        if include_delete is not None:
            self.include_delete = include_delete
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if name_equal is not None:
            self.name_equal = name_equal
        if tags is not None:
            self.tags = tags
        if ip is not None:
            self.ip = ip

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInstancesRequest.

        实例ID。

        :return: The instance_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInstancesRequest.

        实例ID。

        :param instance_id: The instance_id of this ListInstancesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def include_failure(self):
        """Gets the include_failure of this ListInstancesRequest.

        是否返回创建失败的实例数。 当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :return: The include_failure of this ListInstancesRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListInstancesRequest.

        是否返回创建失败的实例数。 当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :param include_failure: The include_failure of this ListInstancesRequest.
        :type include_failure: str
        """
        self._include_failure = include_failure

    @property
    def include_delete(self):
        """Gets the include_delete of this ListInstancesRequest.

        是否返回已删除的实例数。 当参数值为“true”时，返回已删除的实例数。参数值为“false”或者其他值，不返回已删除的实例数。

        :return: The include_delete of this ListInstancesRequest.
        :rtype: str
        """
        return self._include_delete

    @include_delete.setter
    def include_delete(self, include_delete):
        """Sets the include_delete of this ListInstancesRequest.

        是否返回已删除的实例数。 当参数值为“true”时，返回已删除的实例数。参数值为“false”或者其他值，不返回已删除的实例数。

        :param include_delete: The include_delete of this ListInstancesRequest.
        :type include_delete: str
        """
        self._include_delete = include_delete

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.

        实例名称。

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.

        实例名称。

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListInstancesRequest.

        实例状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :return: The status of this ListInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesRequest.

        实例状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :param status: The status of this ListInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def name_equal(self):
        """Gets the name_equal of this ListInstancesRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :return: The name_equal of this ListInstancesRequest.
        :rtype: str
        """
        return self._name_equal

    @name_equal.setter
    def name_equal(self, name_equal):
        """Sets the name_equal of this ListInstancesRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :param name_equal: The name_equal of this ListInstancesRequest.
        :type name_equal: str
        """
        self._name_equal = name_equal

    @property
    def tags(self):
        """Gets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。 

        :return: The tags of this ListInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。 

        :param tags: The tags of this ListInstancesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def ip(self):
        """Gets the ip of this ListInstancesRequest.

        连接缓存实例的IP地址。

        :return: The ip of this ListInstancesRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListInstancesRequest.

        连接缓存实例的IP地址。

        :param ip: The ip of this ListInstancesRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
