# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiGroupsV2Request:

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
        'roma_app_id': 'str',
        'precise_search': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'roma_app_id': 'roma_app_id',
        'precise_search': 'precise_search',
        'domain_name': 'domain_name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, name=None, roma_app_id=None, precise_search=None, domain_name=None):
        r"""ListApiGroupsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param id: API分组编号
        :type id: str
        :param name: API分组名称
        :type name: str
        :param roma_app_id: 集成应用编号
        :type roma_app_id: str
        :param precise_search: 指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  [当前支持name，domain_name。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)[目前仅支持API分组名称](tag:Site)
        :type precise_search: str
        :param domain_name: 域名
        :type domain_name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._roma_app_id = None
        self._precise_search = None
        self._domain_name = None
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
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if precise_search is not None:
            self.precise_search = precise_search
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListApiGroupsV2Request.

        实例ID

        :return: The instance_id of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListApiGroupsV2Request.

        实例ID

        :param instance_id: The instance_id of this ListApiGroupsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListApiGroupsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListApiGroupsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApiGroupsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListApiGroupsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApiGroupsV2Request.

        每页显示的条目数量

        :return: The limit of this ListApiGroupsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApiGroupsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListApiGroupsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListApiGroupsV2Request.

        API分组编号

        :return: The id of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListApiGroupsV2Request.

        API分组编号

        :param id: The id of this ListApiGroupsV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListApiGroupsV2Request.

        API分组名称

        :return: The name of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListApiGroupsV2Request.

        API分组名称

        :param name: The name of this ListApiGroupsV2Request.
        :type name: str
        """
        self._name = name

    @property
    def roma_app_id(self):
        r"""Gets the roma_app_id of this ListApiGroupsV2Request.

        集成应用编号

        :return: The roma_app_id of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        r"""Sets the roma_app_id of this ListApiGroupsV2Request.

        集成应用编号

        :param roma_app_id: The roma_app_id of this ListApiGroupsV2Request.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def precise_search(self):
        r"""Gets the precise_search of this ListApiGroupsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  [当前支持name，domain_name。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)[目前仅支持API分组名称](tag:Site)

        :return: The precise_search of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        r"""Sets the precise_search of this ListApiGroupsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  [当前支持name，domain_name。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)[目前仅支持API分组名称](tag:Site)

        :param precise_search: The precise_search of this ListApiGroupsV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListApiGroupsV2Request.

        域名

        :return: The domain_name of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListApiGroupsV2Request.

        域名

        :param domain_name: The domain_name of this ListApiGroupsV2Request.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, ListApiGroupsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
