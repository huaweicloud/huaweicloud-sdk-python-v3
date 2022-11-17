# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'Template',
        'template_desc': 'str',
        'source_type': 'str',
        'source_repo_url': 'str',
        'runtime': 'RuntimeType'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_desc': 'template_desc',
        'source_type': 'source_type',
        'source_repo_url': 'source_repo_url',
        'runtime': 'runtime'
    }

    def __init__(self, template_name=None, template_desc=None, source_type=None, source_repo_url=None, runtime=None):
        """TemplateView

        The model defined in huaweicloud sdk

        :param template_name: 
        :type template_name: :class:`huaweicloudsdkservicestage.v2.Template`
        :param template_desc: 模板描述。
        :type template_desc: str
        :param source_type: 模板类别。
        :type source_type: str
        :param source_repo_url: 源码仓库URL
        :type source_repo_url: str
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        
        

        self._template_name = None
        self._template_desc = None
        self._source_type = None
        self._source_repo_url = None
        self._runtime = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if template_desc is not None:
            self.template_desc = template_desc
        if source_type is not None:
            self.source_type = source_type
        if source_repo_url is not None:
            self.source_repo_url = source_repo_url
        if runtime is not None:
            self.runtime = runtime

    @property
    def template_name(self):
        """Gets the template_name of this TemplateView.

        :return: The template_name of this TemplateView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.Template`
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateView.

        :param template_name: The template_name of this TemplateView.
        :type template_name: :class:`huaweicloudsdkservicestage.v2.Template`
        """
        self._template_name = template_name

    @property
    def template_desc(self):
        """Gets the template_desc of this TemplateView.

        模板描述。

        :return: The template_desc of this TemplateView.
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        """Sets the template_desc of this TemplateView.

        模板描述。

        :param template_desc: The template_desc of this TemplateView.
        :type template_desc: str
        """
        self._template_desc = template_desc

    @property
    def source_type(self):
        """Gets the source_type of this TemplateView.

        模板类别。

        :return: The source_type of this TemplateView.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this TemplateView.

        模板类别。

        :param source_type: The source_type of this TemplateView.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_repo_url(self):
        """Gets the source_repo_url of this TemplateView.

        源码仓库URL

        :return: The source_repo_url of this TemplateView.
        :rtype: str
        """
        return self._source_repo_url

    @source_repo_url.setter
    def source_repo_url(self, source_repo_url):
        """Sets the source_repo_url of this TemplateView.

        源码仓库URL

        :param source_repo_url: The source_repo_url of this TemplateView.
        :type source_repo_url: str
        """
        self._source_repo_url = source_repo_url

    @property
    def runtime(self):
        """Gets the runtime of this TemplateView.

        :return: The runtime of this TemplateView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this TemplateView.

        :param runtime: The runtime of this TemplateView.
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        self._runtime = runtime

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
        if not isinstance(other, TemplateView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
