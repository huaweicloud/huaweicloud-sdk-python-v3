# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsDatasetInfo:

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
        'version': 'str',
        'version_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'version_name': 'version_name'
    }

    def __init__(self, id=None, version=None, version_name=None):
        r"""OpsDatasetInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 数据集ID，标识已创建的训练数据集。  **取值范围：** 真实存在的数据集ID字符串。
        :type id: str
        :param version: **参数解释：** 数据集版本号。  **取值范围：** 版本号字符串。
        :type version: str
        :param version_name: **参数解释：** 版本显示名称。  **取值范围：** 版本显示名称字符串。
        :type version_name: str
        """
        
        

        self._id = None
        self._version = None
        self._version_name = None
        self.discriminator = None

        self.id = id
        self.version = version
        if version_name is not None:
            self.version_name = version_name

    @property
    def id(self):
        r"""Gets the id of this OpsDatasetInfo.

        **参数解释：** 数据集ID，标识已创建的训练数据集。  **取值范围：** 真实存在的数据集ID字符串。

        :return: The id of this OpsDatasetInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsDatasetInfo.

        **参数解释：** 数据集ID，标识已创建的训练数据集。  **取值范围：** 真实存在的数据集ID字符串。

        :param id: The id of this OpsDatasetInfo.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this OpsDatasetInfo.

        **参数解释：** 数据集版本号。  **取值范围：** 版本号字符串。

        :return: The version of this OpsDatasetInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OpsDatasetInfo.

        **参数解释：** 数据集版本号。  **取值范围：** 版本号字符串。

        :param version: The version of this OpsDatasetInfo.
        :type version: str
        """
        self._version = version

    @property
    def version_name(self):
        r"""Gets the version_name of this OpsDatasetInfo.

        **参数解释：** 版本显示名称。  **取值范围：** 版本显示名称字符串。

        :return: The version_name of this OpsDatasetInfo.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this OpsDatasetInfo.

        **参数解释：** 版本显示名称。  **取值范围：** 版本显示名称字符串。

        :param version_name: The version_name of this OpsDatasetInfo.
        :type version_name: str
        """
        self._version_name = version_name

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
        if not isinstance(other, OpsDatasetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
