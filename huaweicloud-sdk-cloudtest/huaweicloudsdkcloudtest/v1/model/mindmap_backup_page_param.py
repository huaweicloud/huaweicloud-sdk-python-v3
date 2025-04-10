# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapBackupPageParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bak_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'mindmap_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'bak_name': 'bak_name',
        'limit': 'limit',
        'offset': 'offset',
        'mindmap_id': 'mindmap_id',
        'type': 'type'
    }

    def __init__(self, bak_name=None, limit=None, offset=None, mindmap_id=None, type=None):
        r"""MindmapBackupPageParam

        The model defined in huaweicloud sdk

        :param bak_name: 备份名称
        :type bak_name: str
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param mindmap_id: 脑图ID
        :type mindmap_id: str
        :param type: 备份类型
        :type type: str
        """
        
        

        self._bak_name = None
        self._limit = None
        self._offset = None
        self._mindmap_id = None
        self._type = None
        self.discriminator = None

        if bak_name is not None:
            self.bak_name = bak_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if type is not None:
            self.type = type

    @property
    def bak_name(self):
        r"""Gets the bak_name of this MindmapBackupPageParam.

        备份名称

        :return: The bak_name of this MindmapBackupPageParam.
        :rtype: str
        """
        return self._bak_name

    @bak_name.setter
    def bak_name(self, bak_name):
        r"""Sets the bak_name of this MindmapBackupPageParam.

        备份名称

        :param bak_name: The bak_name of this MindmapBackupPageParam.
        :type bak_name: str
        """
        self._bak_name = bak_name

    @property
    def limit(self):
        r"""Gets the limit of this MindmapBackupPageParam.

        每页显示的条目数量，最大支持200条

        :return: The limit of this MindmapBackupPageParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this MindmapBackupPageParam.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this MindmapBackupPageParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this MindmapBackupPageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this MindmapBackupPageParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this MindmapBackupPageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this MindmapBackupPageParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this MindmapBackupPageParam.

        脑图ID

        :return: The mindmap_id of this MindmapBackupPageParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this MindmapBackupPageParam.

        脑图ID

        :param mindmap_id: The mindmap_id of this MindmapBackupPageParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def type(self):
        r"""Gets the type of this MindmapBackupPageParam.

        备份类型

        :return: The type of this MindmapBackupPageParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MindmapBackupPageParam.

        备份类型

        :param type: The type of this MindmapBackupPageParam.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MindmapBackupPageParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
