# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskMappingCreateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ext_info': 'MultiTaskInitElementExtInfo',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'source_columns': 'list[MultiTaskColumnInfo]',
        'target_columns': 'list[MultiTaskColumnInfo]',
        'source_table': 'str',
        'target_table': 'str',
        'mapping_columns': 'list[MappingInfo]'
    }

    attribute_map = {
        'ext_info': 'ext_info',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'source_columns': 'source_columns',
        'target_columns': 'target_columns',
        'source_table': 'source_table',
        'target_table': 'target_table',
        'mapping_columns': 'mapping_columns'
    }

    def __init__(self, ext_info=None, source_datasource_id=None, target_datasource_id=None, source_columns=None, target_columns=None, source_table=None, target_table=None, mapping_columns=None):
        """MultiTaskMappingCreateBody

        The model defined in huaweicloud sdk

        :param ext_info: 
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        :param source_datasource_id: 源端数据源ID
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID
        :type target_datasource_id: str
        :param source_columns: 源端字段列表
        :type source_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        :param target_columns: 目标端字段列表
        :type target_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        :param source_table: 源表名
        :type source_table: str
        :param target_table: 目标表名
        :type target_table: str
        :param mapping_columns: 字段映射列表
        :type mapping_columns: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        
        

        self._ext_info = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._source_columns = None
        self._target_columns = None
        self._source_table = None
        self._target_table = None
        self._mapping_columns = None
        self.discriminator = None

        if ext_info is not None:
            self.ext_info = ext_info
        self.source_datasource_id = source_datasource_id
        self.target_datasource_id = target_datasource_id
        if source_columns is not None:
            self.source_columns = source_columns
        if target_columns is not None:
            self.target_columns = target_columns
        if source_table is not None:
            self.source_table = source_table
        if target_table is not None:
            self.target_table = target_table
        if mapping_columns is not None:
            self.mapping_columns = mapping_columns

    @property
    def ext_info(self):
        """Gets the ext_info of this MultiTaskMappingCreateBody.

        :return: The ext_info of this MultiTaskMappingCreateBody.
        :rtype: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this MultiTaskMappingCreateBody.

        :param ext_info: The ext_info of this MultiTaskMappingCreateBody.
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        """
        self._ext_info = ext_info

    @property
    def source_datasource_id(self):
        """Gets the source_datasource_id of this MultiTaskMappingCreateBody.

        源端数据源ID

        :return: The source_datasource_id of this MultiTaskMappingCreateBody.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        """Sets the source_datasource_id of this MultiTaskMappingCreateBody.

        源端数据源ID

        :param source_datasource_id: The source_datasource_id of this MultiTaskMappingCreateBody.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        """Gets the target_datasource_id of this MultiTaskMappingCreateBody.

        目标端数据源ID

        :return: The target_datasource_id of this MultiTaskMappingCreateBody.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        """Sets the target_datasource_id of this MultiTaskMappingCreateBody.

        目标端数据源ID

        :param target_datasource_id: The target_datasource_id of this MultiTaskMappingCreateBody.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def source_columns(self):
        """Gets the source_columns of this MultiTaskMappingCreateBody.

        源端字段列表

        :return: The source_columns of this MultiTaskMappingCreateBody.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        return self._source_columns

    @source_columns.setter
    def source_columns(self, source_columns):
        """Sets the source_columns of this MultiTaskMappingCreateBody.

        源端字段列表

        :param source_columns: The source_columns of this MultiTaskMappingCreateBody.
        :type source_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        self._source_columns = source_columns

    @property
    def target_columns(self):
        """Gets the target_columns of this MultiTaskMappingCreateBody.

        目标端字段列表

        :return: The target_columns of this MultiTaskMappingCreateBody.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        return self._target_columns

    @target_columns.setter
    def target_columns(self, target_columns):
        """Sets the target_columns of this MultiTaskMappingCreateBody.

        目标端字段列表

        :param target_columns: The target_columns of this MultiTaskMappingCreateBody.
        :type target_columns: list[:class:`huaweicloudsdkroma.v2.MultiTaskColumnInfo`]
        """
        self._target_columns = target_columns

    @property
    def source_table(self):
        """Gets the source_table of this MultiTaskMappingCreateBody.

        源表名

        :return: The source_table of this MultiTaskMappingCreateBody.
        :rtype: str
        """
        return self._source_table

    @source_table.setter
    def source_table(self, source_table):
        """Sets the source_table of this MultiTaskMappingCreateBody.

        源表名

        :param source_table: The source_table of this MultiTaskMappingCreateBody.
        :type source_table: str
        """
        self._source_table = source_table

    @property
    def target_table(self):
        """Gets the target_table of this MultiTaskMappingCreateBody.

        目标表名

        :return: The target_table of this MultiTaskMappingCreateBody.
        :rtype: str
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table):
        """Sets the target_table of this MultiTaskMappingCreateBody.

        目标表名

        :param target_table: The target_table of this MultiTaskMappingCreateBody.
        :type target_table: str
        """
        self._target_table = target_table

    @property
    def mapping_columns(self):
        """Gets the mapping_columns of this MultiTaskMappingCreateBody.

        字段映射列表

        :return: The mapping_columns of this MultiTaskMappingCreateBody.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        return self._mapping_columns

    @mapping_columns.setter
    def mapping_columns(self, mapping_columns):
        """Sets the mapping_columns of this MultiTaskMappingCreateBody.

        字段映射列表

        :param mapping_columns: The mapping_columns of this MultiTaskMappingCreateBody.
        :type mapping_columns: list[:class:`huaweicloudsdkroma.v2.MappingInfo`]
        """
        self._mapping_columns = mapping_columns

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
        if not isinstance(other, MultiTaskMappingCreateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
