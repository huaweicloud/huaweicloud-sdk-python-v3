# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputDataInfoRespDataset:

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
        'version_id': 'str',
        'obs_url': 'str',
        'service_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id',
        'obs_url': 'obs_url',
        'service_type': 'service_type',
        'name': 'name'
    }

    def __init__(self, id=None, version_id=None, obs_url=None, service_type=None, name=None):
        r"""InputDataInfoRespDataset

        The model defined in huaweicloud sdk

        :param id: **参数解释**：训练作业的数据集ID。 **取值范围**：不涉及。
        :type id: str
        :param version_id: **参数解释**：训练作业的数据集版本ID。 **约束限制**：使用旧版数据集即service_type不为V3时必填。 **取值范围**：不涉及。
        :type version_id: str
        :param obs_url: **参数解释**：训练作业需要的数据集OBS路径URL，ModelArts会通过数据集ID和数据集版本ID自动解析生成。如：“/usr/data/”。 **取值范围**：不涉及。
        :type obs_url: str
        :param service_type: **参数解释**：数据集服务类型。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：取值为V3时表示使用的是资产服务提供的数据集，其他表示旧版数据集。
        :type service_type: str
        :param name: **参数解释**：训练作业的数据集名称。 **取值范围**：不涉及。
        :type name: str
        """
        
        

        self._id = None
        self._version_id = None
        self._obs_url = None
        self._service_type = None
        self._name = None
        self.discriminator = None

        self.id = id
        if version_id is not None:
            self.version_id = version_id
        if obs_url is not None:
            self.obs_url = obs_url
        if service_type is not None:
            self.service_type = service_type
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集ID。 **取值范围**：不涉及。

        :return: The id of this InputDataInfoRespDataset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集ID。 **取值范围**：不涉及。

        :param id: The id of this InputDataInfoRespDataset.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        r"""Gets the version_id of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集版本ID。 **约束限制**：使用旧版数据集即service_type不为V3时必填。 **取值范围**：不涉及。

        :return: The version_id of this InputDataInfoRespDataset.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集版本ID。 **约束限制**：使用旧版数据集即service_type不为V3时必填。 **取值范围**：不涉及。

        :param version_id: The version_id of this InputDataInfoRespDataset.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def obs_url(self):
        r"""Gets the obs_url of this InputDataInfoRespDataset.

        **参数解释**：训练作业需要的数据集OBS路径URL，ModelArts会通过数据集ID和数据集版本ID自动解析生成。如：“/usr/data/”。 **取值范围**：不涉及。

        :return: The obs_url of this InputDataInfoRespDataset.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this InputDataInfoRespDataset.

        **参数解释**：训练作业需要的数据集OBS路径URL，ModelArts会通过数据集ID和数据集版本ID自动解析生成。如：“/usr/data/”。 **取值范围**：不涉及。

        :param obs_url: The obs_url of this InputDataInfoRespDataset.
        :type obs_url: str
        """
        self._obs_url = obs_url

    @property
    def service_type(self):
        r"""Gets the service_type of this InputDataInfoRespDataset.

        **参数解释**：数据集服务类型。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：取值为V3时表示使用的是资产服务提供的数据集，其他表示旧版数据集。

        :return: The service_type of this InputDataInfoRespDataset.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this InputDataInfoRespDataset.

        **参数解释**：数据集服务类型。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：取值为V3时表示使用的是资产服务提供的数据集，其他表示旧版数据集。

        :param service_type: The service_type of this InputDataInfoRespDataset.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def name(self):
        r"""Gets the name of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集名称。 **取值范围**：不涉及。

        :return: The name of this InputDataInfoRespDataset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InputDataInfoRespDataset.

        **参数解释**：训练作业的数据集名称。 **取值范围**：不涉及。

        :param name: The name of this InputDataInfoRespDataset.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, InputDataInfoRespDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
