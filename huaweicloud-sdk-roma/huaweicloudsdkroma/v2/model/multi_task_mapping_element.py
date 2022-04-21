# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskMappingElement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'source_table': 'str',
        'target_table': 'str',
        'updated_time': 'int',
        'mapping_percent': 'int',
        'status': 'str',
        'source_columns': 'list[MultiTaskColumnInfo]',
        'target_columns': 'list[MultiTaskColumnInfo]',
        'mapping': 'list[MappingInfo]'
    }

    attribute_map = {
        'id': 'id',
        'source_table': 'source_table',
        'target_table': 'target_table',
        'updated_time': 'updated_time',
        'mapping_percent': 'mapping_percent',
        'status': 'status',
        'source_columns': 'source_columns',
        'target_columns': 'target_columns',
        'mapping': 'mapping'
    }

    def __init__(self, id=None, source_table=None, target_table=None, updated_time=None, mapping_percent=None, status=None, source_columns=None, target_columns=None, mapping=None):
        """MultiTaskMappingElement

        The model defined in huaweicloud sdk

        :param id: 映射唯一ID
        :type id: str
        :param source_table: 源表名
        :type source_table: str
        :param target_table: 目标表名
        :type target_table: str
        :param updated_time: 上次修改时间
        :type updated_time: int
        :param mapping_percent: 匹配度
        :type mapping_percent: int
        :param status: 映射状态 - AUTO (自动映射) - MANUAL (手工新增) - ADD (自动新增) - UPDATE (更新) - DELETE (删除) - USING (使用中)
        :type status: str
        :param source_columns: 源端字段列表
        :type source_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        :param target_columns: 目标端字段列表
        :type target_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        :param mapping: 字段映射列表
        :type mapping: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        
        

        self._id = None
        self._source_table = None
        self._target_table = None
        self._updated_time = None
        self._mapping_percent = None
        self._status = None
        self._source_columns = None
        self._target_columns = None
        self._mapping = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source_table is not None:
            self.source_table = source_table
        if target_table is not None:
            self.target_table = target_table
        if updated_time is not None:
            self.updated_time = updated_time
        if mapping_percent is not None:
            self.mapping_percent = mapping_percent
        if status is not None:
            self.status = status
        if source_columns is not None:
            self.source_columns = source_columns
        if target_columns is not None:
            self.target_columns = target_columns
        if mapping is not None:
            self.mapping = mapping

    @property
    def id(self):
        """Gets the id of this MultiTaskMappingElement.

        映射唯一ID

        :return: The id of this MultiTaskMappingElement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MultiTaskMappingElement.

        映射唯一ID

        :param id: The id of this MultiTaskMappingElement.
        :type id: str
        """
        self._id = id

    @property
    def source_table(self):
        """Gets the source_table of this MultiTaskMappingElement.

        源表名

        :return: The source_table of this MultiTaskMappingElement.
        :rtype: str
        """
        return self._source_table

    @source_table.setter
    def source_table(self, source_table):
        """Sets the source_table of this MultiTaskMappingElement.

        源表名

        :param source_table: The source_table of this MultiTaskMappingElement.
        :type source_table: str
        """
        self._source_table = source_table

    @property
    def target_table(self):
        """Gets the target_table of this MultiTaskMappingElement.

        目标表名

        :return: The target_table of this MultiTaskMappingElement.
        :rtype: str
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table):
        """Sets the target_table of this MultiTaskMappingElement.

        目标表名

        :param target_table: The target_table of this MultiTaskMappingElement.
        :type target_table: str
        """
        self._target_table = target_table

    @property
    def updated_time(self):
        """Gets the updated_time of this MultiTaskMappingElement.

        上次修改时间

        :return: The updated_time of this MultiTaskMappingElement.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this MultiTaskMappingElement.

        上次修改时间

        :param updated_time: The updated_time of this MultiTaskMappingElement.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def mapping_percent(self):
        """Gets the mapping_percent of this MultiTaskMappingElement.

        匹配度

        :return: The mapping_percent of this MultiTaskMappingElement.
        :rtype: int
        """
        return self._mapping_percent

    @mapping_percent.setter
    def mapping_percent(self, mapping_percent):
        """Sets the mapping_percent of this MultiTaskMappingElement.

        匹配度

        :param mapping_percent: The mapping_percent of this MultiTaskMappingElement.
        :type mapping_percent: int
        """
        self._mapping_percent = mapping_percent

    @property
    def status(self):
        """Gets the status of this MultiTaskMappingElement.

        映射状态 - AUTO (自动映射) - MANUAL (手工新增) - ADD (自动新增) - UPDATE (更新) - DELETE (删除) - USING (使用中)

        :return: The status of this MultiTaskMappingElement.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MultiTaskMappingElement.

        映射状态 - AUTO (自动映射) - MANUAL (手工新增) - ADD (自动新增) - UPDATE (更新) - DELETE (删除) - USING (使用中)

        :param status: The status of this MultiTaskMappingElement.
        :type status: str
        """
        self._status = status

    @property
    def source_columns(self):
        """Gets the source_columns of this MultiTaskMappingElement.

        源端字段列表

        :return: The source_columns of this MultiTaskMappingElement.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        return self._source_columns

    @source_columns.setter
    def source_columns(self, source_columns):
        """Sets the source_columns of this MultiTaskMappingElement.

        源端字段列表

        :param source_columns: The source_columns of this MultiTaskMappingElement.
        :type source_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        self._source_columns = source_columns

    @property
    def target_columns(self):
        """Gets the target_columns of this MultiTaskMappingElement.

        目标端字段列表

        :return: The target_columns of this MultiTaskMappingElement.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        return self._target_columns

    @target_columns.setter
    def target_columns(self, target_columns):
        """Sets the target_columns of this MultiTaskMappingElement.

        目标端字段列表

        :param target_columns: The target_columns of this MultiTaskMappingElement.
        :type target_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        self._target_columns = target_columns

    @property
    def mapping(self):
        """Gets the mapping of this MultiTaskMappingElement.

        字段映射列表

        :return: The mapping of this MultiTaskMappingElement.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this MultiTaskMappingElement.

        字段映射列表

        :param mapping: The mapping of this MultiTaskMappingElement.
        :type mapping: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        self._mapping = mapping

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
        if not isinstance(other, MultiTaskMappingElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
