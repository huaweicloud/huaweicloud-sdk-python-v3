# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogLtsConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'enterprise_project_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort': 'str',
        'instance_status': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'enterprise_project_id': 'enterprise_project_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'limit': 'limit',
        'offset': 'offset',
        'sort': 'sort',
        'instance_status': 'instance_status',
        'x_language': 'X-Language'
    }

    def __init__(self, engine=None, enterprise_project_id=None, instance_id=None, instance_name=None, limit=None, offset=None, sort=None, instance_status=None, x_language=None):
        r"""ListLogLtsConfigsRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎，暂只支持mysql。
        :type engine: str
        :param enterprise_project_id: 企业项目ID。默认为空。
        :type enterprise_project_id: str
        :param instance_id: 实例ID。默认为空。
        :type instance_id: str
        :param instance_name: 实例名称。默认为空。
        :type instance_name: str
        :param limit: 查询记录数。默认10。
        :type limit: int
        :param offset: 索引位置，偏移量。默认0。
        :type offset: int
        :param sort: 排序
        :type sort: str
        :param instance_status: 实例状态
        :type instance_status: str
        :param x_language: 语言。
        :type x_language: str
        """
        
        

        self._engine = None
        self._enterprise_project_id = None
        self._instance_id = None
        self._instance_name = None
        self._limit = None
        self._offset = None
        self._sort = None
        self._instance_status = None
        self._x_language = None
        self.discriminator = None

        self.engine = engine
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort
        if instance_status is not None:
            self.instance_status = instance_status
        if x_language is not None:
            self.x_language = x_language

    @property
    def engine(self):
        r"""Gets the engine of this ListLogLtsConfigsRequest.

        引擎，暂只支持mysql。

        :return: The engine of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListLogLtsConfigsRequest.

        引擎，暂只支持mysql。

        :param engine: The engine of this ListLogLtsConfigsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLogLtsConfigsRequest.

        企业项目ID。默认为空。

        :return: The enterprise_project_id of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLogLtsConfigsRequest.

        企业项目ID。默认为空。

        :param enterprise_project_id: The enterprise_project_id of this ListLogLtsConfigsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListLogLtsConfigsRequest.

        实例ID。默认为空。

        :return: The instance_id of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListLogLtsConfigsRequest.

        实例ID。默认为空。

        :param instance_id: The instance_id of this ListLogLtsConfigsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListLogLtsConfigsRequest.

        实例名称。默认为空。

        :return: The instance_name of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListLogLtsConfigsRequest.

        实例名称。默认为空。

        :param instance_name: The instance_name of this ListLogLtsConfigsRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def limit(self):
        r"""Gets the limit of this ListLogLtsConfigsRequest.

        查询记录数。默认10。

        :return: The limit of this ListLogLtsConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLogLtsConfigsRequest.

        查询记录数。默认10。

        :param limit: The limit of this ListLogLtsConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListLogLtsConfigsRequest.

        索引位置，偏移量。默认0。

        :return: The offset of this ListLogLtsConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLogLtsConfigsRequest.

        索引位置，偏移量。默认0。

        :param offset: The offset of this ListLogLtsConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort(self):
        r"""Gets the sort of this ListLogLtsConfigsRequest.

        排序

        :return: The sort of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListLogLtsConfigsRequest.

        排序

        :param sort: The sort of this ListLogLtsConfigsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ListLogLtsConfigsRequest.

        实例状态

        :return: The instance_status of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ListLogLtsConfigsRequest.

        实例状态

        :param instance_status: The instance_status of this ListLogLtsConfigsRequest.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def x_language(self):
        r"""Gets the x_language of this ListLogLtsConfigsRequest.

        语言。

        :return: The x_language of this ListLogLtsConfigsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListLogLtsConfigsRequest.

        语言。

        :param x_language: The x_language of this ListLogLtsConfigsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListLogLtsConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
