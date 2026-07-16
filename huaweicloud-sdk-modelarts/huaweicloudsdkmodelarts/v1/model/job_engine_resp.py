# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEngineResp:

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
        'install_sys_packages': 'bool'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'image_url': 'image_url',
        'install_sys_packages': 'install_sys_packages'
    }

    def __init__(self, engine_id=None, engine_name=None, engine_version=None, image_url=None, install_sys_packages=None):
        r"""JobEngineResp

        The model defined in huaweicloud sdk

        :param engine_id: **参数解释**：训练作业选择的引擎规格ID。 **取值范围**：不涉及。
        :type engine_id: str
        :param engine_name: **参数解释**：训练作业选择的引擎规格名称。 **取值范围**：不涉及。
        :type engine_name: str
        :param engine_version: **参数解释**：训练作业选择的引擎规格版本。 **取值范围**：不涉及。
        :type engine_version: str
        :param image_url: **参数解释**：训练作业选择的自定义镜像地址，地址从swr服务获取。 **取值范围**：不涉及。
        :type image_url: str
        :param install_sys_packages: **参数解释**：是否需要安装训练平台指定的 moxing 版本。 **取值范围**： - true：需要 - false：不需要
        :type install_sys_packages: bool
        """
        
        

        self._engine_id = None
        self._engine_name = None
        self._engine_version = None
        self._image_url = None
        self._install_sys_packages = None
        self.discriminator = None

        if engine_id is not None:
            self.engine_id = engine_id
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if image_url is not None:
            self.image_url = image_url
        if install_sys_packages is not None:
            self.install_sys_packages = install_sys_packages

    @property
    def engine_id(self):
        r"""Gets the engine_id of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格ID。 **取值范围**：不涉及。

        :return: The engine_id of this JobEngineResp.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格ID。 **取值范围**：不涉及。

        :param engine_id: The engine_id of this JobEngineResp.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格名称。 **取值范围**：不涉及。

        :return: The engine_name of this JobEngineResp.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格名称。 **取值范围**：不涉及。

        :param engine_name: The engine_name of this JobEngineResp.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格版本。 **取值范围**：不涉及。

        :return: The engine_version of this JobEngineResp.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this JobEngineResp.

        **参数解释**：训练作业选择的引擎规格版本。 **取值范围**：不涉及。

        :param engine_version: The engine_version of this JobEngineResp.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def image_url(self):
        r"""Gets the image_url of this JobEngineResp.

        **参数解释**：训练作业选择的自定义镜像地址，地址从swr服务获取。 **取值范围**：不涉及。

        :return: The image_url of this JobEngineResp.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this JobEngineResp.

        **参数解释**：训练作业选择的自定义镜像地址，地址从swr服务获取。 **取值范围**：不涉及。

        :param image_url: The image_url of this JobEngineResp.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def install_sys_packages(self):
        r"""Gets the install_sys_packages of this JobEngineResp.

        **参数解释**：是否需要安装训练平台指定的 moxing 版本。 **取值范围**： - true：需要 - false：不需要

        :return: The install_sys_packages of this JobEngineResp.
        :rtype: bool
        """
        return self._install_sys_packages

    @install_sys_packages.setter
    def install_sys_packages(self, install_sys_packages):
        r"""Sets the install_sys_packages of this JobEngineResp.

        **参数解释**：是否需要安装训练平台指定的 moxing 版本。 **取值范围**： - true：需要 - false：不需要

        :param install_sys_packages: The install_sys_packages of this JobEngineResp.
        :type install_sys_packages: bool
        """
        self._install_sys_packages = install_sys_packages

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
        if not isinstance(other, JobEngineResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
