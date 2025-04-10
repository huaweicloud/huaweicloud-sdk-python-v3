# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Scene:

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
        'type': 'str',
        'scene_name': 'str',
        'scene_id': 'str',
        'datasource_id': 'str',
        'status': 'str',
        'created_at': 'int',
        'update_at': 'int',
        'workspace_id': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'type': 'type',
        'scene_name': 'scene_name',
        'scene_id': 'scene_id',
        'datasource_id': 'datasource_id',
        'status': 'status',
        'created_at': 'created_at',
        'update_at': 'update_at',
        'workspace_id': 'workspace_id',
        'service_type': 'service_type'
    }

    def __init__(self, category=None, type=None, scene_name=None, scene_id=None, datasource_id=None, status=None, created_at=None, update_at=None, workspace_id=None, service_type=None):
        r"""Scene

        The model defined in huaweicloud sdk

        :param category: 类型。
        :type category: str
        :param type: 场景类型。
        :type type: str
        :param scene_name: 场景名称。
        :type scene_name: str
        :param scene_id: 场景id。
        :type scene_id: str
        :param datasource_id: 数据源id。
        :type datasource_id: str
        :param status: 状态。
        :type status: str
        :param created_at: 创建时间。
        :type created_at: int
        :param update_at: 更新时间。
        :type update_at: int
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param service_type: 服务类型。
        :type service_type: str
        """
        
        

        self._category = None
        self._type = None
        self._scene_name = None
        self._scene_id = None
        self._datasource_id = None
        self._status = None
        self._created_at = None
        self._update_at = None
        self._workspace_id = None
        self._service_type = None
        self.discriminator = None

        self.category = category
        self.type = type
        self.scene_name = scene_name
        self.scene_id = scene_id
        self.datasource_id = datasource_id
        self.status = status
        self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        self.workspace_id = workspace_id
        self.service_type = service_type

    @property
    def category(self):
        r"""Gets the category of this Scene.

        类型。

        :return: The category of this Scene.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this Scene.

        类型。

        :param category: The category of this Scene.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        r"""Gets the type of this Scene.

        场景类型。

        :return: The type of this Scene.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Scene.

        场景类型。

        :param type: The type of this Scene.
        :type type: str
        """
        self._type = type

    @property
    def scene_name(self):
        r"""Gets the scene_name of this Scene.

        场景名称。

        :return: The scene_name of this Scene.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        r"""Sets the scene_name of this Scene.

        场景名称。

        :param scene_name: The scene_name of this Scene.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def scene_id(self):
        r"""Gets the scene_id of this Scene.

        场景id。

        :return: The scene_id of this Scene.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this Scene.

        场景id。

        :param scene_id: The scene_id of this Scene.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def datasource_id(self):
        r"""Gets the datasource_id of this Scene.

        数据源id。

        :return: The datasource_id of this Scene.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        r"""Sets the datasource_id of this Scene.

        数据源id。

        :param datasource_id: The datasource_id of this Scene.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def status(self):
        r"""Gets the status of this Scene.

        状态。

        :return: The status of this Scene.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Scene.

        状态。

        :param status: The status of this Scene.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this Scene.

        创建时间。

        :return: The created_at of this Scene.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Scene.

        创建时间。

        :param created_at: The created_at of this Scene.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def update_at(self):
        r"""Gets the update_at of this Scene.

        更新时间。

        :return: The update_at of this Scene.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this Scene.

        更新时间。

        :param update_at: The update_at of this Scene.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this Scene.

        工作空间id。

        :return: The workspace_id of this Scene.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this Scene.

        工作空间id。

        :param workspace_id: The workspace_id of this Scene.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def service_type(self):
        r"""Gets the service_type of this Scene.

        服务类型。

        :return: The service_type of this Scene.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this Scene.

        服务类型。

        :param service_type: The service_type of this Scene.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, Scene):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
