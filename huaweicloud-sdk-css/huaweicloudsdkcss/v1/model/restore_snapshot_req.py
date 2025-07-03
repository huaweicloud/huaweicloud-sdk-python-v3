# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreSnapshotReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_cluster': 'str',
        'indices': 'str',
        'rename_pattern': 'str',
        'rename_replacement': 'str',
        'replace_exist_indices': 'bool'
    }

    attribute_map = {
        'target_cluster': 'target_cluster',
        'indices': 'indices',
        'rename_pattern': 'rename_pattern',
        'rename_replacement': 'rename_replacement',
        'replace_exist_indices': 'replace_exist_indices'
    }

    def __init__(self, target_cluster=None, indices=None, rename_pattern=None, rename_replacement=None, replace_exist_indices=None):
        r"""RestoreSnapshotReq

        The model defined in huaweicloud sdk

        :param target_cluster: 快照要恢复到的集群的ID。
        :type target_cluster: str
        :param indices: 指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\&quot;\\\\&lt;|&gt;/?特殊字符。
        :type indices: str
        :param rename_pattern: 匹配要恢复的索引规则，最大支持1024个字符。根据此处定义的过滤条件去恢复符合条件的索引，过滤条件请使用正则表达式。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\&quot;\\\\&lt;|&gt;/?,特殊字符。   renamePattern参数与renameReplacement参数必须同时设置才能生效。
        :type rename_pattern: str
        :param rename_replacement: 索引重命名的规则。0～1024个字符，不能包含空格和大写字母，且不能包含\\\&quot;\\\\&lt;|&gt;/?,特殊字符。例如，“restored_index_$1”表示在所有恢复的索引名称前面加上“restored_”。    renamePattern参数与renameReplacement参数必须同时设置才能生效。
        :type rename_replacement: str
        :param replace_exist_indices: 替换已存在的索引。    
        :type replace_exist_indices: bool
        """
        
        

        self._target_cluster = None
        self._indices = None
        self._rename_pattern = None
        self._rename_replacement = None
        self._replace_exist_indices = None
        self.discriminator = None

        self.target_cluster = target_cluster
        if indices is not None:
            self.indices = indices
        if rename_pattern is not None:
            self.rename_pattern = rename_pattern
        if rename_replacement is not None:
            self.rename_replacement = rename_replacement
        if replace_exist_indices is not None:
            self.replace_exist_indices = replace_exist_indices

    @property
    def target_cluster(self):
        r"""Gets the target_cluster of this RestoreSnapshotReq.

        快照要恢复到的集群的ID。

        :return: The target_cluster of this RestoreSnapshotReq.
        :rtype: str
        """
        return self._target_cluster

    @target_cluster.setter
    def target_cluster(self, target_cluster):
        r"""Sets the target_cluster of this RestoreSnapshotReq.

        快照要恢复到的集群的ID。

        :param target_cluster: The target_cluster of this RestoreSnapshotReq.
        :type target_cluster: str
        """
        self._target_cluster = target_cluster

    @property
    def indices(self):
        r"""Gets the indices of this RestoreSnapshotReq.

        指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。

        :return: The indices of this RestoreSnapshotReq.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        r"""Sets the indices of this RestoreSnapshotReq.

        指定要恢复的索引名称，多个索引用逗号隔开，默认恢复所有索引。支持使用“\\*”匹配多个索引，例如：2018-06\\*，表示恢复名称前缀是2018-06的所有索引的数据。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?特殊字符。

        :param indices: The indices of this RestoreSnapshotReq.
        :type indices: str
        """
        self._indices = indices

    @property
    def rename_pattern(self):
        r"""Gets the rename_pattern of this RestoreSnapshotReq.

        匹配要恢复的索引规则，最大支持1024个字符。根据此处定义的过滤条件去恢复符合条件的索引，过滤条件请使用正则表达式。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?,特殊字符。   renamePattern参数与renameReplacement参数必须同时设置才能生效。

        :return: The rename_pattern of this RestoreSnapshotReq.
        :rtype: str
        """
        return self._rename_pattern

    @rename_pattern.setter
    def rename_pattern(self, rename_pattern):
        r"""Sets the rename_pattern of this RestoreSnapshotReq.

        匹配要恢复的索引规则，最大支持1024个字符。根据此处定义的过滤条件去恢复符合条件的索引，过滤条件请使用正则表达式。  0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?,特殊字符。   renamePattern参数与renameReplacement参数必须同时设置才能生效。

        :param rename_pattern: The rename_pattern of this RestoreSnapshotReq.
        :type rename_pattern: str
        """
        self._rename_pattern = rename_pattern

    @property
    def rename_replacement(self):
        r"""Gets the rename_replacement of this RestoreSnapshotReq.

        索引重命名的规则。0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?,特殊字符。例如，“restored_index_$1”表示在所有恢复的索引名称前面加上“restored_”。    renamePattern参数与renameReplacement参数必须同时设置才能生效。

        :return: The rename_replacement of this RestoreSnapshotReq.
        :rtype: str
        """
        return self._rename_replacement

    @rename_replacement.setter
    def rename_replacement(self, rename_replacement):
        r"""Sets the rename_replacement of this RestoreSnapshotReq.

        索引重命名的规则。0～1024个字符，不能包含空格和大写字母，且不能包含\\\"\\\\<|>/?,特殊字符。例如，“restored_index_$1”表示在所有恢复的索引名称前面加上“restored_”。    renamePattern参数与renameReplacement参数必须同时设置才能生效。

        :param rename_replacement: The rename_replacement of this RestoreSnapshotReq.
        :type rename_replacement: str
        """
        self._rename_replacement = rename_replacement

    @property
    def replace_exist_indices(self):
        r"""Gets the replace_exist_indices of this RestoreSnapshotReq.

        替换已存在的索引。    

        :return: The replace_exist_indices of this RestoreSnapshotReq.
        :rtype: bool
        """
        return self._replace_exist_indices

    @replace_exist_indices.setter
    def replace_exist_indices(self, replace_exist_indices):
        r"""Sets the replace_exist_indices of this RestoreSnapshotReq.

        替换已存在的索引。    

        :param replace_exist_indices: The replace_exist_indices of this RestoreSnapshotReq.
        :type replace_exist_indices: bool
        """
        self._replace_exist_indices = replace_exist_indices

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
        if not isinstance(other, RestoreSnapshotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
