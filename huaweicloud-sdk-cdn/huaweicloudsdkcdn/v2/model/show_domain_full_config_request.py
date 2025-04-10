# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainFullConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'show_special_configs': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'show_special_configs': 'show_special_configs'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, show_special_configs=None):
        r"""ShowDomainFullConfigRequest

        The model defined in huaweicloud sdk

        :param domain_name: 加速域名。
        :type domain_name: str
        :param enterprise_project_id: 企业项目ID， all：所有项目。
        :type enterprise_project_id: str
        :param show_special_configs: 取值为auth_key，用来查询鉴权KEY和鉴权备KEY的值。
        :type show_special_configs: str
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._show_special_configs = None
        self.discriminator = None

        self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if show_special_configs is not None:
            self.show_special_configs = show_special_configs

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainFullConfigRequest.

        加速域名。

        :return: The domain_name of this ShowDomainFullConfigRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainFullConfigRequest.

        加速域名。

        :param domain_name: The domain_name of this ShowDomainFullConfigRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainFullConfigRequest.

        企业项目ID， all：所有项目。

        :return: The enterprise_project_id of this ShowDomainFullConfigRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainFullConfigRequest.

        企业项目ID， all：所有项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainFullConfigRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def show_special_configs(self):
        r"""Gets the show_special_configs of this ShowDomainFullConfigRequest.

        取值为auth_key，用来查询鉴权KEY和鉴权备KEY的值。

        :return: The show_special_configs of this ShowDomainFullConfigRequest.
        :rtype: str
        """
        return self._show_special_configs

    @show_special_configs.setter
    def show_special_configs(self, show_special_configs):
        r"""Sets the show_special_configs of this ShowDomainFullConfigRequest.

        取值为auth_key，用来查询鉴权KEY和鉴权备KEY的值。

        :param show_special_configs: The show_special_configs of this ShowDomainFullConfigRequest.
        :type show_special_configs: str
        """
        self._show_special_configs = show_special_configs

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
        if not isinstance(other, ShowDomainFullConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
