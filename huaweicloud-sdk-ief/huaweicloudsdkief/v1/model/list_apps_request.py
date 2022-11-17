# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'name': 'str',
        'limit': 'str',
        'offset': 'str',
        'alias': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'alias': 'alias',
        'visibility': 'visibility'
    }

    def __init__(self, ief_instance_id=None, name=None, limit=None, offset=None, alias=None, visibility=None):
        """ListAppsRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param name: 应用模板名称，模糊匹配
        :type name: str
        :param limit: 每页显示的条目数量，取值范围1~1000，默认为1000
        :type limit: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: str
        :param alias: 通过别名过滤，模糊匹配
        :type alias: str
        :param visibility: public：公共模板，只有管理员才能创建 private：用户创建的应用模板，默认 shared：第三方应用，其他用户共享类型的模板（保留，未实现）
        :type visibility: str
        """
        
        

        self._ief_instance_id = None
        self._name = None
        self._limit = None
        self._offset = None
        self._alias = None
        self._visibility = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if alias is not None:
            self.alias = alias
        if visibility is not None:
            self.visibility = visibility

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListAppsRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListAppsRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListAppsRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListAppsRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def name(self):
        """Gets the name of this ListAppsRequest.

        应用模板名称，模糊匹配

        :return: The name of this ListAppsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAppsRequest.

        应用模板名称，模糊匹配

        :param name: The name of this ListAppsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListAppsRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :return: The limit of this ListAppsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppsRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :param limit: The limit of this ListAppsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListAppsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListAppsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def alias(self):
        """Gets the alias of this ListAppsRequest.

        通过别名过滤，模糊匹配

        :return: The alias of this ListAppsRequest.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ListAppsRequest.

        通过别名过滤，模糊匹配

        :param alias: The alias of this ListAppsRequest.
        :type alias: str
        """
        self._alias = alias

    @property
    def visibility(self):
        """Gets the visibility of this ListAppsRequest.

        public：公共模板，只有管理员才能创建 private：用户创建的应用模板，默认 shared：第三方应用，其他用户共享类型的模板（保留，未实现）

        :return: The visibility of this ListAppsRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ListAppsRequest.

        public：公共模板，只有管理员才能创建 private：用户创建的应用模板，默认 shared：第三方应用，其他用户共享类型的模板（保留，未实现）

        :param visibility: The visibility of this ListAppsRequest.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ListAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
