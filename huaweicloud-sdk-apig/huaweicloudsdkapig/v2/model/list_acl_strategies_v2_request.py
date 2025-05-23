# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAclStrategiesV2Request:

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
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'name': 'str',
        'acl_type': 'str',
        'entity_type': 'str',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'acl_type': 'acl_type',
        'entity_type': 'entity_type',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, name=None, acl_type=None, entity_type=None, precise_search=None):
        r"""ListAclStrategiesV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param id: ACL策略编号。
        :type id: str
        :param name: ACL策略名称。
        :type name: str
        :param acl_type: 类型 - PERMIT (白名单类型) - DENY (黑名单类型)
        :type acl_type: str
        :param entity_type: 作用的对象类型： - IP - DOMAIN
        :type entity_type: str
        :param precise_search: 指定需要精确匹配查找的参数名称，目前仅支持name
        :type precise_search: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._acl_type = None
        self._entity_type = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if acl_type is not None:
            self.acl_type = acl_type
        if entity_type is not None:
            self.entity_type = entity_type
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAclStrategiesV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAclStrategiesV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListAclStrategiesV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAclStrategiesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListAclStrategiesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAclStrategiesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListAclStrategiesV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAclStrategiesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListAclStrategiesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAclStrategiesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListAclStrategiesV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListAclStrategiesV2Request.

        ACL策略编号。

        :return: The id of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAclStrategiesV2Request.

        ACL策略编号。

        :param id: The id of this ListAclStrategiesV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListAclStrategiesV2Request.

        ACL策略名称。

        :return: The name of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAclStrategiesV2Request.

        ACL策略名称。

        :param name: The name of this ListAclStrategiesV2Request.
        :type name: str
        """
        self._name = name

    @property
    def acl_type(self):
        r"""Gets the acl_type of this ListAclStrategiesV2Request.

        类型 - PERMIT (白名单类型) - DENY (黑名单类型)

        :return: The acl_type of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        r"""Sets the acl_type of this ListAclStrategiesV2Request.

        类型 - PERMIT (白名单类型) - DENY (黑名单类型)

        :param acl_type: The acl_type of this ListAclStrategiesV2Request.
        :type acl_type: str
        """
        self._acl_type = acl_type

    @property
    def entity_type(self):
        r"""Gets the entity_type of this ListAclStrategiesV2Request.

        作用的对象类型： - IP - DOMAIN

        :return: The entity_type of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        r"""Sets the entity_type of this ListAclStrategiesV2Request.

        作用的对象类型： - IP - DOMAIN

        :param entity_type: The entity_type of this ListAclStrategiesV2Request.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def precise_search(self):
        r"""Gets the precise_search of this ListAclStrategiesV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :return: The precise_search of this ListAclStrategiesV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        r"""Sets the precise_search of this ListAclStrategiesV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :param precise_search: The precise_search of this ListAclStrategiesV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListAclStrategiesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
