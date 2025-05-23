# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDbParametersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_language': 'str',
        'add_task_scenario': 'str',
        'main_task_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'add_task_scenario': 'add_task_scenario',
        'main_task_name': 'main_task_name'
    }

    def __init__(self, instance_id=None, x_language=None, add_task_scenario=None, main_task_name=None):
        r"""ListStarRocksDbParametersRequest

        The model defined in huaweicloud sdk

        :param instance_id: StarRocks实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param add_task_scenario: **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。
        :type add_task_scenario: str
        :param main_task_name: **参数解释**：  新增子任务相应的主任务名。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。
        :type main_task_name: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._add_task_scenario = None
        self._main_task_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.x_language = x_language
        if add_task_scenario is not None:
            self.add_task_scenario = add_task_scenario
        if main_task_name is not None:
            self.main_task_name = main_task_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListStarRocksDbParametersRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :return: The instance_id of this ListStarRocksDbParametersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListStarRocksDbParametersRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ListStarRocksDbParametersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListStarRocksDbParametersRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ListStarRocksDbParametersRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListStarRocksDbParametersRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ListStarRocksDbParametersRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def add_task_scenario(self):
        r"""Gets the add_task_scenario of this ListStarRocksDbParametersRequest.

        **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。

        :return: The add_task_scenario of this ListStarRocksDbParametersRequest.
        :rtype: str
        """
        return self._add_task_scenario

    @add_task_scenario.setter
    def add_task_scenario(self, add_task_scenario):
        r"""Sets the add_task_scenario of this ListStarRocksDbParametersRequest.

        **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。

        :param add_task_scenario: The add_task_scenario of this ListStarRocksDbParametersRequest.
        :type add_task_scenario: str
        """
        self._add_task_scenario = add_task_scenario

    @property
    def main_task_name(self):
        r"""Gets the main_task_name of this ListStarRocksDbParametersRequest.

        **参数解释**：  新增子任务相应的主任务名。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。

        :return: The main_task_name of this ListStarRocksDbParametersRequest.
        :rtype: str
        """
        return self._main_task_name

    @main_task_name.setter
    def main_task_name(self, main_task_name):
        r"""Sets the main_task_name of this ListStarRocksDbParametersRequest.

        **参数解释**：  新增子任务相应的主任务名。  **约束限制**：  非必填。  **取值范围**：  不涉及。  **默认值**：  不涉及。

        :param main_task_name: The main_task_name of this ListStarRocksDbParametersRequest.
        :type main_task_name: str
        """
        self._main_task_name = main_task_name

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
        if not isinstance(other, ListStarRocksDbParametersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
