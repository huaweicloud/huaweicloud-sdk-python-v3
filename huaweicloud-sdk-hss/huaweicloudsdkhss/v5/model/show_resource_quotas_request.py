# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'version': 'str',
        'charging_mode': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'version': 'version',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, region=None, enterprise_project_id=None, version=None, charging_mode=None):
        r"""ShowResourceQuotasRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param version: 主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。
        :type version: str
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._version = None
        self._charging_mode = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if version is not None:
            self.version = version
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def region(self):
        r"""Gets the region of this ShowResourceQuotasRequest.

        Region ID

        :return: The region of this ShowResourceQuotasRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowResourceQuotasRequest.

        Region ID

        :param region: The region of this ShowResourceQuotasRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowResourceQuotasRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ShowResourceQuotasRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowResourceQuotasRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ShowResourceQuotasRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ShowResourceQuotasRequest.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :return: The version of this ShowResourceQuotasRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowResourceQuotasRequest.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :param version: The version of this ShowResourceQuotasRequest.
        :type version: str
        """
        self._version = version

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ShowResourceQuotasRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this ShowResourceQuotasRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ShowResourceQuotasRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this ShowResourceQuotasRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, ShowResourceQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
