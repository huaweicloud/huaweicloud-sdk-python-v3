# coding: utf-8

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
        'engine': 'str',
        'name': 'str',
        'instance_id': 'str',
        'status': 'str',
        'include_failure': 'str',
        'exact_match_name': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'engine': 'engine',
        'name': 'name',
        'instance_id': 'instance_id',
        'status': 'status',
        'include_failure': 'include_failure',
        'exact_match_name': 'exact_match_name',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, engine=None, name=None, instance_id=None, status=None, include_failure=None, exact_match_name=None, enterprise_project_id=None, limit=None, offset=None):
        """ListInstancesRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎。
        :type engine: str
        :param name: 实例名称。
        :type name: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param status: 实例状态，详细状态说明请参考[实例状态说明](hrm-api-0010.xml)。
        :type status: str
        :param include_failure: 是否返回创建失败的实例数。  当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。
        :type include_failure: str
        :param exact_match_name: 是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。
        :type exact_match_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param limit: 当次查询返回的最大个数，默认值为10，取值范围为1~50。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._engine = None
        self._name = None
        self._instance_id = None
        self._status = None
        self._include_failure = None
        self._exact_match_name = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if include_failure is not None:
            self.include_failure = include_failure
        if exact_match_name is not None:
            self.exact_match_name = exact_match_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def engine(self):
        """Gets the engine of this ListInstancesRequest.

        消息引擎。

        :return: The engine of this ListInstancesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesRequest.

        消息引擎。

        :param engine: The engine of this ListInstancesRequest.
        :type engine: str
        """
        self._engine = engine

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
    def status(self):
        """Gets the status of this ListInstancesRequest.

        实例状态，详细状态说明请参考[实例状态说明](hrm-api-0010.xml)。

        :return: The status of this ListInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesRequest.

        实例状态，详细状态说明请参考[实例状态说明](hrm-api-0010.xml)。

        :param status: The status of this ListInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def include_failure(self):
        """Gets the include_failure of this ListInstancesRequest.

        是否返回创建失败的实例数。  当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :return: The include_failure of this ListInstancesRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListInstancesRequest.

        是否返回创建失败的实例数。  当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :param include_failure: The include_failure of this ListInstancesRequest.
        :type include_failure: str
        """
        self._include_failure = include_failure

    @property
    def exact_match_name(self):
        """Gets the exact_match_name of this ListInstancesRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :return: The exact_match_name of this ListInstancesRequest.
        :rtype: str
        """
        return self._exact_match_name

    @exact_match_name.setter
    def exact_match_name(self, exact_match_name):
        """Sets the exact_match_name of this ListInstancesRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :param exact_match_name: The exact_match_name of this ListInstancesRequest.
        :type exact_match_name: str
        """
        self._exact_match_name = exact_match_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInstancesRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInstancesRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.

        当次查询返回的最大个数，默认值为10，取值范围为1~50。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.

        当次查询返回的最大个数，默认值为10，取值范围为1~50。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListInstancesRequest.
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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
