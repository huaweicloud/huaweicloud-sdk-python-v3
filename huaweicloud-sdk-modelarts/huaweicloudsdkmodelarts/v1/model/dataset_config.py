# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_name': 'str',
        'dataset_source': 'str',
        'dataset_id': 'str',
        'split_ratio': 'int',
        'used_step': 'str',
        'dataset_proportion': 'int'
    }

    attribute_map = {
        'dataset_name': 'dataset_name',
        'dataset_source': 'dataset_source',
        'dataset_id': 'dataset_id',
        'split_ratio': 'split_ratio',
        'used_step': 'used_step',
        'dataset_proportion': 'dataset_proportion'
    }

    def __init__(self, dataset_name=None, dataset_source=None, dataset_id=None, split_ratio=None, used_step=None, dataset_proportion=None):
        r"""DatasetConfig

        The model defined in huaweicloud sdk

        :param dataset_name: 训练数据集名称，取自数据集列表接口响应体name。
        :type dataset_name: str
        :param dataset_source: 所使用的数据集来源，取值datamng|OBS|DB,分别表示来自于数据工程|OBS|数据库
        :type dataset_source: str
        :param dataset_id: 训练数据集id，取自数据集列表接口响应体dataset_id。
        :type dataset_id: str
        :param split_ratio: 训练、验证数据集分割比率，当该模型支持验证集且验证集来自选择的训练集时使用，取值大于等于1，小于等于50。
        :type split_ratio: int
        :param used_step: 数据集使用的阶段，取值为train|eval|test，分别表示该数据集用于训练|验证|测试。
        :type used_step: str
        :param dataset_proportion: 数据集配比比率，表示使用多少比率的该数据集进行训练。
        :type dataset_proportion: int
        """
        
        

        self._dataset_name = None
        self._dataset_source = None
        self._dataset_id = None
        self._split_ratio = None
        self._used_step = None
        self._dataset_proportion = None
        self.discriminator = None

        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset_source is not None:
            self.dataset_source = dataset_source
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if split_ratio is not None:
            self.split_ratio = split_ratio
        if used_step is not None:
            self.used_step = used_step
        if dataset_proportion is not None:
            self.dataset_proportion = dataset_proportion

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this DatasetConfig.

        训练数据集名称，取自数据集列表接口响应体name。

        :return: The dataset_name of this DatasetConfig.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this DatasetConfig.

        训练数据集名称，取自数据集列表接口响应体name。

        :param dataset_name: The dataset_name of this DatasetConfig.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def dataset_source(self):
        r"""Gets the dataset_source of this DatasetConfig.

        所使用的数据集来源，取值datamng|OBS|DB,分别表示来自于数据工程|OBS|数据库

        :return: The dataset_source of this DatasetConfig.
        :rtype: str
        """
        return self._dataset_source

    @dataset_source.setter
    def dataset_source(self, dataset_source):
        r"""Sets the dataset_source of this DatasetConfig.

        所使用的数据集来源，取值datamng|OBS|DB,分别表示来自于数据工程|OBS|数据库

        :param dataset_source: The dataset_source of this DatasetConfig.
        :type dataset_source: str
        """
        self._dataset_source = dataset_source

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this DatasetConfig.

        训练数据集id，取自数据集列表接口响应体dataset_id。

        :return: The dataset_id of this DatasetConfig.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this DatasetConfig.

        训练数据集id，取自数据集列表接口响应体dataset_id。

        :param dataset_id: The dataset_id of this DatasetConfig.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def split_ratio(self):
        r"""Gets the split_ratio of this DatasetConfig.

        训练、验证数据集分割比率，当该模型支持验证集且验证集来自选择的训练集时使用，取值大于等于1，小于等于50。

        :return: The split_ratio of this DatasetConfig.
        :rtype: int
        """
        return self._split_ratio

    @split_ratio.setter
    def split_ratio(self, split_ratio):
        r"""Sets the split_ratio of this DatasetConfig.

        训练、验证数据集分割比率，当该模型支持验证集且验证集来自选择的训练集时使用，取值大于等于1，小于等于50。

        :param split_ratio: The split_ratio of this DatasetConfig.
        :type split_ratio: int
        """
        self._split_ratio = split_ratio

    @property
    def used_step(self):
        r"""Gets the used_step of this DatasetConfig.

        数据集使用的阶段，取值为train|eval|test，分别表示该数据集用于训练|验证|测试。

        :return: The used_step of this DatasetConfig.
        :rtype: str
        """
        return self._used_step

    @used_step.setter
    def used_step(self, used_step):
        r"""Sets the used_step of this DatasetConfig.

        数据集使用的阶段，取值为train|eval|test，分别表示该数据集用于训练|验证|测试。

        :param used_step: The used_step of this DatasetConfig.
        :type used_step: str
        """
        self._used_step = used_step

    @property
    def dataset_proportion(self):
        r"""Gets the dataset_proportion of this DatasetConfig.

        数据集配比比率，表示使用多少比率的该数据集进行训练。

        :return: The dataset_proportion of this DatasetConfig.
        :rtype: int
        """
        return self._dataset_proportion

    @dataset_proportion.setter
    def dataset_proportion(self, dataset_proportion):
        r"""Sets the dataset_proportion of this DatasetConfig.

        数据集配比比率，表示使用多少比率的该数据集进行训练。

        :param dataset_proportion: The dataset_proportion of this DatasetConfig.
        :type dataset_proportion: int
        """
        self._dataset_proportion = dataset_proportion

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
        if not isinstance(other, DatasetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
