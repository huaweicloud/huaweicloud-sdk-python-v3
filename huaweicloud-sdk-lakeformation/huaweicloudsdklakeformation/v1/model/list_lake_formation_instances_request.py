# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLakeFormationInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'in_recycle_bin': 'bool',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'enterprise_project_id': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'in_recycle_bin': 'in_recycle_bin',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, in_recycle_bin=None, offset=None, limit=None, name=None, enterprise_project_id=None, tags=None):
        r"""ListLakeFormationInstancesRequest

        The model defined in huaweicloud sdk

        :param in_recycle_bin: 是否查询回收站中的实例
        :type in_recycle_bin: bool
        :param offset: 分页查询时的偏移量
        :type offset: int
        :param limit: 分页一页显示数
        :type limit: int
        :param name: 使用LakeFormation实例名进行检索
        :type name: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param tags: 标签条件列表
        :type tags: str
        """
        
        

        self._in_recycle_bin = None
        self._offset = None
        self._limit = None
        self._name = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.in_recycle_bin = in_recycle_bin
        self.offset = offset
        self.limit = limit
        if name is not None:
            self.name = name
        self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def in_recycle_bin(self):
        r"""Gets the in_recycle_bin of this ListLakeFormationInstancesRequest.

        是否查询回收站中的实例

        :return: The in_recycle_bin of this ListLakeFormationInstancesRequest.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        r"""Sets the in_recycle_bin of this ListLakeFormationInstancesRequest.

        是否查询回收站中的实例

        :param in_recycle_bin: The in_recycle_bin of this ListLakeFormationInstancesRequest.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

    @property
    def offset(self):
        r"""Gets the offset of this ListLakeFormationInstancesRequest.

        分页查询时的偏移量

        :return: The offset of this ListLakeFormationInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLakeFormationInstancesRequest.

        分页查询时的偏移量

        :param offset: The offset of this ListLakeFormationInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLakeFormationInstancesRequest.

        分页一页显示数

        :return: The limit of this ListLakeFormationInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLakeFormationInstancesRequest.

        分页一页显示数

        :param limit: The limit of this ListLakeFormationInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListLakeFormationInstancesRequest.

        使用LakeFormation实例名进行检索

        :return: The name of this ListLakeFormationInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListLakeFormationInstancesRequest.

        使用LakeFormation实例名进行检索

        :param name: The name of this ListLakeFormationInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLakeFormationInstancesRequest.

        企业项目id

        :return: The enterprise_project_id of this ListLakeFormationInstancesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLakeFormationInstancesRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListLakeFormationInstancesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ListLakeFormationInstancesRequest.

        标签条件列表

        :return: The tags of this ListLakeFormationInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListLakeFormationInstancesRequest.

        标签条件列表

        :param tags: The tags of this ListLakeFormationInstancesRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListLakeFormationInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
