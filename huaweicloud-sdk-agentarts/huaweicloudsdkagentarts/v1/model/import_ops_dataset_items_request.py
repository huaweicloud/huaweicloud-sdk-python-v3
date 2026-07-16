# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOpsDatasetItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_id': 'str',
        'source_version_id': 'str',
        'overwrite': 'bool',
        'get_obs_url': 'bool',
        'obs_object_name': 'str',
        'obs_file_hash': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'source_version_id': 'source_version_id',
        'overwrite': 'overwrite',
        'get_obs_url': 'get_obs_url',
        'obs_object_name': 'obs_object_name',
        'obs_file_hash': 'obs_file_hash'
    }

    def __init__(self, dataset_id=None, source_version_id=None, overwrite=None, get_obs_url=None, obs_object_name=None, obs_file_hash=None):
        r"""ImportOpsDatasetItemsRequest

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 
        :type dataset_id: str
        :param source_version_id: **参数解释：** 源版本ID。用于指定在数据还原或复制操作中作为参考的基础版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。
        :type source_version_id: str
        :param overwrite: **参数解释：** 覆盖模式开关。决定在导入新数据前是否清空草稿版本中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - &#x60;true&#x60;: 覆盖模式，执行清空操作。 - &#x60;false&#x60;: 追加模式，保留现有数据。 **默认取值：** false。
        :type overwrite: bool
        :param get_obs_url: **参数解释：** 获取OBS预签名URL标识。用于确定是否需要系统生成并返回用于大文件直传的临时上传链接。 **约束限制：** 仅在不使用 multipart/form-data 模式时启用。 **取值范围：** true, false。 **默认取值：** false。
        :type get_obs_url: bool
        :param obs_object_name: **参数解释：** OBS对象名称。指定待导入文件在对象存储（OBS）中的完整存储路径或文件名。 **约束限制：** 字符串长度限制为0到10000个字符。 **取值范围：** 0到10000 字符。 **默认取值：** 不涉及。
        :type obs_object_name: str
        :param obs_file_hash: **参数解释：** 文件哈希值（SHA-256）。用于在服务端进行文件完整性校验，确保上传过程中数据未损坏或被篡改。 **约束限制：** 十六进制字符串，最大长度 256 个字符。 **取值范围：** 0到256字符。 **默认取值：** 不涉及。
        :type obs_file_hash: str
        """
        
        

        self._dataset_id = None
        self._source_version_id = None
        self._overwrite = None
        self._get_obs_url = None
        self._obs_object_name = None
        self._obs_file_hash = None
        self.discriminator = None

        self.dataset_id = dataset_id
        if source_version_id is not None:
            self.source_version_id = source_version_id
        if overwrite is not None:
            self.overwrite = overwrite
        if get_obs_url is not None:
            self.get_obs_url = get_obs_url
        if obs_object_name is not None:
            self.obs_object_name = obs_object_name
        if obs_file_hash is not None:
            self.obs_file_hash = obs_file_hash

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this ImportOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :return: The dataset_id of this ImportOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this ImportOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :param dataset_id: The dataset_id of this ImportOpsDatasetItemsRequest.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def source_version_id(self):
        r"""Gets the source_version_id of this ImportOpsDatasetItemsRequest.

        **参数解释：** 源版本ID。用于指定在数据还原或复制操作中作为参考的基础版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。

        :return: The source_version_id of this ImportOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._source_version_id

    @source_version_id.setter
    def source_version_id(self, source_version_id):
        r"""Sets the source_version_id of this ImportOpsDatasetItemsRequest.

        **参数解释：** 源版本ID。用于指定在数据还原或复制操作中作为参考的基础版本。 **约束限制：** 长度为0到100个字符。 **取值范围：** 0到100字符。 **默认取值：** 不涉及。

        :param source_version_id: The source_version_id of this ImportOpsDatasetItemsRequest.
        :type source_version_id: str
        """
        self._source_version_id = source_version_id

    @property
    def overwrite(self):
        r"""Gets the overwrite of this ImportOpsDatasetItemsRequest.

        **参数解释：** 覆盖模式开关。决定在导入新数据前是否清空草稿版本中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - `true`: 覆盖模式，执行清空操作。 - `false`: 追加模式，保留现有数据。 **默认取值：** false。

        :return: The overwrite of this ImportOpsDatasetItemsRequest.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        r"""Sets the overwrite of this ImportOpsDatasetItemsRequest.

        **参数解释：** 覆盖模式开关。决定在导入新数据前是否清空草稿版本中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - `true`: 覆盖模式，执行清空操作。 - `false`: 追加模式，保留现有数据。 **默认取值：** false。

        :param overwrite: The overwrite of this ImportOpsDatasetItemsRequest.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def get_obs_url(self):
        r"""Gets the get_obs_url of this ImportOpsDatasetItemsRequest.

        **参数解释：** 获取OBS预签名URL标识。用于确定是否需要系统生成并返回用于大文件直传的临时上传链接。 **约束限制：** 仅在不使用 multipart/form-data 模式时启用。 **取值范围：** true, false。 **默认取值：** false。

        :return: The get_obs_url of this ImportOpsDatasetItemsRequest.
        :rtype: bool
        """
        return self._get_obs_url

    @get_obs_url.setter
    def get_obs_url(self, get_obs_url):
        r"""Sets the get_obs_url of this ImportOpsDatasetItemsRequest.

        **参数解释：** 获取OBS预签名URL标识。用于确定是否需要系统生成并返回用于大文件直传的临时上传链接。 **约束限制：** 仅在不使用 multipart/form-data 模式时启用。 **取值范围：** true, false。 **默认取值：** false。

        :param get_obs_url: The get_obs_url of this ImportOpsDatasetItemsRequest.
        :type get_obs_url: bool
        """
        self._get_obs_url = get_obs_url

    @property
    def obs_object_name(self):
        r"""Gets the obs_object_name of this ImportOpsDatasetItemsRequest.

        **参数解释：** OBS对象名称。指定待导入文件在对象存储（OBS）中的完整存储路径或文件名。 **约束限制：** 字符串长度限制为0到10000个字符。 **取值范围：** 0到10000 字符。 **默认取值：** 不涉及。

        :return: The obs_object_name of this ImportOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._obs_object_name

    @obs_object_name.setter
    def obs_object_name(self, obs_object_name):
        r"""Sets the obs_object_name of this ImportOpsDatasetItemsRequest.

        **参数解释：** OBS对象名称。指定待导入文件在对象存储（OBS）中的完整存储路径或文件名。 **约束限制：** 字符串长度限制为0到10000个字符。 **取值范围：** 0到10000 字符。 **默认取值：** 不涉及。

        :param obs_object_name: The obs_object_name of this ImportOpsDatasetItemsRequest.
        :type obs_object_name: str
        """
        self._obs_object_name = obs_object_name

    @property
    def obs_file_hash(self):
        r"""Gets the obs_file_hash of this ImportOpsDatasetItemsRequest.

        **参数解释：** 文件哈希值（SHA-256）。用于在服务端进行文件完整性校验，确保上传过程中数据未损坏或被篡改。 **约束限制：** 十六进制字符串，最大长度 256 个字符。 **取值范围：** 0到256字符。 **默认取值：** 不涉及。

        :return: The obs_file_hash of this ImportOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._obs_file_hash

    @obs_file_hash.setter
    def obs_file_hash(self, obs_file_hash):
        r"""Sets the obs_file_hash of this ImportOpsDatasetItemsRequest.

        **参数解释：** 文件哈希值（SHA-256）。用于在服务端进行文件完整性校验，确保上传过程中数据未损坏或被篡改。 **约束限制：** 十六进制字符串，最大长度 256 个字符。 **取值范围：** 0到256字符。 **默认取值：** 不涉及。

        :param obs_file_hash: The obs_file_hash of this ImportOpsDatasetItemsRequest.
        :type obs_file_hash: str
        """
        self._obs_file_hash = obs_file_hash

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportOpsDatasetItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
