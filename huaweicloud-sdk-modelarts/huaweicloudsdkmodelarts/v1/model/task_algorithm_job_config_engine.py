# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithmJobConfigEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'image_url': 'str',
        'run_user': 'str'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'image_url': 'image_url',
        'run_user': 'run_user'
    }

    def __init__(self, engine_id=None, engine_name=None, engine_version=None, image_url=None, run_user=None):
        r"""TaskAlgorithmJobConfigEngine

        The model defined in huaweicloud sdk

        :param engine_id: **参数解释**：算法选择的引擎规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type engine_id: str
        :param engine_name: **参数解释**：算法选择的引擎规格名称。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type engine_name: str
        :param engine_version: **参数解释**：算法选择的引擎规格版本。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type engine_version: str
        :param image_url: **参数解释**：算法选择的自定义镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type image_url: str
        :param run_user: **参数解释**：容器镜像启动用户，默认为1000，仅自定义镜像场景下支持配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type run_user: str
        """
        
        

        self._engine_id = None
        self._engine_name = None
        self._engine_version = None
        self._image_url = None
        self._run_user = None
        self.discriminator = None

        if engine_id is not None:
            self.engine_id = engine_id
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if image_url is not None:
            self.image_url = image_url
        if run_user is not None:
            self.run_user = run_user

    @property
    def engine_id(self):
        r"""Gets the engine_id of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The engine_id of this TaskAlgorithmJobConfigEngine.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param engine_id: The engine_id of this TaskAlgorithmJobConfigEngine.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格名称。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The engine_name of this TaskAlgorithmJobConfigEngine.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格名称。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param engine_name: The engine_name of this TaskAlgorithmJobConfigEngine.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格版本。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The engine_version of this TaskAlgorithmJobConfigEngine.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的引擎规格版本。 **约束限制**：若填入engine_id则无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param engine_version: The engine_version of this TaskAlgorithmJobConfigEngine.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def image_url(self):
        r"""Gets the image_url of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的自定义镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The image_url of this TaskAlgorithmJobConfigEngine.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this TaskAlgorithmJobConfigEngine.

        **参数解释**：算法选择的自定义镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param image_url: The image_url of this TaskAlgorithmJobConfigEngine.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def run_user(self):
        r"""Gets the run_user of this TaskAlgorithmJobConfigEngine.

        **参数解释**：容器镜像启动用户，默认为1000，仅自定义镜像场景下支持配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The run_user of this TaskAlgorithmJobConfigEngine.
        :rtype: str
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        r"""Sets the run_user of this TaskAlgorithmJobConfigEngine.

        **参数解释**：容器镜像启动用户，默认为1000，仅自定义镜像场景下支持配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param run_user: The run_user of this TaskAlgorithmJobConfigEngine.
        :type run_user: str
        """
        self._run_user = run_user

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
        if not isinstance(other, TaskAlgorithmJobConfigEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
