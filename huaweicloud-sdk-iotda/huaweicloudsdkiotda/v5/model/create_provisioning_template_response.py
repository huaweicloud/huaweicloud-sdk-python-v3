# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProvisioningTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'description': 'str',
        'template_body': 'ProvisioningTemplateBody',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'description': 'description',
        'template_body': 'template_body',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, template_id=None, template_name=None, description=None, template_body=None, create_time=None, update_time=None):
        r"""CreateProvisioningTemplateResponse

        The model defined in huaweicloud sdk

        :param template_id: **参数说明**：预调配模板ID。
        :type template_id: str
        :param template_name: **参数说明**：预调配模板名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。
        :type template_name: str
        :param description: **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param template_body: 
        :type template_body: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        :param create_time: 在物联网平台创建预调配模板的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        :param update_time: 在物联网平台更新预调配模板的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type update_time: str
        """
        
        super(CreateProvisioningTemplateResponse, self).__init__()

        self._template_id = None
        self._template_name = None
        self._description = None
        self._template_body = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if description is not None:
            self.description = description
        if template_body is not None:
            self.template_body = template_body
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板ID。

        :return: The template_id of this CreateProvisioningTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板ID。

        :param template_id: The template_id of this CreateProvisioningTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :return: The template_name of this CreateProvisioningTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板名称。 **取值范围**：长度不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :param template_name: The template_name of this CreateProvisioningTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        r"""Gets the description of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this CreateProvisioningTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProvisioningTemplateResponse.

        **参数说明**：预调配模板的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this CreateProvisioningTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def template_body(self):
        r"""Gets the template_body of this CreateProvisioningTemplateResponse.

        :return: The template_body of this CreateProvisioningTemplateResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this CreateProvisioningTemplateResponse.

        :param template_body: The template_body of this CreateProvisioningTemplateResponse.
        :type template_body: :class:`huaweicloudsdkiotda.v5.ProvisioningTemplateBody`
        """
        self._template_body = template_body

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateProvisioningTemplateResponse.

        在物联网平台创建预调配模板的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this CreateProvisioningTemplateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateProvisioningTemplateResponse.

        在物联网平台创建预调配模板的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this CreateProvisioningTemplateResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateProvisioningTemplateResponse.

        在物联网平台更新预调配模板的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The update_time of this CreateProvisioningTemplateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateProvisioningTemplateResponse.

        在物联网平台更新预调配模板的时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param update_time: The update_time of this CreateProvisioningTemplateResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, CreateProvisioningTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
