# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigInfoDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'value': 'str',
        'task_id': 'str',
        'static_status': 'int',
        'limits': 'list[ParamTypeLimits]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'value': 'value',
        'task_id': 'task_id',
        'static_status': 'static_status',
        'limits': 'limits'
    }

    def __init__(self, name=None, type=None, description=None, value=None, task_id=None, static_status=None, limits=None):
        r"""ConfigInfoDO

        The model defined in huaweicloud sdk

        :param name: 部署参数名称，用户可自定义
        :type name: str
        :param type: 类型，如果填写name字段，则type必选,若type为空则默认为text
        :type type: str
        :param description: 描述
        :type description: str
        :param value: 部署参数值
        :type value: str
        :param task_id: 部署任务id，创建应用后由系统自动生成
        :type task_id: str
        :param static_status: 表示是否为静态参数，值为1时不支持部署时变更参数，值为0时支持，并且也会把该参数上报流水线
        :type static_status: int
        :param limits: 当参数类型为enum枚举类型时，必须填写可选值
        :type limits: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ParamTypeLimits`]
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._value = None
        self._task_id = None
        self._static_status = None
        self._limits = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value
        if task_id is not None:
            self.task_id = task_id
        if static_status is not None:
            self.static_status = static_status
        if limits is not None:
            self.limits = limits

    @property
    def name(self):
        r"""Gets the name of this ConfigInfoDO.

        部署参数名称，用户可自定义

        :return: The name of this ConfigInfoDO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigInfoDO.

        部署参数名称，用户可自定义

        :param name: The name of this ConfigInfoDO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ConfigInfoDO.

        类型，如果填写name字段，则type必选,若type为空则默认为text

        :return: The type of this ConfigInfoDO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigInfoDO.

        类型，如果填写name字段，则type必选,若type为空则默认为text

        :param type: The type of this ConfigInfoDO.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ConfigInfoDO.

        描述

        :return: The description of this ConfigInfoDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigInfoDO.

        描述

        :param description: The description of this ConfigInfoDO.
        :type description: str
        """
        self._description = description

    @property
    def value(self):
        r"""Gets the value of this ConfigInfoDO.

        部署参数值

        :return: The value of this ConfigInfoDO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConfigInfoDO.

        部署参数值

        :param value: The value of this ConfigInfoDO.
        :type value: str
        """
        self._value = value

    @property
    def task_id(self):
        r"""Gets the task_id of this ConfigInfoDO.

        部署任务id，创建应用后由系统自动生成

        :return: The task_id of this ConfigInfoDO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ConfigInfoDO.

        部署任务id，创建应用后由系统自动生成

        :param task_id: The task_id of this ConfigInfoDO.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def static_status(self):
        r"""Gets the static_status of this ConfigInfoDO.

        表示是否为静态参数，值为1时不支持部署时变更参数，值为0时支持，并且也会把该参数上报流水线

        :return: The static_status of this ConfigInfoDO.
        :rtype: int
        """
        return self._static_status

    @static_status.setter
    def static_status(self, static_status):
        r"""Sets the static_status of this ConfigInfoDO.

        表示是否为静态参数，值为1时不支持部署时变更参数，值为0时支持，并且也会把该参数上报流水线

        :param static_status: The static_status of this ConfigInfoDO.
        :type static_status: int
        """
        self._static_status = static_status

    @property
    def limits(self):
        r"""Gets the limits of this ConfigInfoDO.

        当参数类型为enum枚举类型时，必须填写可选值

        :return: The limits of this ConfigInfoDO.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ParamTypeLimits`]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this ConfigInfoDO.

        当参数类型为enum枚举类型时，必须填写可选值

        :param limits: The limits of this ConfigInfoDO.
        :type limits: list[:class:`huaweicloudsdkcodeartsdeploy.v2.ParamTypeLimits`]
        """
        self._limits = limits

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
        if not isinstance(other, ConfigInfoDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
