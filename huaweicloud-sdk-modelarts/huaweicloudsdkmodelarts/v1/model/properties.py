# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Properties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_num': 'int',
        'dataset_size': 'int',
        'prompt_config': 'str',
        'data_copyright': 'str',
        'manifest_file_path': 'str',
        'arguments': 'list[OperatorArgument]',
        'updater': 'str'
    }

    attribute_map = {
        'dataset_num': 'dataset_num',
        'dataset_size': 'dataset_size',
        'prompt_config': 'prompt_config',
        'data_copyright': 'data_copyright',
        'manifest_file_path': 'manifest_file_path',
        'arguments': 'arguments',
        'updater': 'updater'
    }

    def __init__(self, dataset_num=None, dataset_size=None, prompt_config=None, data_copyright=None, manifest_file_path=None, arguments=None, updater=None):
        r"""Properties

        The model defined in huaweicloud sdk

        :param dataset_num: **参数解释**：数据集的条数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_num: int
        :param dataset_size: **参数解释**：数据集资产资源文件总大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_size: int
        :param prompt_config: **参数解释**：数据集资产评测模版相对地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type prompt_config: str
        :param data_copyright: **参数解释**：数据集资产版权信息，包含数据集信息，License和地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type data_copyright: str
        :param manifest_file_path: **参数解释**：数据集资产索引文件地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type manifest_file_path: str
        :param arguments: **参数解释**：算子参数列表。 **约束限制**：不涉及。
        :type arguments: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgument`]
        :param updater: **参数解释**：数据集资产修改人信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type updater: str
        """
        
        

        self._dataset_num = None
        self._dataset_size = None
        self._prompt_config = None
        self._data_copyright = None
        self._manifest_file_path = None
        self._arguments = None
        self._updater = None
        self.discriminator = None

        if dataset_num is not None:
            self.dataset_num = dataset_num
        if dataset_size is not None:
            self.dataset_size = dataset_size
        if prompt_config is not None:
            self.prompt_config = prompt_config
        if data_copyright is not None:
            self.data_copyright = data_copyright
        if manifest_file_path is not None:
            self.manifest_file_path = manifest_file_path
        if arguments is not None:
            self.arguments = arguments
        if updater is not None:
            self.updater = updater

    @property
    def dataset_num(self):
        r"""Gets the dataset_num of this Properties.

        **参数解释**：数据集的条数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_num of this Properties.
        :rtype: int
        """
        return self._dataset_num

    @dataset_num.setter
    def dataset_num(self, dataset_num):
        r"""Sets the dataset_num of this Properties.

        **参数解释**：数据集的条数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_num: The dataset_num of this Properties.
        :type dataset_num: int
        """
        self._dataset_num = dataset_num

    @property
    def dataset_size(self):
        r"""Gets the dataset_size of this Properties.

        **参数解释**：数据集资产资源文件总大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_size of this Properties.
        :rtype: int
        """
        return self._dataset_size

    @dataset_size.setter
    def dataset_size(self, dataset_size):
        r"""Sets the dataset_size of this Properties.

        **参数解释**：数据集资产资源文件总大小。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_size: The dataset_size of this Properties.
        :type dataset_size: int
        """
        self._dataset_size = dataset_size

    @property
    def prompt_config(self):
        r"""Gets the prompt_config of this Properties.

        **参数解释**：数据集资产评测模版相对地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The prompt_config of this Properties.
        :rtype: str
        """
        return self._prompt_config

    @prompt_config.setter
    def prompt_config(self, prompt_config):
        r"""Sets the prompt_config of this Properties.

        **参数解释**：数据集资产评测模版相对地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param prompt_config: The prompt_config of this Properties.
        :type prompt_config: str
        """
        self._prompt_config = prompt_config

    @property
    def data_copyright(self):
        r"""Gets the data_copyright of this Properties.

        **参数解释**：数据集资产版权信息，包含数据集信息，License和地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The data_copyright of this Properties.
        :rtype: str
        """
        return self._data_copyright

    @data_copyright.setter
    def data_copyright(self, data_copyright):
        r"""Sets the data_copyright of this Properties.

        **参数解释**：数据集资产版权信息，包含数据集信息，License和地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param data_copyright: The data_copyright of this Properties.
        :type data_copyright: str
        """
        self._data_copyright = data_copyright

    @property
    def manifest_file_path(self):
        r"""Gets the manifest_file_path of this Properties.

        **参数解释**：数据集资产索引文件地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The manifest_file_path of this Properties.
        :rtype: str
        """
        return self._manifest_file_path

    @manifest_file_path.setter
    def manifest_file_path(self, manifest_file_path):
        r"""Sets the manifest_file_path of this Properties.

        **参数解释**：数据集资产索引文件地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param manifest_file_path: The manifest_file_path of this Properties.
        :type manifest_file_path: str
        """
        self._manifest_file_path = manifest_file_path

    @property
    def arguments(self):
        r"""Gets the arguments of this Properties.

        **参数解释**：算子参数列表。 **约束限制**：不涉及。

        :return: The arguments of this Properties.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgument`]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        r"""Sets the arguments of this Properties.

        **参数解释**：算子参数列表。 **约束限制**：不涉及。

        :param arguments: The arguments of this Properties.
        :type arguments: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgument`]
        """
        self._arguments = arguments

    @property
    def updater(self):
        r"""Gets the updater of this Properties.

        **参数解释**：数据集资产修改人信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The updater of this Properties.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this Properties.

        **参数解释**：数据集资产修改人信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param updater: The updater of this Properties.
        :type updater: str
        """
        self._updater = updater

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
        if not isinstance(other, Properties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
