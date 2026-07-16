# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'endpoints': 'list[EndpointsReq]',
        'flavor': 'str',
        'custom_spec': 'NotebookCustomSpec',
        'image_id': 'str',
        'name': 'str',
        'storage_new_size': 'int',
        'hooks': 'CustomHooks',
        'affinity': 'AffinityType',
        'dew_secret_name': 'str',
        'data_volumes': 'list[VolumeMountRequest]'
    }

    attribute_map = {
        'description': 'description',
        'endpoints': 'endpoints',
        'flavor': 'flavor',
        'custom_spec': 'custom_spec',
        'image_id': 'image_id',
        'name': 'name',
        'storage_new_size': 'storage_new_size',
        'hooks': 'hooks',
        'affinity': 'affinity',
        'dew_secret_name': 'dew_secret_name',
        'data_volumes': 'data_volumes'
    }

    def __init__(self, description=None, endpoints=None, flavor=None, custom_spec=None, image_id=None, name=None, storage_new_size=None, hooks=None, affinity=None, dew_secret_name=None, data_volumes=None):
        r"""NotebookUpdateRequest

        The model defined in huaweicloud sdk

        :param description: **参数解释**：支持更新实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&amp;&lt;&gt;\&quot;&#39;/。 **默认取值**：不涉及。
        :type description: str
        :param endpoints: **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        :param flavor: **参数解释**：支持变更实例的机器规格。支持变更的规格可以通过本章节的[查询支持可切换规格列表](ShowSwitchableFlavors.xml)的API获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        :param image_id: **参数解释**：支持更新镜像ID，镜像ID参考[查询支持的镜像列表](ListImage.xml)获取。 **约束限制**：不涉及。 **取值范围**：调用[查询支持的镜像列表](ListImage.xml)接口获取的合法镜像ID列表。 **默认取值**：不涉及。
        :type image_id: str
        :param name: **参数解释**：支持更新实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。
        :type name: str
        :param storage_new_size: **参数解释**：EVS实例支持动态扩充的容量，单位GB。只允许扩容，不允许缩容。 **约束限制**：不涉及。 **取值范围**：最大允许扩容至4096。 **默认取值**：不涉及。
        :type storage_new_size: int
        :param hooks: 
        :type hooks: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        :param dew_secret_name: **参数解释**：DEW存储的用户AKSK凭据名称。 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dew_secret_name: str
        :param data_volumes: **参数解释**：扩展存储信息。 **约束限制**：不涉及。
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        """
        
        

        self._description = None
        self._endpoints = None
        self._flavor = None
        self._custom_spec = None
        self._image_id = None
        self._name = None
        self._storage_new_size = None
        self._hooks = None
        self._affinity = None
        self._dew_secret_name = None
        self._data_volumes = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if endpoints is not None:
            self.endpoints = endpoints
        if flavor is not None:
            self.flavor = flavor
        if custom_spec is not None:
            self.custom_spec = custom_spec
        if image_id is not None:
            self.image_id = image_id
        if name is not None:
            self.name = name
        if storage_new_size is not None:
            self.storage_new_size = storage_new_size
        if hooks is not None:
            self.hooks = hooks
        if affinity is not None:
            self.affinity = affinity
        if dew_secret_name is not None:
            self.dew_secret_name = dew_secret_name
        if data_volumes is not None:
            self.data_volumes = data_volumes

    @property
    def description(self):
        r"""Gets the description of this NotebookUpdateRequest.

        **参数解释**：支持更新实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&<>\"'/。 **默认取值**：不涉及。

        :return: The description of this NotebookUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NotebookUpdateRequest.

        **参数解释**：支持更新实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&<>\"'/。 **默认取值**：不涉及。

        :param description: The description of this NotebookUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def endpoints(self):
        r"""Gets the endpoints of this NotebookUpdateRequest.

        **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :return: The endpoints of this NotebookUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this NotebookUpdateRequest.

        **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :param endpoints: The endpoints of this NotebookUpdateRequest.
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        """
        self._endpoints = endpoints

    @property
    def flavor(self):
        r"""Gets the flavor of this NotebookUpdateRequest.

        **参数解释**：支持变更实例的机器规格。支持变更的规格可以通过本章节的[查询支持可切换规格列表](ShowSwitchableFlavors.xml)的API获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this NotebookUpdateRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NotebookUpdateRequest.

        **参数解释**：支持变更实例的机器规格。支持变更的规格可以通过本章节的[查询支持可切换规格列表](ShowSwitchableFlavors.xml)的API获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this NotebookUpdateRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this NotebookUpdateRequest.

        :return: The custom_spec of this NotebookUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this NotebookUpdateRequest.

        :param custom_spec: The custom_spec of this NotebookUpdateRequest.
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        """
        self._custom_spec = custom_spec

    @property
    def image_id(self):
        r"""Gets the image_id of this NotebookUpdateRequest.

        **参数解释**：支持更新镜像ID，镜像ID参考[查询支持的镜像列表](ListImage.xml)获取。 **约束限制**：不涉及。 **取值范围**：调用[查询支持的镜像列表](ListImage.xml)接口获取的合法镜像ID列表。 **默认取值**：不涉及。

        :return: The image_id of this NotebookUpdateRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this NotebookUpdateRequest.

        **参数解释**：支持更新镜像ID，镜像ID参考[查询支持的镜像列表](ListImage.xml)获取。 **约束限制**：不涉及。 **取值范围**：调用[查询支持的镜像列表](ListImage.xml)接口获取的合法镜像ID列表。 **默认取值**：不涉及。

        :param image_id: The image_id of this NotebookUpdateRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def name(self):
        r"""Gets the name of this NotebookUpdateRequest.

        **参数解释**：支持更新实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。

        :return: The name of this NotebookUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NotebookUpdateRequest.

        **参数解释**：支持更新实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。

        :param name: The name of this NotebookUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def storage_new_size(self):
        r"""Gets the storage_new_size of this NotebookUpdateRequest.

        **参数解释**：EVS实例支持动态扩充的容量，单位GB。只允许扩容，不允许缩容。 **约束限制**：不涉及。 **取值范围**：最大允许扩容至4096。 **默认取值**：不涉及。

        :return: The storage_new_size of this NotebookUpdateRequest.
        :rtype: int
        """
        return self._storage_new_size

    @storage_new_size.setter
    def storage_new_size(self, storage_new_size):
        r"""Sets the storage_new_size of this NotebookUpdateRequest.

        **参数解释**：EVS实例支持动态扩充的容量，单位GB。只允许扩容，不允许缩容。 **约束限制**：不涉及。 **取值范围**：最大允许扩容至4096。 **默认取值**：不涉及。

        :param storage_new_size: The storage_new_size of this NotebookUpdateRequest.
        :type storage_new_size: int
        """
        self._storage_new_size = storage_new_size

    @property
    def hooks(self):
        r"""Gets the hooks of this NotebookUpdateRequest.

        :return: The hooks of this NotebookUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        """
        return self._hooks

    @hooks.setter
    def hooks(self, hooks):
        r"""Sets the hooks of this NotebookUpdateRequest.

        :param hooks: The hooks of this NotebookUpdateRequest.
        :type hooks: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        """
        self._hooks = hooks

    @property
    def affinity(self):
        r"""Gets the affinity of this NotebookUpdateRequest.

        :return: The affinity of this NotebookUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this NotebookUpdateRequest.

        :param affinity: The affinity of this NotebookUpdateRequest.
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        self._affinity = affinity

    @property
    def dew_secret_name(self):
        r"""Gets the dew_secret_name of this NotebookUpdateRequest.

        **参数解释**：DEW存储的用户AKSK凭据名称。 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dew_secret_name of this NotebookUpdateRequest.
        :rtype: str
        """
        return self._dew_secret_name

    @dew_secret_name.setter
    def dew_secret_name(self, dew_secret_name):
        r"""Sets the dew_secret_name of this NotebookUpdateRequest.

        **参数解释**：DEW存储的用户AKSK凭据名称。 **参数约束**：当category为OBS时必填，仅支持大小写字母、数字、中划线、下划线，长度 1-64 字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dew_secret_name: The dew_secret_name of this NotebookUpdateRequest.
        :type dew_secret_name: str
        """
        self._dew_secret_name = dew_secret_name

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NotebookUpdateRequest.

        **参数解释**：扩展存储信息。 **约束限制**：不涉及。

        :return: The data_volumes of this NotebookUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NotebookUpdateRequest.

        **参数解释**：扩展存储信息。 **约束限制**：不涉及。

        :param data_volumes: The data_volumes of this NotebookUpdateRequest.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        """
        self._data_volumes = data_volumes

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
        if not isinstance(other, NotebookUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
