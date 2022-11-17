# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSlowlogRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name_list': 'list[str]',
        'node_id_list': 'list[str]'
    }

    attribute_map = {
        'file_name_list': 'file_name_list',
        'node_id_list': 'node_id_list'
    }

    def __init__(self, file_name_list=None, node_id_list=None):
        """DownloadSlowlogRequestBody

        The model defined in huaweicloud sdk

        :param file_name_list: - 需要下载的文件的文件名列表。
        :type file_name_list: list[str]
        :param node_id_list: 节点ID列表，取空值，表示查询实例下所有允许查询的节点。使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群下面的 shard节点 - 副本集、单节点下面的所有节点
        :type node_id_list: list[str]
        """
        
        

        self._file_name_list = None
        self._node_id_list = None
        self.discriminator = None

        if file_name_list is not None:
            self.file_name_list = file_name_list
        if node_id_list is not None:
            self.node_id_list = node_id_list

    @property
    def file_name_list(self):
        """Gets the file_name_list of this DownloadSlowlogRequestBody.

        - 需要下载的文件的文件名列表。

        :return: The file_name_list of this DownloadSlowlogRequestBody.
        :rtype: list[str]
        """
        return self._file_name_list

    @file_name_list.setter
    def file_name_list(self, file_name_list):
        """Sets the file_name_list of this DownloadSlowlogRequestBody.

        - 需要下载的文件的文件名列表。

        :param file_name_list: The file_name_list of this DownloadSlowlogRequestBody.
        :type file_name_list: list[str]
        """
        self._file_name_list = file_name_list

    @property
    def node_id_list(self):
        """Gets the node_id_list of this DownloadSlowlogRequestBody.

        节点ID列表，取空值，表示查询实例下所有允许查询的节点。使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群下面的 shard节点 - 副本集、单节点下面的所有节点

        :return: The node_id_list of this DownloadSlowlogRequestBody.
        :rtype: list[str]
        """
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, node_id_list):
        """Sets the node_id_list of this DownloadSlowlogRequestBody.

        节点ID列表，取空值，表示查询实例下所有允许查询的节点。使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群下面的 shard节点 - 副本集、单节点下面的所有节点

        :param node_id_list: The node_id_list of this DownloadSlowlogRequestBody.
        :type node_id_list: list[str]
        """
        self._node_id_list = node_id_list

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
        if not isinstance(other, DownloadSlowlogRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
