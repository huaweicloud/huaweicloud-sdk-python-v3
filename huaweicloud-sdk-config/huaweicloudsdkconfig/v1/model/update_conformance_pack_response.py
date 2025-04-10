# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConformancePackResponse(SdkResponse):

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
        'stack_id': 'str',
        'stack_name': 'str',
        'deployment_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'template_key': 'str',
        'template_uri': 'str',
        'agency_name': 'str',
        'status': 'str',
        'error_message': 'str',
        'vars_structure': 'list[VarsStructure]',
        'created_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stack_id': 'stack_id',
        'stack_name': 'stack_name',
        'deployment_id': 'deployment_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'template_key': 'template_key',
        'template_uri': 'template_uri',
        'agency_name': 'agency_name',
        'status': 'status',
        'error_message': 'error_message',
        'vars_structure': 'vars_structure',
        'created_by': 'created_by'
    }

    def __init__(self, id=None, name=None, stack_id=None, stack_name=None, deployment_id=None, created_at=None, updated_at=None, template_key=None, template_uri=None, agency_name=None, status=None, error_message=None, vars_structure=None, created_by=None):
        r"""UpdateConformancePackResponse

        The model defined in huaweicloud sdk

        :param id: 合规规则包ID。
        :type id: str
        :param name: 合规规则包名称。
        :type name: str
        :param stack_id: 资源栈（stack）的唯一ID。
        :type stack_id: str
        :param stack_name: 资源栈（stack）的名称。
        :type stack_name: str
        :param deployment_id: 部署ID。
        :type deployment_id: str
        :param created_at: 合规规则包创建时间。
        :type created_at: str
        :param updated_at: 合规规则包更新时间。
        :type updated_at: str
        :param template_key: 预定义合规规则包模板名称。
        :type template_key: str
        :param template_uri: 合规规则包模板OBS地址
        :type template_uri: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param status: 合规规则包部署状态。
        :type status: str
        :param error_message: 部署或删除合规规则包错误时的错误信息
        :type error_message: str
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        :param created_by: 创建者
        :type created_by: str
        """
        
        super(UpdateConformancePackResponse, self).__init__()

        self._id = None
        self._name = None
        self._stack_id = None
        self._stack_name = None
        self._deployment_id = None
        self._created_at = None
        self._updated_at = None
        self._template_key = None
        self._template_uri = None
        self._agency_name = None
        self._status = None
        self._error_message = None
        self._vars_structure = None
        self._created_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if stack_id is not None:
            self.stack_id = stack_id
        if stack_name is not None:
            self.stack_name = stack_name
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if template_key is not None:
            self.template_key = template_key
        if template_uri is not None:
            self.template_uri = template_uri
        if agency_name is not None:
            self.agency_name = agency_name
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        r"""Gets the id of this UpdateConformancePackResponse.

        合规规则包ID。

        :return: The id of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateConformancePackResponse.

        合规规则包ID。

        :param id: The id of this UpdateConformancePackResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateConformancePackResponse.

        合规规则包名称。

        :return: The name of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConformancePackResponse.

        合规规则包名称。

        :param name: The name of this UpdateConformancePackResponse.
        :type name: str
        """
        self._name = name

    @property
    def stack_id(self):
        r"""Gets the stack_id of this UpdateConformancePackResponse.

        资源栈（stack）的唯一ID。

        :return: The stack_id of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this UpdateConformancePackResponse.

        资源栈（stack）的唯一ID。

        :param stack_id: The stack_id of this UpdateConformancePackResponse.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def stack_name(self):
        r"""Gets the stack_name of this UpdateConformancePackResponse.

        资源栈（stack）的名称。

        :return: The stack_name of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        r"""Sets the stack_name of this UpdateConformancePackResponse.

        资源栈（stack）的名称。

        :param stack_name: The stack_name of this UpdateConformancePackResponse.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this UpdateConformancePackResponse.

        部署ID。

        :return: The deployment_id of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this UpdateConformancePackResponse.

        部署ID。

        :param deployment_id: The deployment_id of this UpdateConformancePackResponse.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateConformancePackResponse.

        合规规则包创建时间。

        :return: The created_at of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateConformancePackResponse.

        合规规则包创建时间。

        :param created_at: The created_at of this UpdateConformancePackResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateConformancePackResponse.

        合规规则包更新时间。

        :return: The updated_at of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateConformancePackResponse.

        合规规则包更新时间。

        :param updated_at: The updated_at of this UpdateConformancePackResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def template_key(self):
        r"""Gets the template_key of this UpdateConformancePackResponse.

        预定义合规规则包模板名称。

        :return: The template_key of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        r"""Sets the template_key of this UpdateConformancePackResponse.

        预定义合规规则包模板名称。

        :param template_key: The template_key of this UpdateConformancePackResponse.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def template_uri(self):
        r"""Gets the template_uri of this UpdateConformancePackResponse.

        合规规则包模板OBS地址

        :return: The template_uri of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        r"""Sets the template_uri of this UpdateConformancePackResponse.

        合规规则包模板OBS地址

        :param template_uri: The template_uri of this UpdateConformancePackResponse.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdateConformancePackResponse.

        委托名称

        :return: The agency_name of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdateConformancePackResponse.

        委托名称

        :param agency_name: The agency_name of this UpdateConformancePackResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def status(self):
        r"""Gets the status of this UpdateConformancePackResponse.

        合规规则包部署状态。

        :return: The status of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateConformancePackResponse.

        合规规则包部署状态。

        :param status: The status of this UpdateConformancePackResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_message(self):
        r"""Gets the error_message of this UpdateConformancePackResponse.

        部署或删除合规规则包错误时的错误信息

        :return: The error_message of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this UpdateConformancePackResponse.

        部署或删除合规规则包错误时的错误信息

        :param error_message: The error_message of this UpdateConformancePackResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def vars_structure(self):
        r"""Gets the vars_structure of this UpdateConformancePackResponse.

        合规规则包参数。

        :return: The vars_structure of this UpdateConformancePackResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        r"""Sets the vars_structure of this UpdateConformancePackResponse.

        合规规则包参数。

        :param vars_structure: The vars_structure of this UpdateConformancePackResponse.
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def created_by(self):
        r"""Gets the created_by of this UpdateConformancePackResponse.

        创建者

        :return: The created_by of this UpdateConformancePackResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this UpdateConformancePackResponse.

        创建者

        :param created_by: The created_by of this UpdateConformancePackResponse.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, UpdateConformancePackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
