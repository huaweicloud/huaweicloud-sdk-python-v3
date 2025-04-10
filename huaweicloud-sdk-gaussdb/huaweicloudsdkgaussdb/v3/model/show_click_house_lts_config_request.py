# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClickHouseLtsConfigRequest:

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
        'enterprise_project_id': 'str',
        'instance_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'enterprise_project_id': 'enterprise_project_id',
        'instance_name': 'instance_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, instance_id=None, enterprise_project_id=None, instance_name=None, limit=None, offset=None):
        r"""ShowClickHouseLtsConfigRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: ClickHouse实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param limit: 查询记录数，默认10。不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param offset: 索引位置，偏移量，默认0。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._enterprise_project_id = None
        self._instance_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if instance_id is not None:
            self.instance_id = instance_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instance_name is not None:
            self.instance_name = instance_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowClickHouseLtsConfigRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowClickHouseLtsConfigRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowClickHouseLtsConfigRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowClickHouseLtsConfigRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowClickHouseLtsConfigRequest.

        ClickHouse实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowClickHouseLtsConfigRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowClickHouseLtsConfigRequest.

        ClickHouse实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowClickHouseLtsConfigRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowClickHouseLtsConfigRequest.

        企业项目id。

        :return: The enterprise_project_id of this ShowClickHouseLtsConfigRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowClickHouseLtsConfigRequest.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowClickHouseLtsConfigRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowClickHouseLtsConfigRequest.

        实例名称。

        :return: The instance_name of this ShowClickHouseLtsConfigRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowClickHouseLtsConfigRequest.

        实例名称。

        :param instance_name: The instance_name of this ShowClickHouseLtsConfigRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def limit(self):
        r"""Gets the limit of this ShowClickHouseLtsConfigRequest.

        查询记录数，默认10。不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowClickHouseLtsConfigRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowClickHouseLtsConfigRequest.

        查询记录数，默认10。不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowClickHouseLtsConfigRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowClickHouseLtsConfigRequest.

        索引位置，偏移量，默认0。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowClickHouseLtsConfigRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowClickHouseLtsConfigRequest.

        索引位置，偏移量，默认0。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowClickHouseLtsConfigRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowClickHouseLtsConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
