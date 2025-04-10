# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskV2RequestBody:

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
        'deploy_system': 'str',
        'template_id': 'str',
        'operation_list': 'list[DeployV2OperationsDO]'
    }

    attribute_map = {
        'id': 'id',
        'deploy_system': 'deploy_system',
        'template_id': 'template_id',
        'operation_list': 'operation_list'
    }

    def __init__(self, id=None, deploy_system=None, template_id=None, operation_list=None):
        r"""UpdateTaskV2RequestBody

        The model defined in huaweicloud sdk

        :param id: 部署任务id
        :type id: str
        :param deploy_system: 部署系统，deployTemplate：部署模板
        :type deploy_system: str
        :param template_id: 部署模板实例id
        :type template_id: str
        :param operation_list: 部署编排列表信息
        :type operation_list: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeployV2OperationsDO`]
        """
        
        

        self._id = None
        self._deploy_system = None
        self._template_id = None
        self._operation_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if deploy_system is not None:
            self.deploy_system = deploy_system
        if template_id is not None:
            self.template_id = template_id
        if operation_list is not None:
            self.operation_list = operation_list

    @property
    def id(self):
        r"""Gets the id of this UpdateTaskV2RequestBody.

        部署任务id

        :return: The id of this UpdateTaskV2RequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateTaskV2RequestBody.

        部署任务id

        :param id: The id of this UpdateTaskV2RequestBody.
        :type id: str
        """
        self._id = id

    @property
    def deploy_system(self):
        r"""Gets the deploy_system of this UpdateTaskV2RequestBody.

        部署系统，deployTemplate：部署模板

        :return: The deploy_system of this UpdateTaskV2RequestBody.
        :rtype: str
        """
        return self._deploy_system

    @deploy_system.setter
    def deploy_system(self, deploy_system):
        r"""Sets the deploy_system of this UpdateTaskV2RequestBody.

        部署系统，deployTemplate：部署模板

        :param deploy_system: The deploy_system of this UpdateTaskV2RequestBody.
        :type deploy_system: str
        """
        self._deploy_system = deploy_system

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateTaskV2RequestBody.

        部署模板实例id

        :return: The template_id of this UpdateTaskV2RequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateTaskV2RequestBody.

        部署模板实例id

        :param template_id: The template_id of this UpdateTaskV2RequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def operation_list(self):
        r"""Gets the operation_list of this UpdateTaskV2RequestBody.

        部署编排列表信息

        :return: The operation_list of this UpdateTaskV2RequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeployV2OperationsDO`]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this UpdateTaskV2RequestBody.

        部署编排列表信息

        :param operation_list: The operation_list of this UpdateTaskV2RequestBody.
        :type operation_list: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeployV2OperationsDO`]
        """
        self._operation_list = operation_list

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
        if not isinstance(other, UpdateTaskV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
