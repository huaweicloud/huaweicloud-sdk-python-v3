# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGraphRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'graph_id': 'str',
        'keep_backup': 'bool'
    }

    attribute_map = {
        'graph_id': 'graph_id',
        'keep_backup': 'keepBackup'
    }

    def __init__(self, graph_id=None, keep_backup=None):
        """DeleteGraphRequest

        The model defined in huaweicloud sdk

        :param graph_id: 图ID。
        :type graph_id: str
        :param keep_backup: 删除图后是否保留备份，默认保留1个自动备份和2个手动备份。该查询参数为空时，表示不保留。
        :type keep_backup: bool
        """
        
        

        self._graph_id = None
        self._keep_backup = None
        self.discriminator = None

        self.graph_id = graph_id
        if keep_backup is not None:
            self.keep_backup = keep_backup

    @property
    def graph_id(self):
        """Gets the graph_id of this DeleteGraphRequest.

        图ID。

        :return: The graph_id of this DeleteGraphRequest.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this DeleteGraphRequest.

        图ID。

        :param graph_id: The graph_id of this DeleteGraphRequest.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def keep_backup(self):
        """Gets the keep_backup of this DeleteGraphRequest.

        删除图后是否保留备份，默认保留1个自动备份和2个手动备份。该查询参数为空时，表示不保留。

        :return: The keep_backup of this DeleteGraphRequest.
        :rtype: bool
        """
        return self._keep_backup

    @keep_backup.setter
    def keep_backup(self, keep_backup):
        """Sets the keep_backup of this DeleteGraphRequest.

        删除图后是否保留备份，默认保留1个自动备份和2个手动备份。该查询参数为空时，表示不保留。

        :param keep_backup: The keep_backup of this DeleteGraphRequest.
        :type keep_backup: bool
        """
        self._keep_backup = keep_backup

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
        if not isinstance(other, DeleteGraphRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
