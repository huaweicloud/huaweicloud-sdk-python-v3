# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequestBody:

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
        'charge_mode': 'str',
        'enterprise_project_id': 'str',
        'description': 'str',
        'shared': 'bool',
        'specs': 'list[CreateSpec]',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'charge_mode': 'charge_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'shared': 'shared',
        'specs': 'specs',
        'tags': 'tags'
    }

    def __init__(self, name=None, charge_mode=None, enterprise_project_id=None, description=None, shared=None, specs=None, tags=None):
        """CreateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 实例名称。只能包含字母、数字、下划线和中划线，且长度为4到32个字符。
        :type name: str
        :param charge_mode: 支付类型，postPaid为按需期，prePaid为包周期
        :type charge_mode: str
        :param enterprise_project_id: 企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。
        :type enterprise_project_id: str
        :param description: 实例描述。用户输入的描述，最长为255个字符。
        :type description: str
        :param shared: false为物理多租；true为逻辑多租。默认为true。
        :type shared: bool
        :param specs: 规格列表
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        :param tags: 标签列表，最多添加20个标签。
        :type tags: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        """
        
        

        self._name = None
        self._charge_mode = None
        self._enterprise_project_id = None
        self._description = None
        self._shared = None
        self._specs = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.charge_mode = charge_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        self.shared = shared
        if specs is not None:
            self.specs = specs
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateInstanceRequestBody.

        实例名称。只能包含字母、数字、下划线和中划线，且长度为4到32个字符。

        :return: The name of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceRequestBody.

        实例名称。只能包含字母、数字、下划线和中划线，且长度为4到32个字符。

        :param name: The name of this CreateInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateInstanceRequestBody.

        支付类型，postPaid为按需期，prePaid为包周期

        :return: The charge_mode of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateInstanceRequestBody.

        支付类型，postPaid为按需期，prePaid为包周期

        :param charge_mode: The charge_mode of this CreateInstanceRequestBody.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。

        :return: The enterprise_project_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        """Gets the description of this CreateInstanceRequestBody.

        实例描述。用户输入的描述，最长为255个字符。

        :return: The description of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInstanceRequestBody.

        实例描述。用户输入的描述，最长为255个字符。

        :param description: The description of this CreateInstanceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def shared(self):
        """Gets the shared of this CreateInstanceRequestBody.

        false为物理多租；true为逻辑多租。默认为true。

        :return: The shared of this CreateInstanceRequestBody.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this CreateInstanceRequestBody.

        false为物理多租；true为逻辑多租。默认为true。

        :param shared: The shared of this CreateInstanceRequestBody.
        :type shared: bool
        """
        self._shared = shared

    @property
    def specs(self):
        """Gets the specs of this CreateInstanceRequestBody.

        规格列表

        :return: The specs of this CreateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this CreateInstanceRequestBody.

        规格列表

        :param specs: The specs of this CreateInstanceRequestBody.
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        self._specs = specs

    @property
    def tags(self):
        """Gets the tags of this CreateInstanceRequestBody.

        标签列表，最多添加20个标签。

        :return: The tags of this CreateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInstanceRequestBody.

        标签列表，最多添加20个标签。

        :param tags: The tags of this CreateInstanceRequestBody.
        :type tags: list[:class:`huaweicloudsdklakeformation.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
