# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunTimeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_info': 'TableInfo',
        'local_secondary_index_infos': 'list[SecondaryIndexInfo]',
        'global_secondary_index_infos': 'list[GlobalSecondaryIndexInfo]'
    }

    attribute_map = {
        'table_info': 'table_info',
        'local_secondary_index_infos': 'local_secondary_index_infos',
        'global_secondary_index_infos': 'global_secondary_index_infos'
    }

    def __init__(self, table_info=None, local_secondary_index_infos=None, global_secondary_index_infos=None):
        r"""RunTimeInfo

        The model defined in huaweicloud sdk

        :param table_info: 
        :type table_info: :class:`huaweicloudsdkkvs.v1.TableInfo`
        :param local_secondary_index_infos: 索引状态。
        :type local_secondary_index_infos: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndexInfo`]
        :param global_secondary_index_infos: 全局二级索引运行态。
        :type global_secondary_index_infos: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndexInfo`]
        """
        
        

        self._table_info = None
        self._local_secondary_index_infos = None
        self._global_secondary_index_infos = None
        self.discriminator = None

        self.table_info = table_info
        if local_secondary_index_infos is not None:
            self.local_secondary_index_infos = local_secondary_index_infos
        if global_secondary_index_infos is not None:
            self.global_secondary_index_infos = global_secondary_index_infos

    @property
    def table_info(self):
        r"""Gets the table_info of this RunTimeInfo.

        :return: The table_info of this RunTimeInfo.
        :rtype: :class:`huaweicloudsdkkvs.v1.TableInfo`
        """
        return self._table_info

    @table_info.setter
    def table_info(self, table_info):
        r"""Sets the table_info of this RunTimeInfo.

        :param table_info: The table_info of this RunTimeInfo.
        :type table_info: :class:`huaweicloudsdkkvs.v1.TableInfo`
        """
        self._table_info = table_info

    @property
    def local_secondary_index_infos(self):
        r"""Gets the local_secondary_index_infos of this RunTimeInfo.

        索引状态。

        :return: The local_secondary_index_infos of this RunTimeInfo.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndexInfo`]
        """
        return self._local_secondary_index_infos

    @local_secondary_index_infos.setter
    def local_secondary_index_infos(self, local_secondary_index_infos):
        r"""Sets the local_secondary_index_infos of this RunTimeInfo.

        索引状态。

        :param local_secondary_index_infos: The local_secondary_index_infos of this RunTimeInfo.
        :type local_secondary_index_infos: list[:class:`huaweicloudsdkkvs.v1.SecondaryIndexInfo`]
        """
        self._local_secondary_index_infos = local_secondary_index_infos

    @property
    def global_secondary_index_infos(self):
        r"""Gets the global_secondary_index_infos of this RunTimeInfo.

        全局二级索引运行态。

        :return: The global_secondary_index_infos of this RunTimeInfo.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndexInfo`]
        """
        return self._global_secondary_index_infos

    @global_secondary_index_infos.setter
    def global_secondary_index_infos(self, global_secondary_index_infos):
        r"""Sets the global_secondary_index_infos of this RunTimeInfo.

        全局二级索引运行态。

        :param global_secondary_index_infos: The global_secondary_index_infos of this RunTimeInfo.
        :type global_secondary_index_infos: list[:class:`huaweicloudsdkkvs.v1.GlobalSecondaryIndexInfo`]
        """
        self._global_secondary_index_infos = global_secondary_index_infos

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
        if not isinstance(other, RunTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
