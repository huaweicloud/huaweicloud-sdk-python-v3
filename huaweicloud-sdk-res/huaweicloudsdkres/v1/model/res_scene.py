# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResScene:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'datasource_id': 'str',
        'ds_config': 'DataConfig',
        'scene_id': 'str',
        'scene_name': 'str',
        'type': 'str',
        'service_type': 'str',
        'status': 'str',
        'workspace_id': 'str',
        'created_at': 'int',
        'update_at': 'int',
        'specs_config': 'SpecsConfig'
    }

    attribute_map = {
        'category': 'category',
        'datasource_id': 'datasource_id',
        'ds_config': 'ds_config',
        'scene_id': 'scene_id',
        'scene_name': 'scene_name',
        'type': 'type',
        'service_type': 'service_type',
        'status': 'status',
        'workspace_id': 'workspace_id',
        'created_at': 'created_at',
        'update_at': 'update_at',
        'specs_config': 'specs_config'
    }

    def __init__(self, category=None, datasource_id=None, ds_config=None, scene_id=None, scene_name=None, type=None, service_type=None, status=None, workspace_id=None, created_at=None, update_at=None, specs_config=None):
        r"""ResScene

        The model defined in huaweicloud sdk

        :param category: 类型。
        :type category: str
        :param datasource_id: 数据源id。
        :type datasource_id: str
        :param ds_config: 
        :type ds_config: :class:`huaweicloudsdkres.v1.DataConfig`
        :param scene_id: 场景id。
        :type scene_id: str
        :param scene_name: 场景名称。
        :type scene_name: str
        :param type: 场景类型。
        :type type: str
        :param service_type: 服务类型。
        :type service_type: str
        :param status: 状态。
        :type status: str
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param created_at: 创建时间。
        :type created_at: int
        :param update_at: 更新时间。
        :type update_at: int
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        
        

        self._category = None
        self._datasource_id = None
        self._ds_config = None
        self._scene_id = None
        self._scene_name = None
        self._type = None
        self._service_type = None
        self._status = None
        self._workspace_id = None
        self._created_at = None
        self._update_at = None
        self._specs_config = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if datasource_id is not None:
            self.datasource_id = datasource_id
        if ds_config is not None:
            self.ds_config = ds_config
        if scene_id is not None:
            self.scene_id = scene_id
        if scene_name is not None:
            self.scene_name = scene_name
        if type is not None:
            self.type = type
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        if specs_config is not None:
            self.specs_config = specs_config

    @property
    def category(self):
        r"""Gets the category of this ResScene.

        类型。

        :return: The category of this ResScene.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ResScene.

        类型。

        :param category: The category of this ResScene.
        :type category: str
        """
        self._category = category

    @property
    def datasource_id(self):
        r"""Gets the datasource_id of this ResScene.

        数据源id。

        :return: The datasource_id of this ResScene.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        r"""Sets the datasource_id of this ResScene.

        数据源id。

        :param datasource_id: The datasource_id of this ResScene.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def ds_config(self):
        r"""Gets the ds_config of this ResScene.

        :return: The ds_config of this ResScene.
        :rtype: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        return self._ds_config

    @ds_config.setter
    def ds_config(self, ds_config):
        r"""Sets the ds_config of this ResScene.

        :param ds_config: The ds_config of this ResScene.
        :type ds_config: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        self._ds_config = ds_config

    @property
    def scene_id(self):
        r"""Gets the scene_id of this ResScene.

        场景id。

        :return: The scene_id of this ResScene.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this ResScene.

        场景id。

        :param scene_id: The scene_id of this ResScene.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def scene_name(self):
        r"""Gets the scene_name of this ResScene.

        场景名称。

        :return: The scene_name of this ResScene.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        r"""Sets the scene_name of this ResScene.

        场景名称。

        :param scene_name: The scene_name of this ResScene.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def type(self):
        r"""Gets the type of this ResScene.

        场景类型。

        :return: The type of this ResScene.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResScene.

        场景类型。

        :param type: The type of this ResScene.
        :type type: str
        """
        self._type = type

    @property
    def service_type(self):
        r"""Gets the service_type of this ResScene.

        服务类型。

        :return: The service_type of this ResScene.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ResScene.

        服务类型。

        :param service_type: The service_type of this ResScene.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        r"""Gets the status of this ResScene.

        状态。

        :return: The status of this ResScene.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResScene.

        状态。

        :param status: The status of this ResScene.
        :type status: str
        """
        self._status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ResScene.

        工作空间id。

        :return: The workspace_id of this ResScene.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ResScene.

        工作空间id。

        :param workspace_id: The workspace_id of this ResScene.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ResScene.

        创建时间。

        :return: The created_at of this ResScene.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ResScene.

        创建时间。

        :param created_at: The created_at of this ResScene.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ResScene.

        更新时间。

        :return: The update_at of this ResScene.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ResScene.

        更新时间。

        :param update_at: The update_at of this ResScene.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def specs_config(self):
        r"""Gets the specs_config of this ResScene.

        :return: The specs_config of this ResScene.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        r"""Sets the specs_config of this ResScene.

        :param specs_config: The specs_config of this ResScene.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResScene):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
