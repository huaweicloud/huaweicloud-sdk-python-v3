# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsDataset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version'
    }

    def __init__(self, id=None, version=None):
        r"""OpsDataset

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 数据集ID，标识已创建的训练数据集。可通过获取评测集列表接口查询，注意需要使用latest_version不为空的数据集，不为空即表示该数据集已经执行过发布。  **约束限制：** 不涉及  **取值范围：** 数据集ID，可通过[查询数据集列表](https://support.huaweicloud.com/api-agentarts/ListOpsDatasets.html)接口获取。  **默认取值：** 无
        :type id: str
        :param version: **参数解释：** 数据集版本。  **约束限制：** 不涉及  **取值范围：** 数据集版本号字符串。  **默认取值：** 无
        :type version: str
        """
        
        

        self._id = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.version = version

    @property
    def id(self):
        r"""Gets the id of this OpsDataset.

        **参数解释：** 数据集ID，标识已创建的训练数据集。可通过获取评测集列表接口查询，注意需要使用latest_version不为空的数据集，不为空即表示该数据集已经执行过发布。  **约束限制：** 不涉及  **取值范围：** 数据集ID，可通过[查询数据集列表](https://support.huaweicloud.com/api-agentarts/ListOpsDatasets.html)接口获取。  **默认取值：** 无

        :return: The id of this OpsDataset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsDataset.

        **参数解释：** 数据集ID，标识已创建的训练数据集。可通过获取评测集列表接口查询，注意需要使用latest_version不为空的数据集，不为空即表示该数据集已经执行过发布。  **约束限制：** 不涉及  **取值范围：** 数据集ID，可通过[查询数据集列表](https://support.huaweicloud.com/api-agentarts/ListOpsDatasets.html)接口获取。  **默认取值：** 无

        :param id: The id of this OpsDataset.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this OpsDataset.

        **参数解释：** 数据集版本。  **约束限制：** 不涉及  **取值范围：** 数据集版本号字符串。  **默认取值：** 无

        :return: The version of this OpsDataset.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OpsDataset.

        **参数解释：** 数据集版本。  **约束限制：** 不涉及  **取值范围：** 数据集版本号字符串。  **默认取值：** 无

        :param version: The version of this OpsDataset.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, OpsDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
