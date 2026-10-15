# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceHealthReportConfigResponse(SdkResponse):

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
        'template_id': 'int',
        'template_name': 'str',
        'system': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'system': 'system'
    }

    def __init__(self, instance_id=None, template_id=None, template_name=None, system=None):
        r"""ShowInstanceHealthReportConfigResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param template_id: 关联的模板ID，未配置时为null。
        :type template_id: int
        :param template_name: 关联的模板名称，未配置时为null。
        :type template_name: str
        :param system: 关联的模板是否为系统预设模板，未配置时为null。
        :type system: bool
        """
        
        super().__init__()

        self._instance_id = None
        self._template_id = None
        self._template_name = None
        self._system = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if system is not None:
            self.system = system

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceHealthReportConfigResponse.

        实例ID。

        :return: The instance_id of this ShowInstanceHealthReportConfigResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceHealthReportConfigResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceHealthReportConfigResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowInstanceHealthReportConfigResponse.

        关联的模板ID，未配置时为null。

        :return: The template_id of this ShowInstanceHealthReportConfigResponse.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowInstanceHealthReportConfigResponse.

        关联的模板ID，未配置时为null。

        :param template_id: The template_id of this ShowInstanceHealthReportConfigResponse.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowInstanceHealthReportConfigResponse.

        关联的模板名称，未配置时为null。

        :return: The template_name of this ShowInstanceHealthReportConfigResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowInstanceHealthReportConfigResponse.

        关联的模板名称，未配置时为null。

        :param template_name: The template_name of this ShowInstanceHealthReportConfigResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def system(self):
        r"""Gets the system of this ShowInstanceHealthReportConfigResponse.

        关联的模板是否为系统预设模板，未配置时为null。

        :return: The system of this ShowInstanceHealthReportConfigResponse.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this ShowInstanceHealthReportConfigResponse.

        关联的模板是否为系统预设模板，未配置时为null。

        :param system: The system of this ShowInstanceHealthReportConfigResponse.
        :type system: bool
        """
        self._system = system

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceHealthReportConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowInstanceHealthReportConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
