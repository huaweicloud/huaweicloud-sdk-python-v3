# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSeedDataCreateConfig:

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
        'dataset_version_id': 'str',
        'file_name': 'str',
        'obs_tmp_file_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'dataset_id': 'dataset_id',
        'dataset_version_id': 'dataset_version_id',
        'file_name': 'file_name',
        'obs_tmp_file_id': 'obs_tmp_file_id'
    }

    def __init__(self, type=None, dataset_id=None, dataset_version_id=None, file_name=None, obs_tmp_file_id=None):
        r"""EvaluationOpsSeedDataCreateConfig

        The model defined in huaweicloud sdk

        :param type: **参数解释：**   指定种子数据的来源类型。 **约束限制：**   枚举值。 **取值范围：**   字符长度1-100，dataset(平台评测集),file(本地上传文件)。 **默认取值：**   不涉及。 
        :type type: str
        :param dataset_id: **参数解释：**   种子评测集的唯一标识符，通过数据集列表接口获取。 **约束限制：**   0-64个字符；当type为dataset时必填。 **取值范围：**   字符长度0-64，已存在的评测集ID。 **默认取值：**   不涉及。 
        :type dataset_id: str
        :param dataset_version_id: **参数解释：**   指定种子评测集的具体版本标识。 **约束限制：**   0-64个字符。 **取值范围：**   已发布或草稿版本的ID。 **默认取值：**   指向草稿版本。 
        :type dataset_version_id: str
        :param file_name: **参数解释：**   上传的种子数据文件的原始名称。 **约束限制：**   1-200个字符，当type为file时必填。 **取值范围：**   1-200个字符，合法的文件名。 **默认取值：**   不涉及。 
        :type file_name: str
        :param obs_tmp_file_id: **参数解释：**   种子数据文件在OBS中的临时存储路径。 **约束限制：**   最大长度10000字符。 **取值范围：**   OBS路径字符串。 **默认取值：**   不涉及。 
        :type obs_tmp_file_id: str
        """
        
        

        self._type = None
        self._dataset_id = None
        self._dataset_version_id = None
        self._file_name = None
        self._obs_tmp_file_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_version_id is not None:
            self.dataset_version_id = dataset_version_id
        if file_name is not None:
            self.file_name = file_name
        if obs_tmp_file_id is not None:
            self.obs_tmp_file_id = obs_tmp_file_id

    @property
    def type(self):
        r"""Gets the type of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   指定种子数据的来源类型。 **约束限制：**   枚举值。 **取值范围：**   字符长度1-100，dataset(平台评测集),file(本地上传文件)。 **默认取值：**   不涉及。 

        :return: The type of this EvaluationOpsSeedDataCreateConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   指定种子数据的来源类型。 **约束限制：**   枚举值。 **取值范围：**   字符长度1-100，dataset(平台评测集),file(本地上传文件)。 **默认取值：**   不涉及。 

        :param type: The type of this EvaluationOpsSeedDataCreateConfig.
        :type type: str
        """
        self._type = type

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   种子评测集的唯一标识符，通过数据集列表接口获取。 **约束限制：**   0-64个字符；当type为dataset时必填。 **取值范围：**   字符长度0-64，已存在的评测集ID。 **默认取值：**   不涉及。 

        :return: The dataset_id of this EvaluationOpsSeedDataCreateConfig.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   种子评测集的唯一标识符，通过数据集列表接口获取。 **约束限制：**   0-64个字符；当type为dataset时必填。 **取值范围：**   字符长度0-64，已存在的评测集ID。 **默认取值：**   不涉及。 

        :param dataset_id: The dataset_id of this EvaluationOpsSeedDataCreateConfig.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_version_id(self):
        r"""Gets the dataset_version_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   指定种子评测集的具体版本标识。 **约束限制：**   0-64个字符。 **取值范围：**   已发布或草稿版本的ID。 **默认取值：**   指向草稿版本。 

        :return: The dataset_version_id of this EvaluationOpsSeedDataCreateConfig.
        :rtype: str
        """
        return self._dataset_version_id

    @dataset_version_id.setter
    def dataset_version_id(self, dataset_version_id):
        r"""Sets the dataset_version_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   指定种子评测集的具体版本标识。 **约束限制：**   0-64个字符。 **取值范围：**   已发布或草稿版本的ID。 **默认取值：**   指向草稿版本。 

        :param dataset_version_id: The dataset_version_id of this EvaluationOpsSeedDataCreateConfig.
        :type dataset_version_id: str
        """
        self._dataset_version_id = dataset_version_id

    @property
    def file_name(self):
        r"""Gets the file_name of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   上传的种子数据文件的原始名称。 **约束限制：**   1-200个字符，当type为file时必填。 **取值范围：**   1-200个字符，合法的文件名。 **默认取值：**   不涉及。 

        :return: The file_name of this EvaluationOpsSeedDataCreateConfig.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   上传的种子数据文件的原始名称。 **约束限制：**   1-200个字符，当type为file时必填。 **取值范围：**   1-200个字符，合法的文件名。 **默认取值：**   不涉及。 

        :param file_name: The file_name of this EvaluationOpsSeedDataCreateConfig.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def obs_tmp_file_id(self):
        r"""Gets the obs_tmp_file_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   种子数据文件在OBS中的临时存储路径。 **约束限制：**   最大长度10000字符。 **取值范围：**   OBS路径字符串。 **默认取值：**   不涉及。 

        :return: The obs_tmp_file_id of this EvaluationOpsSeedDataCreateConfig.
        :rtype: str
        """
        return self._obs_tmp_file_id

    @obs_tmp_file_id.setter
    def obs_tmp_file_id(self, obs_tmp_file_id):
        r"""Sets the obs_tmp_file_id of this EvaluationOpsSeedDataCreateConfig.

        **参数解释：**   种子数据文件在OBS中的临时存储路径。 **约束限制：**   最大长度10000字符。 **取值范围：**   OBS路径字符串。 **默认取值：**   不涉及。 

        :param obs_tmp_file_id: The obs_tmp_file_id of this EvaluationOpsSeedDataCreateConfig.
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
        if not isinstance(other, EvaluationOpsSeedDataCreateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
