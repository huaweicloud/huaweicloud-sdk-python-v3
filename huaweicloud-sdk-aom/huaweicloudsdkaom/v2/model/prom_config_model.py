# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PromConfigModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remote_write_url': 'str',
        'remote_read_url': 'str',
        'prom_http_api_endpoint': 'str',
        'dashboard_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'remote_write_url': 'remote_write_url',
        'remote_read_url': 'remote_read_url',
        'prom_http_api_endpoint': 'prom_http_api_endpoint',
        'dashboard_id': 'dashboard_id',
        'region_id': 'region_id'
    }

    def __init__(self, remote_write_url=None, remote_read_url=None, prom_http_api_endpoint=None, dashboard_id=None, region_id=None):
        r"""PromConfigModel

        The model defined in huaweicloud sdk

        :param remote_write_url: Prometheus实例remote-write地址。
        :type remote_write_url: str
        :param remote_read_url: Prometheus实例remote-read地址。
        :type remote_read_url: str
        :param prom_http_api_endpoint: Prometheus实例调用url。
        :type prom_http_api_endpoint: str
        :param dashboard_id: Prometheus实例关联dashboard的dashboard id（目前未使用）。
        :type dashboard_id: str
        :param region_id: Prometheus实例所属的region。
        :type region_id: str
        """
        
        

        self._remote_write_url = None
        self._remote_read_url = None
        self._prom_http_api_endpoint = None
        self._dashboard_id = None
        self._region_id = None
        self.discriminator = None

        if remote_write_url is not None:
            self.remote_write_url = remote_write_url
        if remote_read_url is not None:
            self.remote_read_url = remote_read_url
        if prom_http_api_endpoint is not None:
            self.prom_http_api_endpoint = prom_http_api_endpoint
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def remote_write_url(self):
        r"""Gets the remote_write_url of this PromConfigModel.

        Prometheus实例remote-write地址。

        :return: The remote_write_url of this PromConfigModel.
        :rtype: str
        """
        return self._remote_write_url

    @remote_write_url.setter
    def remote_write_url(self, remote_write_url):
        r"""Sets the remote_write_url of this PromConfigModel.

        Prometheus实例remote-write地址。

        :param remote_write_url: The remote_write_url of this PromConfigModel.
        :type remote_write_url: str
        """
        self._remote_write_url = remote_write_url

    @property
    def remote_read_url(self):
        r"""Gets the remote_read_url of this PromConfigModel.

        Prometheus实例remote-read地址。

        :return: The remote_read_url of this PromConfigModel.
        :rtype: str
        """
        return self._remote_read_url

    @remote_read_url.setter
    def remote_read_url(self, remote_read_url):
        r"""Sets the remote_read_url of this PromConfigModel.

        Prometheus实例remote-read地址。

        :param remote_read_url: The remote_read_url of this PromConfigModel.
        :type remote_read_url: str
        """
        self._remote_read_url = remote_read_url

    @property
    def prom_http_api_endpoint(self):
        r"""Gets the prom_http_api_endpoint of this PromConfigModel.

        Prometheus实例调用url。

        :return: The prom_http_api_endpoint of this PromConfigModel.
        :rtype: str
        """
        return self._prom_http_api_endpoint

    @prom_http_api_endpoint.setter
    def prom_http_api_endpoint(self, prom_http_api_endpoint):
        r"""Sets the prom_http_api_endpoint of this PromConfigModel.

        Prometheus实例调用url。

        :param prom_http_api_endpoint: The prom_http_api_endpoint of this PromConfigModel.
        :type prom_http_api_endpoint: str
        """
        self._prom_http_api_endpoint = prom_http_api_endpoint

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this PromConfigModel.

        Prometheus实例关联dashboard的dashboard id（目前未使用）。

        :return: The dashboard_id of this PromConfigModel.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this PromConfigModel.

        Prometheus实例关联dashboard的dashboard id（目前未使用）。

        :param dashboard_id: The dashboard_id of this PromConfigModel.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def region_id(self):
        r"""Gets the region_id of this PromConfigModel.

        Prometheus实例所属的region。

        :return: The region_id of this PromConfigModel.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this PromConfigModel.

        Prometheus实例所属的region。

        :param region_id: The region_id of this PromConfigModel.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, PromConfigModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
