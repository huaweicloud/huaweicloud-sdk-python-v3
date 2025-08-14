# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterProtectPolicyTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'template_name': 'str',
        'template_type': 'str',
        'target_kind': 'str',
        'tag': 'str',
        'level': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'target_kind': 'target_kind',
        'tag': 'tag',
        'level': 'level'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, template_name=None, template_type=None, target_kind=None, tag=None, level=None):
        r"""ListClusterProtectPolicyTemplatesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型
        :type template_type: str
        :param target_kind: 策略模板应用资源类型，多个资源类型通过分号分隔连接
        :type target_kind: str
        :param tag: 标签
        :type tag: str
        :param level: 推荐等级
        :type level: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._template_name = None
        self._template_type = None
        self._target_kind = None
        self._tag = None
        self._level = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.limit = limit
        self.offset = offset
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if target_kind is not None:
            self.target_kind = target_kind
        if tag is not None:
            self.tag = tag
        if level is not None:
            self.level = level

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClusterProtectPolicyTemplatesRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClusterProtectPolicyTemplatesRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListClusterProtectPolicyTemplatesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterProtectPolicyTemplatesRequest.

        每页显示数量

        :return: The limit of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterProtectPolicyTemplatesRequest.

        每页显示数量

        :param limit: The limit of this ListClusterProtectPolicyTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterProtectPolicyTemplatesRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterProtectPolicyTemplatesRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListClusterProtectPolicyTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def template_name(self):
        r"""Gets the template_name of this ListClusterProtectPolicyTemplatesRequest.

        模板名称

        :return: The template_name of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ListClusterProtectPolicyTemplatesRequest.

        模板名称

        :param template_name: The template_name of this ListClusterProtectPolicyTemplatesRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ListClusterProtectPolicyTemplatesRequest.

        模板类型

        :return: The template_type of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ListClusterProtectPolicyTemplatesRequest.

        模板类型

        :param template_type: The template_type of this ListClusterProtectPolicyTemplatesRequest.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def target_kind(self):
        r"""Gets the target_kind of this ListClusterProtectPolicyTemplatesRequest.

        策略模板应用资源类型，多个资源类型通过分号分隔连接

        :return: The target_kind of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._target_kind

    @target_kind.setter
    def target_kind(self, target_kind):
        r"""Sets the target_kind of this ListClusterProtectPolicyTemplatesRequest.

        策略模板应用资源类型，多个资源类型通过分号分隔连接

        :param target_kind: The target_kind of this ListClusterProtectPolicyTemplatesRequest.
        :type target_kind: str
        """
        self._target_kind = target_kind

    @property
    def tag(self):
        r"""Gets the tag of this ListClusterProtectPolicyTemplatesRequest.

        标签

        :return: The tag of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListClusterProtectPolicyTemplatesRequest.

        标签

        :param tag: The tag of this ListClusterProtectPolicyTemplatesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def level(self):
        r"""Gets the level of this ListClusterProtectPolicyTemplatesRequest.

        推荐等级

        :return: The level of this ListClusterProtectPolicyTemplatesRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListClusterProtectPolicyTemplatesRequest.

        推荐等级

        :param level: The level of this ListClusterProtectPolicyTemplatesRequest.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, ListClusterProtectPolicyTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
