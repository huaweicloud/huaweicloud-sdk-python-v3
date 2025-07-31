# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyProjectConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_info_list': 'list[ProjectConfigInfo]',
        'cascade': 'bool'
    }

    attribute_map = {
        'config_info_list': 'config_info_list',
        'cascade': 'cascade'
    }

    def __init__(self, config_info_list=None, cascade=None):
        r"""ModifyProjectConfigRequestBody

        The model defined in huaweicloud sdk

        :param config_info_list: 配置信息列表
        :type config_info_list: list[:class:`huaweicloudsdkhss.v5.ProjectConfigInfo`]
        :param cascade: 是否级联修改。若配置为true且enterprise_project_id&#x3D;all_granted_eps时，对所有企业项目进行修改；配置为false且enterprise_project_id&#x3D;all_granted_eps时，仅对all_granted_eps修改；其他场景该字段不生效。
        :type cascade: bool
        """
        
        

        self._config_info_list = None
        self._cascade = None
        self.discriminator = None

        self.config_info_list = config_info_list
        if cascade is not None:
            self.cascade = cascade

    @property
    def config_info_list(self):
        r"""Gets the config_info_list of this ModifyProjectConfigRequestBody.

        配置信息列表

        :return: The config_info_list of this ModifyProjectConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProjectConfigInfo`]
        """
        return self._config_info_list

    @config_info_list.setter
    def config_info_list(self, config_info_list):
        r"""Sets the config_info_list of this ModifyProjectConfigRequestBody.

        配置信息列表

        :param config_info_list: The config_info_list of this ModifyProjectConfigRequestBody.
        :type config_info_list: list[:class:`huaweicloudsdkhss.v5.ProjectConfigInfo`]
        """
        self._config_info_list = config_info_list

    @property
    def cascade(self):
        r"""Gets the cascade of this ModifyProjectConfigRequestBody.

        是否级联修改。若配置为true且enterprise_project_id=all_granted_eps时，对所有企业项目进行修改；配置为false且enterprise_project_id=all_granted_eps时，仅对all_granted_eps修改；其他场景该字段不生效。

        :return: The cascade of this ModifyProjectConfigRequestBody.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        r"""Sets the cascade of this ModifyProjectConfigRequestBody.

        是否级联修改。若配置为true且enterprise_project_id=all_granted_eps时，对所有企业项目进行修改；配置为false且enterprise_project_id=all_granted_eps时，仅对all_granted_eps修改；其他场景该字段不生效。

        :param cascade: The cascade of this ModifyProjectConfigRequestBody.
        :type cascade: bool
        """
        self._cascade = cascade

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
        if not isinstance(other, ModifyProjectConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
