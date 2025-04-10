# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDefaultCategoryResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_status': 'str',
        'import_error_message': 'str',
        'children': 'list[ImportDefaultCategoryResultDto]',
        'rule_result': 'list[ImportDefaultRuleResultDto]',
        'uuid': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'import_status': 'import_status',
        'import_error_message': 'import_error_message',
        'children': 'children',
        'rule_result': 'rule_result',
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, import_status=None, import_error_message=None, children=None, rule_result=None, uuid=None, name=None, description=None):
        r"""ImportDefaultCategoryResultDto

        The model defined in huaweicloud sdk

        :param import_status: 导入状态 * success 导入成功 * failed 导入失败
        :type import_status: str
        :param import_error_message: 导入错误原因。
        :type import_error_message: str
        :param children: 子分类导入结果。
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultCategoryResultDto`]
        :param rule_result: 此分类绑定的规则导入的结果。
        :type rule_result: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultRuleResultDto`]
        :param uuid: 数据分类id。
        :type uuid: str
        :param name: 数据分类名称。
        :type name: str
        :param description: 数据分类描述。
        :type description: str
        """
        
        

        self._import_status = None
        self._import_error_message = None
        self._children = None
        self._rule_result = None
        self._uuid = None
        self._name = None
        self._description = None
        self.discriminator = None

        if import_status is not None:
            self.import_status = import_status
        if import_error_message is not None:
            self.import_error_message = import_error_message
        if children is not None:
            self.children = children
        if rule_result is not None:
            self.rule_result = rule_result
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def import_status(self):
        r"""Gets the import_status of this ImportDefaultCategoryResultDto.

        导入状态 * success 导入成功 * failed 导入失败

        :return: The import_status of this ImportDefaultCategoryResultDto.
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        r"""Sets the import_status of this ImportDefaultCategoryResultDto.

        导入状态 * success 导入成功 * failed 导入失败

        :param import_status: The import_status of this ImportDefaultCategoryResultDto.
        :type import_status: str
        """
        self._import_status = import_status

    @property
    def import_error_message(self):
        r"""Gets the import_error_message of this ImportDefaultCategoryResultDto.

        导入错误原因。

        :return: The import_error_message of this ImportDefaultCategoryResultDto.
        :rtype: str
        """
        return self._import_error_message

    @import_error_message.setter
    def import_error_message(self, import_error_message):
        r"""Sets the import_error_message of this ImportDefaultCategoryResultDto.

        导入错误原因。

        :param import_error_message: The import_error_message of this ImportDefaultCategoryResultDto.
        :type import_error_message: str
        """
        self._import_error_message = import_error_message

    @property
    def children(self):
        r"""Gets the children of this ImportDefaultCategoryResultDto.

        子分类导入结果。

        :return: The children of this ImportDefaultCategoryResultDto.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultCategoryResultDto`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ImportDefaultCategoryResultDto.

        子分类导入结果。

        :param children: The children of this ImportDefaultCategoryResultDto.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultCategoryResultDto`]
        """
        self._children = children

    @property
    def rule_result(self):
        r"""Gets the rule_result of this ImportDefaultCategoryResultDto.

        此分类绑定的规则导入的结果。

        :return: The rule_result of this ImportDefaultCategoryResultDto.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultRuleResultDto`]
        """
        return self._rule_result

    @rule_result.setter
    def rule_result(self, rule_result):
        r"""Sets the rule_result of this ImportDefaultCategoryResultDto.

        此分类绑定的规则导入的结果。

        :param rule_result: The rule_result of this ImportDefaultCategoryResultDto.
        :type rule_result: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportDefaultRuleResultDto`]
        """
        self._rule_result = rule_result

    @property
    def uuid(self):
        r"""Gets the uuid of this ImportDefaultCategoryResultDto.

        数据分类id。

        :return: The uuid of this ImportDefaultCategoryResultDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ImportDefaultCategoryResultDto.

        数据分类id。

        :param uuid: The uuid of this ImportDefaultCategoryResultDto.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def name(self):
        r"""Gets the name of this ImportDefaultCategoryResultDto.

        数据分类名称。

        :return: The name of this ImportDefaultCategoryResultDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImportDefaultCategoryResultDto.

        数据分类名称。

        :param name: The name of this ImportDefaultCategoryResultDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ImportDefaultCategoryResultDto.

        数据分类描述。

        :return: The description of this ImportDefaultCategoryResultDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImportDefaultCategoryResultDto.

        数据分类描述。

        :param description: The description of this ImportDefaultCategoryResultDto.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImportDefaultCategoryResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
