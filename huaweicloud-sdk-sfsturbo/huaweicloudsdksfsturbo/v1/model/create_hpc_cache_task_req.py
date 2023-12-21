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

        :param type: 任务类型，当前支持import(附加元数据导入)，import_metadata(快速导入)，preload(数据预热)，export(导出)。 附加元数据导入方式会导入OBS对象的元数据（名称、大小、最后修改时间）以及来源于SFS Turbo HPC型导出时的附加元数据（如uid、gid、mode）。 快速导入方式仅会导入OBS对象的元数据（名称、大小、最后修改时间），不会导入其它附加元数据（如uid、gid、mode），SFS Turbo会生成默认的附加元数据（uid:0、gid:0、目录权限:755、文件权限:644）。 数据预热功能会同时导入元数据和数据内容，数据预热中的元数据导入采用快速导入方式，不会导入其它附加元数据（如uid、gid、mode）。 数据导出功能会将您在联动目录里创建的文件，以及对从OBS导入后又做过修改的文件导出存储到OBS桶里。
        :type type: str
        :param src_target: 联动目录名称
        :type src_target: str
        :param src_prefix: 导入导出任务的源端路径前缀，导入时不需要包含OBS桶名，导出时不需要包含联动目录名称。 对于数据预热导入，携带源端路径前缀时必须是以“/”结尾的目录或具体到某个对象。 如果不带该字段，导入时会导入绑定OBS桶内的所有对象，导出时会导出联动目录下的所有文件。
        :type src_prefix: str
        :param dest_target: 目前只支持和src_target保持一致
        :type dest_target: str
        :param dest_prefix: 目前只支持和src_prefix保持一致
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

        任务类型，当前支持import(附加元数据导入)，import_metadata(快速导入)，preload(数据预热)，export(导出)。 附加元数据导入方式会导入OBS对象的元数据（名称、大小、最后修改时间）以及来源于SFS Turbo HPC型导出时的附加元数据（如uid、gid、mode）。 快速导入方式仅会导入OBS对象的元数据（名称、大小、最后修改时间），不会导入其它附加元数据（如uid、gid、mode），SFS Turbo会生成默认的附加元数据（uid:0、gid:0、目录权限:755、文件权限:644）。 数据预热功能会同时导入元数据和数据内容，数据预热中的元数据导入采用快速导入方式，不会导入其它附加元数据（如uid、gid、mode）。 数据导出功能会将您在联动目录里创建的文件，以及对从OBS导入后又做过修改的文件导出存储到OBS桶里。

        :return: The type of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateHpcCacheTaskReq.

        任务类型，当前支持import(附加元数据导入)，import_metadata(快速导入)，preload(数据预热)，export(导出)。 附加元数据导入方式会导入OBS对象的元数据（名称、大小、最后修改时间）以及来源于SFS Turbo HPC型导出时的附加元数据（如uid、gid、mode）。 快速导入方式仅会导入OBS对象的元数据（名称、大小、最后修改时间），不会导入其它附加元数据（如uid、gid、mode），SFS Turbo会生成默认的附加元数据（uid:0、gid:0、目录权限:755、文件权限:644）。 数据预热功能会同时导入元数据和数据内容，数据预热中的元数据导入采用快速导入方式，不会导入其它附加元数据（如uid、gid、mode）。 数据导出功能会将您在联动目录里创建的文件，以及对从OBS导入后又做过修改的文件导出存储到OBS桶里。

        :param type: The type of this CreateHpcCacheTaskReq.
        :type type: str
        """
        self._type = type

    @property
    def src_target(self):
        """Gets the src_target of this CreateHpcCacheTaskReq.

        联动目录名称

        :return: The src_target of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._src_target

    @src_target.setter
    def src_target(self, src_target):
        """Sets the src_target of this CreateHpcCacheTaskReq.

        联动目录名称

        :param src_target: The src_target of this CreateHpcCacheTaskReq.
        :type src_target: str
        """
        self._src_target = src_target

    @property
    def src_prefix(self):
        """Gets the src_prefix of this CreateHpcCacheTaskReq.

        导入导出任务的源端路径前缀，导入时不需要包含OBS桶名，导出时不需要包含联动目录名称。 对于数据预热导入，携带源端路径前缀时必须是以“/”结尾的目录或具体到某个对象。 如果不带该字段，导入时会导入绑定OBS桶内的所有对象，导出时会导出联动目录下的所有文件。

        :return: The src_prefix of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._src_prefix

    @src_prefix.setter
    def src_prefix(self, src_prefix):
        """Sets the src_prefix of this CreateHpcCacheTaskReq.

        导入导出任务的源端路径前缀，导入时不需要包含OBS桶名，导出时不需要包含联动目录名称。 对于数据预热导入，携带源端路径前缀时必须是以“/”结尾的目录或具体到某个对象。 如果不带该字段，导入时会导入绑定OBS桶内的所有对象，导出时会导出联动目录下的所有文件。

        :param src_prefix: The src_prefix of this CreateHpcCacheTaskReq.
        :type src_prefix: str
        """
        self._src_prefix = src_prefix

    @property
    def dest_target(self):
        """Gets the dest_target of this CreateHpcCacheTaskReq.

        目前只支持和src_target保持一致

        :return: The dest_target of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._dest_target

    @dest_target.setter
    def dest_target(self, dest_target):
        """Sets the dest_target of this CreateHpcCacheTaskReq.

        目前只支持和src_target保持一致

        :param dest_target: The dest_target of this CreateHpcCacheTaskReq.
        :type dest_target: str
        """
        self._dest_target = dest_target

    @property
    def dest_prefix(self):
        """Gets the dest_prefix of this CreateHpcCacheTaskReq.

        目前只支持和src_prefix保持一致

        :return: The dest_prefix of this CreateHpcCacheTaskReq.
        :rtype: str
        """
        return self._dest_prefix

    @dest_prefix.setter
    def dest_prefix(self, dest_prefix):
        """Sets the dest_prefix of this CreateHpcCacheTaskReq.

        目前只支持和src_prefix保持一致

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
