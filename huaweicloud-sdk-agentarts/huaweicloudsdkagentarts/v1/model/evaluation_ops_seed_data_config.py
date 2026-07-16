# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSeedDataConfig:

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
        'dataset_id': 'str',
        'dataset_name': 'str',
        'dataset_version_id': 'str',
        'dataset_version': 'str',
        'file_name': 'str',
        'obs_tmp_file_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'dataset_id': 'dataset_id',
        'dataset_name': 'dataset_name',
        'dataset_version_id': 'dataset_version_id',
        'dataset_version': 'dataset_version',
        'file_name': 'file_name',
        'obs_tmp_file_id': 'obs_tmp_file_id'
    }

    def __init__(self, type=None, dataset_id=None, dataset_name=None, dataset_version_id=None, dataset_version=None, file_name=None, obs_tmp_file_id=None):
        r"""EvaluationOpsSeedDataConfig

        The model defined in huaweicloud sdk

        :param type: **参数解释：**   种子数据的来源类型。 **取值范围：**   dataset(评测集)，file(文件)。 
        :type type: str
        :param dataset_id: **参数解释：**   种子评测集的唯一ID。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 
        :type dataset_id: str
        :param dataset_name: **参数解释：**   种子评测集的展示名称。 **取值范围：**   任意字符串。 
        :type dataset_name: str
        :param dataset_version_id: **参数解释：**   种子评测集版本的内部唯一标识符。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 
        :type dataset_version_id: str
        :param dataset_version: **参数解释：**   种子评测集的可读版本号。 **取值范围：**   如0.0.1。 
        :type dataset_version: str
        :param file_name: **参数解释：**   作为种子源的临时文件名称。 **取值范围：**   文件名。 
        :type file_name: str
        :param obs_tmp_file_id: **参数解释：**   种子数据文件在对象存储中的路径。 **取值范围：**   OBS路径。 
        :type obs_tmp_file_id: str
        """
        
        

        self._type = None
        self._dataset_id = None
        self._dataset_name = None
        self._dataset_version_id = None
        self._dataset_version = None
        self._file_name = None
        self._obs_tmp_file_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_version_id is not None:
            self.dataset_version_id = dataset_version_id
        if dataset_version is not None:
            self.dataset_version = dataset_version
        if file_name is not None:
            self.file_name = file_name
        if obs_tmp_file_id is not None:
            self.obs_tmp_file_id = obs_tmp_file_id

    @property
    def type(self):
        r"""Gets the type of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子数据的来源类型。 **取值范围：**   dataset(评测集)，file(文件)。 

        :return: The type of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子数据的来源类型。 **取值范围：**   dataset(评测集)，file(文件)。 

        :param type: The type of this EvaluationOpsSeedDataConfig.
        :type type: str
        """
        self._type = type

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的唯一ID。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 

        :return: The dataset_id of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的唯一ID。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 

        :param dataset_id: The dataset_id of this EvaluationOpsSeedDataConfig.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的展示名称。 **取值范围：**   任意字符串。 

        :return: The dataset_name of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的展示名称。 **取值范围：**   任意字符串。 

        :param dataset_name: The dataset_name of this EvaluationOpsSeedDataConfig.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def dataset_version_id(self):
        r"""Gets the dataset_version_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集版本的内部唯一标识符。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 

        :return: The dataset_version_id of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._dataset_version_id

    @dataset_version_id.setter
    def dataset_version_id(self, dataset_version_id):
        r"""Sets the dataset_version_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集版本的内部唯一标识符。 **取值范围：**   符合通用唯一识别码(UUID)标准的字符串。 

        :param dataset_version_id: The dataset_version_id of this EvaluationOpsSeedDataConfig.
        :type dataset_version_id: str
        """
        self._dataset_version_id = dataset_version_id

    @property
    def dataset_version(self):
        r"""Gets the dataset_version of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的可读版本号。 **取值范围：**   如0.0.1。 

        :return: The dataset_version of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._dataset_version

    @dataset_version.setter
    def dataset_version(self, dataset_version):
        r"""Sets the dataset_version of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子评测集的可读版本号。 **取值范围：**   如0.0.1。 

        :param dataset_version: The dataset_version of this EvaluationOpsSeedDataConfig.
        :type dataset_version: str
        """
        self._dataset_version = dataset_version

    @property
    def file_name(self):
        r"""Gets the file_name of this EvaluationOpsSeedDataConfig.

        **参数解释：**   作为种子源的临时文件名称。 **取值范围：**   文件名。 

        :return: The file_name of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this EvaluationOpsSeedDataConfig.

        **参数解释：**   作为种子源的临时文件名称。 **取值范围：**   文件名。 

        :param file_name: The file_name of this EvaluationOpsSeedDataConfig.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def obs_tmp_file_id(self):
        r"""Gets the obs_tmp_file_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子数据文件在对象存储中的路径。 **取值范围：**   OBS路径。 

        :return: The obs_tmp_file_id of this EvaluationOpsSeedDataConfig.
        :rtype: str
        """
        return self._obs_tmp_file_id

    @obs_tmp_file_id.setter
    def obs_tmp_file_id(self, obs_tmp_file_id):
        r"""Sets the obs_tmp_file_id of this EvaluationOpsSeedDataConfig.

        **参数解释：**   种子数据文件在对象存储中的路径。 **取值范围：**   OBS路径。 

        :param obs_tmp_file_id: The obs_tmp_file_id of this EvaluationOpsSeedDataConfig.
        :type obs_tmp_file_id: str
        """
        self._obs_tmp_file_id = obs_tmp_file_id

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
        if not isinstance(other, EvaluationOpsSeedDataConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
