# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateMetadataResponse(SdkResponse):

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
        'template_description': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_description': 'template_description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, template_id=None, template_name=None, template_description=None, create_time=None, update_time=None):
        r"""ShowTemplateMetadataResponse

        The model defined in huaweicloud sdk

        :param template_id: 模板的唯一ID，由模板服务随机生成
        :type template_id: str
        :param template_name: 模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type template_name: str
        :param template_description: 模板的描述。可用于客户识别自己的模板
        :type template_description: str
        :param create_time: 模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param update_time: 模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type update_time: str
        """
        
        super(ShowTemplateMetadataResponse, self).__init__()

        self._template_id = None
        self._template_name = None
        self._template_description = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        self.create_time = create_time
        self.update_time = update_time

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowTemplateMetadataResponse.

        模板的唯一ID，由模板服务随机生成

        :return: The template_id of this ShowTemplateMetadataResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowTemplateMetadataResponse.

        模板的唯一ID，由模板服务随机生成

        :param template_id: The template_id of this ShowTemplateMetadataResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowTemplateMetadataResponse.

        模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The template_name of this ShowTemplateMetadataResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowTemplateMetadataResponse.

        模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param template_name: The template_name of this ShowTemplateMetadataResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        r"""Gets the template_description of this ShowTemplateMetadataResponse.

        模板的描述。可用于客户识别自己的模板

        :return: The template_description of this ShowTemplateMetadataResponse.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        r"""Sets the template_description of this ShowTemplateMetadataResponse.

        模板的描述。可用于客户识别自己的模板

        :param template_description: The template_description of this ShowTemplateMetadataResponse.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowTemplateMetadataResponse.

        模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this ShowTemplateMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowTemplateMetadataResponse.

        模板的生成时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this ShowTemplateMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowTemplateMetadataResponse.

        模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The update_time of this ShowTemplateMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowTemplateMetadataResponse.

        模板的更新时间，格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param update_time: The update_time of this ShowTemplateMetadataResponse.
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
        if not isinstance(other, ShowTemplateMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
