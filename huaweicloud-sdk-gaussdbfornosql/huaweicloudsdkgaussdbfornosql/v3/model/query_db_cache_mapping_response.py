# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDBCacheMappingResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'source_instance_id': 'str',
        'source_instance_name': 'str',
        'target_instance_id': 'str',
        'target_instance_name': 'str',
        'status': 'str',
        'created': 'str',
        'updated': 'str',
        'rule_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'source_instance_id': 'source_instance_id',
        'source_instance_name': 'source_instance_name',
        'target_instance_id': 'target_instance_id',
        'target_instance_name': 'target_instance_name',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'rule_count': 'rule_count'
    }

    def __init__(self, id=None, name=None, source_instance_id=None, source_instance_name=None, target_instance_id=None, target_instance_name=None, status=None, created=None, updated=None, rule_count=None):
        r"""QueryDBCacheMappingResponse

        The model defined in huaweicloud sdk

        :param id: 内存加速映射ID。
        :type id: str
        :param name: 内存加速映射名称。
        :type name: str
        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param source_instance_name: 源实例名称。
        :type source_instance_name: str
        :param target_instance_id: 目标实例ID。
        :type target_instance_id: str
        :param target_instance_name: 目标实例名称。
        :type target_instance_name: str
        :param status: 内存加速映射关系。  - normal： 表示内存加速映射正常。  - creating： 表示内存加速映射创建中。  - createfail： 表示内存加速映射创建失败。  - deleting： 表示内存加速映射解除中。  - stopped： 表示内存加速映射停止。  - deleted： 表示内存加速映射已解除。
        :type status: str
        :param created: 内存加速映射创建时间。
        :type created: str
        :param updated: 内存加速映射最新变更的时间。
        :type updated: str
        :param rule_count: 该内存加速映射下的规则数量。
        :type rule_count: int
        """
        
        

        self._id = None
        self._name = None
        self._source_instance_id = None
        self._source_instance_name = None
        self._target_instance_id = None
        self._target_instance_name = None
        self._status = None
        self._created = None
        self._updated = None
        self._rule_count = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.source_instance_id = source_instance_id
        self.source_instance_name = source_instance_name
        self.target_instance_id = target_instance_id
        self.target_instance_name = target_instance_name
        self.status = status
        self.created = created
        self.updated = updated
        if rule_count is not None:
            self.rule_count = rule_count

    @property
    def id(self):
        r"""Gets the id of this QueryDBCacheMappingResponse.

        内存加速映射ID。

        :return: The id of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryDBCacheMappingResponse.

        内存加速映射ID。

        :param id: The id of this QueryDBCacheMappingResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this QueryDBCacheMappingResponse.

        内存加速映射名称。

        :return: The name of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryDBCacheMappingResponse.

        内存加速映射名称。

        :param name: The name of this QueryDBCacheMappingResponse.
        :type name: str
        """
        self._name = name

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this QueryDBCacheMappingResponse.

        源实例ID。

        :return: The source_instance_id of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this QueryDBCacheMappingResponse.

        源实例ID。

        :param source_instance_id: The source_instance_id of this QueryDBCacheMappingResponse.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_instance_name(self):
        r"""Gets the source_instance_name of this QueryDBCacheMappingResponse.

        源实例名称。

        :return: The source_instance_name of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._source_instance_name

    @source_instance_name.setter
    def source_instance_name(self, source_instance_name):
        r"""Sets the source_instance_name of this QueryDBCacheMappingResponse.

        源实例名称。

        :param source_instance_name: The source_instance_name of this QueryDBCacheMappingResponse.
        :type source_instance_name: str
        """
        self._source_instance_name = source_instance_name

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this QueryDBCacheMappingResponse.

        目标实例ID。

        :return: The target_instance_id of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this QueryDBCacheMappingResponse.

        目标实例ID。

        :param target_instance_id: The target_instance_id of this QueryDBCacheMappingResponse.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def target_instance_name(self):
        r"""Gets the target_instance_name of this QueryDBCacheMappingResponse.

        目标实例名称。

        :return: The target_instance_name of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._target_instance_name

    @target_instance_name.setter
    def target_instance_name(self, target_instance_name):
        r"""Sets the target_instance_name of this QueryDBCacheMappingResponse.

        目标实例名称。

        :param target_instance_name: The target_instance_name of this QueryDBCacheMappingResponse.
        :type target_instance_name: str
        """
        self._target_instance_name = target_instance_name

    @property
    def status(self):
        r"""Gets the status of this QueryDBCacheMappingResponse.

        内存加速映射关系。  - normal： 表示内存加速映射正常。  - creating： 表示内存加速映射创建中。  - createfail： 表示内存加速映射创建失败。  - deleting： 表示内存加速映射解除中。  - stopped： 表示内存加速映射停止。  - deleted： 表示内存加速映射已解除。

        :return: The status of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryDBCacheMappingResponse.

        内存加速映射关系。  - normal： 表示内存加速映射正常。  - creating： 表示内存加速映射创建中。  - createfail： 表示内存加速映射创建失败。  - deleting： 表示内存加速映射解除中。  - stopped： 表示内存加速映射停止。  - deleted： 表示内存加速映射已解除。

        :param status: The status of this QueryDBCacheMappingResponse.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        r"""Gets the created of this QueryDBCacheMappingResponse.

        内存加速映射创建时间。

        :return: The created of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this QueryDBCacheMappingResponse.

        内存加速映射创建时间。

        :param created: The created of this QueryDBCacheMappingResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this QueryDBCacheMappingResponse.

        内存加速映射最新变更的时间。

        :return: The updated of this QueryDBCacheMappingResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this QueryDBCacheMappingResponse.

        内存加速映射最新变更的时间。

        :param updated: The updated of this QueryDBCacheMappingResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def rule_count(self):
        r"""Gets the rule_count of this QueryDBCacheMappingResponse.

        该内存加速映射下的规则数量。

        :return: The rule_count of this QueryDBCacheMappingResponse.
        :rtype: int
        """
        return self._rule_count

    @rule_count.setter
    def rule_count(self, rule_count):
        r"""Sets the rule_count of this QueryDBCacheMappingResponse.

        该内存加速映射下的规则数量。

        :param rule_count: The rule_count of this QueryDBCacheMappingResponse.
        :type rule_count: int
        """
        self._rule_count = rule_count

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
        if not isinstance(other, QueryDBCacheMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
