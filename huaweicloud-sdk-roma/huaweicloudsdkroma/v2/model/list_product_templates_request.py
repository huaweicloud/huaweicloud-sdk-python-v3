# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductTemplatesRequest:

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
        'limit': 'int',
        'id': 'int',
        'name': 'str',
        'status': 'int',
        'created_user_name': 'str',
        'created_date_start': 'int',
        'created_date_end': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'created_user_name': 'created_user_name',
        'created_date_start': 'created_date_start',
        'created_date_end': 'created_date_end',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, limit=None, id=None, name=None, status=None, created_user_name=None, created_date_start=None, created_date_end=None, offset=None):
        """ListProductTemplatesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param id: 产品模板ID
        :type id: int
        :param name: 产品模板名称
        :type name: str
        :param status: 产品模板状态 0-启用 1-停用
        :type status: int
        :param created_user_name: 创建用户名
        :type created_user_name: str
        :param created_date_start: 创建时间起始，格式timestamp(ms)，使用UTC时区
        :type created_date_start: int
        :param created_date_end: 创建时间截止，格式timestamp(ms)，使用UTC时区
        :type created_date_end: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        """
        
        

        self._instance_id = None
        self._limit = None
        self._id = None
        self._name = None
        self._status = None
        self._created_user_name = None
        self._created_date_start = None
        self._created_date_end = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if created_date_start is not None:
            self.created_date_start = created_date_start
        if created_date_end is not None:
            self.created_date_end = created_date_end
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListProductTemplatesRequest.

        实例ID

        :return: The instance_id of this ListProductTemplatesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListProductTemplatesRequest.

        实例ID

        :param instance_id: The instance_id of this ListProductTemplatesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListProductTemplatesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProductTemplatesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListProductTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this ListProductTemplatesRequest.

        产品模板ID

        :return: The id of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListProductTemplatesRequest.

        产品模板ID

        :param id: The id of this ListProductTemplatesRequest.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListProductTemplatesRequest.

        产品模板名称

        :return: The name of this ListProductTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProductTemplatesRequest.

        产品模板名称

        :param name: The name of this ListProductTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListProductTemplatesRequest.

        产品模板状态 0-启用 1-停用

        :return: The status of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProductTemplatesRequest.

        产品模板状态 0-启用 1-停用

        :param status: The status of this ListProductTemplatesRequest.
        :type status: int
        """
        self._status = status

    @property
    def created_user_name(self):
        """Gets the created_user_name of this ListProductTemplatesRequest.

        创建用户名

        :return: The created_user_name of this ListProductTemplatesRequest.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        """Sets the created_user_name of this ListProductTemplatesRequest.

        创建用户名

        :param created_user_name: The created_user_name of this ListProductTemplatesRequest.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def created_date_start(self):
        """Gets the created_date_start of this ListProductTemplatesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :return: The created_date_start of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._created_date_start

    @created_date_start.setter
    def created_date_start(self, created_date_start):
        """Sets the created_date_start of this ListProductTemplatesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :param created_date_start: The created_date_start of this ListProductTemplatesRequest.
        :type created_date_start: int
        """
        self._created_date_start = created_date_start

    @property
    def created_date_end(self):
        """Gets the created_date_end of this ListProductTemplatesRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :return: The created_date_end of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._created_date_end

    @created_date_end.setter
    def created_date_end(self, created_date_end):
        """Sets the created_date_end of this ListProductTemplatesRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :param created_date_end: The created_date_end of this ListProductTemplatesRequest.
        :type created_date_end: int
        """
        self._created_date_end = created_date_end

    @property
    def offset(self):
        """Gets the offset of this ListProductTemplatesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListProductTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProductTemplatesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListProductTemplatesRequest.
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
        if not isinstance(other, ListProductTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
