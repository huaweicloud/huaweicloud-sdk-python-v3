# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLiveDataQuotaV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datasource': 'str',
        'api': 'str',
        'scripts': 'str',
        'datasource_used': 'str',
        'api_used': 'str'
    }

    attribute_map = {
        'datasource': 'datasource',
        'api': 'api',
        'scripts': 'scripts',
        'datasource_used': 'datasource_used',
        'api_used': 'api_used'
    }

    def __init__(self, datasource=None, api=None, scripts=None, datasource_used=None, api_used=None):
        """ListLiveDataQuotaV2Response

        The model defined in huaweicloud sdk

        :param datasource: 数据源配额
        :type datasource: str
        :param api: 后端api配额
        :type api: str
        :param scripts: 脚本配额
        :type scripts: str
        :param datasource_used: 已使用的数据源数量
        :type datasource_used: str
        :param api_used: 已使用的后端api数量
        :type api_used: str
        """
        
        super(ListLiveDataQuotaV2Response, self).__init__()

        self._datasource = None
        self._api = None
        self._scripts = None
        self._datasource_used = None
        self._api_used = None
        self.discriminator = None

        if datasource is not None:
            self.datasource = datasource
        if api is not None:
            self.api = api
        if scripts is not None:
            self.scripts = scripts
        if datasource_used is not None:
            self.datasource_used = datasource_used
        if api_used is not None:
            self.api_used = api_used

    @property
    def datasource(self):
        """Gets the datasource of this ListLiveDataQuotaV2Response.

        数据源配额

        :return: The datasource of this ListLiveDataQuotaV2Response.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this ListLiveDataQuotaV2Response.

        数据源配额

        :param datasource: The datasource of this ListLiveDataQuotaV2Response.
        :type datasource: str
        """
        self._datasource = datasource

    @property
    def api(self):
        """Gets the api of this ListLiveDataQuotaV2Response.

        后端api配额

        :return: The api of this ListLiveDataQuotaV2Response.
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this ListLiveDataQuotaV2Response.

        后端api配额

        :param api: The api of this ListLiveDataQuotaV2Response.
        :type api: str
        """
        self._api = api

    @property
    def scripts(self):
        """Gets the scripts of this ListLiveDataQuotaV2Response.

        脚本配额

        :return: The scripts of this ListLiveDataQuotaV2Response.
        :rtype: str
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this ListLiveDataQuotaV2Response.

        脚本配额

        :param scripts: The scripts of this ListLiveDataQuotaV2Response.
        :type scripts: str
        """
        self._scripts = scripts

    @property
    def datasource_used(self):
        """Gets the datasource_used of this ListLiveDataQuotaV2Response.

        已使用的数据源数量

        :return: The datasource_used of this ListLiveDataQuotaV2Response.
        :rtype: str
        """
        return self._datasource_used

    @datasource_used.setter
    def datasource_used(self, datasource_used):
        """Sets the datasource_used of this ListLiveDataQuotaV2Response.

        已使用的数据源数量

        :param datasource_used: The datasource_used of this ListLiveDataQuotaV2Response.
        :type datasource_used: str
        """
        self._datasource_used = datasource_used

    @property
    def api_used(self):
        """Gets the api_used of this ListLiveDataQuotaV2Response.

        已使用的后端api数量

        :return: The api_used of this ListLiveDataQuotaV2Response.
        :rtype: str
        """
        return self._api_used

    @api_used.setter
    def api_used(self, api_used):
        """Sets the api_used of this ListLiveDataQuotaV2Response.

        已使用的后端api数量

        :param api_used: The api_used of this ListLiveDataQuotaV2Response.
        :type api_used: str
        """
        self._api_used = api_used

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
        if not isinstance(other, ListLiveDataQuotaV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
