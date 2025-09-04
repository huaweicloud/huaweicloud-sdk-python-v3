# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthenticationTemplateSimple:

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
        'create_time': 'str',
        'update_time': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, template_id=None, template_name=None, create_time=None, update_time=None, description=None, status=None):
        r"""AuthenticationTemplateSimple

        The model defined in huaweicloud sdk

        :param template_id: 鉴权模板id
        :type template_id: str
        :param template_name: 鉴权模板名称
        :type template_name: str
        :param create_time: 鉴权模板创建的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type create_time: str
        :param update_time: 鉴权模板最后一次修改的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type update_time: str
        :param description: 鉴权模板的描述信息
        :type description: str
        :param status: **参数说明**：鉴权模板状态 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。
        :type status: str
        """
        
        

        self._template_id = None
        self._template_name = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._status = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def template_id(self):
        r"""Gets the template_id of this AuthenticationTemplateSimple.

        鉴权模板id

        :return: The template_id of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this AuthenticationTemplateSimple.

        鉴权模板id

        :param template_id: The template_id of this AuthenticationTemplateSimple.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this AuthenticationTemplateSimple.

        鉴权模板名称

        :return: The template_name of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this AuthenticationTemplateSimple.

        鉴权模板名称

        :param template_name: The template_name of this AuthenticationTemplateSimple.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def create_time(self):
        r"""Gets the create_time of this AuthenticationTemplateSimple.

        鉴权模板创建的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The create_time of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AuthenticationTemplateSimple.

        鉴权模板创建的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param create_time: The create_time of this AuthenticationTemplateSimple.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AuthenticationTemplateSimple.

        鉴权模板最后一次修改的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The update_time of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AuthenticationTemplateSimple.

        鉴权模板最后一次修改的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param update_time: The update_time of this AuthenticationTemplateSimple.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this AuthenticationTemplateSimple.

        鉴权模板的描述信息

        :return: The description of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AuthenticationTemplateSimple.

        鉴权模板的描述信息

        :param description: The description of this AuthenticationTemplateSimple.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this AuthenticationTemplateSimple.

        **参数说明**：鉴权模板状态 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。

        :return: The status of this AuthenticationTemplateSimple.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuthenticationTemplateSimple.

        **参数说明**：鉴权模板状态 - ACTIVE：该鉴权模板为激活状态。 - INACTIVE：该鉴权模板为停用状态。

        :param status: The status of this AuthenticationTemplateSimple.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AuthenticationTemplateSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
