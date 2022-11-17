# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMembersDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'dest_project_id': 'str',
        'image_id': 'str',
        'status': 'str',
        'vault_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'dest_project_id': 'dest_project_id',
        'image_id': 'image_id',
        'status': 'status',
        'vault_id': 'vault_id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'sort': 'sort'
    }

    def __init__(self, backup_id=None, dest_project_id=None, image_id=None, status=None, vault_id=None, limit=None, marker=None, offset=None, sort=None):
        """ShowMembersDetailRequest

        The model defined in huaweicloud sdk

        :param backup_id: 备份id
        :type backup_id: str
        :param dest_project_id: 接受备份共享的项目id
        :type dest_project_id: str
        :param image_id: 接受的共享备份副本注册的镜像id
        :type image_id: str
        :param status: 备份共享状态
        :type status: str
        :param vault_id: 目标端接受共享备份的存储库id，仅支持uuid
        :type vault_id: str
        :param limit: 每页显示的条目数量，正整数
        :type limit: int
        :param marker: 上一次查询最后一条的id，仅支持uuid
        :type marker: str
        :param offset: 偏移值，正整数
        :type offset: int
        :param sort: sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如&lt;key1&gt;[:&lt;direction&gt;],&lt;key2&gt;[:&lt;direction&gt;],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。
        :type sort: str
        """
        
        

        self._backup_id = None
        self._dest_project_id = None
        self._image_id = None
        self._status = None
        self._vault_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._sort = None
        self.discriminator = None

        self.backup_id = backup_id
        if dest_project_id is not None:
            self.dest_project_id = dest_project_id
        if image_id is not None:
            self.image_id = image_id
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort

    @property
    def backup_id(self):
        """Gets the backup_id of this ShowMembersDetailRequest.

        备份id

        :return: The backup_id of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ShowMembersDetailRequest.

        备份id

        :param backup_id: The backup_id of this ShowMembersDetailRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def dest_project_id(self):
        """Gets the dest_project_id of this ShowMembersDetailRequest.

        接受备份共享的项目id

        :return: The dest_project_id of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._dest_project_id

    @dest_project_id.setter
    def dest_project_id(self, dest_project_id):
        """Sets the dest_project_id of this ShowMembersDetailRequest.

        接受备份共享的项目id

        :param dest_project_id: The dest_project_id of this ShowMembersDetailRequest.
        :type dest_project_id: str
        """
        self._dest_project_id = dest_project_id

    @property
    def image_id(self):
        """Gets the image_id of this ShowMembersDetailRequest.

        接受的共享备份副本注册的镜像id

        :return: The image_id of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ShowMembersDetailRequest.

        接受的共享备份副本注册的镜像id

        :param image_id: The image_id of this ShowMembersDetailRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def status(self):
        """Gets the status of this ShowMembersDetailRequest.

        备份共享状态

        :return: The status of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowMembersDetailRequest.

        备份共享状态

        :param status: The status of this ShowMembersDetailRequest.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this ShowMembersDetailRequest.

        目标端接受共享备份的存储库id，仅支持uuid

        :return: The vault_id of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ShowMembersDetailRequest.

        目标端接受共享备份的存储库id，仅支持uuid

        :param vault_id: The vault_id of this ShowMembersDetailRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def limit(self):
        """Gets the limit of this ShowMembersDetailRequest.

        每页显示的条目数量，正整数

        :return: The limit of this ShowMembersDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMembersDetailRequest.

        每页显示的条目数量，正整数

        :param limit: The limit of this ShowMembersDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowMembersDetailRequest.

        上一次查询最后一条的id，仅支持uuid

        :return: The marker of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowMembersDetailRequest.

        上一次查询最后一条的id，仅支持uuid

        :param marker: The marker of this ShowMembersDetailRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ShowMembersDetailRequest.

        偏移值，正整数

        :return: The offset of this ShowMembersDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMembersDetailRequest.

        偏移值，正整数

        :param offset: The offset of this ShowMembersDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort(self):
        """Gets the sort of this ShowMembersDetailRequest.

        sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如<key1>[:<direction>],<key2>[:<direction>],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。

        :return: The sort of this ShowMembersDetailRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ShowMembersDetailRequest.

        sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如<key1>[:<direction>],<key2>[:<direction>],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。

        :param sort: The sort of this ShowMembersDetailRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ShowMembersDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
