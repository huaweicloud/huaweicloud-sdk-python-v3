# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'import_templates': 'list[TemplateSrcReq]'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'import_templates': 'import_templates'
    }

    def __init__(self, source_project_id=None, import_templates=None):
        r"""ImportTemplateReq

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param import_templates: 导入模板列表
        :type import_templates: list[:class:`huaweicloudsdkeihealth.v1.TemplateSrcReq`]
        """
        
        

        self._source_project_id = None
        self._import_templates = None
        self.discriminator = None

        self.source_project_id = source_project_id
        self.import_templates = import_templates

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this ImportTemplateReq.

        源项目id

        :return: The source_project_id of this ImportTemplateReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this ImportTemplateReq.

        源项目id

        :param source_project_id: The source_project_id of this ImportTemplateReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def import_templates(self):
        r"""Gets the import_templates of this ImportTemplateReq.

        导入模板列表

        :return: The import_templates of this ImportTemplateReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TemplateSrcReq`]
        """
        return self._import_templates

    @import_templates.setter
    def import_templates(self, import_templates):
        r"""Sets the import_templates of this ImportTemplateReq.

        导入模板列表

        :param import_templates: The import_templates of this ImportTemplateReq.
        :type import_templates: list[:class:`huaweicloudsdkeihealth.v1.TemplateSrcReq`]
        """
        self._import_templates = import_templates

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
        if not isinstance(other, ImportTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
