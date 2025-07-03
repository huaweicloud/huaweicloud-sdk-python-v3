# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_data': 'TemplateData',
        'version_number': 'int',
        'version_id': 'str',
        'version_description': 'str',
        'created_at': 'str',
        'launch_template_id': 'str'
    }

    attribute_map = {
        'template_data': 'template_data',
        'version_number': 'version_number',
        'version_id': 'version_id',
        'version_description': 'version_description',
        'created_at': 'created_at',
        'launch_template_id': 'launch_template_id'
    }

    def __init__(self, template_data=None, version_number=None, version_id=None, version_description=None, created_at=None, launch_template_id=None):
        r"""TemplateVersion

        The model defined in huaweicloud sdk

        :param template_data: 
        :type template_data: :class:`huaweicloudsdkecs.v2.TemplateData`
        :param version_number: 版本号
        :type version_number: int
        :param version_id: 版本id
        :type version_id: str
        :param version_description: 版本描述
        :type version_description: str
        :param created_at: 创建时间
        :type created_at: str
        :param launch_template_id: 模板id
        :type launch_template_id: str
        """
        
        

        self._template_data = None
        self._version_number = None
        self._version_id = None
        self._version_description = None
        self._created_at = None
        self._launch_template_id = None
        self.discriminator = None

        if template_data is not None:
            self.template_data = template_data
        if version_number is not None:
            self.version_number = version_number
        if version_id is not None:
            self.version_id = version_id
        if version_description is not None:
            self.version_description = version_description
        if created_at is not None:
            self.created_at = created_at
        if launch_template_id is not None:
            self.launch_template_id = launch_template_id

    @property
    def template_data(self):
        r"""Gets the template_data of this TemplateVersion.

        :return: The template_data of this TemplateVersion.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateData`
        """
        return self._template_data

    @template_data.setter
    def template_data(self, template_data):
        r"""Sets the template_data of this TemplateVersion.

        :param template_data: The template_data of this TemplateVersion.
        :type template_data: :class:`huaweicloudsdkecs.v2.TemplateData`
        """
        self._template_data = template_data

    @property
    def version_number(self):
        r"""Gets the version_number of this TemplateVersion.

        版本号

        :return: The version_number of this TemplateVersion.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        r"""Sets the version_number of this TemplateVersion.

        版本号

        :param version_number: The version_number of this TemplateVersion.
        :type version_number: int
        """
        self._version_number = version_number

    @property
    def version_id(self):
        r"""Gets the version_id of this TemplateVersion.

        版本id

        :return: The version_id of this TemplateVersion.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this TemplateVersion.

        版本id

        :param version_id: The version_id of this TemplateVersion.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_description(self):
        r"""Gets the version_description of this TemplateVersion.

        版本描述

        :return: The version_description of this TemplateVersion.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this TemplateVersion.

        版本描述

        :param version_description: The version_description of this TemplateVersion.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def created_at(self):
        r"""Gets the created_at of this TemplateVersion.

        创建时间

        :return: The created_at of this TemplateVersion.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this TemplateVersion.

        创建时间

        :param created_at: The created_at of this TemplateVersion.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def launch_template_id(self):
        r"""Gets the launch_template_id of this TemplateVersion.

        模板id

        :return: The launch_template_id of this TemplateVersion.
        :rtype: str
        """
        return self._launch_template_id

    @launch_template_id.setter
    def launch_template_id(self, launch_template_id):
        r"""Sets the launch_template_id of this TemplateVersion.

        模板id

        :param launch_template_id: The launch_template_id of this TemplateVersion.
        :type launch_template_id: str
        """
        self._launch_template_id = launch_template_id

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
        if not isinstance(other, TemplateVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
