# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDevServerJobTemplateResponse(SdkResponse):

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
        'name': 'str',
        'description': 'str',
        'cmd': 'str',
        'swr_path': 'str',
        'resources': 'str',
        'volumes': 'str',
        'volumes_mount': 'str',
        'flavor_type': 'str',
        'timeout': 'str',
        'check_interval': 'str',
        'type': 'str',
        'status': 'str',
        'params': 'list[TemplateParam]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cmd': 'cmd',
        'swr_path': 'swr_path',
        'resources': 'resources',
        'volumes': 'volumes',
        'volumes_mount': 'volumes_mount',
        'flavor_type': 'flavor_type',
        'timeout': 'timeout',
        'check_interval': 'check_interval',
        'type': 'type',
        'status': 'status',
        'params': 'params'
    }

    def __init__(self, id=None, name=None, description=None, cmd=None, swr_path=None, resources=None, volumes=None, volumes_mount=None, flavor_type=None, timeout=None, check_interval=None, type=None, status=None, params=None):
        r"""GetDevServerJobTemplateResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：模板id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：模板名称。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：模板描述。 **取值范围**：不涉及。
        :type description: str
        :param cmd: **参数解释**：容器启动命令。 **取值范围**：不涉及。
        :type cmd: str
        :param swr_path: **参数解释**：任务镜像。 **取值范围**：不涉及。
        :type swr_path: str
        :param resources: **参数解释**：任务规格。 **取值范围**：不涉及。
        :type resources: str
        :param volumes: **参数解释**：卷。 **取值范围**：不涉及。
        :type volumes: str
        :param volumes_mount: **参数解释**：卷挂载。 **取值范围**：不涉及。
        :type volumes_mount: str
        :param flavor_type: **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。
        :type flavor_type: str
        :param timeout: **参数解释**：任务超时时间。 **取值范围**：不涉及。
        :type timeout: str
        :param check_interval: **参数解释**：任务的轮询周期。 **取值范围**：不涉及。
        :type check_interval: str
        :param type: **参数解释**：任务类型。 **取值范围**：-LOG_COLLECT  -COMMON 等
        :type type: str
        :param status: **参数解释**：模板状态。 **取值范围**：ACTIVE。
        :type status: str
        :param params: **参数解释**：模板的其他参数。
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._cmd = None
        self._swr_path = None
        self._resources = None
        self._volumes = None
        self._volumes_mount = None
        self._flavor_type = None
        self._timeout = None
        self._check_interval = None
        self._type = None
        self._status = None
        self._params = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cmd is not None:
            self.cmd = cmd
        if swr_path is not None:
            self.swr_path = swr_path
        if resources is not None:
            self.resources = resources
        if volumes is not None:
            self.volumes = volumes
        if volumes_mount is not None:
            self.volumes_mount = volumes_mount
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if timeout is not None:
            self.timeout = timeout
        if check_interval is not None:
            self.check_interval = check_interval
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if params is not None:
            self.params = params

    @property
    def id(self):
        r"""Gets the id of this GetDevServerJobTemplateResponse.

        **参数解释**：模板id。 **取值范围**：不涉及。

        :return: The id of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetDevServerJobTemplateResponse.

        **参数解释**：模板id。 **取值范围**：不涉及。

        :param id: The id of this GetDevServerJobTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetDevServerJobTemplateResponse.

        **参数解释**：模板名称。 **取值范围**：不涉及。

        :return: The name of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDevServerJobTemplateResponse.

        **参数解释**：模板名称。 **取值范围**：不涉及。

        :param name: The name of this GetDevServerJobTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this GetDevServerJobTemplateResponse.

        **参数解释**：模板描述。 **取值范围**：不涉及。

        :return: The description of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GetDevServerJobTemplateResponse.

        **参数解释**：模板描述。 **取值范围**：不涉及。

        :param description: The description of this GetDevServerJobTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def cmd(self):
        r"""Gets the cmd of this GetDevServerJobTemplateResponse.

        **参数解释**：容器启动命令。 **取值范围**：不涉及。

        :return: The cmd of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this GetDevServerJobTemplateResponse.

        **参数解释**：容器启动命令。 **取值范围**：不涉及。

        :param cmd: The cmd of this GetDevServerJobTemplateResponse.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def swr_path(self):
        r"""Gets the swr_path of this GetDevServerJobTemplateResponse.

        **参数解释**：任务镜像。 **取值范围**：不涉及。

        :return: The swr_path of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._swr_path

    @swr_path.setter
    def swr_path(self, swr_path):
        r"""Sets the swr_path of this GetDevServerJobTemplateResponse.

        **参数解释**：任务镜像。 **取值范围**：不涉及。

        :param swr_path: The swr_path of this GetDevServerJobTemplateResponse.
        :type swr_path: str
        """
        self._swr_path = swr_path

    @property
    def resources(self):
        r"""Gets the resources of this GetDevServerJobTemplateResponse.

        **参数解释**：任务规格。 **取值范围**：不涉及。

        :return: The resources of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this GetDevServerJobTemplateResponse.

        **参数解释**：任务规格。 **取值范围**：不涉及。

        :param resources: The resources of this GetDevServerJobTemplateResponse.
        :type resources: str
        """
        self._resources = resources

    @property
    def volumes(self):
        r"""Gets the volumes of this GetDevServerJobTemplateResponse.

        **参数解释**：卷。 **取值范围**：不涉及。

        :return: The volumes of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this GetDevServerJobTemplateResponse.

        **参数解释**：卷。 **取值范围**：不涉及。

        :param volumes: The volumes of this GetDevServerJobTemplateResponse.
        :type volumes: str
        """
        self._volumes = volumes

    @property
    def volumes_mount(self):
        r"""Gets the volumes_mount of this GetDevServerJobTemplateResponse.

        **参数解释**：卷挂载。 **取值范围**：不涉及。

        :return: The volumes_mount of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._volumes_mount

    @volumes_mount.setter
    def volumes_mount(self, volumes_mount):
        r"""Sets the volumes_mount of this GetDevServerJobTemplateResponse.

        **参数解释**：卷挂载。 **取值范围**：不涉及。

        :param volumes_mount: The volumes_mount of this GetDevServerJobTemplateResponse.
        :type volumes_mount: str
        """
        self._volumes_mount = volumes_mount

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this GetDevServerJobTemplateResponse.

        **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。

        :return: The flavor_type of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this GetDevServerJobTemplateResponse.

        **参数解释**：规格类型。 **取值范围**：-ASCEND_SNT9B   -ASCEND_SNT9C   -ASCEND_GENERIC。

        :param flavor_type: The flavor_type of this GetDevServerJobTemplateResponse.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def timeout(self):
        r"""Gets the timeout of this GetDevServerJobTemplateResponse.

        **参数解释**：任务超时时间。 **取值范围**：不涉及。

        :return: The timeout of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this GetDevServerJobTemplateResponse.

        **参数解释**：任务超时时间。 **取值范围**：不涉及。

        :param timeout: The timeout of this GetDevServerJobTemplateResponse.
        :type timeout: str
        """
        self._timeout = timeout

    @property
    def check_interval(self):
        r"""Gets the check_interval of this GetDevServerJobTemplateResponse.

        **参数解释**：任务的轮询周期。 **取值范围**：不涉及。

        :return: The check_interval of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._check_interval

    @check_interval.setter
    def check_interval(self, check_interval):
        r"""Sets the check_interval of this GetDevServerJobTemplateResponse.

        **参数解释**：任务的轮询周期。 **取值范围**：不涉及。

        :param check_interval: The check_interval of this GetDevServerJobTemplateResponse.
        :type check_interval: str
        """
        self._check_interval = check_interval

    @property
    def type(self):
        r"""Gets the type of this GetDevServerJobTemplateResponse.

        **参数解释**：任务类型。 **取值范围**：-LOG_COLLECT  -COMMON 等

        :return: The type of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GetDevServerJobTemplateResponse.

        **参数解释**：任务类型。 **取值范围**：-LOG_COLLECT  -COMMON 等

        :param type: The type of this GetDevServerJobTemplateResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this GetDevServerJobTemplateResponse.

        **参数解释**：模板状态。 **取值范围**：ACTIVE。

        :return: The status of this GetDevServerJobTemplateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetDevServerJobTemplateResponse.

        **参数解释**：模板状态。 **取值范围**：ACTIVE。

        :param status: The status of this GetDevServerJobTemplateResponse.
        :type status: str
        """
        self._status = status

    @property
    def params(self):
        r"""Gets the params of this GetDevServerJobTemplateResponse.

        **参数解释**：模板的其他参数。

        :return: The params of this GetDevServerJobTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this GetDevServerJobTemplateResponse.

        **参数解释**：模板的其他参数。

        :param params: The params of this GetDevServerJobTemplateResponse.
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.TemplateParam`]
        """
        self._params = params

    def to_dict(self):
        import warnings
        warnings.warn("GetDevServerJobTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GetDevServerJobTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
