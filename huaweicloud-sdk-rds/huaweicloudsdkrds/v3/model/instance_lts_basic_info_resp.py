# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLtsBasicInfoResp:

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
        'engine_name': 'str',
        'engine_version': 'str',
        'engine_category': 'str',
        'status': 'str',
        'enterprise_project_id': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'engine_category': 'engine_category',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'actions': 'actions'
    }

    def __init__(self, id=None, name=None, engine_name=None, engine_version=None, engine_category=None, status=None, enterprise_project_id=None, actions=None):
        r"""InstanceLtsBasicInfoResp

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名称
        :type name: str
        :param engine_name: 引擎名
        :type engine_name: str
        :param engine_version: 引擎版本
        :type engine_version: str
        :param engine_category: 引擎分类
        :type engine_category: str
        :param status: 实例状态
        :type status: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param actions: 实例进行中的任务
        :type actions: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._engine_category = None
        self._status = None
        self._enterprise_project_id = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if engine_category is not None:
            self.engine_category = engine_category
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        r"""Gets the id of this InstanceLtsBasicInfoResp.

        实例id

        :return: The id of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceLtsBasicInfoResp.

        实例id

        :param id: The id of this InstanceLtsBasicInfoResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InstanceLtsBasicInfoResp.

        实例名称

        :return: The name of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceLtsBasicInfoResp.

        实例名称

        :param name: The name of this InstanceLtsBasicInfoResp.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this InstanceLtsBasicInfoResp.

        引擎名

        :return: The engine_name of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this InstanceLtsBasicInfoResp.

        引擎名

        :param engine_name: The engine_name of this InstanceLtsBasicInfoResp.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this InstanceLtsBasicInfoResp.

        引擎版本

        :return: The engine_version of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this InstanceLtsBasicInfoResp.

        引擎版本

        :param engine_version: The engine_version of this InstanceLtsBasicInfoResp.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def engine_category(self):
        r"""Gets the engine_category of this InstanceLtsBasicInfoResp.

        引擎分类

        :return: The engine_category of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._engine_category

    @engine_category.setter
    def engine_category(self, engine_category):
        r"""Sets the engine_category of this InstanceLtsBasicInfoResp.

        引擎分类

        :param engine_category: The engine_category of this InstanceLtsBasicInfoResp.
        :type engine_category: str
        """
        self._engine_category = engine_category

    @property
    def status(self):
        r"""Gets the status of this InstanceLtsBasicInfoResp.

        实例状态

        :return: The status of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceLtsBasicInfoResp.

        实例状态

        :param status: The status of this InstanceLtsBasicInfoResp.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstanceLtsBasicInfoResp.

        企业项目id

        :return: The enterprise_project_id of this InstanceLtsBasicInfoResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstanceLtsBasicInfoResp.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this InstanceLtsBasicInfoResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def actions(self):
        r"""Gets the actions of this InstanceLtsBasicInfoResp.

        实例进行中的任务

        :return: The actions of this InstanceLtsBasicInfoResp.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this InstanceLtsBasicInfoResp.

        实例进行中的任务

        :param actions: The actions of this InstanceLtsBasicInfoResp.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, InstanceLtsBasicInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
