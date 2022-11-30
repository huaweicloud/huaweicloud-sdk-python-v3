# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRestorableInstancesRequest:

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
        'source_instance_id': 'str',
        'backup_id': 'str',
        'restore_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'source_instance_id': 'source_instance_id',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, source_instance_id=None, backup_id=None, restore_time=None, offset=None, limit=None):
        """ListRestorableInstancesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param source_instance_id: 源实例id，需要恢复的实例ID。
        :type source_instance_id: str
        :param backup_id: 实例备份信息ID，根据备份ID查询实例拓扑信息，过滤查询出来的实例，包含节点数，副本数等。参数为空时，根据restore_time查询。。
        :type backup_id: str
        :param restore_time: 恢复点，当备份ID为空时，通过此参数查询实例拓扑信息，过滤实例列表。
        :type restore_time: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._x_language = None
        self._source_instance_id = None
        self._backup_id = None
        self._restore_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.source_instance_id = source_instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListRestorableInstancesRequest.

        语言。

        :return: The x_language of this ListRestorableInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListRestorableInstancesRequest.

        语言。

        :param x_language: The x_language of this ListRestorableInstancesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this ListRestorableInstancesRequest.

        源实例id，需要恢复的实例ID。

        :return: The source_instance_id of this ListRestorableInstancesRequest.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this ListRestorableInstancesRequest.

        源实例id，需要恢复的实例ID。

        :param source_instance_id: The source_instance_id of this ListRestorableInstancesRequest.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this ListRestorableInstancesRequest.

        实例备份信息ID，根据备份ID查询实例拓扑信息，过滤查询出来的实例，包含节点数，副本数等。参数为空时，根据restore_time查询。。

        :return: The backup_id of this ListRestorableInstancesRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ListRestorableInstancesRequest.

        实例备份信息ID，根据备份ID查询实例拓扑信息，过滤查询出来的实例，包含节点数，副本数等。参数为空时，根据restore_time查询。。

        :param backup_id: The backup_id of this ListRestorableInstancesRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this ListRestorableInstancesRequest.

        恢复点，当备份ID为空时，通过此参数查询实例拓扑信息，过滤实例列表。

        :return: The restore_time of this ListRestorableInstancesRequest.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this ListRestorableInstancesRequest.

        恢复点，当备份ID为空时，通过此参数查询实例拓扑信息，过滤实例列表。

        :param restore_time: The restore_time of this ListRestorableInstancesRequest.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def offset(self):
        """Gets the offset of this ListRestorableInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListRestorableInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRestorableInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListRestorableInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRestorableInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListRestorableInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRestorableInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListRestorableInstancesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRestorableInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
