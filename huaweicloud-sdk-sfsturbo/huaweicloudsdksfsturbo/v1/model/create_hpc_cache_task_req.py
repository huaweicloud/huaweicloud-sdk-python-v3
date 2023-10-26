# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHpcCacheTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'src_target': 'str',
        'src_prefix': 'str',
        'dest_target': 'str',
        'dest_prefix': 'str'
    }

    attribute_map = {
        'type': 'type',
        'src_target': 'src_target',
        'src_prefix': 'src_prefix',
        'dest_target': 'dest_target',
        'dest_prefix': 'dest_prefix'
    }

    def __init__(self, type=None, src_target=None, src_prefix=None, dest_target=None, dest_prefix=None):
        """CreateHpcCacheTaskReq

        The model defined in huaweicloud sdk

        :param type: 操作类型，当前支持import(普通导入)，export(导出)，import_metadata(元数据导入)，preload(数据预热)
        :type type: str
        :param src_target: 源端对象。OBS桶绑定文件系统后的文件系统路径名称
        :type src_target: str
        :param src_prefix: 源端路径前缀。例如，&#39;/mnt/sfs_turbo&#39; 为您的挂载目录，对于导入任务，前缀为prefix，则会导入到 &#39;/mnt/sfs_turbo/prefix&#39;；如导入前缀为空，则会直接导入到 &#39;/mnt/sfs_turbo&#39;。对于导出任务，前缀为prefix，则会导出到 &#39;/mnt/sfs_turbo/prefix&#39;；如导出前缀为空，则会直接导出到 &#39;/mnt/sfs_turbo&#39;。
        :type src_prefix: str
        :param dest_target: 目的端对象。目前只支持和src_target保持一致
        :type dest_target: str
        :param dest_prefix: 目的端路径。目前只支持和src_prefix保持一致
        :type dest_prefix: str
        """
        
        

        self._type = None
        self._src_target = None
        self._src_prefix = None
        self._dest_target = None
        self._dest_prefix = None
        self.discriminator = None

        self.type = type
        self.src_target = src_target
        if src_prefix is not None:
            self.src_prefix = src_prefix
        self.dest_target = dest_target
        if dest_prefix is not None:
            self.dest_prefix = dest_prefix

    @property
    def type(self):
        """Gets the type of this CreateHpcCacheTaskReq.

        操作类型，当前支持import(普通导入)，export(导出)，import_metadata(元数据导入)，preload(数据预热)

        :return: The type of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateHpcCacheTaskReq.

        操作类型，当前支持import(普通导入)，export(导出)，import_metadata(元数据导入)，preload(数据预热)

        :param type: The type of this CreateHpcCacheTaskReq.
        :type type: str
        """
        self._type = type

    @property
    def src_target(self):
        """Gets the src_target of this CreateHpcCacheTaskReq.

        源端对象。OBS桶绑定文件系统后的文件系统路径名称

        :return: The src_target of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._src_target

    @src_target.setter
    def src_target(self, src_target):
        """Sets the src_target of this CreateHpcCacheTaskReq.

        源端对象。OBS桶绑定文件系统后的文件系统路径名称

        :param src_target: The src_target of this CreateHpcCacheTaskReq.
        :type src_target: str
        """
        self._src_target = src_target

    @property
    def src_prefix(self):
        """Gets the src_prefix of this CreateHpcCacheTaskReq.

        源端路径前缀。例如，'/mnt/sfs_turbo' 为您的挂载目录，对于导入任务，前缀为prefix，则会导入到 '/mnt/sfs_turbo/prefix'；如导入前缀为空，则会直接导入到 '/mnt/sfs_turbo'。对于导出任务，前缀为prefix，则会导出到 '/mnt/sfs_turbo/prefix'；如导出前缀为空，则会直接导出到 '/mnt/sfs_turbo'。

        :return: The src_prefix of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._src_prefix

    @src_prefix.setter
    def src_prefix(self, src_prefix):
        """Sets the src_prefix of this CreateHpcCacheTaskReq.

        源端路径前缀。例如，'/mnt/sfs_turbo' 为您的挂载目录，对于导入任务，前缀为prefix，则会导入到 '/mnt/sfs_turbo/prefix'；如导入前缀为空，则会直接导入到 '/mnt/sfs_turbo'。对于导出任务，前缀为prefix，则会导出到 '/mnt/sfs_turbo/prefix'；如导出前缀为空，则会直接导出到 '/mnt/sfs_turbo'。

        :param src_prefix: The src_prefix of this CreateHpcCacheTaskReq.
        :type src_prefix: str
        """
        self._src_prefix = src_prefix

    @property
    def dest_target(self):
        """Gets the dest_target of this CreateHpcCacheTaskReq.

        目的端对象。目前只支持和src_target保持一致

        :return: The dest_target of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._dest_target

    @dest_target.setter
    def dest_target(self, dest_target):
        """Sets the dest_target of this CreateHpcCacheTaskReq.

        目的端对象。目前只支持和src_target保持一致

        :param dest_target: The dest_target of this CreateHpcCacheTaskReq.
        :type dest_target: str
        """
        self._dest_target = dest_target

    @property
    def dest_prefix(self):
        """Gets the dest_prefix of this CreateHpcCacheTaskReq.

        目的端路径。目前只支持和src_prefix保持一致

        :return: The dest_prefix of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._dest_prefix

    @dest_prefix.setter
    def dest_prefix(self, dest_prefix):
        """Sets the dest_prefix of this CreateHpcCacheTaskReq.

        目的端路径。目前只支持和src_prefix保持一致

        :param dest_prefix: The dest_prefix of this CreateHpcCacheTaskReq.
        :type dest_prefix: str
        """
        self._dest_prefix = dest_prefix

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
        if not isinstance(other, CreateHpcCacheTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
