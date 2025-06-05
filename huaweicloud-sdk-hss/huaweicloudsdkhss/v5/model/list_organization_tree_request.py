# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'region': 'str',
        'is_refresh': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'region': 'region',
        'is_refresh': 'is_refresh',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, x_security_token=None, region=None, is_refresh=None, enterprise_project_id=None):
        r"""ListOrganizationTreeRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param region: Region ID
        :type region: str
        :param is_refresh: 是否强制从organization同步组织信息
        :type is_refresh: bool
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        """
        
        

        self._x_security_token = None
        self._region = None
        self._is_refresh = None
        self._enterprise_project_id = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if region is not None:
            self.region = region
        if is_refresh is not None:
            self.is_refresh = is_refresh
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListOrganizationTreeRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListOrganizationTreeRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListOrganizationTreeRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def region(self):
        r"""Gets the region of this ListOrganizationTreeRequest.

        Region ID

        :return: The region of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListOrganizationTreeRequest.

        Region ID

        :param region: The region of this ListOrganizationTreeRequest.
        :type region: str
        """
        self._region = region

    @property
    def is_refresh(self):
        r"""Gets the is_refresh of this ListOrganizationTreeRequest.

        是否强制从organization同步组织信息

        :return: The is_refresh of this ListOrganizationTreeRequest.
        :rtype: bool
        """
        return self._is_refresh

    @is_refresh.setter
    def is_refresh(self, is_refresh):
        r"""Sets the is_refresh of this ListOrganizationTreeRequest.

        是否强制从organization同步组织信息

        :param is_refresh: The is_refresh of this ListOrganizationTreeRequest.
        :type is_refresh: bool
        """
        self._is_refresh = is_refresh

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListOrganizationTreeRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListOrganizationTreeRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListOrganizationTreeRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListOrganizationTreeRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListOrganizationTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
