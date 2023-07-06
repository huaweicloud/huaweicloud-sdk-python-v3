# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskCheckParamters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_id': 'int',
        'name': 'str',
        'checker_configs': 'list[CheckConfigInfo]'
    }

    attribute_map = {
        'check_id': 'check_id',
        'name': 'name',
        'checker_configs': 'checker_configs'
    }

    def __init__(self, check_id=None, name=None, checker_configs=None):
        """TaskCheckParamters

        The model defined in huaweicloud sdk

        :param check_id: 检查工具ID
        :type check_id: int
        :param name: 编译参数名称
        :type name: str
        :param checker_configs: 检查参数配置信息
        :type checker_configs: list[:class:`huaweicloudsdkcodeartscheck.v2.CheckConfigInfo`]
        """
        
        

        self._check_id = None
        self._name = None
        self._checker_configs = None
        self.discriminator = None

        if check_id is not None:
            self.check_id = check_id
        if name is not None:
            self.name = name
        if checker_configs is not None:
            self.checker_configs = checker_configs

    @property
    def check_id(self):
        """Gets the check_id of this TaskCheckParamters.

        检查工具ID

        :return: The check_id of this TaskCheckParamters.
        :rtype: int
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this TaskCheckParamters.

        检查工具ID

        :param check_id: The check_id of this TaskCheckParamters.
        :type check_id: int
        """
        self._check_id = check_id

    @property
    def name(self):
        """Gets the name of this TaskCheckParamters.

        编译参数名称

        :return: The name of this TaskCheckParamters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskCheckParamters.

        编译参数名称

        :param name: The name of this TaskCheckParamters.
        :type name: str
        """
        self._name = name

    @property
    def checker_configs(self):
        """Gets the checker_configs of this TaskCheckParamters.

        检查参数配置信息

        :return: The checker_configs of this TaskCheckParamters.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.CheckConfigInfo`]
        """
        return self._checker_configs

    @checker_configs.setter
    def checker_configs(self, checker_configs):
        """Sets the checker_configs of this TaskCheckParamters.

        检查参数配置信息

        :param checker_configs: The checker_configs of this TaskCheckParamters.
        :type checker_configs: list[:class:`huaweicloudsdkcodeartscheck.v2.CheckConfigInfo`]
        """
        self._checker_configs = checker_configs

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
        if not isinstance(other, TaskCheckParamters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
